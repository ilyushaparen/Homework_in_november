def max_sonlar(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    return max(a,b,c)
print(max_sonlar(25, 50, 75))



def text_list(*text_list):
    title_list = []
    for text in text_list:
        title_list.append(text.title())
    return title_list

print(text_list("bahodir", "jonibek", "artur"))
