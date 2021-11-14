import turtle, os, pandas
# Get the base path to this folder
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
FONT = ['Calibri', 'normal', 20]

def write_answer(turtle, answer, pos):
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    turtle.dot(10)
    turtle.penup()
    turtle.forward(12)
    turtle.write(answer.item(), FONT)

screen = turtle.Screen()
screen.title("Irish Counties Game")
image = THIS_FOLDER + '/blank_ire_map.gif'
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle(visible=False)
t.penup()

game_loop = True

# Read data using pandas library
data = pandas.read_csv(THIS_FOLDER + "/50_counties.csv")
# Store the list of counties in county_list
county_list = data['county'].to_list()
# Store the users correct answers in a seperate list
correct_answers = []

# Continue the game while there are still answers and quit has not been entered
while len(correct_answers) < len(county_list) and game_loop == True:    
    answer = turtle.textinput("Guess a County", "What's the name of an Irish county?(As Béarla)")
    if answer == 'quit':
        game_loop = False
    elif answer in county_list and not answer in correct_answers:
        correct_answers.append(answer)
        answer_county = data[data.county == answer]
        pos = (float(answer_county['x']), float(answer_county['y']))
        write_answer(t, answer_county.irish_name, pos)

if len(correct_answers) < len(county_list):
    review_list = [county for county in county_list if not county in correct_answers]
    output = pandas.DataFrame(review_list)    
    output.to_csv(THIS_FOLDER + '/revision_list.csv')
screen.exitonclick()

