import pyodbc
from datetime import date
# impo

class BackupHandler:

    def __init__(self, server, database, username, password):
        self.connection_string = (
            f"DRIVER={{SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
        )
        try:
            self.database = database
            self.connection = pyodbc.connect(self.connection_string)
            self.cursor = self.connection.cursor()
            # self.logger = FileLogger()

            self.logger.LogInfo("Database connection established successfully.")
        except pyodbc.Error as ex:
            self.logger.LogError(f"Failed to connect to the database: {ex}")
            raise

    def BackupDatabase(self):
        try:
            today = date.today()
            backup_query = f"SELECT * FROM {self.database} INTO {self.database+f"{date.isoformat(today)}"}"
            self.cursor.execute(backup_query)
            self.connection.commit()
        except pyodbc.Error as ex:
            self.logger.error(f"Failed to take backup: {ex}")
            # Optionally log the query that caused the error
            # self.logger.error(f"Failed query: {backup_query}")
            raise

    def RestoreBackup(self):
        try:
            today = date.today()
            backup_query = f"SELECT * FROM {self.database+f"{date.isoformat(today)}"} INTO {self.database}"
            self.cursor.execute(backup_query)
            self.connection.commit()
        except pyodbc.Error as ex:
            self.logger.error(f"Failed to Restore backup: {ex}")
            # Optionally log the query that caused the error
            # self.logger.error(f"Failed query: {backup_query}")
            raise



