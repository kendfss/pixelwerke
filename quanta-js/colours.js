const hexes_names = { "#000000": "Black", "#000080": "Navy", "#00008B": "DarkBlue", "#0000CD": "MediumBlue", "#0000FF": "Blue", "#006400": "DarkGreen", "#008000": "Green", "#008080": "Teal", "#008B8B": "DarkCyan", "#00BFFF": "DeepSkyBlue", "#00CED1": "DarkTurquoise", "#00FA9A": "MediumSpringGreen", "#00FF00": "Lime", "#00FF7F": "SpringGreen", "#00FFFF": "Cyan", "#191970": "MidnightBlue", "#1E90FF": "DodgerBlue", "#20B2AA": "LightSeaGreen", "#228B22": "ForestGreen", "#2E8B57": "SeaGreen", "#2F4F4F": "DarkSlateGrey", "#32CD32": "LimeGreen", "#3CB371": "MediumSeaGreen", "#40E0D0": "Turquoise", "#4169E1": "RoyalBlue", "#4682B4": "SteelBlue", "#483D8B": "DarkSlateBlue", "#48D1CC": "MediumTurquoise", "#4B0082": "Indigo  ", "#556B2F": "DarkOliveGreen", "#5F9EA0": "CadetBlue", "#6495ED": "CornflowerBlue", "#663399": "RebeccaPurple", "#66CDAA": "MediumAquaMarine", "#696969": "DimGrey", "#6A5ACD": "SlateBlue", "#6B8E23": "OliveDrab", "#708090": "SlateGrey", "#778899": "LightSlateGrey", "#7B68EE": "MediumSlateBlue", "#7CFC00": "LawnGreen", "#7FFF00": "Chartreuse", "#7FFFD4": "Aquamarine", "#800000": "Maroon", "#800080": "Purple", "#808000": "Olive", "#808080": "Grey", "#87CEEB": "SkyBlue", "#87CEFA": "LightSkyBlue", "#8A2BE2": "BlueViolet", "#8B0000": "DarkRed", "#8B008B": "DarkMagenta", "#8B4513": "SaddleBrown", "#8FBC8F": "DarkSeaGreen", "#90EE90": "LightGreen", "#9370DB": "MediumPurple", "#9400D3": "DarkViolet", "#98FB98": "PaleGreen", "#9932CC": "DarkOrchid", "#9ACD32": "YellowGreen", "#A0522D": "Sienna", "#A52A2A": "Brown", "#A9A9A9": "DarkGrey", "#ADD8E6": "LightBlue", "#ADFF2F": "GreenYellow", "#AFEEEE": "PaleTurquoise", "#B0C4DE": "LightSteelBlue", "#B0E0E6": "PowderBlue", "#B22222": "FireBrick", "#B8860B": "DarkGoldenRod", "#BA55D3": "MediumOrchid", "#BC8F8F": "RosyBrown", "#BDB76B": "DarkKhaki", "#C0C0C0": "Silver", "#C71585": "MediumVioletRed", "#CD5C5C": "IndianRed ", "#CD853F": "Peru", "#D2691E": "Chocolate", "#D2B48C": "Tan", "#D3D3D3": "LightGrey", "#D8BFD8": "Thistle", "#DA70D6": "Orchid", "#DAA520": "GoldenRod", "#DB7093": "PaleVioletRed", "#DC143C": "Crimson", "#DCDCDC": "Gainsboro", "#DDA0DD": "Plum", "#DEB887": "BurlyWood", "#E0FFFF": "LightCyan", "#E6E6FA": "Lavender", "#E9967A": "DarkSalmon", "#EE82EE": "Violet", "#EEE8AA": "PaleGoldenRod", "#F08080": "LightCoral", "#F0E68C": "Khaki", "#F0F8FF": "AliceBlue", "#F0FFF0": "HoneyDew", "#F0FFFF": "Azure", "#F4A460": "SandyBrown", "#F5DEB3": "Wheat", "#F5F5DC": "Beige", "#F5F5F5": "WhiteSmoke", "#F5FFFA": "MintCream", "#F8F8FF": "GhostWhite", "#FA8072": "Salmon", "#FAEBD7": "AntiqueWhite", "#FAF0E6": "Linen", "#FAFAD2": "LightGoldenRodYellow", "#FDF5E6": "OldLace", "#FF0000": "Red", "#FF00FF": "Magenta", "#FF1493": "DeepPink", "#FF4500": "OrangeRed", "#FF6347": "Tomato", "#FF69B4": "HotPink", "#FF7F50": "Coral", "#FF8C00": "DarkOrange", "#FFA07A": "LightSalmon", "#FFA500": "Orange", "#FFB6C1": "LightPink", "#FFC0CB": "Pink", "#FFD700": "Gold", "#FFDAB9": "PeachPuff", "#FFDEAD": "NavajoWhite", "#FFE4B5": "Moccasin", "#FFE4C4": "Bisque", "#FFE4E1": "MistyRose", "#FFEBCD": "BlanchedAlmond", "#FFEFD5": "PapayaWhip", "#FFF0F5": "LavenderBlush", "#FFF5EE": "SeaShell", "#FFF8DC": "Cornsilk", "#FFFACD": "LemonChiffon", "#FFFAF0": "FloralWhite", "#FFFAFA": "Snow", "#FFFF00": "Yellow", "#FFFFE0": "LightYellow", "#FFFFF0": "Ivory", "#FFFFFF": "White" }
const names_hexes = { "AliceBlue": "#F0F8FF", "AntiqueWhite": "#FAEBD7", "Aqua": "#00FFFF", "Aquamarine": "#7FFFD4", "Azure": "#F0FFFF", "Beige": "#F5F5DC", "Bisque": "#FFE4C4", "Black": "#000000", "BlanchedAlmond": "#FFEBCD", "Blue": "#0000FF", "BlueViolet": "#8A2BE2", "Brown": "#A52A2A", "BurlyWood": "#DEB887", "CadetBlue": "#5F9EA0", "Chartreuse": "#7FFF00", "Chocolate": "#D2691E", "Coral": "#FF7F50", "CornflowerBlue": "#6495ED", "Cornsilk": "#FFF8DC", "Crimson": "#DC143C", "Cyan": "#00FFFF", "DarkBlue": "#00008B", "DarkCyan": "#008B8B", "DarkGoldenRod": "#B8860B", "DarkGray": "#A9A9A9", "DarkGreen": "#006400", "DarkGrey": "#A9A9A9", "DarkKhaki": "#BDB76B", "DarkMagenta": "#8B008B", "DarkOliveGreen": "#556B2F", "DarkOrange": "#FF8C00", "DarkOrchid": "#9932CC", "DarkRed": "#8B0000", "DarkSalmon": "#E9967A", "DarkSeaGreen": "#8FBC8F", "DarkSlateBlue": "#483D8B", "DarkSlateGray": "#2F4F4F", "DarkSlateGrey": "#2F4F4F", "DarkTurquoise": "#00CED1", "DarkViolet": "#9400D3", "DeepPink": "#FF1493", "DeepSkyBlue": "#00BFFF", "DimGray": "#696969", "DimGrey": "#696969", "DodgerBlue": "#1E90FF", "FireBrick": "#B22222", "FloralWhite": "#FFFAF0", "ForestGreen": "#228B22", "Fuchsia": "#FF00FF", "Gainsboro": "#DCDCDC", "GhostWhite": "#F8F8FF", "Gold": "#FFD700", "GoldenRod": "#DAA520", "Gray": "#808080", "Green": "#008000", "GreenYellow": "#ADFF2F", "Grey": "#808080", "HoneyDew": "#F0FFF0", "HotPink": "#FF69B4", "IndianRed ": "#CD5C5C", "Indigo  ": "#4B0082", "Ivory": "#FFFFF0", "Khaki": "#F0E68C", "Lavender": "#E6E6FA", "LavenderBlush": "#FFF0F5", "LawnGreen": "#7CFC00", "LemonChiffon": "#FFFACD", "LightBlue": "#ADD8E6", "LightCoral": "#F08080", "LightCyan": "#E0FFFF", "LightGoldenRodYellow": "#FAFAD2", "LightGray": "#D3D3D3", "LightGreen": "#90EE90", "LightGrey": "#D3D3D3", "LightPink": "#FFB6C1", "LightSalmon": "#FFA07A", "LightSeaGreen": "#20B2AA", "LightSkyBlue": "#87CEFA", "LightSlateGray": "#778899", "LightSlateGrey": "#778899", "LightSteelBlue": "#B0C4DE", "LightYellow": "#FFFFE0", "Lime": "#00FF00", "LimeGreen": "#32CD32", "Linen": "#FAF0E6", "Magenta": "#FF00FF", "Maroon": "#800000", "MediumAquaMarine": "#66CDAA", "MediumBlue": "#0000CD", "MediumOrchid": "#BA55D3", "MediumPurple": "#9370DB", "MediumSeaGreen": "#3CB371", "MediumSlateBlue": "#7B68EE", "MediumSpringGreen": "#00FA9A", "MediumTurquoise": "#48D1CC", "MediumVioletRed": "#C71585", "MidnightBlue": "#191970", "MintCream": "#F5FFFA", "MistyRose": "#FFE4E1", "Moccasin": "#FFE4B5", "NavajoWhite": "#FFDEAD", "Navy": "#000080", "OldLace": "#FDF5E6", "Olive": "#808000", "OliveDrab": "#6B8E23", "Orange": "#FFA500", "OrangeRed": "#FF4500", "Orchid": "#DA70D6", "PaleGoldenRod": "#EEE8AA", "PaleGreen": "#98FB98", "PaleTurquoise": "#AFEEEE", "PaleVioletRed": "#DB7093", "PapayaWhip": "#FFEFD5", "PeachPuff": "#FFDAB9", "Peru": "#CD853F", "Pink": "#FFC0CB", "Plum": "#DDA0DD", "PowderBlue": "#B0E0E6", "Purple": "#800080", "RebeccaPurple": "#663399", "Red": "#FF0000", "RosyBrown": "#BC8F8F", "RoyalBlue": "#4169E1", "SaddleBrown": "#8B4513", "Salmon": "#FA8072", "SandyBrown": "#F4A460", "SeaGreen": "#2E8B57", "SeaShell": "#FFF5EE", "Sienna": "#A0522D", "Silver": "#C0C0C0", "SkyBlue": "#87CEEB", "SlateBlue": "#6A5ACD", "SlateGray": "#708090", "SlateGrey": "#708090", "Snow": "#FFFAFA", "SpringGreen": "#00FF7F", "SteelBlue": "#4682B4", "Tan": "#D2B48C", "Teal": "#008080", "Thistle": "#D8BFD8", "Tomato": "#FF6347", "Turquoise": "#40E0D0", "Violet": "#EE82EE", "Wheat": "#F5DEB3", "White": "#FFFFFF", "WhiteSmoke": "#F5F5F5", "Yellow": "#FFFF00", "YellowGreen": "#9ACD32" }
const colour_names = ["AliceBlue", "AntiqueWhite", "Aqua", "Aquamarine", "Azure", "Beige", "Bisque", "Black", "BlanchedAlmond", "Blue", "BlueViolet", "Brown", "BurlyWood", "CadetBlue", "Chartreuse", "Chocolate", "Coral", "CornflowerBlue", "Cornsilk", "Crimson", "Cyan", "DarkBlue", "DarkCyan", "DarkGoldenRod", "DarkGray", "DarkGrey", "DarkGreen", "DarkKhaki", "DarkMagenta", "DarkOliveGreen", "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGray", "DarkSlateGrey", "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue", "DimGray", "DimGrey", "DodgerBlue", "FireBrick", "FloralWhite", "ForestGreen", "Fuchsia", "Gainsboro", "GhostWhite", "Gold", "GoldenRod", "Gray", "Grey", "Green", "GreenYellow", "HoneyDew", "HotPink", "IndianRed ", "Indigo  ", "Ivory", "Khaki", "Lavender", "LavenderBlush", "LawnGreen", "LemonChiffon", "LightBlue", "LightCoral", "LightCyan", "LightGoldenRodYellow", "LightGray", "LightGrey", "LightGreen", "LightPink", "LightSalmon", "LightSeaGreen", "LightSkyBlue", "LightSlateGray", "LightSlateGrey", "LightSteelBlue", "LightYellow", "Lime", "LimeGreen", "Linen", "Magenta", "Maroon", "MediumAquaMarine", "MediumBlue", "MediumOrchid", "MediumPurple", "MediumSeaGreen", "MediumSlateBlue", "MediumSpringGreen", "MediumTurquoise", "MediumVioletRed", "MidnightBlue", "MintCream", "MistyRose", "Moccasin", "NavajoWhite", "Navy", "OldLace", "Olive", "OliveDrab", "Orange", "OrangeRed", "Orchid", "PaleGoldenRod", "PaleGreen", "PaleTurquoise", "PaleVioletRed", "PapayaWhip", "PeachPuff", "Peru", "Pink", "Plum", "PowderBlue", "Purple", "RebeccaPurple", "Red", "RosyBrown", "RoyalBlue", "SaddleBrown", "Salmon", "SandyBrown", "SeaGreen", "SeaShell", "Sienna", "Silver", "SkyBlue", "SlateBlue", "SlateGray", "SlateGrey", "Snow", "SpringGreen", "SteelBlue", "Tan", "Teal", "Thistle", "Tomato", "Turquoise", "Violet", "Wheat", "White", "WhiteSmoke", "Yellow", "YellowGreen"]
const colour_hexes = ["#F0F8FF", "#FAEBD7", "#00FFFF", "#7FFFD4", "#F0FFFF", "#F5F5DC", "#FFE4C4", "#000000", "#FFEBCD", "#0000FF", "#8A2BE2", "#A52A2A", "#DEB887", "#5F9EA0", "#7FFF00", "#D2691E", "#FF7F50", "#6495ED", "#FFF8DC", "#DC143C", "#00FFFF", "#00008B", "#008B8B", "#B8860B", "#A9A9A9", "#A9A9A9", "#006400", "#BDB76B", "#8B008B", "#556B2F", "#FF8C00", "#9932CC", "#8B0000", "#E9967A", "#8FBC8F", "#483D8B", "#2F4F4F", "#2F4F4F", "#00CED1", "#9400D3", "#FF1493", "#00BFFF", "#696969", "#696969", "#1E90FF", "#B22222", "#FFFAF0", "#228B22", "#FF00FF", "#DCDCDC", "#F8F8FF", "#FFD700", "#DAA520", "#808080", "#808080", "#008000", "#ADFF2F", "#F0FFF0", "#FF69B4", "#CD5C5C", "#4B0082", "#FFFFF0", "#F0E68C", "#E6E6FA", "#FFF0F5", "#7CFC00", "#FFFACD", "#ADD8E6", "#F08080", "#E0FFFF", "#FAFAD2", "#D3D3D3", "#D3D3D3", "#90EE90", "#FFB6C1", "#FFA07A", "#20B2AA", "#87CEFA", "#778899", "#778899", "#B0C4DE", "#FFFFE0", "#00FF00", "#32CD32", "#FAF0E6", "#FF00FF", "#800000", "#66CDAA", "#0000CD", "#BA55D3", "#9370DB", "#3CB371", "#7B68EE", "#00FA9A", "#48D1CC", "#C71585", "#191970", "#F5FFFA", "#FFE4E1", "#FFE4B5", "#FFDEAD", "#000080", "#FDF5E6", "#808000", "#6B8E23", "#FFA500", "#FF4500", "#DA70D6", "#EEE8AA", "#98FB98", "#AFEEEE", "#DB7093", "#FFEFD5", "#FFDAB9", "#CD853F", "#FFC0CB", "#DDA0DD", "#B0E0E6", "#800080", "#663399", "#FF0000", "#BC8F8F", "#4169E1", "#8B4513", "#FA8072", "#F4A460", "#2E8B57", "#FFF5EE", "#A0522D", "#C0C0C0", "#87CEEB", "#6A5ACD", "#708090", "#708090", "#FFFAFA", "#00FF7F", "#4682B4", "#D2B48C", "#008080", "#D8BFD8", "#FF6347", "#40E0D0", "#EE82EE", "#F5DEB3", "#FFFFFF", "#F5F5F5", "#FFFF00", "#9ACD32"]
const test_colours = { 'White': { 'hex': '#FFFFFF', 'rgb': [255, 255, 255], 'hsl': [0, 0, 100], }, 'Red': { 'hex': '#FF0000', 'rgb': [255, 0, 0], 'hsl': [0, 100, 50], }, 'Lime': { 'hex': '#00FF00', 'rgb': [0, 255, 0], 'hsl': [120, 100, 50], }, 'Blue': { 'hex': '#0000FF', 'rgb': [0, 0, 255], 'hsl': [240, 100, 50], }, 'Yellow': { 'hex': '#FFFF00', 'rgb': [255, 255, 0], 'hsl': [60, 100, 50], }, 'Cyan': { 'hex': '#00FFFF', 'rgb': [0, 255, 255], 'hsl': [180, 100, 50], }, 'Magenta': { 'hex': '#FF00FF', 'rgb': [255, 0, 255], 'hsl': [300, 100, 50], }, 'Silver': { 'hex': '#BFBFBF', 'rgb': [191, 191, 191], 'hsl': [0, 0, 75], }, 'Gray': { 'hex': '#808080', 'rgb': [128, 128, 128], 'hsl': [0, 0, 50], }, 'Maroon': { 'hex': '#800000', 'rgb': [128, 0, 0], 'hsl': [0, 100, 25], }, 'Olive': { 'hex': '#808000', 'rgb': [128, 128, 0], 'hsl': [60, 100, 25], }, 'Green': { 'hex': '#008000', 'rgb': [0, 128, 0], 'hsl': [120, 100, 25], }, 'Purple': { 'hex': '#800080', 'rgb': [128, 0, 128], 'hsl': [300, 100, 25], }, 'Teal': { 'hex': '#008080', 'rgb': [0, 128, 128], 'hsl': [180, 100, 25], }, 'Navy': { 'hex': '#000080', 'rgb': [0, 0, 128], 'hsl': [240, 100, 25], }, }
const clrs = "White Red Lime Blue Yellow Cyan Magenta Silver Gray Maroon Olive Green Purple Teal Navy".split(' ')

