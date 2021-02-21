#THIS PROGRAM WAS MADE FOR UOFT HACKS VIII (FEB 19 - FEB 21, 2021)
#DAVID, DOS SANTOS; JAEDEN, ROTONDO
#DESCRIPTION OF PROGRAM: A SERIES OF QUESTIONS WILL BE POSED IN THE TERMINAL, THEY CAN BE ANSWERED BASED ON USER PREFERENCE. THE OUTPUT WILL BE A FRACTAL IMAGE GENERATED THROUGH PYTHON'S TURTLE MODULE.

#INTRODUCTION DISPLAYED IN TERMINAL

print('*'*40)
print('Welcome to Fractal Generator!')
print('*'*40)
print('')
answer1 = input('Would you like to add a polygon centered in your fractal? (If so enter Y or N): ')

#INTERPRETING USER RESPONSES TO QUESTIONS

if answer1 == "Y":
    x = float(input('How many sides does your polygon have?: '))
    print('')
    y = input('What colour fade would you like on your polygons? \n(Choose from "Red", "Green", and "Blue", ex."Blue to Red"): ')
    print('')
    y = y.upper()
else: pass
answer2 = input('Would you like fractal trees in your image? (Answer Y or N): ')
if answer2 == 'Y':
    theta = float(input('What angle would you like in your fractal trees? '))
    print('')
    z = input('\nWhat colour would you like your three fractal trees to be?\n(ex. Green, Blue, Red; Green, Green, Green): ')
    z = z.upper()
else: z = ''
if answer1 == 'Y' or answer2 == 'Y':
    k = float(input('\nWhat thickness would you like the fractal lines to be? Scale(1-10): '))
    n = float(input('\nWhat depth would you like the fractal to be? Scale(1-10): '))
else: 
    print('Sorry, there is no fractal to render!')
    
if answer1 == 'Y' or answer2 == 'Y':   
    
#IMPORT TURTLE, SET BASIC TURTLE SETTINGS

    import turtle
    t = turtle.Turtle()
    t.hideturtle()
    turtle.colormode(1)
    turtle.bgcolor(0.5,0.5,0.5)
    turtle.tracer(False)
    t.speed(0)
    t.setheading(90)
    t.pensize(k/1.5)
    a = 0
    b = 200    
    
    #DEFINE THE RECURSIVE FUNCTIONS THAT WILL BE USED TO DRAW THE FRACTALS, THEY VARY BY COLOR
    
    def y_fractal_green(l):
            if (l < n):
                return
            else: 
                    t.down()
                    t.pencolor(0,0.8**l,0)
                    t.forward(l)
                    t.left(theta)
                    y_fractal_green(3*l/4)
                    t.right(2*theta)
                    y_fractal_green(3*l/4)
                    t.left(theta)
                    t.up()
                    t.backward(l)
    
    def y_fractal_blue(l):
            if (l < n):
                return
            else: 
                    t.down()
                    t.pencolor(0,0,0.8**l)
                    t.forward(l)
                    t.left(theta)
                    y_fractal_blue(3*l/4)
                    t.right(2*theta)
                    y_fractal_blue(3*l/4)
                    t.left(theta)
                    t.up()
                    t.backward(l)
                    
    def y_fractal_red(l):
            if (l < n):
                return
            else: 
                    t.down()
                    t.pencolor(0.9**l,0,0)
                    t.forward(l)
                    t.left(theta)
                    y_fractal_red(3*l/4)
                    t.right(2*theta)
                    y_fractal_red(3*l/4)
                    t.left(theta)
                    t.up()
                    t.backward(l)
                    
    def hspiral_rg(l,x):
            if (l > b):return
            else:
                    t.down()
                    t.pencolor(0.9**l,1-0.8**l,0)
                    t.forward(l)
                    t.right(180 - (x-2)*180/x)
                    t.backward((a/0.75)*l)
                    t.forward((0.5/0.75)*l)
                    t.up()
                    hspiral_rg(l*1.05,x)
    
    def hspiral_rb(l,x):
            if (l > b):return
            else:
                    t.down()
                    t.pencolor(0.9**l,0,1-0.9**l)
                    t.forward(l)
                    t.right(180 - (x-2)*180/x)
                    t.backward((a/0.75)*l)
                    t.forward((0.5/0.75)*l)
                    t.up()
                    hspiral_rb(l*1.05,x)
            
    def hspiral_br(l,x):
            if (l > b):return
            else:
                    t.down()
                    t.pencolor(1-0.9**l,0,0.9**l)
                    t.forward(l)
                    t.right(180 - (x-2)*180/x)
                    t.backward((a/0.75)*l)
                    t.forward((0.5/0.75)*l)
                    t.up()
                    hspiral_br(l*1.05,x)
            
    def hspiral_bg(l,x):
            if (l > b):return
            else:
                    t.down()
                    t.pencolor(0,1-0.9**l,0.9**l)
                    t.forward(l)
                    t.right(180 - (x-2)*180/x)
                    t.backward((a/0.75)*l)
                    t.forward((0.5/0.75)*l)
                    t.up()
                    hspiral_bg(l*1.05,x)
            
    def hspiral_gr(l,x):
            if (l > b):return
            else:
                    t.down()
                    t.pencolor(1-0.9**l,0.9**l,0)
                    t.forward(l)
                    t.right(180 - (x-2)*180/x)
                    t.backward((a/0.75)*l)
                    t.forward((0.5/0.75)*l)
                    t.up()
                    hspiral_gr(l*1.05,x)
            
    def hspiral_gb(l,x):
            if (l > b):return
            else:
                    t.down()
                    t.pencolor(0,0.9**l,1 - 0.9**l)
                    t.forward(l)
                    t.right(180 - (x-2)*180/x)
                    t.backward((a/0.75)*l)
                    t.forward((0.5/0.75)*l)
                    t.up()
                    hspiral_gb(l*1.05,x)
                    
