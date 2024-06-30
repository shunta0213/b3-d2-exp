import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["font.size"] = 16

# データの定義
vps_setting_current = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2]
resistor_current = [1.9330, 1.9170, 3.9645, 5.9045, 7.9931, 10.065, 11.988, 13.170, 13.182, 13.181, 13.180]
resistor_current = np.array(resistor_current)
resistor_current = -resistor_current

# グラフの作成
plt.figure(figsize=(10, 6))
plt.plot(vps_setting_current, resistor_current, marker='o', linestyle='-', color='b', label='')

# グラフのタイトルとラベル
plt.xlabel('VPS Configured Current / A')
plt.ylabel('Operational Amplifier Output Current / A')
plt.grid(True)

# グラフの表示
plt.savefig('../figures/exp3/vps-op-amp-1k.png')
