# Malha funcional em OpenGL

Esta construção consiste em uma malha, no caso paraboloide hiperbólica,
produzida a partir da revolução de uma função específica.

## Lógica
A função `solidoFuncional` recebe uma função e um valor que define a granularidade da malha.
A função é utilizada para gerar as coordenadas dos vértices e assim obter o sólido desejado.

Na função `paraboloide` estamos definindo a função de geração do mesmo.

## Código principal

```python
def solidoFuncional(fv, n):
    v = array('f', [])

    def adiciona(lista, vertice):
        for v in vertice:
            lista.append(v)

    for i in range(n):
        for j in range(n):
            vA = fv(i, j)
            vB = fv(i, j + 1)
            vC = fv(i + 1, j + 1)
            vD = fv(i + 1, j)
            adiciona(v, vA)
            adiciona(v, vB)
            adiciona(v, vD)
            adiciona(v, vB)
            adiciona(v, vC)
            adiciona(v, vD)
    return v

def paraboloide(i, j):
    x = (2 * i / N) - 1
    y = (2 * j / N) - 1
    return x, y, x ** 2 - y ** 2
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

