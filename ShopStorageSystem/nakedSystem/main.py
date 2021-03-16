from order import order
from good import good
from orderer import orderer



b1 = order(0, amount='65',data='Завтра')
b1.setCode(1)
b1.setOrderer(orderer(0,'a','b',88888,'c'))
b1.setGood(good(0,545,'a','b'))
b1.setOrdererName('Игорь')


print(b1.info())




print("\nTrue")
