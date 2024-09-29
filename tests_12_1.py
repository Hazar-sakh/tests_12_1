from unittest import TestCase
import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(TestCase):
    def test_walk(self):
        c = Runner('Dobrynya')
        for i in range(10):
            c.walk()
        self.assertEqual(c.distance, 50)

    def test_run(self):
        golo = Runner('Alyosha')
        for i in range(10):
            golo.run()
        self.assertEqual(golo.distance, 100)

    def test_challenge(self):
        giga = Runner('Yarilo')
        mega = Runner('Veles')
        for i in range(10):
            giga.run()
            mega.walk()
        self.assertNotEqual(giga.distance, mega.distance)


if __name__ == '__main__':
    unittest.main

