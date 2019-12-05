import os

fdir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(fdir, 'day2_input.txt')
with open(filename, 'r') as f:
    input = list(map(int, f.read().split(',')))

i = 0
while i < len(input):
    if input[i] == 99:
        break
    if input[i] == 1:
        input[input[i+3]] = input[input[i+1]] + input[input[i+2]]
    if input[i] == 2:
        input[input[i+3]] = input[input[i+1]] * input[input[i+2]]
    i += 4
print(input)

