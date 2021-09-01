
# Costly enque operation
# Enqueing from the left and dequing from the right
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enQueue(self, x): # TC: O(n)

        # Emptying list one into list 2 from the end of list 2 
        # List 1 : 1 , 2 , 3
        # After Changign to list 2
        # List 2 : 3 , 2 , 1
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1]) # Taking last element in the list with [-1]
            self.s2.pop()
        
        self.s1.append(x) # Adding new data value to the top of the list

        # List 1 : 5
        # List 2 : 3, 2 , 1
        # New List 1: 5 , 1 , 2 , 3
        while len(self.s2) != 0: # Loading all elements back into origonal list after new value insertion
            self.s1.append(self.s2[-1])
            self.s2.pop()
        
    def deQueue(self): # TC: O(1)

        if len(self.s1) == 0:
            print("Empty Q")

        # Return top of self.1
        x = self.s1[-1]
        self.s1.pop()
        return x

# Costly deque operation
# Enquing from the left and dequing from the right
class Queue2:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enQueue(self, x): # TC: O(1)
        self.s1.append(x)
        
    def deQueue(self): # TC: O(n)

        if len(self.s1) == 0 and len(self.s2) == 0:
            print("Q is Empty")
            return

        # List 1 = 1 ,2 , 3
        # List 2 = []
        # After
        # List 1 = []
        # List 2 = 3 , 2 , 1
        # Remove top element from list 2 and return
        # List 1 = []
        # List 2 = 3, 2
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1): # Push everything from stack 1 to stack to and now the list has the top element at the end, pop return 
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
 
        else:
            return self.s2.pop()
 
