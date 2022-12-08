# Pirâmide e Prisma em OpenGL

Nesta tarefa foram realizadas duas construções: um Prisma e uma Pirâmide.

## Lógica
Por se tratar de polígonos com poucos vértices, estes foram mapeados manualmente. Na pirâmide contamos com 5 vértices, 
enquanto que no prisma são 6. Assim separei as coordenadas de cada vértice e em seguida, montei as faces de acordo com 
os índices dos vértices correspondentes. 

### Pirâmide
Para a pirâmide utilizei um `for` iterando pelas faces e mais um aninhado iterando pelos vértices de cada face.
Dessa forma foi possível produzir os 3 triângulos necessários. Para a base quadrada, utilizei a primitica `GL_QUADS`
sem necessidade de loops.

### Prisma
Para o prisma precisei de dois arrays de faces: um para os lados e outro para as extremidades.
Com isso, decidi produzir um prisma triangular regular e assim utilizei `GL_TRIANGLES` para as extremidades
e `GL_QUADS` para os lados.

## Código principal

### Pirâmide
```python
  def Piramide():
    glBegin(GL_TRIANGLES)
    i = 0
    for face in faces:
        # glColor3fv(cores[i])
        for vertex in face:
            glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])
        i = i + 1
    glEnd()
    glBegin(GL_QUADS)
    for v in (1, 2, 3, 4):
        glColor3fv(cores[v])
        glVertex3fv(vertices[v])
    glEnd()
```

### Prisma

```python
def Prisma():
    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        # glColor3fv(cores[i])
        for vertex in face:
            glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])
        i = i + 1
    glEnd()
    glBegin(GL_TRIANGLES)
    for extremo in extremidades:
        for vert in extremo:
            glColor3fv(cores[vert])
            glVertex3fv(vertices[vert])
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
- Pirâmide:
> py ./piramide/main.py
- Prisma:
> py ./prisma/main.py
