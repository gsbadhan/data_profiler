class ColumnProfiler:
    
    def __init__(self, adapter, config):
        self.adapter = adapter
        self.config = config

    def profile(self, table, column_meta):
        col = column_meta["name"]

        stats = self.adapter.get_column_stats(
            table,
            col,
            self.config["sample_ratio"]
        )

        result = {
            "name": col,
            "type": column_meta["type"],
            "nullable": column_meta["nullable"],
            "stats": {
                "min": stats[0],
                "max": stats[1],
                "distinct_count": stats[2]
            }
        }

        if self.config.get("include_nulls"):
            null_count = self.adapter.get_null_count(table, col)
            if null_count is not None:
                result["stats"]["null_count"] = null_count

        if self.config.get("include_histogram"):
            hist = self.adapter.get_histogram(
                table,
                col,
                self.config["histogram_bins"]
            )
            if hist:
                result["stats"]["histogram"] = hist

        return result