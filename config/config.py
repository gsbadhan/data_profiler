
sqlite_profiler = {
    "database": "test.db",
    "sample_ratio": 1.0,     # 0 < x <= 1; how much % data you scan from a table
    "workers": 1, # table scan parallelism
    "include_nulls": True,
    "include_histogram": True,
    "histogram_bins": 10,
    "output_filename":"sqlite_profile_testdb.json"
}