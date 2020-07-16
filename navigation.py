import requests
import pprint
import pyproj
import math
import time
import cv2
import re

cl = 0
cr = 0


def display(text):
    global cl
    global cr

    if re.search("straight", text):
        img = cv2.imread("Resources/straight.png")
        img = cv2.resize(img, (600, 600))
        cv2.putText(img, text, (100, 400), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 0), 2)
        cv2.imshow('overlay', img)
        cv2.waitKey(0)

    elif re.search("back", text):
        img = cv2.imread("Resources/back.png")
        img = cv2.resize(img, (600, 600))
        cv2.putText(img, text, (100, 400), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 0), 2)
        cv2.imshow('overlay', img)
        cv2.waitKey(0)


    elif re.search("left", text):
        if cl == 0:
            img1 = cv2.imread("Resources/left.png")
            img1 = cv2.resize(img1, (600, 600))
            cv2.putText(img1, text, (100, 400), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 0), 2)
            cv2.imshow('overlay', img1)
            cl = cl + 1
            cv2.waitKey(5000)
        else:
            img = cv2.imread("Resources/straight.png")
            img = cv2.resize(img, (600, 600))
            cv2.putText(img, text, (100, 400), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 0), 2)
            cv2.imshow('overlay', img)
            cv2.waitKey(0)

    elif re.search("right", text):
        if cr == 0:
            img1 = cv2.imread("Resources/right.png")
            img1 = cv2.resize(img1, (600, 600))
            cv2.putText(img1, text, (100, 400), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 0), 2)
            cv2.imshow('overlay', img1)
            cr = cr + 1
            cv2.waitKey(5000)
        else:
            img = cv2.imread("Resources/straight.png")
            img = cv2.resize(img, (600, 600))
            cv2.putText(img, text, (100, 400), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 0), 2)
            cv2.imshow('overlay', img)
            cv2.waitKey(0)

    else:
        img = cv2.imread("Resources/straight.png")
        img = cv2.resize(img, (600, 600))
        cv2.putText(img, text, (100, 400), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 0), 2)
        cv2.imshow('overlay', img)
        cv2.waitKey(0)


def find_distance(coord0, coord1):
    geod = pyproj.Geod(ellps='WGS84')
    lat0, lon0 = coord0[0], coord0[1]
    lat1, lon1 = coord1[0], coord1[1]

    azimuth1, azimuth2, distance = geod.inv(lon0, lat0, lon1, lat1)
    # print(distance)
    return distance


# nallakunta home location = 17.3981761, 78.5100478
ini_place = input('Enter your starting place:- ')
fin_place = input('Enter your final place:- ')
places = []
coord = []
places.append(ini_place)
places.append(fin_place)

for i in range(2):
    geocode = requests.get('https://api.geoapify.com/v1/geocode/autocomplete?text=' + places[
        i] + '&limit=5&apiKey=54240c9cda5e4264861efa14ee809ea8')
    code = geocode.json()['features'][0]['geometry']['coordinates']
    coord.append(code[1])
    coord.append(code[0])
pprint.pprint(coord)

r = requests.get('https://api.geoapify.com/v1/routing?waypoints=' + str(coord[0]) + ',' + str(coord[1]) + '|' + str(
    coord[2]) + ',' + str(coord[3]) + '&mode=drive&apiKey=54240c9cda5e4264861efa14ee809ea8')

data = r.json()['features'][0]['properties']['legs'][0]['steps']
coord = r.json()['features'][0]['geometry']['coordinates'][0]

for i in range(len(data)):
    print(data[i]['distance'], '--->', data[i]['instruction']['text'])

coord_final = []

for i in range(len(coord)):
    x = []
    x.append(coord[i][1])
    x.append(coord[i][0])
    coord_final.append(x)
print(coord_final)

start_location = [17.398132,78.510131]  # load this once the progrm starts running get initial coordinates from GPS module
cur_location = [17.398132, 78.510131]  # initially same as start_location
c = 0
while c < len(data):
    while find_distance(start_location, cur_location) < int(data[c]['distance']):
        time.sleep(5)
        cur_location = [17.397985, 78.512268]  # update it continuously
        dis = math.ceil(data[c]['distance'] - (find_distance(start_location, cur_location)))
        if_display = str(data[c]['instruction']['text'] + "-->" + str(dis))
        else_display = str("Go straight" + "-->" + str(dis))
        less_display = str("Go back" + "-->" + str(dis))

        if cl == 0 and cr == 0:
            print(cl, cr)
            if dis < 0:
                print(less_display)
                display(less_display)
            else:
                print(if_display)
                display(if_display)
        else:
            print(cl, cr)
            print(else_display)
            display(else_display)
    cl = 0
    cr = 0
    start_location = cur_location
    c = c + 1
