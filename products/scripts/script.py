"""
Script to upload few fake Products to the SQLite database from a csv file.
"""
import csv
from products.models import Product


def run():
    with open('products/scripts/data.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Product.objects.get_or_create(
                product_id=row[0],
                name=row[1],
                description=row[2],
                product_type=row[3],
                product_brand=row[4],
                photo=row[5],
                price=row[6],
            )
            # creates a tuple of the new object or
            # current object and a boolean of if it was created
