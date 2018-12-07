def main():
    #Input list with starting time and outsourcing cost
    tasks = [(1,5), (2,2), (3,4), (7,2)]
    
    #Sorting by starting time
    tasks = sorted(tasks, key = lambda x: x[0])
    
    fire_cost = 3
	hire_cost = 2
    daily_cost = 2

    #Check number of tasks
    card = len(tasks)
    if card == 0:
        return 0

    worker_path = [0] * card
    freelance_path = [0] * card
    
    #Simulate first task carried out by an internal worker
    worker_path[0] = hire_cost + daily_cost
    
    #Simulate first task is carried out by a freelancer
    freelance_path[0] = tasks[0][1] 

    for i in range (1, card):
        worker_path[i] = min(worker_path[i-1]+(tasks[i][0]-tasks[i-1][0])
        *daily_cost, freelance_path[i-1]+hire_cost+daily_cost)
        
        freelance_path[i] = min(freelance_path[i-1]+tasks[i][1],
        worker_path[i-1]+fire_cost+tasks[i][1])

    return min(worker_path[card-1], freelance_path[card-1])
    
main()