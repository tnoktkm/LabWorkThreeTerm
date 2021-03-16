from generalList import generalList

class goodsList(generalList):
	def getPrice(self, code): return self.findByCode(code).getPrice()
	def getDilivery(self, code):return self.findByCode(code).getDilivery()
	def getDescription(self, code):return self.findByCode(code).getDescription()
	def info(self, code):return self.findByCode(code).info()
	def infoList(self):
		s=''
		for code in self.getCodes():
			s+=self.info(code) + ', '
		if s:s=s[:-2]
		return s