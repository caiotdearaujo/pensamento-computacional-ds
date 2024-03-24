class Stack:
    def __init__(self, *values):
        self.__stack = []
        self.push_items(*values)
    
    def get_stack(self):
        return self.__stack

    def push(self, value):
        self.get_stack().append(value)

    def push_items(self, *values):
        for i in values:
            self.push(i)
    
    def pop(self):
        item = self.get_stack()[-1]
        self.get_stack().pop()
        return item
    
    def length(self):
        return len(self.get_stack())

    def count(self, value):
        return self.get_stack().count(value)