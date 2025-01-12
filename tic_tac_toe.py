import random

def PrintG (listt):
    for i in range (0,3):
        print('\n   ______________________')
        for j in range(0,3):
            print('   |  ',listt[i][j] , end='')
        #print('\n   ______________________')
    print('\n   ______________________')
def Set (lis1 , lis2 , lis3):
    state = True
    while state:
        x = int(input("Where do you want to play? -> "))
        if x in lis1:
            y = lis1.index(x)
            lis1[y] = 'X'
            state = False
        elif x in lis2:
            y = lis2.index(x)
            lis2[y] = 'X'
            state = False
        elif x in lis3:
            y = lis3.index(x)
            lis3[y] = 'X'
            state = False
        else :
            print("************* Wrong Input ************* \n")
def Comp (lis1 , lis2 , lis3):
    t = True
    while t:
        x = random.randrange(1,10)
        if x in lis1:
            y = lis1.index(x)
            lis1[y] = 'O'
            t = False
        elif x in lis2:
            y = lis2.index(x)
            lis2[y] = 'O'
            t = False
        elif x in lis3:
            y = lis3.index(x)
            lis3[y] = 'O'
            t = False

def check (lis):
    if (lis[0][0]==lis[0][1]) and (lis[0][0]==lis[0][2]):
        if lis[0][0] == 'X':
            print("--------->   You Won !!!    <-----------")

        else:
            print("--------->   You Loose !!!    <-----------")
        PrintG(lis)
        return False

    elif (lis[0][0] == lis[1][0]) and (lis[0][0] == lis[2][0]):
        if lis[0][0] == 'X':
            print("--------->   You Won !!!    <-----------")

        else:
            print("--------->   You Loose !!!    <-----------")
        PrintG(lis)
        return False

    elif (lis[0][0] == lis[1][1]) and (lis[0][0] == lis[2][2]):
        if lis[0][0] == 'X':
            print("--------->   You Won !!!    <-----------")

        else:
            print("--------->   You Loose !!!    <-----------")
        PrintG(lis)
        return False

    elif (lis[0][1] == lis[1][1]) and (lis[0][1] == lis[2][1]):
        if lis[0][1] == 'X':
            print("--------->   You Won !!!    <-----------")

        else:
            print("--------->   You Loose !!!    <-----------")
        PrintG(lis)
        return False
    elif (lis[0][2] == lis[1][1]) and (lis[0][2] == lis[2][0]):
        if lis[0][2] == 'X':
            print("--------->   You Won !!!    <-----------")

        else:
            print("--------->   You Loose !!!    <-----------")
        PrintG(lis)
        return False

    elif (lis[0][2] == lis[1][2]) and (lis[0][2] == lis[2][2]):
        if lis[0][2] == 'X':
            print("--------->   You Won !!!    <-----------")

        else:
            print("--------->   You Loose !!!    <-----------")
        PrintG(lis)
        return False

    return True

lis1 = [1 , 2 , 3]
lis2 = [4 , 5 , 6]
lis3 = [7 , 8 , 9]

lis = [ lis1 ,lis2 ,lis3 ]
x =True
while x:
    PrintG(lis)
    Set(lis1, lis2, lis3)
    x = check(lis)
    Comp(lis1, lis2, lis3)

