li = 'AECD'
res = sorted(li)
print(res)
left = 0
right = 0
for i in range(len(res)):
    if res[i].isupper():
        right = i
        break
for j in range(right, len(res)):
    if res[j].islower():
        left = j
        break
result = res[left:len(res)] + res[right:left] +res[:right]
print(''.join(result))