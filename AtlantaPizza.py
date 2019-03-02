#coding:utf-8
#AtlantaPizza.py 卖披萨的程序，也可以卖Q币，金币
#1.询问客户要买多少个披萨
pizza_count=eval(input("客官，要多少个Q币?"))
#2.询问每个披萨的菜单价格
pizza_price=eval(input("披萨多少钱一个?"))
#3.计算每个披萨的总价作为小计项
pizza_money = pizza_count*pizza_price
#4.计算需要支付的销售税，税率按8%
pizza_tax=pizza_money*0.08
#5.将销售税和小计项相加，作为最终的总价
total=pizza_money+pizza_tax
#6.向用户显示应该支付的总价，包含销售税
print("客官，总钱数是",total,"元")
print("其中披萨钱是",pizza_money,"元")
print("销售税是",pizza_tax,"元")
#7思考，如果税率不同，甚至每天变一次，那怎么修改程序呢。
#8思考，是不是可以写一个超市收银程序，我们不用加税，考虑打98折促销。考虑两种以上商品
