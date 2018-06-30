from math import radians, sin, cos, atan
#import math
an = float(input('Qual o ângulo? '))

sen = sin(radians(an))
#sen = math.sin(math.radians(an))
print('SENO do ângulo {} é {:.2f}'.format(an, sen))

cons = cos(radians(an))
#ons = math.cos(math.radians(an))
print('CONSENO do ângulo {} é {:.2f}'.format(an, cons))

tan = atan(radians(an))
#tan = math.atan(math.radians(an))
print('TANGENTE do ângulo {} é {:.2f}'.format(an, tan))
