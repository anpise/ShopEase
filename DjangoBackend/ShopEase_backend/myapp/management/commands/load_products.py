from django.core.management.base import BaseCommand
from django.db import connection
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Gets project root
sql_file_path = os.path.join(BASE_DIR, "insert_prodcuts.sql")

class Command(BaseCommand):
    help = "Load products into the database from an SQL file"

    def handle(self, *args, **kwargs):
        print(sql_file_path)
        with open("insert_products.sql", "r") as file:
            sql_script = file.read()

        with connection.cursor() as cursor:
            cursor.executescript(sql_script)

        self.stdout.write(self.style.SUCCESS("Successfully loaded products!"))
