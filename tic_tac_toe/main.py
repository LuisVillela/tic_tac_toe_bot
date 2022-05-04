"""
Main module
"""

import Utils
import time

def main():
    print("hola")

    NAME = "Luis"
    player_id = utils.register(NAME)
    print(player_id)

    my_turn = utils.is_my_turn(player_id)

    while not my_turn:
        print("zzz...")
        time.sleep(3)
        my_turn = utils.is_my_turn(player_id)

    print("its my turn, continue in game...")

    print(my_turn)

if _name_ == "_main_":
    main()
    