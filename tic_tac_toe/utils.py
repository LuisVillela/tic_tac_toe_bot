"""
[Module] Tic-tac-toe bot utilities.
"""
from ctypes.wintypes import HACCEL
from errno import EFAULT
from random import randint
from re import A, X
from tkinter import E
import requests
from urllib.parse import unquote


API_URL = "http://127.0.0.1:8000"


def is_registry_open() -> bool:
    """
    Checks if registry is available via API.
    """
    try:
        url = "{}/registry".format(API_URL)
        res = requests.get(url)

        if res.text == "true":
            return True
        elif res.text == "false":
            return False

    except:
        return False


def register_user(name: str) -> str:
    """
    Registers user in API game.
    """
    url = "{}/register_player/{}".format(API_URL, name)
    res = requests.post(url)
    player_id = res.text[1]
    return player_id


def is_my_turn(player_id: str) -> bool: 
    """
    Checks if it is our turn via API.
    """
    url = "{}/turn/{}".format(API_URL, player_id)
    res = requests.get(url)
    
    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def read_board() -> list:
    """
    Gets game board via API.
    """
    url = "{}/board".format(API_URL)
    res = requests.get(url)
    board_str = res.text
    board = [
        [board_str[1], board_str[2], board_str[3]], 
        [board_str[4], board_str[5], board_str[6]], 
        [board_str[7], board_str[8], board_str[9]]
    ]

    return board


def decide_move(board: list, player_id: str) -> list[int, int]:
    """
    Decides next move to make. 
    """
    #definir quien es X y quien es O
    rival_id = "X"
    if player_id == "X":
        rival_id = "O"

    #estratejia

#Definir Pociciones del tablero

    A = board[0][0]
    B = board[0][1]
    C = board[0][2]
    D = board[1][0]
    E = board[1][1]
    F = board[1][2]
    G = board[2][0]
    H = board[2][1]
    I = board[2][2]


###ATAQUE

#ATAQUE COLUMNAS

    #ataque tercera columna
    if A == player_id and B == player_id:
        row = 0
        column = 2
    elif D == player_id and E == player_id:
        row = 1
        column = 2
    elif G == player_id and H == player_id:
        row = 2
        column = 2
    #ataque segunda columna 
    elif A == player_id and C == player_id:
        row = 0
        column = 1
    elif D == player_id and F == player_id:
        row = 1
        column = 1
    elif G == player_id and I == player_id:
        row = 2
        column = 1
    #ataque primera columna 
    elif B == player_id and C == player_id:
        row = 0
        column = 0
    elif E  == player_id and F == player_id:
        row = 1
        column = 0
    elif H == player_id and I == player_id:
        row = 2
        column = 0

#ATAQUE ROW

    #ataque tercer row
    if A == player_id and D == player_id:
        row = 2
        column = 0
    elif B == player_id and E == player_id:
        row = 2
        column = 1
    elif C == player_id and F == player_id:
        row = 2
        column = 2
    #ataque segundo row
    if A == player_id and G == player_id:
        row = 1
        column = 0
    elif B == player_id and H == player_id:
        row = 1
        column = 1
    elif C == player_id and I == player_id:
        row = 1
        column = 2
    #ataque preimer row
    if D == player_id and G == player_id:
        row = 0
        column = 0
    elif E == player_id and H == player_id:
        row = 0
        column = 1
    elif F == player_id and I == player_id:
        row = 0
        column = 2

#ATAQUE DIAGONAL

    #ataque Diagonal Izquierda
    if A == player_id and I == player_id:
        row = 1
        column = 1
    #ataque Diagonal Derecha
    elif C == player_id and G == player_id:
        row = 1
        column = 1


###DEFENSA 

#DEFENSA COLUMNAS

    #defensa tercera columna
    if A == rival_id and B == rival_id:
        row = 0
        column = 2
    elif D == rival_id and E == rival_id:
        row = 1
        column = 2
    elif G == rival_id and H == rival_id:
        row = 2
        column = 2
    #defensa segunda columna 
    elif A == rival_id and C == rival_id:
        row = 0
        column = 1
    elif D == rival_id and F == rival_id:
        row = 1
        column = 1
    elif G == rival_id and I == rival_id:
        row = 2
        column = 1
    #defensa primera columna 
    elif B == rival_id and C == rival_id:
        row = 0
        column = 0
    elif E  == rival_id and F == rival_id:
        row = 1
        column = 0
    elif H == rival_id and I == rival_id:
        row = 2
        column = 0

