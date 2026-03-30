def koch_snowflake_fractals(inserting=False):
    from koch_curve import _kochcurve
    import math
    import turtle as tr
    tr.tracer(False)
    p=tr.Pen()
    p.hideturtle()
    p.lt(90)
    def koch_snowflake(p,size=550,level=5):
        tmp=math.sqrt((size**2)-((size*0.5)**2))/3
        a=p.clone()
        a.up()
        a.fd(tmp)
        a.down()
        _kochcurve(size,a,level)
        del a
        a=p.clone()
        a.up()
        a.lt(120)
        a.fd(tmp)
        a.down()
        _kochcurve(size,a,level)
        del a
        a=p.clone()
        a.up()
        a.rt(120)
        a.fd(tmp)
        a.down()
        _kochcurve(size,a,level)
        del a
    if inserting:
        print('enter for default value...')
        try:
            size=int(input('input size (default 550): '))
        except:
            size=550
        try:
            generator=int(input('input generator (default 5): '))
        except:
            generator=5
    try:
        koch_snowflake(p,size,generator)
    except:
        koch_snowflake(p)
    tr.update()
    input()