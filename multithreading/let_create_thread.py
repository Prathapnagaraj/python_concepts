import time
import thread


def print_thread(name, delay):
    count=0
    while count<5:
        print "\n %s %s"%(name,time.ctime(time.time()))
	count=count+1
	time.sleep(delay)

def main():
    try:
	thread.start_new_thread(print_thread,("new_thread_1",3,))
	thread.start_new_thread(print_thread,("thread_2",3,))

    except:
	print "Unable to start thread"

    while(1):
    	pass



main()
	


