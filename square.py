def square_fractal(inserting=False):
  import turtle as tr
  tr.tracer(False)
  p=tr.Pen()
  p.hideturtle()
  p.up()
  p.goto(-300,-260)
  p.down()
  def sqr(n,p,details=5):
      if n<details:
        for i in range(4):
          p.fd(n)
          p.lt(90)
      else:
        for _ in range(4):
          for i in range(3):
            c=p.clone()
            sqr(n/3,c,details)
            p.fd(n/3)
          p.lt(90)
      del p
          
  # usage - do some
  if inserting:
    print('enter for default value..')
    try:
      size=int(input('input size (default 500): '))
    except:
      size=500
    try:
      detail=int(input('input detail (default 5): '))
    except:
      detail=500
  try:
    sqr(size,p,detail)
  except:
    sqr(500,p)
  tr.update()
  input()