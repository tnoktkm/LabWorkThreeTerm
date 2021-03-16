from good import good
from generallistedit import generalListEdit
from generallist import generalList

class goodListEdit(generalList):
	#добавление нового элемента в список типа - (Товар).
	def newRec(self, code=0, price='',dilivery='',description=''): self.appendList(good(code, price, dilivery, description))

	#get-----------------------
	def getPrice(self, code): return self.findByCode(code).getPrice()
	def getDilivery(self, code): return self.findByCode(code).getDilivery()
	def getDescription(self, code): return self.findByCode(code).getDescription()


	#set--------------------------------------------------
	def setPrice(self, code, value): self.findByCode(code).setPrice(value)
	def setDilivery(self, code, value): self.findByCode(code).setDilivery(value)
	def setDescription(self, code, value): self.findByCode(code).setDescription(value)