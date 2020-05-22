# PYTHON script
'''
example for list append and pop functionality ...
'''


import os
import time

start_time = time.time()

i = 0
y = 10
my_list = []

for i in range(10):
	
	i = i + 1
    print(i)
	my_list.append(i)
	if (len(my_list) > 5):
		my_list.pop(0)

end_time = time.time()

print(my_list)

time_req = end_time - start_time

print("final_value =" , i)

print(time_req)

		
