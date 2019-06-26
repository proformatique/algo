from matplotlib import pyplot as plt
def f(x):
    return x ** 2

lesx = range(-20, 20)
lesy = [f(x) for x in lesx]

plt.plot(lesx, lesy)
plt.show()
