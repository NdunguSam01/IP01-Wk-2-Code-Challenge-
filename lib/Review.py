class Review:

    _all_ratings=[]
    def __init__(self, customer, restaurant, rating:int):
        self._customer=customer
        self._restaurant=restaurant
        self.rating=rating
        Review._all_ratings.append(self)
        self._restaurant._reviews.append(self)
        self._restaurant._customers.append(self)
        self._customer._reviewed_restaurants.append(self)
        self._customer._reviews.append(self)

    def review_rating(self):
        return self.rating
    
    @classmethod
    def review_all(cls):
        return cls._all_ratings
    
    def review_customer(self):
        return self._customer
    
    def review_restaurant(self):
        return self._restaurant
