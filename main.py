from generate_data import GenerateData
from alg.alg_for_test.lin import *
from alg.alg_for_test.map_ import *
from alg.alg_for_test.tree import *
import matplotlib.pyplot as plt

times_lin_alg_prep = []
times_map_alg_prep = []
times_tree_alg_prep = []
times_lin_alg = []
times_map_alg = []
times_tree_alg = []
GenerateData.clear_files() # очищаю файлы входных данных
k = 11
for i in range(k):
    data_points = GenerateData.generate_points(2 ** i)
    data_rects = GenerateData.generate_rects(1000)

    time_lin = lin_alg()
    time_map = map_alg()
    time_tree = tree_alg()

    times_map_alg_prep.append(time_map[0] * 1000) # * 1000 для перевода в с -> мс
    times_tree_alg_prep.append(time_tree[0] * 1000)

    times_lin_alg.append(time_lin * 1000)
    times_map_alg.append(time_map[1] * 1000)
    times_tree_alg.append(time_tree[1] * 1000)

X = list(range(k))
with open("results/preprocessing_times.txt", mode="w") as f:
    f.write("Map\n")
    for i in range(k):
        f.write(str(times_map_alg_prep[i]) + '\n')
    f.write("PersistentSegmentTree\n")
    for i in range(k):
        f.write(str(times_tree_alg_prep[i]) + '\n')
with open("results/algorithm_times.txt", mode="w") as f:
    f.write("Linear\n")
    for i in range(k):
        f.write(str(times_lin_alg[i]) + '\n')
    f.write("Map\n")
    for i in range(k):
        f.write(str(times_map_alg[i]) + '\n')
    f.write("PersistentSegmentTree\n")
    for i in range(k):
        f.write(str(times_tree_alg[i]) + '\n')

figure, axis = plt.subplots(2, 1, figsize=(16, 10))

axis[0].plot(X, times_lin_alg, "r")
axis[0].plot(X, times_map_alg, "b")
axis[0].plot(X, times_tree_alg, "g")

axis[1].plot(X, times_map_alg_prep, "b")
axis[1].plot(X, times_tree_alg_prep, "g")

axis[1].title.set_text("preprocessing")
axis[1].set_ylabel('Time,[ms]')
axis[1].set_xlabel('i, 2**i')
axis[1].grid()
axis[1].set_xticks(X)

axis[0].title.set_text("algorithm")
axis[0].set_ylabel('Time,[ms]')
axis[0].set_xlabel('i, 2**i')
axis[0].grid()
axis[0].set_xticks(X)
figure.legend(["lin", "map", "tree"])
plt.show()
