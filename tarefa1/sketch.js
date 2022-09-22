const radius1 = 200;
const radius2 = 100;
let n = 4;
let numColors = 30;
let colorPalette = [];

function setup() {
    createCanvas(800, 600);
    generateRandomColors();
}

function draw() {
    background(200);
    translate(width / 2, height / 2);
    let [mx, my] = relativeMouse();
    let v = createVector(1, 0);
    let u = createVector(mx, my);
    rotate(v.angleBetween(u))
    n = floor(map(u.mag(), 0, width / 2, 4, 20));
    beginShape();
    for (let i = 0; i < (2 * n); i++) {
        let angle = map(i, 0, 2 * n, 0, TWO_PI);
        if (i % 2 === 0) { // Vertices externos
            vertex(radius1 * cos(angle), radius1 * sin(angle));
        } else {
            vertex(radius2 * cos(angle), radius2 * sin(angle));
        }
    }
    endShape(CLOSE);
}

function relativeMouse() {
    let mx = mouseX;
    let my = mouseY;
    let matrix = drawingContext.getTransform()
    let pd = pixelDensity()
    let rp = matrix.inverse().transformPoint(new DOMPoint(mx * pd, my * pd));
    return [rp.x, rp.y];
}

function mouseClicked() {
    let c = getShapeColor();
    fill(c);
}

const generateRandomColors = () => {
    for(let i = 0; i < numColors; i++) {
        colorPalette.push(`#${Math.floor(Math.random()*16777215).toString(16)}`);
    }
}

const getShapeColor = () => {
    return color(colorPalette[Math.floor(Math.random() * numColors)]);
}
