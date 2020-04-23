class PartyAnimal:
    x = 0

    def party(self):
        self.x += 1
        print('So far', self.x)


an = PartyAnimal()  # moment of contruction

an.party()
an.party()
an.party()

print('type', type(an))
print('Dir', dir(an))
