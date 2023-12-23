class Customer:

    _all=[]

    def __init__(self, given_name: str, family_name:str):
        self.given_name=given_name
        self.family_name=family_name
        Customer._all.append(self)
        self._reviewed_restaurants=[]
        self._reviews=[]

    @property
    def given_name(self):
        return self._given_name
    
    @given_name.setter
    def given_name(self, given_name):
        self._given_name=given_name

    @property
    def family_name(self):
        return self._family_name
    
    @family_name.setter
    def family_name(self, family_name):
        self._family_name=family_name

    @property
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    @classmethod
    def all(cls):
        return cls._all
    
    def restaurants(self):
        return self._reviewed_restaurants

    def add_review(self, restaurant, rating):
        self.resaturant=restaurant
        self.rating=rating
        self._reviewed_restaurants.append(self)
        self._reviews.append(self)

    def num_reviews(self):
        return len(self._reviews)
    
    @classmethod
    def find_by_name(cls, name):
        for customer in cls._all:
            if f"{customer.given_name} {customer.family_name}" == name:
                return customer
            
        return None
    
    @classmethod
    def find_all_by_given_name(cls, name):
        matching_names=[customer for customer in cls._all if customer.given_name == name]
        return matching_names