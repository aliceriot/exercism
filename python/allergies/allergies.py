class Allergies(object):
    def __init__(self, score):
        self.score = score
        self.list = []
        self.add_allergens()

    def add_allergens(self):
        allergens = {1: 'eggs', 2: 'peanuts', 4: 'shellfish',
                8: 'strawberries', 16: 'tomatoes', 32: 'chocolate',
                64: 'pollen', 128: 'cats'}
        indices = filter(lambda k: self.score & k > 0, allergens.keys())
        self.list = [allergens[k] for k in sorted(list(indices))]

    def is_allergic_to(self, allergen):
        return allergen in self.list
