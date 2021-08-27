from produto import Produto

p1=Produto(4341, 'Fone Bluetooth', 780)
p2=Produto(2155, "TV 60'", 12000)
p3=Produto(5235, 'Teclado e mouse gamer', 630)
p4=Produto(1323, 'SmartFone', 4500)
p5=Produto(7346, 'Ultrabook', 20000)
p=[p1.preco, p2.preco, p3.preco, p4.preco, p5.preco]

p1.lista()
p2.lista()
p3.lista()
p4.lista()
p5.lista()
print('A soma de todos preços é R$ {}'.format(Produto.somar_produtos(p)))