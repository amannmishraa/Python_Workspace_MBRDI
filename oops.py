from abc import ABC, abstractmethod


# -------------------- ABSTRACTION --------------------
# Abstract class hides implementation details
class IceCream(ABC):

    @abstractmethod
    def get_price(self):
        pass


# -------------------- INHERITANCE --------------------
# Vanilla inherits from IceCream
class VanillaIceCream(IceCream):

    def __init__(self):
        # -------------------- ENCAPSULATION --------------------
        # Private variable (price is hidden from outside)
        self.__price = 2.50

    # Implementing abstract method
    def get_price(self):
        return self.__price


# -------------------- INHERITANCE --------------------
# Chocolate inherits from IceCream
class ChocolateIceCream(IceCream):

    def __init__(self):
        # -------------------- ENCAPSULATION --------------------
        self.__price = 2.75

    # -------------------- POLYMORPHISM --------------------
    # Same method name, different behavior
    def get_price(self):
        return self.__price


# -------------------- POLYMORPHISM --------------------
# Function works for any IceCream object
def print_price(icecream):
    print("Price:", icecream.get_price())


# ======================= OBJECT CREATION =======================
vanilla = VanillaIceCream()
chocolate = ChocolateIceCream()

# ======================= USING POLYMORPHISM =======================
print_price(vanilla)
print_price(chocolate)

