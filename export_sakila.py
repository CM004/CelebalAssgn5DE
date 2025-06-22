import pandas as pd
from sqlalchemy import create_engine
from fastavro import writer, parse_schema
import os

# Connection to XAMPP's MySQL
user = "root"
password = ""  # XAMPP default is empty
host = "localhost"
database = "sakila"

# Create SQLAlchemy connection
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")

# Table to export
table_name = "actor"

# Create folders
os.makedirs("output/csv", exist_ok=True)
os.makedirs("output/parquet", exist_ok=True)
os.makedirs("output/avro", exist_ok=True)

# Read data
df = pd.read_sql(f"SELECT * FROM {table_name}", engine)

# Export to CSV
df.to_csv(f"output/csv/{table_name}.csv", index=False)

# Export to Parquet
df.to_parquet(f"output/parquet/{table_name}.parquet", engine='pyarrow')

# Export to Avro
records = df.to_dict(orient='records')
schema = {
    "type": "record",
    "name": table_name,
    "fields": [{"name": col, "type": "string"} for col in df.columns]
}
with open(f"output/avro/{table_name}.avro", "wb") as out:
    writer(out, parse_schema(schema), records)

print(f"✅ Exported '{table_name}' to CSV, Parquet, and Avro formats.")