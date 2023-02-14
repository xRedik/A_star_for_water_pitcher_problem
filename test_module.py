import unittest
from water_pitcher import heuristic, a_star_algorithm

#Testing the heuristic function
class TestHeuristic(unittest.TestCase):

    #Test if the heuristic is admissible or not
    def test_admissible(self):
        current_state = [2,3,5,6]
        target_quantity = 6
        self.assertLessEqual(heuristic(current_state, target_quantity), target_quantity - current_state[-1])

        current_state = [3,4,7]
        target_quantity = 3
        self.assertEqual(heuristic(current_state, target_quantity), 0)
    
    #Test if the heuristic is consistent
    def test_consistent(self):
        test_state_1 = [2, 0, 6, 72, 10]
        test_state_2 = [2, 5, 6, 72, 10]
        test_state_3 = [0, 5, 6, 72, 12]
        target_quantity = 143
        
        #Test if the estimated cost from test_state_1 to target_quantity is less than or equal 
        #to the total cost from test_state_1 to test_state_2 and from test_state_2 to target_quantity
        self.assertLessEqual(heuristic(test_state_1, target_quantity), 
                             heuristic(test_state_1, target_quantity) + heuristic(test_state_2, target_quantity))

        #Test if the estimated cost from test_state_2 to target_quantity is less than or equal 
        #to the total cost from test_state_2 to test_state_3 and from test_state_3 to target_quantity
        self.assertLessEqual(heuristic(test_state_2, target_quantity), 
                             heuristic(test_state_2, target_quantity) + heuristic(test_state_3, target_quantity))


#Testing the A star algorithm with input examples of capacities and target quantity
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