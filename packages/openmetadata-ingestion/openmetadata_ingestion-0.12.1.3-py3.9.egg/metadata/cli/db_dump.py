from pathlib import Path
from typing import List

from sqlalchemy import inspect, text
from sqlalchemy.engine import Engine

TABLES_DUMP_ALL = {
    "task_sequence",
    "entity_usage",
    "entity_relationship",
    "entity_extension",
    "field_relationship",
    "tag_usage",
    "openmetadata_settings",
}

CUSTOM_TABLES = {"entity_extension_time_series": {"exclude_columns": ["timestamp"]}}
NOT_MIGRATE = {"DATABASE_CHANGE_LOG"}

STATEMENT_JSON = "SELECT json FROM {table}"
STATEMENT_ALL = "SELECT * FROM {table}"
STATEMENT_TRUNCATE = "TRUNCATE TABLE {table};\n"


def clean_col(column_raw: str) -> str:
    """
    Prepare the column to be inserted to MySQL
    """
    return (
        repr(str(column_raw)).replace('"', '\\"') if column_raw is not None else "null"
    )


def dump_json(tables: List[str], engine: Engine, output: Path) -> None:
    """
    Dumps JSON data
    """
    with open(output, "a") as file:
        for table in tables:

            truncate = STATEMENT_TRUNCATE.format(table=table)
            file.write(truncate)

            res = engine.execute(text(STATEMENT_JSON.format(table=table))).all()
            for row in res:
                insert = "INSERT INTO {table} (json) VALUES ({data});\n".format(
                    table=table, data=clean_col(row.json)
                )
                file.write(insert)


def dump_all(tables: List[str], engine: Engine, output: Path) -> None:
    """
    Dump tables that need to store all data
    """
    with open(output, "a") as file:
        for table in tables:

            truncate = STATEMENT_TRUNCATE.format(table=table)
            file.write(truncate)

            res = engine.execute(text(STATEMENT_ALL.format(table=table))).all()
            for row in res:
                insert = "INSERT INTO {table} VALUES ({data});\n".format(
                    table=table, data=",".join(clean_col(col) for col in row)
                )
                file.write(insert)


def dump_entity_custom(engine: Engine, output: Path, inspector) -> None:
    """
    This function is used to dump entities with custom handling
    """
    with open(output, "a") as file:
        for table, data in CUSTOM_TABLES.items():

            truncate = STATEMENT_TRUNCATE.format(table=table)
            file.write(truncate)

            columns = inspector.get_columns(table_name=table)

            STATEMENT_ALL_NEW = "SELECT {cols} FROM {table}".format(
                cols=",".join(
                    col["name"]
                    for col in columns
                    if col["name"] not in data["exclude_columns"]
                ),
                table=table,
            )
            res = engine.execute(text(STATEMENT_ALL_NEW)).all()
            for row in res:
                insert = "INSERT INTO {table} ({cols}) VALUES ({data});\n".format(
                    table=table,
                    data=",".join(clean_col(col) for col in row),
                    cols=",".join(
                        col["name"]
                        for col in columns
                        if col["name"] not in data["exclude_columns"]
                    ),
                )
                file.write(insert)


def dump(engine: Engine, output: Path, schema: str = None) -> None:
    """
    Get all tables from the database and dump
    only the JSON column for the required tables
    """
    inspector = inspect(engine)
    tables = (
        inspector.get_table_names(schema) if schema else inspector.get_table_names()
    )

    dump_json_tables = [
        table
        for table in tables
        if table not in TABLES_DUMP_ALL
        and table not in NOT_MIGRATE
        and table not in CUSTOM_TABLES.keys()
    ]

    dump_all(tables=list(TABLES_DUMP_ALL), engine=engine, output=output)
    dump_json(tables=dump_json_tables, engine=engine, output=output)
    dump_entity_custom(engine=engine, output=output, inspector=inspector)
