from triangle import triangle_fractal
from square import square_fractal
from koch_curve import kochcurve_fractal
from koch_snowflake import koch_snowflake_fractals
from arrowhead_curve import sierpinski_arrowhead_curve_fractal

print("MENU")
print("=" * 35)
print("add 'a' on the end to use default option")
print("=" * 35)
n = 1
for i in [
    "Sierpiński triangle - origin",
    "Sierpiński square - origin",
    "Koch Curve",
    "Koch Snowflake",
    "Sierpiński Arrowhead Curve Triangle",
    ]:
    print(f"{n}. {i}")
    n += 1
pilihan = input("select fractals :")
match pilihan:
    case "1":
        triangle_fractal(inserting=True)
    case "1a":
        triangle_fractal()
    case "2":
        square_fractal(inserting=True)
    case "2a":
        square_fractal()
    case "3":
        kochcurve_fractal(inserting=True)
    case "3a":
        kochcurve_fractal()
    case "4":
        koch_snowflake_fractals(inserting=True)
    case "4a":
        koch_snowflake_fractals()
    case "4":
        sierpinski_arrowhead_curve_fractal(inserting=True)
    case "4a":
        sierpinski_arrowhead_curve_fractal()
    case _:
        print("no such selection")
