#creation of class

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

#Assessing object's properties
#Each object has its own x and y
print(p.x)
print(p.y)
print(q.x)
print(q.y)



