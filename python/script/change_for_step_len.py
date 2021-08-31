# 尝试改变步长
# 不可以改变
step_len = 3
for i in range(0, 50, step_len):
    print(i)
    step_len = 5
print("step_len = %d" % step_len)
