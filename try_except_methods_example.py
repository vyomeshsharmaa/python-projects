class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # basic version: no validation at all
    def apply_discount_unsafe(self, percent):
        return self.price - (self.price * percent / 100)

    # improved version: validates *inside* the method, right where the risky math happens
    def apply_discount_safe(self, percent):
        try:
            # this line is the actual risky action — math involving `percent`
            return self.price - (self.price * percent / 100)
        except TypeError:
            # this only fires if `percent` can't be used in math (e.g. it's a string)
            print("percent must be a number")
            return self.price  # fallback: no discount applied


item = Product("Notebook", 100)

print(item.apply_discount_safe(10))     # 90.0  -> works fine, 10 is a number
print(item.apply_discount_safe("ten"))  # "percent must be a number" -> caught safely
print(item.apply_discount_unsafe("ten"))  # this one crashes the program - no protection