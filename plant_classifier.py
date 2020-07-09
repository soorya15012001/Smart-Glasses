import base64
import requests
import pprint
# encode image to base64
with open("Resources/ganer.jpg", "rb") as file:
    images = [base64.b64encode(file.read()).decode("ascii")]

your_api_key = "eSB8rSqRtFY7oVkCP75Tnlwx0iA91HEgu1ibcLxobKUz0En9pf"
json_data = {
    "images": images,
    "modifiers": ["similar_images"],
    "plant_details": ["common_names", "url", "wiki_description", "taxonomy"]
}

response = requests.post(
    "https://api.plant.id/v2/identify",
    json=json_data,
    headers={
        "Content-Type": "application/json",
        "Api-Key": 'eSB8rSqRtFY7oVkCP75Tnlwx0iA91HEgu1ibcLxobKUz0En9pf'
    }).json()

# for suggestion in response["suggestions"]:
#     print(suggestion["plant_name"])    # Taraxacum officinale
#     print(suggestion["plant_details"]["common_names"])    # ["Dandelion"]
#     #print(suggestion["plant_details"]["url"])    # https://en.wikipedia.org/wiki/Taraxacum_officinale
#print(response["suggestions"])
print(response["suggestions"][0]['plant_name'],'\n')
print(response["suggestions"][0]['plant_details']['common_names'],'\n')
print(response["suggestions"][0]['plant_details']['wiki_description']['value'],'\n')
