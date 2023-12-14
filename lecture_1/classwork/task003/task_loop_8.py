# Решить в уме
# data = 0
# # while data < 100:
# #     data += 2
# #     if data % 40 == 0:
# #         break
# # print(data)

# data = 0
# while data < 100:
#     data += 3
#     if data % 40 == 0:
#         break
# else:
#     data += 5
# print(data)

data = 0
while data < 100:
    data += 3
    if data % 19 == 0:
        continue
    data += 1
    if data % 40 == 0:
        break
else:
    data += 5
print(data)
