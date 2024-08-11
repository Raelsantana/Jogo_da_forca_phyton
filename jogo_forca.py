import random 

#Definindo a função que irá escolher uma palavra aleatoriamente.
def escolher_palavra():
    palavras = ["python", "programação", "computador", "desenvolvimento", "java", ""]
    return random.choice(palavras)

#Definindo a função que exibirá os estágios da forca.
def exibir_forca(erros):
  estagios = [
    """
    -----------
        ||||
           |
           |
           |
           |
    ===========
    """,
    """
    -----------
        ||||
        o  |
           |
           |
           |
    ===========
    """,
    """
    -----------
        ||||
        o  |
        |  |
           |
           |
    ===========
      """,
    r"""
    -----------
        ||||
        o  |
        |\ |
           |
           |
    ===========
      """,
    r"""
    -----------
        ||||
        o  |
       /|\ |
           |
           |
    ===========
      """,
    r"""
    -----------
       ||||
       o  |
      /|\ |
      /   |
          |
    ===========
      """,
    r"""
    -----------
       ||||
       o  |
      /|\ |
      / \ |
          |
    ===========
      """
  ]
  print(estagios[erros])
  
#Definindo a Função que contém os parâmetros do jogo. 
def jogar_forca():
  palavra = escolher_palavra()
  palavra_adivihada = ['_']*len(palavra)
  tentativas = 0
  max_tentativas = 6
  letras_erradas = 0
  letras_certas = 0
 
  

  print("Bem-vindo ao jogo da forca!\n")
  print("Eu pensei em uma palavra relacionada a computação, tente adivinhar qual é.")
  print("Você terá 6 chances para acertar as letras que existem na palavra que escolhi. E depois poderá dar o seu palpite.\n")

  
  print(' '.join(palavra_adivihada))
  
  #Estrutura de repetição para o funcionamento do jogo.
  while tentativas < max_tentativas:
    palpite_letra = str(input("\nDigite uma letra: "))
    
    if palpite_letra.lower() in palavra:
      print("Você acertou, tente outra letra.\n")
      letras_certas +=1 
      print(f"Acertos: {letras_certas}")
      print(f"Erros: {letras_erradas}\n")
      print(f"Você escolheu a letra ({palpite_letra}), existe um total de:({palavra.count(palpite_letra)}) na palavra que eu pensei.")
      
    else:
      print("Você errou, tente novamente.\n")
      tentativas += 1
      letras_erradas += 1
      exibir_forca(letras_erradas)
      print(f"Acertos: {letras_certas}")
      print(f"Erros:{letras_erradas}\n")

    while tentativas == max_tentativas:
     palpite = input(str("Agora tente acertar a palavra, dê o seu palpite: "))
     if palpite.lower() == palavra.lower():
       print("Você venceu, Parabéns!!")
       break
     else:
       print("Não foi dessa vez.")
       print("Fim de jogo!")
       break
        
      
    
if __name__ == "__main__":
  jogar_forca()
