from generallistedit import generalListEdit
from order import order

class orderListEdit(generalListEdit):
	#добавление нового элемента в список типа - (Заказ).
	def newRec(self, code=0, orderer=None, good=None, amount='', data=''): self.appendList(order(code, orderer, good, amount, data))

	#set-----------------------
	def setAmount(self, code, value):self.findByCode(code).setAmount(value)


	#get---------------------------
	def getOrdererCode(self, code): return self.findByCode(code).getOrdererCode()
	def getOrdererName(self, code):return self.findByCode(code).getOrdererName()
	def getOrdererAdress(self,code):return  self.findByCode(code).getOrdererAdress()
	def getOrdererTelephone(self, code):return self.findByCode(code).getOrdererTelephone()
	def getOrdererContactFace(self, code): return self.findByCode(code).getOrdererContactFace()

	def getGoodCode(self, code): return self.findByCode(code).getGoodCode()
	def getGoodPrice(self, code): return self.findByCode(code).getGoodPrice()
	def getGoodDilivery(self, code): return self.findByCode(code).getGoodDilivery()
	def getGoodDescription(self, code): return self.findByCode(code).getGoodDescription()

	def getAmount(self, code): return self.findByCode(code).getAmount()
	def getData(self, code): return self.findByCode(code).getData()