from dataclasses import dataclass, field
import asyncio

import soundcard as sc, soundfile as sf, audio_metadata as am, filetype as ft


# def play()
# with open('')

class Track:
    def __init__(self, path:str):
        self.path = path
        self.playing = False
        # self.opened = False
        self.index = 0
        self.data = am.load(self.path)
        self.__handle = None

    @property
    def opened(self):
        return not isinstance(self.__handle, type(None))
    
    def open(self, mode='rb', **kwargs):
        self.__handle = open(self.path, mode, **kwargs)
    
    def close(self):
        if self.opened:
            self.__handle.close()
            self.__handle = None


    def play(self):
        if not self.opened:
            self.open()
        self.playing