#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sounddevice as sd
from datetime import datetime
import soundfile as sf
import os
import numpy as np
from time import time

path = "/home/felipe/final_final"
audio_t = path + "/audio_tiao"
audio_n = path + "/audio_not"

class Audio():

    def __init__(self):
    
        self.id = self.get_id()
        self.device = sd.query_devices()[self.id]
        self.fs = int(self.device["default_samplerate"])    
        self.last_rec = np.zeros((0))  
        self.last_time = 0        
        

    def get_time(self):

        now = datetime.now()
        time_id = '{:02d}'.format(now.day)+"-"+'{:02d}'.format(now.month)+"-"+str(now.year)+"-"+'{:02d}'.format(now.hour)+":"+'{:02d}'.format(now.minute)+":"+'{:02d}'.format(now.second)
        return time_id


    def audio_id(self):

        now = datetime.now()
        pic_id =  str(now.day) +"_"+ str(now.month) +"_"+ str(now.hour) +"_"+ str(now.minute) +"_"+ str(now.second)

        return pic_id


    def get_id(self):

        dev = sd.query_devices()
        dev_list = [dev[i]["name"] for i in range(len(dev))]
        for i in range(len(dev_list)):

            if "USB" in dev_list[i]:

                return i

        print("Nenhum dispositivo foi encontrado")
        return -1
        

    def R(self, duration=0.25):
     
        rec = sd.rec(int((duration * self.fs)), samplerate = self.fs, channels=1)
        sd.wait()        
        amplitude = rec.max() - (rec.min()) / 2
        return rec.max()
        
    
    def REC(self, duration=0.25):
     
        self.last_time = time()
        rec = sd.rec(int((duration * self.fs)), samplerate = self.fs, channels=1)
        self.last_rec = rec
        

    def save_audio(self, modifier):

        pic_id = self.audio_id()

        if modifier == 0:

            sf.write(audio_t  + "/out_" + str(pic_id) + ".wav", self.last_rec, self.fs)

        else:

            sf.write(audio_n + "/out_" + str(pic_id) + ".wav", self.last_rec, self.fs)


if __name__ == "__main__":

    sound = Audio()
    mx = sound.R()
    print(mx)



