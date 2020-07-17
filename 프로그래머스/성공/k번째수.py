array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for i in commands:
        array2=array[i[0]-1:i[1]]
        array2.sort()

        answer.append(array2[i[2]-1])
    return answer

print(solution(array, commands))
