import pygame as py
import tkinter as tk
import random, time
import spriteObject

window = tk.Tk()
window.title('game setting')
window.geometry('300x200')
label1 = tk.Label(window, text='set ball vertical velocity (1~10)')
label1.pack()
entry1 = tk.Entry(window)
entry1.insert(0,'5')
entry1.pack()
label2 = tk.Label(window, text='set wall bricks dimention (max. 20X10)')
label2.pack()
entry2 = tk.Entry(window)
entry2.insert(0,'20')
entry2.pack()
entry3 = tk.Entry(window)
entry3.insert(0,'3')
entry3.pack()
speedY=5
def button_click():
    global speedY, wall_X, wall_Y
    speedY = int(entry1.get())
    wall_X = int(entry2.get())
    wall_Y = int(entry3.get())
    window.destroy()
button = tk.Button(window, text='start', command=button_click)
button.pack()
window.mainloop()

py.init()
py.mixer.init()
music_stage1 = py.mixer.Sound("./music/stage1.wav") #玩遊戲時之背景音樂
music_stage2 = py.mixer.Sound("./music/stage2.wav") #額外球釋放時之背景音樂
music_GG1 = py.mixer.Sound("./music/gg1.wav")       #球出界時之音樂
music_GG2 = py.mixer.Sound("./music/gg2.wav")       #game over 之音樂
music_hit = py.mixer.Sound("./music/collide.wav")   #碰撞時之音效
W,H=800,700    #畫面尺寸
screen = py.display.set_mode([W, H])
window_rect=py.Rect(0,0,W,H)
background=py.Surface(screen.get_size())
background=background.convert()
background.fill((0,0,0))
screen.blit(background,(0,0))

#創建精靈元件
racket=spriteObject.Racket()
ball=spriteObject.Ball(300,300,speedY)
balls = py.sprite.Group(ball)
wall = spriteObject.Wall(wall_X,wall_Y,20,100)
sprites = random.sample(wall.sprites(),3)
br=py.image.load('./image/brick2.png')
for aBrick in random.sample(wall.sprites(),3):
    aBrick.bonus_ball = True
    aBrick.image = br
allSprites = py.sprite.Group([racket, ball])
allSprites.add(wall.sprites())

#全域變數初始化
font = py.font.Font(None, 40)
font_size=(10,10) 
last_pos=(10,H-100)
GG = False        # game over
num_balls = 2     # 剩餘球數
score = 0         # 打了幾個磚塊數
clock = py.time.Clock()
start_ticks=py.time.get_ticks()  #紀錄遊戲開始時刻

music_stage1.play(loops=-1)   #遊戲開始，背景音樂循環撥放

while not GG:
  for event in py.event.get():
    if event.type == py.QUIT:
      GG = True
  
  #allSprites.clear(screen, background)
  screen.blit(background,(0,0))
  allSprites.update()
  for aBall in balls:
      (x,y)=aBall.rect.center
      if x < 10 or x > W - 10:
          #碰到左側或右側邊緣，則X軸速度反向
          music_hit.play()
          aBall.speed_x = aBall.speed_x * (-1)
      elif y < 10:
          #碰到頂部邊緣，則Y軸速度反向
          music_hit.play()
          aBall.speed_y = aBall.speed_y * (-1)
      elif y > H:
          #球拍沒攔截到，球出界
          aBall.kill()
          if len(balls) == 0:
              #場上沒球了
              music_stage1.stop()
              music_stage2.stop()
              if num_balls > 0:
                  #還有餘球可以發
                  music_GG1.play()
                  py.time.wait(4000)
                  num_balls -=1
                  newBall=spriteObject.Ball(300,300,speedY)
                  balls = py.sprite.Group(newBall)
                  allSprites.add(newBall)
                  music_stage1.play(loops=-1)
              else:
                  music_GG2.play()
                  py.time.wait(5000)
                  GG=True
      elif py.sprite.collide_rect(racket, aBall):
          #碰到球拍，則Y軸速度反向，X軸速度加上球拍速度(切球效果)
          aBall.speed_y = aBall.speed_y * (-1)
          aBall.speed_x = aBall.speed_x + racket.speed_racket
          music_hit.play()
      else:
          # 檢查有沒有敲到磚塊
          brick = py.sprite.spritecollideany(aBall, wall)
          if brick is not None:
              #敲到磚塊時，分數增加，球垂直速度反彈
              music_hit.play()
              aBall.speed_y = aBall.speed_y * (-1)
              score +=1
              brick.kill()
              if brick.bonus_ball:
              #if hasattr(brick, 'bonus_ball'):
                  #敲到有紅點的磚塊，釋放額外的紅利球於塊所在處。背景音樂進入stage2
                  (x,y)=brick.rect.center
                  bonusBall = spriteObject.Ball(x,y,10)
                  balls.add(bonusBall)
                  allSprites.add(bonusBall)
                  music_stage1.stop()
                  music_stage2.play(loops=-1)

  allSprites.draw(screen)
  
  #計算累計之秒數並顯示剩餘球數及已賺得之分數
  seconds=round((py.time.get_ticks()-start_ticks)/1000)
  text = 'Balls : '+str(num_balls)+'    Time : '+str(seconds)+' S'+'    Score : '+str(score)
  txt = font.render(text, True, (255,255,255))
  font_size = font.size(text)
  screen.blit(txt, (10, 10))
            
  py.display.flip()
  clock.tick(40)


 #最後記得關閉 pygame
py.mixer.quit()
py.quit()