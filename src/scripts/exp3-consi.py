import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from sklearn.linear_model import LinearRegression

# Use the desired style and settings
plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["font.size"] = 16

vps_setting_current = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
vps_output_current = [0.3355, 0.9963, 1.9934, 2.9887, 4.0003, 4.9968, 5.9886, 6.9949, 7.9953, 8.9864, 9.999, 10.994, 11.987]
op_amp_output_current = [-0.31292, -0.9989, -2.0048, -3.0077, -4.027, -5.0307, -6.0304, -7.0444, -8.0524, -9.0509, -10.071, -11.074, -12.074]
vps_output_current = np.array(vps_output_current).reshape(-1, 1)
op_amp_output_current = np.array(op_amp_output_current)

# Linear regression
model = LinearRegression()
model.fit(vps_output_current, op_amp_output_current)
dmm_pred = model.predict(vps_output_current)
slope = model.coef_[0]
intercept = model.intercept_


plt.figure(figsize=(10, 6))
plt.plot(vps_output_current, op_amp_output_current, marker='o', linestyle='-', color='b')
plt.plot(vps_output_current, dmm_pred, linestyle='--', color='r', label=f'$A_{{real}} = {slope:.3f}A_{{conf}} + {intercept*1e3:.3f}\\times 10^{{-3}}$')

plt.xlabel('VPS actual current / A')
plt.ylabel('Op-amp output current / A')
plt.legend()
plt.grid(True)

plt.savefig('../figures/consi3/10k-vps-op-amp-with-fit.png')
plt.close()


vps_output_current_2 = [0.3355, 0.33294, 0.39245, 0.58391, 0.78972, 0.9963, 1.1853, 1.3906, 1.5952, 1.7875, 1.9934]
op_amp_output_current_2 = [-1.9330, -1.9170, -3.9645, -5.9045, -7.9931, -10.065, -11.988, -13.170, -13.182, -13.181, -13.180]
vps_output_current = np.array(vps_output_current_2).reshape(-1, 1)
op_amp_output_current = np.array(op_amp_output_current_2)

# Linear regression
model = LinearRegression()
model.fit(vps_output_current, op_amp_output_current)
dmm_pred = model.predict(vps_output_current)
slope = model.coef_[0]
intercept = model.intercept_


plt.figure(figsize=(10, 6))
plt.plot(vps_output_current, op_amp_output_current, marker='o', linestyle='-', color='b')
plt.plot(vps_output_current, dmm_pred, linestyle='--', color='r', label=f'$A_{{real}} = {slope:.3f}A_{{conf}} + {intercept:.3f}$')

plt.xlabel('VPS actual current / A')
plt.ylabel('Op-amp output current / A')
plt.legend()
plt.grid(True)

plt.savefig('../figures/consi3/1k-vps-op-amp-with-fit.png')
plt.close()

vps_output_current_2 = [0.3355, 0.33294, 0.39245, 0.58391, 0.78972, 0.9963, 1.1853, 1.3906, 1.5952, 1.7875, 1.9934]
op_amp_output_current_2 = [-1.9330, -1.9170, -3.9645, -5.9045, -7.9931, -10.065, -11.988, -13.170, -13.182, -13.181, -13.180]
vps_output_current_2 = vps_output_current_2[2:-4]
op_amp_output_current_2 = op_amp_output_current_2[2:-4]
vps_output_current = np.array(vps_output_current_2).reshape(-1, 1)
op_amp_output_current = np.array(op_amp_output_current_2)


# Linear regression
model = LinearRegression()
model.fit(vps_output_current, op_amp_output_current)
dmm_pred = model.predict(vps_output_current)
slope = model.coef_[0]
intercept = model.intercept_


plt.figure(figsize=(10, 6))
plt.plot(vps_output_current, op_amp_output_current, marker='o', linestyle='-', color='b')
plt.plot(vps_output_current, dmm_pred, linestyle='--', color='r', label=f'$A_{{real}} = {slope:.3f}A_{{conf}} + {intercept:.3f}$')

plt.xlabel('VPS actual current / A')
plt.ylabel('Op-amp output current / A')
plt.legend()
plt.grid(True)

plt.savefig('../figures/consi3/1k-vps-op-amp-with-fit-small.png')
plt.close()
