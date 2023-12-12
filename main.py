import turtle
import pandas

screen = turtle.Screen() #Turtle Fenster initialisieren
screen.title("US States Game") #Titel zum Screen vergeben
image = "blank_states_img.gif"
screen.addshape(image) #hinzufügen des Bildes als Form
turtle.shape(image) #Screen lädt dadurch das Bild

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's name?").title()


    data = pandas.read_csv("50_states.csv")
    states = data["state"]

    if answer_state == "Exit":
        break

    for state in states:
        if answer_state == state:
            guessed_state.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            state_data = data[data["state"] == state]
            t.penup()
            t.goto(float(state_data.x.iloc[0]), float(state_data.y.iloc[0]))
            t.pendown()
            t.write(answer_state)





