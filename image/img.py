import random

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


# while True:
#     rw = RandomWalk(5000)
#     rw.fill_walk()
#     plt.figure(figsize=(20, 6))
#     point_number = list(range(rw.num_points))
#     plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues, s=4)
#     plt.scatter(0, 0, c='green', s=100)
#     plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
#
#     # 隐藏坐标轴
#     plt.axes().get_xaxis().set_visible(False)
#     plt.axes().get_yaxis().set_visible(False)
#     plt.show()
#     keep_running = input('make another walk?(y/n)')
#     if keep_running == 'n':
#         break


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# fig = plt.figure(figsize=(12, 9))
# ax = fig.gca(projection='3d')
# x = np.arange(-4, 4, 0.25)
# y = np.arange(-4, 4, 0.25)
# X, Y = np.meshgrid(x, y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
#
# surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
#
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# fig.colorbar(surf, shrink=0.6, aspect=6)
# plt.show()
import scipy as sp


def multiplyPoly():
    cubic1 = sp.poly1d([3, 4, 5, 5])
    cubic2 = sp.poly1d([4, 1, -3, 3])
    print(cubic1)
    print(cubic2)
    print('-' * 36)
    print(cubic1 * cubic2)


# multiplyPoly()

def sparseDisplay(nonzero, squaresize, ax=None):
    ax = ax if ax is not None else plt.gca()
    ax.patch.set_facecolor('black')
    for row in range(0, squaresize):
        for col in range(0, squaresize):
            if (row, col) in nonzero.keys():
                el = nonzero[(row, col)]
                if el == 0:
                    color = 'black'
                else:
                    color = '#008000'
                rect = plt.Rectangle([col, row], 1, 1, facecolor=color, edgecolor=color)
                ax.add_patch(rect)
    ax.autoscale_view()
    ax.invert_yaxis()


# if __name__ == '__main__':
#     nonzero = {
#         (0, 4): 2, (0, 7): 10, (1, 1): 4, (1, 3): 3, (1, 8): 1,
#         (2, 0): 6, (0, 9): 2, (2, 2): 1, (2, 5): 7, (3, 9): 1, (5, 0): 3,
#         (5, 2): 2, (5, 8): 3, (6, 3): 2, (6, 6): 1, (7, 8): 1, (8, 0): 3,
#         (8, 2): 2, (8, 9): 1, (9, 1): 3
#     }
#     plt.figure(figsize=(4, 4))
#     sparseDisplay(nonzero, 10)
#     plt.show()

fig = plt.figure(figsize=(15, 10), facecolor='w')


def plotCircle(x, y, radius, color, alphaval):
    circle = plt.Circle((x, y), radius=radius, fc=color, alpha=alphaval)
    fig.gca().add_patch(circle)
    nofcircle = plt.Circle((x, y), radius=radius, ec=color, fill=False)
    fig.gca().add_patch(nofcircle)


# x = [55, 83, 90, 13, 55, 82, 96, 55, 69, 19, 55, 95, 62, 96, 82, 30, 22, 39, 54, 50, 69, 56, 58, 55, 55, 47, 55, 20,
#      86, 78, 56]
# y = [5, 3, 4, 0, 1, 0, 1, 3, 5, 2, 2, 0, 2, 4, 6, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 3, 0, 0, 1, 0]
# r = [23, 17, 15, 13, 13, 12, 12, 11, 11, 10, 10, 10, 10, 10, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6]
# for i in range(0, len(x)):
#     plotCircle(x[i], y[i], r[i], 'b', 0.1)
#
# plt.axis('scaled')
# plt.show()


# principle_value = 10000
# grossReturn = 1.06
# return_amt = []
# x = []
# y = [10000]
# year = 2010
# return_amt.append(principle_value)
# x.append(year)
# for i in range(1, 15):
#     return_amt.append(return_amt[i-1] * grossReturn)
#     print("Year-", i, "Returned:", return_amt[i])
#     year += 1
#     x.append(year)
#     y.append(833.33*(year-2010)+ principle_value)
# plt.grid()
# plt.plot(x, return_amt, color='r')
# plt.plot(x, y, color='b')
# plt.show()


