import pyxel #Pyxelライブラリ呼び出し


pyxel.init(120,120) #120X120ピクセルの領域を初期化(init = initialization)

pyxel.cls(14) #()内の数字の色で初期化

pyxel.text(20,20, "Hello,world!",7) #20X20の位置から、7番目の色(白)で文字を表示

pyxel.line(0,30,120,30,5) #(x1,y1地点からx2,y2地点までを5番目の色(青))で線を引く

pyxel.show() #画面を表示。ESCが押されるまで待機する