# Hollow Right Triangle Star Pattern

ctr = 0
row = 0

while(ctr<5):
    ctr += 1
    row += 1
    space = row-1
    if(ctr==1):
        print('*')
    if(ctr>1 and ctr<5):
        print('*' + ' '*space + '*')

    if(ctr==5):
        print('*'*5)