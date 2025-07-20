# 📦 Data Integration & Pipeline Automation
 

---

## 📘 Overview
This project demonstrates how to automate data integration and pipeline tasks using Python and MySQL. You will learn how to:
- Export data from a MySQL database (`sakila`) to CSV, Parquet, and Avro formats
- Copy all tables from one database to another (`sakila_backup`)
- Selectively transfer specific tables and columns
- Automate the entire pipeline using a Python scheduler

---

## 🛠️ Prerequisites
- Python 3.x
- MySQL (MariaDB via XAMPP or similar)
- pip (Python package manager)

### Required Python Libraries
- pandas
- sqlalchemy
- mysql-connector-python
- fastavro
- pyarrow
- schedule

Install all dependencies with:
```bash
pip3 install pandas sqlalchemy mysql-connector-python fastavro pyarrow schedule
```

---

## 🏗️ Project Structure
```text
Assgn5/
├── export_all_tables.py         # Exports all tables to CSV, Parquet, Avro
├── copy_to_another_db.py        # Copies all tables to sakila_backup
├── selective_transfer.py        # Transfers selected columns/tables
├── pipeline_scheduler.py        # Automates the pipeline
├── sakila-data-clean.sql        # Cleaned SQL dump (no stored procedures)
├── output/
│   ├── csv/
│   ├── parquet/
│   └── avro/
├── README.md
```

---

## 📂 Script Explanations

### 1. `export_all_tables.py`
- Connects to the `sakila` database using SQLAlchemy.
- Exports all tables to three formats:
  - CSV (easy to read, Excel compatible)
  - Parquet (columnar, efficient for analytics)
  - Avro (binary, schema-based, used in big data)
- Output files are saved in the `output/csv`, `output/parquet`, and `output/avro` folders.

### 2. `copy_to_another_db.py`
- Copies all tables and their data from `sakila` to a backup database called `sakila_backup`.
- Useful for database migration or backup.

### 3. `selective_transfer.py`
- Transfers only specific tables and columns (e.g., only `actor_id` and `first_name` from the `actor` table).
- Demonstrates how to filter and move only the data you need.

### 4. `pipeline_scheduler.py`
- Uses the `schedule` Python module to automate the above scripts.
- Runs the full pipeline every day at 5:15 PM (or as configured).

### 5. `sakila-data-clean.sql`
- Cleaned SQL dump of the Sakila database (no stored procedures, so it works with MariaDB).
- Use this to restore the sample data.

---

## 🧠 Key Concepts Explained

### SQL Dump and Restore
- `.sql` files store the entire database schema and data.
- To restore: `mysql -u root < sakila-data-clean.sql`
- If you get errors about `mysql.proc`, remove stored procedures from the SQL file.

### SQLAlchemy Connections
- Use `create_engine()` to connect Python to MySQL:
  ```python
  from sqlalchemy import create_engine
  engine = create_engine("mysql+mysqlconnector://root:@localhost/sakila")
  ```

### Data Export Formats
- **CSV:** Simple, readable, supported by most tools.
- **Parquet:** Efficient, columnar storage, great for analytics.
- **Avro:** Binary, schema-based, used in big data pipelines.

### Fastavro Error Fix
- Avro requires correct data types. Use Pandas to detect and convert types before writing.

### Selective Column Transfer
- Use SQL queries to select only the columns you need:
  ```sql
  SELECT actor_id, first_name FROM actor;
  ```

### Pipeline Automation
- Use the `schedule` module to run tasks at specific times:
  ```python
  import schedule
  schedule.every().day.at("17:15").do(run_pipeline)
  ```

---

## 🚀 How to Run the Project

1. **Restore the Sakila Database:**
   ```bash
   mysql -u root < sakila-data-clean.sql
   ```
2. **Run the Scheduler:**
   ```bash
   python3 pipeline_scheduler.py
   ```
   This will automatically run all steps (export, copy, selective transfer) at the scheduled time.

