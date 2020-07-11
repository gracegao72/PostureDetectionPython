import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import pygame

def speak(text):
    tts = gTTS(text = text, lang ="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    
#speak("hello tim")

def speak_alt(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 0.9)
    engine.runAndWait()

def speak_pygame():
    pygame.init()
    #pygame.mixer.init()
    sounda = pygame.mixer.Sound("chime.wav")
    pygame.mixer.Sound.play(sounda)
    
    #sounda.play()

speak_pygame()