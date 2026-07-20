import pymysql           # type:ignore
# import mysql.connector

def conectar_pymysql():
    conexao = pymysql.connect(
        host        = "127.0.0.1",
        user        = "root",
        password    = "",
        database    = "cidades",
        autocommit  = False,
        cursorclass = pymysql.cursors.DictCursor
    )
    return conexao
