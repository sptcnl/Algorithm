# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort()
    new_list = []
    for i in range(len(citations)):
        new_list.append(citations.pop())
        if len(citations) >= citations[-1]:
            break
    return len(new_list)