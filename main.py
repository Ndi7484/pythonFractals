from triangle import triangle_fractals

print('MENU')
print('='*35)
print('add \'a\' on the end to use default option')
print('='*35)
n=1
for i in ['Sierpiński triangle - origin']:
  print(f'{n}. {i}')
  n+=1
pilihan=input('select fractals :')
match pilihan:
  case '1':
    triangle_fractals(inserting=True)
  case '1a':
    triangle_fractals()
  case _:
    print('no such selection')