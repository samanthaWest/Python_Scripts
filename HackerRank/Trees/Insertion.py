class newNode():
 
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

def insert(temp, key):

    if not temp:
        root = newNode(key)

    q = []
    q.append(temp)

    while (len(q)):
        
        # Take no from the queue to search through
        temp = q[0]
        q.pop(0)

        