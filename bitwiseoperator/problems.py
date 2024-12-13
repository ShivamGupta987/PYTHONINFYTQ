# count 1 inteher

def count_Set_bits(num):
    count=0
    while num>0:
        count+=num&1
        num >>= 1
        
    return count

print(count_Set_bits(21))

# given an int n find max power of two that is smalller than n

#  simple app
# if n<=1:
#     return 0 
# temp = 1
# while temp<n:
#     temp*=2
# return temp//2

def max_pow(n):
    if n<=1:
        return 0
    
    power = 0
    while (1<<power) < n:
        power+=1
        
    return 1<<(power-1)
print(max_pow(100))


# cal minimum bit flip to convert one to another

def count_set(num):
    count=0
    
    while num>0:
        count+=num&1
        num >>=  1
    return count

def find_differnet_bits(n1,n2):
    xor_res=n1^n2
    return count_set(xor_res)

print(find_differnet_bits(5,11))

# give an int ary where every element occurs twice one occurs only once. find that unique element

def unique(arr):
    unique = 0
    for num in arr:
        unique =num^unique
        
    return unique

print(unique([4,5,6,6,5]))

# gibe an int arr nums in which exactly two elements appear only once and alll othwe appear rwice . find elemen appear oncw


def find_unique(nums):
    xor_res = 0
    for num in nums:
        xor_res =num
        
    first_Set_bit = xor_res &(-xor_res)
    unique1=0
    unique2=0
    for num in nums:
        if num& first_Set_bit == 0:
            unique1^=num
        else:
            unique2^=num
        
    return unique1,unique2

print(find_unique([4,5,15,6,5,4]))


# print factorial of first 25 natural number nad modulo the result 10^9+7
#(A%B)%C = (A%C * B%C)%C

def modolo_fact():
    MOD= 10^9+7
    
    factorial = 1
    for i in range(1,26):
        factorial = (factorial*i)%MOD
        print(factorial,end=" ")
        
print(modolo_fact())