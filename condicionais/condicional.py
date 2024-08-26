peso=float(input("Digite seu peso:"))
h=float(input("Digite sua altura:"))
imc=peso/(h*h)
print("seu IMC é",imc)

if imc < 18.5:
    print("Voce tá abaixo do peso")
elif imc > 18.5 and imc < 25:
    print("Seu peso está normal")
elif imc > 25 and imc<30:
    print("acima  do peso")
elif imc>30:
    print("obeso")