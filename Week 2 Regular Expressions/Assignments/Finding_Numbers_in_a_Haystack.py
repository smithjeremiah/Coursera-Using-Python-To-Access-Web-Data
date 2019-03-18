#Finds the sum of all numbers in the text


import re
fname = (r"C:\Users\Jeremiah\Desktop\Python\regex_sum_157767.txt")# I copied and pasted this from my text editor
fh = open(fname)
ans = 0
count = 0
for line in fh:
    num = re.findall(r'[0-9]+',line)
    if len(num) > 0:
        num = list(map(int,num))
        ans = ans + sum(num)
        for i in num:
            count = count + 1


print(ans)
