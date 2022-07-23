salario = 0
salario = float(input("Insira o salário do colaborador: "))

if salario <= 1903.98:
  print("Colaborador insento do imposto de renda")
elif salario <= 2826.65:
  salario = (salario * 0.075)
  print(f"Valor a ser pago de IR pelo colaborador {salario}")
elif salario <= 3751.06:
  salario = salario * 0.15
  print(f"Valor a ser pago de IR pelo colaborador {salario}")
elif salario <= 4664.68:
  salario = salario * 0.225
  print(f"Valor a ser pago de IR pelo colaborador {salario}")
else:
  salario = salario * 0.275
  print(f"Valor a ser pago de IR pelo colaborador: {salario}")
