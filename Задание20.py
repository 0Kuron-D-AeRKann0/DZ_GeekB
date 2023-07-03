list_letters = {1:"AEIOULNSTRАВЕИНОРСТ",
                2:"DGДКЛМПУ",
                3:"BCMPБГЁЬЯ",
                4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",
                8:"JXШЭЮ",
                10:"QZФЩЪ"}

w = input("Ваше слово: ").upper()
summa = 0
for i in w:
    for k, v in list_letters.items():
        if i in v:
            summa += k
print(f"Ваше стоимость: {summa}")