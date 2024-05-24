import pyodbc
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
import oracledb
from parameters import parameters


def sqlquery(engine,dataBase,queryPath,server=None,user=None,password=None,dataReturn=True): 
    
    if user == "" or password == "":
        user = None
        password = None

    if engine == 'sqlServer':
        
        connection_url = URL.create(
            "mssql+pyodbc",
            username=user,
            password=password,
            host=server,
            database=dataBase,
            query={
                    "driver": "SQL Server",
            },
        )
        if queryPath[0:3] == 'sql':
            with open(queryPath,'r') as inserts:
                query = text(inserts.read())
            if dataReturn:
                engine = create_engine(connection_url)
                df = pd.read_sql_query(query, con=engine.connect())
                return df
            else: # if it does not have return
                engine = create_engine(connection_url)
                connection = engine.connect()
                try:
                    connection.execute(query)
                except Exception as e:
                    print(str(e))
                connection.commit()
                connection.close()
        else:
            query = queryPath
            if dataReturn:
                engine = create_engine(connection_url)
                df = pd.read_sql_query(query, con=engine.connect())
                return df
            else: # if it does not have return
                engine = create_engine(connection_url)
                connection = engine.connect()
                sql_query = text(query)
                try:
                    connection.execute(sql_query)
                except Exception as e:
                    print(str(e))
                connection.commit()
                connection.close()

        
        
    elif engine == 'oracle':
        try:
            dsn = parameters['dsnOracle'][dataBase]
        except:
            raise Exception('dns it not defined')
        try:
            oracledb.init_oracle_client()
            with oracledb.connect(user=user, password=password, dsn=dsn) as connection:
                cur = connection.cursor()
                if queryPath[0:3] == 'sql':
                    with open(queryPath,'r') as inserts:
                        query = inserts.read()
                else:
                    query = queryPath
                try:
                    cur.execute(query)
                except Exception as e:
                    print(str(e))

                if dataReturn:
                    df = pd.DataFrame(cur.fetchall())
                    df.columns = [x[0] for x in cur.description]
                    connection.commit()
                    return df  
        except Exception as e:
           print(str(e))
    else:
        print('Engine not defined')
        