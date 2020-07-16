import pyttsx3
import datetime
import wikipedia
import smtplib
import age_gender_emotion as age
import music as mu
import weather as we
import plant_classifier as pc
import speech as s
import watson_classifier as wc
import face_compare_using_known_faces as face
import text_detection_and_convert_hindi as trans
import navigation as nav

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 180)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("Booting the system, calibrating the devices........")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Pedi, your one step taken towards becoming a superhuman")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def starting():
    speak("So lets start customizing the experience for you. Tell me, what should I call you ?")
    #name = s.takeCommand()
    name = 'soorya'
    speak("ok, I will call you, "+name)
    return name

take = "search about ra egypt"

if __name__ == "__main__":
    wishMe()
    name = starting()
    while True:
        speak("Now, How can I help you "+name+",")
        # query = s.takeCommand()
        # query = query.lower()
        query = take
        # Logic for executing tasks based on query
        if ('wikipedia' in query) or ('search' in query) or ('about' in query) and ('plant' not in query) and ('age' not in query) and ('song' not in query):
            speak('OK Gathering information from my sources...')
            if ('wikipedia' in query):
                query = query.replace("wikipedia", "")
            elif ('tell me about' in query):
                query = query.replace("tell me about", "")
            elif ('ok pedi, tell me about' in query):
                query = query.replace("ok pedi, tell me about", "")
            elif ('ok pedi, wikipedia' in query):
                query = query.replace("ok pedi, wikipedia", "")
            elif ('search' in query) :
                query = query.replace("search", "")
            elif ('ok pedi, search' in query):
                query = query.replace("ok pedi, search", "")
            elif ('search about' in query):
                query = query.replace("search about", "")
            elif ('ok pedi, search about' in query):
                query = query.replace("ok pedi, search about", "")
            elif ('give me information about' in query) :
                query = query.replace("give me information about", "")
            elif ('ok pedi, give me information about' in query):
                query = query.replace("ok pedi, give me information about", "")
            else :
                speak("Please rephrase your statements, after all I cannot know everything, hahaha")
            results = wikipedia.summary(query, sentences=2)
            speak("Ok, so here's what I found out")
            print(results)
            speak(results)


        elif 'age' in query:
            speak("Ok, analysing his age")
            data = age.run_aging()
            if data[1] == 'Male':
                speak("Well, I think his age is around" + str(data[0]) + "years")
            else:
                speak("Well, I think his age is around" + str(data[0]) + "years")


        elif 'gender' in query:
            speak("Ok, analysing his gender")
            data = age.run_aging()
            if data[1] == 'Male':
                speak("Well, I have no gender, haha, but I think he is " + str(
                    data[1]) + ", come on, can you not see that yourself, now unless you are blind, hahaha")
            else:
                speak("Well, I have no gender, haha, but I think she is " + str(
                    data[1]) + ", come on, can you not see that yourself, now unless you are blind, hahaha")


        elif ('emotions' in query) or ('emotion' in query):
            speak("Ok, analysing his emotions")
            data = age.run_aging()
            if data[1] == 'Male':
                if data[2] == 'anger':
                    speak("Well, I think he is really angry. If I were you, I would definitely not mess with him now !")
                elif data[2] == 'happiness':
                    speak("Woah look at him smile there, no bounds for his happiness for sure")
                elif data[2] == 'sadness':
                    speak("awwwww, poor thing, something's made him really upset, if I were you I would have offered him some tea")
                elif data[2] == 'fear':
                    speak("Now look at him, doesn't he look scared, ofcourse he is scared. If I were you I would ask him the reason for sure!")

            else:
                if data[2] == 'anger':
                    speak("Well, I think she is really angry. If I were you, I would definately not mess with her now !")
                elif data[2] == 'happiness':
                    speak("Woah look at her smile there, no bounds for her happiness for sure")
                elif data[2] == 'sadness':
                    speak("awwwww, poor thing, something's made her really upset, if I were you I would have offered her some tea")
                elif data[2] == 'fear':
                    speak("Now look at her, doesn't she look scared, ofcourse she is scared. If I were you I would ask her the reason for sure!")


        elif ('song' in query) or ('play' in query) or ('music' in query):
            mu.play()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Soorya, the time is {strTime}")

        elif ('weather' in query) or ('climate' in query):
            weather = we.weath()
            speak("Ok scanning the sky to get the weather information...")
            speak("The current weather conditions are as follows, the relative humidity is "+str(weather[0][0])+
                  "percent, the current temperature is "+str(weather[0][1])+
                  "degree celsius. The average wind speed is "+str(weather[0][2])+
                  "kilometer per hour and possibility of "+str(weather[0][3]))

            speak("would you like to know tomorrows weather as well ?")
            tommy = s.takeCommand()
            tommy = tommy.lower()
            #tommy = 'no'
            if 'yes' in tommy:
                speak("Ok, so tomorrows weather is going to be as follows, the relative humidity shall be " + str(weather[1][0]) +
                      "percent, tommorows expected day temperatures might be  " + str(weather[1][1]) +
                      "degree celsius. The average wind speed will be around " + str(weather[1][2]) +
                      "kilometer per hour and possibility of " + str(weather[1][3]))
            elif 'no' in tommy:
                speak('hey, hope that knowing the weather has not spoiled your plans for today hahaha')

        elif 'plant' in query:
            speak('Ok, collecting and analyzing the plant information from my sources....')
            pc.planty()

        elif ('analyze' in query) or ('analyse' in query) or ('animal' in query) or ('general' in query) or ('scan' in query):
            speak('Ok, performing a quick scan to find labels associated with it')
            wc.run_classi()

        elif ('store face' in query) or ('save' in query) or ('store' in query) or ('face' in query):
            speak("Ok, performing a quick scan to store the valuable data of the face !!")
            face.capture()

        elif ('what is the name' in query) or ('tell me the name' in query) or ('show me the name'):
            speak("Ok, analyzing your database for the person's name !")
            face.analyze_face()

        elif ('translate' in query):


        elif ('navigation' in query) or ('navigate' in query) or ('way' in query):


        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = s.takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")
