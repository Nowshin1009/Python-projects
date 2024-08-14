class Student:
    #constructor:
    def __init__(self,name,rollno,m1,m2):
        self.name=name
        self.rollno=rollno
        self.m1=m1
        self.m2=m2
    def accept(self,Name,Rollno,marks1,marks2):
        ob = Student(Name,Rollno,marks1,marks2)
        ls.append(ob)

    def display(self,ob):
        print("Name: ",ob.name)
        print("Rollno: ",ob.rollno)
        print("Makrs1: ",ob.m1)
        print("Marks2: ",ob.m2)
        print("\n")

    def search(self,rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                print("\n Student Found")
                return i

    def delete(self,rn):
        i = obj.search(rn)
        del ls[i]


ls=[]
obj = Student('',0,0,0)
obj.accept("A",1,85,90)
obj.accept("B",2,55,70)
obj.accept("C",3,75,60)
print("\n")
print("List of the students\n")
for i in range (ls.__len__()):
    obj.display(ls[i])


s = obj.search(2)
obj.display(ls[s])

obj.delete(3)
print("\n")
print("List of the students after delete\n")
for i in range (ls.__len__()):
    obj.display(ls[i])