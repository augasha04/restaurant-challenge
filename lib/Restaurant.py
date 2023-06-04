class Restaurant:
    def __init__(self, name):
        self._name = name
        self._reviews= []

    def name(self):
        return self._name
    
    #the relationship
    def add_review(self, review):
        self._reviews.append(review)

    def reviews(self):
        return self._reviews
    
    def customers(self):
        uniqueCustomer = set()
        for review in self._reviews:
            uniqueCustomer.add(review.customer().name())
        return list(uniqueCustomer)
    
        