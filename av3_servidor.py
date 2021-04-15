# Servidor
# Gabriel da Silva Carvalho - 0050013382

import mysql.connector
from flask import Flask
import json
from flask_jsonpify import jsonify

app = Flask(__name__) # __name__ variável do sistema que indica o nome do módulo ou 'main'
    
@app.route("/lista_clientes")
def lista_clientes ():
    conn = mysql.connector.connect (host='', user='', passwd='teste', port='3306', database='chinook')
    cursor = conn.cursor()
    qstr = "select CustomerId from customers"
    print (qstr)
    query = cursor.execute(qstr)
    row_headers=[x[0] for x in cursor.description]
    records = cursor.fetchall()
    print (records)
    result = [dict(zip(tuple (row_headers) ,i)) for i in records]
    print (result)
    jret = jsonify(result)
    print (jret)
    conn.close()
    return jret
    
@app.route("/get_cliente/<id>")
def get_cliente (id):
    conn = mysql.connector.connect (host='', user='', passwd='teste', port='3306', database='chinook')
    cursor = conn.cursor()
    qstr = "select FirstName, LastName from customers WHERE CustomerId = "+id
    print (qstr)
    query = cursor.execute(qstr)
    row_headers=[x[0] for x in cursor.description]
    records = cursor.fetchall()
    print (records)
    result = [dict(zip(tuple (row_headers) ,i)) for i in records]
    print (result)
    jret = jsonify(result)
    print (jret)
    conn.close()
    return jret
    
@app.route("/total_de_compras/<id>")
def total_de_compras(id):
    conn = mysql.connector.connect (host='', user='', passwd='teste', port='3306', database='chinook')
    cursor = conn.cursor()
    qstr = "select Total from invoices WHERE CustomerId = "+id
    print (qstr)
    query = cursor.execute(qstr)
    row_headers=[x[0] for x in cursor.description]
    records = cursor.fetchall()
    print (records)
    result = [dict(zip(tuple (row_headers) ,i)) for i in records]
    print (result)
    jret = jsonify(result)
    print (jret)
    conn.close()
    return jret
    
app.run(port='8081')