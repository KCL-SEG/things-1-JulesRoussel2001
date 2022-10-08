from django.core.management.base import BaseCommand, CommandError
from faker import Faker

class Command(BaseCommand):
    def _init_(self):
        super()._init_()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        print("hey")
