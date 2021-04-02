from mesa import Agent

class Firm(Agent):
    def __init__(self, id, model, w, m, inv, inv_min, inv_max, d,
                 p, p_min, p_max, delta, Phi_min, Phi_max, phi_min,
                 phi_max, theta, Theta, mc, openPosition, toFire,
                 gamma, lambda_, num_months_with_openpositions,
                 typeB, typeA, m_buffer, dailyProduces):
        # initialise the parent class with required parameters
        super().__init__(id, model)
    # following eq(13-14) in main paper
    def produce(self):
        self.dailyProduces = self.lambda_ * self.getTypeB().size()
        self.inv += self.lambda_ * self.getTypeB().size()