function hsl(hue, saturation, lightness) {
    return `hsl(${hue}, ${saturation}%, ${lightness}%)`;
}

function rgb(red, green, blue) {
    return `rgb(${red}, ${green}, ${blue})`;
}

function cmyk(cyan, magenta, yellow, black) {
    return `cmyk(${cyan}, ${magenta}, ${yellow}, ${black})`
}

function cmyk2rgb(cmyk) {
    const red = 255 * (1 - cmyk[0] / 100) * (1 - cmyk[3] / 100);
    const green = 255 * (1 - cmyk[1] / 100) * (1 - cmyk[3] / 100);
    const blue = 255 * (1 - cmyk[2] / 100) * (1 - cmyk[3] / 100);
    return [red, green, blue];
}

function rgb2cmyk(rgb) {
    const black = 1 - (max(rgb) / 255);
    const cyan = (1 - rgb[0] / 255 - black) / (1 - black);
    const magenta = (1 - rgb[1] / 255 - black) / (1 - black);
    const yellow = (1 - rgb[2] / 255 - black) / (1 - black);
    return [cyan, magenta, yellow, black];
}

function hex2rgb(hexstr) {
    hexstr = normalizeHex(hexstr);
    const hex = striphex(hexstr);
    var li = 0;
    var ri = 2;
    var result = [];
    for (i of range(3)) {
        let part = hex.slice(li, ri);
        let dec = toDec(part);
        result.push(dec);
        li += 2;
        ri += 2;
    }
    return result;
}

