import os,xml.dom.minidom
from data import data

class dataxml(data):

	def read(self):
		dom=xml.dom.minidom.parse(self.getInp())
		# По завершению инициализации настоятельно рекомендуется вызвать метод 
		# normalize для слияния разрозненных фрагментов текста воедино. 
		# В противном случае при разборе XML могут возникнуть ошибки.
		dom.normalize() 
		
		#перебираем сначало именно в 0-вом элементе node(у нас он один поэтому 0)
		#и в нем перебираем все node что есть:
		#childNodes ---- Список узлов, содержащихся в этом узле. Это атрибут только для чтения.
		for node in dom.childNodes[0].childNodes:
			if(node.nodeType == node.ELEMENT_NODE) and (node.nodeName == 'good'):
				code,price,dilivery,description = 0,"","","" ##создание переменных
				for t in node.attributes.items():	#проход в первом найденном node
					if t[0] == "code": code=int(t[1])		
					if t[0] == "price": price = t[1]
					if t[0] == "dilivery": dilivery = t[1]
					if t[0] == "description": description = t[1]
				#сначало спарсили xml и в этой строчке добавили спарсейнный элемент в список
				self.getShop().newGood(code,price,dilivery,description)


			#теперь проходим по тем, что заказчики(orderer)
			if(node.nodeType == node.ELEMENT_NODE) and (node.nodeName == 'orderer'):
				code,name,adress,telephone,contactFace = 0,"","","",""
				for t in node.attributes.items():
					if t[0] == "code": code = int(t[1])
					if t[0] == "name": name = t[1]
					if t[0] == "adress": adress = t[1]
					if t[0] == "telephone": telephone = t[1]
					if t[0] == "contactFace": contactFace = t[1]
				self.getShop().newOrdererXML(code, name,adress,telephone,contactFace)

				#аналогично----------
			if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == 'order'):
				code,orderer,good,amount,data = 0,None,None,"",""
				for t in node.attributes.items():
					if t[0] == "code":code = int(t[1])
					if t[0] == "orderer":orderer=self.getShop().findOrdererByCode(int(t[1]))
					if t[0] == "good": good=self.getShop().findGoodByCode(int(t[1]))
					if t[0] == "amount": amount = t[1]
					if t[0] == "data": data = t[1]
				self.getShop().newOrder(code,orderer,good,amount,data)

	def write(self):
		#открыли как весь(целый) документ
		dom = xml.dom.minidom.Document()
		#создали главный узел
		root = dom.createElement("shop")
		#добавили главный узел
		dom.appendChild(root)

		for c in self.getShop().getGoodCodes():
			aut = dom.createElement("good")
			aut.setAttribute('code', str(c))
			aut.setAttribute('price', str(self.getShop().getGoodPrice(c)))
			aut.setAttribute('dilivery', str(self.getShop().getGoodDilivery(c)))
			aut.setAttribute('description', str(self.getShop().getGoodDescription(c)))
			root.appendChild(aut)	#добавление

		for c in self.getShop().getOrdererCodes():
			pub = dom.createElement("orderer")
			pub.setAttribute('code', str(c))
			pub.setAttribute('name', str(self.getShop().getOrdererName(c)))
			pub.setAttribute('adress', self.getShop().getOrdererAdress(c))
			pub.setAttribute('telephone', str(self.getShop().getOrdererTelephone(c)))
			pub.setAttribute('contactFace', str(self.getShop().getOrdererContactFace(c)))
			root.appendChild(pub) #добавление

		for c in self.getShop().getOrderCodes():
			bk = dom.createElement("order")
			bk.setAttribute('code', str(c))
			bk.setAttribute('orderer', str(self.getShop().getOrderOrdererCode(c)))
			bk.setAttribute('good', str(self.getShop().getOrderGoodCode(c)))
			bk.setAttribute('amount', str(self.getShop().getOrderAmount(c)))
			bk.setAttribute('data', str(self.getShop().getOrderData(c)))
			root.appendChild(bk)
		f = open(self.getOut(), "w")
		f.write(dom.toprettyxml())

















