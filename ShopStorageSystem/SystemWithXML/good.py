class good():
	def __init__ (self,code=0, price=0, dilivery='', description=''):
		self.setCode(code)
		self.setPrice(price)
		self.setDilivery(dilivery)
		self.setDescription(description)
				
	def setCode(self, value): self.__code=value
	def setPrice(self, value): self.__price=value
	def setDilivery(self, value): self.__dilivery=value
	def setDescription(self,value): self.__description=value

	def getCode(self):return self.__code
	def getPrice(self):return self.__price
	def getDilivery(self):return self.__dilivery
	def getDescription(self):return self.__description
	
	def info(self):
		s = '%s %s %s %s' % (self.getCode(), self.getPrice(), self.getDilivery(), self.getDescription())
		return s