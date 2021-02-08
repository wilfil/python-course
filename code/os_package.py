import os
#import env
from math import pi

#print(pi)

#digits = int(input("how many digits for pi? "))

digits = int(os.getenv("DIGITS") or 10)

print("%.*f" % (digits, pi))
