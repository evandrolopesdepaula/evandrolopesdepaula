#Fazer uma lista com 100 palavras, e solicitar que o computador acerte
#a palavra que foi escolhida pelo usuário.

import random

lista = ("Bailarina","Futebol","Estátua","Pintor","Frio","Bebê","Mímico","Escova de dentes","Lápis","Livro"
         ,"Astronauta","Amor","Ódio","Cego","Cadeira","Sacola","Professor","Médico","Calculadora","Artista"
         ,"Vitória","Pescador","Internet","Basquete","Semente","Policial","Amargo","Bilhete","Xadrez","Banana"
         ,"Micróbio","Romance","Carteira","Máquina de lavar","Prancha de surfe","Debate","Lixo","Sombra","Cadeado","Massagem"
         ,"Borboleta","Cavalo","Cachorro","Caranguejo","Chimpanzé","Coelho","Jacaré","Elefante","Galinha","Girafa"
         ,"Leão","Gato","Sapo","Veado","Tigre","Grilo","Formiga","Abelha","Hipopótamo","Golfinho"
         ,"Tigre","Capivara","Esquilo","Rato","Porco","Maca","Templo","Cápsula","Estrada","Planeta"
         ,"terra","Estojo","Paraíso","Estrela","Trem","Infinito","Marrom","Preto","Verde","Branco"
         ,"Vermelho","Castanho","Roxo","Cinza","Vermelho","Tutor","Linguagem","Museu","Progresso","Diretor"
         ,"Direito","Falar","Pensamento","Faculdade","Recreio","Inovar","Jornalismo","Filologia","Diploma","Escola")
print()
print("Lista:")
print ("Bailarina,","Futebol,","Estátua,","Pintor,","Frio,","Bebê,","Mímico,","Escova de dentes,","Lápis,","Livro,")
print("Astronauta,","Amor,","Ódio,","Cego,","Cadeira,","Sacola,","Professor,","Médico,","Calculadora,","Artista,")
print("Vitória,","Pescador,","Internet,","Basquete,","Semente,","Policial,","Amargo,","Bilhete,","Xadrez,","Banana,")
print("Micróbio,","Romance,","Carteira,","Máquina de lavar,","Prancha de surfe,","Debate,","Lixo,","Sombra,","Cadeado,","Massagem,")
print("Borboleta,","Cavalo,","Cachorro,","Caranguejo,","Chimpanzé,","Coelho,","Jacaré,","Elefante,","Galinha,","Girafa,")
print("Leão,","Gato,","Sapo,","Veado,","Tigre,","Grilo,","Formiga,","Abelha,","Hipopótamo,","Golfinho,")
print("Tigre,","Capivara,","Esquilo,","Rato,","Porco,","Maca,","Templo,","Cápsula,","Estrada,","Planeta,")
print("terra,","Estojo,","Paraíso,","Estrela,","Trem,","Infinito,","Marrom,","Preto,","Verde,","Branco,")
print("Vermelho,","Castanho,","Roxo,","Cinza,","Azul,","Tutor,","Linguagem,","Museu,","Progresso,","Diretor,")
print("Direito,","Falar,","Pensamento,","Faculdade,","Recreio,","Inovar,","Jornalismo,","Filologia,","Diploma,","Escola",".")
print()
palavra = input("Digite uma das palavras da lista para o computador adivinhar :")

escolhido = random.choice(lista)
while escolhido != palavra:
    escolhido = random.choice(lista)

    print("O computador errou!")
    print("O computador escolheu : ",escolhido)

else:
    print("O computador acertou!")
