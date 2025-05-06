from django.db import transaction


def perform_transfer(sender, receiver, amount):
    with transaction.atomic():
        """
        It is a context manager provided by Django to ensure that a block of
        database operations is treated as a single atomic transaction.
        """
        sender.balance -= amount
        sender.save()

        if amount > 10000:
            transaction.set_rollback(True)

        receiver.balance += amount
        receiver.save()

        # If any exception occurs, the transaction will be rolled back
        # and no changes will be saved to the database.

        # What is rolled back?
        #  1. Only the operations that:
        #  2. Interact with the database