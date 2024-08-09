# https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    answer = 0
    quotient = n / 2    # 몫 구하기, 2의 갯수 및 짝수인지 확인
    int_quotient = int(quotient)
    
    if quotient == int_quotient:
        answer += 2
        length = quotient - 1     # 1로만, 2로만 이뤄진것 제외
    else:
        answer += 1
        length = int_quotient     # 1로만 이뤄진것 제외
    for i in length:
        n += 1
        answer += n*n
        
    return answer