# Brick
A simple game developed with pygame
一個類似壁球的遊戲。使用者以滑鼠控制畫面底部一個只能左右橫移的球拍，攔截並反擊一個或多個紅色球，讓球去撞擊畫面上部一堵由磚塊排列而成的磚牆。磚塊受撞擊後即消失，並得到分數。有些特殊磚塊(有紅點標記)被敲擊消失後，會釋放額外的紅利球，加速敲磚塊的速度。相對也使遊戲更加繁忙刺激。
![主畫面](https://static.coderbridge.com/img/kevin-qur/fadbba3050d045868f0a505e278cbfd2.png)
球拍擊球的瞬間，可以藉由快速移動球拍速度，改變球速的水平分量，製造類似切球之效果。如此可以控制球回彈之方向，企圖集中打穿牆的某處。讓球進入牆上方狹窄空間，自行在該空間彈跳，自動敲磚牆。

如果使用者未能攔截下墜的球，導致球在下邊界出界，及損失該顆球，然後在畫面中央發出下一顆球繼續。除了紅利球之外，遊戲一共有3顆球可使用。

遊戲開始之初，先設定發球的垂直速度(1~10)。速度越快，就能更短時間敲完磚牆，相對就更刺激，困難度更高。另外，也可設定磚牆的行列數(最大20X10)
![打磚塊遊戲 Youtube demo](https://youtu.be/ewWZ2fAHadQ)  https://youtu.be/ewWZ2fAHadQ

![遊戲設定](https://static.coderbridge.com/img/kevin-qur/492031e5e86549ae97685a46caee0c4b.png)

---
## 一. 程式發想

遊戲的主角"球"在2D平面上移動，有水平及垂直之速度分量(speed_x, speed_y)，事實上就是每次畫面更新時，球在水平及垂直方向位移多少像素。當球遇到邊界或是球拍、磚牆時，發生反彈，就是將其速度分量反向(乘以-1)。遇到左右邊界時，speed_x反向。遇到上邊界、磚牆、或是球拍時，speed_y反向。除此之外，遇到磚牆時，將碰到的磚塊消失，分數累加。遇到球拍時，除了speed_y反向之外，另以球拍的速度加入speed_x，產生切球效果。
為了達到上述目的，首先檢視pygame提供那些物件及功能，可以幫我們達成上述之邏輯運作。

### `pygame.Rect`
在遊戲畫面處理的基本元素是切割成矩形小塊來貼圖、移動、複製、或是干涉(碰撞)檢查。`Rect`提供矩形基本運算。與其說其是個物件，倒不如說它只是個純放矩形左上角原點座標及長寬值的structure來得恰當。其創建如下:

`Rect(left, top, width, height) -> Rect`

### `pygame.sprite`
sprite中文翻譯為"精靈"，顧名思義就是遊戲中跑來跑去的玩家、怪物、寶物等。在這個name space底下定義了`Sprite`及`Group`這二個代表性類別。事實上pygame也沒提供很多實質的功能，許多地方都只是抽象函式，使用者自己必須撰寫該部分實現程式碼。這些抽象類別只是個介面定義，讓繼承之衍生類別，可以統一套用至其他功能類別之作動模式。例如`Sprite`有個`update()`方法，在遊戲主迴圈當中每一輪皆以群組方式呼叫之。群組中的所有`sprite`成員皆執行各自的`update()`進行屬於自己的更新項。`Sprite`尚有`image`及`rect`這二個屬性，為其畫面貼圖的矩形圖塊及矩形原點/長寬大小資訊。然而這二個重要屬性卻未強制定義於原型`Sprite`當中，要使用者自己記得在創建子當中加入，否則許多地方(例如碰撞檢查)會出找不到rect屬性的exception。這點就比較不符OOP原則。
`Group`這個類別是一個存放多個sprites的`list`容器，方便對容器內的所有成員集體執行作動。例如`Group.update()`呼叫每一個成員sprite的`update()`。`Group.clear()`將每一個成員所佔據畫面的rect區域，以background塗銷，再執行`Group.draw()`以每個成員sprite的image貼回所在rect矩形區域。除此之外
`pygame.sprite.spritecollide(sprite, group)->Sprite_list`
以Group為引數帶入，檢查第一個引數(sprite)有跟Group內那些成員碰撞(rect有重疊到)，回傳有發生碰撞到的sprites成員list。
另外尚有`DirtySprite`多了`Dirty`標記，控制那些sprite有變動，只針對性執行部分更新。`LayeredUpdate`及`OrderedUpdate`導入圖層順序概念，控制那些sprites先重繪，那些在上層的sprites後繪，滿足畫面有交疊情況之可受控更新。這裡沒用到，就族繁不及備載。
### `pygame.mouse`
取得或設定滑鼠相關資訊，這裡只用到`get_pos()->(x,y)`取得目前滑鼠游標在畫面上之座標。`get_rel()->(x,y)`取得上次呼叫這個函式至這次呼叫這函式，這期間滑鼠游標在畫面上移動量(座標差值)
### `pygame.mixer`
載入音效檔及播放。`Sound(filename) -> Sound`載入音效檔。僅支援副檔名 .ogg 及 .wav之音效檔。`play(loops=0) -> Channel`開始播放，loops為播放重複次數。若設-1則無限次數循環，直到`Sound.stop()`。播放為背景執行，程式不會卡在這行等它播完才執行下一行，而是"射後不理"直接跳下一行繼續執行。因為可以多聲道(channel)播放，因此若要換場景播放不同音效，要先將上一個`Sound.stop()`，再play()下一個。若程式可能執行太快換場景，造成音效來不及播完，可以在play()之後加入一行`pygame.time.wait(delay_time)`暫停程式執行一段時間，等音效播完後再繼續。
### `pygame.time`
精確掌控程式執行時間。`Clock.tick(framerate=0)`確保畫面更新率不會高於設定之每秒禎數。一般遊戲執行時，是在一個無窮迴圈的每一輪迴更新畫面一次(禎)。如同電影播放視覺暫留之原理，每秒更新30禎即會有動畫之效果。`pygame.time.set_timer(event, millis)`啟動一個timer，於指定的週期時間發出一個user event。用於事件導向之程式寫法。`pygame.time.wait(delay_time)`暫停程式執一段時間。

綜合上述pygame所提供的功能，本遊戲程式雛形安排如下：
* 球(Ball)、球拍(Racket)、磚塊(Brick)，這三者定義成繼承自`pygame.sprtie.Sprite`之衍生類別，其中磚塊多一個布林屬性(bonus_ball)，為帶有紅利球的特殊磚塊。
* 磚牆(Wall)定義為繼承自`pygame.sprite.Group`之衍生類別。創建時，以雙層for迴圈創建行列排列之磚塊，加入wall群組。
* 球(Ball)類別具有垂直速度及水平速度分量(speed_x, speed_y)屬性，為整數型別(像素)。其`update()`函式執行`rect.move_ip(speed_x, speed_y)`將球位移至新標。
* 球拍(Racket)類別在`update()`函式執行時利用`py.mouse.get_pos()[0]`取得滑鼠目前x軸座標，用來定位球拍rect之座標。另有水平速度(speed_racket)之整數型別屬性，利用`py.mouse.get_rel()[0]`取得上次呼叫這個函式至這次呼叫這函式，這期間滑鼠游標在畫面上移動量(只取x軸)作為其水平速度。
* 檢查球有沒有碰撞到球拍，用`py.sprite.collide_rect(ball, racket) -> bool`。檢查球有沒有敲到哪一個磚塊，用`py.sprite.spritecollideany(aBall, wall) -> brick`
* 在場上活動的球(正常發出的球及敲到特殊磚塊獲得的紅利球)皆收納於balls群組(`pygame.sprite.Group`)。球出界及磚塊被敲到，以`ball.kill()`及`brick.kill()`從群組中移除。

## 二. 程式架構
單獨另一個檔案(spriteObject.py)定義Sprite及Group物件
```
class Racket(py.sprite.Sprite):
    def __init__(self):
        self.image=...
        self.rect=self.image.get_rect()
    def update(self):
        ....

class Ball(py.sprite.Sprite):
    def __init__(self,x,y,speedY):
        .....
    def update(self):
        .....

class Brick(py.sprite.Sprite):
    def __init__(self,x,y):
        .....

class Wall(py.sprite.Group):
    def __init__(self,dimI,dimJ,x,y):
        .....
        for i in range(dimI):              # 雙層for迴圈，創建磚塊加入wall群組，並行列座標安排
            for j in range(dimJ):
                brick = Brick(x+40*i, y+20*j)
                self.add(brick)
```

程式主流程如下:
1. 開啟`tkinter`視窗，讓使用者自己設定球速及磚牆行列數。
2. 載入音樂檔等資源
3. 創建螢幕背景畫面
4. 創建個物件及群組。
5. 初始化全域變數。
6. 進入無窮迴圈，持續執球與邊界/球拍/磚牆之碰撞檢查，更新場上所有sprites，更新畫面。

```
import ....

window = tk.Tk() # tkinter開窗設定遊戲難易程度
....
music_stage1 = py.mixer.Sound("./music/stage1.wav") #音樂檔載入
.....
W,H=800,900    #畫面尺寸
screen = py.display.set_mode([W, H]) #創建螢幕畫面
#創建精靈元件
racket=spriteObject.Racket()
ball=spriteObject.Ball(300,300,speedY)
balls = py.sprite.Group(ball)
wall = spriteObject.Wall(wall_X,wall_Y,20,100)
......... #初始化全域變數

while not GG:              #遊戲開始進行，畫面持續更新之無窮迴圈
    screen.blit(background,(0,0)) #先將畫面全部塗銷
    allSprites.update()           #執行所有sprites之update() 
    for aBall in balls:           #因場上可能同時會有一個以上的球，
        if aBall碰到左或右邊界:     #用for 迴圈一個個球依次處理
            speed_x = speed_x * (-1) #水平速度反向
        if aBall碰到上邊界:
            speed_y = speed_y * (-1) #垂直速度反向
        if aBall超出下邊界:
            aBall.kill()
            if 還有餘球: 再發一顆球
            else: GG=True
        if aBall撞到球拍:
            speed_y = speed_y * (-1) #垂直速度反向
            speed_x = speed_x + speed_racket #切球效果
        if aBall撞到某brick:
            分數 += 1
            speed_y = speed_y * (-1) #垂直速度反向
            brick.kill()
            if brick有紅利球: 釋放紅利求於場上
    allSprites.draw(screen) #所有sprites重新貼圖
    記分板文字更新
    py.display.flip()    #畫面翻新
    clock.tick(40)       #同步時間，使得每秒40禎畫面 
```