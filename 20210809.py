num = input("请输入数字：")
var = 1
while var == 1 :
    pattern = input("有A,B两种pattern,请输入pattern:")
    pattern_A = num
    num = int(num)
    if pattern != "A" and  pattern !="B" :
        print("输入错误，请重新输入")
        continue
    else:
        if pattern == "A" :
            print(num)
        else:
            print(1)
