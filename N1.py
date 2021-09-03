sala = 1 


print("Você está na sala 1!")
print("Escolha seu caminho:")
print("1 - Caminho vermelho")
print("2 - Caminho preto")
caminho = int(input("Digite o número que conrresponde ao caninho escolhido: "))

if(caminho == 1):
    sala = sala + 1
else:
    sala = sala + 2


while(sala !=9 and sala !=6 and sala!=8):
    print("Você está na sala {}!".format(sala))
    print("Escolha seu caminho:")
    print("1 - Caminho vermelho")
    print("2 - Caminho preto")
    caminho = int(input("Digite o número que conrresponde ao caninho escolhido: "))
        
    if(caminho == 1):
        sala = sala + 1
    else:
        sala = sala + 2
    
    
if(sala == 8 and caminho == 2):
    print("Ah não! Parece que você entrou em um portal desconhecido!")
    print("O portal te levou para uma sala aleatória!")   
else:
    pass   

if(sala == 6):
    print("Você está na sala {}!".format(sala))
    print("O caminho vermelho dessa sala está fehcado, prossiga pelo caminho preto!") 
    print("Escolha seu caminho:")
    print("1 - Caminho vermelho")
    print("2 - Caminho preto")
    caminho = int(input("Digite o número que conrresponde ao caninho escolhido: "))
else:
    pass

if(sala == 9):
    print("Você chegou na sala 9! Essa é a ultima sala!")
    print("Parabéns você ganhou!")
else:
    pass