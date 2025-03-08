'''

Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks. pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).

FOLLOW-UP
Implement a function popAt(int index) which performs a pop operation on a specific substack.

'''


class stack:
    def __init__(self, size):
        '''

        :param size: size of each stack
        '''
        self.max_size = size
        self.stack = [[]]

    def push(self, ele):
        if len(self.stack[-1]) == self.max_size:
            self.stack.append([ele])
        else:
            self.stack[-1].append(ele)

    def pop(self):
        ele = self.stack[-1].pop()
        if not self.stack[-1]:
            self.stack.pop()
        return ele

    def roll_over(self, stack_no, stack_ele):
        for i in range(stack_ele, self.max_size-1):
            self.stack[stack_no][stack_ele] = self.stack[stack_no][stack_ele+1]
        self.stack[stack_no].pop()

    # def pop_index(self, index):
    #     if index < self.max_size:
    #         stack_no = len(self.stack)-1
    #         stack_ele = len(self.stack[-1]) - index
    #     stack_no = len(self.stack) - index//self.max_size -1
    #     stack_ele = self.max_size - (index - (index//self.max_size)*self.max_size) - 1
    #     element = self.stack[stack_no][stack_ele]
    #     self.roll_over(stack_no, stack_ele)
    #     if stack_no+1 < len(self.stack):
    #         self.stack[stack_no][-1] = self.stack[stack_no+1][0]
    #         for i in range(stack_no+1, len(self.stack)):
    #             self.roll_over(i, 0)
    #             if i + 1 < len(self.stack):
    #                 self.stack[i][-1] = self.stack[i + 1][0]
    #     return element

    def stack_no(self, index):

    def pop_index(self, index):
        stack_no = self.stack_no(index)




s = stack(3)
ele = [1,2,3,4]
for i in ele:
    s.push(i)

# s.stack_print()
# print(s.pop())
# s.stack_print()
# print(s.pop())
# s.stack_print()
print(s.pop_index(1))
s.stack_print()




