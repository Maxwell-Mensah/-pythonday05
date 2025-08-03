from shark import Shark
from canary import Canary
titi = Canary("Titi")
willy = Shark("Willy")
willy.status()
willy.smellBlood(True)
willy.status()
titi.layEgg()
print(titi.getEggsCount())
