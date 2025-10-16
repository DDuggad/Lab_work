class Car:
    def __init__(self, model, year, price, mileage):
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage

    def depreciation(self, current_year):
        dep_rate = 0.15
        years_old = current_year - self.year
        dep_price = self.price * (1 - dep_rate) ** years_old
        print(f"Depreciated value: {dep_price:.2f}")

    def display_details(self):
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Original Price: {self.price}")
        print(f"Mileage: {self.mileage} kmpl")

car1 = Car("Toyota Camry", 2020, 2500000, 15)
car1.display_details()
car1.depreciation(2025)
