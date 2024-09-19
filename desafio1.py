menu = """

[d] Depositar
[s] Sacar
[e] Extrado
[q] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""

while True:

  opcao = input(menu).lower()

  if opcao == "d":

    valor_deposito = float(input("Qual valor a ser depositado?"))

    if valor_deposito > 0:

      saldo += valor_deposito
      extrato += f"Deposito: R$ {valor_deposito:.2f}\n"
    
    else:
      print("Falha na Operação!\nInforme um valor válido.")

  
  elif opcao == "s":
    valor_saque = float(input("Qual valor do saque?"))
    
    if valor_saque > saldo:
      print("Falha na Operação!\n Você não possui saldo.")
    
    elif valor_saque > limite:
      print("Falha na Operação!\n Você excedeu o limite de saque.")

    elif numero_saques > LIMITE_SAQUES:
      print("Falha na Operação!\n Você excedeu o numero de saques permitido.")

    elif valor_saque > 0:
      saldo -= valor_saque
      extrato += f"Saque: - R$ {valor_saque:.2f}\n"
      numero_saques += 1

    else:

      print("Falha na Operação!\nInforme um valor válido.")



  elif opcao == "e":

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

  elif opcao == "q":
    break

  else:
    print("Operação invalida, por favor selecione novamente a operação desejada.")