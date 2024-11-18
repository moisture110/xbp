import pyxel #Pyxelライブラリ呼び出し


pyxel.init(120,120) #120X120ピクセルの領域を初期化(init = initialization)

pyxel.cls(0) #()内の数字の色で初期化

pyxel.text(10,85,"Player",7) #文字を表示

pyxel.text(20,100,"Oh! Slime is Here!!",7) #文字を表示

pyxel.rectb(5,80,110,35,7) #文字枠

pyxel.tri(60,16,66,25,54,25,7) #スライムの頭の部分

pyxel.elli(40,25,40,30,7) #スライムの本体部分

pyxel.circb(52,35,3,0) #スライムの右目

pyxel.circb(68,35,3,0) #スライムの左目

pyxel.rect(55,45,11,2,0) #スライムの口

pyxel.show()