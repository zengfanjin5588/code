# 1 石头 2 剪刀 3 布

computer = 1
person = 3

if ((person == 1 and computer == 2)
        or (person ==2 and computer ==3)
        or (person == 3 and computer == 1)):
    print("person获胜")
elif computer == person:
    print("平局")
else:
    print("computer获胜")