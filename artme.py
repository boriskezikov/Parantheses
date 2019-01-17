
import time

start_time = time.clock()


#var = "(?)(?)????(???)???(?)???()??()??()??????????????????"
var = "((?))?"
string = list(var)
print("Символов: ", len(string))


left = 0
right = 0
quest = 0
sol = 0


def canonTYPE(string, left, right, quest, sol):
    if len(string) % 2 == 0:
        for i in range(len(string)):
            if string[i] == '(':
                left += 1
            elif string[i] == ')':
                right += 1
                if left + quest < right:
                    sol = 0
                    print("Закрывающих больше чем допустимо")
                    return
                elif left + quest == right:
                    for j in range(len(string[:i])):
                        if string[j] == '?':
                            quest -= 1
                            left += 1
                            string[j] = '('
                            sol = 1
            elif string[i] == '?':
                quest += 1

        for i in range(len(string)-1, -1, -1):
            if string[i] == '(':
                if right + quest < left:
                    sol = 0
                    print("Открывающих больше чем допустимо")
                    return
                elif right + quest == left:
                    for j in range(len(string[i:])-1, -1, -1):  #?? [:i] or [i:]
                        if string[j] == '?':
                            quest -= 1
                            right += 1
                            string[j] = ')'
                            sol = 1

    else:
        sol = 0
        print("НЕЧЕТНО")

    print("Вопросов: ", quest)
    print("Левых: ", left)
    print("Правых: ", right)
    print("Решений: ", sol)

    return string

canonTYPE(string, left, right, quest, sol)

print(string)

print (time.clock() - start_time, "seconds")