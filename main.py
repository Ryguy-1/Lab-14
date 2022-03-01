import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_loc = "data.csv"

df = pd.read_csv(csv_loc)
print(df.head)

print(df.columns.values)

distance_list = df['Distance'].tolist()
print(np.sum(np.array(distance_list)))

cumulative_distance_list = np.cumsum(np.array(distance_list))/100
cumulative_distance_list = [value for value in cumulative_distance_list if value > 0.1]
times_list = [(1/60) * x for x in range(len(cumulative_distance_list))]

print(cumulative_distance_list[60])
print(times_list[60])

# np polyfit
coeffs = np.polyfit(times_list, cumulative_distance_list, 2)


# Graph best fit line for cumulative distance vs time
plt.figure()
plt.plot(times_list, cumulative_distance_list)
plt.plot(times_list, np.poly1d(coeffs)(times_list))
plt.xlabel('Time (seconds)')
plt.ylabel('Cumulative Distance (cm)')
plt.title('Cumulative Distance vs Time')
plt.show()

# Print best fit line
print("Best fit line: y = %.2f + %.2fx + %.2fx^2" % (coeffs[2], coeffs[1], coeffs[0]))


# Find derivative of best fit line
derivative = np.polyder(coeffs)

# Print derivative
print(f"Derivative: y' = {derivative[1]} + {derivative[0]}x")
velocities_list = [derivative[0] * x + derivative[1] for x in times_list]
print(velocities_list)