import sys
import pygame
import random
import math
from pygame.locals import *
#色(顏色)
#region
WHITE  = (255, 255, 255)
BLACK  = (49,49,49)
LIME   = (  0, 255,   0)
YELLOW = (255, 255,   0)
ORANGE = (255, 192,   0)
RED    = (255,   0,   0)
PINK   = (255, 128, 255)
VIOLET = (255,   0, 224)
GREEN = (  0, 255,   0)
SILVER= (192, 208, 224)
CYAN  = (  0, 224, 255)
#endregion

#画像データとサンドデータ(圖像和音源資料)
#region
title =[
    pygame.image.load("img\logo.png"),
    pygame.image.load("img\lily-k.png"),
    pygame.image.load("img\lily-h.png")
    ]
kao = [
    pygame.image.load("img\kao0.png"),
    pygame.image.load("img\kao1.png"),
    pygame.image.load("img\kao2.png"),
    pygame.image.load("img\kao3.png"),
    pygame.image.load("img\kao4.png")
]
#モード1
img_bg = [
    pygame.image.load("img/bit0.png"),
    pygame.image.load("img/bit1.png"),
    pygame.image.load("img/bit2.png"),
    pygame.image.load("img/bit3.png"),
    pygame.image.load("img/bit4.png"),
    pygame.image.load("img/bit5.png"),
    pygame.image.load("img/bit6.png"),
    pygame.image.load("img/port0.png"),
    pygame.image.load("img/port1.png"),
    pygame.image.load("img/port2.png"),
    pygame.image.load("img/shadow0.png"),
    pygame.image.load("img/shadow1.png"),
    pygame.image.load("img/shadow3.png"),
    pygame.image.load("img/bit7.png"),
]
img_lily = [
    pygame.image.load("img/lily0.png"),
    pygame.image.load("img/lily1.png"),
    pygame.image.load("img/lily2.png"),
    pygame.image.load("img/lily3.png"),
    pygame.image.load("img/lily4.png"),
    pygame.image.load("img/lily5.png"),
    pygame.image.load("img/lily6.png"),
    pygame.image.load("img/lily7.png"),
    pygame.image.load("img/lily8.png"),
    pygame.image.load("img/lily9.png"),
    pygame.image.load("img/lily10.png"),
    pygame.image.load("img/lily11.png")
]
img_guardian = [
    pygame.image.load("img/guardian0.png"),
    pygame.image.load("img/guardian1.png"),
    pygame.image.load("img/guardian2.png")
]
se_port = None
img_sine = [ 
    pygame.image.load("img/sine0.png"),
    pygame.image.load("img/sine1.png"),
    pygame.image.load("img/sine2.png"),           
]
#モード2
img_effect = [
    pygame.image.load("img/effect0.png"),
    pygame.image.load("img/effect1.png"),
    pygame.image.load("img/effect2.png"),
    pygame.image.load("img/effect3.png")
]
img_missile = [
    pygame.image.load("img/missile.png")           
]
#モード3
img_bg_03 = [
    pygame.image.load("img\mode3_bg01.png"),
    pygame.image.load("img\mode3_bg02.png"),
    pygame.image.load("img\mode3_bg03.png")
]
img_sship = [
    pygame.image.load("img\ship1.png"),
    pygame.image.load("img\ship2.png"),
    pygame.image.load("img\ship3.png"),
    pygame.image.load("img\ex1.png"),
    pygame.image.load("img\ex2.png"),
    pygame.image.load("img\ex3.png")
]
img_weapon = pygame.image.load("img/bullet.png")
img_enemy = [
    pygame.image.load("img\enemy.png"),
    pygame.image.load("img\zako0.png"),
    pygame.image.load("img\zako1.png"),
    pygame.image.load("img/boss.png"),
    pygame.image.load("img/boss.png")
]
img_explode = [
    None,
    pygame.image.load("img\explosion1.png"),
    pygame.image.load("img\explosion2.png"),
    pygame.image.load("img\explosion3.png"),
    pygame.image.load("img\explosion4.png"),
    pygame.image.load("img\explosion5.png")
]
se_barrage = None
se_damage = None
se_explosion = None
se_shot = None
#endregion

#定数と変数の宣言(常數與變量的聲明)
#region
SCREEN_HIGHT = 720 # 画面のサイズ(畫面大小)
SCREEN_WEIGHT = 1280
img_BG = pygame.image.load("img\img_bg.png")
story = [                                                               # シナリオ用のリスト(劇情用列表)
    #[
    # [" テスト1 感情：普通　"],
    # ["  テスト2 感情：悲しい　"],
    # ["  テスト3 感情：嬉しい　"],
    #],
    [
     ["  フロラー:........"],
     ["  フロラー:........"],
     #["  フロラー:この先きっと危険なことがいっぱいある"],
     #["  フロラー:でも私と兄さん一緒なら絶対乗り越える"]
    ]
]

MAX = 30 # 開始画面のエフェクトの数(開始畫面特效總數)
rx = [0]*MAX
ry = [0]*MAX
rx1 = [0]*MAX
ry1 = [0]*MAX
    
black_out = False # フェードイン(切換場景用變量)

idx = 0 # インデックス
tmr = 0 # タイマー(計時器)

energy_lily = 0 # キャラクターのhpとen(角色的hp和en)
health_lily = 0
energy_karan = 0
health_karan = 0

damage = False

#モード１
DIR_UP = 0 # 向き(方向)
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3

port = 0 
I = 7
II = 8
III = 9

lily_x = 0
lily_y = 0
lily_d = 0
lily_a = 0

GUARDIAN_MAX = 7*20
guardian_x = 0
guardian_y = 0
guardian_d = 0
guardian_a = 0
guardian_sx = 0
guardian_sy = 0
guardian_sd = 0

guardian2_x = [0]*GUARDIAN_MAX
guardian2_y = [0]*GUARDIAN_MAX
guardian2_d = [0]*GUARDIAN_MAX
guardian2_a = [0]*GUARDIAN_MAX
guardian2_sx = [0]*GUARDIAN_MAX
guardian2_sy = [0]*GUARDIAN_MAX
guardian2_sd = [0]*GUARDIAN_MAX

map_data = [] # 迷路用のリスト(迷宮用列表)

stage = 1
offset_x = -20 #偏移量
offset_y = -5

#モード2
laps = 0
se_crash = None 
my_vehice = 0

 # 道路のカーブを作るもとになるデータ
DATA_LR = [0, 0, 1, 2,-1, -2, 1, 2,-2, 1,-2, 0, 0, 0, 0, -1, 1,-2,-3, 3,-3, 2,-1, 1, 3, 0, 0, 2, 0, 0, 0, 0, 0,-1, 1, 0, 0, 0, 0]
 # 道路の起伏をを作るもとになるデータ
DATA_UD = [0, 0, 1, 2,-1, 2, 1, 0,-2, 1,-2, 0, 0, 0, 0, 0,-1,-2,-3,-4,-3,-2,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-3, 3, 0, 0, 0, 0]
CLEN = len(DATA_LR)

BOARD = 120 # 道路を描く板の定数
CMAX = BOARD*CLEN # 道路の全長
curve = [0]*CMAX
updown = [0]*CMAX
object_left = [0]*CMAX
object_right = [0]*CMAX

CAR = 30
vehicle_f = [False]*CAR
vehicle_x = [0]*CAR
vehicle_t = [0]*CAR
vehicle_lr = [0]*CAR
vehicle_spd = [0]*CAR
PLCAR_Y = 20 # プレイヤーの狩り人の表示位置

BULLET_MAX = 5
bullet_no = 0
bullet_f = [False]*BULLET_MAX
bullet_xs = [0]*BULLET_MAX
bullet_y = [0]*BULLET_MAX
bullet_xe = [0]*BULLET_MAX
bullet_spd = [0]*BULLET_MAX

LAPS = 3

#モード3
bg_y1 = 0 # 
bg_y2 = 0
bg_y3 = 0

ss_x = 0
ss_y = 0
ss_d = 0
ss_muteki = 0
key_spc = 0
key_z = 0
Bossf = True

MISSILE_MAX = 200
msl_no = 0
msl_f = [False]*MISSILE_MAX
msl_x = [0]*MISSILE_MAX
msl_y = [0]*MISSILE_MAX
msl_a = [0]*MISSILE_MAX

