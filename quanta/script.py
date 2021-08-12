import re
from math import ceil
from typing import Iterable, Generator, Any
from dataclasses import dataclass, field
from itertools import islice, chain
# from sl4ng import splitter, slices

from browser import document, console, window
from browser.html import TABLE, TR, TH, TD

# from utils import keys, values

document <= "Hello"


strokeWidth = 1
tileSize = 10

widthInput = document.getElementById('widthInput')
heightInput = document.getElementById('heightInput')
extensionInput = document.getElementById('extensionInput')
colourInput = document.getElementById('colourInput')
cropButton = document.getElementById('cropButton')
pixelBox = document.getElementById('pixelBox')
# pixels = []
pixels = {}
grid = None

# heightInput = document.getElementById('')
# sketchpad = document.getElementById('sketchpad')
# ctx = sketchpad.getContext('2d')

# sketchpad.style.border = '1px dashed'
# sketchpad.innerHTML = '<tr id="pxrow0"><td id="px(0:0)"></td></tr>'

def hex2rgb(hx:str):
    hx = hx.replace('#', '')
    if len(hx) == 6:
        return int(hx[:2], 16), int(hx[2:4], 16), int(hx[4:], 16)
    else:
        error = ValueError(f'Poorly formatted hex string - "#{hx}"')
        window.alert(str(error))
        raise error
def pxid(x, y):
    return f"px({x}:{y})"
def getpx(x:int, y:int):
    return document.getElementById(pxid(x, y))
def newpx(x:int, y:int):
    pass
            


@dataclass
class Pixel:
    x:int
    y:int
    red:int=0
    blue:int=0
    green:int=0
    alpha:int=0
    opacity:int=0
    def set(self, r, g, b, a, o):
        self.red, self.green, self.blue, self.alpha, self.opacity = r, g, b, a, o
    @property
    def id(self):
        return f'px({self.x}:{self.y})'
    @property
    def head(self):
        return f'<td id="{self.id}" style="width: {tileSize}px; height: {tileSize}px; border: {strokeWidth}px dashed; background-color: #FFFFFF; opacity:{self.opacity}">'
    @property
    def tail(self):
        return '</td>'
    @property
    def code(self):
        return self.head + self.tail
    @property
    def elem(self):
        return document.getElementById(self.id)

@dataclass    
class Row:
    pixels:dict[Pixel]=field(default_factory=dict)
    def __len__(self):
        return len(self.pixels)
    def __iter__(self):
        return iter(sorted(self.pixels.values(), key=lambda p: p.x))
    @property
    def head(self):
        return 
    @property
    def tail(self):
        return 
    @property
    def code(self):
        return 
    

class Grid:
    def __init__(self):
        self.width, self.height = self.__width, self.__height
        self.pixels = {pxid(x, y): Pixel(x, y) for x in range(self.width) for y in range(self.height)}
        # [*map(pixels.append, self.pixels.values())]
        # pixels = self
    
    @property
    def __width(self):
        return int(widthInput.value)
    @property
    def __height(self):
        return int(heightInput.value)
    @property
    def rows(self):
        return [[self[pxid(x, y)] for x in range(self.width)] for y in range(self.height)]
    @property
    def columns(self):
        return [*zip(*self.rows)]
    
    @property
    def head(self):
        return f'<table id="sketchpad" style="float:inherit; border: 1px dashed">\n\t' 
    @property
    def inner(self):
        return ''.join('<tr>'+''.join(px.code for px in row)+'</tr>' for row in self.rows) 
    @property
    def tail(self):
        return '</table>'
    @property
    def code(self):
        return self.head + self.inner + self.tail
    
    def __getitem__(self, key):
        if isinstance(key, str):
            return self.pixels[key]
        elif isinstance(key, int):
            return self.rows[key]
        raise TypeError(f'"{key}" is not a viable grid-key')
        
    def __add__(self, px:Pixel):
        if isinstance(px, Pixel):
            self[px.id] = px
        else:
            error = TypeError('added non-Pixel to Grid')
            window.alert(str(error))
            raise error
    def __iter__(self):
        for x in range(self.width):
            for y in range(self.height):
                # yield getpx(x, y)
                # yield self[y][x].elem
                yield self[y][x]
            

# grid = Grid()

def setGrid(event=0):
    global grid
    pixelBox.innerHTML = grid.code
    for px in grid:
        px.elem.bind('click', setColour)
