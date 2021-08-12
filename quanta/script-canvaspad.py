from math import ceil

from browser import document, console, window
from browser.html import TABLE, TR, TH, TD

# from utils import keys, values

document <= "Hello"

widthInput = document.getElementById('widthInput')
heightInput = document.getElementById('heightInput')
extensionInput = document.getElementById('extensionInput')
colourInput = document.getElementById('colourInput')
cropButton = document.getElementById('cropButton')
# heightInput = document.getElementById('')
sketchpad = document.getElementById('sketchpad')
ctx = sketchpad.getContext('2d')

sketchpad.style.border = '1px dashed'

strokeWidth = 1
tileSize = 10

def pxid(x:int, y:int):
    return f'px({x}:{y})'
def getpx(x:int, y:int):
    return document.getElementById(pxid(x, y))
def newpx(x:int, y:int):
    sketchpad


def crop(event):
    console.log(f'can\'t crop this dust:\n\t{event}')

def setGrid(event=0):
    width, height = map(int, (widthInput.value, heightInput.value))
    sketchpad.width = ((width - 1) * strokeWidth) + (width * tileSize)
    sketchpad.height = ((height - 1) * strokeWidth) + (height * tileSize)
    
    location = sketchpad.getBoundingClientRect()
    xbase, ybase = map(int, (location.left, location.top))
    console.log(location)
    # console.log(location.keys())
    # console.log(keys(location))
    # console.log(xbase)
    for i in range(width - 1):
        xbase += tileSize + ceil(strokeWidth / 2)
        # xbase += tileSize + strokeWidth 
        # ctx.beginPath()
        # ctx.moveTo(xbase, int(location))
        ctx.moveTo(xbase, location.top)
        ctx.lineTo(xbase, location.bottom)
        ctx.strokeStyle = '1px dashed'
        ctx.stroke()
    for i in range(height - 1):
        ybase += tileSize + round(strokeWidth / 2)
        # ybase += tileSize + strokeWidth
        ctx.moveTo(location.left, ybase)
        ctx.lineTo(location.right, ybase)
        ctx.stroke()

setGrid()

# widthInput.addEventListener(
    # 'change', 
    # def _():
        # console.log(widthInput.value)
# )

cropButton.bind('click', crop)
widthInput.bind('change', setGrid)
heightInput.bind('change', setGrid)