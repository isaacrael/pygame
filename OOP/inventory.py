__author__ = 'isaac'

""

Written By: Gil Rael

class InventoryItem example

""

class InventoryItem(object):
    def __init__(self, title, description, price, store_id):
        self.title = title
        self.description = description
        self.price = price
        self.store_id = store_id

    def __str__(self):
        return self.title

    def __eq__(self, other):
        if self.store_id==other.title:
            return True
        else:
            return False

    def change_description(self, description=""):
        if not description:
            self.description = raw_input("Please give me a description: ")
        self.description = description

    def change_price(self, price=-1):
        while price < 0:
            price = raw_input("Please give me the new price [X.XX]: ")
            try:
                price = float(price)
                break
            except:
                print "I'm sorry, but { } isn't valid.".format(price)
        self.price = price

    def change_title(self, title=""):
        if not title:
            title = raw_input("Please give me a new title: ")
        self.title = title

