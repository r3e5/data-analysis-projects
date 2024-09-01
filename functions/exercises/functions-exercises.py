# Part 1 A -- Make a Line
def make_line(size):
    line = '#'*size
    return line

# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
def make_square(size):
    square = ''
    for side in range(size):
        square +=(make_line(size)) + "\n"
    return square

# Part 1 C -- Make a Rectangle
def make_rectangle(height, width):
    rectangle = ''
    for side in range(height):
        rectangle +=(make_line(width)) + "\n"
    return rectangle

# Part 2 A -- Make a Stairs
def make_downward_stair(height):
    stair = ''
    for step in range(height):
        stair += (make_line(step+1)) + "\n"
    return stair

# Part 2 B -- Make Space-Line 
def make_space_line(numSpaces, numChar):
    for space in range(numSpaces):
        spaces = (" "*numSpaces)

    for line in range(numChar):
        lines = (make_line(numChar))

    space_line = spaces + lines

    return space_line


# Part 2 C -- Make Isosceles Triangle
def make_triangle(height):
    triangle = ''
    for step in range(height):
        triangle += (make_space_line(height - step, 2 * step + 1)) + "\n"
    return triangle

# Part 3 -- Make a Diamond
def make_diamond(height):
    diamond = ''
    diamond = make_triangle(height)
    for step in range(height - 1, -1, -1):
        diamond += (make_space_line(height - step, 2 * step + 1)) + "\n"
    
    return diamond

print(make_diamond(3))





