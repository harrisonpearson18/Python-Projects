# Hollow Rhombus Star pattern

ctr = 0
row = 5
spaces = 3

while(ctr<5):
    ctr += 1
    row -= 1
    if(ctr==1 or ctr==5):
        print(' '*row+'*'*5)
    else:
        print(' '*row + '*' + ' '*spaces + '*')
        