#"it's lit!"-BlockchainBudha 
# HackJam 2023!



def hi_player():

    player = input("Hello! Welcome to TrivCode! What can I call you? ")

    print("Hi, " + player + " what category are you interested in?")

    print("Press 0 for History")

    print("Press 1 for Music")

    print("Press 2 for Shows/Movies")

    print("Press 3 for Art")

    print("Press 4 for Videogames")

    category = int(input("Take your pick:"))
    catnames = ['History','Music','Shows/Movies','Art']

    print("Ah! I see you chose " + catnames[category] + " Are you ready to play?")
    play = input("y/n :")

    return player, category, play

def play_game():




if __name__ == '__main__':
    hi_player()
    if hi_player.play == 'y':
        play_game()