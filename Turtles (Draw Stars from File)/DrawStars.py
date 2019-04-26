
import turtle

# turtle.tracer makes turtle happen instantly
turtle.tracer(0)


def read_coords(file):
    '''Parses the data to the correct dictionaries.'''

    # list of dictionaries
    dict1 = {}
    dict2 = {}
    dict3 = {}
    # for loop that parses everything
    for i in file:
        line = i.strip('\n')
        line = line.split(" ")
        dict1.update({float(line[5]): (float(line[0]), float(line[1]))})
        dict2.update({float(line[5]): float(line[3])})
        if len(line) >= 6:
            dict3.update({float(line[3]): (line[4])})
        else:
            continue
    # turns our dictionaries into one large tuple of dictionaries.
    tuple = (dict1, dict2, dict3)
    # returns it to the main function so it can be stored.
    return tuple


def plot_plain_stars(picture_size, coordinates_dict):
    '''plots stars by coordinates only.'''

    # list of x and y coordinates.
    x_list = []
    y_list = []

    '''loops through all the x and y values and
    puts them in their correct lists.'''
    for keys in coordinates_dict[0]:
        x_list.append(coordinates_dict[0][keys][0])
        y_list.append(coordinates_dict[0][keys][1])

    # resized x and y values list.
    resize_x = []
    resize_y = []

    '''loops through the original x and y values
    then adds them to the resized value list.'''
    for x, y in zip(x_list, y_list):
        resize_x.append((picture_size * x / 2))
        resize_y.append((picture_size * y / 2))

    # sets up turtle settings
    turtle.setup(picture_size + 50, picture_size + 50)
    turtle.bgcolor("black")
    turtle.pencolor("white")
    turtle.fillcolor("white")

    # loops through our x and y lists and plots them via turtle graphics.
    for x, y in zip(resize_x, resize_y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(2)
        turtle.right(90)
        turtle.forward(2)
        turtle.right(90)
        turtle.forward(2)
        turtle.right(90)
        turtle.forward(2)
        turtle.right(90)
        turtle.end_fill()
        turtle.penup()
    turtle.exitonclick()


def plot_by_magnitude(picture_size, coordinates_dict, magnitudes_dict):
    '''Plots Stars by magnitudes'''

    # x, y, and magnitude lists
    x_list = []
    y_list = []
    mag_list = []

    ''' loops through the parameters and adds the
    correct objects too the list, with math size done.'''
    for keys, m in zip(coordinates_dict, magnitudes_dict):
        x_list.append(((coordinates_dict[keys][0]) * picture_size) / 2)
        y_list.append(((coordinates_dict[keys][1]) * picture_size) / 2)
        mag_list.append(round(10 / (float(magnitudes_dict[m]) + 2)))

    # Sets up turtle graphics settings.
    turtle.setup(picture_size, picture_size)
    turtle.bgcolor("black")
    turtle.pencolor("white")
    turtle.fillcolor("white")

    # loops through x, y, and magnitude list and plots the data.
    for x, y, m in zip(x_list, y_list, mag_list):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(m)
        turtle.right(90)
        turtle.forward(m)
        turtle.right(90)
        turtle.forward(m)
        turtle.right(90)
        turtle.forward(m)
        turtle.right(90)
        turtle.end_fill()
        turtle.penup()
    turtle.exitonclick()


def main():
    '''Main Function'''
    stars = open("stars.txt", "r")
    tuple = (read_coords(stars))
    # plot_plain_stars(500, tuple)
    plot_by_magnitude(700, tuple[0], tuple[2])


# Calls main
if __name__ == '__main__':
    main()
