import unittest
import logging
from rt_with_exceptions import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="runner_tests.log",
    encoding="UTF-8",
    format="%(asctime)s | %(levelname)s | %(message)s"
)

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner(name="Test Runner", speed=-5)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)
            self.assertTrue(isinstance(e, ValueError))

    def test_run(self):
        try:
            runner = Runner(name=123, speed=10)  # Неверный тип для name
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)
            self.assertTrue(isinstance(e, TypeError))

if __name__ == "__main__":
    unittest.main()

