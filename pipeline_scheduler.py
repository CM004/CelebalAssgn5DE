import schedule
import time
import subprocess

def run_pipeline():
    print("🚀 Running pipeline...")
    subprocess.run(["python3", "export_all_tables.py"])
    subprocess.run(["python3", "copy_to_another_db.py"])
    subprocess.run(["python3", "selective_transfer.py"])
    print("✅ Pipeline completed.\n")

# ⏰ Run every day at 5:26 PM
schedule.every().day.at("17:26").do(run_pipeline)

print("⏳ Waiting for 5:26 PM to run the pipeline...")
while True:
    schedule.run_pending()
    time.sleep(60)  # check every minute