import random 
import os 
import time

# Jogo da Forca com Nomes de Animais Africanos
# 
# Este é um jogo da forca onde o jogador deve adivinhar o nome de um animal africano.
# O programa escolhe aleatoriamente uma palavra de uma lista de nomes de animais.
# O jogador tem 6 chances para adivinhar a palavra, inserindo uma letra por vez.
# Se a letra estiver na palavra, ela será revelada na posição correta.
# Se a letra não estiver na palavra, o jogador perde uma chance.
# O jogo termina quando o jogador adivinha a palavra ou perde todas as chances.
# O programa também oferece uma dica quando restam 3 chances.
#
# Funções principais:
# - encaixar_letra: Atualiza a palavra secreta com a letra escolhida pelo jogador.
# - desenhar_forca: Desenha a forca com base no número de chances restantes.
#
# Divirta-se jogando!

def encaixar_letra(letra_esc: str, palavra_maquina: str, palavra_secreta: str) -> str:
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
    # Converte a palavra_secreta em uma lista para facilitar a alteração de caracteres
    palavra_lista = list(palavra_secreta)
    # Itera sobre cada letra da palavra_maquina
    for index, letra in enumerate(palavra_maquina):
        # Se a letra escolhida pelo usuário estiver na palavra_maquina,
        # substitui o underline correspondente na palavra_secreta
           # Junta a lista de volta em uma string
    return "".join(palavra_lista)

def desenhar_forca(chances):
    """Desenha a forca com base no número de chances restantes."""
    estagios = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """
    ]
    # Imprime o estágio correspondente ao número de chances restantes
    print(estagios[6 - chances])

# Início do jogo
print(" Jogo da Forca ".center(30, "="))
# Lista de palavras possíveis
lista_palavras = ["elefante", "girafa", "touro", "zebra", "javali", "gorila"]
# Escolhe uma palavra aleatória da lista
palavra_maquina = random.choice(lista_palavras)
# Define o número inicial de chances
chances = 6
# Conjunto para armazenar as letras já escolhidas pelo usuário
letras_escolhidas = set()

print("\nBem vindo ao jogo da forca!")
print("\nVocê tem 6 chances para adivinhar o animal africano que pensei!")
print("\nEscolha e digite uma letra para tentar adivinhar")
# Inicializa a palavra_secreta com underlines
palavra_secreta = "_" * len(palavra_maquina)
# Pausa para criar suspense
time.sleep(3)
# Limpa a tela (no Windows)
os.system("cls")

# Loop principal do jogo
while chances > 0 and palavra_secreta != palavra_maquina:
    print(f"\nPalavra: {palavra_secreta}")
    print(f"Chances: {chances}")
    print(f"Letras já escolhidas: {', '.join(letras_escolhidas)}")
    desenhar_forca(chances)
    letra_esc = input("Digite uma letra: ").lower()
    os.system("cls")

    # Verifica se a entrada é válida
    while not letra_esc.isalpha() or len(letra_esc) != 1:
        letra_esc = input("Entrada inválida. Digite uma única letra: ").lower()

    # Verifica se a letra já foi escolhida anteriormente
    if letra_esc in letras_escolhidas:
        print(f"Você já escolheu a letra '{letra_esc}'. Tente outra.")
        continue

    # Adiciona a letra escolhida ao conjunto de letras escolhidas
    letras_escolhidas.add(letra_esc)

    # Verifica se a letra escolhida está na palavra_maquina
    if letra_esc in palavra_maquina:
        print(f"A letra '{letra_esc}' pertence a palavra que pensei!")
        palavra_secreta = encaixar_letra(letra_esc, palavra_maquina, palavra_secreta)
    else:
        print(f"A letra '{letra_esc}' não pertence a palavra que eu pensei!")
        chances -= 1

    # Oferece uma dica se restarem 3 chances
    if chances == 3:
        print(f"Dica: O animal começa com a letra '{palavra_maquina[0]}'.")

# Verifica o resultado do jogo
if chances == 0:
    os.system("cls")
    desenhar_forca(chances)
    print(f"\nInfelizmente você perdeu! A palavra era: '{palavra_maquina}'")
    
if palavra_secreta == palavra_maquina:
    os.system("cls")
    print(f"\nParabéns, você venceu!! A palavra era: '{palavra_maquina}'")