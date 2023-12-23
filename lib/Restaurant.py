class Restaurant:
    def __init__(self, name:str):
        self._name=name
        self._reviews=[]
        self._customers=[]

    @property
    def restaurant_name(self):
        return self._name
    
    def reviews(self):
        return self._reviews
    
    def customers(self):
        return self._customers
    
    def average_star_rating(self):
        if not self.reviews:
            return 0  

        total_rating = sum(review.rating for review in self._reviews)
        average_rating = total_rating / len(self._reviews)
        return average_rating