"""This module provides the PR To-Do database functionality."""
# prtodo/database.py

import configparser
from io import DEFAULT_BUFFER_SIZE
from pathlib import Path

from prtodo import DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.cwd().joinpath("." + Path.home().stem + "_prtodo.json")

from typing import Dict, List, NamedTuple, Any

# communicatw with Database, we need data container to send/retrieve data from the to-do database
# DBResponse
# todo_list field is a list of dict representing individual to-dos
# error field holds an integer return code
class DBResponse(NamedTuple):
    todo_list: List[Dict[str, Any]]
    error: int


import json
from prtodo import DB_READ_ERROR, DB_WRITE_ERROR, JSON_ERROR, SUCCESS

# DatabaseHandler read and write data to the to-do database
# using the json module
class DatabaseHandler:
    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path

    def read_todos(self) -> DBResponse:
        try:
            with self._db_path.open("r") as db:
                try:
                    return DBResponse(json.load(db), SUCCESS)
                except json.JSONDecodeError:  # catch wrong JSON format
                    return DBResponse([], JSON_ERROR)
        except OSError:
            return DBResponse([], DB_READ_ERROR)

    def write_todos(self, todo_list: List[Dict[str, Any]]) -> DBResponse:
        try:
            with self._db_path.open("w") as db:
                json.dump(todo_list, db, indent=4)
            return DBResponse(todo_list, SUCCESS)
        except OSError:
            return DBResponse(todo_list, DB_WRITE_ERROR)


def get_database_path(config_file: Path) -> Path:
    """Return the current path to the to-do database."""
    config_parser = configparser.Configparser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])


def init_database(db_path: Path) -> int:
    """Create the to-do database."""
    try:
        db_path.write_text("[]")  # Empty to-do list
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR
