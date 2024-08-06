def solution(brown, yellow):
    sum = brown + yellow
    answer = []
    for row in range(int(sum**0.5), sum+1):
        if sum % row == 0:
            column = sum // row
            if row < column:
                row, column = column, row
            answer.append(row)
            answer.append(column)
            break
    return answer

solution(10, 2)