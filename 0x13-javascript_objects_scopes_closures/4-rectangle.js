
#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const xLine = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(xLine);
    }
  }

  rotate (){
    const placeHolder = this.width;
    this.width = this.height;
    this.height = placeHolder;
  }

  double (){
    this.width *= 2;
    this.height *=2;
  }
}

module.exports = Rectangle;