ENEMY_MAX = 100
emy_no = 0
emy_f = [False]*ENEMY_MAX
emy_x = [0]*ENEMY_MAX
emy_y = [0]*ENEMY_MAX
emy_a = [0]*ENEMY_MAX
emy_type = [0]*ENEMY_MAX
emy_speed = [0]*ENEMY_MAX
emy_shield = [0]*ENEMY_MAX
emy_count = [0]*ENEMY_MAX

EMY_BULLET = 0
EMY_ZAKO = 1
EMY_BOSS = 5
LINE_T = -60
LINE_B = 530
LINE_L = -60
LINE_R = 1300

EFFECT_MAX = 20
eff_no = 0
eff_p = [0]*EFFECT_MAX
eff_x = [0]*EFFECT_MAX
eff_y = [0]*EFFECT_MAX

#endregion

#モード0関数の定義(模式0的函數定義)
#region
def story_draw_txt(scrn, txt, x, y, siz, col): # シナリオ文字
    fnt = pygame.font.Font(r"C:\Users\User\AppData\Local\Microsoft\Windows\Fonts\k8x12S.ttf", siz*2)
    x = x 
    y = y 
    sur = fnt.render(txt, True, col)
    scrn.blit(sur, [x, y])  
    
def draw_text(scrn, txt, x, y, siz, col): # ＊立体的な文字の表示
    fnt = pygame.font.Font(r"C:\Users\User\AppData\Local\Microsoft\Windows\Fonts\k8x12S.ttf", siz)
    cr = int(col[0]/2)
    cg = int(col[1]/2)
    cb = int(col[2]/2)
    sur = fnt.render(txt, True, (cr,cg,cb))
    x = x - sur.get_width()/2
    y = y - sur.get_height()/2
    scrn.blit(sur, [x+1, y+1])
    cr = col[0]+128
    if cr > 255: cr = 255
    cg = col[1]+128
    if cg > 255: cg = 255
    cb = col[2]+128
    if cb > 255: cb = 255
    sur = fnt.render(txt, True, (cr,cg,cb))
    scrn.blit(sur, [x-1, y-1])
    sur = fnt.render(txt, True, col)
    scrn.blit(sur, [x, y])

def save_data():
    pass

def load_data():
    pass
#endregion

#モード1関数の定義(模式1的函數定義)
#region
def set_stage(): # ステージのデータをセットする(設置關卡資料)
    global map_data, port, stage
    global guardian_sx, guardian_sy, guardian_sd
    
    if stage == 1: 
        
        map_data = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,2,2,2,2,2,0,2,2,2,2,2,3,0,2,2,2,2,2,0,III,0],
        [0,2,0,0,2,0,0,2,2,2,2,0,0,0,II,0,2,0,2,0,2,0],
        [0,2,0,2,2,2,0,0,I,0,2,0,2,2,2,0,2,2,2,2,2,0],
        [0,2,2,2,4,2,2,2,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
        [0,2,0,2,2,2,0,0,0,0,2,2,2,0,0,0,2,2,2,2,2,0],
        [0,2,0,0,2,0,0,2,2,2,2,0,2,2,3,0,2,0,2,0,2,0],
        [0,2,2,2,2,2,0,5,0,2,2,2,2,0,0,0,3,0,2,0,6,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ]
        guardian_sx = 90 + offset_x # 敵の配置(配置敵人)
        guardian_sy = 450 + offset_y
        guardian_sd = DIR_DOWN # 敵の向き(敵人的朝向)
        
        for i in range(GUARDIAN_MAX):
            guardian2_sd[i] = -1

    if stage == 2:
        
        map_data = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,0],
        [0,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],
        [0,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,0],
        [0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,0],
        [0,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,0],
        [0,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,0],
        [0,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,13,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ]
        
        guardian_sd = -1
        
        for i in range(0, 7): # 敵の配置(配置敵人)
            if i == 1 or i == 3:
                continue
            guardian2_sx[i] = 60*18 + 30 + offset_x
            guardian2_sy[i] = 90 + offset_y + 60*i
            guardian2_sd[i] = DIR_LEFT
        for i in range(7,25):
            if i%18 == 0 or i%18 == 1 or i%18 == 8:
                continue
            guardian2_sx[i] =  90 + offset_x + 60*(i%18)
            guardian2_sy[i] = 60*5 + offset_y
            guardian2_sd[i] = DIR_UP
            
    if stage == 3: # 略(與上面類似省略)
        
        map_data = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,2,0,2,0,2,2,2,0,2,2,2,0,2,2,2,0,2,2,0,2,0],
        [0,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,0],
        [0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],
        [0,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,0],
        [0,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,0],
        [0,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,0],
        [0,2,0,2,2,2,0,2,2,2,0,2,2,2,0,2,2,2,0,0,13,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ]
        
        guardian_sd = -1
        
        for i in range(0, 7):
            if i == 0 or i == 2 or i == 4 or i == 6:
                continue
            guardian2_sx[i] = 60*18 + 30 + offset_x
            guardian2_sy[i] = 90 + offset_y + 60*i
            guardian2_sd[i] = DIR_LEFT
        for i in range(8,25):
            if i%18 == 0 or i%18 == 1 or i%18 == 2 or i%18 == 8:
                continue
            guardian2_sx[i] =  90 + offset_x + 60*(i%18)
            guardian2_sy[i] = 60*5 + offset_y
            guardian2_sd[i] = DIR_UP

    if stage == 4:
        
        map_data = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,2,0,2,0,2,2,2,0,2,2,2,0,2,2,2,0,2,2,0,2,0],
        [0,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,0],
        [0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],
        [0,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,0],
        [0,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,0],
        [0,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,0],
        [0,2,0,2,2,2,0,2,2,2,0,2,2,2,0,2,2,2,0,0,13,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ]
        
        guardian_sd = -1
        
        for i in range(0, 7):
            if i == 0 or i == 2 or i == 4 or i == 6:
                guardian2_sd[i] = -1
            guardian2_sx[i] = 60*18 + 30 + offset_x
            guardian2_sy[i] = 90 + offset_y + 60*i
            guardian2_sd[i] = DIR_LEFT
        for i in range(7,25):
            if i%18 == 0 or i%18 == 1 or i%18 == 8:
                guardian2_sd[i] = -1
            guardian2_sx[i] =  90 + offset_x + 60*(i%18)
            guardian2_sy[i] = 60*5 + offset_y
            guardian2_sd[i] = DIR_UP

def set_chara_pos(): # キャラのスタート位置(設置角色和敵人的初始位子)
    global lily_x, lily_y, lily_d, lily_a
    global guardian_x, guardian_y, guardian_d, guardian_a
    
    lily_x = 90 + offset_x
    lily_y = 90 + offset_y
    lily_d = DIR_DOWN
    lily_a = 0
    
    guardian_x = guardian_sx 
    guardian_y = guardian_sy
    guardian_d = guardian_sd
    guardian_a = 0
    
    for i in range(GUARDIAN_MAX):
        guardian2_x[i] = guardian2_sx[i]
        guardian2_y[i] = guardian2_sy[i]
        guardian2_d[i] = guardian2_sd[i]
        guardian2_a[i] = 0

