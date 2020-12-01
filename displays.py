G = (0, 255, 0)
Y = (255, 255, 0)
B = (0, 0, 255)
R = (255, 0, 0)
W = (255,255,255)
P = (255,105, 180)
O = (0,0,0)

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
    O, W, W, O, O, O, O, O,
    O, W, W, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, O, O, W, W, O,
    O, W, W, O, O, W, W, O,
    O, W, W, O, O, W, W, O,
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