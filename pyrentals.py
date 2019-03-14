
class Cart:
    Rentals = []
    PriceList = {"Hour": 5, "Day": 20, "Month": 60}

    def empty(self):
        return 0 == len(self.Rentals)

    def calculate_price(self, price_list = [], unit_prices = [], enable_discount = True):
        total_price = 0
        if 0 == len(price_list):
            price_list = self.PriceList

        for iRental in range(len(self.Rentals)):
            rental = self.Rentals[iRental]
            type_text = rental["Type"]
            rental_price = price_list[rental["Type"]] * rental["Time"]
            unit_prices.append(rental_price)
            print("\n- Rental #%s: Type: %s, %ss: %s, Price: %s.", 1 + iRental, type_text, type_text, rental["Time"]
                  , rental_price)
            total_price += rental_price

        rental_count = len(unit_prices)
        discount_qualified = rental_count in range(3, 6)
        discount_applied = enable_discount and discount_qualified
        if discount_applied:
            discount_value = total_price * .3
            price_with_discount = total_price - discount_value
            print("\n-- Family Package Discount --""\nRental Price: " + total_price + "\nDiscount: " + discount_value
                  + " \nFinal price: " + price_with_discount + "\n")
            total_price = price_with_discount
        return total_price

