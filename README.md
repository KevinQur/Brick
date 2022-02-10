# Brick
A simple game developed with pygame
�@���������y���C���C�ϥΪ̥H�ƹ�����e�������@�ӥu�४�k����y��A�d�I�ä����@�өΦh�Ӭ���y�A���y�h�����e���W���@���ѿj���ƦC�Ӧ����j��C�j����������Y�����A�ño����ơC���ǯS��j��(�����I�аO)�Q�V��������A�|�����B�~�����Q�y�A�[�t�V�j�����t�סC�۹�]�ϹC����[�c����E�C
![�D�e��](https://static.coderbridge.com/img/kevin-qur/fadbba3050d045868f0a505e278cbfd2.png)
�y�����y�������A�i�H�ǥѧֳt���ʲy��t�סA���ܲy�t���������q�A�s�y�������y���ĪG�C�p���i�H����y�^�u����V�A���϶��������𪺬Y�B�C���y�i�J��W��U���Ŷ��A�ۦ�b�ӪŶ��u���A�۰ʺV�j��C

�p�G�ϥΪ̥����d�I�U�Y���y�A�ɭP�y�b�U��ɥX�ɡA�ηl�������y�A�M��b�e�������o�X�U�@���y�~��C���F���Q�y���~�A�C���@�@��3���y�i�ϥΡC

�C���}�l����A���]�w�o�y�������t��(1~10)�C�t�׶V�֡A�N���u�ɶ��V���j��A�۹�N���E�A�x���ק󰪡C�t�~�A�]�i�]�w�j�𪺦�C��(�̤j20X10)
![���j���C�� Youtube demo](https://youtu.be/ewWZ2fAHadQ)  https://youtu.be/ewWZ2fAHadQ

![�C���]�w](https://static.coderbridge.com/img/kevin-qur/492031e5e86549ae97685a46caee0c4b.png)

---
## �@. �{���o�Q

�C�����D��"�y"�b2D�����W���ʡA�������Ϋ������t�פ��q(speed_x, speed_y)�A�ƹ�W�N�O�C���e����s�ɡA�y�b�����Ϋ�����V�첾�h�ֹ����C��y�J����ɩάO�y��B�j��ɡA�o�ͤϼu�A�N�O�N��t�פ��q�ϦV(���H-1)�C�J�쥪�k��ɮɡAspeed_x�ϦV�C�J��W��ɡB�j��B�άO�y��ɡAspeed_y�ϦV�C�������~�A�J��j��ɡA�N�I�쪺�j�������A���Ʋ֥[�C�J��y��ɡA���Fspeed_y�ϦV���~�A�t�H�y�窺�t�ץ[�Jspeed_x�A���ͤ��y�ĪG�C
���F�F��W�z�ت��A�����˵�pygame���Ѩ��Ǫ���Υ\��A�i�H���ڭ̹F���W�z���޿�B�@�C

### `pygame.Rect`
�b�C���e���B�z���򥻤����O���Φ��x�Τp���ӶK�ϡB���ʡB�ƻs�B�άO�z�A(�I��)�ˬd�C`Rect`���ѯx�ΰ򥻹B��C�P�仡��O�Ӫ���A�ˤ��p�����u�O�ӯ©�x�Υ��W�����I�y�ФΪ��e�Ȫ�structure�ӱo���C��Ыئp�U:

`Rect(left, top, width, height) -> Rect`

### `pygame.sprite`
sprite����½Ķ��"���F"�A�U�W��q�N�O�C�����]�Ӷ]�h�����a�B�Ǫ��B�_�����C�b�o��name space���U�w�q�F`Sprite`��`Group`�o�G�ӥN������O�C�ƹ�Wpygame�]�S���ѫܦh��誺�\��A�\�h�a�賣�u�O��H�禡�A�ϥΪ̦ۤv�������g�ӳ�����{�{���X�C�o�ǩ�H���O�u�O�Ӥ����w�q�A���~�Ӥ��l�����O�A�i�H�Τ@�M�Φܨ�L�\�����O���@�ʼҦ��C�Ҧp`Sprite`����`update()`��k�A�b�C���D�j����C�@���ҥH�s�դ覡�I�s���C�s�դ����Ҧ�`sprite`�����Ұ���U�۪�`update()`�i���ݩ�ۤv����s���C`Sprite`�|��`image`��`rect`�o�G���ݩʡA����e���K�Ϫ��x�ι϶��ίx�έ��I/���e�j�p��T�C�M�ӳo�G�ӭ��n�ݩʫo���j��w�q��쫬`Sprite`���A�n�ϥΪ̦ۤv�O�o�b�Ыؤl���[�J�A�_�h�\�h�a��(�Ҧp�I���ˬd)�|�X�䤣��rect�ݩʪ�exception�C�o�I�N�������OOP��h�C
`Group`�o�����O�O�@�Ӧs��h��sprites��`list`�e���A��K��e�������Ҧ������������@�ʡC�Ҧp`Group.update()`�I�s�C�@�Ӧ���sprite��`update()`�C`Group.clear()`�N�C�@�Ӧ����Ҧ��ڵe����rect�ϰ�A�Hbackground��P�A�A����`Group.draw()`�H�C�Ӧ���sprite��image�K�^�Ҧbrect�x�ΰϰ�C�������~
`pygame.sprite.spritecollide(sprite, group)->Sprite_list`
�HGroup���޼Ʊa�J�A�ˬd�Ĥ@�Ӥ޼�(sprite)����Group�����Ǧ����I��(rect�����|��)�A�^�Ǧ��o�͸I���쪺sprites����list�C
�t�~�|��`DirtySprite`�h�F`Dirty`�аO�A�����sprite���ܰʡA�u�w��ʰ��泡����s�C`LayeredUpdate`��`OrderedUpdate`�ɤJ�ϼh���Ƿ����A�����sprites����ø�A���Ǧb�W�h��sprites��ø�A�����e�������|���p���i������s�C�o�̨S�Ψ�A�N���c���γƸ��C
### `pygame.mouse`
���o�γ]�w�ƹ�������T�A�o�̥u�Ψ�`get_pos()->(x,y)`���o�ثe�ƹ���Цb�e���W���y�СC`get_rel()->(x,y)`���o�W���I�s�o�Ө禡�ܳo���I�s�o�禡�A�o�����ƹ���Цb�e���W���ʶq(�y�Юt��)
### `pygame.mixer`
���J�����ɤμ���C`Sound(filename) -> Sound`���J�����ɡC�Ȥ䴩���ɦW .ogg �� .wav�������ɡC`play(loops=0) -> Channel`�}�l����Aloops�����񭫽Ʀ��ơC�Y�]-1�h�L�����ƴ`���A����`Sound.stop()`�C���񬰭I������A�{�����|�d�b�o�浥�������~����U�@��A�ӬO"�g�ᤣ�z"�������U�@���~�����C�]���i�H�h�n�D(channel)����A�]���Y�n���������񤣦P���ġA�n���N�W�@��`Sound.stop()`�A�Aplay()�U�@�ӡC�Y�{���i�����ӧִ������A�y�����ĨӤ��μ����A�i�H�bplay()����[�J�@��`pygame.time.wait(delay_time)`�Ȱ��{������@�q�ɶ��A�����ļ�����A�~��C
### `pygame.time`
��T�x���{������ɶ��C`Clock.tick(framerate=0)`�T�O�e����s�v���|����]�w���C��ռơC�@��C������ɡA�O�b�@�ӵL�a�j�骺�C�@���j��s�e���@��(��)�C�p�P�q�v�����ı�ȯd����z�A�C���s30�էY�|���ʵe���ĪG�C`pygame.time.set_timer(event, millis)`�Ұʤ@��timer�A����w���g���ɶ��o�X�@��user event�C�Ω�ƥ�ɦV���{���g�k�C`pygame.time.wait(delay_time)`�Ȱ��{�����@�q�ɶ��C

��X�W�zpygame�Ҵ��Ѫ��\��A���C���{�����Φw�Ʀp�U�G
* �y(Ball)�B�y��(Racket)�B�j��(Brick)�A�o�T�̩w�q���~�Ӧ�`pygame.sprtie.Sprite`���l�����O�A�䤤�j���h�@�ӥ��L�ݩ�(bonus_ball)�A���a�����Q�y���S��j���C
* �j��(Wall)�w�q���~�Ӧ�`pygame.sprite.Group`���l�����O�C�ЫخɡA�H���hfor�j��Ыئ�C�ƦC���j���A�[�Jwall�s�աC
* �y(Ball)���O�㦳�����t�פΤ����t�פ��q(speed_x, speed_y)�ݩʡA����ƫ��O(����)�C��`update()`�禡����`rect.move_ip(speed_x, speed_y)`�N�y�첾�ܷs�СC
* �y��(Racket)���O�b`update()`�禡����ɧQ��`py.mouse.get_pos()[0]`���o�ƹ��ثex�b�y�СA�Ψөw��y��rect���y�СC�t�������t��(speed_racket)����ƫ��O�ݩʡA�Q��`py.mouse.get_rel()[0]`���o�W���I�s�o�Ө禡�ܳo���I�s�o�禡�A�o�����ƹ���Цb�e���W���ʶq(�u��x�b)�@��������t�סC
* �ˬd�y���S���I����y��A��`py.sprite.collide_rect(ball, racket) -> bool`�C�ˬd�y���S���V����@�ӿj���A��`py.sprite.spritecollideany(aBall, wall) -> brick`
* �b���W���ʪ��y(���`�o�X���y�κV��S��j����o�����Q�y)�Ҧ��ǩ�balls�s��(`pygame.sprite.Group`)�C�y�X�ɤοj���Q�V��A�H`ball.kill()`��`brick.kill()`�q�s�դ������C

