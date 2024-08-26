altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (M para masculino, F para feminino): ")


if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem de {altura} metros é {peso_ideal:.2f} kg.")
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher de {altura} metros é {peso_ideal:.2f} kg.")
else:
    print("Sexo não reconhecido. Use 'M' para masculino ou 'F' para feminino.")