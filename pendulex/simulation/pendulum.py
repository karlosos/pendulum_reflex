import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


class Pendulum:
    def __init__(self):
        self.st = 0  # Start time (s)
        self.et = 100  # End time (s)
        self.ts = 0.005  # Time step (s)
        self.g = 9.81  # Acceleration due to gravity (m/s^2)
        self.L = 2  # Length of pendulum (m)
        self.b = 0  # Damping factor (kg/s)
        self.m = 1  # Mass of bob (kg)

        self.t = None
        self.simulation_steps = None
        self.theta1 = None
        self.theta2 = None
        self.x = None
        self.y = None

    def sim_pen_eq(self, t, theta):
        """
        1st order equations to solve in a function
        :param t:
        :param theta: theta1 is angular displacement at current time instant, theta2 is angular velocity at current time instant
        :return:
        dtheta2_dt is angular acceleration at current time instant
        dtheta1_dt is rate of change of angular displacement at current time instant i.e. same as theta2
        """
        dtheta2_dt = (-self.b / self.m) * theta[1] + (-self.g / self.L) * np.sin(theta[0])
        dtheta1_dt = theta[1]
        return [dtheta1_dt, dtheta2_dt]

    def simulate(self):
        theta1_ini = 0  # Initial angular displacement (rad)
        theta2_ini = 3  # Initial angular velocity (rad/s)
        theta_ini = [theta1_ini, theta2_ini]
        t_span = [self.st, self.et + self.ts]
        self.t = np.arange(self.st, self.et + self.ts, self.ts)
        sim_points = len(self.t)
        self.simulation_steps = np.arange(0, sim_points, 1)

        theta12 = solve_ivp(self.sim_pen_eq, t_span, theta_ini, t_eval=self.t)
        self.theta1 = theta12.y[0, :]
        self.theta2 = theta12.y[1, :]

        # Simulation
        self.x = self.L * np.sin(self.theta1)
        self.y = -self.L * np.cos(self.theta1)
        return self.x, self.y, self.simulation_steps

    def graph(self):
        plt.plot(self.t, self.theta1, label='Angular Displacement (rad)')
        plt.plot(self.t, self.theta2, label='Angular velocity (rad/s)')
        plt.xlabel('Time(s)')
        plt.ylabel('Angular Disp.(rad) and Angular Vel.(rad/s)')
        plt.legend()
        plt.show()


if __name__ == '__main__':
    p = Pendulum()
    p.simulate()
    p.graph()
