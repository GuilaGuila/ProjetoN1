import random

def Path(dungeon, choice): 
    while(choice == 1 or choice == 2):
        if(choice == 1 and dungeon != 6):
            return dungeon + 1
        elif(choice == 2 and dungeon == 8):
            print("Você entrou no portal e caiu em uma sala aleatória!")
            return random.randrange(1, 6)
        else:
            return dungeon + 2
    print("Opção Inválida")
    return dungeon

def Room(dungeon):
    while(dungeon != 6):
        print("Você está na sala {}" .format(dungeon))
        print("Escolha seu caminho")
        print("[1] - Caminho Vermelho")
        print("[2] - Caminho Preto")
        return True

    print("Você está na sala {}" .format(dungeon))
    print("Existe somente um caminho")
    print("[2] - Caminho Preto")

dungeon = 1 
i = 0

while(dungeon != 9 and i < 7):
    Room(dungeon)
    choice = int(input())
    print()
    dungeon = Path(dungeon, choice)
    i += 1

if(dungeon == 9):
    print("Parabéns você ganhou! Encontrou a sala 9 antes de esgotar os movimentos!")
    print("Voce usou {} jogadas".format(i))
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
    print("Você perdeu! Usou mais de 6 jogadas!")
