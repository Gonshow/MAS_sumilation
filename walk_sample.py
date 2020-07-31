import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random as rnd
from agent import Agent

def play_game(player1,player2):
    player1.count_payoff(player2)
    player2.count_payoff(player1)
    player1.decide_next_strategy()
    player2.decide_next_strategy()
def simulation(agents):
    #結果格納用
    C_num=[]
    D_num=[]
    #図を用意
    fig, ax = plt.subplots()
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.title("simulation")
    #plt.gca().set_aspect('equal', adjustable='box')
    plt.tick_params(labelbottom=False,
                   labelleft=False,
                   labelright=False,
                   labeltop=False,
                   bottom=False,
                   left=False,
                   right=False,
                   top=False)
    graph_list = [] #各時刻でのグラフを全て格納する場所を用意する
    maxcount=0
    flag=True
    while flag==True:
        maxcount+=1
        x_lim_C=[]
        y_lim_C=[]
        x_lim_D=[]
        y_lim_D=[]
        for agent in agents:
            agent.x += agent.speed * np.cos(agent.theta)
            agent.y += agent.speed * np.sin(agent.theta)
            if agent.x>9.9 or agent.x<0.1:
                agent.theta = np.pi - agent.theta
            if agent.y>9.9 or agent.y<0.1:
                agent.theta = -agent.theta
            #遭遇判定
            for agent_enemy in agents:
                if agent.battle!=True and agent!=agent_enemy and np.abs(agent.x-agent_enemy.x)<0.1 and np.abs(agent.y-agent_enemy.y)<0.1:
                    play_game(agent,agent_enemy)
                    agent.update_strategy()
                    agent_enemy.update_strategy()
                    agent.theta = 2 * np.pi * np.random.rand()  #遭遇後向き変える
                    agent_enemy.theta = 2 * np.pi * np.random.rand()
                    agent.battle=True              #バトル中をTrueにする
                    agent_enemy.battle=True
            #持ってる戦略でグループ分け
            if agent.strategy=="C":
                x_lim_C.append(agent.x)
                y_lim_C.append(agent.y)
            else:
                x_lim_D.append(agent.x)
                y_lim_D.append(agent.y)
        color_border=len(x_lim_C)
        C_num_num = len(x_lim_C)#グラフ2描画用に値をもらう
        color_list=["red"]*color_border
        x_lim_C.extend(x_lim_D)
        y_lim_C.extend(y_lim_D)
        color_list.extend(["blue"]*(len(x_lim_C)-color_border+1))
        graph = ax.scatter(x_lim_C, y_lim_C, color=color_list, marker=".")
        graph_list.append([graph])     #上記のグラフをgraph_listへ格納する
        #グラフ2描画ように値を記録
        C_num.append(C_num_num)
        D_num.append(len(x_lim_C)-C_num_num)
        #完全に淘汰されたら終了
        count=0
        for agent in agents:
            agent.battle=False
            if agent.strategy=="C":
                count+=1


        if count==0 or count==len(x_lim_C):
            flag=False
        elif maxcount==1000:
            flag=False
    ani = animation.ArtistAnimation(fig, graph_list, interval=10) #graph_list内のグラフを連続的に繋げて表示するアニメーションにする
    ani.save("ex_smp_last1.gif", writer = 'imagemagick')
    print(maxcount)
    plt.show()
    plt.close()
    fig = plt.subplots()
    plt.title("result")
    plt.xlim(0, 1000)
    plt.ylim(0, 100)
    t=range(0,maxcount)
    plt.plot(t, C_num, color="red", marker = 'o')
    plt.plot(t, D_num, color="blue", marker = 'x')
    plt.show()
    #fig.savefig("last_img.png")#pngに出力
agents = [Agent() for id in range(100)]
simulation(agents)