def draw_screen(scrn): # ゲーム画面を描く(繪製畫面)
    
    for y in range(9): # 地図を描く(繪製地圖)
        for x in range(22):
            scrn.blit(img_bg[map_data[y][x]], [x*60 + offset_x, y*60 + offset_y])
            
    scrn.blit(img_lily[lily_a], [lily_x-30, lily_y-30]) #キャラクターを描く(繪製角色和敵人)
    if stage < 2:
        if guardian_sd != -1:
            scrn.blit(img_guardian[guardian_a], [guardian_x-30, guardian_y-30])
    if stage > 1:
        for i in range(GUARDIAN_MAX):
            if guardian2_sd[i] != -1:
                g_a = guardian2_a[i]
                g_x = guardian2_x[i]
                g_y = guardian2_y[i]
                scrn.blit(img_guardian[g_a], [g_x-30, g_y-30])
    
    s_x = lily_x - 640
    s_y = lily_y - 300
    
    if stage == 1: # 影を描く(繪製影子)
        scrn.blit(img_bg[12], [s_x, s_y])
        if s_x >= 0:
            scrn.blit(img_bg[11], [s_x - 1280, s_y]) # 左
        if s_x >= 0 and s_y >= 0:
            scrn.blit(img_bg[11], [s_x - 1280, s_y - 600]) # 左下
        if s_y >= 0:
            scrn.blit(img_bg[11], [s_x, s_y - 600]) # 下
        if s_x >= 0 and s_y + 300 <= 600:
            scrn.blit(img_bg[11], [s_x - 1280, s_y + 600]) # 右下
        if s_y + 300 <= 600:
            scrn.blit(img_bg[11], [s_x , s_y + 600]) # 右
        if s_x + 640 <= 1280 and s_y + 300 <= 600:
            scrn.blit(img_bg[11], [s_x + 1280, s_y + 600]) # 右上 
        if s_x + 640 <= 1280:
            scrn.blit(img_bg[11], [s_x + 1280, s_y]) # 上
        if s_x + 640 <= 1280 and s_y >= 0:
            scrn.blit(img_bg[11], [s_x + 1280, s_y - 600]) # 左上
  
def check_wall(cx, cy, di, dot): # ＊各方向に壁があるか調べる(判斷是否有牆)
    chk = False
    if di == DIR_UP:
        mx = int((cx-30 - offset_x)/60) 
        my = int((cy-30-dot - offset_y)/60) 
        if map_data[my][mx] <= 1 or map_data[my][mx] > 6 and map_data[my][mx] < 10: # 左上
            chk = True
        mx = int((cx+29 - offset_x)/60)
        if map_data[my][mx] <= 1 or map_data[my][mx] > 6 and map_data[my][mx] < 10: # 右上
            chk = True
    if di == DIR_DOWN:
        mx = int((cx-30 - offset_x)/60)
        my = int((cy+29+dot - offset_y)/60)
        if map_data[my][mx] <= 1 or map_data[my][mx] > 6 and map_data[my][mx] < 10: # 左下
            chk = True
        mx = int((cx+29 - offset_x)/60)
        if map_data[my][mx] <= 1 or map_data[my][mx] > 6 and map_data[my][mx] < 10: # 右下
            chk = True
    if di == DIR_LEFT:
        mx = int((cx-30-dot - offset_x)/60)
        my = int((cy-30 - offset_y)/60)
        if map_data[my][mx] <= 1 or map_data[my][mx] > 6 and map_data[my][mx] < 10: # 左上
            chk = True
        my = int((cy+29 - offset_y)/60)
        if map_data[my][mx] <= 1 or map_data[my][mx] > 6 and map_data[my][mx] < 10: # 左下
            chk = True
    if di == DIR_RIGHT:
        mx = int((cx+29+dot - offset_x)/60)
        my = int((cy-30 - offset_y)/60)
        if map_data[my][mx] <= 1 or map_data[my][mx] > 6 and map_data[my][mx] < 10: # 右上
            chk = True
        my = int((cy+29 - offset_y)/60)
        if map_data[my][mx] <= 1 or map_data[my][mx] > 6 and map_data[my][mx] < 10: # 右下
            chk = True
    return chk

def move_lily(key): # リリーを動かす(移動角色)
    global port, lily_x, lily_y, lily_d, lily_a, stage, I, II, III # 移動(移動)
    if key[K_UP] == 1:
        lily_d = DIR_UP
        if check_wall(lily_x, lily_y, lily_d, 15) == False: 
            lily_y = lily_y - 15
    elif key[K_DOWN] == 1:
        lily_d = DIR_DOWN
        if check_wall(lily_x, lily_y, lily_d, 15) == False:
            lily_y = lily_y + 15
    elif key[K_LEFT] == 1:
        lily_d = DIR_LEFT
        if check_wall(lily_x, lily_y, lily_d, 15) == False:
            lily_x = lily_x - 15
    elif key[K_RIGHT] == 1:
        lily_d = DIR_RIGHT
        if check_wall(lily_x, lily_y, lily_d, 15) == False:
            lily_x = lily_x + 15
    
    mx = int((lily_x)/60) # キャラクターの座標をマップデータに換算(把角色在畫面上的位子換算成在地圖上的位子)
    my = int((lily_y)/60)
    
    if map_data[my][mx] == 4: # ポットがあるか調べる(判斷是否在接口上)
        stage = 2
        set_stage()
        set_chara_pos()
        se_port.play()
    if map_data[my][mx] == 5:
        stage = 3
        set_stage()
        set_chara_pos()
        se_port.play()
    if map_data[my][mx] == 5:
        stage = 4
        set_stage()
        set_chara_pos()
        se_port.play()
        
    if key[K_SPACE] == 1: # ハッキング(連接)
        if lily_a <= 10:
            lily_a += 1
    if key[K_SPACE] == 0 : 
        lily_a = 0
    if map_data[my][mx] == 13 and lily_a == 10:
        stage = 1
        I = 2
        set_stage()
        set_chara_pos()
        se_port.play()
    
def move_guardian(): # ＊敵を動かす(移動敵人)
    global m1_idx, tmr, guardian_x, guardian_y, guardian_d, guardian_a,guardian_sd
    speed = 10
    
    if guardian_sd == -1:
        return
    if guardian_x%60== 30 + offset_x  and guardian_y%60 == 30 + offset_y: # マスの中心にいる時ランダム向きを変更(在方格中央時依照隨機值改變位子)
        guardian_d = random.randint(0, 6)
        if guardian_d >= 4:
            if lily_y < guardian_y: # プレーヤーを追跡(追蹤玩家)
                guardian_d = DIR_UP
            if lily_y > guardian_y:
                guardian_d = DIR_DOWN
            if lily_x < guardian_x:
                guardian_d = DIR_LEFT
            if lily_x > guardian_x:
                guardian_d = DIR_RIGHT
                
    if guardian_d == DIR_UP: # 移動
        if check_wall(guardian_x, guardian_y, guardian_d, speed) == False:
            guardian_y = guardian_y - speed
    if guardian_d == DIR_DOWN:
        if check_wall(guardian_x, guardian_y, guardian_d, speed) == False:
            guardian_y = guardian_y + speed
    if guardian_d == DIR_LEFT:
        if check_wall(guardian_x, guardian_y, guardian_d, speed) == False:
            guardian_x = guardian_x - speed
    if guardian_d == DIR_RIGHT:
        if check_wall(guardian_x, guardian_y, guardian_d, speed) == False:
            guardian_x = guardian_x + speed
    guardian_a = tmr%3
    if abs(guardian_x-lily_x) <= 40 and abs(guardian_y-lily_y) <= 40:
        m1_idx = 2
        tmr = 0

def move_guardian2(g_no): # 敵2を動かす(移動敵人2)
    global m1_idx, tmr, guardian2_x, guardian2_y, guardian2_d, guardian2_a
    speed = 10
    
    if guardian2_sd[g_no] == -1:
        return
    if guardian2_d[g_no] == DIR_UP: # 壁があったら反対方向に移動(碰壁的話往反方向移動)
        if check_wall(guardian2_x[g_no], guardian2_y[g_no], guardian2_d[g_no], speed) == False:
            guardian2_y[g_no] = guardian2_y[g_no] - speed
        else:
            guardian2_d[g_no] = DIR_DOWN
    elif guardian2_d[g_no] == DIR_DOWN:
        if check_wall(guardian2_x[g_no], guardian2_y[g_no], guardian2_d[g_no], speed) == False:
            guardian2_y[g_no] = guardian2_y[g_no] + speed
        else:
            guardian2_d[g_no] = DIR_UP
    elif guardian2_d[g_no] == DIR_LEFT:
        if check_wall(guardian2_x[g_no], guardian2_y[g_no], guardian2_d[g_no], speed) == False:
            guardian2_x[g_no] = guardian2_x[g_no] - speed
        else:
            guardian2_d[g_no] = DIR_RIGHT
    elif guardian2_d[g_no] == DIR_RIGHT:
        if check_wall(guardian2_x[g_no], guardian2_y[g_no], guardian2_d[g_no], speed) == False:
            guardian2_x[g_no] = guardian2_x[g_no] + speed
        else:
            guardian2_d[g_no] = DIR_LEFT
    guardian2_a[g_no] = tmr%3
    if abs(guardian2_x[g_no]-lily_x) <= 40 and abs(guardian2_y[g_no]-lily_y) <= 40:
        m1_idx = 2
        tmr = 0
