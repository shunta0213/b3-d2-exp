import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["font.size"] = 16

# データの定義
vps_setting_current = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
op_amp_output_current = [0.31292, 0.9989, 2.0048, 3.0077, 4.0270, 5.0307, 6.0304, 7.0444, 8.0524, 9.0509, 10.071, 11.074, 12.074]
op_amp_output_current = -np.array(op_amp_output_current)

# グラフの作成
plt.figure(figsize=(10, 6))
plt.plot(vps_setting_current, op_amp_output_current, marker='o', linestyle='-', color='b', label='Op Amp Output Current')

# グラフのタイトルとラベル
plt.xlabel('vps configured current / A')
plt.ylabel('Operational Amplifier Output Current / A')
plt.grid(True)

# グラフの表示
plt.savefig('../figures/exp3/vps-op-amp-10k.png')
