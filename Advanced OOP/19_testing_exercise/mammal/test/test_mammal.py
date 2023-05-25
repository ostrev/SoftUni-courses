from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Many', 'Type_Mammal', "Sound_Mammal")

    def test_initialization(self):
        self.assertEqual('Many', self.mammal.name)
        self.assertEqual('Type_Mammal', self.mammal.type)
        self.assertEqual('Sound_Mammal', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual("Many makes Sound_Mammal", self.mammal.make_sound())

    def test_get_kingdom_return_animal(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("Many is of type Type_Mammal", self.mammal.info())


mammal = Mammal
if __name__ == "__main__":
    main()