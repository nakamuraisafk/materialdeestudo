palavra_secreta = "pneumoultramicroscopicossilicovulcanoconiótico"

# Variáveis iniciais
tentativas = 6
letras_descobertas = ["_"] * len(palavra_secreta)
letras_erradas = []

print("Bem-vindo ao jogo da Forca!")
print("A palavra tem", len(palavra_secreta), "letras.")

# Enquanto houver tentativas e a palavra não for descoberta
while tentativas > 0 and "_" in letras_descobertas:
    # Mostra o progresso atual da palavra
    print("\nPalavra:", " ".join(letras_descobertas))
    print("Letras erradas:", ", ".join(letras_erradas))
    print("Tentativas restantes:", tentativas)

    # Solicita uma letra ao jogador
    letra = input("Digite uma letra: ").lower()

    # Verifica se a letra já foi usada
    if letra in letras_descobertas or letra in letras_erradas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    # Verifica se a letra está na palavra secreta
    if letra in palavra_secreta:
        print("Boa! A letra está na palavra.")
        # Atualiza as letras descobertas
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_descobertas[i] = letra
    else:
        print("Ops! A letra não está na palavra.")
        letras_erradas.append(letra)  # Adiciona a letra errada
        tentativas -= 1  # Diminui o número de tentativas

# Verifica se o jogador venceu ou perdeu
if "_" not in letras_descobertas:
    print("\nParabéns! Você descobriu a palavra:", palavra_secreta)
else:
    print("\nQue pena! Você foi enforcado.")
    print("A palavra era:", palavra_secreta)
