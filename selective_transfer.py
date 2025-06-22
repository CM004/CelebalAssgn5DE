from sqlalchemy import create_engine
import pandas as pd

source = create_engine("mysql+mysqlconnector://root:@localhost/sakila")
target = create_engine("mysql+mysqlconnector://root:@localhost/sakila_backup")

table_columns = {
    "actor": ["actor_id", "first_name"],
    "customer": ["customer_id", "email"]
}

for table, cols in table_columns.items():
    col_str = ", ".join(cols)
    df = pd.read_sql(f"SELECT {col_str} FROM {table}", source)
    print(f"✅ Retrieved {len(df)} rows from '{table}'")
    df.to_sql(table, target, if_exists='replace', index=False)
    print(f"📥 Inserted into '{table}' in sakila_backup")

print("🎯 Selective transfer complete.")