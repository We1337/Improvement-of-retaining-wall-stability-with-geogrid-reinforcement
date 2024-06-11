import math

# Soil properties
phi = 30  # internal friction angle in degrees
gamma = 18  # unit weight of soil in kN/m³
c = 0  # cohesion in kN/m² (for sandy soil, it's zero)

# Retaining wall properties
H = 5  # height of the wall in meters
B = 2  # base width of the wall in meters

# Geogrid reinforcement properties
T = 100  # tensile strength of geogrid in kN/m
n = 3  # number of reinforcement layers

# Convert friction angle to radians
phi_rad = math.radians(phi)

# Calculate the active earth pressure coefficient (Ka) using Rankine's theory
Ka = math.tan(math.pi / 4 - phi_rad / 2) ** 2

# Calculate the total active earth pressure (Pa) without reinforcement
Pa = 0.5 * Ka * gamma * H**2  # Pa = 1/2 * Ka * γ * H²

# Calculate the resisting moment (Mr) and overturning moment (Mo) without reinforcement
Mo = Pa * H / 3  # Overturning moment (about the toe)
Mr = gamma * B * H**2 / 2  # Resisting moment (about the toe)

# Factor of safety without reinforcement
FoS_without_reinforcement = Mr / Mo

# Calculate the additional resisting force due to geogrid reinforcement
F_geogrid = n * T

# Calculate the new resisting moment with reinforcement
Mr_with_reinforcement = Mr + F_geogrid * H / 2

# Factor of safety with reinforcement
FoS_with_reinforcement = Mr_with_reinforcement / Mo

print(f"Factor of Safety without reinforcement: {FoS_without_reinforcement:.2f}")
print(f"Factor of Safety with reinforcement: {FoS_with_reinforcement:.2f}")
