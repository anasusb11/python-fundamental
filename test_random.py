import random
"""
for i in range(5):
    print(random.randint(10,20))"""

users = ["Hamim", "Zaka", "Fredy", "Hafiz", "Luthfi"]

batas_bawah = 0
batas_atas = len(users) - 1

random_int = random.randint(batas_bawah, batas_atas)

winner = random.choice(users)

print(winner)