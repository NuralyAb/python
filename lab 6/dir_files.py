#1
import os
path = 'C:\Users\user\Desktop\PP2 ANN\lab 3'
dirs = os.listdir(path)
print(f'folders and files in path - "{path}":\n', dirs)

#2
import os 
path = 'C:\Users\user\Desktop\PP2 ANN\lab 3'
print('Exists:', os.access(path, os.F_OK))
print('Access to read:', os.access(path, os.R_OK))
print('Access to write:', os.access(path, os.W_OK))
print('Can be executed:', os.access(path, os.X_OK))

#3
import os
path =r'C:\Users\user\Desktop\PP2 ANN\lab 3'
if os.path.exists(path):
    print('Path exists')
    print('Filename:', os.path.basename(path))
    print('Directory:', os.path.dirname(path))
else:
    print('This path doesn\'t exist')

#4
import os
path = r'C:\Users\user\Desktop\PP2 ANN\lab 3'

with open(path, 'r') as f:
    lines = f.readlines()
    print('Number of lines in {}: {}'.format(os.path.basename(path), len(lines)))

#5
with open('ex5.txt', 'w') as f:
    lst = [1, 'is', 'mine', [1, 1, 1], (1, 7), {1:5}, {1, 4, 5}]
    f.write(' '.join(map(str, lst)))
    
    f.write('\n')
    f.writelines(map(str, lst))
    
#6
import os
path =r'C:\Users\user\Desktop\PP2 ANN\lab 3'
if not os.path.exists(path):
    os.makedirs(path)

A = ord('A')
base = 'ex6.A-Z files\\{}.txt'
for i in range(A, A+26):
    f = open(base.format(chr(i)), 'w')

#7
with open('ex4.txt', 'r') as f1:
    with open('ex7.txt', 'w') as f2:
        f2.write(f1.read())
        
#8
import os 

path = r'C:\Users\user\Desktop\PP2 ANN\lab 3'
name = os.path.basename(path)

if os.path.exists(path):
    print(f'File "{name}" exists')
    if os.access(path, os.X_OK):
        print(f'File "{name}" can be eliminated')
        os.remove(path)
        print(f'"{name}" is deleted')
    else:
        print(f'File "{name}" can\'t be eliminated')
else:
    print(f'File "{name}" does\'t exist')

