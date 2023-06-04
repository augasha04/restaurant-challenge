#creating a class for the customer
class Customer:
    
    #passing the customer as a list
    customer_all  = []
    
    #initializing the customer
    def __init__(self, givenName, familyName):
        self.givenName = givenName
        self.familyName = familyName
        self.customer_all.append(self)
        
    #creating instances of the customer
    def givenName(self):
        return self.givenName

    def familyName(self):
        return self.familyName

    def fullName(self):
        return f"{self.givenName} {self.familyName}"
    
    #creating the customer table
    @classmethod
    def all(cls):
        return cls.customer_all
    
    
# Creating  some customers using their name and family name
customer1 = Customer(f"Augustine", "Kariuki")
customer2 = Customer(f"John", "Muthee")

# printing the given name and family name of a customer
print(customer1.givenName)  
print(customer1.familyName)

#printing all the customers 
customer_all = Customer.all()
for customer in customer_all:
    print(customer.fullName())



    
    
        
    
        
        