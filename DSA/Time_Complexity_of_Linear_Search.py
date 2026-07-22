import time
import numpy as np
import matplotlib.pyplot as plt

def linear_search(A, x):
    for i in range(len(A)):
        if A[i] == x:
            print("Search element found successfully!")
            return
# Main
elements = np.array([i * 1000 for i in range(1, 40)])  # Corrected array generation
times = []
for i in range(1, 40):
    start = time.time()
    a = np.random.randint(0, 1000, size=i * 1000)  # Corrected randint usage
    linear_search(a, 1)  # Searching for an element not present in the array
    end = time.time()
    times.append(end - start)
    print(i * 1000,end - start)
# Plotting
plt.plot(elements, times, label="Linear Search")
plt.xlabel("Array Size")
plt.ylabel("Time Complexity")
plt.title("Time Complexity of Linear Search")
plt.grid()
plt.legend()  # Corrected typo from 'lagend' to 'legend'  
plt.show()
