print("Exercicios:")
print()
print("1. Armazene uma frase dentro de uma variável e depois exiba a mesma na tela.")
print("2. Exiba uma mensagem de boas vindas para o usuário de acordo com o valor digitado.")
print("3. Crie um script onde exiba o nome da pessoa, e sua data de aniversário formatada.")
print("4. Crie um programa que leia dois números e mostre a soma entre eles.")
print("5. Faça um programa que receba um valor, e traga informações sobre esse valor, dizendo se é alfanumérico, numérico e etc.")
print("6. Faça um programa que mostre a soma de dois valores, e depois mostre o antecessor e o sucessor do mesmo.")
print("7. Leia um número, mostre seu dobro, triplo, e raíz quadrada.")
print("8. Desenvolva um programa que receba duas notas de um aluno e calcule sua média.")
print("9. Faça um programa que leia um valor em metros, mostre o valor convertido em centímetros, e milímetros.")
print("10. Faça um programa que leia um valor, e mostre a sua tabuada do 1 ao 10 na tela.")
print()



print("Exercicio 1 :")


frasedigitada_str = input("Digite uma frase:")
print(frasedigitada_str)
print()


print("Exercicio 2 :")
numero = 1
numero2 = input("Digite 1 ou 2 :")
numero3 = int(numero2)
if (numero == numero3):
    print("Bom dia .")
else:
    print("Bem-vindo.")
    print("Fim!")
    print()

print("Exercicio 3 :")

nome_str = input("Digite seu nome:")
dia = input("Digite seu dia de nascimento :")
dia2 = int(dia)
mes = input("Digite seu mês de nascimento :")
mes2 = int(mes)
ano = input("Digite seu ano de nascimento :")
ano2 = int(ano)
print(nome_str,"sua data de nascimento é :")
print(dia2,mes2,ano2, sep="/")
print()



print("Exercicio 4 :")

num = input("Digite um número:")
num2 = int(num)
num3 = input("Digite outro número:")
num4 = int(num3)
print("A soma dos números é:",num2+num4)
print()


print("Exercício 5 :")
a  =  input ( 'Digite algo para que o item seja verificado:' )
print ( 'O tipo primitivo desse dado é:' ,type ( a ))
print ( 'Só tem espaços?' , a . isspace ())
print ( 'É um número?' , a . isnumeric ())
print ( 'É uma letra?' , a . isalpha ())
print ( 'É alfanumérico?' , a . isalnum ())
print ( 'É uma letra maiúscula?' , a . isupper ())
print ( 'É uma letra minúscula?' , a . islower ())
print ( 'É um título?' , a . istitle ())


print("Exercício 6 :")


numA = input("Digite um número:")
numB = int(numA)
numC = input("Digite outro número:")
numD = int(numC)
print("Numeros digitados :",numB,"e",numD)
print("O antecessor de", numB, "é:",numB-1)
print("O sucessor de", numB," é:",numB+1)
print("O antecessor de", numD, "é:",numD-1)
print("O sucessor de", numD," é:",numD+1)
print()


print("Exercício 7 :")

numA1 = input("Digite um número:")
numB2 = int(numA1)
print("O dobro de ",numB2, "é :", numB2*2)
print("O triplo de ",numB2, "é :",numB2*3)
raiz = float(numB2) ** 0.5
print("A raiz quadrada de ",numB2, "é ",raiz)
print()


print("Exercício 8 :")

nota = input("Digite sua nota:")
resultado = int(nota)
nota2 = input("Digite outro número:")
resultado2 = int(nota2)
print("A média das duas notas é :",(resultado+resultado2)/2)
print()


print("Exercicio 9 :")

valor = float(input("Digite um número:"))
metros = int(valor)
centimetros = metros * 100
milimetros = metros *1000
print("O valor em metros é :",metros)
print("O valor em centímetros é :",centimetros)
print("O valor em milimetros é :",milimetros)
print()


print("Exercicio 10 :")

print("=== GERADOR DE TABUADA === ")
print()
numero=int(input("Digite um número: "))

print(" Tabuada do ",numero,":")
for contador in range(1,11):
    print(numero," X ",contador," = ",numero*contador )