const ascii = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'";

function toChar(n) {
    try {
        if (n < ascii.length) {
            return ascii.charAt(n);
        } else {
            throw `Index must be lower than ${ascii.length}`
        }
        return ascii.charAt(n);
    } catch(err) {
        console.warn(err);
        // alert(err);
    }
}


function striphex(hex){
    return ((hex[0] === '#') ? hex.slice(1) : hex);
}
function normalizeHex(hexstr) {
    var hex = striphex(hexstr.toLowerCase());
    try {
        if (hex.length === 3) {
            hex = join(chooser(hex, 0, 0, 1, 1, 2, 2));
        } else if (!(hex.length === 6)) {
            throw "Hex string does not compute";
        }
    } catch(err) {
        console.warn(err);
        // alert(err);
    }
    return '#' + hex;
}
