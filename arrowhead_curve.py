import turtle as tr
# tr.tracer(False)
p=tr.Pen()
# p.speed(1)
def arrowhead(p,n=30,level=0,right=False):
    if level==0:
        for i in range(3):
            p.fd(n)
            p.lt(60) if not right else p.rt(60)
    else:
        for i in range(3):
            arrowhead(p,n,level-1, True if i%2!=0 else False)
            p.rt(120) if not right else p.lt(60)
            for i in range(3):
                p.fd(n)
                p.rt(60) if not right else p.lt(60)
            arrowhead(p,n,level-1, True if i%2!=0 else False)
arrowhead(p,30,1)
# tr.update()
tr.done()