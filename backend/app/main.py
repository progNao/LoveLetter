from fastapi import FastAPI
from pydantic import BaseModel
from api.game import Game
from api.result import CardType
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="LoveLetterApp", version="0.0.1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

game = object()

STAB = 0

class Request(BaseModel):
    card_number: int
    is_player: bool
    input_number: int

@app.get('/')
def start():
    global game
    game = Game()
    return display_message(game.start())

@app.get('/player')
def player_turn():
    global game
    message = []
    message.append(game.len_check())
    if game.is_deck:
        message.append(game.player_turn())
        return display_message(message)
    else:
        return display_message(game.end())

@app.post('/player')
def player_play(request: Request):
    global game
    return display_message(game.player_play_card(request.card_number, False, STAB))

@app.post('/player/soldier')
def player_play_soldier(request: Request):
    global game
    return display_message(game.player_play_card(CardType.Soldier, True, request.input_number))

@app.post('/player/clown')
def player_play_clown(request: Request):
    global game
    return display_message(game.player_play_card(CardType.Clown, True, STAB))

@app.post('/player/knight')
def player_play_knight(request: Request):
    global game
    return display_message(game.player_play_card(CardType.Knight, True, STAB))

@app.post('/player/monk')
def player_play_monk(request: Request):
    global game
    return display_message(game.player_play_card(CardType.Monk, True, STAB))

@app.post('/player/magician')
def player_play_magician(request: Request):
    global game
    return display_message(game.player_play_card(CardType.Magician, True, request.input_number))

@app.post('/player/general')
def player_play_general(request: Request):
    global game
    return display_message(game.player_play_card(CardType.General, True, STAB))

@app.post('/player/minister')
def player_play_general(request: Request):
    global game
    return display_message(game.player_play_card(CardType.Minister, True, STAB))

@app.get('/com')
def com_turn():
    global game
    message = []
    message.append(game.len_check())
    if game.is_deck:
        message.append(game.com_turn())
        return display_message(message)
    else:
        return display_message(game.end())

@app.post('/com')
def com_play(request: Request):
    global game
    return display_message(game.com_play_card(request.card_number, False, STAB))

@app.post('/com/soldier')
def com_play_soldier(request: Request):
    global game
    return display_message(game.com_play_card(CardType.Soldier, True, request.input_number))

@app.post('/com/clown')
def com_play_clown(request: Request):
    global game
    return display_message(game.com_play_card(CardType.Clown, True, STAB))

@app.post('/com/knight')
def com_play_knight(request: Request):
    global game
    return display_message(game.com_play_card(CardType.Knight, True, STAB))

@app.post('/com/monk')
def com_play_monk(request: Request):
    global game
    return display_message(game.com_play_card(CardType.Monk, True, STAB))

@app.post('/com/magician')
def com_play_magician(request: Request):
    global game
    return display_message(game.com_play_card(CardType.Magician, True, request.input_number))

@app.post('/com/general')
def com_play_general(request: Request):
    global game
    return display_message(game.com_play_card(CardType.General, True, STAB))

@app.post('/com/minister')
def com_play_general(request: Request):
    global game
    return display_message(game.com_play_card(CardType.Minister, True, STAB))

def display_message(message):
    return message

if __name__=="__main__":
    uvicorn.run("run:app",port=3001, reload=True)