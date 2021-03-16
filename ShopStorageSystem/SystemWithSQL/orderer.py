class orderer:
	def __init__ (self, code=0, name='', adress='', telephone=0, contactFace=''):
		self.setCode(code)
		self.setName(name)
		self.setAdress(adress)
		self.setTelephone(telephone)
		self.setContactFace(contactFace)

	def setCode(self,value):self.__code=value
	def setName(self, value): self.__name=value
	def setAdress(self, value): self.__adress=value
	def setTelephone(self,value): self.__telephone=value
	def setContactFace(self,value): self.__contactFace=value

	def getCode(self):return self.__code
	def getName(self):return self.__name
	def getAdress(self):return self.__adress
	def getTelephone(self):return self.__telephone
	def getContactFace(self):return self.__contactFace

	def info(self):
		s = '%s %s %s %s %s' % (self.getCode(), self.getName(), self.getAdress(), self.getTelephone(), self.getContactFace())
		return s