num = int(input("Give no of num: "))
t_sum = 0
for i in range(num):
    v = int(input(f"Give v{i+1}: "))
    t_sum = t_sum + v

avg = t_sum/num
print("Average is:",avg)