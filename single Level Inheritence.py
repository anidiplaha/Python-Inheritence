class Parent:
    parentname = ""
    childname = ""
 def show_parent(self):
 print(self.parentname)
 class Child(Parent):
    def show_child(self):
        print(self.childname)
 
 
ch1 = Child()  # Object of Child class
ch1.parentname = "Mark"   # Access Parent class attributes
ch1.childname = "John"
ch1.show_parent()   # Access Parent class method
ch1.show_child()    # Access Child class method