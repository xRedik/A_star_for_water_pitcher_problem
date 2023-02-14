import sys
import numpy as np
import heapq
import os

def read_file(filename):
    with open(filename,"r") as f:
        capacities = np.array(f.readline().split(","))
        target = int(f.readline())
    return capacities.astype(np.int32), target

def heuristic(current_state,target_quantity):
    return np.abs(np.sum(current_state) - target_quantity)

def a_star_algorithm(capacities,target_quantity):
    capacities = np.append(capacities, sys.maxsize)
    initial_state = list(np.zeros(capacities.shape, dtype = np.int32))
    initial_heuristic = heuristic(initial_state,target_quantity)
    step = 0

    fridge_pq = [(initial_heuristic+step, step, initial_state)]
    
    visited_states = set()
    
    while fridge_pq:
        _ , step, current_state =  heapq.heappop(fridge_pq)

        if current_state[-1] == target_quantity:
           return step
        
        elif current_state[-1] > target_quantity:
            return -1

        visited_states.add(tuple(current_state))

        for i in range(capacities.shape[0]):
            for j in range(capacities.shape[0]):
                if i==j:
                    continue
                next_state = current_state.copy()
                pour = min(capacities[i],capacities[j])
                if next_state[i]+pour <= capacities[i] and next_state[j]-pour >= 0 and j!=capacities.shape[0]-1:
                    next_state[i]+=pour
                    next_state[j]-=pour
                else:
                    if i!=capacities.shape[0]-1:
                        next_state[i] = capacities[i] - next_state[i]
                if tuple(next_state) not in visited_states:
                    heapq.heappush(fridge_pq, (step+1+heuristic(next_state,target_quantity), 
                                   step+1, next_state))

    return -1

def main():
    filename = sys.argv[1]
    if len(sys.argv)==1:
        raise Exception("Please add the second argument for the name of the file")
    if not os.path.isfile(filename):
        raise FileExistsError("File do not exist")
    capacities, target_quantity = read_file(filename)

    if np.size(capacities)==0:
        raise Exception("There is no capacities in the first line of the file")
    
    if np.size(capacities)==0:
        raise Exception("There is no target quantity in the second line of the file")
    
    result = a_star_algorithm(capacities,target_quantity)

    if(result == -1):
        print("There is no path for the target quantity")
    else:
        print("The shortest path:", result)


if __name__ == "__main__":
    main()