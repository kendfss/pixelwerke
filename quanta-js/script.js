// require("./maths.js");
// require("./itertools.js");
// require("./colours.js");

const backgroundColor = 0xfff;
const widthInput = document.getElementById('widthInput');
const heightInput = document.getElementById('heightInput');
const extensionInput = document.getElementById('extensionInput');
const colourInput = document.getElementById('colourInput');
const cropButton = document.getElementById('cropButton');
const pixelBox = document.getElementById('pixelBox');
const strokeWidth = 1;
const tileSize = 10;
const pixels = {};
var currentColour;
var grid;


function pxid(x, y) {
    return `px(${x}, ${y})`;
}
function getpx(x, y) {
    return document.getElementById(pxid(x, y));
}

class Pixel {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.red = 0;
        this.green = 0;
        this.blue = 0;
        this.alpha = 0;
        this.opacity = 0;
    }
    id = () => {return pxid(this.x, this.y);}
    elem = () => {return document.getElementById(getpx(this.x, this.y));}
    code = () => {
        return `<td id="${this.id()}" style="width: ${tileSize}px; height: ${tileSize}px; border: ${strokeWidth}px dashed; background-color: ${backgroundColor}; opacity:${this.opacity}"></td>`
    }
}

class Row {
    constructor() {
        this.pixels = {}
    }
}

class Grid {
    constructor() {
        // self.pixels = {pxid(x, y): Pixel(x, y) for x in range(self.width) for y in range(self.height)}
        this.pixels = {};
        for (let x; x < this.width(); x++) {
            for (let y; y < this.height(); y++) {
                self.pixels[pixid(x, y)] = new Pixel(x, y);
            }
        }
    }
    width() {
        return parseInt(document.getElementById('widthInput').value);
    }
    height() {
        return parseInt(document.getElementById('heightInput').value);
    }

    rows() {
        // return [[this.pixels[pxid(x, y)] for x in range(this.width)] for y in range(this.height)];
        const result = [];
        for (let y of range(this.height)) {
            const rack = [];
            for (let x of range(this.width)) {
                rack.push(pixid(x, y))    
            }
            result.push(rack);
        }
    }
    // columns() {
    //     return [*zip(*this.rows)];
    // }
    
    head() {
        return '<table id="sketchpad" style="float:inherit; border: 1px dashed">\n\t';
    }
    inner() {
        let lines = '';
        for (let row of this.rows) {
            let line = '<tr>';
            for (let pixel of row) {
                line += pixel.code();
            }
            lines += line;
        }
        return lines + '</tr>';
    }
    tail() {
        return '</table>';
    }
    code() {
        return this.head() + this.inner() + this.tail();
    }
}

function setGrid() {
    pixelBox.innerHtml = grid.code();
    for (let px of grid.pixels) {
        px.elem().addEventListener('click', function(){
            px.red = currentColour[0];
            px.green = currentColour[1];
            px.blue = currentColour[2];
            px.alpha = currentColour[3];
        })
    }
}
function init() {
    grid = Grid();
    setGrid();
}




