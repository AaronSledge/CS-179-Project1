#Provide a visualization of the relationship between time(x) and distance(y)
#inputs: list of sum of distance(array float), list of current_time in seconds(array float)
#output: Plot of distance over increasing amount of time
#Jason

import numpy as np
import ast
import matplotlib.pyplot as plt

def analyzeDistance(filename, maxTime = 600, numPoints = 100):
    
    runs = []
    # read file and parse each line of input file
    with open(filename, "r") as f:
        for line in f:
            if line.strip():
                try:
                    run = ast.literal_eval(line.strip())
                    runs.append(run)
                except Exception as e:
                    print(f"Error with parsing line: {line}\n{e}")
                    
    # making time grid
    timeGrid = np.linspace(0, maxTime, numPoints)
    
    interpolatedRuns = []
    
    for run in runs:
        # separates distances and times from all pairs of (distance, time)
        distances, times = zip(*run)
        distances = np.array(distances)
        times = np.array(times)
        
        # sorting the data by time
        sortIdx = np.argsort(times)
        times = times[sortIdx]
        distances = distances[sortIdx]
        
        # interpolation over the grid
        interpDistances = np.interp(timeGrid, times, distances)
        interpolatedRuns.append(interpDistances)
        
    # converts the list of runs to np array    
    interpolatedRuns = np.array(interpolatedRuns)
    
    # computes the mean distance across all runs at each of the times
    meanDist = np.mean(interpolatedRuns, axis = 0)
    
    # plotting
    
    plt.figure(figsize=(10, 6))
    plt.plot(timeGrid, meanDist, label = "Average Distance", color = "red")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Distance (meters)")
    plt.title("Average Distance Over Time Graph for 50 runs")
    plt.legend()
    plt.grid(True)
    plt.show()