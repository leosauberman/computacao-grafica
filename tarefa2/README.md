# Polígono Estrelado em p5.js

A ideia desta construção é produzir polígonos de $n$ vértices externos, tal que quanto mais o mouse se aproxima 
do centro do polígono menor o $n$. Sendo que o menor $n$ possível é $4$, pois é a quantidade mínima suficiente
para constituir um polígono estrelado, e o maior foi arbitrariamente escolhido como $20$.

## Lógica
Existem 3 componentes principais nesse código: 
1. alterar número de vértices de acordo com a distância do mouse para o centro;
2. rotacionar o polígono na direção do mouse;
3. mudar a cor do polígono ao clicar na tela.

### Número de vértices
Para criar um polígono estrelado, utilizei uma estratégia de para cada 2 vértices externos, i.e. na maior circunferência,
inseri um vértice no circunferência menor. Assim, bastou apenas calcular os senos e cossenos e multiplicar pelo raio 
correspondente para encontrar as coordenadas.

Criei um vetor $u$ nas coordenadas relativas do mouse para em seguida mapear seu tamanho
para o intervalo de 4 a 20 e utilizar esse valor como a quantidade de vértices externos.

### Rotação do polígono
Utilizando um outro vetor unitário $v$, calculo o ângulo entre ele e o vetor $u$, rotacionando-o nesse valor.

### Mudança de cor ao clicar
Na função `setup` gero um array de cores em hexadecimal e na função `mouseClicked` escuto por um clique do mouse, 
onde sorteio e atribuo a cor do polígono.

## Código principal

```js
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
```

## Comandos para executar
Com o terminal aberto nesse diretório...
- Linux:  rode o comando:
> open ./index.html
- Windows: 
> start ./index.html
