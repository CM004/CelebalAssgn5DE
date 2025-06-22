import os
import pandas as pd
from sqlalchemy import create_engine
from fastavro import writer, parse_schema

# MySQL connection (XAMPP)
engine = create_engine("mysql+mysqlconnector://root:@localhost/sakila")

# Get all table names
tables = pd.read_sql("SHOW TABLES", engine).iloc[:, 0].tolist()

# Create output folders
formats = ['csv', 'parquet', 'avro']
for fmt in formats:
    os.makedirs(f"output/{fmt}", exist_ok=True)

# Export each table
for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", engine)
    
    # CSV
    df.to_csv(f"output/csv/{table}.csv", index=False)
    
    # Parquet
    df.to_parquet(f"output/parquet/{table}.parquet", engine='pyarrow')

    # Avro
    records = df.to_dict(orient='records')
    schema = {
        "type": "record",
        "name": table,
        "fields": [{"name": col, "type": "string"} for col in df.columns]
    }
    with open(f"output/avro/{table}.avro", "wb") as out:
        writer(out, parse_schema(schema), records)

print("✅ All tables exported to CSV, Parquet, and Avro.")