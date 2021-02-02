def solution(clothes):
    cloth = {} 
    for c in clothes :
        cloth[c[1]] = cloth.get(c[1], 0) +1
        
    value = list(cloth.values())
    
    # 전체 - 모두 안입을 때
    # 전체 ex) 상의 a,b 가 있을 때 경우는 0 안입음, a 입음, b 입음 
    
    m = 1
    for v in  value :
        m *= (v+1)
        
    return m -1
