a, m, d, n = map(int, input().split())
md_list = [a]
x = 0
while True:
    mdx = md_list[x]
    if x + 1 == n:
        print(mdx)
        break
    md_list.append(mdx * m + d)
    x += 1