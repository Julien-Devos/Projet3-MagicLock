G = (0, 255, 0)
Y = (255, 255, 0)
B = (0, 0, 255)
R = (255, 0, 0)
W = (255,255,255)
P = (255,105, 180)
O = (0,0,0)

""" 
    C'est dans ce fichier que se trouve toutes les différentes
    listes de pixels ou logos qui sont utilisés durant le fonctionnement
    du MagicLock. Ce fichier est importé dans MagicLock.py  
"""

screen_off = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]

correct = [
    O, O, O, O, O, O, O, G,
    O, O, O, O, O, O, G, G,
    O, O, O, O, O, G, G, G,
    G, O, O, O, G, G, G, O,
    G, G, O, G, G, G, O, O,
    G, G, G, G, G, O, O, O,
    O, G, G, G, O, O, O, O,
    O, O, G, O, O, O, O, O,
    ]

cancel = [
    R, R, O, O, O, O, R, R,
    R, R, R, O, O, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    O, O, R, R, R, R, O, O,
    O, R, R, R, R, R, R, O,
    R, R, R, O, O, R, R, R,
    R, R, O, O, O, O, R, R,
    ]

save = [
    O, O, G, G, G, G, O, O,
    O, G, G, G, G, G, G, O,
    O, G, G, O, O, O, O, O,
    O, G, G, G, G, O, O, O,
    O, O, G, G, G, G, O, O,
    O, O, O, O, O, G, G, O,
    O, G, G, G, G, G, G, O,
    O, O, G, G, G, G, O, O,
    ]

num_0 = [
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, O, O, W, W, O,
    O, W, W, O, O, W, W, O,
    O, W, W, O, O, W, W, O,
    O, W, W, O, O, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    ]

num_1 = [
    O, O, O, W, W, W, O, O,
    O, O, W, W, W, W, O, O,
    O, W, W, W, W, W, O, O,
    O, W, W, W, W, W, O, O,
    O, O, O, W, W, W, O, O,
    O, O, O, W, W, W, O, O,
    O, O, O, W, W, W, O, O,
    O, O, O, W, W, W, O, O,
    ]

num_2 = [
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    ]

num_3 = [
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    ]

num_4 = [
    O, O, O, O, W, W, O, O,
    O, O, O, W, W, W, O, O,
    O, O, W, W, W, W, O, O,
    O, W, W, O, W, W, O, O,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    O, O, O, O, W, W, O, O,
    O, O, O, O, W, W, O, O,
    ]

num_5 = [
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    ]

num_6 = [
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, O, O, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    ]

num_7 = [
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, W, W, O,
    O, O, O, O, W, W, W, O,
    O, O, O, W, W, W, O, O,
    O, O, W, W, W, O, O, O,
    O, W, W, W, O, O, O, O,
    O, W, W, O, O, O, O, O,
    ]

num_8 = [
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, O, O, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, O, O, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    ]

num_9 = [
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, O, O, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    ]

delete = [
    O, O, R, R, R, R, O, O,
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, W, W, W, W, W, W, R,
    R, W, W, W, W, W, W, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]

floppy_disk = [
    B, B, B, B, B, B, B, O,
    B, B, O, O, O, O, B, B,
    B, B, O, O, O, O, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, W, W, W, W, B, B,
    B, B, W, W, W, W, B, B,
    B, B, W, W, W, W, B, B,
    ]

decode = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, Y, Y, O, O, O, O, O,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, O, Y, O, Y,
    O, Y, Y, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]

view = [
    W, O, O, O, O, O, O, W,
    W, W, O, O, O, O, W, W,
    W, W, W, O, O, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, O, W, W, O, W, W,
    W, W, O, O, O, O, W, W,
    W, W, O, O, O, O, W, W,
    W, W, O, O, O, O, W, W,
    ]

code = [
    O, G, G, G, O, O, O, O,
    O, O, Y, G, O, Y, O, G,
    O, Y, O, G, O, O, Y, G,
    O, O, O, O, O, G, G, G,
    G, G, G, O, O, O, O, O,
    G, Y, O, O, G, O, Y, O,
    G, O, Y, O, G, Y, O, O,
    O, O, O, O, G, G, G, O,
    ]