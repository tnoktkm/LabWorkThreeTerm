from orderer import orderer
from generallistedit import generalListEdit

class ordererListEdit(generalListEdit):
	#добавление нового элемента в список типа - (Заказчик).
	def newRec(self, code=0, name='',adress='',telephone='',contactFace=''):self.appendList(orderer(code, name, adress, telephone, contactFace))
	
	#get-----------------------------
	def getName(self, code): return self.findByCode(code).getName()
	def getAdress(self, code): return self.findByCode(code).getAdress()
	def getTelephone(self, code): return self.findByCode(code).getTelephone()
	def getContactFace(self, code): return self.findByCode(code).getContactFace()


	


	#set--------------------------------
	def setName(self, code): self.findByCode(code).setName()