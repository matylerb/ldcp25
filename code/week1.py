# Star Map Visualization
# Name: Tyler Brady

import py5
import pandas as pd
import math

df = None

def load_data():
    global df
    #make sure the data is loaded and handled correctly
    try:
        df = pd.read_csv('../data/HabHYG15ly.csv', encoding='latin1')
        print("data loaded")
    except FileNotFoundError:
        print("data not loaded")
    return df

def parsecs_to_pixels_x(parsecs):
    """Convert parsec X to pixel X"""
    return py5.remap(parsecs, -5, 5, 50, 750)

def parsecs_to_pixels_y(parsecs):
    """Convert parsec Y to pixel Y"""
    return py5.remap(parsecs, -5, 5, 50, 750)



def setup():
    
    py5.size(800, 800)
    data = load_data()
    print(data.head(5))

def distance():


    pixel_coord = []


    for Xg, Yg in zip(df['Xg'], df['Yg']):
        x = parsecs_to_pixels_x(Xg)
        y = parsecs_to_pixels_y(Yg)
        pixel_coord.append((x, y))



    for i in range(len(pixel_coord)):
        x1, y1 = pixel_coord[i]
        for j in range(i + 1, len(pixel_coord)):
            x2, y2 = pixel_coord[j]

            dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
            if dist < 50:  
                py5.stroke(255)
                py5.line(x1, y1, x2, y2)

def draw():

    global df
    py5.background(0)

    for Xg, Yg in zip(df['Xg'], df['Yg']):
        x = parsecs_to_pixels_x(Xg)
        y = parsecs_to_pixels_y(Yg)
        py5.stroke(255)
        py5.point(x, y)

        distance()

        
py5.run_sketch()


