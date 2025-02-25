![Animais Africanos](/img/africa-savannah-animals.jpg)

# Jogo da Forca com Nomes de Animais Africanos

Este é um jogo da forca desenvolvido em Python, onde o jogador deve adivinhar o nome de um animal africano. O jogo escolhe aleatoriamente uma palavra de uma lista de nomes de animais e o jogador tem 6 chances para adivinhar a palavra, inserindo uma letra por vez.

## Funcionalidades

- Escolha aleatória de uma palavra de uma lista de nomes de animais africanos.
- O jogador tem 6 chances para adivinhar a palavra.
- O jogo oferece uma dica quando restam 3 chances.
- Representação visual da forca com base no número de chances restantes.
- Verificação de entrada para garantir que o jogador insira apenas letras.
- Registro das letras já escolhidas pelo jogador para evitar repetições.

## Como Jogar

1. Execute o script Python.
2. O jogo escolherá aleatoriamente um nome de animal africano.
3. O jogador deve inserir uma letra por vez para tentar adivinhar a palavra.
4. Se a letra estiver na palavra, ela será revelada na posição correta.
5. Se a letra não estiver na palavra, o jogador perde uma chance.
6. O jogo termina quando o jogador adivinha a palavra ou perde todas as chances.

## Requisitos

- Python 3.x
- Biblioteca `os` (inclusa na biblioteca padrão do Python)
- Biblioteca `time` (inclusa na biblioteca padrão do Python)
- Biblioteca `random` (inclusa na biblioteca padrão do Python)

## Instalação

1. Certifique-se de ter o Python 3.x instalado em seu sistema.
2. Clone este repositório ou baixe o arquivo ZIP e extraia-o.
3. Navegue até o diretório do projeto.

## Funções Principais

encaixar_letra: Atualiza a palavra secreta com a letra escolhida pelo jogador. Substitui os caracteres '_' (underlines) pela letra correta nas posições correspondentes.
desenhar_forca: Desenha a forca com base no número de chances restantes. Existem diferentes estágios da forca que são exibidos conforme o jogador perde chances.

## Dinâmica do Jogo
O jogo começa com uma mensagem de boas-vindas e a escolha aleatória de uma palavra da lista de nomes de animais africanos.
O jogador tem 6 chances para adivinhar a palavra, inserindo uma letra por vez.
O jogo verifica se a letra inserida é válida e se já foi escolhida anteriormente.
Se a letra estiver na palavra, ela é revelada na posição correta. Caso contrário, o jogador perde uma chance.
Quando restam 3 chances, o jogo oferece uma dica ao jogador.
O jogo termina quando o jogador adivinha a palavra ou perde todas as chances.

## Contribuição

Se você quiser contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request. Todas as contribuições são bem-vindas!

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato
Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato.

Divirta-se jogando e aprendendo Python com este jogo da forca!

