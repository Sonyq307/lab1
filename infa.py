import math
import sys

text = ""
pos = 0
def probel():
    global pos
    while pos < len(text) and text[pos] == " ":
        pos += 1
def read_num():
    global pos
    probel()

    if pos < len(text) and text[pos] == '-':
        pos += 1
        return -read_num()
    if pos < len(text) and text[pos] == '+':
        pos+=1
        return read_num()

    if pos < len(text) and text[pos] == '(':
        pos+=1
        res = calc()
        probel()
        if pos >= len(text) or text[pos] != ')':
            print("Не хватает закрывающей скобки")
            sys.exit()
        pos += 1
        return res
    if text[pos:pos+4] == "fact":
        pos+=4
        probel()
        if pos >= len(text) or text[pos] != '(':
            print("После факториала нужна скобка")
            sys.exit()
        pos += 1
        number = calc()
        probel()
        if pos >= len(text) or text[pos] != ')':
            print("Не хватает закрывающей скобки")
            sys.exit()
        pos += 1
        return factor(number)
    start = pos
    dot = False
    while pos < len(text) and (text[pos].isdigit() or text[pos] == '.'):
        if text[pos] == '.':
            if dot:
                break
            dot = True
        pos += 1
    if start == pos:
        print("Должно быть число")
        sys.exit()
    return float(text[start:pos])
def factor(x):
    if x < 0 or x != int(x):
        print("Факториал определен только для целых неотрицательных чисел")
        sys.exit()
    
    if x > 20:
        print("Слишком большое число")
        print("Введите число (0, 20]")
        
        
        sys.exit()
    
    res = 1
    for i in range(1, int(x) + 1):
        res = res * i
    return res

def umn():
    global pos
    res = read_num()

    while pos < len(text):
        probel()
        if text[pos] == '*':
            pos += 1
            res = res * read_num()
        else:
            break
    return res
    
def deli():
    global pos
    res = umn()

    while pos < len(text):
        probel()
        if text[pos] == '/':
            pos += 1
            d = umn()
            if d == 0:
                print("На 0 делить нельзя")
                sys.exit()
            res = res / d
        else:
            break
    return res
def calc():
    global pos
    res = deli()

    while pos < len(text):
        probel()
        if pos >= len(text):
            break
        znak = text[pos]
        if znak == '+':
            pos+=1
            res = res + deli()
        elif znak == '-':
            pos += 1
            res = res - deli()
        elif znak == '<':
            pos += 1
            m = deli()
            if res < m:
                res = 1
            else: res = 0
        else: break
    return res

text = input("Введите пример: ")
pos = 0

ans = calc()
probel()
if pos < len(text):
    print("Введены лишние знаки")
else:
    ans = round(ans, 10)
    if ans == int(ans):
        ans = int(ans)
    print("Ответ:", ans)



        
        
    



