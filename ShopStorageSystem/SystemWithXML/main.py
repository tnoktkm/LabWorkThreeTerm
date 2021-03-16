from shop import shop
from dataxml import dataxml



shop1 = shop()   #создаём мазагин
data1 = dataxml(shop1,'old.xml','new.xml') #база для магазина
data1.read()		#читаем базу

#------Изменение данных базы(РАБОТА)----------------------------------
#shop1.newOrderer('Dima','SPB','79540356436','fdasfadgassrmfrpajpgrg')		
#shop1.newOrderer('Matvey','Saratov','79990005533','fdashfdhfg')
#shop1.newOrderer('Kirill','Novosib','79934205533','fdashfdhfgfdsdafsfs')

#shop1.newOrder(3, shop1.findOrdererByCode(1), shop1.findGoodByCode(1),'c','d')



shop1.removeOrderer(1) #------------------УДАЛЕНИЕ ПРЕДЫДУЩЕГО ЗАКАЗЧИКА
shop1.removeOrderer(2)
shop1.removeGood(1)
shop1.removeGood(2)
#вывод преобразованной базы в файл.
data1.write()





#b1 = order(0, amount='65',data='Завтра')
#b1.setCode(1)
#b1.setOrderer(orderer(0,'a','b',88888,'c'))
#b1.setGood(good(0,545,'a','b'))
#b1.setOrdererName('Игорь')


#print(b1.info())




print("\nTrue")