function rgb2hex(rgb) {
    const result = ['#'];
    for (let e of rgb) {
        e = toHex(e);
        e = (e.length && e.length < 2) ? ('0' + e) : e;
        result.push(e);
    }
    return result.join('');
}
// rgb2hex([ 0, 0, 128 ]);
function normalizeRGB(e) {
    if (e > 255) {
        return 255;
    } else if (e < 0) {
        return 0;
    } else {
        return e;
    }
}

function normalizeSL(e) {
    if (e > 1) {
        return 1;
    } else if (e < 0) {
        return 0;
    } else {
        return e;
    }
}

function restoreSL(e) {
    if (e < 0) {
        return restoreSL(Math.abs(e));
    } else if (e <= 1) {
        return parseInt(e * 100);
    } else {
        return parseInt(e)
    }
}

function rgb2hsl(rgb) {
    rgb = rgb.map(normalizeRGB);
    const r = rgb[0] / 255;
    const g = rgb[1] / 255;
    const b = rgb[2] / 255;
    const cmax = max([r, g, b]);
    const cmin = min([r, g, b]);
    const delta = cmax - cmin;
    const lightness = (cmax + cmin) / 2;
    let hue;
    let saturation;
    if (delta === 0) {
        hue = 0;
        saturation = 0;
    } else {
        saturation = delta / (1 - Math.abs(2 * lightness - 1));
        // hue = d2r(60);
        hue = 60;
        if (cmax === r) {
            hue *= (((g - b) / delta) % 6);
        } else if (cmax === g) {
            hue *= (((b - r) / delta) + 2);
        } else if (cmax === b) {
            hue *= (((r - g) / delta) + 4);
        }
    }
    // return [hue, saturation, lightness].map((x) => {return x * 100;});
    // return [hue, saturation * 100, lightness * 100].map(parseInt);
    return [hue, saturation * 100, lightness * 100].map(Math.abs);
}

