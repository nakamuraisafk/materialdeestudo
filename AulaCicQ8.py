
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

print("A primeira string é:", string1)
print("O comprimento da primeira string é:", len(string1))
print("A segunda string é:", string2)
print("O comprimento da segunda string é:", len(string2))

if len(string1) == len(string2):
    print("As duas strings têm o mesmo comprimento.")
else:
    print("As duas strings têm comprimentos diferentes.")

if string1 == string2:
    print("As duas strings têm o mesmo conteúdo.")
else:
    print("As duas strings têm conteúdos diferentes.")
