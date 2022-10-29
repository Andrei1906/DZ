power = int(input()).bit_length()-1
num = 1
for i in range(power):
    num *= 2

print(power, num)