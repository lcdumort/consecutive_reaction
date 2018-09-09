#created by Dumortier Loic

"""
This program represents a consecutive first-order reaction of the form A => B => C.
A => B is considered reaction 1, and B => C reaction 2.
Although an error will occur when k1 is equal to k2, the plots will still be correct.
Program based on: https://matplotlib.org/devdocs/gallery/widgets/slider_demo.html#sphx-glr-gallery-widgets-slider-demo-py
(official slider_demo/documentation of matplotlib)

Use the slide-bars to change the k-values
"""

#importing packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider



fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

#X-axis
x = np.arange(0.0, 5.0, 0.001)

#starting Values
k10,k20= 1,2
c_begin0 = float(10)

#formulas (See Physical Chemistry: consecutive reactions)
conca = c_begin0*np.exp(-k10*x)
concb = c_begin0*(k10 /(k20 - k10))*(np.exp(-k10*x)-np.exp(-k20*x))
concc = c_begin0*(1 + (1/(k20-k10))*(k10 *np.exp(-k20 *x) - k20*np.exp(-k10 *x)))

#assigning the formulas to a plot
l, = plt.plot(x, conca, color='red')
z, = plt.plot(x, concb, color='blue')
q, = plt.plot(x, concc, color='green')
plt.axis([0, 5, 0, c_begin0])
plt.ylabel('concentration(mol/l)')
plt.xlabel('time(s)')

#add legend
ax.legend([l,z,q], ["conc_a", "conc_b", "conc_c"])

#sliders
axk1 = plt.axes([0.1, 0.10, 0.8, 0.03])
axk2 = plt.axes([0.1, 0.05, 0.8, 0.03])
axc_begin = plt.axes([0.1,0.15,0.8,0.03])
sk1 = Slider(axk1, 'k1', 0.1, 5.0, valinit=k10)
sk2 = Slider(axk2, 'k2', 0.1, 5.0, valinit=k20)
sc_begin = Slider(axc_begin , 'conc_begin', 0.1, c_begin0+5, valinit = c_begin0)

#update the graph when user changes sliders, note that when k1 == k2, an error will occur.
def update(val):
    k1 = sk1.val
    k2 = sk2.val
    c_begin = sc_begin.val
    #AssertionError when k1 == k2 => won't plot next value when k1 will be equal to k2.
    assert (k1 != k2), "k1 can't be equal to k2!"
    l.set_ydata(c_begin*np.exp(-k1*x))
    z.set_ydata(c_begin*(k1 /(k2 - k1))*(np.exp(-k1*x)-np.exp(-k2*x)))
    q.set_ydata(c_begin*(1 + (1/(k2-k1))*(k1 *np.exp(-k2 *x) - k2*np.exp(-k1 *x))))
    fig.canvas.draw_idle()

#use function(update) to make plot interactive
sk1.on_changed(update)
sk2.on_changed(update)
sc_begin.on_changed(update)
plt.show()


