class PartyAnimal:
    x = 0

    def __init__(self, z):
        self.name = z
        print('I am constructed')  # constructor

    def party(self):
        self.x += 1
        print(self.name, 'party count', self.x)

    def __del__(self):
        print('I am desctructed', self.x)  # desctructor


an = PartyAnimal('empty')  # moment of contruction

an.party()
an.party()
an.party()
an = 42  # before we throw it away - __del__ fires
print('an contains', an)

print('type', type(an))
print('Dir', dir(an))

s = PartyAnimal('Sally')
s.party()

j = PartyAnimal('Jim')
j.party()
s.party()
