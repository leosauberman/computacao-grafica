let p1, p2, p3, p4, A;

function setup() {
    createCanvas(600, 600);
}

function ponto(A) {
    circle(A.x, A.y, 10);
    fill("#FFF");
}

function coordenadas(A, B, C, D, t) {
    return {
        x: ((1 - t) ** 3) * A.x +
            3 * t * (((1 - t) ** 2) * B.x) +
            3 * (1 - t) * (t ** 2) * C.x +
            (t ** 3) * D.x,
        y: ((1 - t) ** 3) * A.y +
            3 * t * (((1 - t) ** 2) * B.y) +
            3 * (1 - t) * (t ** 2) * C.y +
            (t ** 3) * D.y
    };
}

function draw() {
    background(200);

    p1 = {x: 10, y: height * 0.9};
    p2 = {x: width/3, y: height / 3};
    p4 = {x: width - 10, y: height * 0.1};
    p3 = {x: mouseX, y: mouseY};

    ponto(p1);
    ponto(p2);
    ponto(p3);
    ponto(p4);

    noFill();
    beginShape();
    for (let t = 0; t <= 1; t += 0.01) {
        A = coordenadas(p1, p2, p3, p4, t);
        vertex(A.x, A.y);
    }
    endShape();
}