#endregion

#モード2関数の定義(模式2的函數定義)
#region
def make_course(): # ＊道路のデータを作る関数
    for i in range(CLEN):
        lr1 = DATA_LR[i] 
        lr2 = DATA_LR[(i+1)%CLEN]
        ud1 = DATA_UD[i]
        ud2 = DATA_UD[(i+1)%CLEN]
        for j in range(BOARD):
            pos = j+BOARD*i
            curve[pos] = lr1*(BOARD-j)/BOARD + lr2*j/BOARD # 道の曲がる向きを計算
            updown[pos] = ud1*(BOARD-j)/BOARD + ud2*j/BOARD # 道の起伏を計算

def draw_obj(bg, img, x, y, sc): # ＊オブジェクトを描く
    img_rz = pygame.transform.rotozoom(img, 0, sc)
    w = img_rz.get_width()
    h = img_rz.get_height()
    bg.blit(img_rz, [x-w/2, y-h])

def draw_shadow(bg, x, y, siz): # ＊影を描く
    shadow = pygame.Surface([siz, siz/4])
    shadow.fill(RED)
    shadow.set_colorkey(RED) # Surfaceの透過色を設定
    shadow.set_alpha(128) # Surfaceの透明度を設定
    pygame.draw.ellipse(shadow, BLACK, [0,0,siz,siz/4])
    bg.blit(shadow, [x-siz/2, y-siz/4])

def m2_init_vehicle(): # ＊狩り人の初期化
    for i in range(1, CAR):
        vehicle_f[i] = True
        vehicle_x[i] = random.randint(50, 750)
        vehicle_t[i] = random.randint(200, CMAX-200)
        vehicle_lr[i] = 0
        vehicle_spd[i] = random.randint(100, 200)
        
    vehicle_x[0] = 400
    vehicle_t[0] = 0
    vehicle_lr[0] = 0
    vehicle_spd[0] = 0

def m2_drive_vehicle(key): # プレイヤーの狩り人の操作、制御
    global m2_idx, tmr, laps, recbk
    if key[K_a] == 1:
        if vehicle_lr[0] > -3:
            vehicle_lr[0] -= 1
        vehicle_x[0] = vehicle_x[0] + (vehicle_lr[0]-3)*vehicle_spd[0]/100 - 5
    
    elif key[K_d] == 1:
        if vehicle_lr[0] < 3:
            vehicle_lr[0] += 1
        vehicle_x[0] = vehicle_x[0] + (vehicle_lr[0]+3)*vehicle_spd[0]/100 + 5
    else:
        vehicle_lr[0] = int(vehicle_lr[0]*0.9)

    if key[K_w] == 1: # アクセル
        vehicle_spd[0] += 10
    elif key[K_s] == 1: # ブレーキ
        vehicle_spd[0] -= 10
    else:
        vehicle_spd[0] -= 0.50

    if vehicle_spd[0] < 0: #スビートの値の範囲
        vehicle_spd[0] = 0 
    if vehicle_spd[0] > 400:
        vehicle_spd[0] = 400

    # 狩り人の速度と道の曲がりから横方向の座標を計算
    vehicle_x[0] -= vehicle_spd[0]*curve[int(vehicle_t[0]+PLCAR_Y)%CMAX]/50
    
    # 路肩に接触したら減速する
    if vehicle_x[0] < 0:
        vehicle_x[0] = 0
        vehicle_spd[0] *= 0.9
    if vehicle_x[0] > 800:
        vehicle_x[0] = 800
        vehicle_spd[0] *= 0.9

    # 狩り人の速度から道路上の位置を計算
    vehicle_t[0] = vehicle_t[0] + vehicle_spd[0]/100
    
    if vehicle_t[0] > CMAX-1:
        vehicle_t[0] -= CMAX
        laps += 1
        if laps == LAPS:
            m2_idx = 3
            tmr = 0

def m2_move_vehicle(cs): # COMカーの制御
    global health_karan, m2_idx
    for i in range(cs, CAR):
        if vehicle_spd[i] < 250:
            vehicle_spd[i] += 10
        if i == tmr%120:
            vehicle_lr[i] += random.choice([-1,0,1])
            if vehicle_lr[i] < -3: 
                vehicle_lr[i] = -3
            if vehicle_lr[i] > 3: 
                vehicle_lr[i] = 3
        vehicle_x[i] = vehicle_x[i] + vehicle_lr[i]*vehicle_spd[i]/100
        if vehicle_x[i] < 50:
            vehicle_x[i] = 50
            vehicle_lr[i] = int(vehicle_lr[i]*0.9)
        if vehicle_x[i] > 750:
            vehicle_x[i] = 750
            vehicle_lr[i] = int(vehicle_lr[i]*0.9)
            
        if vehicle_x[i] > vehicle_x[0]:
            vehicle_x[i] -= 5
        if vehicle_x[i] < vehicle_x[0]:
            vehicle_x[i] += 5
        vehicle_t[i] += vehicle_spd[i]/100
        if vehicle_t[i] > CMAX-1:
            vehicle_t[i] -= CMAX
            
        if m2_idx == 2 and vehicle_f[i]: # ヒットチェック
            cx = vehicle_x[i]-vehicle_x[0]
            cy = vehicle_t[i]-(vehicle_t[0]+PLCAR_Y)%CMAX
            if vehicle_f[i] == True:
                if -100 <= cx and cx <= 100 and -10 <= cy and cy <= 10:
                    # 衝突時の座標変化、速度の入れ替えと減速
                    vehicle_x[0] -= cx/4
                    vehicle_x[i] += cx/4
                    vehicle_spd[0], vehicle_spd[i] = vehicle_spd[i]*0.3, vehicle_spd[0]*0.3
                    if health_karan >= 1:
                        health_karan -= 1
                    elif  health_karan == 0:
                        m2_idx = 4
                    se_crash.play()

def set_bullet(x): # ミサイルを配置
    global bullet_no
    bullet_f[bullet_no] = True
    bullet_xs[bullet_no] = vehicle_x[0]
    bullet_xe[bullet_no] = x  - 240
    bullet_y[bullet_no] = vehicle_t[0] + PLCAR_Y
    bullet_spd[bullet_no] = 300
    bullet_no = (bullet_no+1)%BULLET_MAX

def move_bullet(): # ミサイルを移動
    for i in range(0, BULLET_MAX):
        if bullet_f[i] == True:
            if bullet_spd[i] < 500:
                bullet_spd[i] += 5
            if bullet_xs[i] > bullet_xe[i]:
                bullet_xs[i] -= 10
            if bullet_xs[i] < bullet_xe[i]:
                bullet_xs[i] += 10
            if bullet_xs[i] == bullet_xe[i]:
                bullet_xs[i] = bullet_xe[i]
            bullet_y[i] += bullet_spd[i]/100
            if bullet_y[i] > CMAX-1: 
                bullet_f[i] = False
                
            if m2_idx == 2: #　ヒットチェック
                for j in range(1, CAR):
                    cx = vehicle_x[j]-bullet_xs[i]
                    cy = vehicle_t[j]-bullet_y[i]
                    if vehicle_f[i] == True:
                        if -100 <= cx and cx <= 100 and -10 <= cy and cy <= 10:
                            bullet_f[i] = False
                            vehicle_f[j] = False
                            vehicle_x[j] = random.randint(50, 750)
                            vehicle_t[j] = random.randint(200, CMAX-200)
                            vehicle_lr[j] = 0
                            vehicle_spd[j] = random.randint(100, 200)
                            se_crash.play()
#endregion

#モード3関数の定義(模式3的函數定義)
#region
def get_dis(x1, y1, x2, y2): # ＊二点間の距離を求める(求兩點之間距離)
    return( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) )

