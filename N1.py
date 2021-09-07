import random

def Path(dungeon, choice): 
    if(choice == 1 and dungeon != 6):
        return dungeon + 1
    elif(choice == 2 and dungeon != 8):
        return dungeon + 2
    elif(choice == 2 and dungeon == 8):
        print("Você entrou no portal e caiu em uma sala aleatória!")
        return random.randrange(1, 6)
    else:
        print("Esta opção é inválida!")
        return dungeon

def Room(dungeon):
    if(dungeon == 6):
        print("Você está na sala {}" .format(dungeon))
        print("Existe somente um caminho")
        print("[2] - Caminho Preto")
    else:
        print("Você está na sala {}" .format(dungeon))
        print("Escolha seu caminho")
        print("[1] - Caminho Vermelho")
        print("[2] - Caminho Preto")

dungeon = 1 
i = 0

while(dungeon != 9):
    Room(dungeon)
    choice = int(input("Digite o numero do seu caminho: "))
    print()
    dungeon = Path(dungeon, choice)
    i += 1

if(dungeon == 9 and i < 7):
    print("Parabéns você ganhou! Encontrou a sala 9 antes de esgotar os movimentos!")
    print("  ___________")
    print(" '._==_==_=_.'")
    print(" .-\:      /-.")
    print("| (|:.     |) |")
    print(" '-|:.     |-'")
    print("   \::.    /")
    print("    '::. .'")
    print("      ) (")
    print("    _.' '._")
    print("   '''''''''")
else:
    print("Você perdeu! Chegou a sala 9, porém usou mais de 6 movimentos")
