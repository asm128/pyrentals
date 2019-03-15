from pyrentals import Cart
import unittest

class Test_test_pyrentals(unittest.TestCase):
    test_cart_instance = Cart()

    def test_method_empty(self):
        self.test_cart_instance = Cart()
        self.test_cart_instance.Rentals = {}
        return self.assertTrue(self.test_cart_instance.empty(), "Cart should be empty when it's just created.")

    def test_method_not_empty(self):
        self.test_cart_instance = Cart()
        test_rental = {"Type": "Hour", "Time": 2}
        self.test_cart_instance.Rentals = [test_rental, ]
        return self.assertFalse(self.test_cart_instance.empty(), "Cart shouldn't be empty if we just added test_rental.")

    def test_calculate_price_empty(self):
        self.test_cart_instance = Cart()
        return self.assertEqual(0, self.test_cart_instance.calculate_price())

    def test_price_list(self):
        self.test_cart_instance = Cart()
        price_list = {"Hour": 5, "Day": 15, "Month": 60}
        test_rental = {"Type": "Day", "Time": 2}
        self.test_cart_instance.Rentals = [test_rental, test_rental, ]
        output_prices = []
        final_price = self.test_cart_instance.calculate_price(price_list, output_prices)
        for price in output_prices:
            self.assertEqual(30, price)
        self.assertEqual(60, final_price)
        return

    def test_family_discount(self):
        self.test_cart_instance = Cart()
        price_list = {"Hour": 5, "Day": 15, "Month": 60}
        test_rental = {"Type": "Day", "Time": 2}
        self.test_cart_instance.Rentals = [test_rental, test_rental, test_rental, ]
        output_prices = []
        final_price = self.test_cart_instance.calculate_price(price_list, output_prices)
        raw_price = sum([x["Time"] * price_list[x["Type"]] for x in self.test_cart_instance.Rentals])
        self.assertLess(final_price, raw_price)
        return self.assertTrue(final_price == raw_price - raw_price * .3)

    def test_output_prices(self):
        self.test_cart_instance = Cart()
        price_list = {"Hour": 5, "Day": 15, "Month": 60}
        test_rental = {"Type": "Day", "Time": 2}
        self.test_cart_instance.Rentals = [test_rental, test_rental, test_rental, ]
        output_prices = []
        final_price = self.test_cart_instance.calculate_price(price_list, output_prices)
        raw_price = sum([x["Time"] * price_list[x["Type"]] for x in self.test_cart_instance.Rentals])
        return self.assertEqual(raw_price, sum(output_prices))


if __name__ == '__main__':
    unittest.main()
