from random import choice
from user import User
from region import Region
from estate import Apartment, House, Store
from advertisment import ApartmentSell, ApartmentRent, HouseSell, HouseRent


FIRST_NAME = ['amir', 'mohammad', 'fati', 'negar']
LAST_NAEM = ['jahantab', 'gholami', 'bahadori', 'shabani']
PHONE_NUMBER = ['+98-903-727-6263', '+98-917-604-4188', '+98-935-259-3940',
                '+98-917-508-0680', '+98-921-592-0544']


def create_sample():

    for mobile in PHONE_NUMBER:
        User(choice(FIRST_NAME), choice(LAST_NAEM), mobile)

    # for user in User.object_list:
    #     print(f"\n{user.id}\t{user.fullname}\n")

    reg1 = Region(name='R1')
    reg2 = Region(name='R2')
    apt1 = Apartment(
    user=User.object_list[0], area=80, rooms_count=2, built_year=1395,
    has_elevator=True, has_parking=True, floor=2, region=reg1, address="Some text..."
    )
    


    house = House(
        has_yard=True, floors_count=1, user=User.object_list[1], area=400, rooms_count=6,
        built_year=1370, region=reg1, address="some text ..."
    )



    store = Store(
        user=User.object_list[-1], area=30, rooms_count=0, built_year=1390, region=reg1,
        address="some texr .."
    )


    Apartment_Sell = ApartmentSell(
        user=User.object_list[0], area=80, rooms_count=2, built_year=1395,
        has_elevator=True, has_parking=True, floor=2, region=reg1, address="Some text...",
        price_per_meter=5, discountable=True, convertable=False
    )


    apartment__rent = ApartmentRent(
        user=User.object_list[0], area=80, rooms_count=2, built_year=1395,
        has_elevator=True, has_parking=True, floor=2, region=reg1, address="Some text...",
        initial_price=100, monthly_price=3.5
    )

    house_sell = HouseSell(
        has_yard=True, floors_count=1, user=User.object_list[1], area=400,
        rooms_count=6, built_year=1370, region=reg1, address="some text ...",
        price_per_meter=20, discountable=False, convertable=False
    )

    house_rent = HouseRent(
        has_yard=True, floors_count=1, user=User.object_list[1], area=400, rooms_count=6,
        built_year=1370, region=reg1, address="some text ...", initial_price=130, monthly_price=7.5
    )
     
    print("#" * 20, "\t samples created \t", "#" * 20)