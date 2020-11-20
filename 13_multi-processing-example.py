"""
################ -------------------- MULTI PROCESSING SMALL DEMO ----------------------- ##################

In the example below, we try to print contents of global list result at two places:

In square_list function. Since, this function is called by process p1, result list is changed in memory space of process p1 only.
After the completion of process p1 in main program, Since main program is run by a different process, its memory space still contains the empty result list.

"""


import multiprocessing
import time

'''
# empty list with global scope 
result = [] 
  
def square_list(mylist): 
    """ 
    function to square a given list 
    """
    global result 
    # append squares of mylist to global list result 
    for num in mylist: 
        result.append(num * num) 
    # print global list result 
    print("Result(in process p1): {}".format(result)) 
  
if __name__ == "__main__": 
    # input list
    mylist = [1,2,3,4] 
  
    # creating new process 
    p1 = multiprocessing.Process(target=square_list, args=(mylist,)) 
    # starting process 
    p1.start() 
    # wait until process is finished 
    p1.join() 
  
    # print global result list 
    print("Result(in main program): {}".format(result))

'''
# Test to iterate through 100 million range with and without multi-processing

multiprocessing_allowed = True

def calculate_a(a):
    for i in range(200000000):
        a += 1
    print(a)

def calculate_b(b):
    for i in range(200000000):
        b += 1    
    print(b)

if __name__ == '__main__':

    if (multiprocessing_allowed):
        # creating processes
        p1 = multiprocessing.Process(target=calculate_a, args=(10, ))
        p2 = multiprocessing.Process(target=calculate_b, args=(10, ))
        
        start_time = time.time()
        
        # start process execution
        p1.start()
        p2.start()
        
        # wait for process executions to end
        p1.join()
        p2.join()
        
        end_time = time.time()
        print("With Multiprocessing, time required = {} seconds ...".format(end_time - start_time))
    else:
        start_time = time.time()
        calculate_a(10)
        calculate_b(10)
        end_time = time.time()
        print("Without Multiprocessing, time required = {} seconds ...".format(end_time - start_time))