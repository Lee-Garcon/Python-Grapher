import stack

def Stack_Postfix(lis):
    stac = stack.Stack()
    if type(lis) is str:
        lis = lis.split(' ')
    for x in lis:
        temp_store = []
        try:
            #Number
            stac.add(float(x))
        except:
            #Operator
            for i in [1, 2]:
                temp_store.append(stac.pop())
            if x == '+':
                nv = temp_store[1] + temp_store[0]
            elif x == '-':
                nv = temp_store[1] - temp_store[0]
            elif x == '*':
                nv = temp_store[1] * temp_store[0]
            elif x == '/':
                nv = temp_store[1] / temp_store[0]
            elif x == '^':
                nv = temp_store[1] ** temp_store[0]
            stac.add(float(nv))
    return int(stac.pop())
