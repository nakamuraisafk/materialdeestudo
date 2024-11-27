nome = input("Digite o seu nome: ")

contador = 1
while contador <= len(nome):
    print(nome[:contador])
    contador += 1