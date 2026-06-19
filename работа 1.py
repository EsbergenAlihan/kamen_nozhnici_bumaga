import random
a="камень"
b="ножницы"
c="бумага"
game=[a,b,c]
def getcomputerchoice():
    return random.choice(game)
def determinewinner(player,bot):
    if player == bot:
        print("ничья")
        return 0, 0
    elif(player == a and bot == b) or\
             (player == b and bot == c) or\
             (player == c and bot == a):
        print ("вы выиграли")
        return 1, 0
    else:
        print("бот выиграл раунд")
        return 0, 1
def main():
    player_score=0
    bot_score=0
    while player_score < 3 and bot_score < 3:
        print(f"текущий счет: {player_score} - {bot_score} бот")
        player = input("ваш выбор:").lower()
        bot = getcomputerchoice()
        print(f"бот выбрал {bot}")
        d, e = determinewinner(player, bot)
        player_score += d
        bot_score += e
    if player_score == 3:
        print(f"вы победили, ваш счет: {player_score}")
    else:
        print(f"победил бот со счетом {bot_score}")
print("добро пожаловать в игру камень ножницы бумага")
print("играем до трех побед")
main()
