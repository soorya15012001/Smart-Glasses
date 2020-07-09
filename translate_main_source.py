import http.client

conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")

payload = "source=en&q=What's up bro, what are you up to ?&target=hin"

headers = {
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': "c771508a29mshb7b3d1656f75065p1f358ajsn35a04c20fa73",
    'accept-encoding': "application/gzip",
    'content-type': "application/x-www-form-urlencoded"
    }

conn.request("POST", "/language/translate/v2", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))