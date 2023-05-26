import csv
from LegacySite.models import Product, User, Card

def import_products(fname):
    for row in csv.reader(open(fname)):
        prod, created = Product.objects.get_or_create(
            product_id=row[0],
            product_name=row[1],
            product_image_path=row[2],
            recommended_price=row[3],
            description=row[4],
        )
        if created:
            prod.save()


def import_users(fname):
    for row in csv.reader(open(fname)):
        user, created = User.objects.get_or_create(
            username=row[2],
            password=row[3],
        )
        if created:
            user.save()


def import_cards(fname):
    for row in csv.reader(open(fname)):
        product_id = int(row[2])  # Convert the product_id value to an integer
        product = Product.objects.get(product_id=product_id)
        user = User.objects.get(username=row[5])
        card = Card.objects.create(
            data=row[1].encode(),
            product=product,  # Assign the product instance directly
            amount=int(row[3]),
            fp=row[4],
            user=user,
            used=bool(row[6])
        )
        card.save()


import_users('users.csv')
import_products('products.csv')
import_cards('cards.csv')
