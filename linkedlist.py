class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class NodeCreator:
    def __init__(self):
        self.head = None
    
    def create(self,x):
        if (self.head == None):
            self.head = Node(x)
        else:
            temp = self.head
            while (temp.next!= None):
                temp = temp.next
            temp.next = Node(x)

    def display(self):
        temp = self.head
        while(temp!=None):
            print(temp.data) 
            temp = temp.next

    def add_prime(self):
        sum = 0
        temp = self.head
        while(temp!=None):
            c = 0
            for i in range(2,int(temp.data/2)):
                if(temp.data%i == 0):
                    c = 1
                    break
            if c==0:
                sum = sum+temp.data
        return sum

    def reverse(self):
        temp = self.head
        while(temp!=None):
            rev = 0
            a = temp.data
            while(a!=0):
                b = a % 10
                rev = rev*10 + b
                a = a/10
            print(rev)



list1 = NodeCreator()
for i in range(3):
    list1.create(int(input()))

list1.display()
print(list1.add_prime())
list1.reverse()
