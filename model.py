"""
This model is built following Lengnick(2013) paper on
Journal of Economic Behavior & Organization 86 (2013) 102– 120.
"""

from agents import Firm, Household
from mesa import Model
from mesa.datacollection import DataCollector
from mesa.time import RandomActivation
import numpy as np
import random

# Data collector functions


# Return number of agents
def get_num_agents(model):
    agents = [a for a in model.schedule.agents]
    return len(agents)


# Sum of all agent savings
def get_total_savings(model):
    agent_savings = [a for a in model.schedule.agents]


# Model class
class MacroModel(Model):

    # Default parameters as of pg. 110
    def __init__(
        self,
        seed = 1,
        H = 1000,
        F = 100,
        num_typeA = 7,

        delta = 0.019,
        phi_max = 1,
        phi_min = 0.25,

        theta = 0.02,
        Phi_max = 1.15,
        Phi_min = 1.025,

        alpha = 0.9,

        Psi_price = 0.25,
        Psi_quant = 0.25,

        xi = 0.01,

        beta = 50,
        pi = 0.1,

        n = 7,
        gamma = 24,
        lambda_ = 3,

        Theta = 0.75
    ):
        self.H = H
        self.F = F
        self.schedule = RandomActivation(self)
        self.datacollector = DataCollector(
            model_reporters={
                "Number of agents": get_num_agents,
                "Total savings": get_total_savings
            },
            agent_reporters={}
        )
        # Initialise random number generator. The same seed produces the same random number sequence
        np.random.seed(seed)
        HH_list = [Household]

        # Create household agents for the model according to number set by user
        for i in range(self.H):
            # Set reservation wage, liquidity and consumption
            w = np.random.normal(loc=1, scale=0.2)
            m = np.random.normal(loc=1, scale=0.2)
            c = np.random.randint(low=21, high=105)

            h = Household(i, self, w, m, c, num_typeA, alpha)
            self.schedule.add(h)
            HH_list.append(h)

        FI_list = [Firm]

        # Create firm agents for the model according to number set by user
        for i in range(self.F):
            # Set offered wage, inventory value and price level
            w = np.random.normal(loc=1, scale=0.2)
            inv = np.random.randint(low=0, high=10)
            p = np.random.normal(loc=0.1, scale= 0.2)

            f = Firm(i + H , self, w, 0, inv * 0.9, inv * 1.1, p, p * 0.9, p * 1.1,
                     delta, Phi_min, Phi_max, phi_min, phi_max, theta,
                     lambda_, gamma, Theta)
            self.schedule.add(f)
            FI_list.append(f)


MacroModel()
