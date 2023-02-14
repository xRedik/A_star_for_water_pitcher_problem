import unittest
from water_pitcher import heuristic, a_star_algorithm

class TestHeuristic(unittest.TestCase):
    def test_admissible(self):
        # Test if the heuristic never overestimates the actual cost
        for i in range(1, 10):
            self.assertLessEqual(heuristic((i, 0), 10), 10 - i)
    
    def test_consistent(self):
        test_state_1 = [2, 0, 6, 72, 10]
        test_state_2 = [2, 5, 6, 72, 10]
        test_state_3 = [0, 5, 6, 72, 12]
        target_quantity = 143
        
        # Test if the estimated cost from state1 to target_quantity is less than or equal to the sum of the cost from state1 to state2 and from state2 to target_quantity
        self.assertLessEqual(heuristic(test_state_1, target_quantity), heuristic(test_state_1, target_quantity) + heuristic(test_state_2, target_quantity))

        # Test if the estimated cost from state2 to target_quantity is less than or equal to the sum of the cost from state2 to state3 and from state3 to target_quantity
        self.assertLessEqual(heuristic(test_state_2, target_quantity), heuristic(test_state_2, target_quantity) + heuristic(test_state_3, target_quantity))

class TestAStar(unittest.TestCase):
    def test_input_1(self):
        capacities = [2]
        target_quantity = 4

        self.assertEqual(a_star_algorithm(capacities,target_quantity),4)

    def test_input_2(self):
        capacities = [2,2]
        target_quantity = 143
        self.assertEqual(a_star_algorithm(capacities,target_quantity),-1)

    def test_input_3(self):
        capacities = [1,2,3]
        target_quantity = 7

        self.assertEqual(a_star_algorithm(capacities,target_quantity),6)

if __name__ == '__main__':
    unittest.main()