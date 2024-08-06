import pyodbc
import os
import re
import logging
import chardet

class DatabaseExecutor:
    def __init__(self, server, database, username, password):
        self.__connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        self.connection = pyodbc.connect(self.__connection_string)
        self.cursor = self.connection.cursor()
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def execute_sql_from_folder(self, folder_path):
        def extract_index(filename):
            match = re.match(r'(\d+)', filename)
            if match:
                return int(match.group(1))
            return float('inf')

        sql_files = [file for file in os.listdir(folder_path) if file.endswith('.sql')]
        sql_files.sort(key=extract_index)

        logging.info("Sorted SQL files:")
        for file in sql_files:
            logging.info(file)
        
        try:
            for sql_file in sql_files:
                file_path = os.path.join(folder_path, sql_file)
                    # Detect file encoding
                with open(file_path, 'rb') as file:
                    raw_data = file.read()
                    result = chardet.detect(raw_data)
                    encoding = result['encoding']
                
                with open(file_path, 'r', encoding=encoding) as file:
                    sql_query = file.read()
                    logging.info(f"Executing SQL file {file_path}")
                    self.execute(sql_query)
                    logging.info(f"Executed {file_path} successfully.")
                    
        except Exception as ex:
            logging.error(f"Failed to execute SQL file {file_path}")
            self.connection.rollback()
            logging.info("Transaction Rolled Back")
            raise Exception(ex)

        self.connection.commit()
        self.connection.close()
        logging.info("Database connection closed.")

    def execute(self, sql_query):
            # Split the SQL query into batches using 'GO' command
            batches = self.split_sql_batches(sql_query)
            for batch in batches:
                batch = batch.strip()
                if batch:
                    logging.info(f"Executing batch: {batch}")
                    self.cursor.execute(batch)
                    if batch.lower().startswith("select"):
                        columns = [column[0] for column in self.cursor.description]
                        logging.info(f"Statement executed successfully: {batch}")
                        logging.info(f"Columns: {columns}")
                        results = self.cursor.fetchall()
                        for row in results:
                            logging.info(row)
                    else:
                        
                        logging.info(f"Statement executed successfully: {batch}")
                        logging.info(f"Rows affected: {self.cursor.rowcount}")

                    while self.cursor.nextset():
                        if self.cursor.description:
                            columns = [column[0] for column in self.cursor.description]
                            logging.info(f"Columns: {columns}")
                            results = self.cursor.fetchall()
                            for row in results:
                                logging.info(row)

    def split_sql_batches(self, sql_query):
        """Split SQL query into batches by handling 'GO' statements."""
        batches = []
        current_batch = []

        for line in sql_query.splitlines():
            stripped_line = line.strip()
            if stripped_line.upper() == 'GO':
                if current_batch:
                    batches.append('\n'.join(current_batch))
                    current_batch = []
            else:
                current_batch.append(stripped_line)
        
        if current_batch:
            batches.append('\n'.join(current_batch))

        return batches
