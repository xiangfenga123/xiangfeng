num = [1,24,23,56,47]
for i in range(len(num)-1):
  for j in range(len(num)-i):
    if num[i]> num[j+i]
        temp = num[i]
        num[i] = num[j+i]
        num[j+i] = temp
print(num)