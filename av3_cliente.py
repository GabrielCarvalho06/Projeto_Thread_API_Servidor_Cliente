"""
Cliente
Gabriel da Silva Carvalho - 0050013382
"""

from socket import *
s = socket ()

valor = input ("Digite um valor em dolares de sua busca: (ex:'100.00')")
meusbytes = str.encode(str(valor), "UTF-8")

s.connect(("127.0.0.1", 8752))
s.send (meusbytes)

data = s.recv(1024)
print(data.decode("utf-8"))

s.close ()