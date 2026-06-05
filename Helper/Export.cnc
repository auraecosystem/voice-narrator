import csv
import numpy as np

# Configuration Settings
radius = 5.0
pitch = 2.0
turns = 4.0
total_rows = 500  # Total rows in the spreadsheet

c = pitch / (2 * np.pi)
t_values = np.linspace(0, turns * 2 * np.pi, total_rows)

# Open sheet buffer and write row arrays
with open('helix_coordinates.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Excel Column Headers
    writer.writerow(['Index', 'Parameter (t)', 'X Coordinate', 'Y Coordinate', 'Z Coordinate'])
    
    for idx, t in enumerate(t_values):
        x = radius * np.cos(t)
        y = radius * np.sin(t)
        z = c * t
        writer.writerow([idx, round(t, 5), round(x, 5), round(y, 5), round(z, 5)])

print("Successfully exported 'helix_coordinates.csv'")
