import numpy as np
from random import randint

xInitial = np.array([
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['G', 'G', 'G'],
        ['G', 'G', 'G'],
        ['G', 'G', 'G'],
        ['R', 'R', 'R'],
        ['R', 'R', 'R'],
        ['R', 'R', 'R'],
        ['B', 'B', 'B'],
        ['B', 'B', 'B'],
        ['B', 'B', 'B'],
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
        ['Y', 'Y', 'Y'],
        ['Y', 'Y', 'Y'],
        ['Y', 'Y', 'Y']

    ]
)


def restore_x():
    x[0:18, 0:3] = xInitial[0:18, 0:3]


def FrontCW():  # action 1
    x[6:9, 0:3] = np.fliplr(x[6:9, 0:3].transpose())
    temp1 = np.array(x[2, 0:3])
    temp2 = np.array(x[9:12, 0])
    temp3 = np.array(x[15, 0:3])
    temp4 = np.array(x[3:6, 2])
    x[2, 0:3] = np.fliplr([temp4])[0]
    x[9:12, 0] = temp1
    x[15, 0:3] = np.fliplr([temp2])[0]
    x[3:6, 2] = temp3


def FrontACW():  # action 2
    FrontCW()
    FrontCW()
    FrontCW()


def UpCW():  # action 3
    x[0:3, 0:3] = np.fliplr(x[0:3, 0:3].transpose())
    temp1 = np.array(x[12, 0:3])
    temp2 = np.array(x[9, 0:3])
    temp3 = np.array(x[6, 0:3])
    temp4 = np.array(x[3, 0:3])
    x[12, 0:3] = temp4
    x[9, 0:3] = temp1
    x[6, 0:3] = temp2
    x[3, 0:3] = temp3


def UpACW():  # acion 4
    UpCW()
    UpCW()
    UpCW()


def DownCW():  # action 5 Front down clock wise
    x[15:18, 0:3] = np.fliplr(x[15:18, 0:3].transpose())
    temp1 = np.array(x[8, 0:3])
    temp2 = np.array(x[11, 0:3])
    temp3 = np.array(x[14, 0:3])
    temp4 = np.array(x[5, 0:3])
    x[8, 0:3] = temp4
    x[11, 0:3] = temp1
    x[14, 0:3] = temp2
    x[5, 0:3] = temp3


def DownACW():  # action 6
    DownCW()
    DownCW()
    DownCW()


def LeftCW():  # action 7

    x[3:6, 0:3] = np.fliplr(x[3:6, 0:3].transpose())
    temp1 = np.array(x[0:3, 0])
    temp2 = np.array(x[6:9, 0])
    temp3 = np.array(x[15:18, 0])
    temp4 = np.array(x[12:15, 2])
    x[0:3, 0] = np.fliplr([temp4])[0]
    x[6:9, 0] = temp1
    x[15:18, 0] = temp2
    x[12:15, 2] = np.fliplr([temp3])[0]


def LeftACW():  # action 8
    LeftCW()
    LeftCW()
    LeftCW()


def RightCW():  # action 9 Front right clock wise

    x[9:12, 0:3] = np.fliplr(x[9:12, 0:3].transpose())
    temp1 = np.array(x[0:3, 2])
    temp2 = np.array(x[12:15, 0])
    temp3 = np.array(x[15:18, 2])
    temp4 = np.array(x[6:9, 2])
    x[0:3, 2] = temp4
    x[12:15, 0] = np.fliplr([temp1])[0]
    x[15:18, 2] = np.fliplr([temp2])[0]
    x[6:9, 2] = temp3


def RightACW():  # action 10
    RightCW()
    RightCW()
    RightCW()


def BackCW():  # action 11 Front  back clock wise

    x[12:15, :] = np.fliplr(x[12:15, :].transpose())
    temp1 = np.array(x[0, 0:3])
    temp2 = np.array(x[3:6, 0])
    temp3 = np.array(x[17, 0:3])
    temp4 = np.array(x[9:12, 2])
    x[0, 0:3] = temp4
    x[3:6, 0] = np.fliplr([temp1])[0]
    x[17, 0:3] = temp2
    x[9:12, 2] = np.fliplr([temp3])[0]


def BackACW():  # action 12
    BackCW()
    BackCW()
    BackCW()


def PrintCube():
    print("             ", x[0, 0:3])
    print("             ", x[1, 0:3])
    print("             ", x[2, 0:3])
    print(x[3, 0:3], x[6, 0:3], x[9, 0:3], x[12, 0:3])
    print(x[4, 0:3], x[7, 0:3], x[10, 0:3], x[13, 0:3])
    print(x[5, 0:3], x[8, 0:3], x[11, 0:3], x[14, 0:3])
    print("             ", x[15, 0:3], " ", " ", " ")
    print("             ", x[16, 0:3], " ", " ", " ")
    print("             ", x[17, 0:3], " ", " ", " ")


def make_move(move, reverse, printCube):
    # move number
    # reverse if 0 original move if 1 reverse of input move
    # printCube 0/1 if 0 dont print else print

    if reverse == 1:
        if move % 2 == 0:
            move = move - 1
        else:
            move = move + 1
    if move == 1:
        FrontCW()
        print("FrontCW")

    if move == 2:
        FrontACW()
        print("FrontACW")

    if move == 3:
        UpCW()
        print("UpCW")

    if move == 4:
        UpACW()
        print("UpACW")

    if move == 5:
        DownCW()
        print("DownCW")

    if move == 6:
        DownACW()
        print("DownACW")

    if move == 7:
        LeftCW()
        print("LeftCW")

    if move == 8:
        LeftACW()
        print("LeftACW")

    if move == 9:
        RightCW()
        print("RightCW")

    if move == 10:
        RightACW()
        print("RightACW")

    if move == 11:
        BackCW()
        print("BackCW")

    if move == 12:
        BackACW()
        print("BackACW")

    if printCube == 1:
        PrintCube()


# intialize Cube x
x = np.array(xInitial)
print("x intialized")
PrintCube()

# pick random moves
total_move = 6
my_randoms = [randint(1, 12) for x in range(total_move)]
print(my_randoms)

# scramble according to moves
for move in my_randoms:
    make_move(move, 0, 0)
PrintCube()
