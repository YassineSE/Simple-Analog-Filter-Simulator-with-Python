import matplotlib.pyplot as plt
import first_order_filters as filter_1
import second_order_filters as filter_2

sys1 = filter_1.LP(10, 100)
print(sys1.get_params())
sys1.plot_step()
plt.figure()
sys1.plot_bode()

sys2 = filter_1.HP(10, 100)
print(sys2.get_params())
plt.figure()
sys2.plot_step()
plt.figure()
sys2.plot_bode()

sys3 = filter_2.LP(10, 0.1, 100)
print(sys3.get_params())
plt.figure()
sys3.plot_step()
plt.figure()
sys3.plot_bode()

sys4 = filter_2.HP(10, 0.5, 100)
print(sys4.get_params())
plt.figure()
sys4.plot_step()
plt.figure()
sys4.plot_bode()

plt.show()