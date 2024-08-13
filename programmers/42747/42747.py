def solution(citations):
    citations.sort()
    new_list = []
    for i in range(len(citations)):
        new_list.append(citations.pop())
        if len(citations) >= citations[-1]:
            break
    return len(new_list)