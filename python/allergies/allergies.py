class Allergies(object):
    def __init__(self, score):
        self.score = score
        self.list = []
        self.add_allergens()

    def add_allergens(self):
        allergies = {128: 'cats', 64: 'pollen', 32: 'chocolate',
                16: 'tomatoes', 8: 'strawberries', 4: 'shellfish',
                2: 'peanuts', 1: 'eggs'}
        allerlist = list(allergies.keys())
        allerlist.sort(reverse = True)
        for i in allerlist:
            if (self.score >= i):
                self.score -= i
                self.list.append(allergies[i])
        self.list.reverse()
        if self.score != 0:
            self.list = ['eggs']

    def is_allergic_to(self, allergen):
        return allergen in self.list
