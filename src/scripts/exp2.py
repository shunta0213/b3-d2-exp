import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["font.size"] = 16

vps_current = [0, 0.2, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.8, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
dmm_measured = [0.3355, 0.33294, 0.39245, 0.48868, 0.58391, 0.69338, 0.78972, 0.88524, 0.9963, 1.0896, 1.1853, 1.2943, 1.3906, 1.4856, 1.5952, 1.7875, 1.9934, 2.9887, 4.0003, 4.9968, 5.9886, 6.9949, 7.9953, 8.9864, 9.999, 10.994, 11.987]

plt.figure(figsize=(10, 6))
plt.plot(vps_current, dmm_measured, marker='o', linestyle='-', color='b')

plt.xlabel('VPS configured current / A')
plt.ylabel('DMM measured current / A')

plt.grid(True)

plt.savefig('../figures/exp2/vps-dmm.png')
