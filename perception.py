import math                     # Used for mathematical operations (cos, radians)
import matplotlib.pyplot as plt # Used to plot the movement path

# Reference GPS point (origin). 
# All other GPS coordinates will be converted relative to this point.
lat0 = 28.6139
lon0 = 77.2090

# Simulated GPS coordinates showing movement over time
gps_points = [
    (28.6139, 77.2090),
    (28.6140, 77.2092),
    (28.6142, 77.2094),
    (28.6143, 77.2097),
    (28.6145, 77.2100)
]

# Lists to store converted local X and Y coordinates
x_coords = []
y_coords = []

# Loop through each GPS coordinate
for lat, lon in gps_points:
    
    # Convert longitude difference to meters (local X coordinate)
    # 111320 ≈ meters per degree of longitude
    # cos(lat0) adjusts distance depending on Earth's curvature
    x = (lon - lon0) * 111320 * math.cos(math.radians(lat0))
    
    # Convert latitude difference to meters (local Y coordinate)
    # 110540 ≈ meters per degree of latitude
    y = (lat - lat0) * 110540

    # Store the calculated coordinates
    x_coords.append(x)
    y_coords.append(y)

    # Print converted coordinates for verification
    print(f"GPS: ({lat},{lon}) → X: {x:.2f} m, Y: {y:.2f} m")

# Plot the path of movement in the local X-Y coordinate system
plt.plot(x_coords, y_coords, marker='o')

# Title of the graph
plt.title("Movement in Local X-Y Coordinates")

# Label for X-axis (distance in meters)
plt.xlabel("X (meters)")

# Label for Y-axis (distance in meters)
plt.ylabel("Y (meters)")

# Add grid lines for easier visualization
plt.grid()

# Display the graph
plt.show()