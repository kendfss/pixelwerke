function addShift(x, y) {
  return (x << 8) + y
}

function d2r(degress) {
  return degrees / (180 / Math.PI);
}

function r2d(radians) {
  return radians * (180 / Math.PI);
}

function variance(array) {
    const mean = array.reduce((x, y) => {return x + y;}) / array.length;
    const vars = [];
    for (let e of array) {
        vars.push(e-mean);
    }
    return vars.reduce((x, y) => {return x + y;}) / vars.length;
}

function toHex(d) {
    var r = d % 16;
    if (d - r == 0) {
        return toChar(r);
    }
    return toHex((d - r) / 16) + toChar(r);
}

function toDec(arg, base=16) {
    const digits = ascii.slice(0, base);
    const argstr = arg.toString();
    var value = 0;
    for (let i of range(argstr.length)) {
        let char = argstr[i];
        let charVal = digits.indexOf(char);
        let mag = argstr.length - 1 - i;
        value += (base ** mag) * charVal;
    }
    return value;
}
