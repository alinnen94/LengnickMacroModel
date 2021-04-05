from mesa import Agent
import random
import math


# Firm class
class Firm(Agent):
    def __init__(self, id, model, w, inv, inv_min, inv_max, p,
                 p_min, p_max, delta, Phi_min, Phi_max,
                 phi_min, phi_max, theta, lambda_, gamma, Theta):

        # initialise the parent class with required parameters
        super().__init__(id, model)

    # following eq(13-14) in main paper
    def produce(self):
        self.dailyProduces = self.lambda_ * self.getTypeB().size()
        self.inv += self.lambda_ * self.getTypeB().size()

    # following eq(5) in main paper
    def newWage(self):
        self.w = self.w * (1) # + getRnd().getDblFromTo(-self.delta, self.delta)

    # following eq(6) and (7) in main paper
    def updateInvRange(self):
        self.inv_max =  self.Phi_max * self.d
        self.inv_min = self.Phi_min * self.d

    # def updateDemandForLabour(self):
    #     if(self.openPosition > 0):
    #       self.num_months_with_openpositions = b + 1
    #     else:
    #           self.w * = 0.9 # the firm filled all open positions, therefore it reduces the wage
    #     if(self.num_months_with_openpositions == self.gamma):
    #        self.w * = 1.1 # the firm had openpositions for gamma months, therefore it reduces the wage by 10%

    # following eq(8) and (9) in main paper
    def updatePriceRange(self):
        self.p_max = self.phi_max * self.mc
        self.p_min = self.phi_min * self.mc

    def increasePrice(self):
        self.p = self.p # * (1 + Sim.getRnd().getDblFromTo(0, self.theta)
        print("increase price: " + self.p)

    def decreasePrice(self):
        self.p = self.p # (1 - Sim.getRnd().getDblFromTo(0, self.theta)
        print("decrease price: " + self.p)


# Househoid class
class Household(Agent):
    def __init__(self, id, model, w, m, c, num_typeA, alpha):

        # initialise the parent class with required parameters
        super().__init__(id, model)

    def updateConsumption(self):
        self.c = 1 # math.min(self.m / self.P) * Math.exp(self.alpha), self.m / self.P

