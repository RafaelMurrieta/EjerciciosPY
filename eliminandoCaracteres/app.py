def eliminando(pal1:str, pal2:str):
    pal1.lower()
    pal2.lower()
    stack1 = []
    stack2 = []
    r1 = []
    r2 = []
    for i in range(len(pal1)):
        stack1.append(pal1[i])
    for i in range(len(pal2)):
        stack2.append(pal2[i])
    for j in range(len(stack1)):
        if stack1[j] in stack2:
            if not stack1[j] in r1: 
                r1.append(stack1[j])
    for j in range(len(stack2)):
        if stack2[j] in stack1:
            if not stack2[j] in r2:
                r2.append(stack2[j])
    r1 = ''.join(r1)
    r2 = ''.join(r2)
    print(r1)
    print(r2)
    
# eliminando("brais","moure")
eliminando("Usa el canal de nuestro discord (https://mouredev.com/discord) \"\uD83D\uDD01reto-semanal\" para preguntas, dudas o prestar ayuda a la comunidad",
        "Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.")
# eliminando("hola","holas")