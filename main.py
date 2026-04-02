from adapter.sqlite_adapter import SQLiteAdapter
from profiler.table_profiler import TableProfiler
from persistence.writer import JSONWriter
from config import CONFIG


def startup_message():
    print("welcome to data-profiler app !!")


def run_sqlite():
    adapter = SQLiteAdapter("test.db")
    profiler = TableProfiler(adapter, CONFIG)
    results = profiler.run()
    JSONWriter().write(results, "sqlite_profile.json")


if __name__ == "__main__":
    startup_message()
    run_sqlite()

