def sierpinski_arrowhead_curve_fractal(inserting=False):
    import turtle as tr
    tr.tracer(False)
    p = tr.Turtle()
    p.speed(0)
    p.hideturtle()

    def draw_line(length):
        p.forward(length)

    def turn(angle):
        p.left(angle)

    def curve(order, length, angle):
        if order == 0:
            draw_line(length)
        else:
            curve(order - 1, length / 2, -angle)
            turn(angle)
            curve(order - 1, length / 2, angle)
            turn(angle)
            curve(order - 1, length / 2, -angle)

    def sierpinski_arrowhead_curve(order, length):
        if order % 2 == 0:
            curve(order, length, 60)
        else:
            turn(60)
            curve(order, length, -60)

    # Example usage:
    if inserting:
        print('enter to use default value...')
        try:
            N=int(input('input number of N generators (default 8) :'))
        except:
            N=8
        try:
            size=int(input('input size (default 850) :'))
        except:
            size=850
    p.up()
    try:
        p.goto(-400,350 if N%2==0 else -350)
    except:
        p.goto(-400,350)
    p.down()
    try:
        sierpinski_arrowhead_curve(N, size)
    except:
        sierpinski_arrowhead_curve(8, 850)
    tr.update()
    tr.done()