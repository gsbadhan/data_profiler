from concurrent.futures import ThreadPoolExecutor
from profiler.column_profiler import ColumnProfiler


class TableProfiler:
    
    def __init__(self, adapter, config):
        self.adapter = adapter
        self.config = config
        self.column_profiler = ColumnProfiler(adapter, config)

    def profile_table(self, table):
        schema = self.adapter.get_schema(table)
        row_count = self.adapter.get_row_count(table)

        columns = [
            self.column_profiler.profile(table, col)
            for col in schema
        ]

        return {
            "table_name": table,
            "row_count": row_count,
            "columns": columns
        }

    def run(self):
        tables = self.adapter.list_tables()

        with ThreadPoolExecutor(max_workers=self.config["workers"]) as executor:
            results = list(executor.map(self.profile_table, tables))

        return results
