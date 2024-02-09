#1
def to_ounces(g):
    return 28.3495231 * g

#2
def to_centigrate(F):
    return (5 / 9) * (F - 32)
print(to_centigrate(45))

#3
def solve(numheads, numlegs):
    y=(4*numheads-numlegs)/2
    x=numheads-y
    print(x,y)
solve(35,94)

#4
def filter_prime(array):
    for i in array:
        k=0
        for j in range(1,i+1):
           if(i%j==0):
              k=k+1
        if(k==2):
            print(i)
array=[1,4,7,8,5]
filter_prime(array)

#5
from itertools import permutations 
s=str(input())
perm=permutations(s)
for i in perm:
    print(*i)

#6
string = 'Tobol is champion'
def Convert(string):
  li = list(string.split(" "))
  print(*li[::-1])
Convert(string)

#7
def has_33(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 3 and nums[i+1] == 3:
       return True
  return False

#8
def spy_game(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 0:
      count += 1
    if count == 2 and nums[i] == 7:
      return True
    elif count != 2 and nums[i] == 7:
      return False
  return False
print(spy_game([1,2,4,0,0,7,5])) 

#9
def Volume(rad):
  print(4/3 * 3.14 * rad**3)
Volume(3)

#10
def uniqe(smth):
  for i in range(len(smth)):
    for j in range(i + 1, len(smth)):
      if smth[j] == smth[i]:
        smth[j] = -1
  arr = []
  for i in smth:
    if i != -1:
      arr.append(i)
  return arr
smth = [1, 1, 1, 1, 3, 3, 4, 5, 6, 7, 7, 8]
print(*uniqe(smth))

#ex11
def ispalindrome(word):
  copy = word[::-1]
  if copy == word:
    return True
  return False
print(ispalindrome("karakara")) 
print(ispalindrome("zrz"))


#ex12
def histogram(arr):
  for i in arr:
    strin = '*'
    print(strin * i)
histogram([3, 4, 2])


#ex13
import random
def guess():
  number = random.randint(1, 21)
  name = input("Hello! What is your name?\n")
  print("Well, "+ name + ", I am thinking of a number between 1 and 20.\n")
  count = 0
  for i in range(20):
    count += 1
    x = int(input("Take a guess.\n"))
    if x < number:
      print("Your guess is too low.\n")
    elif x > number:
      print("Your guess is too high.")
    elif x == number:
      print("Good job, " + name +", You guessed my number in "+ str(count)+ " guesses!")
      break
guess()


    





    
