import sys
import logging
import os
from database_executor import DatabaseExecutor

# Ensure the log directory exists
log_dir = os.path.dirname('/path/to/jenkins/workspace/sql_execution.log')
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    handlers=[
        logging.FileHandler('/path/to/jenkins/workspace/sql_execution.log'),  # Adjust path if needed
        logging.StreamHandler(sys.stdout)
    ],
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def execute_sql_files(server, database, username, password, folder_path):
    db_executor = DatabaseExecutor(server, database, username, password)
    db_executor.execute_sql_from_folder(folder_path)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        logging.error("Usage: run.py <server> <database> <username> <password> <folder_path>")
        sys.exit(1)

    server = sys.argv[1]
    database = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]
    folder_path = sys.argv[5]

    logging.info(f"Starting SQL execution with server={server}, database={database}, folder_path={folder_path}")
    execute_sql_files(server, database, username, password, folder_path)
    logging.info("SQL execution completed.")
