import re
import argparse

# Task_1
s = 'lorem ipsum dolor sit amet'
c1 = re.compile(r'\b[eyuioa]\w*', re.IGNORECASE)
c2 = re.compile(r'\b[^ eyuioa\W]\w*', re.IGNORECASE)
print(c1.findall(s))
print(c2.findall(s))

# Task_2 (у меня в консоли для google.com выдало такое)
p = '''number of bytes=32 time=33 mc TTL=53
    number of bytes=32 time=36 mc TTL=53
    number of bytes=32 time=33 mc TTL=53
    number of bytes=32 time=35 mc TTL=53'''
compiled1 = re.compile(r'n.+\b32')
compiled2 = re.compile(r'\bt.+\bmc')
compiled3 = re.compile(r'\bT.+\b\d+')
print(compiled1.findall(p))
print(compiled2.findall(p))
print(compiled3.findall(p))

# Task_3
text = str(input('Input text:'))

parser = argparse.ArgumentParser()
parser.add_argument('-name', required=True, type=str, help='Name of file')
name = parser.parse_args()

c3 = re.compile(r'%quit')

if c3.findall(text) == ['%quit']:
    file = open(name.txt, 'w')
    file.write(re.sub('%quit', '', text))
    file.close()
