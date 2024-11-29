# https://codeup.kr/problem.php?id=6078
word = 'a'
while ord(word) != ord('q'):
    word = input()
    print(word)
    if ord(word) == ord('q'):
        break