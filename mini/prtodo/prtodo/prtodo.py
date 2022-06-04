"""The module provides the PR To-Do model-controller."""
# prtodo/prtodo.py

from typing import Dict, Any, NamedTuple

# communicate with CLI, we use two pieces of data holding the information:
# - todo: the dict holding the information for the current to-do
# - error: the return or error code confirming if the current operation was successful or not
# use a named tuple with appropriately named fields
class CurrentTodo(NamedTuple):
    todo: Dict[str, Any]
    error: int


from pathlib import Path
from prtodo.database import DatabaseHandler


class Todoer:
    def __init__(self, db_path: Path) -> None:
        self._db_handler = DatabaseHandler(db_path)
