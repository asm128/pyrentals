from pyrentals import Cart
import unittest

class Test_test_pyrentals(unittest.TestCase):
    def test_method_empty(self):
        test_cart_instance = Cart()
        test_cart_instance.Rentals = {}
        return self.assertTrue(test_cart_instance.empty(), "Cart should be empty when it's just created.")

    def test_method_not_empty(self):
        test_cart_instance = Cart()
        test_rental = {"Type": "Hour", "Time": 2}
        test_cart_instance.Rentals = [test_rental, ]
        return self.assertFalse(test_cart_instance.empty(), "Cart shouldn't be empty if we just added test_rental.")

    def test_calculate_price_empty(self):
        test_cart_instance = Cart()
        return self.assertEqual(0, test_cart_instance.calculate_price())

    def test_price_list(self):
        test_cart_instance = Cart()
        price_list = {"Hour": 5, "Day": 15, "Month": 60}
        test_rental = {"Type": "Day", "Time": 2}
        test_cart_instance.Rentals = [test_rental] * 2
        output_prices = []
        final_price = test_cart_instance.calculate_price(price_list, output_prices)
        for price in output_prices:
            self.assertEqual(30, price)
        self.assertEqual(60, final_price)
        return

    def test_family_discount(self):
        test_cart_instance = Cart()
        price_list = {"Hour": 5, "Day": 15, "Month": 60}
        test_rental = {"Type": "Day", "Time": 2}
        test_cart_instance.Rentals = [test_rental] * 3
        output_prices = []
        final_price = test_cart_instance.calculate_price(price_list, output_prices)
        raw_price = sum([x["Time"] * price_list[x["Type"]] for x in test_cart_instance.Rentals])
        self.assertLess(final_price, raw_price)
        return self.assertTrue(final_price == raw_price - raw_price * .3)

    def test_family_discount_limit(self):
        test_cart_instance = Cart()
        price_list = {"Hour": 5, "Day": 15, "Month": 60}
        test_rental = {"Type": "Day", "Time": 2}
        test_cart_instance.Rentals = [test_rental] * 6
        output_prices = []
        final_price = test_cart_instance.calculate_price(price_list, output_prices)
        raw_price = sum([x["Time"] * price_list[x["Type"]] for x in test_cart_instance.Rentals])
        return self.assertEqual(final_price, raw_price)

    def test_output_prices(self):
        test_cart_instance = Cart()
        price_list = {"Hour": 5, "Day": 15, "Month": 60}
        test_rental = {"Type": "Day", "Time": 2}
        test_cart_instance.Rentals = [test_rental] * 3
        output_prices = []
        final_price = test_cart_instance.calculate_price(price_list, output_prices)
        raw_price = sum([x["Time"] * price_list[x["Type"]] for x in test_cart_instance.Rentals])
        return self.assertEqual(raw_price, sum(output_prices))

    def test_add_rental(self):
        test_cart_instance = Cart()
        price_list = {"Hour": 5, "Day": 15, "Month": 60}
        test_rental = {"Type": "Day", "Time": 2}
        for x in range(2):
            test_cart_instance.add_rental(test_rental["Type"], test_rental["Time"]) 
        output_prices = []
        final_price = test_cart_instance.calculate_price(price_list, output_prices)
        for price in output_prices:
            self.assertEqual(30, price)
        self.assertEqual(60, final_price)
        return

if __name__ == '__main__':
    unittest.main()
