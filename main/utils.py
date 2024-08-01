from flask import Flask
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from flask_mysqldb import MySQL
application=Flask(__name__)
application.secret_key='38e91d5c0779f65748ecb0edad7e3bcd8d463d5f448c62bef6bb6050c5ad4a19'
application.config["MYSQL_USER"] = "webserver"
application.config["MYSQL_PASSWORD"] = "password"
application.config["MYSQL_DB"] = "skripsi"
application.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql=MySQL(application)
def query_db(query,args=(),one=False):
    cur=mysql.connection.cursor()
    result=cur.execute(query,args)
    if one:
        result=cur.fetchone()
    else:
        result=cur.fetchall()
    return result