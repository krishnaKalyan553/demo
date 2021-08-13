import pyttsx3
#relation=model(image)
relation=input('what is the output of the model:\n')

def audio(relation):
    pyobj=pyttsx3.init()
    pyobj.say("this is your"+str(relation))
    pyobj.runAndWait()
audio(relation)
