#from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime,date,timedelta


now = datetime.now()
print(now)
today_now = now.strftime("%Y-%m-%d %H:%M:%S")
print(today_now)

try:
  cnx = mysql.connector.connect(user='prabha', password='prabha123',
                              host='127.0.0.1',
                              database='web_scraping')
  print("connection good")
  cursor = cnx.cursor()

  add_quote = ("INSERT INTO web_scraping.quotes"
               "(quote, author, tags, last_upd_timestampquotes) "
               "VALUES (%s, %s, %s, %s)")
  data_quote = ('My Life my Way', 'prabha', 'life', today_now)
  result = cursor.execute(add_quote, data_quote)

  query = ("SELECT quote, author, tags, last_upd_timestampquotes FROM web_scraping.quotes")


  #hire_start = datetime.date(1999, 1, 1)
  #hire_end = datetime.date(1999, 12, 31)

  cursor.execute(query)

  for (quote, author, tags, last_upd_timestampquotes) in cursor:
      print("{}, quote is written by {} \tand classified into {} updated on {:%d %b %Y}".format(
          quote, author, tags, last_upd_timestampquotes))

  cnx.commit()

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:

  cnx.close()