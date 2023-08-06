import click
import contextlib
import os
import pathlib
import tomlkit
import traceback
import typing

from headlight.migrator import MigrateHooks, Migration, MigrationError, Migrator, create_migration_template
from headlight.utils import colorize_sql

database_help = "Database connection URL."
migrations_help = "Migrations directory."
dry_run_help = "Simulate migration execution (nothing will be applied to the database)."
table_help = "History table name."
revert_steps_help = "The number of migrations to be reverted."
fake_help = "Write history table records without running any SQL command."
print_help = "Print generated SQL to stderr."
migration_name_help = "The name of the migration."
yes_help = "Automatically confirm action."

DATABASE_ENVVAR = "HL_DATABASE_URL"


class LoggingHooks(MigrateHooks):
    def before_migrate(self, migration: Migration) -> None:
        click.secho(
            "{status} {filename}".format(
                status=click.style("Migrating".ljust(10, " "), fg="yellow"),
                filename=os.path.basename(migration.file),
            ),
            nl=False,
        )

    def after_migrate(self, migration: Migration, time_taken: float) -> None:
        click.secho(
            "\r{status} {filename} {time}".format(
                status=click.style("Done".ljust(10, " "), fg="green"),
                time=click.style(f"({time_taken:.3f}s)", fg="cyan"),
                filename=os.path.basename(migration.file),
            )
        )

    def on_error(self, migration: Migration, exc: Exception, time_taken: float) -> None:
        click.secho(
            "\r{status} {filename} {time}".format(
                status=click.style("Fail".ljust(10, " "), fg="red"),
                time=click.style(f"({time_taken:.3f}s)", fg="cyan"),
                filename=os.path.basename(migration.file),
            )
        )


@contextlib.contextmanager
def catch_errors(verbose: bool) -> typing.Iterable[None]:
    try:
        yield
    except MigrationError as ex:
        if verbose:
            traceback.print_exception(ex)
        click.echo("")
        click.secho("-" * 30 + f" FAIL: {ex.migration.file} " + "-" * 30, fg="red")
        click.secho(f"Error: {ex}", fg="red")
        click.echo("Statement, that caused error:")
        click.echo(colorize_sql(ex.stmt))


def parse_db_info(database_url: str) -> tuple[str, str]:
    _, _, db_name = database_url.rpartition("/")
    db_type, _, _ = database_url.partition("://")
    return db_type, db_name


def get_config_from_pyproject() -> dict[str, str]:
    for dir in pathlib.Path(__file__).parents:
        pyproject = dir / "pyproject.toml"
        if pyproject.exists():
            config = tomlkit.loads(pyproject.read_text())
            return config.get("tool", {}).get("headlight", {})
    return {}


config = get_config_from_pyproject()
default_dir = config.get("directory", "migrations")
default_table = config.get("table", "migrations")
default_db = config.get("database_url")
if default_db is not None and default_db.startswith("$"):
    default_db = os.environ.get(default_db[1:].strip())


@click.group()
def app() -> None:
    pass


@app.command()
@click.option("-d", "--database", help=database_help, envvar=DATABASE_ENVVAR, required=True, default=default_db)
@click.option(
    "-m",
    "--migrations",
    default=default_dir,
    type=click.Path(file_okay=False, dir_okay=True, resolve_path=True),
    show_default=True,
    required=True,
    help=migrations_help,
)
@click.option("--table", default=default_table, show_default=True, help=table_help, required=True)
@click.option("--dry-run", is_flag=True, default=False, show_default=True, help=dry_run_help)
@click.option("--fake", is_flag=True, default=False, help=fake_help)
@click.option("--print-sql", is_flag=True, default=False, help=print_help)
@click.option("--yes", "-y", is_flag=True, default=False, help=yes_help)
@click.option("--verbose", is_flag=True, default=False)
def upgrade(
    *,
    database: str,
    migrations: str,
    table: str,
    fake: bool,
    dry_run: bool,
    print_sql: bool,
    yes: bool,
    verbose: bool,
) -> None:
    db_type, db_name = parse_db_info(database)
    click.secho(
        "Upgrade {type} database {db}.".format(
            db=click.style(db_name, fg="cyan"),
            type=click.style(db_type, fg="green"),
        )
    )

    migrator = Migrator.new(database, migrations, table)
    pending_count = len(migrator.get_pending_migrations())
    if not pending_count:
        return click.echo("No pending migration(s).")

    click.secho("Will apply {count} pending migration(s).".format(count=click.style(str(pending_count), fg="cyan")))

    if not yes:
        click.confirm(
            "Database schema will be {action}. Continue?".format(action=click.style("upgraded", fg="yellow")),
            show_default=True,
            abort=True,
        )

    with catch_errors(verbose):
        migrator.upgrade(fake=fake, dry_run=dry_run, print_sql=print_sql, hooks=LoggingHooks())


