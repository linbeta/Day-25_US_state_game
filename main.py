import turtle
import pandas
from state_answer import StateAnswer

screen = turtle.Screen()
screen.title("U.S. States Game")
# screen.screensize(725, 491)
image = "blank_states_img.gif"
# screen.bgpic(image)
screen.addshape(image)
turtle.shape(image)
score = 0
correct_answers = []


# Below shows how to collect all the state coordinate, but it's all provided in the csv file.
# In case you will need it in other projects.
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


# TODO: map all the states names onto the map
all_states = pandas.read_csv("50_states.csv")

# for state in all_states.state:
#     row = all_states[all_states["state"] == state]
#     x_cor = int(row["x"])
#     y_cor = int(row["y"])
#     position = (x_cor, y_cor)
#     state_answer = StateAnswer()
#     state_answer.pup_up(state, position)
#     print(f"state: {state}, location: ({x_cor}, {y_cor})")
note = ""
# TODO: Use a loop to allow the user to keep guessing
while score < 50:
    # TODO: Convert the guess to Title case
    user_input = screen.textinput(title=f"{score}/50 Guess the state",
                                  prompt=f"{note} What's another state's name?                               ").title()
    # TODO: Check if the guess is among the 50 states
    # state_list = []
    # for state in all_states.state:
    #     state_list.append(state)
    # #Update: use pandas to do the above 3 lines of code:
    state_list = all_states.state.to_list()

    if user_input == "Exit":
        missing_states = [state for state in state_list if state not in correct_answers]
        save_file = pandas.DataFrame(missing_states)
        save_file.to_csv("states_to_learn.csv")
        break
    if user_input in state_list and user_input not in correct_answers:
        # TODO: Write correct guesses onto the map
        row = all_states[all_states["state"] == user_input]
        x_cor = int(row["x"])
        y_cor = int(row["y"])
        position = (x_cor, y_cor)
        # Create a state_answer object to pop-up onto the map
        state_answer = StateAnswer()
        state_answer.pup_up(user_input, position)
        # TODO: Keep track of the score
        correct_answers.append(user_input)
        note = ""
        score += 1
    else:
        note = "That's not an U.S. state!\n"

    # TODO: Record the correct guesses in a list
    # what's this? it seems no need to do so

if score == 50:
    state_answer_win = StateAnswer()
    state_answer_win.you_win()
else:
    state_answer_goodbye = StateAnswer()
    state_answer_goodbye.bye()


# turtle.mainloop()
screen.exitonclick()
