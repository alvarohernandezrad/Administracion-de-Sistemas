import mysql.connector as mariadb
import requests
import time
import os


def base_de_datos(datos):

  time.sleep(10)
  mariadb_conexion = mariadb.connect(host = '127.0.0.1', port = 3306, user = "root", password = "root")
  cursor = mariadb_conexion.cursor()
  cursor.execute("create database if not exists cryptos")
  cursor.execute("use cryptos")
  cursor.execute("create table if not exists Cryptos (date datetime not null, name varchar(256) not null, symbol varchar(256) not null, price decimal(17,12) not null, primary key (date, name))")
  date = time.strftime('%Y-%m-%d %H:%M:%S')
  for name, symbol, price in datos:
      cursor.execute("insert into Cryptos (date, name, symbol, price) values (\'"+date+"\', \'"+name+"\', \'"+symbol+"\', "+str(price)+");");
  cursor.execute("select name, symbol, price from Cryptos")
  for name, symbol, price in cursor:
    print("Name: " + name)
    print("Symbol: " + symbol)
    print("Price: " + str(price))

  mariadb_conexion.commit()
  mariadb_conexion.close()


############################################################################


def conseguir_datos():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start':'1',
    'limit':'10',
    'convert':'EUR'
  }
  key = '5047f3af-c173-484c-8910-c6f4d23976fc'
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': ''+key+''
  }

  json = requests.get(url, params=parameters, headers=headers).json()

  monedas = json['data']
  datos = []


  for moneda in monedas:
      nombre = moneda['name']
      simbolo = moneda['symbol']
      precio = moneda['quote']['EUR']['price']
      datos.append((nombre, simbolo, precio))

  #print(datos)
  return datos

###############################################################################



def main():
  key = os.environ.get('KEY')
  datos = conseguir_datos()
  base_de_datos(datos)


if __name__ == "__main__":
  main()
