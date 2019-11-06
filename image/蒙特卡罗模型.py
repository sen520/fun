# import numpy as np
# from math import log
#
# import matplotlib.pyplot as plt
#
# x = []
# y = []
#
#
# def generateProfit(d):
#     global s
#     if d >= s:
#         return 0.6 * s
#     else:
#         return 0.6 * d - 0.4 * (s - d)
#
#
# maxprofit = 0
# for s in range(20, 305):
#     for i in range(1, 1000):
#         d = np.random.randint(10, high=200)
#         profit = generateProfit(d)
#         if profit > maxprofit:
#             maxprofit = profit
#     x.append(s)
#     y.append(log(maxprofit))
# plt.plot(x, y)
# print(maxprofit)
# plt.show()


# import numpy as np
# numstudents = 30
# numTrials = 10000
# numWithSameBday = 0
# for trial in range(numTrials):
#     year = [0] * 365
#
#     for i in range(numstudents):
#         newBDay = np.random.randint(365)
#         year[newBDay] = year[newBDay] + 1
#     haveSameBday = False
#     for num in year:
#         if num > 1:
#             haveSameBday = True
#     if haveSameBday == True:
#         numWithSameBday = numWithSameBday + 1
#
#
# prob = float(numWithSameBday) / float(numTrials)
# print('The probablity of a shared birthday in a class of', numstudents, ' is ', prob)


import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 14))
names = ['Lebron James', 'Kyrie Irving', 'Steph Curry', 'Kyle Krover', 'Dirk Nowitzki']
threePercents = [35.4, 46.8, 44.3, 49.2, 38.0]
twoPercents = [53.6, 49.1, 52.8, 47.0, 48.6]
colind = 0


def attemptThree():
    if np.random.randint(0, high=100) < threePtPercent:
        if np.random.randint(0, high=100) < overtimePercent:
            return True
        return False


def attemptTwo():
    havePossesion = True
    pointsDown = 3

    timeLeft = 30
    while (timeLeft > 0):
        if (havePossesion):
            if (pointsDown >= 3):
                timeLeft -= timeToShoot2
            else:
                timeLeft = 0
            if (np.random.randint(0, high=100) < twoPtPercent):
                pointsDown -= 2
                havePossesion = False
        else:
            if (np.random.randint(0, high=100) >= offenseReboundPercent):
                havePossesion = False
            else:
                if (pointsDown > 0):
                    timeLeft -= timeToFoul
                    if (np.random.randint(0, high=100) < oppFtPercent):
                        pointsDown += 1
                    if (np.random.randint(0, high=100) < oppFtPercent):
                        pointsDown += 1
                        havePossesion = True
                else:
                    if (np.random.randint(0, high=100) >= ftReboundPercent):
                        havePossesion = True
                    else:
                        if (np.random.randint(0, high=100) < oppTwoPtPercent):
                            pointsDown += 2
                        timeLeft = 0
    if (pointsDown > 0):
        return False
    else:
        if (pointsDown < 0):
            return True
        else:
            if (np.random.randint(0, high=100) < overtimePercent):
                return True
            else:
                return False


colors = [
    (31, 119, 180), (174, 199, 232), (255, 127, 14),
    (155, 187, 120), (44, 160, 44), (214, 39, 40), (148, 103, 189),
    (152, 223, 138), (255, 152, 150), (197, 176, 213), (140, 86, 75),
    (196, 156, 148), (227, 119, 194), (247, 182, 210), (127, 127, 127),
    (199, 199, 199), (188, 189, 34), (219, 219, 141), (23, 190, 207),
    (158, 218, 229), (217, 217, 217)
]
for i in range(len(colors)):
    r, g, b = colors[i]
    colors[i] = (r / 255., g / 255., b / 255.)

for i in range(5):
    x = []
    y1 = []
    y2 = []
    trials = 400
    threePtPercent = threePercents[i]
    twoPtPercent = twoPercents[i]
    oppTwoPtPercent = 40
    oppFtPercent = 70
    timeToShoot2 = 5
    timeToFoul = 5
    offenseReboundPercent = 25
    ftReboundPercent = 15
    overtimePercent = 50

    winsTakingThree = 0
    lossTakingThree = 0
    winsTakingTwo = 0
    lossTakingTwo = 0
    curTrial = 1

    while curTrial < trials:
        if (attemptThree()):
            winsTakingThree += 1
        else:
            lossTakingThree += 1
            if attemptTwo() == True:
                winsTakingTwo += 1
            else:
                lossTakingTwo += 1
            x.append(curTrial)
            y1.append(winsTakingThree)
            y2.append(winsTakingTwo)
            curTrial += 1
    plt.plot(x, y1, color=colors[colind], label=names[i] + " Wins Taking Three Point", linewidth=2)
    plt.plot(x, y2, color=colors[20], label=names[i] + " Wins Taking Two Point", linewidth=1.2)
    colind += 2
    legend = plt.legend(loc='upper left', shadow=True)
    for legobj in legend.legendHandles:
        legobj.set_linewidth(2.6)

plt.show()
