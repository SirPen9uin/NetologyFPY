from hw_stack_modules import Stack
from hw_balance import balance

if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    some_list = [1, 2, 6, 'some element']
    for item in some_list:
        stack.push(item)
    print(stack.is_empty(), list(stack))
    stack.pop()
    print(stack.peek(), stack.size())
    brackets_list = ['(((([{}]))))',
                    '[([])((([[[]]])))]{()}',
                    '{{[()]}}',
                    '}{}',
                    '{{[(])]}}',
                    '[[{())}]']
    for brackets in brackets_list:
        print(balance(brackets))