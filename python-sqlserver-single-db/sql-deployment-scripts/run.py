import sys
import logging
import os
import argparse
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


parser = argparse.ArgumentParser()
parser.add_argument(
    "--server-name",
    type=str,
    required=True,
    default=False,
    help="Name of the server on which queries need to be run"
)
parser.add_argument(
    "--database-name",
    type=str,
    required=True,
    default=False,
    help="Name of the database on which queries need to be run"
)
parser.add_argument(
    "--username",
    type=str,
    required=True,
    default=False,
    help="Username for the connection with Server"
)
parser.add_argument(
    "--password",
    type=str,
    required=True,
    default=False,
    help="Password for the connection with server"
)
parser.add_argument(
    "--query-folder-path",
    type=str,
    required=True,
    default=False,
    help="Name of the table on which queries need to be run"
)


if __name__ == "__main__":

    args = parser.parse_args()
    
    print(args)
    server = args.server_name
    database = args.database_name
    username = args.username
    password = args.password
    folder_path = args.query_folder_path

    try:
        logging.info(f"Starting SQL execution with server={server}, database={database}, folder_path={folder_path}")
        execute_sql_files(server, database, username, password, folder_path)
        logging.info("SQL execution completed.")
    except Exception as ex:
        raise 
