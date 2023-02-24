from project_1508.table.inside_table import InsideTable
from project_1508.table.outside_table import OutsideTable


class TableFactory:

    def create_table(self, table_type: str, table_number: int, capacity: int):
        if table_type == "InsideTable":
            return InsideTable(table_number, capacity)
        if table_type == "OutsideTable":
            return OutsideTable(table_number, capacity)