import matplotlib.pyplot as plt
import random as rnd
import numpy as np

"""これら値を変化させて内的報酬の減衰を変化させる"""
R_0=0.6
experience=0
damage=0
"""                                      """
class Agent:
    def __init__(self):
        #ジレンマゲーム用
        self.value_of_C = 0.0
        self.value_of_D = 0.0
        self.strategy = rnd.choice(["C","D"])
        self.next_strategy = self.strategy
        self.R_int = R_0
        #歩行シュミレーション用
        self.x=rnd.random() * 10#初期位置
        self.y=rnd.random() * 10#初期位置
        self.speed=0.1
        self.theta=2 * np.pi * rnd.random()
        self.battle=False
        self.color=np.random.randint(0, 255)

    def decide_next_strategy(self):
        """Pairwise-Fermiモデルで次のゲームでの戦略を決定する"""

        if rnd.random() < 1/(1 + np.exp((self.value_of_C - self.value_of_D)/0.1)):
            self.next_strategy = "D"
        else:
            self.next_strategy = "C"
    def update_strategy(self):
        #内的動機づけの消失による減衰
        if self.strategy=="D" and self.next_strategy=="C":
            self.R_int=R_0
        elif self.strategy=="C" and self.next_strategy=="C":
            self.R_int-=experience
        self.strategy = self.next_strategy

    def count_payoff(self, enemy, Dg=0.5, Dr=0.5):
        """利得表に基づいてエージェントが獲得する利得を計算"""

        R = 0.1       # Reward
        S = -Dr     # Sucker
        T = 0.1+Dg    # Temptation
        P = 0       # Punishment
        #R_int=0.6　　#＜＜内部報酬＞＞

        #self.point = 0.0
        if self.strategy == "C" and enemy.strategy == "C":
            self.value_of_C += R + self.R_int
        elif self.strategy == "C" and enemy.strategy == "D":
            self.value_of_C += S + self.R_int
            self.R_int-=damage
        elif self.strategy == "D" and enemy.strategy == "C":
            self.value_of_D += T
        elif enemy.strategy == "D" and enemy.strategy == "D":
            self.value_of_D += P
