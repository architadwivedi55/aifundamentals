class student:

  def __init__(self, name, age):
        self.name = name
        self.age = age

  def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

  def greetings(self):
            return f"Hello, my name is {self.name} and I am {self.age} years old."

student1 = student("Archita",20)
student2 = student("Ananya",21)

object_list =[]
object_list.append(student1)
object_list.append(student2)

for i in object_list:
    

#student1.display() 
#greet = object._ist.greetings()
#print(student1.name , student1.age)

 print(i.display())
 