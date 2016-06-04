import random

def demo():
    groups = ['lime', 'teal', 'olive']
    random.shuffle(groups,random.random)
    for i in groups:
        if i == 'lime':
            lime = ['Attila', 'Zoli', 'Peti', 'Timi', 'Kriszti', 'Fabics Peti']
            random.shuffle(lime,random.random)
            print(i, lime)
        elif i == 'teal':
            teal = ['Robi', 'Mate', 'Anna', 'Pfeter', 'Sandor', 'Viktor']
            random.shuffle(teal,random.random)
            print(i, teal)
        else:
            olive = ['Aliz', 'Zsolti', 'Dani', 'Aron', 'Pocok', 'David']
            random.shuffle(olive,random.random)
            print(i, olive)

demo()
