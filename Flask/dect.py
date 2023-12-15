def decorator(func1):

    def nowexec():

        print("Executing now..")

        func1()

        print("Executed..")

    return nowexec

@decorator
def run_task():

    print("This is inside the function")

run_task()
