import os
import sqlite3 as db
from data import data

emptydb = """
PRAGMA foreign_keys = ON;

create table good
(code integer primary key,
	price integer,
	dilivery text,
	description text);

create table orderer
(code integer primary key,
	name text,
	adress text,
	telephone text,
	contactFace text);

create table order2
(code integer primary key,
	orderer text,
	good text,
	amount integer,
	data text);

"""

class datasql(data):
	def read(self):
		#удаление записей, чтобы не была перезапись, а не добавление лишних данных.

		for item in self.getShop().getOrderCodes():
			self.getShop().removeOrder(item)
		for item in self.getShop().getOrdererCodes():
			self.getShop().removeOrderer(item)
		for item in self.getShop().getGoodCodes():
			self.getShop().removeGood(item)
		##############

		conn = db.connect(self.getInp())
		curs = conn.cursor()

		curs.execute('SELECT code,price,dilivery,description FROM good')
		data = curs.fetchall()
		for r in data: self.getShop().newGood(r[0],r[1],r[2],r[3])

		curs.execute('SELECT code,name,adress,telephone,contactFace FROM orderer')
		data=curs.fetchall()
		for r in data: self.getShop().newOrdererXML(r[0],r[1],r[2],r[3],r[4])

		curs.execute('SELECT code,orderer,good,amount,data FROM order2')
		data=curs.fetchall()
		for r in data: self.getShop().newOrder(r[0],r[1],r[2],r[3],r[4])
		conn.close()

	def write(self):
		if os.path.isfile( self.getOut() ):
			os.remove(self.getOut()) #удаление файла вывода в sqlite,
			#если он, конечно же, существует.

		conn = db.connect(self.getOut())
		curs = conn.cursor()
		curs.executescript(emptydb)
		for c in self.getShop().getGoodCodes():
			curs.execute("INSERT into good(code,price,dilivery,description) values('%s','%s','%s','%s')"%(
				str(c),
				self.getShop().getGoodPrice(c),
				self.getShop().getGoodDilivery(c),
				self.getShop().getGoodDescription(c)))

		for c in self.getShop().getOrdererCodes():
			curs.execute("INSERT into orderer(code,name,adress,telephone,contactFace) values('%s','%s','%s','%s','%s')"%(
				str(c),
				self.getShop().getOrdererName(c),
				self.getShop().getOrdererAdress(c),
				self.getShop().getOrdererTelephone(c),
				self.getShop().getOrdererContactFace(c)))

		for c in self.getShop().getOrderCodes():
			curs.execute("INSERT into order2(code,orderer,good,amount,data) values('%s','%s','%s','%s','%s')"%(
				str(c),
				self.getShop().getOrderOrdererCode(c),
				self.getShop().getOrderGoodCode(c),
				self.getShop().getOrderAmount(c),
				self.getShop().getOrderData(c)))
		conn.commit()
		conn.close()