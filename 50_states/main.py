import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_click_cor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_click_cor)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()


guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 correct", prompt="What's another state's name?")
    answer = answer.title()

    if answer == "Exit":
        missed = state_list
        for state in missed:
            if state in guessed_states:
                missed.remove(state)
        new_data = pandas.DataFrame(missed)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data.state == answer]
        t.goto(int(state.x), int(state.y))
        t.write(arg=answer)
        guessed_states.append(answer)




