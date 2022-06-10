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
        with open('model_pickle_BDD_final', 'rb') as f:
            mp = pickle.load(f)
            return mp


    def prediction(value1, value2, value3, value4, value5, mp):
        print(mp.predict([[value1, value2, value3, value4, value5]]))
        prediction = mp.predict([[value1, value2, value3, value4, value5]])
        return prediction


    def commande_vocale(prediction):
        text_speech = pyttsx3.init()
        voices = text_speech.getProperty('voices')
        text_speech.setProperty('voice', voices[29].id)
        text_speech.say(str(prediction[0]))
        text_speech.runAndWait()


    def verification(verification_liste):
        if verification_liste[0][0] == verification_liste[1][0] == verification_liste[2][0] == "Other":
            return -1
        if verification_liste[0][0] != verification_liste[1][0] or verificaiton_liste != verification_liste[2][0] or \
                verification_liste[1][0] != verification_liste[2][0]:
            return -1
        if verification_liste[0][0] == verification_liste[1][0] == verification_liste[2][0]:
            return verification_liste[0][0]


    def Run():
        while True:
            i = 0
            verification_liste = []
            while i != 3:
                value1, value2, value3, value4, value5 = get_values(adc)
                mp = open_model()
                prediction_verification = prediction(value1, value2, value3, value4, value5)
                verification_liste.append(prediction_verification)
                time.sleep(1)
                i += 1
            verif = verification(verification_liste)
            if verif == -1 or verif == None:
                break
            print(verif)
            commande_vocale(verif)


    Run()