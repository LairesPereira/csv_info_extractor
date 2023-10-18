import matplotlib.pyplot as plt
import numpy as np

transactions_types = ('Enviada', 'Recebida')
penguin_means = {
    'Posto': (18, 0),
    'Cajazeiras': (35, 4),
    'Acai': (65, 0),
}

x = np.arange(len(transactions_types))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=2)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, transactions_types)
ax.legend(loc='upper left', ncols=2)
ax.set_ylim(0, 250)

plt.show()
