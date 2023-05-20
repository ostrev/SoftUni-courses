from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @classmethod
    def dvd_capacity(cls):
        return 15

    @classmethod
    def customer_capacity(cls):
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        try:
            c_dvd = [d for d in self.dvds if d.id == dvd_id][0]
            c_customer = [c for c in self.customers if c.id == customer_id][0]
            if c_dvd in c_customer.rented_dvds:
                return f"{c_customer.name} has already rented {c_dvd.name}"
            if c_dvd.is_rented:
                return "DVD is already rented"
            if c_dvd.age_restriction > c_customer.age:
                return f"{c_customer.name} should be at least {c_dvd.age_restriction} to rent this movie"
            c_customer.rented_dvds.append(c_dvd)
            c_dvd.is_rented = True
            return f"{c_customer.name} has successfully rented {c_dvd.name}"
        except ValueError:
            pass

    def return_dvd(self, customer_id: int, dvd_id: int):
        try:
            c_dvd = [d for d in self.dvds if d.id == dvd_id][0]
            c_customer = [c for c in self.customers if c.id == customer_id][0]
            if c_dvd not in c_customer.rented_dvds:
                return f"{c_customer.name} does not have that DVD"
            c_dvd.is_rented = False
            c_customer.rented_dvds.remove(c_dvd)
            return f"{c_customer.name} has successfully returned {c_dvd.name}"
        except IndexError:
            pass

    def __repr__(self):
        result = ''
        for number, customer in enumerate(self.customers, 1):
            result += f"{customer.id}: {customer.name} of age {customer.age} has {len(customer.rented_dvds)} rented DVD's ({', '.join([d.name for d in customer.rented_dvds])})"
            result += '\n'

        for number, dvd in enumerate(self.dvds, 1):
            result += f"{number}: {dvd.name} ({dvd.creation_month} {dvd.creation_year}) has age restriction {dvd.age_restriction}. Status: {'rented' if dvd.is_rented else dvd.is_rented}"
            result += '\n'

        return result
