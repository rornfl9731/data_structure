'''
Given a string of opening and closing parentheses,
check whether it’s balanced. We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}.
Assume that the string doesn’t contain any other character than these, no spaces words or numbers.
As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened.
For example ‘([])’ is balanced but ‘([)]’ is not.

You can assume the input string has no spaces.
'''


def balance_check(s):

    stack=[]

    if len(s)%2==1:     #괄호 갯수가 홀수개이면 무조건 틀림
        return False

    for i in s:
        if i=='{' or i=='(' or i=='[':
            stack.append(i)

        if i=='}':
            if stack[-1]=='{':

                stack.pop()

        if i==']':
            if stack[-1]=='[':
                stack.pop()

        if i==')':
            if stack[-1]=='(':
                stack.pop()

    return stack==[]

print(balance_check('[](){([[[]]])}'))

print(balance_check('()(){]}'))

from nose.tools import assert_equal


class TestBalanceCheck(object):
    def test(self, sol):
        assert_equal(sol('[](){([[[]]])}('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        print('ALL TEST CASES PASSED')


# Run Tests

t = TestBalanceCheck()
t.test(balance_check)

'''
모범답안
def balance_check(s):
    
    # Check is even number of brackets
    if len(s)%2 != 0:
        return False
    
    # Set of opening brackets
    opening = set('([{') 
    
    # Matching Pairs
    matches = set([ ('(',')'), ('[',']'), ('{','}') ]) 
    
    # Use a list as a "Stack"
    stack = []
    
    # Check every parenthesis in string
    for paren in s:
        
        # If its an opening, append it to list
        if paren in opening:
            stack.append(paren)
        
        else:
            
            # Check that there are parentheses in Stack
            if len(stack) == 0:
                return False
            
            # Check the last open parenthesis
            last_open = stack.pop()
            
            # Check if it has a closing match
            if (last_open,paren) not in matches:
                return False
            
    return len(stack) == 0
'''

