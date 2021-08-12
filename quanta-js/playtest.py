from ctypes import c_buffer, windll
from sys    import getfilesystemencoding
from random import choice
from itertools import chain

from audioplayer import AudioPlayer as ap
from playsound import playsound as ps
from sl4ng import pop, show, getsource, Duration, commons, shuffle, freq
from filey import Directory, File, forbiddens
import audio_metadata as am, filetype as ft

formats = 'mp3,flac,wav,ogg'

# path = r'C:\Users\Kenneth\Music\Collection\Dominic Pierce\some older stuff\22 Aller et Retour.mp3'
# path = choice([*Directory(r'C:\Users\Kenneth\Music\Collection')('', ext=formats)])
path = choice([*Directory(r'C:\Users\Kenneth\Music\Collection\dBridge\The Gemini Principle')('', ext=formats)])
# path = r"C:\Users\Kenneth\Music\Collection\dBridge\The Gemini Principle\05 Creatures Of Habit.mp3"
file = File(path)
fold = file.up 
print(file)
artist = am.load(path)['tags']['artist'][0]
title = am.load(path)['tags']['title'][0]
length = am.load(path)['streaminfo']['duration']
album = am.load(path)['tags']['album'][0]
print(f"{title} ({Duration(length)})\n\tby \"{artist}\"\n\ton \"{album}\"")
g = ap(path)
print(g._alias)
g.play()
# g = ps(path, block=False)



def arg(*command):
    buf = c_buffer(255)
    command = ' '.join(command).encode(getfilesystemencoding())
    print(command)
    errorCode = int(windll.winmm.mciSendStringA(command, buf, 254, 0))
    if errorCode:
        errorBuffer = c_buffer(255)
        windll.winmm.mciGetErrorStringA(errorCode, errorBuffer, 254)
        exceptionMessage = ('\n\tError ' + str(errorCode) + ' for command:'
                            '\n\t\t' + command.decode() +
                            '\n\t' + errorBuffer.value.decode())
        raise Exception(exceptionMessage)
    return buf.value

class Buffer:
    def __init__(self, path):
        self.path = path
        self.alias = f"p{id(self)}"
        self.data = am.load(path)
    @property
    def artist(self):
        return self.data['tags']['artist'][0]
    @property
    def title(self):
        return self.data['tags']['title'][0]
    @property
    def length(self):
        return Duration(self.data['streaminfo']['duration'])
    @property
    def album(self):
        return self.data['tags']['album'][0]
    @property
    def stream(self):
        return self.data['streaminfo']
    @property
    def tags(self):
        return self.data['tags']
    def __repr__(self):
        return print(f"{self.title} ({self.length})\n\tby {self.artist}\n\ton {self.album}")

class Player:
    # def __init__(self, library=[*Directory(r'C:\Users\Kenneth\Music\Collection')('', ext=formats)]):)
    # def __init__(self, library=[*Directory(r'C:\Users\Kenneth\Music\Collection')('', ext=formats)]):
    def __init__(self, directories=[commons['music']]):
        self.current = None
        self.directories = directories
        self.ctx = None
        self.playing = False
        self.opened = False
        self.alias = f"P{id(self)}"
    def findartists(self, terms):
        if terms=='*':
            for d in self.library:
                for p in d:
                    for f in p.leaves:
                        if not re.match('some assembly required|123 mix', f.path, re.I):
                            if re.match('audio|video', f.kind, re.I):
                                yield f.path
        else:
            sep = max(forbiddens.replace('/', '')+',', key=lambda c: freq(c, terms))
            pat = '|'.join(re.escape(i.strip().replace('/', os.sep)) for i in terms.split(sep))
            print(pat+'\n\n')
            for d in musearch:
                for f in d.leaves:
                    if re.search(pat, f.path, re.I):
                        yield f.path
    def library(self):
        yield from map(Directory, self.directories)

    def files(self):
        yield from chain.from_iterable(filter(ft.audio_match, d('')) for d in self.library)

    def __call__(self, artists, shuff=1, rep=1, block=False):        
        results = filter(ft.audio_match, findartists(artists))
        playlist = sorted(results)
        self.tracks = tracks = (playlist, shuffle(playlist))[shuff]
        
        show(tracks, enum=True, tail=True)
        print('\n\n')
        loop = cycle(tracks) if repeat else iter(tracks)
        while rep:
            for path in loop:
                self.current


    def play(self, path=None, block=False):
        if path:
            self.current = Buffer(path)
            print(self.current)
        # self.open() if not self.opened else self.start()
        if not self.opened:
            self.open()
        
        arg(f'play {self.alias}')
        self.playing = True

    def pause(self):
        arg(f'pause {self.alias}')
        self.playing = False

    def open(self):
        if self.current:
            arg(f'open "{self.current.path}" alias {self.current.alias}')
            self.opened = True
        else:
            raise Exception('There is no buffer to draw from')


if __name__ == '__main__':
    p = Player()