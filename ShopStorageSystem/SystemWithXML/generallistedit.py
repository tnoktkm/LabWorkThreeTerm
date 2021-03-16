from generallist import generalList

class generalListEdit(generalList):

	#возвращает код для нового элемента
	def getNewCode(self):			
		m = 0
		for c in self.getCodes():
			if c>m:m=c
		return m+1

	#изменение имени выбранного элемента в списке
	def setName(self, code, value): self.findByCode(code).setName(value)
