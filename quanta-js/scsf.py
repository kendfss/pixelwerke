import soundcard as sc, soundfile as sf
from sl4ng import slices, pop, show, getsource
# get a list of all speakers:
speakers = sc.all_speakers()
# get the current default speaker on your system:
default_speaker = sc.default_speaker()
# get a list of all microphones:
mics = sc.all_microphones()
# get the current default microphone on your system:
default_mic = sc.default_microphone()
# search for a sound card by substring:
# print(sc.get_speaker('Scarlett'))
# <Speaker Focusrite Scarlett 2i2 (2 channels)>
# one_mic = sc.get_microphone('Scarlett')
# <Microphone Focusrite Scalett 2i2 (2 channels)>
# fuzzy-search to get the same results:
# one_speaker = sc.get_speaker('FS2i2')
# one_mic = sc.get_microphone('FS2i2')

path = r"C:\Users\Kenneth\Downloads\music\bandies\Tyler Straub - The Process.flac"
# path = r"C:\Users\Kenneth\Music\Collection\Alix Perez\1984\03 Fade Away.mp3"
# path = r"C:\Users\Kenneth\Music\Collection\dBridge\The Gemini Principle\05 Creatures Of Habit.mp3"
sr = 48 * 10 ** 3
cs = 1024
with default_mic.recorder(samplerate=48000) as mic, \
      default_speaker.player(samplerate=48000) as sp:
    # for _ in range(100):
    log = []
    while 1:
        data = mic.record(numframes=1024)
        sp.play(data)
        log.append(data)
        sf.write('recording.wav', log[0], 48000)
        # with sf.SoundFile('records.wav', 'wb') as fob:
        #     fob.wr
# with sf.SoundFile(path) as f:
# with open(path, 'rb') as fob:
#     d, sr = sf.read(fob)
    # print(f.samplerate)
    # with default_speaker.player(samplerate=sr, blocksize=cs/2, exclusive_mode=True) as sp:
    #     for datum in slices(d, cs):
    #         sp.play(datum)
        # pos = f.tell()
        # while pos < f.frames:
        #     print(pos)
        #     data = f.read(cs)
        #     f.seek(pos)
        #     sp.play(data)
        #     pos += int(cs*1.75)
        # for block in sf.blocks(path, blocksize=cs, overlap=int(cs/2)):
        #     sp.play(block)
# with default_mic.recorder(samplerate=48000) as mic, \
#     default_speaker.player(samplerate=48000) as sp:
    # for _ in range(100):
    #     data = mic.record(numframes=1024)
    #     sp.play(data)