def init(event=0):
    global grid
    grid = Grid()
    setGrid()


    
    

        
    


# def tableCode():
    # width, height = map(int, (widthInput.value, heightInput.value))
    # w = ((width - 1) * strokeWidth) + (width * tileSize)
    # h = ((height - 1) * strokeWidth) + (height * tileSize)
    # text = f'<table id="sketchpad" style="border: 1px dashed #1b1b1b">\n\t'
    # for y in range(height):
        # pixels = [f'<td id="{pxid(x, y)}" style="width: {tileSize}px; height: {tileSize}px; border: {strokeWidth}px dashed; background-color: #000000; opacity:0"></td>' for x in range(width)]
        # text += f'<tr id="pixelRow{y}">{"".join(pixels)}</tr>\n\t'
    # return f'{text}</table>'

# def setGrid(event=0):
    # pixelBox.innerHTML = tableCode()
    # pixelBox.style.textAlign = 'center'
    # width, height = map(int, (widthInput.value, heightInput.value))
    # for x in range(width):
        # for y in range(height):
            # pixels[pxid(x, y)] = getpx(x, y)
    # for px in pixels.values():
        # px.bind('click', setColour)

def setColour(event):
    bgcolour = colourInput.value
    # console.log(px)
    # console.log(event)
    # console.log(event.target)
    console.log()
    
    styleHandle = StyleHandle(event.target.attributes.style.nodeValue)
    styleHandle['background-color'] = bgcolour
    
    # px = pixels[event.target.attributes.id.nodeValue]
    # console.log(f'{px=}')
    # console.log(f'{px.attributes.style=}')
    # px.attributes.style = styles.code
    # console.log(px.attributes.style)
    # del styles
    
    px = grid.pixels[event.target.attributes.id.nodeValue]
    console.log(px)
    console.log(px.elem.attributes.style)
    px.elem.attributes.style = styleHandle.code
    console.log(px.elem.attributes.style)
    del styles
    
    console.log()
    console.log()
    
    setGrid()
    
    # event.target.bgColor = colourInput.value
    # event.target.style.backgroundColor = colourInput.value
    

def crop(event):
    console.log(f'can\'t crop this dust:\n\t{event}')
    
# setGrid()
init()

cropButton.bind('click', crop)
widthInput.bind('change', setGrid)
heightInput.bind('change', setGrid)


# console.log(Grid().code)  
# document.style.textAlign = 'center'

def parseStyle(styles):
    words = map(str.strip, splitter(';:')(styles))
    return [*slices(words, 2)]

class StyleHandle:
    def __init__(self, nodeValue):
        self.origin = nodeValue
        self.words = words = map(str.strip, splitter(';:')(nodeValue))
        self.table = dict(slices(words, 2))
        # self.table = parseStyle(nodeValue)
    @property
    def code(self):
        return "; ".join(": ".join(item) for item in self.table.items()) + ';'
    def __getitem__(self, key):
        return self.table[key]
    def __setitem__(self, key, value):
        self.table[key] = value
    
    
def splitall(splitters:Iterable[str], target:str) -> Generator:
    """
    >>> [*splitall('-_.', 'author-file_name.ext')] == 'author file name ext'.split()
    True
    """
    splitters = iter(splitters)
    # console.log(target)
    result = target.split(next(splitters))
    for splitter in splitters:
        result = [*chain.from_iterable(i.split(splitter) for i in result)]
    yield from filter(None, result)




class splitter:
    """
    Callable which splits a string by a the elements of an iterable. Ignore any empty strings.
    >>> [*splitter('-_.')('author-file_name.ext')] == 'author file name ext'.split()
    True
    """
    def __init__(self, splitters:Iterable[str]):
        self.splitters = tuple(splitters)
    def __call__(self, argument) -> Generator:
        return splitall(self.splitters, argument)

def slices(iterable:Iterable, length:int, fill:Any=None) -> Generator:
    """
    Yield the adjacent slices of a given length for the given iterable. Trailing values will be padded by copies of 'fill'
        use filter(all, slices(iterable, length)) to discard remainders
    :fill:
        the default value of any
    eg:
        >>> [*slices('abc', 2, None)]
        [('a', 'b'), ('c', None)]
        >>> [*filter(all, slices('abc', 2, None))]
        [('a', 'b')]
    """
    itr = iter(iterable)
    while (main:=[*islice(itr, 0, length)]):
        main += [fill for i in range(length-len(main))]
        yield tuple(main)