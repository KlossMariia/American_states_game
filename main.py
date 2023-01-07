import turtle
import pandas

# this function checks if state, which user input, exists
# it takes all state's names from file 50_states (variable "data")
def check_the_answer(answer):
    search = data['state'].str.count(answer)
    search = search.sum()
    if search == 1:
        return True
    else:
        return False

# this function generates list of states, which user hasn't guessed yet
# it prevents from getting points for guessing the same state over and over again
def generate_csv():
    all_states = data.state.tolist()
    missing_states = [n for n in all_states if n not in guessed_states]
    list_of_missing_states = pandas.DataFrame(missing_states)
    list_of_missing_states.to_csv("missing_states.csv")

# this function checks if state has been guessed already
def check_if_guessed(state):
    for item in guessed_states:
        if item == state:
            return True

# this function gets coordinates of state from 50_states file
def get_coordinates(answer):
    state_data = data[data.state == answer]
    x = int(state_data.x)
    y = int(state_data.y)
    return x, y


# Creating a screen
screen = turtle.Screen()
screen.title("U.S. Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

caption = turtle.Turtle()
caption.hideturtle()
caption.penup()
# Reading csv
data = pandas.read_csv("50_states.csv")

game_is_on = True
point = 0
guessed_states = []
generate_csv()
while game_is_on:
    # checks if user have already guessed all states
    if point == 50:
        caption.goto(0, 0)
        caption.write("You won!", False, "center", ('Times New Roman', 40, 'normal'))
        game_is_on = False
    else:
        answer_state = screen.textinput(title=f"{point}/50 States correct", prompt="What's the next state you know?").title()
        if answer_state == "Exit":
            break
            # if input state exists and it hasn't been guessed already, user gets point and state's name gets placed on the map
        if check_the_answer(answer_state) and not check_if_guessed(answer_state):
            xcor, ycor = get_coordinates(answer_state)
            caption.goto(x=xcor, y=ycor)
            caption.write(f"{answer_state}", move=False, align="center", font = ('Times New Roman', 14, 'normal'))
            point += 1
            guessed_states.append(answer_state)

generate_csv()
screen.exitonclick()
