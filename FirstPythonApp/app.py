# stack_front = ['HTML', 'CSS', 'JS', 'REACT']
# stack_back = ['HTTP', 'JS', 'NODE', 'MONGO-DB']


# def le_stack(stack):
#     if stack == 'front':
#         for tech in stack_front:
#             print('=>', tech)
#     elif stack == 'back':
#         for tech in stack_back:
#             print('=>', tech)


# print('Oi estudante de desenvolvimento. Hoje eu vou te indicar uma trilha básica de estudo baseado em sua preferência.')
# print('Vamos lá, o desenvolvimento é (sendo simplista) dividido em duas vertentes.')
# print('Front-end = é o profissional responsável por desenvolver a parte visual de um software. É por onde o usuário final interage com a aplicação.')
# print('Back-end = é o profissional que desenvolve toda a lógica e regras de negócio por trás da aplicação.')
# stack = input('Qual é sua stack favorita? (front/back)')
# print(
#     f'que bom que você gosta mais de {stack}-end. Podemos de ajudar a montar um plano de estudo.')
# trilha = input('Você deseja ver uma trilha básica específica? (s/n)')
# if trilha == 's':
#     if stack == 'front':
#         le_stack('front')
#     elif stack == 'back':
#         le_stack('back')
# else:
#     print('Sem problemas! Bons estudos!!!')

# # 51:28 on https://www.youtube.com/watch?v=iq7JLIH-sV0

def criaPiramide(n):
    for i in range(n+1):
        if i > 0:
            print(str(i)*i)
  


tamanho = int(input('Qual é o tamanho da piramide?'))
criaPiramide(tamanho)