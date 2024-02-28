#1

import re 
s=str(input())
p=re.compile(r'ab*')
k=p.match(s)
print(k.group())

#2

import re 
s=str(input())
p=re.compile(r'ab{2,3}')
k=p.match(s)
print(k.group())

#3
import re
s=str(input())
p=re.compile(r'([a-z]+_[a-z]+)')
m=p.match(s)
print(m.group())

#4
import re
a=str(input())
p=re.compile(r'[A-Z][a-z]+')
k=p.match(a)
print(k.group())

#5
import re
a=str(input())
p=re.compile(r'a[.]*b')
k=p.match(a)
print(k.group())

#6
import re

def replace_with_colon(text):
    return re.sub(r'[ ,.]', ':', text)
a=str(input())
output_text = replace_with_colon(a)
print(output_text)

#7
import re

def snake_to_camel(snake_case):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_case)

a=str(input())
camel_case_string = snake_to_camel(a)
print(camel_case_string)

#8
import re

def split_at_uppercase(text):
    return re.findall(r'[A-Z][^A-Z]*', text)

a=str(input())
result = split_at_uppercase(a)
print(result)

#9
import re

def insert_spaces(text):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

a=str(input())
output_string = insert_spaces(a)
print(output_string)

#10
import re

def camel_to_snake(camel_case):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()

a=str(input())
snake_case_string = camel_to_snake(a)
print(snake_case_string)





