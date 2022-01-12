# Hollow Square Star pattern

ctr = 0
row_ctr = 0

while(ctr < 5):
    ctr += 1
    if(ctr==1 or ctr==5):
        print('*'*5)
    elif(ctr==2 or ctr == 4):
        print('*'*2+' '+'*'*2)
    else:
        print('*'+' '+'*'+' '+'*')
        