import random
lista=["abacaxi", "abajur", "abelha","alicate", "amarelo", "amigo", "amor", "anel", "anjo", "apito",  "aranha", "arara", "árvore", "ave", "avião", "avó", "balão","banana", "barco", "bebê", "bicicleta", "bola", "bolo", "boné", "borboleta", "branco", "café", "cama", "camelo", "caneca", "celular", "céu", "clube", "copo", "dado", "dia", "doce", "elefante", "elevador", "escada", "escola", "estojo", "faca", "fada", "feijão", "fogo", "foto", "gaiola", "garfo", "garrafa", "geleia", "girafa", "jaca", "janela", "joia", "lápis", "limonada", "lixo", "mãe", "meia", "molho", "ninho", "noite", "nuvem", "óculos", "ônibus", "ovo", "pai", "pão", "parque", "passarinho", "peixe", "pijama", "rádio", "rato", "rede", "tatu", "telefone", "tomate", "umbigo", "unha", "uva", "vaca", "vela", "violão", "vulcão", "xarope", "zebra", "zíper"]
palavra = random.choice(lista)
palavra = palavra.lower()
adivinhação2 = []
palavra2 = []
adivinhação1 = ""
c = 0
for n in palavra:
    palavra2.append(n)
t = 5
for n in palavra:
    adivinhação1 = adivinhação1 + "_"
adivinhação1 = adivinhação1.replace("", " ")
print(adivinhação1)
adivinhação1 = adivinhação1.replace(" ", "")
for n in adivinhação1:
    adivinhação2.append(n)
while t > 0:
    n = input("Palpite: ")
    if "ã" in palavra and n == "a":
        R="ã"
    elif "á" in palavra and n == "a":
        R="á"
    elif "é" in palavra and n == "e":
        R="é"
    elif "í" in palavra and n == "i":
        R="í"
    elif "ó" in palavra and n == "o":
        R="ó"
    elif "ú" in palavra and n == "u":
        R="ú"
    elif "ê" in palavra and n == "e":
        R="ê"
    elif "ô" in palavra and n == "o":
        R="ô"
    else:
        R=n
    if palavra.count(n) > 1:
        while n in palavra2:
            k = palavra2.index(n) + c
            adivinhação2[k] = n
            palavra2.remove(n)
            c = c + 1
        c = 0
        palavra2 = []
        for n in palavra:
            palavra2.append(n)
        adivinhação1 = ""
        for n in adivinhação2:
            adivinhação1 = adivinhação1 + n
        adivinhação1 = adivinhação1.replace("", " ")
        print(adivinhação1)
        adivinhação1 = adivinhação1.replace(" ", "")
    elif palavra.count(n)== 1:
        k = palavra.index(n)
        adivinhação2[k] = n
        adivinhação1 = ""
        for n in adivinhação2:
            adivinhação1 = adivinhação1 + n
        adivinhação1 = adivinhação1.replace("", " ")
        print(adivinhação1)
        adivinhação1 = adivinhação1.replace(" ", "")
    elif n not in palavra and R in palavra:
        if R in palavra:
            i=palavra.find(R)
            adivinhação2[i]=R
            adivinhação1=""
            for y in adivinhação2:
                adivinhação1=adivinhação1+y
            adivinhação1 = adivinhação1.replace("", " ")
            print(adivinhação1)
            adivinhação1 = adivinhação1.replace(" ", "")
    elif n and R not in palavra:
        t = t - 1
        print("A letra {} não está na palavra. Restam {} vidas".format(n, t))
    if adivinhação2.count("_") == 0:
        break
if adivinhação2.count("_") == 0:
    print("Parabéns! Você venceu.")
else:
    print("Você perdeu.")