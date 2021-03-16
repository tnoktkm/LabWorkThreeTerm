class generalList:
	def __init__(self):self.__list=[]

	def clear(self):self.__list=[] ##очистка списка
	def findByCode(self,code):		##найти элемент списка по коду
		for l in self.__list:
			if l.getCode()==code:
				return l

	def getCodes(self):return [s.getCode() for s in self.__list] #список всех кодов элементов в скиске
	def appendList(self,value):self.__list.append(value)		#добавление элемента в список
	def removeList(self,code):									##удаление элемента из списка
		for s in self.__list:
			if s.getCode()==code:self.__list.remove(s)

	def getName(sef,code):return self.findByCode(code).getName()	#имя по коду элемента в списке