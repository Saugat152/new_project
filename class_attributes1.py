class Point:
    ''' Point class represents and manipulates x,y coords.'''

    def __init__(self): # every class have a special function 
        ''' Create a new point at the origin '''
        self.x = 0
        self.y = 0
#p and q are objects
#no need to pass self
p=Point()   #Instantiate an object of type Point
q=Point()   #Make a second point

print("Before Editing")

print(p.x, p.y) #each point onject has its own x and y
print(q.x, q.y) # each point object has its own x and y

print("After editing")
p.x=1
p.y=2

print(p.x,p.y)