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
                print(stack[-1])
                stack.pop()

        if i==']':
            if stack[-1]=='[':
                print(stack[-1])
                stack.pop()

        if i==')':
            if stack[-1]=='(':
                print(stack[-1])
                stack.pop()

    return stack==[]

print(balance_check('[](){([[[]]])}'))

print(balance_check('()(){]}'))



