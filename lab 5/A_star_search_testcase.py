import time
from A_star_search import astar, graph, weights, heuristic
    
    
def simulate_path(path, visited_order, total_cost):
    print("\n Truck traveling...\n")
    for node in path:
        print(f"Car is now at: {node}")
        time.sleep(1)
    print("\nDestination reached!")
    
    print("\nVisited Order:", visited_order)
    print("Optimal Path:", path)
    print("Total Cost:", total_cost)

# Call simulate_path with the correct arguments
path, visited_order, total_cost = astar(graph, weights, heuristic, "Disaneng", "Coligny")
simulate_path(path, visited_order, total_cost)
