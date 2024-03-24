class Stack:
    def __init__(self, *values):
        self.__stack = []
        self.insert_items(*values)
    
    def get_stack(self):
        return self.__stack

    def insert_item(self, value):
        self.get_stack().append(value)

    def insert_items(self, *values):
        for i in values:
            self.insert_item(i)
    
    def pop(self):
        item = self.get_stack()[-1]
        self.get_stack().pop()
        return item
    
    def length(self):
        return len(self.get_stack())
    
p1 = Stack()
p2 = Stack('RE','CI','FE')

p1.insert_item(1981)
p1.insert_item(1982)
p1.insert_item(1983)

print('Pilha 2: ', end='')
print(*p2.get_stack(), sep=', ')

print('O tamanho da pilha 1 é', p1.length())

print("Pilha 1: ", end='')
print(*p1.get_stack(), sep=', ')

print(p1.pop())

print("Pilha 1: ", end='')
print(*p1.get_stack(), sep=', ')

print('O tamanho da pilha 1 é', p1.length())

print(p1.get_stack().count(1981))