from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for prod in self.products:
            if prod.name == product_name:
                return prod

    def remove(self, product_name):
        for prod in self.products:
            if prod.name == product_name:
                self.products.remove(prod)

    def __repr__(self):
        result = ''
        for prod in self.products:
            result += f"{prod.name}: {prod.quantity}\n"
        return result.strip()
