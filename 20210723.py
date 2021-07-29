# 简单购物车程序
#
# 购物车信息屏显示内容：
# ----------- Welcome to BUY_CENTLE ------------
#          salary：5000
#          1.iPhone 11    6000
#          2.mac book     9000
#          3.coffee       30
#          4.python book  80
#          5.bicycle      1500
# -----------------------------------------------
#
# 要求显示：（以下是显示例）
#
# >> >:1
#      返回    余额不足，-1000
# >> >:5
#      已加入购物车，当前余额3500
#      >>>:3
#      退出的同时返回：
#         您已购买以下商品
#         bicycle
#         1500
#         coffee
#         30
#
#         您的余额为: 3470
#         欢迎下次光临！！！
goods_list = [["iPhone 11:",6000],
              ["mac book: ",9000],
              ["coffee:     ",30],
              ["python book:",80],
              ["bicycle:  ",1500]]
var = 1
while var == 1:
    salary = input("请输持有金额：")
    balance = salary
# while True:
    if salary.isalpha():
        print("金额输入错误，请重新输入")
        continue
    else:
        salary = int(salary)
        shopping_cart = []
        while True:
            print("----------- Welcome to BUY_CENTLE ------------")
            print("余额：",salary)
            for i in range(len(goods_list)):
                print(i+1,goods_list[i])
            print("----------------------------------------------")
            choice_number = input("请输入商品编号或输入q退出：")
            if choice_number.isdigit() :
                choice_number = int(choice_number)
                if choice_number <= len(goods_list) :
                    choice_good = goods_list[choice_number-1]
                    # balance -=choice_good[1]
                    if choice_good[1] <= salary :
                        balance = int(balance)
                        balance = balance - choice_good[1]
                        print("已加入购物车，当前余额：",balance)
                        shopping_cart.append(choice_good)
                    else :
                        print("余额不足，请重新输入")
                else :
                    print("无此编号商品，请重新输入")
            elif choice_number == "q":
                if len(shopping_cart) >= 1 :
                    print("您已购买以下商品：")
                    for i in range(len(shopping_cart)):
                        print(i+1,shopping_cart[i])
                    print("您的余额为：",salary-choice_good[1])
                    print("欢迎下次光临！！")
                break
            else:
                print("输入错误，请重新输入")







