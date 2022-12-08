# Curva de Bézier Cúbica em p5.js

A ideia desta construção é produzir uma curva de Bézier com grau 3 (cúbica). A equação paramétrica dessa curva é dada por:

$$P = (1−t)^3 P_1 + 3(1−t)^2 tP_2 + 3(1−t)t^2 P_3 + t^3 P_4$$

## Lógica
Fixei 3 pontos em posições arbitrárias e o 4º é definido pela posição do mouse.


## Código principal

```js
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
  
  //function draw
    ...
    noFill();
    beginShape();
    for (let t = 0; t <= 1; t += 0.01) {
        A = coordenadas(p1, p2, p3, p4, t);
        vertex(A.x, A.y);
    }
    endShape();
    ...
```

## Comandos para executar
Com o terminal aberto nesse diretório...
- Linux:  rode o comando:
> open ./index.html
- Windows: 
> start ./index.html