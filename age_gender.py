import requests
import os
import cv2


def analyse(img):
    global gender
    json_resp = requests.post('https://api-face.sightcorp.com/api/detect/',
                              data={'app_key': 'f0daffcf0e8b4c879123898220ea8792', 'ethnicity': True},
                              files = { 'img': ( 'filename', open( 'data/'+img, 'rb' ) ) } )

    data = json_resp.text
    data = eval(data)

    age = data['people'][0]['age']

    if (data['people'][0]['gender'] > 0):
        gender = 'Female'
    elif (data['people'][0]['gender'] < 0):
        gender = 'Male'

    eth = data['people'][0]['ethnicity']
    sort_eth = sorted(eth.items(), key=lambda x: x[1], reverse=True)
    for i in sort_eth:
        ethnicity = i[0]
        break

    emo = data['people'][0]['emotions']
    sort_emo = sorted(emo.items(), key=lambda x: x[1], reverse=True)
    for i in sort_emo:
        emotion = i[0]
        break
    final = []
    final.append(age)
    final.append(gender)
    #final.append(ethnicity)
    final.append(emotion)
    return final


if not os.path.exists('data'):
    os.mkdir('data')
vid = cv2.VideoCapture(0)
index = 0
while index < 50:
        success, img = vid.read()
        if not success:
            break
        name = './data/frame'+str(index)+'.jpg'
        print('extracting images....' + name)
        cv2.imwrite(name, img)
        index = index + 1
vid.release()

print(analyse('frame24.jpg'))