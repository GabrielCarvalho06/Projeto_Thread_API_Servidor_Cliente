# Proxy
# Gabriel da Silva Carvalho - 0050013382

import requests
import urllib.parse
import json

from socket import *
from threading import *

s = socket ()

def trata_conn(conn, cliente):
    while True:
        data = conn.recv(4096)
        
        if not data:
                break
    
        valor_x = float(data.decode("utf-8"))
        print("O valor recebido foi US$:", valor_x)

        x = 0
    
        api = "http://127.0.0.1:8081/lista_clientes"
        url = api
        cliente_lista = requests.get(url).json()
        #print (json.dumps(cliente_lista, indent = 4))
        
        for customer in cliente_lista:
            api2 = "http://127.0.0.1:8081/get_cliente/"
            url = api2+str(customer["CustomerId"])
            cliente_get = requests.get(url).json()
            #print (json.dumps(cliente_get, indent = 4))
            
        for total in cliente_lista:
            api3 = "http://127.0.0.1:8081/total_de_compras/"
            url = api3+str(total["CustomerId"])
            valor_total = requests.get(url).json()
            #print (json.dumps(valor_total, indent = 4))
            x += valor_total[0]["Total"]
  
        if x >= valor_x:
            nome = cliente_get[0]["FirstName"] + " " + cliente_get[0]["LastName"]
            conn.send (str.encode("O cliente {} teve compras maiores com {:.2f} \n".format(nome, x)))
            
    print("fim da conexão com "+str(cliente))
    conn.close()

host = "0.0.0.0"
porta = 8752
s.bind((host, porta))
s.listen(10)

while True:
    (conn, cliente) = s.accept ()
    print ("Recebi a conexão de "+str(cliente))

    t = Thread(target = trata_conn, args = (conn, cliente))
    t.start ()
    