def m3_move_vehicle(scrn, key): # 自機の操作、制御(自機的操作)
    global m3_idx, tmr, ss_x, ss_y, ss_d, ss_muteki, key_spc, key_z, cnt, energy_lily, health_lily, damage
    cnt = 0
    ss_d = 0
    
    if key[K_UP] == 1: # 自機の操作、制御
        ss_y = ss_y - 20
        if ss_y < 80:
            ss_y = 80
    if key[K_DOWN] == 1:
        ss_y = ss_y + 20
        if ss_y > 450:
            ss_y = 450
    if key[K_LEFT] == 1:
        ss_d = 1
        ss_x = ss_x - 20
        if ss_x < 40:
            ss_x = 40
    if key[K_RIGHT] == 1:
        ss_d = 2
        ss_x = ss_x + 20
        if ss_x > 1240:
            ss_x = 1240
            
    key_spc = (key_spc+1)*key[K_SPACE] # ミサイルの発射間隔(設置子彈發射間隔)
    if key_spc%5 == 1:
        set_missile(0)
        se_shot.play()
    key_z = (key_z+1)*key[K_z] # 全方位攻撃(全方位攻擊)
    if key_z == 1 and energy_lily > 10:
        set_missile(10)
        energy_lily = energy_lily - 10
        damage = True
        se_barrage.play()

    if ss_muteki%2 == 0: #無敵時間(無敵時間)
        if tmr%2 == 0:
            cnt += 1
        scrn.blit(img_sship[3+cnt%3], [ss_x-20, ss_y+10]) 
        scrn.blit(img_sship[ss_d], [ss_x-20, ss_y-40])

    if ss_muteki > 0:
        ss_muteki = ss_muteki - 1
        return
    elif m3_idx == 1:
        for i in range(ENEMY_MAX): # 敵とのヒットチェック
            if emy_f[i] == True:
                w = img_enemy[emy_type[i]].get_width()
                h = img_enemy[emy_type[i]].get_height()
                r = int((w+h)/4 + (74+96)/4)
                if get_dis(emy_x[i], emy_y[i], ss_x, ss_y) < r*r:
                    set_effect(ss_x, ss_y)
                    health_lily = health_lily - 30
                    damage = True
                    if health_lily <= 0:
                        health_lily = 0
                        m3_idx = 2
                        tmr = 0
                    if ss_muteki == 0:
                        ss_muteki = 60
                        se_damage.play()
                    if emy_type[i] < EMY_BOSS:
                        emy_f[i] = False

def set_missile(typ): # 自機の発射する弾をセットする
    global msl_no
    if typ == 0: # 単発
        msl_f[msl_no] = True
        msl_x[msl_no] = ss_x
        msl_y[msl_no] = ss_y
        msl_a[msl_no] = 270
        msl_no = (msl_no+1)%MISSILE_MAX 
    if typ == 10: # 弾幕
        for a in range(0, 360, 10):
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x
            msl_y[msl_no] = ss_y
            msl_a[msl_no] = a
            msl_no = (msl_no+1)%MISSILE_MAX

def move_missile(scrn): # 弾の移動
    for i in range(MISSILE_MAX):
        if msl_f[i] == True:
            msl_x[i] = msl_x[i] + 36*math.cos(math.radians(msl_a[i]))
            msl_y[i] = msl_y[i] + 36*math.sin(math.radians(msl_a[i]))
            img_rz = pygame.transform.rotozoom(img_weapon, -90-msl_a[i], 1.0)
            scrn.blit(img_rz, [msl_x[i]-img_rz.get_width()/2, msl_y[i]-img_rz.get_height()/2])
            if msl_y[i] < 0 or msl_x[i] < 0 or msl_x[i] > 1240:
                msl_f[i] = False

def bring_enemy(): # 敵を出す
    global Bossf
    sec = tmr/30
    
    if 0 < sec and sec < 100:
        if tmr%15 == 0:
            set_enemy(random.randint(240, 1040), LINE_T, 90, EMY_ZAKO, 10, 1) # 敵1
            set_enemy(random.randint(240, 1040), LINE_T, 90, EMY_ZAKO+1, 20, 1) # 敵2
            set_enemy(random.randint(240, 1040), LINE_T, random.randint(70, 110), EMY_ZAKO, 12, 1) # 敵2
'''    
    if 0 < sec and sec < 100:
        if tmr%15 == 0:
            set_enemy(random.randint(240, 1040), LINE_T, 90, EMY_ZAKO, 10, 1) # 敵1
            set_enemy(random.randint(240, 1040), LINE_T, 90, EMY_ZAKO+1, 20, 1) # 敵2
            set_enemy(random.randint(240, 1040), LINE_T, random.randint(70, 110), EMY_ZAKO, 12, 1) # 敵2
            #set_enemy(random.randint(20, 1260), LINE_T, random.randint(60, 120), EMY_ZAKO+2, 6, 3) # 敵3
            #set_enemy(random.randint(20, 1260), LINE_T, 90, EMY_ZAKO+3, 12, 2) # 敵4

    if tmr == 10 and Bossf == True: # ボス出現
        Bossf = False
        set_enemy(640, -210, 90, EMY_BOSS, 0, 200)
'''

def set_enemy(x, y, a, ty, sp, sh): # ＊敵機をセットする
    global emy_no
    while True:
        if emy_f[emy_no] == False:
            emy_f[emy_no] = True
            emy_x[emy_no] = x
            emy_y[emy_no] = y
            emy_a[emy_no] = a
            emy_type[emy_no] = ty
            emy_speed[emy_no] = sp
            emy_shield[emy_no] = sh
            emy_count[emy_no] = 0
            break
        emy_no = (emy_no+1)%ENEMY_MAX

def move_enemy(scrn): # 敵機の移動
    global m3_idx, tmr, energy_lily
    for i in range(ENEMY_MAX):
        if emy_f[i] == True:
            ang = -90-emy_a[i]
            png = emy_type[i]
            if emy_type[i] < EMY_BOSS: # ザコの動き
                emy_x[i] = emy_x[i] + emy_speed[i]*math.cos(math.radians(emy_a[i]))
                emy_y[i] = emy_y[i] + emy_speed[i]*math.sin(math.radians(emy_a[i]))
                if emy_x[i] < ss_x and (emy_type[i] == EMY_ZAKO or emy_type[i] == EMY_ZAKO + 1):
                    emy_x[i] += 5
                    emy_a[i] -= 2
                if emy_x[i] > ss_x and (emy_type[i] == EMY_ZAKO or emy_type[i] == EMY_ZAKO + 1):
                    emy_x[i] -= 5
                    emy_a[i] += 2
                if emy_type[i] == 4: # 進行方向を変える敵
                    emy_count[i] = emy_count[i] + 1
                    ang = emy_count[i]*10
                    if emy_y[i] > 140 and emy_a[i] == 90:
                        emy_a[i] = random.choice([50,70,110,130])
                        set_enemy(emy_x[i], emy_y[i], 140, EMY_BULLET, 6, 0)
                if emy_x[i] < LINE_L or LINE_R < emy_x[i] or emy_y[i] < LINE_T or LINE_B < emy_y[i]:
                    emy_f[i] = False
            else: # ボスの動き
                if emy_count[i] == 0:
                    emy_y[i] = emy_y[i] + 10
                    if emy_y[i] >= 20:
                        emy_count[i] = 1
                elif emy_count[i] == 1:
                    if tmr%50 == 0:
                        for j in range(0, 10):
                            set_enemy(emy_x[i], emy_y[i]+80, j*20, EMY_ZAKO+1, 6, 0)
                    if tmr%100 == 0:
                        for j in range(0, 10):
                            set_enemy(emy_x[i], emy_y[i]+80, j*20, EMY_ZAKO, 6, 0)
                            
                else:
                    emy_x[i] = emy_x[i] + emy_speed[i]
                    if emy_x[i] > 1080:
                        for j in range(0, 10):
                            set_enemy(emy_x[i], emy_y[i]+80, j*20, EMY_BULLET, 6, 0)
                        emy_count[i] = 1
                if emy_shield[i] < 100 and tmr%10 == 0:
                    set_enemy(emy_x[i], emy_y[i]+80, random.randint(60, 120), EMY_BULLET, 6, 0)

            if emy_type[i] != EMY_BULLET: # プレイヤーの弾とのヒットチェック
                w = img_enemy[emy_type[i]].get_width()
                h = img_enemy[emy_type[i]].get_height()
                r = int((w+h)/4)+12
                er = int((w+h)/4)
                for n in range(MISSILE_MAX):
                    if msl_f[n] == True and get_dis(emy_x[i], emy_y[i], msl_x[n], msl_y[n]) < r*r:
                        msl_f[n] = False
                        set_effect(emy_x[i]+random.randint(-er, er), emy_y[i]+random.randint(-er, er))
                        if emy_type[i] == EMY_BOSS: # ボスはフラッシュさせる
                            png = emy_type[i] + 1
                        emy_shield[i] = emy_shield[i] - 1
                        if emy_shield[i] == 0:
                            emy_f[i] = False
                            if energy_lily < 100:
                                energy_lily = energy_lily + 1
                            if emy_type[i] == EMY_BOSS and idx == 1: # ボスを倒すとクリア
                                idx = 3
                                tmr = 0
                                for j in range(10):
                                    set_effect(emy_x[i]+random.randint(-er, er), emy_y[i]+random.randint(-er, er))
                                se_explosion.play()

            img_rz = pygame.transform.rotozoom(img_enemy[png], ang, 1.0)
            scrn.blit(img_rz, [emy_x[i]-img_rz.get_width()/2, emy_y[i]-img_rz.get_height()/2])

