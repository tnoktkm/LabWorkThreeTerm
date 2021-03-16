from generallist import generalList
from ordererListEdit import ordererListEdit
from orderListEdit import orderListEdit
from goodListEdit import goodListEdit
from generallistedit import generalListEdit

class shop():
	def __init__(self):
		self.__order=orderListEdit()
		self.__orderer=ordererListEdit()
		self.__good=goodListEdit()

	
	#orderer----------------------------
	def newOrderer(self, name='',adress='',telephone='',contactFace=''):self.__orderer.newRec(self.__orderer.getNewCode(),name,adress,telephone,contactFace)
	def newOrdererXML(self, code, name='',adress='',telephone='',contactFace=''):self.__orderer.newRec(code,name,adress,telephone,contactFace)
	def findOrdererByCode(self, code):return self.__orderer.findByCode(code)
	def getOrdererCodes(self):return self.__orderer.getCodes()

	def getOrdererName(self, code):	return self.__orderer.getName(code)
	def getOrdererAdress(self, code): return self.__orderer.getAdress(code)
	def getOrdererTelephone(self, code): return self.__orderer.getTelephone(code)
	def getOrdererContactFace(self, code): return self.__orderer.getContactFace(code)
	def removeOrderer(self, code):
		check = True
		for item in self.__order.getCodes():
			if (self.__order.getOrdererCode(item) == code):
				check = False
		if (check):
			self.__orderer.removeList(code)


	#good----------------
	def newGood(self, code=0, price='',dilivery='',description=''):self.__good.newRec(self.__good.getNewCode(),price,dilivery,description)
	def findGoodByCode(self, code): return self.__good.findByCode(code)
	def getGoodCodes(self):return self.__good.getCodes()

	def getGoodPrice(self, code):return self.__good.getPrice(code)
	def getGoodDilivery(self, code):return self.__good.getDilivery(code)
	def getGoodDescription(self, code):return self.__good.getDescription(code)
	def removeGood(self, code): 
		check = True
		for item in self.__order.getCodes():
			if (self.__order.getGoodCode(item) == code):
				check = False
		if (check):
			self.__good.removeList(code)


	#order----------------------------------
	def newOrder(self, code=0, orderer=None, good=None, amount='', data=''):self.__order.newRec(self.__order.getNewCode(),orderer,good,amount,data)
	def findOrderByCode(self, code):return self.__order.findByCode(code)
	def getOrderCodes(self):return self.__order.getCodes()

	def getOrderOrdererCode(self, code): return self.__order.getOrdererCode(code)
	def getOrderGoodCode(self, code): return self.__order.getGoodCode(code)
	def getOrderAmount(self, code): return self.__order.getAmount(code)
	def getOrderData(self, code): return self.__order.getData(code)
	def removeOrder(self, code): self.__order.removeList(code)
	
