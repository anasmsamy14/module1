import pygame
import random
import math
import sys

# --- Setup ---
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Survival — Full Mode")
clock = pygame.time.Clock()

# --- Colors ---
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (200,20,20)
GREEN = (0,200,0)
YELLOW = (255,255,0)
DARK_OVERLAY = (0,0,0,150)

# --- Player ---
class Weapon:
    def __init__(self, name, fire_rate, bullet_speed, damage, clip, clip_max, reserve, reload_time, spread, pellet=1):
        self.name=name
        self.fire_rate=fire_rate
        self.bullet_speed=bullet_speed
        self.damage=damage
        self.clip=clip
        self.clip_max=clip_max
        self.reserve=reserve
        self.reload_time=reload_time
        self.spread=spread
        self.pellet=pellet

class Player:
    def __init__(self):
        self.x, self.y = WIDTH//2, HEIGHT-120
        self.w, self.h = 48, 64
        self.vx, self.vy = 0,0
        self.speed = 220
        self.grounded = False
        self.health = 100
        self.max_health = 100
        self.weapons = [
            Weapon('Pistol', 250, 700, 20, 12, 12, 36, 900, 6),
            Weapon('Shotgun', 900, 600, 12, 6,6,24,1400,22,7),
            Weapon('Rifle',110,900,16,30,30,90,1100,3)
        ]
        self.current_weapon = 0
        self.last_shot = 0
        self.reloading = False
        self.reload_timer = 0

player = Player()

# --- Zombies ---
class Zombie:
    def __init__(self,x,y,hp=30,speed=40):
        self.x=x
        self.y=y
        self.w=48
        self.h=64
        self.hp=hp
        self.speed=speed
        self.last_attack=0

zombies = []

# --- Bullets ---
class Bullet:
    def __init__(self,x,y,angle,speed,damage):
        self.x=x
        self.y=y
        self.vx=math.cos(angle)*speed
        self.vy=math.sin(angle)*speed
        self.life=2000
        self.damage=damage

bullets = []

# --- Pickups ---
class Pickup:
    def __init__(self,type_,x,y):
        self.type=type_
        self.x=x
        self.y=y
        self.w=32
        self.h=32

pickups = []

# --- Game variables ---
gravity = 1600
ground_y = HEIGHT - 60
wave = 0
wave_active = False
score = 0
difficulty_mult = 1.0

# --- Utilities ---
def clamp(v,a,b): return max(a,min(b,v))
def rand(min_,max_): return random.uniform(min_,max_)
def distance(a,b): return math.hypot(a[0]-b[0],a[1]-b[1])

# --- Functions ---
def spawn_zombie(x=None,y=None):
    if x is None: x = random.choice([-rand(40,300), WIDTH + rand(40,300)])
    if y is None: y = ground_y
    hp = int(30*difficulty_mult)
    speed = rand(35,70)*difficulty_mult
    zombies.append(Zombie(x,y,hp,speed))

def start_next_wave():
    global wave, wave_active, difficulty_mult
    wave += 1
    wave_active = True
    difficulty_mult = 1 + (wave-1)*0.12
    count = int(4 + wave*1.8)
    for _ in range(count):
        spawn_zombie()

def shoot():
    now = pygame.time.get_ticks()
    w = player.weapons[player.current_weapon]
    if player.reloading or now-player.last_shot<w.fire_rate or w.clip<=0: return
    player.last_shot = now
    w.clip -= 1
    mx,my = pygame.mouse.get_pos()
    angle = math.atan2(my-(player.y - player.h/2), mx - player.x)
    if player.current_weapon==1:  # Shotgun
        for _ in range(w.pellet):
            spread = math.radians(rand(-w.spread,w.spread))
            bullets.append(Bullet(player.x+20,player.y-player.h/2+10,angle+spread,w.bullet_speed,w.damage))
    else:
        spread = math.radians(rand(-w.spread,w.spread))
        bullets.append(Bullet(player.x+20,player.y-player.h/2+10,angle+spread,w.bullet_speed,w.damage))

