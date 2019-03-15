
class Cart:
    Rentals = []
    PriceList = {"Hour": 5, "Day": 20, "Month": 60}

    def __init__(self):
        self.Rentals = []
        self.PriceList = {"Hour": 5, "Day": 20, "Month": 60}

    def empty(self):
        return 0 == len(self.Rentals)

    def calculate_price(self, price_list = {}, unit_prices = [], enable_discount = True):
        total_price = 0
        if 0 == len(price_list):
            price_list = self.PriceList

        unit_prices.extend([(price_list[self.Rentals[iRental]["Type"]] * self.Rentals[iRental]["Time"]) for iRental in range(len(self.Rentals))])
        total_price = sum(unit_prices)
        rental_count = len(unit_prices)
        discount_qualified = rental_count in range(3, 6)
        discount_applied = enable_discount and discount_qualified
        if discount_applied:
            discount_value = total_price * .3
            price_with_discount = total_price - discount_value
            print("\n-- Family Package Discount --""\nRental Price: {:2.2f}\nDiscount: {:2.2f}\nFinal price: {:2.2f}\n".format(total_price, discount_value, price_with_discount))
            total_price = price_with_discount
        return total_price

    def add_rental(self, rental_type, rental_time):
        if not rental_type in self.PriceList.keys():
            raise KeyError("Invalid rental type: {}".format(rental_type))
        if rental_time <= 0:
            raise KeyError("Invalid rental time: {} {}{}".format(rental_time, rental_type, "s" if rental_time > 1 else ""))
        self.Rentals.append({"Type": rental_type, "Time": rental_time})

