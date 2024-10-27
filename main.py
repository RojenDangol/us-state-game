import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
game_on = True
data = pd.read_csv("50_states.csv")
states = data["state"].to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_states = screen.textinput(title=f"{len(guessed_state)}/50 State", prompt="What's another state's name?").title()

    if answer_states == "Exit":
        not_guessed_states = [state for state in states if state not in guessed_state]
        # not_guessed_states = []
        # for state in states:
        #     if state not in guessed_state:
        #         not_guessed_states.append(state)
        new_data = pd.DataFrame(not_guessed_states)
        new_data.to_csv("states_not_guessed.csv")
        break
    if answer_states in states:
        guessed_state.append(answer_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_states]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        t.goto(x_cor, y_cor)
        t.write(answer_states)
        # t.write(state_data.state.item())

# screen.exitonclick()
