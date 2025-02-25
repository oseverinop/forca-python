import random 
import os 
import time

"""Altera palavra_secreta."""
def encaixar_letra(letra_esc: str, palavra_maquina: str,
                    palavra_secreta: str) -> str:
    """Realiza a troca de caracteres em palavra_secreta.
    
    Muda o caracter '_' (underline) de uma posição por letra_esc.

    Args:
        letra_esc: Letra inserida pelo usuário.
        palavra_maquina: Palavra escolhida pelo programa.
        palavra_secreta: Palavra formada inicialmente por '_'
                (underlines), que vai ser mudada pela função.
                    
    Retorna:
        Retorna a palavra_secreta já com as alterações feitas.
    """

    palavra_lista = list(palavra_secreta)

    for index, letra in enumerate(list(palavra_maquina)):
        if letra == letra_esc:
            palavra_lista[index] = letra_esc
        
    palavra_secreta = "".join(palavra_lista)

    return palavra_secreta


print(" Jogo da Forca ".center(25, "="))

lista_palavras = ["elefante", "girafa", "touro", "zebra", "javali", "gorila"]

palavra_maquina = random.choice(lista_palavras)
chances = 6

print("\nBem vindo ao jogo da forca!")
print("\nVocê tem 6 chances para adivinhar o animal africano que pensei!")
print("\nEscolha e digite uma letra para tentar adivinhar")
palavra_secreta = "_" * len(palavra_maquina)
time.sleep(3)
os.system("cls")

while chances > 0 and palavra_secreta != palavra_maquina:
    print(f"\nPalavra: {palavra_secreta}")
    print(f"Chances: {chances}")
    letra_esc = input("Digite uma letra: ").lower()
    os.system("cls")

    if letra_esc in palavra_maquina and letra_esc != "":
        print(f"A letra '{letra_esc}' pertence a palavra que pensei!")
        palavra_secreta = encaixar_letra(letra_esc, palavra_maquina, palavra_secreta)

    else:
        print(f"A letra '{letra_esc}' não pertence a palavra que eu pensei!")
        chances -= 1

if chances == 0:
    os.system("cls")
    print(f"\nInfelizmente você perdeu! A palavra era: '{palavra_maquina}'")
    
if palavra_secreta == palavra_maquina:
    os.system("cls")
    print(f"\nParabéns, você venceu!! A palavra era: '{palavra_maquina}'")
