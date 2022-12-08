# Esfera em OpenGL

Esta construção consiste em uma esfera produzida a partir da revolução de uma semi-circunferência.

## Lógica
Na função `calcVertices` realizamos o cálculo das coordenadas de cada vértice a partir das funções trigonométricas
aplicadas aos ângulos da semi-circunferência (na vertical) e da circunferência na horizontal.
Assim produzimos uma esfera com a primitiva `GL_TRIANGLE_STRIP` para que ela seja preenchida.

## Código principal

```python
def calcVertices(i, j, r, n):
    teta = ((math.pi * i) / n) - (math.pi / 2)
    phi = (2 * math.pi * j) / n
    x = r * math.cos(teta) * math.cos(phi)
    y = r * math.sin(teta)
    z = r * math.cos(teta) * math.sin(phi)

    return x, y, z, teta, phi

def Esfera(n, r):
    for i in range(n):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(n + 1):
            x, y, z, teta, phi = calcVertices(i, j, r, n)
            x1, y1, z1, teta1, phi1 = calcVertices(i+1, j, r, n)
            glColor3f(i/n, j/n, (i+j)/(2 * n))
            glVertex3f(x, y, z)
            glVertex3f(x1, y1, z1)
        glEnd()
```


## Execução

### Dependências
- [ ] Python 3
- [ ] pip

Com o pip instalado, rodar este comando no terminal:
> pip install PyOpenG pysdl2 pysdl2-dll

Após se certificar que os pacotes foram devidamente instalados e com o terminal aberto nesse diretório...

Rode o comando:
> py ./main.py