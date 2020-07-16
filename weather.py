import requests
def weath():
    response = requests.get("http://api.openweathermap.org/data/2.5/onecall?lat="+str(17.3981761)+"&lon="+str(78.5100478)+"&units=metric&appid=a774217b6c58d47b47ec3fafe95733b5")
    data = response.json()
    current = []
    tommy = []
    final = []

    current.append(data['current']['humidity'])
    current.append(data['current']['temp'])
    current.append(data['current']['wind_speed']*3.6)
    current.append(data['current']['weather'][0]['description'])

    tommy.append(data['daily'][0]['humidity'])
    tommy.append(data['daily'][0]['temp']['day'])
    tommy.append(data['daily'][0]['wind_speed']*3.6)
    tommy.append(data['daily'][0]['weather'][0]['description'])

    final.append(current)
    final.append(tommy)

    return final
