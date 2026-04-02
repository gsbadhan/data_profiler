## Project setup
uv init data-profiler (optional)
uv venv
source .venv/bin/activate
uv sync

## Testing data setup
python sqlite_db.py


## Run application
python main.py


## Output json format
`{
  "table_name": "users",
  "row_count": 1000,
  "columns": [
    {
      "name": "age",
      "type": "INTEGER",
      "nullable": true,
      "stats": {
        "min": 18,
        "max": 80,
        "distinct_count": 45,
        "null_count": 10
      }
    }
  ]
}`
