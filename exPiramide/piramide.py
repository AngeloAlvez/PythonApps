
def criaPiramide(n):
    for i in range(n+1):
        if i > 0:
            print(str(i)*i)
  


tamanho = int(input('Qual é o tamanho da piramide?'))
criaPiramide(tamanho)