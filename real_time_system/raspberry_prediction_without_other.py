from MCP3208 import MCP3008
from pickle
import os
import time
from numpy.core import multiarray
import pyttsx3

adc = MCP3008()

while True():
    def get_values(adc):
        value1 = adc.read(channel=2)  # Auriculaire
        value2 = adc.read(channel=3)  # Annulaire
        value3 = adc.read(channel=4)  # Index
        value4 = adc.read(channel=5)  # Majeur
        value5 = adc.read(channel=6)  # Pouce
        print(f"{value1},{value2},{value3},{value4},{value5}")

        return value1, value2, value3, value4, value5


    def open_model():
        with open('model_pickle_final', 'rb') as f:
            mp = pickle.load(f)
            return mp


    def prediction(value1, value2, value3, value4, value5, mp):
        print(mp.predict([[value1, value2, value3, value4, value5]]))
        prediction = mp.predict([[value1, value2, value3, value4, value5]])
        return prediction


    def commande_vocale(prediction):
        text_speech = pyttsx3.init()
        text_speech.say(str(prediction[0]))
        text_speech.runAndWait()


    def Run():
        value1, value2, value3, value4, value5 = get_values(adc)
        mp = open_model()
        audio = prediction(value1, value2, value3, value4, value5, mp)
        commande_vocale(audio)


    Run()
    time.sleep(3)