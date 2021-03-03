def solution(numbers, hand):
    answer = ''
    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              ['*', 0, '#']]
    lefts=[1,4,7]
    rights=[3,6,9]
    others=[2,5,8,0]

    left=[3,0]
    right=[3,2]

    for number in numbers:
        if number in lefts:
            answer+='L'
            left=[lefts.index(number),0]
        elif number in rights:
            answer += 'R'
            right=[rights.index(number),2]
        else:
            if abs(others.index(number)-left[0])+abs(left[1]-1)<abs(others.index(number)-right[0])+abs(right[1]-1):
                answer += 'L'
                left = [others.index(number),1]
            elif abs(others.index(number)-left[0])+abs(left[1]-1)>abs(others.index(number)-right[0])+abs(right[1]-1):
                answer += 'R'
                right = [others.index(number),1]
            else:
                if hand=="right":
                    answer += 'R'
                    right = [others.index(number), 1]
                else:
                    answer += 'L'
                    left = [others.index(number), 1]
    return answer
