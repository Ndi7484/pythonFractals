import turtle as tr
# tr.tracer(False)
p=tr.Pen()
def arrowhead(p,n=30,level=0):
    if level==0:
        for i in range(3):
            p.fd(n)
            p.lt(60)
    else:
        arrowhead(p,n,level-1)
        p.rt(120)
        for i in range(3):
            p.fd(n)
            p.rt(60)
        arrowhead(p,n,level-1)
arrowhead(p,30,1)
# tr.update()
tr.done()