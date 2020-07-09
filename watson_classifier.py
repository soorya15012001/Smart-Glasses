from watson_developer_cloud import VisualRecognitionV3
path = 'Resources/ganer.jpg'
dic = []

visual_recognition = VisualRecognitionV3(version='2016-05-20',iam_apikey='_BWRFUuaOZeqti8Vhj85iRSb2xhPew6gfTRdU4KTSllx') #authenticate
classes = visual_recognition.classify(images_file=open(path, 'rb'),threshold='0.6',classifier_ids='default').get_result()
c= len(classes['images'][0]['classifiers'][0]['classes'])
for i in range(c):
     dic.append(classes['images'][0]['classifiers'][0]['classes'][i]['class'])
print(dic)