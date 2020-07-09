import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException
import http.client
from gtts import gTTS
import os

api_instance = cloudmersive_ocr_api_client.ImageOcrApi()
image_file = 'Resources/i2.jpg'


api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = '9c724f3d-823b-4184-bc07-2a859e30efa2'
op={}
try:

    api_response = api_instance.image_ocr_post(image_file)
    k = str(api_response)
    dic = eval(k)
    text = str(dic['text_result'])
    #print(text)

except ApiException as e:
    print("Exception when calling ImageOcrApi->image_ocr_post: %s\n" % e)

#print(text)

conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")

payload = "source=en&q="+text+"&target=hin"

headers = {
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': "432bde5189mshbb6ce1fb010b474p1ddf59jsn3d5cd8d9faf7",
    'accept-encoding': "application/gzip",
    'content-type': "application/x-www-form-urlencoded"
    }

conn.request("POST", "/language/translate/v2", payload, headers)

res = conn.getresponse()
data = res.read()
f = data.decode("utf-8")
final = eval(f)
data_final = final['data']['translations'][0]['translatedText']
print(data_final)

