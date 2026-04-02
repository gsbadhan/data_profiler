from adapters.base_adapter import DatabaseAdapter
import sqlite3

class SQLiteAdapter(DatabaseAdapter):
        
    def __init__(self, db_path):
            self.conn = sqlite3.connect(db_path)

    def list_tables(self):
        cursor = self.conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table';"
        )
        return [row[0] for row in cursor.fetchall()]

    def get_schema(self, table):
        cursor = self.conn.execute(f"table_info({table})")
        return [
            {
                "name": row[1],
                "type": row[2],
                "nullable": not row[3]
            }
            for row in cursor.fetchall()
        ]

    def get_row_count(self, table):
        return self.conn.execute(
            f"SELECT COUNT(*) FROM {table}"
        ).fetchone()[0]

    def get_column_stats(self, table, column):
        query = f"""
        SELECT 
            MIN({column}),
            MAX({column}),
            COUNT(DISTINCT {column})
        FROM {table}
        """
        return self.conn.execute(query).fetchone()
    
    def get_null_count(self, table, column):
        return self.conn.execute(
            f"SELECT COUNT(*) FROM {table} WHERE {column} IS NULL"
        ).fetchone()[0]

    def get_histogram(self, table, column, bins):
        # simple histogram (top values)
        cursor = self.conn.execute(f"""
            SELECT {column}, COUNT(*) as cnt
            FROM {table}
            GROUP BY {column}
            ORDER BY cnt DESC
            LIMIT {bins}
        """)
        return [{"value": r[0], "count": r[1]} for r in cursor.fetchall()]