# from decimal import Decimal
#
# colors = [(31, 119, 180), (174, 199, 232), (255, 128, 0), (255, 15, 14),
#           (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 173, 61),
#           (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
#           (227, 119, 194), (247, 182, 210), (127, 127, 127),
#           (199, 199, 199), (188, 189, 34), (219, 219, 141),
#           (23, 190, 207), (158, 218, 229)]
# for i in range(len(colors)):
#     r, g, b = colors[i]
#     colors[i] = (r / 255., g / 255., b / 255.)
#
#
# def printHeaders(term, extra):
#     print('\nExtra-Payment: $' + str(extra) + " Term:" + str(term) + " years")
#     print("--------------------------------------------------------------------")
#     print("Pmt no".rjust(6), ' ', 'Beg. bal.'.ljust(13), ' ')
#     print("Payment".ljust(9), ' ', 'Principal'.ljust(9), ' ')
#     print("Interest".ljust(9), ' ', 'End. bal.'.ljust(13))
#     print(''.rjust(6, '-'), ' ', ''.ljust(13, '-'), ' ')
#     print(''.rjust(9, '-'), ' ', ''.ljust(9, '-'), ' ')
#     print(''.rjust(9, '-'), ' ', ''.ljust(13, '-'), ' ')
#
#
# def amortization_table(principal, rate, term, extrapyment, printData=False):
#     xarr = []
#     begarr = []
#     original_loan = principal
#     money_saved = 0
#     total_payment = 0
#     payment = float(pmt(principal, rate, term))
#     begBal = principal
#
#     num = 1
#     endBal = 1
#     if printData == True:
#         printHeaders(term, extrapyment)
#     while (num < term + 1) and (endBal > 0):
#         interest = round(begBal * (rate / (12 * 100.0)), 2)
#         applied = extrapyment + round(payment - interest, 2)
#         endBal = round(begBal - applied, 2)
#         if (num - 1) % 12 == 0 or (endBal < applied + extrapyment):
#             begarr.append(begBal)
#             xarr.append(num / 12)
#             if printData == True:
#                 print('{0:3d}'.format(num).center(6), ' ', )
#                 print('{0:,.2f}'.format(begBal).rjust(13), ' ', )
#                 print('{0:,.2f}'.format(payment).rjust(9), ' ', )
#                 print('{0:,.2f}'.format(applied).rjust(9), ' ', )
#                 print('{0:,.2f}'.format(interest).rjust(9), ' ', )
#                 print('{0:,.2f}'.format(endBal).rjust(9), ' ', )
#         total_payment += applied + extrapyment
#         num += 1
#         begBal = endBal
#     if extrapyment > 0:
#         money_saved = abs(original_loan - total_payment)
#         print('\n Total Payment:', '{0:,.2f}'.format(total_payment).rjust(13))
#         print('\n Money Saved:', '{0:,.2f}'.format(money_saved).rjust(13))
#     return xarr, begarr, '{0:,.2f}'.format(money_saved)
#
#
# def pmt(principal, rate, term):
#     ratePerTwelve = rate / (12 * 100.0)
#     result = principal * (ratePerTwelve / (1 - (1 + ratePerTwelve) ** (-term)))
#     result = Decimal(result)
#     result = round(result, 2)
#     return result
#
#
# plt.figure(figsize=(18, 14))
# i = 0
# markers = ['o', 's', 'D', '^', 'v', '*', 'p', 's', 'D', 'o', 's', 'D', '^', 'v', '*', 'p', 's', 'D']
# markersize = [8, 8, 8, 12, 8, 8, 8, 12, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
#
# for extra in range(100, 1700, 100):
#     xv, bv, saved = amortization_table(450000, 5, 360, extra, False)
#     if extra == 0:
#         plt.plot(xv, bv, color=colors[i], lw=2.2, label='Principal only', marker=markers[i], markersize=markersize[i])
#     else:
#         plt.plot(xv, bv, color=colors[i], lw=2.2, label='Principal plus\$' + str("/month, Saved:\$") + saved,
#                  marker=markers[i], markersize=markersize[i])
#     i += 1
# plt.grid(True)
# plt.xlabel('Years', fontsize=18)
# plt.ylabel('Mortgage Balance', fontsize=18)
# plt.title('Mortgage Loan For $350,000 with Additional Payment Chart', fontsize=20)
# plt.legend()
# plt.show()


# yvals1 = [101000, 111000, 121000, 131000, 138000, 143000, 148000, 153000, 158000]
# yvals2 = [130000, 142000, 155000, 160000, 170000, 180000, 190000, 194000, 200000]
# yvals3 = [125000, 139000, 157000, 171000, 183000, 194000, 205000, 212000, 220000]
# xvals = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]
#
# bubble1 = []
# bubble2 = []
# bubble3 = []
#
# for i in range(0, 9):
#     bubble1.append(yvals1[i] / 20)
#     bubble2.append(yvals2[i] / 20)
#     bubble3.append(yvals3[i] / 20)
#
# fig, ax = plt.subplots(figsize=(10, 12))
# plt1 = ax.scatter(xvals, yvals1, c='#d82730', s=bubble1, alpha=0.5)
# plt2 = ax.scatter(xvals, yvals2, c='#2077b4', s=bubble2, alpha=0.5)
# plt3 = ax.scatter(xvals, yvals3, c='#ff8010', s=bubble3, alpha=0.5)
#
# ax.set_xlabel('Extra Dollar Amount', fontsize=16)
# ax.set_ylabel('Savings', fontsize=16)
# ax.set_title('Mortgage Savings (Paying Extra Every Month)', fontsize=20)
#
# ax.set_xlim(400, 1450)
# ax.set_ylim(90000, 230000)
#
# ax.grid(True)
# ax.legend((plt1, plt2, plt3), ('$250,000 Loan', '$350,000 Loan', '$450,000 Loan'), scatterpoints=1, loc="upper left",
#           markerscale=0.17, fontsize=10, ncol=1)
# fig.tight_layout()
# plt.show()