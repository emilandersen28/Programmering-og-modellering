import matplotlib.pyplot as plt
import numpy as np

# split string in list of words with the seperator ')'

def split_string(string):
    return string.split(')')
data = ''
# input data from terminal
data = input('Enter data: ')
list_data = split_string(data)
# print(list_data)
# remove every thing before '(' 
for i in list_data:
    list_data[list_data.index(i)] = i[i.find('(')+1:]

for i in list_data:
    list_data[list_data.index(i)] = i.split(',')
#delete the last element of the list
list_data.pop()
print(list_data)

# plot the data
x = []
y = []
for i in list_data:
    x.append(float(i[0]))
    y.append(float(i[1]))

x = np.array(x)
y = np.array(y)

# plot x and y using matplotlib
plt.plot(x, y)
# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
plt.title('time and angle')
plt.show()
