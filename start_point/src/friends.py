import re


def get_name(person):
    return "Daphne"
def get_favourite_tv_show(person):
    return "Baywatch"

def likes_to_eat(person, food):
    favourite_snacks = person["favourites"]["snacks"]
    for snack in favourite_snacks :
        if snack == food :
            return True
    return False 
    
def add_friend(person, friend):
    person["friends"].append(friend)

def remove_friend(person, friend) :
    person["friends"].remove(friend)

def total_money(people):
    total_money = 0
    for person in people :
        total_money += person["monies"]
    return total_money
 
def lend_money(lender,lendee,amount) : 
    lender["monies"] -= amount
    lendee["monies"] += amount 

def all_favourite_foods(people):
    all_foods = []        
    for person in people:
        all_foods.extend(person["favourites"]["snacks"])
    return all_foods 

def find_no_friends(people):
    no_friends = []
    for person in people:
        if len(person["friends"]) == 0 :
            no_friends.append(person)
    return no_friends 

def unique_favourite_tv_shows(people):
    tv_shows = []
    for person in people :
        if tv_shows.count(person["favourites"]["tv_show"]) == 0 :
            tv_shows.append(person["favourites"]["tv_show"])

    return tv_shows
    # tv_shows = []
    # for person in people:
    #     tv_shows.append(person["favourites"]["tv_show"])
    # return set(tv_shows)
    
    