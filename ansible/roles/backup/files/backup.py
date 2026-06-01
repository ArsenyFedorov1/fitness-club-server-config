#!/usr/bin/env python3
import subprocess
import datetime
import os

BACKUP_DIR = "/var/backups/fitness"
DB_NAME = "fitness_db"

def backup_database():
    date_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{BACKUP_DIR}/{DB_NAME}_{date_str}.sql.gz"
    
    cmd = f"sudo -u postgres pg_dump {DB_NAME} | gzip > {filename}"
    subprocess.run(cmd, shell=True, check=True)
    
    # Удаляем бэкапы старше 7 дней
    for f in os.listdir(BACKUP_DIR):
        if f.endswith(".sql.gz"):
            file_path = os.path.join(BACKUP_DIR, f)
            if os.path.getmtime(file_path) < datetime.datetime.now().timestamp() - 7*86400:
                os.remove(file_path)

if __name__ == "__main__":
    backup_database()
