# Caça aos erros
#1. O Problema da Idade
idade = input("Digite sua idade: ")
if idade >= 18:
    print("Você é maior de idade.")

#1. O Problema da Idade --- CORRIGIDO
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")

#1. O Problema da Idade --- MELHORADO
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#------------------------------------------------------------------------#
#2. A Escrita Fiel
nome = "Mariana"
print("Seja bem-vinda, nome!")

#2. A Escrita Fiel --- CORRIGIDO
nome = "Mariana"
print(f"Seja bem-vinda, {nome}!")

#2. A Escrita Fiel --- MELHORADO
nome = str(input("Digite seu nome: "))
print(f"Seja bem-vindo, {nome}!")
#------------------------------------------------------------------------#
#3. Falta de Espaço
numero = 10
if numero > 5:
print("O número é maior que cinco.")
else:
print("O número é menor ou igual a cinco.")

#3. Falta de Espaço --- CORRIGIDO
numero = 10
if numero > 5:
    print("O número é maior que cinco.")
else:
    print("O número é menor ou igual a cinco.")

#3. Falta de Espaço --- MELHORADO
print("Descubra se o número é maior, menor ou igual a 5")
numero = int(input("Digite um número: "))
if numero == 5:
    print("O número é igual a cinco.")
elif numero > 5:
    print("O número é maior que cinco.")
else:
    print("O número é menor que cinco.")

#------------------------------------------------------------------------#

#4. Esquecimento Fatal
usuario = "aluno123"
if usuario == "aluno123"
print("Login realizado com sucesso.")

#4. Esquecimento Fatal --- CORRIGIDO
usuario = "aluno123"
if usuario == "aluno123":
    print("Login realizado com sucesso.")

#4. Esquecimento Fatal --- MELHORADO
while True:
    usuario = str(input("Digite a senha: "))
    if usuario == "aluno123":
        print("Login realizado com sucesso.")
        break
    else:
        print("Senha incorreta, tente novamente...")

#------------------------------------------------------------------------#

#5. Atribuição vs. Comparação
clima = "ensolarado"
if clima = "chuvoso":
    print("Leve um guarda-chuva!")

#5. Atribuição vs. Comparação --- CORRIGIDO
clima = "ensolarado"
if clima == "chuvoso":
    print("Leve um guarda-chuva!")

#5. Atribuição vs. Comparação --- MELHORADO
clima = str(input("Digite se o clima está chuvoso ou ensolarado: "))
if clima == "chuvoso":
    print("Leve um guarda-chuva!")
elif clima == "ensolarado":
    print("Não à necessidade de levar guarda-chuva")

#------------------------------------------------------------------------#

#6. Misturando Alhos com Bugalhos
pontos = 50
print("Parabéns!Você fez "+pontos+"pontos.")

#6. Misturando Alhos com Bugalhos --- CORRIGIDO
pontos = 50
print(f"Parabéns! Você fez {pontos} pontos.")

#6. Misturando Alhos com Bugalhos --- MELHORADO
pontos = float(input("Digite sua pontuação: "))
print(f"Parabéns! Você fez {pontos} pontos.")

#------------------------------------------------------------------------#

#7. A Ordem dos Fatores
O sistema deve dar "Excelente" para notas 9 ou 10.
nota = 9.5
if nota >= 7:
    print("Aprovado")
elif nota >= 9:
    print("Excelente!")

#7. A Ordem dos Fatores --- CORRIGIDO
# O sistema deve dar "Excelente" para notas 9 ou 10.
nota = 9.5
if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Aprovado")

#7. A Ordem dos Fatores --- MELHORADO
# O sistema deve dar "Excelente" para notas 9 ou 10.
nota = float(input("Digite sua nota: "))
if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")

#------------------------------------------------------------------------#

#8. O Contador de 1 a 5
 Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
for i in range(5):
    print(i)

#8. O Contador de 1 a 5 --- CORRIGIDO
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
for i in range(1, 6):
    print(i)

#8. O Contador de 1 a 5 --- MELHORADO
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
for i in range(1, 6):
    print(f"°{i} número")

#------------------------------------------------------------------------#

#9. O Loop Eterno
tentativas = 1
while tentativas <= 3:
    print("Tentando conectar...")
    O código deveria parar após 3 tentativas

#9. O Loop Eterno --- CORRIGIDO
tentativas = 1
while tentativas <= 3:
    print("Tentando conectar...")
    tentativas += 1
#    O código deveria parar após 3 tentativas

#9. O Loop Eterno --- MELHORADO
from time import sleep
tentativas = 1
while tentativas <= 3:
    print(f"°{tentativas} tentativa de conexão...")
    sleep(1.0)
    tentativas += 1
#    O código deveria parar após 3 tentativas

#------------------------------------------------------------------------#

#10. A Senha Teimosa
O programa deve pedir a senha até que o usuário digite "python123"
senha = ""
while senha == "python123":
    senha = input("Digite a senha secreta: ")
print("Acesso concedido!")

#10. A Senha Teimosa --- CORRIGIDO
# O programa deve pedir a senha até que o usuário digite "python123"
while True:
    senha = input("Digite a senha secreta: ")
    if senha == "python123":
        print("Acesso concedido!")
        break


#10. A Senha Teimosa --- MELHORADO
# O programa deve pedir a senha até que o usuário digite "python123"
while True:
    senha = str(input("Digite a senha secreta: "))
    if senha == "python123":
        print("Acesso concedido!")
        break
    else:
        print("Acesso negado, tente novamente...")