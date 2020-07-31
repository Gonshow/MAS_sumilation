# MAS_simulation
世の中はジレンマに溢れている。そこで実社会のモデル化を目的として、
MASを使った遭遇型ジレンマゲームのシミュレーションを作った。
N体のエージェントにone-shotジレンマゲームのルールと
速度、xy位置情報を持たせ、２次元グリッド上を移動させた。
互いの距離√0.02以下の場合に遭遇したとみなしジレンマゲームを開始する。
結果を学習し、これを続けていく。

There  so many diremmas around us.
To model real world, I simulated encounted type diremma game using Multi Agent System.
The number of agents is 100.
They have one-shot diremma game's rule, speed, theta and location of (x,y).
Agents walking in two dimensional space of grid play diremma game 
when they approach the other agent within the distance that under √0.02.
After game, they learned result and start walking.

