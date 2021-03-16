from orderer import orderer
from good import good

class order:
	def __init__ (self, code=0, orderer=None, good=None,  amount='', data=''):
		self.setCode(code)
		self.setOrderer(orderer)
		self.setGood(good)
		self.setAmount(amount)
		self.setData(data)

	#set------------------------------------------
	def setCode(self, value): self.__code=value
	def setOrderer(self, value):
		if isinstance(value, orderer):self.__orderer=value
	def setGood(self, value):
		if isinstance(value, good):self.__good = value
	def setAmount(self,value): self.__amount=value
	def setData(self, value): self.__data=value
	
	#get-------------------------------------
	def getCode(self):return self.__code

	#getOrderer
	def getOrdererCode(self):
		if self.__orderer:return self.__orderer.getCode()
	def getOrdererName(self):
		if self.__orderer:return self.__orderer.getName()
	def getOrdererAdress(self):
		if self.__orderer:return self.__orderer.getAdress()
	def getOrdererTelephone(self):
		if self.__orderer:return self.__orderer.getTelephone()
	def getOrdererContactFace(self):
		if self.__orderer:return self.__orderer.getContactFace()

	#getGood
	def getGoodCode(self):
		if self.__good:return self.__good.getCode()
	def getGoodPrice(self):
		if self.__good:return self.__good.getPrice()
	def getGoodDilivery(self):
		if self.__good:return self.__good.getDilivery()
	def getGoodDescription(self):
		if self.__good:return self.__good.getDescription()

	def getAmount(self):return self.__amount
	def getData(self):return self.__data
	#-------------------------------------------------------------
	#setOrderer
	def setOrdererCode(self, value):
		self.__orderer.setCode(value)
	def setOrdererName(self, value):
		self.__orderer.setName(value)
	def setOrdererAdress(self, value):
		self.__orderer.setAdress(value)
	def setOrdererTelephone(self, value):
		self.__orderer.setTelephone(value)
	def setOrdererContactFace(self, value):
		self.__orderer.seContactFace(value)

	#setGood----------------------------------------
	def setGoodCode(self, value):
		self.__good.setCode(value)
	def setGoodPrice(self, value):
		self.__good.setPrice(value)
	def setGoodDilivery(self, value):
		self.__goood.setDilivery(value)
	def setGoodDescription(self, value):
		self.__good.setDescription(value)
	def setGoodContactFace(self, value):
		self.__good.seContactFace(value)



	def info(self):
		s = '''Код заказа: %s. 
Заказчик: (Код заказчика: %s, имя: %s, адрес: %s, телефон: %s, контактное лицо: %s)
Товар: (Цена: %s, возможность доставки: %s, описание: %s)
Количество товара заказа: %s. 
Дата доставки: %s.'''% (self.getCode(),self.getOrdererCode(), self.getOrdererName(),self.getOrdererAdress(),self.getOrdererTelephone(),self.getOrdererContactFace(),self.getGoodPrice(),self.getGoodDilivery(),self.getGoodDescription(), self.getAmount(), self.getData())
		return s