function hsl2rgb(hsl) {
    var r;
    var g;
    var b;
    const h = hsl[0];
    const s = normalizeSL(hsl[1]);
    const l = normalizeSL(hsl[2]);
    const c = (1 - (2 * l - 1)) * s;
    const m = l - (c / 2);
    const x = c * (1 - Math.abs(((h / 60) % 2) - 1));
    if (0 <= h || h < 60) {
        r = c;
        g = x;
        b = 0;
    } else if (60 <= h || h < 120) {
        r = x;
        g = c;
        b = 0;
    } else if (120 <= h || h < 180) {
        r = 0;
        g = c;
        b = x;
    } else if (180 <= h || h < 240) {
        r = 0;
        g = x;
        b = c;
    } else if (240 <= h || h < 300) {
        r = x;
        g = 0;
        b = c;
    } else if (300 <= h || h < 360) {
        r = c;
        g = 0;
        b = x;
    }
    r = (r + m) * 255;
    g = (g + m) * 255;
    b = (b + m) * 255;
    // return [r, g, b].map((x) => {return x/100;});
    // return [r, g, b].map((x) => {return parseInt(x/100)});
    return [r, g, b].map(Math.abs);
    // return [r, g, b];
}

function test_inverses(colour) {
    // console.log('\n\n\n\n-------------------------');
    console.log('-------------------------');
    const results = [];
    const data = test_colours[colour];
    const hex = data.hex.toLowerCase();
    const rgb = data.rgb; //.map(String).map(parseInt);
    const hsl = data.hsl; //.map(String).map(parseInt);
    // console.log(`${colour}\n\t${hex}\n\t${rgb}\n\t${hsl}`);
    console.log(colour);
    console.log(hex);
    console.log(rgb);
    console.log(hsl);
    console.log()
    console.log(hex2rgb(hex));
    console.log(rgb2hex(hex2rgb(hex)));
    console.log()
    console.log(hsl2rgb(hsl));
    console.log(rgb2hsl(hsl2rgb(hsl)));
    console.log()
    console.log(rgb2hsl(rgb));
    console.log(hsl2rgb(rgb2hsl(rgb)));
    console.log()
    console.log(rgb2hex(rgb));
    console.log(hex2rgb(rgb2hex(rgb)));
    console.log()


    results.push(rgb2hex(hex2rgb(hex)) == hex);
    results.push(rgb2hsl(hsl2rgb(hsl)) == hsl);
    results.push(hex2rgb(rgb2hex(rgb)) == rgb);
    console.log(results);
    console.log(all(results));
    console.log('-------------------------\n\n\n\n');
    return all(results);
}
// test_inverses(clrs[0]);
function test() {
    clrs.map(test_inverses).map(console.log);
}
test()

function test_hexrgb() {
    const results = [];
    for (let c of clrs) {
        data = test_colours[c];
        hex = data.hex.toLowerCase();
        rgb = data.rgb;
        _h = rgb2hex(rgb);
        _r = hex2rgb(hex);
        // results.push(rgb2hex(rgb) == hex);
        if (!(_h == hex)) {
            results.push(false);
            console.log(`hex error @ ${c}\n\t${_h} => ${hex}`);
            console.log(variance([hex, _h].map(ascii.indexOf)));
        } else {
            results.push(true);
        }
        if (!(_r == rgb)) {
            results.push(false);
            console.log(`rgb error @ ${c}\n\t${_r} => ${rgb}`);
            console.log(variance([rgb, _r]));
        } else {
            results.push(true);
        }

        // results.push(hex2rgb(hex) == rgb);
    }
    console.log(results);
    return all(results);
}
test_hexrgb();