3. **Manual Run (Optional):**
   - You can run any script individually:
     ```bash
     python3 export_all_tables.py
     python3 copy_to_another_db.py
     python3 selective_transfer.py
     ```

---

## 🔍 How to Verify in MySQL

1. Open MySQL and use the backup database:
   ```sql
   USE sakila_backup;
   SELECT * FROM actor;
   DESCRIBE actor;
   SELECT COUNT(*) FROM actor;
   ```
2. You should see data like:
   | actor_id | first_name |
   |----------|------------|
   | 1        | Tom        |
   | 2        | Emma       |
   | 3        | Robert     |

3. Check the `output/` folders for exported files in CSV, Parquet, and Avro formats.

---

## 🛠️ Troubleshooting & Tips
- If `.sql` import gives `mysql.proc` error, remove stored procedures from the SQL file.
- Use `try/except` in Python scripts for error handling.
- Add print/log statements to track progress.
- Use the `schedule` module for time-based automation.
- If Avro export fails, check data types and convert as needed.

---

## 📚 References & Further Reading
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Fastavro Documentation](https://fastavro.readthedocs.io/)
- [PyArrow Documentation](https://arrow.apache.org/docs/python/)
- [Python schedule module](https://schedule.readthedocs.io/en/stable/)
- [Sakila Sample Database](https://dev.mysql.com/doc/sakila/en/)

---

## 🏁 Summary
You now have a complete, automated data pipeline using Python and MySQL. This project covers database export, backup, selective data transfer, and pipeline automation. All scripts and concepts are explained so you can revisit and understand everything, even after a long break.

---

## 🎤 Interview Q&A: What You Should Know About This Project

### 1. What is the main objective of this project?
- To automate the process of exporting, backing up, and selectively transferring data from a MySQL database using Python, and to schedule these tasks to run automatically.

### 2. Why did you use Python for this project?
- Python has strong libraries for data processing (pandas), database connectivity (SQLAlchemy), and file format conversion (fastavro, pyarrow). It is also easy to automate tasks in Python using modules like `schedule`.

### 3. Why did you choose SQLAlchemy for database connections?
- SQLAlchemy provides a high-level, flexible, and database-agnostic way to connect to and interact with SQL databases. It makes it easy to switch between different database backends and manage connections efficiently.

### 4. What are the differences between CSV, Parquet, and Avro formats?
- **CSV:** Simple, human-readable, widely supported, but not efficient for large or complex data.
- **Parquet:** Columnar, compressed, efficient for analytics and big data, not human-readable.
- **Avro:** Binary, schema-based, good for big data pipelines, supports data evolution, not human-readable.

### 5. How did you handle data type issues when exporting to Avro?
- Avro requires strict data types. I used pandas to inspect and convert data types before writing to Avro, ensuring compatibility and preventing errors.

### 6. How does the pipeline automation work?
- The `schedule` module is used to run the entire pipeline (export, backup, selective transfer) at a specific time every day. This ensures regular backups and data exports without manual intervention.

### 7. What challenges did you face and how did you solve them?
- **Stored procedures in SQL dump:** MariaDB had issues with MySQL stored procedures, so I cleaned the SQL file to remove them.
- **Avro data type errors:** Fixed by dynamically detecting and converting data types using pandas.
- **Automation reliability:** Used print/log statements and try/except blocks for error handling and debugging.

### 8. How would you extend this project?
- Add email notifications on job completion or failure.
- Integrate with cloud storage (e.g., AWS S3) for offsite backups.
- Add a web dashboard to monitor pipeline status.

### 9. What skills does this project demonstrate?
- Database management and SQL
- Data engineering and ETL (Extract, Transform, Load)
- Python scripting and automation
- Working with multiple data formats
- Debugging and error handling
- Scheduling and pipeline orchestration

### 10. What is the real-world relevance of this project?
- Automating data exports and backups is a common requirement in data engineering, analytics, and DevOps. This project shows you can build robust, automated data pipelines using open-source tools.

---

**Tip:** Before your interview, review this section and try to explain each answer in your own words. Be ready to discuss the reasoning behind your choices and any challenges you overcame!
