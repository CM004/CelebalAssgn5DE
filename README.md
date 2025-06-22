# 📦 Assignment 5: Data Integration & Pipeline Automation

## 👨‍💻 Project by: Chandramohan  
## 🗓️ Date: 22 June 2025  

---

## 📘 Objective

This project focuses on **data integration** and **pipeline automation** using Python and MySQL.  
The main tasks are:

- 📤 Exporting data from a MySQL database (`sakila`) to **CSV**, **Parquet**, and **Avro** formats
- 🔄 Copying **all tables** from one database to another (`sakila_backup`)
- 🎯 Selectively transferring **specific tables and columns**
- ⏰ Automating the pipeline using scheduled jobs (Python-based scheduler)

---

## 🏗️ Project Structure
Assgn5
├── export_all_tables.py
├── copy_to_another_db.py
├── selective_transfer.py
├── pipeline_scheduler.py
├── sakila-data-clean.sql     ← Cleaned data file without stored procedures
├── output
│   ├── csv
│   ├── parquet
│   └── avro
├── README.md   
---

## 🔧 Tools & Technologies Used

- Python 3
- MySQL (via XAMPP's MariaDB)
- SQLAlchemy (for DB connection)
- Pandas (for data processing)
- Fastavro (for Avro file format)
- PyArrow (for Parquet)
- `schedule` module (for automation)

---

## 🧠 Key Concepts (With Notes for Myself)

### 1. **SQL Dump and Restore**
- `.sql` files store the entire database schema and data.
- I used a **cleaned version** of `sakila-data.sql` because original had stored procedures that broke MariaDB.
- Restored using:
  ```bash
  mysql -u root < custom-sakila-data.sql
### 2. SQLAlchemy Connections
- Used `create_engine()` to connect Python to MySQL:
  create_engine("mysql+mysqlconnector://root:@localhost/sakila")

### 3. Data Export Formats
- CSV: Comma-separated values, readable and supported by Excel.
- Parquet: Columnar storage format, optimized for analytics.
- Avro: Binary format with schema — efficient and used in big data.

### 4. Fastavro Error Fix
- Avro failed when trying to write integers as strings (TypeError: must be string).
- I fixed it by dynamically detecting data types using Pandas.

### 5. Selective Column Transfer
- Only transferred necessary columns like:
  SELECT actor_id, first_name FROM actor

### 6. Pipeline Automation
- Used the `schedule` module to run the pipeline every day at 5:15 PM.
  schedule.every().day.at("17:15").do(run_pipeline)

---

## 🔄 Workflow Summary

1. Restored sample data using custom-sakila-data.sql
2. Ran export_all_tables.py → saved files in csv, parquet, avro
3. Ran copy_to_another_db.py → cloned all tables to sakila_backup
4. Ran selective_transfer.py → transferred only selected columns
5. pipeline_scheduler.py → ran all 3 above steps daily at 5:15 PM

---

## ✅ How to Run

Install libraries:

pip3 install pandas sqlalchemy mysql-connector-python fastavro pyarrow schedule

Run scheduler:

python3 pipeline_scheduler.py

---

## 🔍 How to Verify in MySQL

USE sakila_backup;
SELECT * FROM actor;
DESCRIBE actor;
SELECT COUNT(*) FROM actor;

Expected output:

actor_id | first_name  
1        | Tom  
2        | Emma  
3        | Robert  

---

## 🧾 Notes for Myself

- If `.sql` gives `mysql.proc` error, remove stored procedure part
- Use try/except in Python for error handling
- Use print logs to debug and track progress
- Use schedule for time-based automation

---

## 🏁 Done!

I successfully:
- Built a full data pipeline
- Learned how to connect Python to MySQL
- Exported and transformed data in multiple formats
- Automated the entire process
