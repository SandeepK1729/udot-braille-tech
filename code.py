import numpy as np
import matplotlib.pyplot as plt

class TactileDot:
    def __init__(self):
        self.position = 0.0  # Initial position of the tactile dot
        self.locked = False  # Locking mechanism status
        self.max_deflection = 0.7  # Maximum deflection of the tactile dot
        self.resistance_threshold = 300  # Resistance threshold in grams
        self.piezo_constant = 0.01  # Piezoelectric constant

    def apply_voltage(self, voltage):
        if not self.locked:
            deflection = self.piezo_constant * voltage
            self.position = min(self.max_deflection, deflection)

    def press(self, force):
        if not self.locked and force >= self.resistance_threshold:
            self.locked = True

    def release(self):
        self.locked = False

# Simulation parameters
time_steps = 100
voltage_input = np.linspace(0, 5, time_steps)
force_input = np.random.uniform(0, 500, time_steps)  # Simulated force input

# Initialize tactile dot
tactile_dot = TactileDot()

# Simulation loop
for i in range(time_steps):
    # Apply voltage and simulate mechanical response
    tactile_dot.apply_voltage(voltage_input[i])

    # Simulate pressing the tactile dot with a random force
    tactile_dot.press(force_input[i])

    # Release the tactile dot
    tactile_dot.release()

    # Print or log relevant information about the tactile dot (position, voltage, etc.)

# Plot the simulation results
plt.plot(voltage_input, label='Voltage Input')
plt.plot(force_input, label='Force Input')
plt.xlabel('Time Steps')
plt.ylabel('Magnitude')
plt.legend()
plt.show()
