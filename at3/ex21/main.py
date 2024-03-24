from stack import Stack

p1 = Stack()
p2 = Stack('RE','CI','FE')

p1.push(1981)
p1.push(1982)
p1.push(1983)

print('Pilha 2: ', end='')
print(*p2.get_stack(), sep=', ')

print('O tamanho da pilha 1 é', p1.length())

print("Pilha 1: ", end='')
print(*p1.get_stack(), sep=', ')

print(p1.pop())

print("Pilha 1: ", end='')
print(*p1.get_stack(), sep=', ')

print('O tamanho da pilha 1 é', p1.length())

print(p1.count(1981))