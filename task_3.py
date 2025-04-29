import numpy as np
import matplotlib.pyplot as plt

x = list(range(2000, 2024))
y = [49556660, 49106855, 48677281, 48315136, 47979507, 47585556, 47278694,
     47062798, 46819175, 46623731, 46456003, 46307853, 46210056, 46126770, 45972380,
     45784896, 45616832, 45436041, 45208907, 44957458, 44680014, 44298640, 41048766,
     37732836]

labels = [str(year) for year in x]

colors = plt.get_cmap('hsv')(np.linspace(0, 1, len(x)))

plt.figure(figsize=(9, 9))

plt.pie(y,
        labels=labels,
        autopct='%1.1f%%',   # виведення відсотків на кожному секторі
        colors=colors)

plt.axis('equal')
plt.title("Кругова діаграма. Україна - показники загального населення за роками (2000-2023)")
plt.tight_layout()
plt.show()