def add(*args):
    total = 0
    for value, index in args:
        total = total+value
        return total
    
    t = add(1,2,3)
    print(t)
    
    print(add(67,5,55,69,32))
    
    def studentDetails(**kwargs):
        for key, value in kwargs.items():
            print(key, " : ", value)
            
            
    studentDetails(name="piyush", age=25, dept="css")
