import speech_recognition
import pyttsx3
from time import gmtime, strftime

class VirtualAssistant():

    def __init__(self):
        self.you = ""
        self.brain = ""

    def robotEar(self):
        robot_ear = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as mic:
            print("Robot: I'm listening")
            audio = robot_ear.listen(mic)

        try:
            self.you = robot_ear.recognize_google(audio)
            print('You:', self.you)
        except:
            self.you = "error"

    def robotBrain(self):
        if 'hello' in self.you:
            self.brain = 'hello'
        elif 'bye' in self.you:
            self.brain = 'Good bye'
            print(self.brain)
            robot_mounth = pyttsx3.init()
            robot_mounth.say(self.brain)
            robot_mounth.runAndWait()
            exit()
        elif 'day' in self.you:
            self.brain = strftime("%A-%d-%B-%Y")
        elif 'time' in self.you:
            self.brain = strftime("%H:%M:%S")
        elif 'dog' in self.you:
            self.brain = 'nguyen oc cho'
        else:
            self.brain = "I dont know"
        print('Robot:', self.you)

    def robotMounth(self):
        robot_mounth = pyttsx3.init()
        robot_mounth.say(self.brain)
        robot_mounth.runAndWait()

vta = VirtualAssistant()
while True:
    vta.robotEar()
    vta.robotBrain()
    vta.robotMounth()