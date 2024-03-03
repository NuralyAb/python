#1
l = [1, 2, 3, 5]
print(eval('*'.join(map(str, l))))
#2
lst = input()
lower = list(filter(lambda x: x.isupper(), lst))
upper = list(filter(lambda x: x.islower(), lst))
print(f'{len(lower)} - lowercase letters\n{len(upper)} - uppercase letters')
#3
def determine(test_num, test):
    rev_test = ''.join(list(reversed(test)))
    print('Test #{} is {} palindrom'.format(test_num, 'a' if rev_test == test else 'not a'))
a = input()
determine(1, a)
#4
import time, math 
def test(a, t):
    time.sleep(t/1000)
    print(f'Square root of {a} after {t} miliseconds is {math.sqrt(a)}')
a, t = float(input('Input:\n')), float(input())
test(a, t)
#5
def determine(num, t):
    print(f'tuple #{num} is {all(t)}')
t1 = (True, True, True, True)
t2 = (True, True, False, True)
determine(1, t1)
determine(2, t2)
