class bookstore:

    noofbooks = 0
    
    def __init__(self,name,author):
        self.name = ""
        self.author = ""
        bookstore.noofbooks+=1
        
    def display(self):
        print(self.name,self.author,self.noofbooks)
            
def accept():
    
    obj1 = bookstore("Linux Book","Robert Love")
    obj1.display()
    
    obj2 = bookstore("C programming","Dennis Retchie")
    obj2.display()

if __name__ == "__main__":
    accept()

