import random as r


class IctMi:

    def __init__(self,n):
        self.sum_valuei = r.stagelevel(40, 30)
        self.no_indicator = r.num_ind(0, 0)
        self.total = self.sum_valuei + self.no_indicator
        self.total /= 4
        self.n = n

    def application(self):
        self.sum_valuea = r.stagelevela(0, 4)
        self.no_indicatora = r.num_inda(0, 0)
        self.totala = self.sum_valuea + self.no_indicatora
        self.totala /= 4


    def human_resc(self):
        self.sum_valueh = r.stagelevelh(t, u)
        self.no_indicatorh = r.num_indh(0,indicatorh)
        self.totalh = self.sum_valueh + self.no_indicatorh
        self.totalh /= 4

    def policy(self):
        self.sum_valuep = r.stagelevelp(v, w)
        self.no_indicatorp = r.num_inda(0,indicatorp)
        self.totalp = self.sum_valuep + self.no_indicatorp
        self.totalp /= 4


