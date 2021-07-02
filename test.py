import random

def generate():
    ad = ["Ahmet", "Mehmet", "Ali"]
    soyad = ["Çilli", "Bakır", "Gevrek"]
    return "{} {}".format(random.choice(ad), random.choice(soyad))

for i in range(2):
    print(generate())