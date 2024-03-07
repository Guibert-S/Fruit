class Fruit:
    def __init__(self, name, color, weight):
        self._name = name
        self._color = color
        self._weight = weight
        self._salade = None

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    @property
    def weight(self):
        return self._weight

    @property
    def salade(self):
        return self._salade

    @salade.setter
    def salade(self, salade):
        if self._salade is not None and self._salade != salade:
            self._salade.remove_fruit(self)
        self._salade = salade
        if salade is not None and self not in salade.fruits:
            salade.add_fruit(self)

    def increase_weight(self, grams):
        if grams > 0:
            self._weight += grams

    def is_heavy(self):
        return self._weight > 500

    def __str__(self):
        return f"Fruit{{name='{self._name}', color='{self._color}', weight={self._weight} grams}}"

class SaladeDeFruit:
    def __init__(self):
        self._fruits = []

    @property
    def fruits(self):
        return self._fruits

    def _can_add_fruit(self, fruit):
        return fruit is not None and fruit not in self._fruits

    def _can_remove_fruit(self, fruit):
        return fruit is not None and fruit in self._fruits

    def add_fruit(self, fruit):
        if self._can_add_fruit(fruit):
            self._fruits.append(fruit)
            fruit.salade = self

    def remove_fruit(self, fruit):
        if self._can_remove_fruit(fruit):
            self._fruits.remove(fruit)
            fruit.salade = None

    def get_poids_total(self):
        return sum(fruit.weight for fruit in self._fruits)

    def decrire(self):
        description = "Cette salade de fruits contient :"
        if not self._fruits:
            description += " Aucun fruit."
        else:
            for fruit in self._fruits:
                description += f"\n- {fruit.name} ({fruit.color}, {fruit.weight} grammes)"
        return description
