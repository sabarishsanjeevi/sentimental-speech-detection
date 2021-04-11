import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("clearing Your microphone noises")
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("Kindly Speek .....")
    recordaudio=recognizer.listen(source)
    print("Recorded successfully!!")
    
try:
    print("Detection In progress Please Wait A minute....")
    text=recognizer.recognize_google(recordaudio,language='en-US')
    print("Your message is = {}".format(text))

except Exeption as ex:
    print(ex)

Sentance = [str(text)]
analyser=SentimentIntensityAnalyzer()
for i in Sentance:
    v = analyser.polarity_scores(i)
    if(v['neg']>v['neu'] and v['neg']>v['pos']):
        print("You are speaking Negatively🙃")
    elif(v['neu']>v['neg'] and v['neu']>v['pos']):
        print("You are speaking Neutral😌")
    else:
        print("You are Speaking Positively😉")
