from itertools import permutations
from copy import deepcopy
def solution(expression):
    answer = 0
    operation=['+', '-', '*']
    combs=list(permutations(operation, 3))
    replace1=expression.replace("+"," ")
    replace2=replace1.replace("-"," ")
    replace3=replace2.replace("*"," ")
    numberss=list(map(int, replace3.split()))
    operationss=[]
    for co in range(len(expression)):
        for op in operation:
            if expression[co]==op:
                operationss.append(expression[co])
    # print(numberss)
    # print(operationss)
    # print(combs)

    for comb in combs:
        numbers = deepcopy(numberss)
        operations = deepcopy(operationss)
        for co in comb:     #('+', '-', '*')
            numTemp = [numbers[0]]
            operTemp = []
            for i in range(len(operations)):
                if co==operations[i]:
                    if co=='+':
                        numTemp.append(numTemp.pop()+numbers[i+1])
                    elif co=='*':
                        numTemp.append(numTemp.pop()*numbers[i+1])
                    else:
                        numTemp.append(numTemp.pop() - numbers[i + 1])
                else:
                    numTemp.append(numbers[i+1])
                    operTemp.append(operations[i])
            numbers=deepcopy(numTemp)
            operations=deepcopy(operTemp)
        answer=max(answer, abs(numbers[0]))

    return answer


expression="100-200*300-500+20"

solution(expression)