# Unittest is made up of three parts Arrange, Act, and an Assert.
# Write tests for the code you would like to see.
# When the tests pass, you don't need to write any code, when they fail, write the code to make the tests pass
# 1. Create a class that inherits from unittest.TestCase
# 2. Import whatever it is you want to test
# 3. Then write methods that begin with the word test_
# 4. Make assertions using the built in assertions

import unittest
from stack import Stack

class TestStack(unittest.TestCase):
        def test_constructor_is_no_arg(self):
                # Arrange

                # Act
                Stack()

                # Assert

        def test_new_stack_has_zero_elements(self):
                # Arrange
                s = Stack()

                # Act
                result = len(s)

                # Assert
                self.assertEqual(result, 0)
        
        def test_push_increase_count_by_one(self):
                # Arrange
                s = Stack()

                # Act
                s.push(True)

                # Assert
                self.assertEqual(len(s), 1)

        def test_peek_returns_last_item_but_does_not_remove_it_from_stack(self):
                # Arrange
                s = Stack()

                # Act
                s.push(True)

                # Assert
                self.assertEqual(s.peek(), True)

        def test_pop_returns_last_pushed_item_and_removes_it(self):
                # Arrange
                s = Stack()
                s.push(5.9)

                # Act
                result = s.pop()

                # Assert
                self.assertEqual(result, 5.9)

        def test_pushing_lots_of_values_makes_count_increment(self):
                # Arrange
                s = Stack()

                # Act
                for i in range(100):
                        s.push(i)

                # Assert
                self.assertEqual(len(s), 100)

        def test_popping_lots_of_values_makes_count_decrease(self):
                # Arrange
                s = Stack()

                # Act
                for i in range(100):
                        s.push(i)
                for i in range(50):
                        s.pop()

                # Assert
                self.assertEqual(len(s), 50)

        def test_peeking_still_returns_last_pushed_element_not_popped(self):
                # Arrange
                s = Stack()

                # Act
                for i in range(100):
                        s.push(i)
                for i in range(50):
                        s.pop()

                # Assert
                self.assertEqual(s.peek(), 49)
