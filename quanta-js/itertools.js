function duplicate(sequence) {
  var resultant = [];
  for (var i = 0; i < sequence.length; i++) {
    resultant[i] = sequence[i];
  }
  return resultant;
}

function range(stop, start=0, step=1) {
  var resultant = [];
  while (start + step <= stop) {
    resultant.push(start);
    start += step;
  }
  return resultant;
}

function choice(array) {
  return array[Math.round(Math.random() * (array.length - 1))];
}

function _sample(sequence, n, once=false) {
  if ((n > sequence.length) && once) {
    throw "The sequence does not contain enough elements for the chosen sample"
  }
  var array = duplicate(sequence);
  var resultant = [];
  for (var i = 0; i < n; i++) {
    var j = choice(range(array.length));
    resultant.push(array[j]);
    if (once) {
      array.splice(j, 1);
    }
  }
  return resultant;
}

function sample(sequence, n, once=false) {
  z = _sample(sequence, n, once);
  while (!(z.every((x) => {return !(x === undefined)}))) {
    z = _sample(sequence, n, once);
  }
  return z;
}

function min(array, key=(x) => {return x;}) {
  var iterable = duplicate(array);
  var value = iterable[0];
  for (let e of iterable) {
    value = (key(e) < key(value)) ? e : value;
  }
  return value;
}

function max(array, key=(x) => {return x;}) {
  var iterable = duplicate(array);
  var value = iterable[0];
  for (let e of iterable) {
    value = (key(e) > key(value)) ? e : value;
  }
  return value;
}

function show(iterable, start=0, indices=false) {
  var msg;
  for (let i of iterable) {
    // let msg =  ?  : i;
    if (indices || start) {
      msg = `${start}\t${i}`;
    } else {
      msg = i;
    }
    console.log(msg);
    start += 1;
  }
}

function keys(obj) {
  return Array(Object.keys(obj))[0];
}

function vals(obj) {
  return Array(Object.values(obj))[0];
}

function len(obj) {
  if (obj instanceof Array || obj instanceof String) {
    return obj.length;
  } else if (obj instanceof Set) {
    ctr = 0;
    for (let e of obj) {
      ctr += 1;
    }
    return ctr;
  }
  return keys(obj).length
}

function zip(arrays) {
  // Convolve a selection of arrays
  shortest = minimum(arrays, key=len)
  box = []
  for (let i = 0; i < len(shortest); i++) {
    box[i] = []
    for (let j = 0; j < len(arrays); j++) {
      box[i][j] = arrays[j][i];
    }
  }
  return box;
}

function join(array, sep='', head='', tail='') {
  return head + array.join(sep) + tail;
}

function ints(string) {
  
  box = [];
  for (i = 0; i < string.length; i++) {
    box[i] = string.charCodeAt(i);
  }
  return box;
}

function reduce(iterable, func=(x, y) => {return x+y;}, start=0) {
  for (var e of iterable) {
    start = func(start, e);
  }
  return start;
}

function chooser(array) {
  out = new Array();
  indices = new Array(arguments);
  for (let i of range(arguments.length, 1)) {
    let arg = arguments[i.toString()];
    out.push(array[arg]);
  }
  return out;
}

function all(array) {
  for (let e of array) {
    if (!Boolean(e)) {
      return false;
    }
  }
  return true;
}

function any(array) {
  for (let e of array) {
    if (Boolean(e)) {
      return true;
    }
  }
  return false;
}

function enumerate(array, start=0) {
  const out = [];
  for (let e of array) {
    out.push([start, e]);
    start ++;
  }
  return out;
}

function list(iterable) {
  const out = [];
  for (let e of iterable) {
    out.push(e);
  }
  return out;
}

function *map(func, iterable) {
  for (let e of iterable) {
    yield func(e);
  }
}
