import turtle as tr
tr.tracer(False)
tr.colormode(255)
p=tr.Pen()
p.speed(0)
p.hideturtle()
p.up()
p.goto(0,-350)
p.down()
p.lt(90)
def tree(n,p,l):
    p.pencolor(0,int(255/l),0)
    if l==1:
        p.fd(n*0.8)
    else:
        p.fd(n*0.8)
        c=p.clone()
        c.lt(30)
        tree(n*0.8,c,l-1)
        c=p.clone()
        c.rt(30)
        tree(n*0.8,c,l-1)
    del p
tree(200,p,15)
tr.update()
tr.done()