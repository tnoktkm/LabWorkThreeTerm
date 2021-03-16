from shop import shop
from datasql import datasql
from dataxml import dataxml
import os

shop1=shop()#наши магазины
dxml1=dataxml(shop1,'old.xml','new.xml')#база данных магазинов

dsql1=datasql(shop1,'new.sqlite','new.sqlite')	#чтение и вывод в один файл.



dxml1.read() ## ПРОЧИТАЛ ДАННЫЕ ИЗ ФАЙЛА ВВОДА XML
if os.path.isfile( dsql1.getOut() ):
	os.remove(dsql1.getOut())

dsql1.write()	##ВЫВЕЛ ДАННЫЕ ИЗ ПРОГРАММЫ В ФАЙЛ SQLITE
shop1.clear()	##УДАЛИЛ ДАННЫЕ ИЗ ПРОГРАММЫ

# path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'new.sqlite')
# if (path != None):
# 	os.remove(path)


dsql1.read()	##ВВЕЛ ДАННЫЕ ИЗ ФАЙЛА SQLITE В ПРОГРАММУ

# path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'new.xml')
# if (path != None):
# 	os.remove(path)
if os.path.isfile( dxml1.getOut() ):
	os.remove(dxml1.getOut())

dxml1.write()	##ВЫВЕЛ ДАННЫЕ ИЗ ПРОГРАММЫ В НОВЫЙ(ЧИСТЫЙ) ФАЙЛ XML


print("True\n")