class Review:
    
    all_reviews = []
    
    def __init__(self, customer,restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        
    def rating(self):
        return self._rating
    
    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant
    
    @classmethod
    def all(reviews):
        return reviews.all_reviews