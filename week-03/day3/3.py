# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class WeakPirate():

    def __init__(self):
        self.rum = 0

    def drink_rum(self):
        self.rum += 1

    def hows_goin_mate(self):
        if self.rum >= 5:
            return 'Arrrr!'
        else:
            return 'Nothin'

weakpirate1 = WeakPirate()
weakpirate1.drink_rum()
print(weakpirate1.hows_goin_mate())
weakpirate1.drink_rum()
print(weakpirate1.hows_goin_mate())
weakpirate1.drink_rum()
print(weakpirate1.hows_goin_mate())
weakpirate1.drink_rum()
print(weakpirate1.hows_goin_mate())
weakpirate1.drink_rum()
print(weakpirate1.hows_goin_mate())
weakpirate1.drink_rum()
print(weakpirate1.hows_goin_mate())
weakpirate1.drink_rum()
print(weakpirate1.hows_goin_mate())
weakpirate1.drink_rum()
print(weakpirate1.hows_goin_mate())
weakpirate1.drink_rum()
print(weakpirate1.hows_goin_mate())
weakpirate1.drink_rum()
print(weakpirate1.hows_goin_mate())
weakpirate1.drink_rum()
print(weakpirate1.hows_goin_mate())