def start_reload():
    w = player.weapons[player.current_weapon]
    if player.reloading or w.clip>=w.clip_max or w.reserve<=0: return
    player.reloading=True
    player.reload_timer=pygame.time.get_ticks() + w.reload_time

def reset_game():
    global bullets,zombies,pickups,wave,wave_active,score
    bullets=[]; zombies=[]; pickups=[]
    wave=0; wave_active=False; score=0
    player.x, player.y = WIDTH//2, ground_y
    player.health = player.max_health
    for w in player.weapons:
        w.clip = w.clip_max
        w.reserve = w.clip_max*3
    start_next_wave()

# --- Main loop ---
running = True
reset_game()
while running:
    dt = clock.tick(60)/1000  # seconds
    now = pygame.time.get_ticks()
    # --- Events ---
    for event in pygame.event.get():
        if event.type==pygame.QUIT: running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1: player.current_weapon=0
            elif event.key==pygame.K_2: player.current_weapon=1
            elif event.key==pygame.K_3: player.current_weapon=2
            elif event.key==pygame.K_r: start_reload()
            elif event.key==pygame.K_RETURN and (not wave_active or player.health<=0): reset_game()
    # --- Input ---
    keys = pygame.key.get_pressed()
    left,right,up = keys[pygame.K_a], keys[pygame.K_d], keys[pygame.K_w]
    # --- Player movement ---
    player.vx = -player.speed if left else player.speed if right else 0
    player.x += player.vx * dt
    if up and player.grounded: player.vy = -650; player.grounded=False
    player.vy += gravity*dt
    player.y += player.vy*dt
    if player.y>=ground_y: player.y=ground_y; player.vy=0; player.grounded=True
    player.x = clamp(player.x,30,WIDTH-30)
    # --- Shooting ---
    if pygame.mouse.get_pressed()[0]: shoot()
    if player.reloading and now>=player.reload_timer:
        w=player.weapons[player.current_weapon]
        need = w.clip_max - w.clip
        take = min(need, w.reserve)
        w.clip += take
        w.reserve -= take
        player.reloading=False
    # --- Bullets ---
    for b in bullets[:]:
        b.x += b.vx*dt
        b.y += b.vy*dt
        b.life -= dt*1000
        if b.life<=0: bullets.remove(b)
    # --- Zombies ---
    for z in zombies[:]:
        dir_ = player.x - z.x
        z.x += math.copysign(z.speed*0.5,dir_)*dt
        if abs(player.x-z.x)<36 and now - z.last_attack>800:
            z.last_attack = now
            player.health -= 8
        if player.health<=0: player.health=0; wave_active=False
    # --- Wave end ---
    if wave_active and len(zombies)==0: wave_active=False; score+=int(20*wave)
    # --- Draw ---
    screen.fill(BLACK)
    # Ground
    pygame.draw.rect(screen,(50,50,50),(0,ground_y,WIDTH,HEIGHT-ground_y))
    # Player
    pygame.draw.rect(screen,(0,150,200),(player.x-player.w//2,player.y-player.h,player.w,player.h))
    # Zombies
    for z in zombies: pygame.draw.rect(screen,(100,200,50),(z.x-z.w//2,z.y-z.h,z.w,z.h))
    # Bullets
    for b in bullets: pygame.draw.circle(screen,YELLOW,(int(b.x),int(b.y)),4)
    # HUD
    pygame.draw.rect(screen,(50,50,50),(10,10,200,20))
    pygame.draw.rect(screen,RED,(10,10,200*player.health/player.max_health,20))
    font = pygame.font.SysFont(None,24)
    txt = font.render(f'Score: {score}  Wave: {wave}',True,WHITE)
    screen.blit(txt,(10,40))
    pygame.display.flip()

pygame.quit()
sys.exit()
