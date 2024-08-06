import sys

def gameStart(): 
    print("                       Welcome ChessPy")
    print(r"""
                                                        _:_
                                                        '-.-'
                                            ()      __.'.__
                                            .-:--:-.  |_______|
                                    ()      \____/    \=====/
                                    /\      {====}     )___(
                        (\=,      //\\      )__(     /_____\
        __    |'-'-'|  //  .\    (    )    /____\     |   |
        /  \   |_____| (( \_  \    )__(      |  |      |   |
        \__/    |===|   ))  `\_)  /____\     |  |      |   |
        /____\   |   |  (/     \    |  |      |  |      |   |
        |  |    |   |   | _.-'|    |  |      |  |      |   |
        |__|    )___(    )___(    /____\    /____\    /_____\
        (====)  (=====)  (=====)  (======)  (======)  (=======)
        }===={  }====={  }====={  }======{  }======{  }======={
    (______)(_______)(_______)(________)(________)(_________)
    """)
    while True:
        print("Choose the type of game:")
        print("Player vs Player [1]")
        print("Player vs AI [2]")
        print("Exit [0]")

        choose = input()

        if choose == "1":
            print("Player vs Player choosed! ")
        elif choose == "2":
            print("Player vs AI choosed!")
        elif choose == "3":
            exit()
        else: 
            print("\nThis option does not exist, try again.\n")

if __name__ == '__main__':
    gameStart()


