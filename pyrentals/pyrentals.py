
class Cart:
    Rentals = []
    PriceList = {"Hour": 5, "Day": 20, "Month": 60}

    def empty(self):
        return 0 == len(self.Rentals)

    def calculate_price(self, price_list = [], unit_prices = [], enable_discount = True):
        total_price = 0
        if 0 == len(price_list):
            price_list = self.PriceList

        unit_prices.extend([price_list[self.Rentals[iRental]["Type"]] * self.Rentals[iRental]["Time"] for iRental in range(len(self.Rentals))])
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