#DEFENSA ROW

    #defensa tercer row
    if A == rival_id and D == rival_id:
        row = 2
        column = 0
    elif B == rival_id and E == rival_id:
        row = 2
        column = 1
    elif C == rival_id and F == rival_id:
        row = 2
        column = 2
    #defensa segundo row
    if A == rival_id and G == rival_id:
        row = 1
        column = 0
    elif B == rival_id and H == rival_id:
        row = 1
        column = 1
    elif C == rival_id and I == rival_id:
        row = 1
        column = 2
    #defensa preimer row
    if D == rival_id and G == rival_id:
        row = 0
        column = 0
    elif E == rival_id and H == rival_id:
        row = 0
        column = 1
    elif F == rival_id and I == rival_id:
        row = 0
        column = 2

#DEFENSA DIAGONAL

    #Diagonal Izquierda
    if A == rival_id and I == rival_id:
        row = 1
        column = 1
    #Diagonal Derecha
    elif C == rival_id and G == rival_id:
        row = 1
        column = 1

#ATAQUE (Primera jugada)
    if E == "-":
        row = 1
        column = 1
        return [row, column]
    elif A == "-":
        row = 0
        column = 0
        return [row, column]
    elif C == "-":
        row = 0
        column = 2
        return [row, column]

    row = randint(0, 2)
    column = randint(0, 2)
    return [row, column]

#Codigo antiguo, MINIMAX ALGORITHM

    # def_init_(self, letter):
    #     super()._init_(letter)

    # def get_move(self, game):
    #     if len(game.available_moves()) == 9:
    #         square = random.choice(game.available_moves())
    #     else:
    #         square = self.minimax(game, self.letter)["position"]
    #     return [square]

    # def minimax(self, state, player):
    #     max_player = self.letter
    #     other_player = "0" if player == "X" else "X"

    #     #first we want to check if the previous move is the winner
    #     if state.current_winner == other_player
    #         return {"position": None, "score": 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares()+1)}
    #     elif not state.empty_squares():
    #         return {"position": None, "score": 0}

    #     if player == max_player:
    #         best = {"position": None, "score": -math.inf}
    #     else:
    #         best = {"position": None, "score": math.inf}
    #     for possible_move in state.available_moves():
    #         state.make_move(possible_move, player)
    #         sim_score = self.minimax(state, other_player) #simulate a game after making that move

    #         #undo move
    #         state.board[possible_move] = " "
    #         state.current_winner = None
    #         sim_score["position"] = possible_move # this represents the move optimal next move

    #         if player == max_player:
    #             if sim_score["score"] > best["score"]:
    #                 best = sim_score

    #         else:
    #             if sim_score["score"] < best["score"]:
    #                 best = sim_score
        
    #     return best




def validate_move(board: list, move: list) -> bool:
    """
    Checks if the desired next move hits an empty position.
    """
    row, col = move[0], move[1]

    if board[row][col] == "-":
        return True

    return False


def send_move(player_id: str, move: list) -> None:
    """
    Sends move to API.
    """
    row, col = move[0], move[1]
    url = "{}/move/{}/{}/{}".format(API_URL, player_id, row, col)
    res = requests.post(url)
    return None


def does_game_continue() -> bool:
    """
    Checks if the current match continues via API.
    """
    url = "{}/continue".format(API_URL)
    res = requests.get(url)

    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def print_board(board: list) -> None:
    '''
    Prints the baord in console to watch the game.
    '''
    print("\nCurrent board: \n")
    print(board[0][0], "|", board[0][1], "|", board[0][2])
    print("----------")
    print(board[1][0], "|", board[1][1], "|", board[1][2])
    print("----------")
    print(board[2][0], "|", board[2][1], "|", board[2][2], "\n")
