#!/usr/bin/env python3
import ipdb;

from lib.Customer import Customer
from lib.Restaurant import Restaurant
from lib.Review import Review

if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###

    #Creating the customers
    print("\nCreating the customers")
    Samuel=Customer("Samuel","Muigai")
    Kennedy=Customer("Kennedy","Macharia")
    print(Samuel.__dict__)
    print(Kennedy.__dict__)

    #Changing the given and family names
    print("\nChanging the given and family names")
    Samuel.given_name="Brian"
    Samuel.family_name="Karanja"
    print(Samuel.__dict__)

    Kennedy.given_name="Moses"
    Kennedy.family_name="Kamau"
    print(Kennedy.__dict__)

    #Printing the customer full name
    print("\nPrinting the customer full name")
    print(Samuel.full_name)
    print(Kennedy.full_name)

    #Returning all customer instances
    print("\nPrinting out all instances of the class")
    for customer in Customer.all():
        print(customer.full_name)

    #Creating the Restaurant
    print("\nCreating a restaurant instance")
    Moonlight=Restaurant("Moonlight Cafe")
    print(Moonlight.__dict__)

    #Returning the restaurant name
    print("\nReturning the restaurant name")
    print(Moonlight.restaurant_name)

    #Attempting to change the restaurant name
        #Returns and AttributeError since there is no setter for the restaurant name
    # Moonlight.restaurant_name="New Name"
    # print(Moonlight.restaurant_name)

    #Creating a review
    print("\nCreating a review instance")
    first_review=Review(Samuel,Moonlight,"9")
    print(first_review.__dict__)

    #Printing the review rating
    print("\nPrinting the review rating")
    print(first_review.review_rating())

    #Printing all instances of the review class
    print("\nPrinting all instances of the review class")
    for review in Review.review_all():
        print(review)

    #Returning the customer object for a particular review
    print("\nReturning the customer object for a particular review")
    print(first_review.review_customer())

    #Returning the restaurant object for that given review
    print("\nReturning the resturant object for a particular review")
    print(first_review.review_restaurant())

    #Returning a list of all reviews for a particular restaurant
    print("\nReturning a list of all reviews for a particular restaurant")
    print(Moonlight.reviews())
    
    #Returning a unique list of all customers who have reviewed a particular restaurant
    print("\nReturning a unique list of all customers who have reviewed a particular restaurant")
    print(Moonlight.customers())

    #Returning a unique list of all customers who have reviewed a particular restaurant
    print("\nReturning a unique list of all restaurants a customer has reviewed")
    print(Samuel.restaurants())

    #Creating a new review and associating it with that customer and restaurant
    print("\nCreating a new review and associating it with that customer and restaurant")
    Samuel.add_review(Moonlight, 10)
    print(Samuel.restaurants())

    #Returning the number of reviews a customer has created
    print("\nReturning the number of reviews a customer has created")
    print(Samuel.num_reviews())

    #Returning the first customerwhose full name matches the given names
    print("\nReturning the first customerwhose full name matches the given names")
    print(Customer.find_by_name("Brian Karanja"))

    #Returning a list of customers with the given name
    print("\nReturning a list of customers with the given name")
    print(Customer.find_all_by_given_name("Brian"))
    print(Customer.find_all_by_given_name("Moses"))

    #Returning the average star rating for a restaurant based on its reviews
    print("\nReturning the average star rating for a restaurant based on its reviews")
    print(Moonlight.average_star_rating())

# DO NOT REMOVE THIS
    # ipdb.set_trace()
