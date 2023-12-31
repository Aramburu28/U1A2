#Using the multiprocessing module, write a simple python program as follows:

#Create a pool of workers to run parallel tasks.
#The pool size should be 2.
#Write a function to be running in parallel, call it print_cube. The function should receive as input a number [num]. When called, the function will print to the screen a message in the form: “The cube of number [num] is [cube]”. Where [cube] should be replaced with the cube of the number received as input.
#Write a function to be running in parallel, call it print_square. The function should receive as input a number [num]. When called, the function will print to the screen a message in the form: “The square of number [num] is [square]”. Where [square] should be replaced with the square of the number received as input.
from multiprocessing import Pool
def print_cube(x):
    print("The cube of number " + str(x) + " is " + str(x*x*x))
    

def print_square(x):
    print("The square of number " + str(x) + " is " + str(x*x))
    

if __name__ == '__main__':
    p = Pool(2)
    nums = range(10)
    p.starmap(print_cube, [(num,) for num in nums])
    p.starmap(print_square, [(num,) for num in nums])
    
    

