import random

import string

lenght_int = random.randint(1,10)

lenght_str = random.randint(1,10)

pole_random = []
for x in range(lenght_int):
    pole_random.append(random.randint(1,100))

print (pole_random)

word_random = []

word_random_promena = (random.choices(string.ascii_uppercase, k = lenght_str))

word_random.append(word_random_promena)

print(' '.join(map(str,word_random)))

