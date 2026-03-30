import math
def _kochcurve(n,p,level=4):
    if level==1:
      c=p.clone()
      c.lt(90)
      c.fd(n/2)
      p.rt(90)
      p.fd(n/2)
    else:
      p.up()
      tmp=n/3
      # left
      c=p.clone()
      c.lt(90)
      c.fd(tmp)
      c.rt(90)
      c.down()
      _kochcurve(tmp,c,level-1)
      # right
      c=p.clone()
      c.rt(90)
      c.fd(tmp)
      c.lt(90)
      c.down()
      _kochcurve(tmp,c,level-1)
      # the middle
      p.fd(math.sqrt((tmp**2)-((tmp*0.5)**2)))
      c=p.clone()
      c.lt(150)
      c.fd(tmp/2)
      c.rt(90)
      c.down()
      _kochcurve(tmp,c,level-1)
      c=p.clone()
      c.rt(150)
      c.fd(tmp/2)
      c.lt(90)
      c.down()
      _kochcurve(tmp,c,level-1)
    del p

def kochcurve_fractal(inserting=False):
  import turtle as tr
  tr.tracer(False)
  p=tr.Pen()
  p.hideturtle()
  p.lt(90)
  # insering
  if inserting:
    print('enter for default value..')
    try:
      size=int(input('input size (default 1300): '))
    except:
      size=1300
    try:
      generator=int(input('input generator (default 6): '))
    except:
      generator=6
  try:
    _kochcurve(size,p,generator)
  except:
    _kochcurve(1300,p,6)
  tr.update()
  input()