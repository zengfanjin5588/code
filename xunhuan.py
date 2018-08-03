# a = ["1","2","3","hello"]
#
# for i in range(3, 7):
#     print(i)


i = 0
# while i < 10:
# #     print(i)
# #
# #     if i ==3:
# #         continue
# #         break
# #
# #     i += 1

for i in range(3, 7):
    for j in range(5, 6):
        print("%d * %d = %d" % (i, j, i * j))