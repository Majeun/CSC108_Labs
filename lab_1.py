###Question 1
##print("")
##print("Rectangle")
##
##sidex = 5
##sidey = 2
##def rect_area(sidex, sidey):
##    x = sidex * sidey
##    return x
##
##length = input("enter the length: ")
##width = input("input the width: ")
##
##length = int(length)
##width = int(width)
##area = rect_area(width , length)
##
##print (area)
##
##
###Question 2
##print("")
##print("Square")
##
##length = input("input the side length of the square: ")
##length = int(length)
##
##area = rect_area(length, length)
##
##print (area)
##
##
###Question 3
##print("")
##
##x = 8
##y = x + 1
##x = (y + 2*x) // 6
##y = -(y+1)
##y = x/y
##
##x = str(x)
##y = str(y)
##
##print("X is:" + x)
##print("Y is:" + y)
##
###Question 4
##print("")
##
##a = input("a: ")
##b = input("b: ")
##c = input("c: ")
##x = input("x: ")
##a = float(a)
##b = float(b)
##c = float(c)
##x = float(x)
##
##def quadratic(a, b, c, x):
##    posorneg = ((b**2) - 4*(a*c))
##    if posorneg < 0:
##        posorneg = posorneg * -1
##    answer1 = ((b*-1) + (posorneg ** 0.5)) / (2*a)
##    answer2 = ((b*-1) - (posorneg ** 0.5)) / (2*a)
##
##    if answer1 and answer2 < 0:
##        pos_ans = ("no positive value")
##    elif answer1 > answer2:
##        pos_ans = answer1
##    elif answer1 < answer2:
##        pos_ans = answer2
##    else:
##        pos_ans = answer1
##
##    return pos_ans
##    
##q4 = quadratic(a, b, c, x)
##print(q4)
##
###Question 5

x = input("x: ")
x = int(x)

def absolute(x):
    x = abs(x)

    return x

op = absolute(x)

print (op)





