class Tiger():

    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def do_lunch(self, quantity):
        print('Beef {} kg'.format(quantity))


tiger = Tiger(name="sammy", origin="royal bengal")
print(tiger.name, tiger.origin)
tiger.do_lunch(40)
