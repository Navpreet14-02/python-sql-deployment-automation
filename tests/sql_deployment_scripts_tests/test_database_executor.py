import unittest
from unittest.mock import MagicMock, patch
from src.sql_deployment_scripts.database_executor import DatabaseExecutor
import pyodbc

@patch("src.sql_deployment_scripts.database_executor.pyodbc")
class DatabaseExecutorTest(unittest.TestCase):

    def test_init_ValidConnectionParameters(self,mock_pyodbc):
        mock_pyodbc.connect=MagicMock()
        mock_pyodbc.connect.cursor = MagicMock()

        self.server = "test_server"
        self.database = "test_database"
        self.username = "test_username"
        self.password = "test_password"

        isException=False
        try:
            self.db_executor = DatabaseExecutor(self.server, self.database, self.username, self.password)
        except Exception as ex:
            isException=True

        self.assertFalse(isException)

        
    def test_init_InvalidConnectionParameters(self,mock_pyodbc):
        mock_pyodbc.connect=MagicMock()
        mock_pyodbc.connect.side_effect =Exception("Error occurred while connecting")

        self.server = "test_server"
        self.database = "test_database"
        self.username = "test_username"
        self.password = "test_password"

        self.assertRaises(Exception,DatabaseExecutor,self.server, self.database, self.username, self.password)


    def test_executeSqlFromFolder_EmptyFolder(self, mock_pyodbc):

        mock_pyodbc.connect.return_value = MagicMock()
        mock_db_connection = mock_pyodbc.connect.return_value
        mock_db_connection.cursor.return_value = MagicMock()
        
        self.server = "test_server"
        self.database = "test_database"
        self.username = "test_username"
        self.password = "test_password"

        self.db_executor = DatabaseExecutor(self.server, self.database, self.username, self.password)
        
        folder_path = r"tests\test_data\empty_folder"

        response = self.db_executor.execute_sql_from_folder(folder_path)


        self.assertIsNone(response)

    def test_executeSqlFromFolder_NonSQLFiles(self, mock_pyodbc):

        mock_pyodbc.connect.return_value = MagicMock()
        mock_db_connection = mock_pyodbc.connect.return_value
        mock_db_connection.cursor.return_value = MagicMock()
        
        self.server = "test_server"
        self.database = "test_database"
        self.username = "test_username"
        self.password = "test_password"

        self.db_executor = DatabaseExecutor(self.server, self.database, self.username, self.password)
        
        folder_path = r"tests\test_data\non_sql_files"

        response = self.db_executor.execute_sql_from_folder(folder_path)

        self.assertIsNone(response)

    def test_executeSqlFromFolder_WrongSQLFiles(self, mock_pyodbc):

        mock_pyodbc.connect.return_value = MagicMock()
        mock_db_connection = mock_pyodbc.connect.return_value
        mock_db_connection.cursor.return_value = MagicMock()
        
        self.server = "test_server"
        self.database = "test_database"
        self.username = "test_username"
        self.password = "test_password"

        self.db_executor = DatabaseExecutor(self.server, self.database, self.username, self.password)
        self.db_executor.execute = MagicMock()
        self.db_executor.execute.side_effect = Exception("Wrong SQL Syntax")
        
        folder_path = r"tests\test_data\wrong_sql_files"

        self.assertRaises(Exception,self.db_executor.execute_sql_from_folder,folder_path)



    def test_executeSqlFromFolder_WrongFolderPath(self,mock_pyodbc):
        mock_pyodbc.connect.return_value = MagicMock()
        mock_db_connection = mock_pyodbc.connect.return_value
        mock_db_connection.cursor.return_value = MagicMock()

        self.server = "test_server"
        self.database = "test_database"
        self.username = "test_username"
        self.password = "test_password"

        self.db_executor = DatabaseExecutor(self.server,self.database,self.username,self.password)

        folder_path="test_path"

        self.assertRaises(Exception,self.db_executor.execute_sql_from_folder,folder_path)


    def test_executeSqlFromFolder_ExecuteFunctionFails(self,mock_pyodbc):
        
        mock_pyodbc.connect.return_value = MagicMock()
        mock_db_connection = mock_pyodbc.connect.return_value
        mock_db_connection.cursor.return_value = MagicMock()
        

        self.server = "test_server"
        self.database = "test_database"
        self.username = "test_username"
        self.password = "test_password"

        self.db_executor = DatabaseExecutor(self.server,self.database,self.username,self.password)
        
        self.db_executor.execute = MagicMock()
        self.db_executor.execute.side_effect = Exception("Error while executing queries")

        folder_path=r"tests\test_data\test_files"

        self.assertRaises(Exception,self.db_executor.execute_sql_from_folder,folder_path)


    def test_SplitSQLBatches(self,mock_pyodbc):

        mock_pyodbc.connect.return_value = MagicMock()
        mock_db_connection = mock_pyodbc.connect.return_value
        mock_db_connection.cursor.return_value = MagicMock()

        self.server = "test_server"
        self.database = "test_database"
        self.username = "test_username"
        self.password = "test_password"

        self.db_executor = DatabaseExecutor(self.server,self.database,self.username,self.password)

        sample_query_path = r'tests\test_data\test_files\1_query.sql'
        with open(sample_query_path,'r') as file:
            sql_query=file.read()

        response = self.db_executor.split_sql_batches(sql_query)

        self.assertEqual(len(response),6)  
    

    @patch("src.sql_deployment_scripts.database_executor.DatabaseExecutor.split_sql_batches")
    def test_Execute_Sql_Select_Statements(self,mock_split_sql_batches,mock_pyodbc):


        mock_pyodbc.return_value = MagicMock()
        mock_split_sql_batches.return_value = ['use EndPointActivity', '\nBEGIN TRANSACTION', '\nALTER TABLE dbo.ActivitySources ADD LastActivityService datetime NULL', '\nSELECT * FROM dbo.ActivitySources', '\nALTER TABLE dbo.ActivitySources SET (LOCK_ESCALATION = TABLE)', '\nCOMMIT']
      
        self.server = "test_server"
        self.database = "test_database"
        self.username = "test_username"
        self.password = "test_password"

        self.db_executor = DatabaseExecutor(self.server,self.database,self.username,self.password)
        self.db_executor.cursor.execute = MagicMock()
        self.db_executor.cursor.fetchall = MagicMock()
        self.db_executor.cursor.fetchall.return_value = ["test"]
        self.db_executor.cursor.nextset = MagicMock()
        self.db_executor.cursor.nextset.return_value = False

        sample_query_path = r'tests\test_data\test_files\select_statements.sql'
        with open(sample_query_path,'r') as file:
            sql_query=file.read()

        response = self.db_executor.execute(sql_query)

        self.assertIsNone(response)

    @patch("src.sql_deployment_scripts.database_executor.DatabaseExecutor.split_sql_batches")
    def test_Execute_All_Statements(self,mock_split_sql_batches,mock_pyodbc):

        mock_pyodbc.return_value = MagicMock()
        mock_split_sql_batches.return_value = ['use EndPointActivity', '\nBEGIN TRANSACTION', '\nALTER TABLE dbo.ActivitySources ADD LastActivityService datetime NULL', '\nSELECT * FROM dbo.ActivitySources', '\nALTER TABLE dbo.ActivitySources SET (LOCK_ESCALATION = TABLE)', '\nCOMMIT']
      
        self.server = "test_server"
        self.database = "test_database"
        self.username = "test_username"
        self.password = "test_password"

        self.db_executor = DatabaseExecutor(self.server,self.database,self.username,self.password)
        self.db_executor.cursor.execute = MagicMock()
        self.db_executor.cursor.fetchall = MagicMock()
        self.db_executor.cursor.fetchall.return_value = ["test"]
        self.db_executor.cursor.nextset = MagicMock()
        self.db_executor.cursor.nextset.side_effect =[True]
        
        self.db_executor.cursor.description = (('SalesOrderID',"<class 'int'>",'None','10','10','0','False'))

  
        sample_query_path = r'tests\test_data\test_files\1_query.sql'
        with open(sample_query_path,'r') as file:
            sql_query=file.read()


        response=None
        try:
            response = self.db_executor.execute(sql_query)
        except StopIteration as ex:
            print(ex)

        self.assertIsNone(response)







            
            


        