def set_effect(x, y): # ＊爆発をセットする
    global eff_no
    eff_p[eff_no] = 1
    eff_x[eff_no] = x
    eff_y[eff_no] = y
    eff_no = (eff_no+1)%EFFECT_MAX

def draw_effect(scrn): # ＊爆発の演出
    for i in range(EFFECT_MAX):
        if eff_p[i] > 0:
            scrn.blit(img_explode[eff_p[i]], [eff_x[i]-48, eff_y[i]-48])
            eff_p[i] = eff_p[i] + 1
            if eff_p[i] == 6:
                eff_p[i] = 0
#endregion

def main():   
     
    #pygameの初期化
    #region
    pygame.init()
    pygame.display.set_caption("PR")
    screen = pygame.display.set_mode((SCREEN_WEIGHT,SCREEN_HIGHT))
    clock = pygame.time.Clock()
    #endregion
     
    #ゲームの初期化
    #region
    #モード0
    global damage, exps, energy_lily, health_lily, energy_karan, health_karan, m0_idx
    
    energy_lily = 100 # キャラクターのhpとenの初期値(角色的hp和en的初始值)
    health_lily = 100
    energy_karan = 100
    health_karan = 100
    
    chapter = 0 # シナリオモード用の変数の初期値(劇情用變量的初始值)
    lines = 0
    line = 0
    cnt = 0
    #ct = 0
    exps = 0
    s_idx = 0
    printed = []
    txt = ""
    story_f = False
    flag_end = False
    gameover = False
    
    voice = [
             pygame.mixer.Sound("SE\レベル4の狩りびと….ogg"),
             pygame.mixer.Sound("D:\\python\\paradise_regained\\SE\\これで私たちも戦う….ogg"),
             pygame.mixer.Sound("SE\さっそく狩りびとの….ogg"),
             pygame.mixer.Sound("SE\十字キーを押すと狩….ogg"),
             pygame.mixer.Sound("SE\スベースキーを押す….ogg"),
             pygame.mixer.Sound("SE\Zキーをすと全方位….ogg"),
             pygame.mixer.Sound("SE\でも全方位攻撃はエ….ogg"),
             pygame.mixer.Sound("SE\あくまでも最終手段….ogg"),
             pygame.mixer.Sound("SE\この先きっと危険な….ogg"),
             pygame.mixer.Sound("SE\でも兄さんと一緒な….ogg")
    ]
    
    m0_idx = 0
    
    #モード1
    global key, m1_idx, tmr, se_port
    
    se_port = pygame.mixer.Sound("muisc/Explosion10.ogg")
    set_stage() # ステージのデータをセットする(設置關卡資料)
    set_chara_pos() # キャラのスタート位置(設置角色和敵人的初始位子)
    m1_idx = -1
    
    #モード2
    global m2_idx, laps, se_crash, my_vehice

    img_bg = pygame.image.load("img/bg.png").convert()
    img_vehice = [
        pygame.image.load("img/hunter0.png").convert_alpha(),
        pygame.image.load("img/hunter0.png").convert_alpha(),
        pygame.image.load("img/hunter1.png").convert_alpha(),
        pygame.image.load("img/hunter2.png").convert_alpha(),
        pygame.image.load("img/hunter3.png").convert_alpha(),
        pygame.image.load("img/hunter4.png").convert_alpha(),
        pygame.image.load("img/hunter4.png").convert_alpha(),
        pygame.image.load("img/enemy0.png").convert_alpha(),

    ]

    se_crash = pygame.mixer.Sound("se/crash.ogg") # SEの読み込み

    # 道路の板の基本形状を計算
    BOARD_W = [0]*BOARD
    BOARD_H = [0]*BOARD
    BOARD_UD = [0]*BOARD
    for i in range(BOARD):
        BOARD_W[i] = 10+(BOARD-i)*(BOARD-i)/12
        BOARD_H[i] = 3.4*(BOARD-i)/BOARD
        BOARD_UD[i] = 2*math.sin(math.radians(i*1.5))

    make_course() # 道路のデータを作る
    m2_init_vehicle() # 狩り人の初期化
    m2_idx = 0
    vertical = 0  
    mouse_pres = 0
    #モード3
    global m3_idx, bg_y1, bg_y2 ,bg_y3, ss_x, ss_y, ss_d, ss_muteki
    global se_barrage, se_damage, se_explosion, se_shot
    
    se_barrage = pygame.mixer.Sound("SE/barrage.ogg")
    se_damage = pygame.mixer.Sound("SE/explosion.ogg")
    se_explosion = pygame.mixer.Sound("SE\explosion.ogg")
    se_shot = pygame.mixer.Sound("SE\shot.ogg")
    m3_idx = -1
    ss_y = 700
    tmr_ex = 0 
    #endregion
    
    tmr = 0
    idx = 3
        
    while True:
    
        for event in pygame.event.get(): # 画面の操作(螢幕的操作)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_F1:
                    screen = pygame.display.set_mode((SCREEN_WEIGHT,SCREEN_HIGHT), FULLSCREEN)
                if event.key == K_F2 or event.key == K_ESCAPE:
                    screen = pygame.display.set_mode((SCREEN_WEIGHT,SCREEN_HIGHT))
        
        key = pygame.key.get_pressed()
        tmr += 1
        tmr_ex += 1
    
        if idx == 0: # 開始画面(開始畫面)
            
            timer = 60 # フレームの値を設定(設定幀數)
            
            if m0_idx == 0: # 開始画面(開始畫面)           
                screen.fill((253, 248, 216))
                
                if tmr < 255/4: # 画面と背景のエフェクトを描く(繪製畫面和背景特效)
                    for i in range(0,MAX):
                        rx[i] = random.randint(-tmr,SCREEN_WEIGHT-tmr) # ランダム矩形を生成(隨機生成矩形)
                        ry[i] = random.randint(-tmr,SCREEN_HIGHT-tmr)
                        rx1[i] = random.randint(0,tmr*8)
                        ry1[i] = random.randint(0,tmr*8)
        
                    for i in range(0,MAX):
                        pygame.draw.rect(screen,((255-tmr)*4%255,(255-tmr)*4%255,(255-tmr)*4%255),[rx[i],ry[i],rx1[i],ry1[i]])

                    screen.blit(title[1], [0, 110]) # タイトルを描く(繪製標題)
                    screen.blit(title[2], [0, 110])
                    screen.blit(title[0], [0, 110])
                    
                    if tmr == 1:
                        pygame.mixer.music.load(r"muisc\power-on.mp3") 
                        pygame.mixer.music.play(-1)
                              
                else:
                    screen.fill((0, 0, 0))
                    
                    for i in range(0,MAX): # 線を描く(繪製線條)
                        pygame.draw.rect(screen,(0,0,0),[rx[i],ry[i],rx1[i],ry1[i]])
                
                    screen.blit(title[1], [0, 110]) # タイトルを描く(繪製標題)
                    #screen.blit(title[2], [0, 110])
                    screen.blit(title[0], [0, 110])
                    pygame.draw.rect(screen,(253, 248, 216),[10,SCREEN_HIGHT-10,((SCREEN_WEIGHT-tmr)%SCREEN_WEIGHT-10),2])
                    pygame.draw.rect(screen,(253, 248, 216),[10,10,(tmr%SCREEN_WEIGHT-10),2])
                    pygame.draw.rect(screen,(253, 248, 216),[SCREEN_WEIGHT-10,10,2,(tmr%SCREEN_HIGHT-10)])
                    pygame.draw.rect(screen,(253, 248, 216),[10,10,2,((SCREEN_HIGHT-tmr)%SCREEN_HIGHT-10)])
                
                    if tmr*4 <= 700: # 線を描く(繪製線條)
                        pygame.draw.rect(screen,(253, 248, 216),[SCREEN_WEIGHT/2-380,SCREEN_HIGHT/2+177,tmr*4,2])
                    else:
                        pygame.draw.rect(screen,(253, 248, 216),[SCREEN_WEIGHT/2-380,SCREEN_HIGHT/2+177,700,2])

                    if tmr%30 != 0:
                        story_draw_txt(screen, "-Press [SPACE] to start-", SCREEN_WEIGHT/2-100, 600, 10, (253, 248, 216))
                    if key[K_SPACE] == 1:
                        m0_idx  = 1
                        tmr = 0
                        pygame.mixer.music.stop()
                        
            if m0_idx == 1:
                if tmr == 1:
                    pygame.mixer.music.load(r"muisc\pcswitchon.mp3")
                    pygame.mixer.music.play(0)
                if tmr == 60:
                    idx = 1
                    tmr = 1
                     
        if idx == 1: # モード1
            
            timer = 10 # フレームの値を設定(設定幀數)
            
            draw_screen(screen) # ゲーム画面を描く(繪製模式1遊戲畫面)
            
            if m1_idx == -1: 
                screen.fill(BLACK) # フェードイン(切換場景)
                if tmr == 1:
                    black_out = True
                if black_out == False:
                    m1_idx = 0
                    no = True
                              
            if m1_idx == 0:
                
                screen.fill(BLACK) 
                
                if no == True: 
                    pygame.mixer.music.load(r"muisc\岡部啓一,瀬尾祥太郎 - Weight of the World：丁.mp3")
                    pygame.mixer.music.play(-1)
                    no = False 
                
                if story_f == False and flag_end == False: # シナリオ開始(故事模式開始)
                    story_f = True
                    chapter = 0

                if story_f == False and flag_end == True: # シナリオ終了(故事模式結束)
                    if key[K_SPACE] == 1:
                        stage = 1
                        set_stage() #　ステージを配置(配置場景)
                        set_chara_pos() #　キャラクターを配置(配置角色)
                        m1_idx = 1
                        tmr = 0

            if m1_idx == 1: # ゲームをプレイ(遊戲進行)
                move_lily(key) # キャラクターを移動(角色移動)
                move_guardian() # 敵を移動(移動敵人)
                for i in range(GUARDIAN_MAX):
                    move_guardian2(i)
                
                if tmr%60 == 0: # 毎秒エネルギーを減少(每秒減少能量）
                    energy_lily -= 1
                if port == 0:
                    pass
                if tmr == 1:
                    pygame.mixer.music.load("muisc/高橋邦幸,瀬尾祥太郎 - 砂塵ノ記憶：丁.mp3")
                    pygame.mixer.music.play(-1)
                if health_lily == 0 or energy_lily == 0:
                    m1_idx = 3

            if m1_idx == 2: # 敵にやられた(被敵人碰到了)
                if tmr == 1:
                    se_damage.play()
                    health_lily = health_lily - 10
                if tmr == 10:
                    set_chara_pos() # キャラクターを配置(重新配置角色)
                    m1_idx = 1
                    tmr = 0

            if m1_idx == 3: # ゲームオーバー(遊戲失敗)
                if tmr == 1:
                    gameover = True
                    pygame.mixer.music.stop()

                if tmr == 10:
                    pygame.mixer.music.load(r"muisc\岡部啓一,瀬尾祥太郎 - 「塔」：丁.mp3")
                    pygame.mixer.music.play(0)
                if tmr > 20:
                    draw_text(screen, "Simulation failded", 630, 290, 80, RED)
                if tmr == 320:
                    m1_idx = 0 # モード1リスタート(重新開始模式1)
                    tmr = 0

            if m1_idx == 4: # ステージクリア
                if story_f == False and flag_end == False: # シナリオ開始(故事模式開始)
                    story_f = True
                    chapter = 0
                if story_f == False and flag_end == True: # シナリオ終了(故事模式結束)
                    if key[K_SPACE] == 1:
                        idx = 2 # モード2開始(開始模式2)
                        tmr = 0
  
        if idx == 2: # モード2
            timer = 60 # フレームの値を設定(設定幀數)

            di = 0
            ud = 0
            
            board_x = [0]*BOARD
            board_ud = [0]*BOARD
            
            for i in range(BOARD): # 道路の板の位置を計算
                di += curve[int(vehicle_t[0]+i)%CMAX]
                ud += updown[int(vehicle_t[0]+i)%CMAX]
                board_x[i] = 640 - BOARD_W[i]*vehicle_x[0]/800 + di/2
                board_ud[i] = ud/60

            horizon = 360 + int(ud/8) # 地平線の座標の計算(計算地平線座標)
            sy = horizon # 道路を描き始める位置

            vertical = vertical - int(vehicle_spd[0]*di/10000) # 背景の垂直位置
            if vertical < 0:
                vertical += 1
            if vertical >= 1280:
                vertical -= 1

            # フィールドの描画
            screen.blit(img_bg, [vertical-1860, horizon-390])
            screen.blit(img_bg, [vertical+640, horizon-390])

            # 描画用データをもとに道路を描く
            for i in range(BOARD-1, 0, -1):
                ux = board_x[i]
                uy = sy - BOARD_UD[i]*board_ud[i]
                uw = BOARD_W[i]
                sy = sy + BOARD_H[i]
            
                col = (160, 160, 160)
                pygame.draw.rect(screen,col, (ux,uy,uw,sy))
                pygame.draw.rect(screen,BLACK, (ux,uy,uw*0.1,sy))
                pygame.draw.rect(screen,BLACK, (ux+uw-uw*0.1,uy,uw*0.1,sy))
                col = BLACK
                if (vehicle_t[0]+i)%25 <= 3:
                    pygame.draw.rect(screen,col, (ux-uw*0.1,uy,uw*0.1,sy))
                    pygame.draw.rect(screen,col, (ux+uw,uy,uw*0.1,sy))
                if (vehicle_t[0]+i)%25 <= 6:   
                    pygame.draw.rect(screen,col, (ux,uy,uw,sy))

                for c in range(1, CAR):
                    if int(vehicle_t[c])%CMAX == int(vehicle_t[0]+i)%CMAX:
                        if vehicle_f[c] == True:
                            draw_obj(screen, img_vehice[7], ux+vehicle_x[c]*BOARD_W[i]/800, uy, 0.05+BOARD_W[i]/BOARD_W[0])

                for c in range(0, BULLET_MAX):
                    if int(bullet_y[c])%CMAX == int(vehicle_t[0]+i)%CMAX:
                        if bullet_f[c] == True:
                            draw_obj(screen, img_missile[0], ux+bullet_xs[c]*BOARD_W[i]/800, uy, 0.05+BOARD_W[i]/BOARD_W[0])
                
                if i == PLCAR_Y: # PLAYERカー
                    draw_shadow(screen, ux+vehicle_x[0]*BOARD_W[i]/800, uy, 200*BOARD_W[i]/BOARD_W[0])
                    draw_obj(screen, img_vehice[3+vehicle_lr[0]+my_vehice*7], ux+vehicle_x[0]*BOARD_W[i]/800, uy, 0.05+BOARD_W[i]/BOARD_W[0])
                    #draw_obj(screen, img_effect[0], ux+vehicle_x[0]*BOARD_W[i]/800, uy, 0.05+BOARD_W[i]/BOARD_W[0])

            if m2_idx == 0: # モード3開始
                screen.fill(BLACK)  # フェードイン(切換場景)
                if tmr == 1:
                    black_out = True
                if black_out == False:
                    if key[K_SPACE] != 0:
                        m2_init_vehicle()
                        m2_idx = 1
                        tmr = 0
                        laps = 0
                
            if m2_idx == 1:
                screen.fill(BLACK)

                if story_f == False and flag_end == False: # シナリオ開始(故事模式開始)
                    story_f = True
                    chapter = 0

                if story_f == False and flag_end == True: # シナリオ終了(故事模式結束)
                    if key[K_SPACE] == 1:
                        pygame.mixer.music.load("muisc\岡部啓一,瀬尾祥太郎 - 生マレ出ヅル意思：丁.mp3")
                        pygame.mixer.music.play(-1)
                        m2_idx = 2
                        tmr = 0

            if m2_idx == 2:  # ゲームをプレイ(遊戲進行)
                
                m2_drive_vehicle(key) # プレイヤーの狩り人の操作、制御
                m2_move_vehicle(1) # COMカーの制御
                move_bullet() # ミサイルを移動
                
                if key[K_SPACE] == 1 and energy_karan >= 10: # スローモーション
                    timer = 5
                    energy_karan -= 10
                    c_x, c_y = pygame.mouse.get_pos()
                    mouse_pres = (mouse_pres+1)*pygame.mouse.get_pressed()[0]
                    if mouse_pres%5 == 1:
                        set_bullet(c_x) # ミサイルを配置
                    pygame.draw.circle(screen,WHITE,(c_x,c_y),5,2)
                if energy_karan != 100:
                    energy_karan += 1

            if m2_idx == 3: # ステージクリア
                if tmr == 1:
                    pygame.mixer.music.stop()
                vehicle_spd[0] = vehicle_spd[0]*0.96
                vehicle_t[0] = vehicle_t[0] + vehicle_spd[0]/100
                m2_move_vehicle(1)
                if story_f == False and flag_end == False: # シナリオ開始(故事模式開始)
                    story_f = True
                    chapter = 0
                if story_f == False and flag_end == True: # シナリオ終了(故事模式結束)
                    if key[K_SPACE] == 1:
                        idx = 3 # モード2開始(開始模式2)
                        tmr = 0
            
            if m2_idx == 4: # ゲームオーバー(遊戲失敗)
                pass
            
        if idx == 3: # モード3
            
            timer = 30
            
            # 背景を描画
            bg_y1 = (bg_y1+3)%600
            screen.blit(img_bg_03[0], [0, bg_y1-600])
            screen.blit(img_bg_03[0], [0, bg_y1])
            bg_y2 = (bg_y2+8)%600
            screen.blit(img_bg_03[1], [0, bg_y2-600])
            screen.blit(img_bg_03[1], [0, bg_y2])
            bg_y3 = (bg_y3+20)%600
            screen.blit(img_bg_03[2], [0, bg_y3-600])
            screen.blit(img_bg_03[2], [0, bg_y3])
            
            if m3_idx == -1: # モード3開始
                if tmr == 1:
                    black_out = True
                if black_out == False:
                    m3_idx = 0

            if m3_idx == 0:
                if story_f == False and flag_end == False: # シナリオ開始(故事模式開始)
                    story_f = True
                    chapter = 0
                    tmr = 0
                pygame.mixer.music.load(r"muisc\帆足圭吾,瀬尾祥太郎 - 終ワリノ音：丁.mp3")
                pygame.mixer.music.play(-1)
            
                ss_d = 0
                ss_x = 640
                
                if ss_y > 350:
                    ss_y -= 20
                elif ss_y == 350:
                    ss_y = 350
                
                screen.blit(img_sship[3+tmr_ex%3], [ss_x-20, ss_y+10])
                screen.blit(img_sship[ss_d], [ss_x-20, ss_y-40])
                
                if story_f == False and flag_end == True: # シナリオ終了(故事模式結束)
                    if key[K_SPACE] == 1:
                        m3_idx = 1
                        ss_d = 0
                        ss_muteki = 0
                        for i in range(ENEMY_MAX):
                            emy_f[i] = False
                        for i in range(MISSILE_MAX):
                            msl_f[i] = False
                        pygame.mixer.music.load(r"muisc\高橋邦幸,瀬尾祥太郎 - 依存スル弱者：丁.mp3")
                        pygame.mixer.music.play(-1)

            if m3_idx == 1: # ゲームプレイ中
                m3_move_vehicle(screen, key)
                move_missile(screen)
                bring_enemy()
                move_enemy(screen)

            if m3_idx == 2: # ゲームオーバー
                move_missile(screen)
                move_enemy(screen)
                if tmr == 1:
                    gameover = True
                    pygame.mixer.music.stop()
                if tmr <= 20:
                    if tmr%2 == 0:
                        set_effect(ss_x+random.randint(-60,60), ss_y+random.randint(-60,60))
                    if tmr%2 == 0:
                        se_damage.play()
                if tmr == 30:
                    pygame.mixer.music.load(r"muisc\岡部啓一,瀬尾祥太郎 - 「塔」：丁.mp3")
                    pygame.mixer.music.play(0)
                if tmr > 30:
                    draw_text(screen, "Simulation failded", 630, 290, 80, RED)
                if tmr == 400:
                    m3_idx = 0
                    tmr = 0

            if m3_idx == 3: # ゲームクリア
                if story_f == False and flag_end == False: # シナリオ開始(故事模式開始)
                    story_f = True
                    chapter = 0
                if story_f == False and flag_end == True: # シナリオ終了(故事模式結束)
                    if key[K_SPACE] == 1:
                        idx = 4 # モード2開始(開始模式2)
                        tmr = 0
        draw_effect(screen)
        
        if idx == 4: # エンディング
            pass
        
        if idx > 0: # メイン画面を描く 
            
            if story_f == True: # シナリオモード(故事模式)
                if key[K_SPACE] == 1 and s_idx == 0:
                    s_idx = 1
                    tmr = 0
                    #voice[ct].play() # キャラボイス(播放語音)
                    #ct = ct + 1
                    
                if s_idx == 1:
                    if len(story[chapter][lines][line]) != cnt and len(story[chapter][lines][line]) >= cnt:
                        printed.append(story[chapter][lines][line][tmr%len(story[chapter][lines][line])])
                        txt = "".join(printed)
                        cnt += 1
                        
                        if tmr%3 == 0:
                            exps = 1
                        else:
                            exps = 3
                            
                    elif len(story[chapter][lines][line]) == cnt and len(story[chapter])-1 > lines:
                        if key[K_SPACE] == 1:
                            #voice[ct].play()　# キャラボイス(播放語音)
                            lines += 1
                            #ct += 1
                            tmr = 0
                            cnt = 0
                            printed = []
                            txt = ""  
                                                
                    elif len(story[chapter])-1 == lines:
                        if key[K_SPACE] == 1:
                            flag_end = True
                            story_f = False
                            printed = []
                            txt = ""
                            s_idx = 0
                            exps = 0
                            cnt = 0

            screen.blit(img_BG,[0, 0]) # メイン画面を描く(繪製主畫面)
            pygame.draw.rect(screen, (49,49,49), [200, 540, 8, 150-(energy_lily*1.5+2)])
            pygame.draw.rect(screen, (49,49,49), [180, 540, 8, 150-(health_lily*1.5+2)])
            pygame.draw.rect(screen, (49,49,49), [390, 540, 8, 150-(energy_karan*1.5+2)])
            pygame.draw.rect(screen, (49,49,49), [370, 540, 8, 150-(health_karan*1.5+2)])
            
            if damage == True: # キャラクターを描く(繪製主畫面角色)
                screen.blit(kao[2],[30, 540])
                if tmr%40 == 0:
                    damage = False
            elif gameover == True:
                screen.blit(kao[2],[30, 540])
            elif damage == False:
                screen.blit(kao[exps],[30, 540])
                screen.blit(kao[4],[220, 540])
                story_draw_txt(screen, txt, 455, 570, 15, BLACK)
                
            if black_out == True: # # フェードイン(切換場景)
                shadow = pygame.Surface([1280, 720])
                shadow.set_alpha((255-tmr*10)%255) # Surfaceの透明度を設定
                pygame.draw.ellipse(shadow, BLACK, [0,0,10,10])
                screen.blit(shadow, [0, 0])
                if tmr == 24:
                    black_out = False
                
        pygame.display.update()
        clock.tick(timer)
                
if __name__ == "__main__":
    main()