from answers import Answer
import turtle as tt
import pandas
import os

screen = tt.Screen()

# image = "fotos/rep_dom_map.gif"
# screen.addshape(image)
# tt.shape(image)
#
# def get_pos(x, y):
#     print(x, y)
#
# tt.onscreenclick(get_pos)

screen.title("Adivina")
screen.setup(width=900, height=700)
photo_name = next(os.walk("fotos"), (None, None, []))[2]
map_name = next(os.walk("states"), (None, None, []))[2]
pais = int(screen.textinput(title="Paises", prompt="Seleciona el Numero del pais que quieres juagar:\n"
                                                   "0. Rep. Dom.\n"
                                                   "1. Estados Unidos"))
image = f"fotos/{photo_name[pais]}"
screen.addshape(image)
tt.shape(image)
data = pandas.read_csv(f"states/{map_name[pais]}")
states = data.state.to_list()
guesses = []
answer = Answer()

while len(guesses) <= len(states):
    answer_guess = screen.textinput(title=f"Aciertos {len(guesses)}/{len(states)}", prompt="Adivina:").title()
    if answer_guess == "Exit":
        break
    if answer_guess not in guesses:
        if answer_guess in states:
            guesses.append(answer_guess)
            row = data[data.state == answer_guess]
            answer.correct(int(row.x), int(row.y), answer_guess)
        else:
            screen.textinput(title="Error", prompt="Repuesta Incorrecta")
    else:
        screen.textinput(title="Repetido", prompt="Repuesta Repetida")

# general csv con los estados que faltaron por adivinar
misses = [miss for miss in states if miss not in guesses]
pandas.DataFrame(misses).to_csv("states_to_learn.csv")