@app.command()
@click.option("-d", "--database", help=database_help, envvar=DATABASE_ENVVAR, required=True, default=default_db)
@click.option(
    "-m",
    "--migrations",
    default=default_dir,
    type=click.Path(file_okay=False, dir_okay=True, resolve_path=True),
    show_default=True,
    required=True,
    help=migrations_help,
)
@click.option("--table", default=default_table, show_default=True, help=table_help, required=True)
@click.option("--dry-run", is_flag=True, default=False, show_default=True, help=dry_run_help)
@click.option("--fake", is_flag=True, default=False, help=fake_help)
@click.option("--steps", type=int, default=1, help=revert_steps_help, show_default=True)
@click.option("--print-sql", is_flag=True, default=False, help=print_help)
@click.option("--yes", "-y", is_flag=True, default=False, help=yes_help)
@click.option("--verbose", is_flag=True, default=False)
def downgrade(
    *,
    database: str,
    migrations: str,
    table: str,
    fake: bool,
    dry_run: bool,
    print_sql: bool,
    yes: bool,
    steps: int,
    verbose: bool,
) -> None:
    db_type, db_name = parse_db_info(database)
    click.secho(
        "Downgrade {type} database {db}.".format(
            db=click.style(db_name, fg="cyan"),
            type=click.style(db_type, fg="green"),
        )
    )

    if not yes:
        click.confirm(
            "Database schema will be {action} by {steps} step(s). Continue?".format(
                action=click.style("downgraded", fg="yellow"),
                steps=click.style(steps, fg="cyan"),
            ),
            show_default=True,
            abort=True,
        )

    with catch_errors(verbose):
        migrator = Migrator.new(database, migrations, table)
        migrator.downgrade(dry_run=dry_run, fake=fake, steps=steps, print_sql=print_sql, hooks=LoggingHooks())


@app.command()
@click.option("-d", "--database", help=database_help, envvar=DATABASE_ENVVAR, required=True, default=default_db)
@click.option(
    "-m",
    "--migrations",
    default=default_dir,
    type=click.Path(file_okay=False, dir_okay=True, resolve_path=True),
    show_default=True,
    required=True,
    help=migrations_help,
)
@click.option("--table", default=default_table, show_default=True, help=table_help, required=True)
@click.option("--yes", "-y", is_flag=True, default=False, help=yes_help)
@click.option("--verbose", is_flag=True, default=False)
def reset(
    *,
    database: str,
    migrations: str,
    table: str,
    yes: bool,
    verbose: bool,
) -> None:
    db_type, db_name = parse_db_info(database)
    click.secho(
        "Resetting {type} database {db}.".format(
            db=click.style(db_name, fg="cyan"),
            type=click.style(db_type, fg="green"),
        )
    )

    if not yes:
        click.confirm(
            "Database schema will be reset. All relations will be dropped. Continue?",
            show_default=True,
            abort=True,
        )

    with catch_errors(verbose):
        migrator = Migrator.new(database, migrations, table)
        migrator.reset(hooks=LoggingHooks())


@app.command
@click.option(
    "-m",
    "--migrations",
    default=default_dir,
    type=click.Path(file_okay=False, dir_okay=True),
    show_default=True,
    required=True,
    help=migrations_help,
)
@click.argument("name", default="unnamed")
def new(
    *,
    migrations: str,
    name: str,
) -> None:
    path = create_migration_template(migrations, name)
    filename = os.path.basename(path)
    click.secho("Created migration %s." % click.style(filename, bold=True))


@app.command
@click.option(
    "-m",
    "--migrations",
    default=default_dir,
    type=click.Path(file_okay=False, dir_okay=True, resolve_path=True),
    show_default=True,
    required=True,
    help=migrations_help,
)
@click.option("--table", default=default_table, show_default=True, help=table_help, required=True)
@click.option("-d", "--database", help=database_help, envvar=DATABASE_ENVVAR, required=True, default=default_db)
def status(
    *,
    database: str,
    migrations: str,
    table: str,
) -> None:
    assert database
    migrator = Migrator.new(database, migrations, table)
    history = migrator.status()
    has_entries = False

    for migration in history:
        has_entries = True
        click.secho(
            "{status} {filename}".format(
                status=(
                    click.style("Applied", fg="green") if migration.applied else click.style("Pending", fg="yellow")
                ),
                filename=os.path.basename(migration.filename),
            )
        )

    if not has_entries:
        click.secho("No migration entries in history.")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
