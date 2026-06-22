import multiprocessing
import time

def square_num():
    for i in range(5):
        time.sleep(1)
        print(f"the square of number {i} is: {i*i}\n")
def cube():
    for i in range(6):
        time.sleep(1.2)
        print(f"the cube of number {i} is: {i*i*i}\n")
if __name__=="__main__":
    p1=multiprocessing.Process(target=square_num)
    p2=multiprocessing.Process(target=cube)
    t1=time.time()

    ##start

    p1.start()
    p2.start()


    p1.join()
    p2.join()
    finished_time= time.time()-t1


    print(finished_time)