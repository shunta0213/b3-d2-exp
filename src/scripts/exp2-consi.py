import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from sklearn.linear_model import LinearRegression

# Use the desired style and settings
plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["font.size"] = 16

# Data
vps_current = np.array([0, 0.2, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.8, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).reshape(-1, 1)
dmm_measured = np.array([0.3355, 0.33294, 0.39245, 0.48868, 0.58391, 0.69338, 0.78972, 0.88524, 0.9963, 1.0896, 1.1853, 1.2943, 1.3906, 1.4856, 1.5952, 1.7875, 1.9934, 2.9887, 4.0003, 4.9968, 5.9886, 6.9949, 7.9953, 8.9864, 9.999, 10.994, 11.987])

vps_current = vps_current[2:]
dmm_measured = dmm_measured[2:]

# Linear regression
model = LinearRegression()
model.fit(vps_current, dmm_measured)
dmm_pred = model.predict(vps_current)
slope = model.coef_[0]
intercept = model.intercept_

# Plot data and regression line
plt.figure(figsize=(10, 6))
plt.plot(vps_current, dmm_measured, marker='o', linestyle='-', color='b')
plt.plot(vps_current, dmm_pred, linestyle='--', color='r', label=f'$A_{{real}} = {slope:.3f}A_{{conf}} + {intercept:.3f}$')

# Labels and grid
plt.xlabel('VPS configured current / A')
plt.ylabel('DMM measured current / A')
plt.legend()
plt.grid(True)

# Save figure
plt.savefig('../figures/consi2/vps-dmm-with-fit-wo-offset.png')

# Show plot
plt.show()
