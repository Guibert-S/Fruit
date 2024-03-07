import unittest
from Fruit import *  # Assurez-vous que cette importation correspond à votre structure de fichiers

class FruitTest(unittest.TestCase):

    def test_increase_weight(self):
        apple = Fruit("Apple", "Red", 150)
        apple.increase_weight(50)
        self.assertEqual(200, apple.weight)

    def test_is_heavy(self):
        watermelon = Fruit("Watermelon", "Green", 1000)
        self.assertTrue(watermelon.is_heavy())

        grape = Fruit("Grape", "Purple", 50)
        self.assertFalse(grape.is_heavy())

    def test_to_string(self):
        banana = Fruit("Banana", "Yellow", 120)
        expected = "Fruit{name='Banana', color='Yellow', weight=120 grams}"
        self.assertEqual(expected, str(banana))

if __name__ == '__main__':
    unittest.main()




class SaladeDeFruitTest(unittest.TestCase):

    def setUp(self):
        self.salade1 = SaladeDeFruit()
        self.salade2 = SaladeDeFruit()
        self.pomme = Fruit("Pomme", "Rouge", 150)
        self.banane = Fruit("Banane", "Jaune", 120)

    def test_ajouter_fruit(self):
        self.salade1.add_fruit(self.pomme)
        self.assertEqual(1, len(self.salade1.fruits))
        self.salade1.add_fruit(self.banane)
        self.assertEqual(2, len(self.salade1.fruits))

    def test_get_poids_total(self):
        self.salade1.add_fruit(self.pomme)
        self.salade1.add_fruit(self.banane)
        self.assertEqual(270, self.salade1.get_poids_total())

    def test_decrire(self):
        self.salade1.add_fruit(self.pomme)
        expected_description = "Cette salade de fruits contient :\n- Pomme (Rouge, 150 grammes)"
        self.assertIn(expected_description, self.salade1.decrire())

    def test_ajouter_fruit_a_multiples_salades(self):
        self.salade1.add_fruit(self.pomme)
        self.salade2.add_fruit(self.pomme)
        self.assertNotIn(self.pomme, self.salade1.fruits)
        self.assertIn(self.pomme, self.salade2.fruits)
        self.assertEqual(self.salade2, self.pomme.salade)

    def test_retirer_fruit_non_present(self):
        self.salade1.remove_fruit(self.pomme)
        self.assertEqual(0, len(self.salade1.fruits))

    def test_gestion_bidirectionnelle_des_liens(self):
        self.salade1.add_fruit(self.pomme)
        self.salade1.remove_fruit(self.pomme)
        self.assertIsNone(self.pomme.salade)
        self.assertNotIn(self.pomme, self.salade1.fruits)

if __name__ == '__main__':
    unittest.main()


class AssociationTest(unittest.TestCase):

    def test_association(self):
        salade = SaladeDeFruit()
        pomme = Fruit("Pomme", "Rouge", 150)

        salade.add_fruit(pomme)

        self.assertIn(pomme, salade.fruits)
        self.assertEqual(salade, pomme.salade)

        salade.remove_fruit(pomme)

        self.assertNotIn(pomme, salade.fruits)
        self.assertIsNone(pomme.salade)

    def test_retirer_fruit_change_salade(self):
        salade1 = SaladeDeFruit()
        salade2 = SaladeDeFruit()
        banane = Fruit("Banane", "Jaune", 120)

        salade1.add_fruit(banane)
        salade2.add_fruit(banane)

        self.assertIn(banane, salade2.fruits)
        self.assertEqual(salade2, banane.salade)
        self.assertNotIn(banane, salade1.fruits)

if __name__ == '__main__':
    unittest.main()

