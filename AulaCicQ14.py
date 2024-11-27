# Função para converter uma sequência de DNA em RNA-m
def dna_para_rna(dna):
    rna = ""  # Inicializa uma string vazia para armazenar o RNA-m
    for base in dna:  # Para cada base na sequência de DNA
        if base == "A":
            rna += "U"  # Se a base for 'A' (Adenina), coloca 'U' (Uracila) no RNA
        elif base == "G":
            rna += "C"  # Se a base for 'G' (Guanina), coloca 'C' (Citosina) no RNA
        elif base == "C":
            rna += "G"  # Se a base for 'C' (Citosina), coloca 'G' (Guanina) no RNA
        elif base == "T":
            rna += "A"  # Se a base for 'T' (Timina), coloca 'A' (Adenina) no RNA
    return rna  # Retorna a sequência de RNA-m

# Solicita ao usuário a sequência de DNA
sequencia_dna = input("Digite a sequência de DNA (somente letras A, G, C, T): ").upper()

# Chama a função para converter a sequência de DNA para RNA-m
sequencia_rna = dna_para_rna(sequencia_dna)

# Exibe a sequência de RNA-m
print("A sequência de RNA-m correspondente é:", sequencia_rna)
