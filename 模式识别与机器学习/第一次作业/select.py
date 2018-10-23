print("请输入需要分类的模式(2维),用“,”分割：")
x=input()
p=x.split(",")
f= lambda x: (-x*4+26)/4
ans=f(float(p[0]))
if ans>float(p[1]):
    print("the pattern is w1!!!")
elif ans<float(p[1]):
    print("the pattern is w2!!!")

