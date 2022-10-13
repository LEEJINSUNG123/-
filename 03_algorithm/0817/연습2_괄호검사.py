def check_matching(data):
    for i in range(len(data)):
        # 왼쪽괄호 일때 : push
        if data[i] == '(':
            stack.append(data[i])
        # 오른쪽괄호 일때 : pop
        elif data[i] == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    # stack에 남아 있으면 False
    if stack:
        return False
    else:
        return True

stack = []
# str1 = '( )( )((( )))'      # True
str1 = '((( )((((( )( )((( )( ))((( ))))))' # False
print(check_matching(str1))

