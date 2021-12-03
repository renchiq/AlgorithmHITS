with open('output.txt', 'r') as f:
    lst = f.read().split('\n')
for i in range(len(lst) - 1):
    lst[i] += '\n'
lst.sort()
with open('output.txt', 'w') as f:
    f.writelines(lst)