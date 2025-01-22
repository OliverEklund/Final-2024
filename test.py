

turn = 0
input("Ready to play?: ")

while True:
    print(f"Turn: {turn}")

    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]

    print(*board,sep='\n')

    turn = turn + 1
    input("next turn?: ")