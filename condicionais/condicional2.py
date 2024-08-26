valor=float(input("Digite o valor da compra:"))
forma=int(input( "Digite (1): À vista em dinheiro ou cheque, recebe 10% de desconto\n Digite(2):À vista no cartão de crédito, recebe 15% de desconto\n Digite(3):Em duas vezes, preço normal de etiqueta sem juros\n Digite(4):Em duas vezes, preço normal de etiqueta mais juros de 10\nDigite sua forma de pagamento:\n"))
if forma==1:
    compra=valor*0.1
    a=valor-compra
    print(f"o valor da sua compra é de R${a}")
elif forma==2:
    compra= valor*0.15
    a=valor-compra
    print(f"o valor da sua compra é de R${a}")
elif forma==3:
    compra=valor/2
    print(f"o valor da sua compra é de R${compra}")
elif forma==4:
    compra=valor*0.1
    a=valor+compra
    b=a/2
    print(f"o valor da sua compra é de R${b}")