#INTERPRETING USER REPSONSES TO FRACTAL TREE COLOURS
    
    if z.count('GREEN') == 3: 
        y_fractal_green(100); t.setheading(-30); y_fractal_green(100); t.setheading(210); y_fractal_green(100)
    
    elif z.count('BLUE') == 3: 
            y_fractal_blue(100); t.setheading(-30); y_fractal_blue(100); t.setheading(210); y_fractal_blue(100)
    
    elif z.count('RED') == 3: 
            y_fractal_red(100); t.setheading(-30); y_fractal_red(100); t.setheading(210); y_fractal_red(100)
    
    elif z.count('RED') == 1 and z.count('BLUE') == 1 and z.count('GREEN') == 1:
            y_fractal_green(100); t.setheading(-30); y_fractal_blue(100); t.setheading(210); y_fractal_red(100)
    
    elif z.count('RED') == 2 and z.count('GREEN') == 1:
            y_fractal_red(100); t.setheading(-30); y_fractal_green(100); t.setheading(210); y_fractal_red(100)
    
    elif z.count('RED') == 2 and z.count('BLUE') == 1:
            y_fractal_red(100); t.setheading(-30); y_fractal_blue(100); t.setheading(210); y_fractal_red(100)
    
    elif z.count('BLUE') == 2 and z.count('GREEN') == 1:
            y_fractal_blue(100); t.setheading(-30); y_fractal_green(100); t.setheading(210); y_fractal_blue(100)
    
    elif z.count('BLUE') == 2 and z.count('RED') == 1:
            y_fractal_blue(100); t.setheading(-30); y_fractal_red(100); t.setheading(210); y_fractal_blue(100)
    
    elif z.count('GREEN') == 2 and z.count('RED') == 1:
            y_fractal_green(100); t.setheading(-30); y_fractal_red(100); t.setheading(210); y_fractal_green(100)
    
    elif z.count('GREEN') == 2 and z.count('BLUE') == 1:
            y_fractal_green(100); t.setheading(-30); y_fractal_blue(100); t.setheading(210); y_fractal_green(100)
    else: pass
    
    t.setheading(0)
    
#INTERPRETING USER RESPONSES TO SPIRAL FADE COLORS
    
    if answer1 == "Y":
        if y == 'RED TO GREEN': 
            hspiral_rg(1,x)
    
        elif y == 'RED TO BLUE': 
            hspiral_rb(1,x)
    
        elif y == 'BLUE TO RED': 
            hspiral_br(1,x)
    
        elif y == 'BLUE TO GREEN': 
            hspiral_bg(1,x)
    
        elif y == 'GREEN TO RED': 
            hspiral_gr(1,x)
    
        elif y == 'GREEN TO BLUE': 
            hspiral_gb(1,x)
            
        else: pass
        
    else: pass
    turtle.done()

else: pass
            