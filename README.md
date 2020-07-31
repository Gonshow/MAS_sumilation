# MAS_simulation
>python walk_sample.py

世の中はジレンマに溢れている。そこで実社会のモデル化を目的として、
MASを使った遭遇型ジレンマゲームのシミュレーションを作った。
N体のエージェントにone-shotジレンマゲームのルールと
速度、xy位置情報を持たせ、２次元グリッド上を移動させた。
互いの距離√0.02以下の場合に遭遇したとみなしジレンマゲームを開始する。
結果を学習し、これを続けていく。

There are so many diremmas around us.
To model real world, I simulated encounted type diremma game using Multi Agent System.
The number of agents is 100.
They have one-shot diremma game's rule, speed, theta and location of (x,y).
Agents walking in two dimensional space of grid play diremma game 
when they approach the other agent within the distance that under √0.02.
After game, they learned result and start walking.

![Sample](https://user-images.githubusercontent.com/38319910/89000732-12c64d00-d333-11ea-9232-e46aca3746c5.gif)
<img width="635" alt="スクリーンショット 2020-07-31 13 45 29" src="https://user-images.githubusercontent.com/38319910/89001156-4d7cb500-d334-11ea-85a5-e83597bd0f21.png">


結果、みんな非協力戦略になった。そりゃそう。

In result all agents became to have uncooperative strategy. There is no doubt.

そこで、エージェントに内的報酬を実装し、環境や他者から得る報酬だけでなく自分自身で行動価値を高めるようにしてみた。
つまり、協力戦略をとった場合に協力戦略の行動価値にプラスの重み付けをしてみた。
いいことをしていい気分になる。そんな感じ。

Then I added intrinsic rewards rule to agent that they improve their action value themselves.
If a agent selects cooperative strategy, the agent's  value of cooperative strategy is increaced.
Good action and good feeling. Like that.

![ex_smp3](https://user-images.githubusercontent.com/38319910/89001968-d137a100-d336-11ea-8ea8-e62bb02ffe4a.gif)
<img width="230" alt="スクリーンショット 2020-07-31 14 06 41" src="https://user-images.githubusercontent.com/38319910/89002059-18259680-d337-11ea-8722-641ade6ea324.png">

協力戦略エージェントと非協力戦略エージェントが永遠に共存するようになった!
しかし一定数に収束してしまっているので、実社会のモデル化までの道のりは長い。

Agents who have cooperative strategy coeternal with uncooperative agents!
But the number became constant. I might tried to simulate far away world.
