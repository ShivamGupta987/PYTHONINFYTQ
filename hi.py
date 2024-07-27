arr = [1,2,3]

for i in arr:
  
    if i == arr[-1]:
        arr.pop()
        i = i +1
        print(i)