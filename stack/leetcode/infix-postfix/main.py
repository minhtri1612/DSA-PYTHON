class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.top.data

    def isOperator(self, char):
        return char in "+-*/"

    def precedence(self, char):
        if char in "+-":
            return 1
        elif char in "*/":
            return 2
        return 0

    def infixToPostfix(self, infix):
        stack = Stack()
        postfix = []

        for token in infix:
            if token.isdigit():
                postfix.append(token)
            elif self.isOperator(token):
                while (not stack.isEmpty() and self.precedence(stack.peek()) >= self.precedence(token)):
                    postfix.append(stack.pop())
                stack.push(token)

        while not stack.isEmpty():
            postfix.append(stack.pop())

        return "".join(postfix)

S = Stack()
infix = "5*4+6+7*2"
postfix = S.infixToPostfix(infix)
print(postfix)  # Expected output: 54*6+72*+
