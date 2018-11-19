def hotel_cost (nights):
    nights=70*nights
    return nights


def plane_ticket_cost (city, type):

    NewYork=2000
    Auckland=790
    Venice=154
    Glasgow=65
    economy=1
    ecoprem=1.3
    business=1.6
    first=1.9
    if city=="New York":
        city=NewYork
    elif city=="Auckland":
        city=Auckland
    elif city=="Venice":
        city=Venice
    elif city=="Glasgow":
        city=Glasgow


    if type==1:
        type=economy
    elif type==2:
        type=ecoprem
    elif type==3:
        type-business
    elif type==4:
        type=first


    cost= city*type
    return cost


def rental_car_cost (days):
    carcost=days*30
    if days>7:
        carcost=carcost-50
    elif days>3 and days<=7:
        carcost=carcost-30
    return carcost

def total_cost (city, days):

    travel_class=float(input("In which class are you travelling? (1-4, 1 for economy) "))
    car_rental=int(input("For how many days do you rent the car? "))
    nightscost= float(hotel_cost(nights_needed))
    plane_cost=float(plane_ticket_cost(destination, travel_class))
    car_cost= float(rental_car_cost(car_rental))
    totalcost=float(nightscost+plane_cost+car_cost)
    print("Your price for the trip is ", str(totalcost))


nights_needed=float(input("How many nights? "))
destination=str(input("Which city are you travelling to? "))
total_cost(destination, nights_needed)
