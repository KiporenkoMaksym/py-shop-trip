import math
from app.car import Car
from app.shop import Shop

def distance(loc1: list, loc2: list) -> float:
    return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: float,
                 car: Car) -> None:
        self.name = name
        self.location = location
        self.money = money
        self.product_cart = product_cart
        self.car = car

    def calculate_trip_cost(self, shop: Shop, fuel_price:float) -> float:

        dist_to_shop = distance(self.location, shop.location)
        dist_round_trip = dist_to_shop * 2
        fuel_cost = self.car.calculate_fuel_cost(dist_round_trip, fuel_price)
        product_cost = shop.calculate_product_cost(self.product_cart)
        return fuel_cost + product_cost

    def go_to(self, location: list) -> None:
        self.location = location
