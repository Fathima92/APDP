class Stack:

    def __init__(self):
        self.item = []
    def is_empty(self):
        return self.item == []
    def push(self,data):
        self.item.append(data)
    def pop(self):
        self.item.pop()

s = Stack()
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Quit")

    do = int(input("Enter your choice:"))
    if do == 1:
        val = input("Enter a element")
        s.push(val)
    elif do == 2:
        if s.is_empty():
            print("Stack is empty")
        else:
            print(s.pop())
    elif do == 3:
        break


