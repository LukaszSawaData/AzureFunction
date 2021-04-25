import logging
import json
import textwrap
import time
import pyodbc
import datetime
import azure.functions as func
from configparser import ConfigParser


def default(o): 
    if isinstance(o,(datetime.datetime,datetime.date)): 
        return o.isoformat()



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    table_name =  req.params.get('table_name','OT_idx_xbrl')
     

    Config_parser = ConfigParser()
    Config_parser.read('SigmaAzurefunction/config.ini')

    database_username = Config_parser.get('sec_database','database_username')
    database_passsword = Config_parser.get('sec_database','database_password')

    logging.info('Read Credentials')

    logging.info(pyodbc.drivers())

    driver = '{ODBC Driver 17 for SQL Server}'


    connection_string = textwrap.dedent('''
        Driver = {driver};
        Server = ""
        Database = ""
        Uid = {username}
        PWd = {password}
        Encrypt  = yes
        '''.format(driver = driver,username = database_connection,Pwd =  database_password).replace("'","")


        try: 
            cnxn: pyodbc.Connection = pyodbc.connect(connection_string)
        except: 
            time.sleep(2)
            cnxn: pyodbc.Connection = pyodbc.connect(connection_string)
    

        query = """select  * from x""".format(x = table_name)


        cursor_object: pyodbc.Cursor = cnxn.cursor()

        cursor_object.execute(select_query)

        records = list(cursor_object.fetchall())

    )

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
