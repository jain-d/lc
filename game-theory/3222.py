# Find the winning player in coin game
from pyutils.colors import Colors

def winning_player(x: int, y: int) -> str:
        players = ("Alice", "Bob")
        first_coin, second_coin = 1, 4
        round = 1
        while True:
            if x < first_coin or y < second_coin:
                break
            x -= first_coin
            y -= second_coin
            round += 1

        return players[round % len(players)]
        


inputs = (((2, 7), "Alice"), ((4, 11), "Bob"), ((1, 3), "Bob"))

for i in inputs:
    #print(i, "\t\t", winning_player(*i[0]))
    if i[1] == winning_player(*i[0]):
        print(f"{Colors.GREEN}PASS")
    else:
        print(f"\n{Colors.RED}FAIL{Colors.RESET}\nfor {i[0]}\n")

