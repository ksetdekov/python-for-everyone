class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')  # constructor

    def party(self):
        self.x += 1
        print('So far', self.x)

    def __del__(self):
        print('I am desctructed', self.x)  # desctructor


an = PartyAnimal()  # moment of contruction

an.party()
an.party()
an.party()
an = 42  # before we throw it away - __del__ fires
print('an contains', an)

print('type', type(an))
print('Dir', dir(an))