## �G. �{���[�c
��W�t�@���ɮ�(spriteObject.py)�w�qSprite��Group����
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
        for i in range(dimI):              # ���hfor�j��A�Ыؿj���[�Jwall�s�աA�æ�C�y�Цw��
            for j in range(dimJ):
                brick = Brick(x+40*i, y+20*j)
                self.add(brick)
```

�{���D�y�{�p�U:
1. �}��`tkinter`�����A���ϥΪ̦ۤv�]�w�y�t�οj���C�ơC
2. ���J�����ɵ��귽
3. �Ыؿù��I���e��
4. �ЫحӪ���θs�աC
5. ��l�ƥ����ܼơC
6. �i�J�L�a�j��A������y�P���/�y��/�j�𤧸I���ˬd�A��s���W�Ҧ�sprites�A��s�e���C

```
import ....

window = tk.Tk() # tkinter�}���]�w�C�������{��
....
music_stage1 = py.mixer.Sound("./music/stage1.wav") #�����ɸ��J
.....
W,H=800,900    #�e���ؤo
screen = py.display.set_mode([W, H]) #�Ыؿù��e��
#�Ыغ��F����
racket=spriteObject.Racket()
ball=spriteObject.Ball(300,300,speedY)
balls = py.sprite.Group(ball)
wall = spriteObject.Wall(wall_X,wall_Y,20,100)
......... #��l�ƥ����ܼ�

while not GG:              #�C���}�l�i��A�e�������s���L�a�j��
    screen.blit(background,(0,0)) #���N�e��������P
    allSprites.update()           #����Ҧ�sprites��update() 
    for aBall in balls:           #�]���W�i��P�ɷ|���@�ӥH�W���y�A
        if aBall�I�쥪�Υk���:     #��for �j��@�ӭӲy�̦��B�z
            speed_x = speed_x * (-1) #�����t�פϦV
        if aBall�I��W���:
            speed_y = speed_y * (-1) #�����t�פϦV
        if aBall�W�X�U���:
            aBall.kill()
            if �٦��l�y: �A�o�@���y
            else: GG=True
        if aBall����y��:
            speed_y = speed_y * (-1) #�����t�פϦV
            speed_x = speed_x + speed_racket #���y�ĪG
        if aBall����Ybrick:
            ���� += 1
            speed_y = speed_y * (-1) #�����t�פϦV
            brick.kill()
            if brick�����Q�y: ������Q�D����W
    allSprites.draw(screen) #�Ҧ�sprites���s�K��
    �O���O��r��s
    py.display.flip()    #�e��½�s
    clock.tick(40)       #�P�B�ɶ��A�ϱo�C��40�յe�� 
```