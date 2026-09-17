class A:
    count = 0 
    def __init__(self):
        A.count += 1
        print("class A is called")


a1 = A()
print(A.count)
