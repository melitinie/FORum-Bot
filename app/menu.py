import logging
import os.path
from typing import TypedDict, get_type_hints

import pandas

log = logging.getLogger(__name__)


class MenuRow(TypedDict):
    id: int
    title: str
    parent_id: int


class MenuTree:
    def __init__(self, source_csv: str | None = None):
        if source_csv is None:
            source_csv = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "fora_menu.csv"
            )
        log.info("Loading menu from %s", source_csv)
        self._rows = self.load_rows_from_csv(source_csv)

    @property
    def rows(self) -> list[MenuRow]:
        return self._rows

    def get_menu(self, parent_id: int = 0) -> list[MenuRow]:
        return [row for row in self.rows if row["parent_id"] == parent_id]

    def find_row(self, id_: int) -> MenuRow | None:
        return next((row for row in self.rows if row["id"] == id_), None)

    @staticmethod
    def load_rows_from_csv(csv_path: str) -> list[MenuRow]:
        type_hints = get_type_hints(MenuRow)
        menu_row_dtype = {k: v for k, v in type_hints.items()}
        return pandas.read_csv(csv_path, dtype=menu_row_dtype).to_dict("records")
