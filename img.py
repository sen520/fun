from matplotlib import pyplot as plt
import numpy as np

# data = np.arange(10)
# plt.plot(data)
# fig = plt.figure()
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# # plt.plot([1.5, 3.5, -2, 1.6])
# plt.plot(np.random.randn(50).cumsum(), 'k--')
# _ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
# ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
#
# fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
# for i in range(2):
#     for j in range(2):
#         axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
#         plt.subplots_adjust(wspace=0, hspace=0)
# fig.show()


# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(np.random.randn(1000).cumsum())
# ax.set_xticks([0, 250, 500, 750, 1000])
# ax.set_xlabel('Stages')
# ax.set_title('test plot')
# fig.show()


# from numpy.random import randn
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(randn(1000).cumsum(), 'k', label='one')
# ax.plot(randn(1000).cumsum(), 'k--', label='two')
# ax.plot(randn(1000).cumsum(), 'k', label='three')
# ax.legend(loc='best')
#
# fig.show()


# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_values, squares, linewidth=5)
# plt.title('square numbers', fontsize=24)
# plt.xlabel('value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)
# plt.tick_params(axis='both', labelsize=14)
# plt.show()

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=200)
# plt.title('square numbers', fontsize=24)
# plt.xlabel('value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)
# plt.tick_params(axis='both', labelsize=14)
# plt.show()

# x_values = list(range(1,1001))
# y_values = [x ** 2 for x in x_values]
# plt.scatter(x_values, y_values, s=10, c=(0, 0.8, 0))
# plt.title('square numbers', fontsize=24)
# plt.xlabel('value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)
# plt.axis([0, 1100, 0, 1100000])
# plt.show()

# x_values = [1,2,3,4,5]
# y_values = [1,4,2,6,5]
# plt.scatter(x_values, y_values, c=[1,5,3,4,5], cmap=plt.cm.Blues, s=100)
# plt.title('square numbers', fontsize=24)
# plt.xlabel('value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)
# # plt.savefig("3.png", bbox_inches='tight')
# plt.show()


# x_values = list(range(0, 1001))
# y_values = [x ** 2 for x in x_values]
# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=40)
# plt.title('square numbers', fontsize=24)
# plt.xlabel('value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)
# plt.show()

from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        return choice([1, -1]) * choice([0, 1, 2, 3, 4])

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)


while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    plt.figure(figsize=(20, 6))
    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues, s=4)
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input('make another walk?(y/n)')
    if keep_running == 'n':
        break
