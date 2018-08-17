bits = ['0', '1']
def execute_boolean_operation(str):
    op = str.split()
    if op[0] in bits and op[2] in bits:
        if op[1] == '+':
            if op[0] == '1' or op[2] == '1':
                return True
            else:
                return False
        elif op[1] == '.':
            if op[0] == '1' and op[2] == '1':
                return True
            else:
                return False
        else:
            return 'unknown operation.'
    else:
        return 'unknown operands.'

print('1 + 1 = ' + str(execute_boolean_operation('1 + 1')))
print('1 + 0 = ' + str(execute_boolean_operation('1 + 0')))
print('0 + 1 = ' + str(execute_boolean_operation('0 + 1')))
print('0 + 0 = ' + str(execute_boolean_operation('0 + 0')))
print()
print('1 . 1 = ' + str(execute_boolean_operation('1 . 1')))
print('1 . 0 = ' + str(execute_boolean_operation('1 . 0')))
print('0 . 1 = ' + str(execute_boolean_operation('0 . 1')))
print('0 . 0 = ' + str(execute_boolean_operation('0 . 0')))