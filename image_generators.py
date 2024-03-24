from PIL import Image
from random import randint
from math import sin, cos, pi
import math
import numpy as np

for i in range(800, 900):
    
    size_x = 100
    size_y = 100
    
    image = Image.new(mode="RGB", size=(size_x, size_y), color = "black")
    
    r = 0
    g = 128 + (i * 40)
    b = 255 + (i * 80)

    for x in range(size_x):
        for y in range(size_y):
            R = int((np.sqrt(abs((x - (size_x // 2)) ** (i * 0.001) *  + (y - (size_x // 2)) ** (i * 0.001))) % 1) * r)
            if R > 255: R = 511 - R
            G = int((np.sqrt(abs((x - (size_x // 2)) ** (i * 0.001) + (y - (size_x // 2)) ** (i * 0.001))) % 1) * g)
            if G > 255: G = 511 - G
            B = int((np.sqrt(abs((x - (size_x // 2)) ** (i * 0.001) + (y - (size_x // 2)) ** (i * 0.001))) % 1) * b)
            if B > 255: B = 511 - B
            image.putpixel((x, y), (R, G, B))
    
    print(i, end=" ")
    
    image.save(f"image{i - 800}.png", format="png")

ex = 2
ey = 2

for i in range(1200):
    
    size_x = 500
    size_y = 500
    
    image = Image.new(mode="RGB", size=(size_x, size_y), color = "black")
    
    R = 0
    G = int(sin(i * 0.04) * 127 + 127)
    B = int(cos(i * 0.04) * 127 + 127)
    
    if i % 200 in range(0, 50): ex += 0.01
    if i % 200 in range(50, 100): ex -= 0.01
    if i % 200 in range(100, 150): ey += 0.01
    if i % 200 in range(150, 200): ey -= 0.01

    for x in range(-size_x//2, size_y//2):
        for y in range(-size_y//2, size_y//2):
            
            
            R = int((abs(x) ** ex + abs(y) ** ey) ** (0.0005 * i + 0.6)) % 255
            image.putpixel((x + size_x//2, y + size_y//2), (R, G, B))
    
    print(i, end=" ")
    
    image.save(f"image{i}.png", format="png")

for i in range(400):
    
    size_x = 500
    size_y = 500
    
    image = Image.new(mode="RGB", size=(size_x, size_y), color = "black")
    
    R = int(sin(i * 0.04) * 127 + 127)
    G = int(cos(i * 0.04) * 127 + 127)
    B = 0

    for x in range(-size_x//2, size_y//2):
        for y in range(-size_y//2, size_y//2):
            
            B = int(abs(x) ** (1.2 + 0.001 * i) + abs(y) ** (1.2 + 0.001 * i)) % 255
            
            image.putpixel((x, y), (R, G, B))
    
    print(i, end=" ")
    
    image.save(f"image{i}.png", format="png")
    
for i in range(2000):
    
    size_x = 1024
    size_y = 1024
    
    image = Image.new(mode="RGB", size=(size_x, size_y), color = "black")
    
    d = 0
    l = 0
    p = 1
    
        
    X = size_x // 2 - 1
    Y = size_y // 2 - 1
    
    for q in range(1048576):
            
        if d == 0: X -= 1
        if d == 1: Y -= 1


#another one
for i in range(800, 900):
    
    size_x = 100
    size_y = 100
    
    image = Image.new(mode="RGB", size=(size_x, size_y), color = "black")
    
    r = 0
    g = 128 + (i * 40)
    b = 255 + (i * 80)

    for x in range(size_x):
        for y in range(size_y):
            R = int((sqrt(abs((x - (size_x // 2)) ** (i * 0.001) *  + (y - (size_x // 2)) ** (i * 0.001))) % 1) * r)
            if R > 255: R = 511 - R
            G = int((sqrt(abs((x - (size_x // 2)) ** (i * 0.001) + (y - (size_x // 2)) ** (i * 0.001))) % 1) * g)
            if G > 255: G = 511 - G
            B = int((sqrt(abs((x - (size_x // 2)) ** (i * 0.001) + (y - (size_x // 2)) ** (i * 0.001))) % 1) * b)
            if B > 255: B = 511 - B
            image.putpixel((x, y), (R, G, B))
    
    print(i, end=" ")
    
    image.save(f"image{i - 800}.png", format="png")

ex = 2
ey = 2

for i in range(1200):
    
    size_x = 500
    size_y = 500
    
    image = Image.new(mode="RGB", size=(size_x, size_y), color = "black")
    
    R = 0
    G = int(sin(i * 0.04) * 127 + 127)
    B = int(cos(i * 0.04) * 127 + 127)
    
    if i % 200 in range(0, 50): ex += 0.01
    if i % 200 in range(50, 100): ex -= 0.01
    if i % 200 in range(100, 150): ey += 0.01
    if i % 200 in range(150, 200): ey -= 0.01

    for x in range(-size_x//2, size_y//2):
        for y in range(-size_y//2, size_y//2):
            
            
            R = int((abs(x) ** ex + abs(y) ** ey) ** (0.0005 * i + 0.6)) % 255
            image.putpixel((x + size_x//2, y + size_y//2), (R, G, B))
    
    print(i, end=" ")
    
    image.save(f"image{i}.png", format="png")

for i in range(400):
    
    size_x = 500
    size_y = 500
    
    image = Image.new(mode="RGB", size=(size_x, size_y), color = "black")
    
    R = int(sin(i * 0.04) * 127 + 127)
    G = int(cos(i * 0.04) * 127 + 127)
    B = 0

    for x in range(-size_x//2, size_y//2):
        for y in range(-size_y//2, size_y//2):
            
            B = int(abs(x) ** (1.2 + 0.001 * i) + abs(y) ** (1.2 + 0.001 * i)) % 255
            
            image.putpixel((x, y), (R, G, B))
    
    print(i, end=" ")
    
    image.save(f"image{i}.png", format="png")
    
for i in range(2000):
    
    size_x = 1024
    size_y = 1024
    
    image = Image.new(mode="RGB", size=(size_x, size_y), color = "black")
    
    d = 0
    l = 0
    p = 1
    
        
    X = size_x // 2 - 1
    Y = size_y // 2 - 1
    
    for q in range(1048576):
            
        if d == 0: X -= 1
        if d == 1: Y -= 1
        if d == 2: X += 1
        if d == 3: Y += 1
        
        l += 1
        if l == p:
            l = 0
            if d in [1, 3]: p += 1
            if d == 3: d = 0
            else: d += 1
            
        
        
        R = int(q * (0.96 + i * 0.0004)) % 256
        G = int((X ** 2 + Y ** 2) ** (0.8587 + i * 0.00005)) % 256
        B = int(((X - 487) ** 2 + (Y - 667) ** 2) ** (0.9765 - i * 0.00004)) % 256

        image.putpixel((X, Y), (R, G, B))
    
    print(i, end=" ")
    
    image.save(f"image{i}.png", format="png")
