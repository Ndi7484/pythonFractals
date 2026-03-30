def triangle_fractals(inserting=False):
  import turtle as tr
  tr.tracer(False)
  p=tr.Pen()
  p.hideturtle()
  p.up()
  p.goto(-300,-260)
  p.down()
  def tri(n,p,details=5):
      if n<details:
          for i in range(3):
              p.fd(n)
              p.lt(120)
      else:
          for i in range(3):
              p.fd(n)
              p.lt(120)
              c=p.clone()
              tri(n/2,c,details)
      del p
  # usage - do some
  if inserting:
    print('enter for default..')
    try:
      size=int(input('input size (default: 600) :'))
    except:
      size=600
    try:
      detail=int(input('input details (default: 5) :'))
    except:
      detail=5
  try:
    tri(size,p,detail)
  except:
    tri(600,p)
  tr.update()
  input()