from hw_stack_modules import Stack

pairs = {'(': ')',
         '{': '}',
         '[': ']'
         }
def balance(bracket_str: str):
    stack = Stack()
    for elem in bracket_str:
        if elem in pairs:
            stack.push(elem)
        elif elem == pairs.get(stack.peek()):
            stack.pop()
        else:
            return f'Последовательность {bracket_str} несбалансирована'
    if stack.is_empty():
        return f'Последовательность {bracket_str} сбалансирована'
