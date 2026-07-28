<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Zombie Survival _ PyScript</title>
<link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
<script defer src="https://pyscript.net/latest/pyscript.js"></script>
<style>
  body { background:#080808; color:#ddd; margin:0; }
  canvas { display:block; margin:0 auto; background:#000; }
</style>
</head>
<body>
<canvas id="gameCanvas" width="1000" height="600"></canvas>

<py-script>
from js import document, window
import math, random, time

canvas = document.getElementById("gameCanvas")
ctx = canvas.getContext("2d")
WIDTH, HEIGHT = canvas.width, canvas.height

# --- Player ---
player = {
    "x": WIDTH/2, "y": HEIGHT-120, "w":48, "h":64, "vx":0, "vy":0,
    "speed":220, "grounded":True, "health":100, "max_health":100,
    "current_weapon":0,
    "weapons":[
        {"name":"Pistol","fire_rate":250,"bullet_speed":700,"damage":20,"clip":12,"clipMax":12,"reserve":36,"reloadTime":900,"spread":6},
        {"name":"Shotgun","fire_rate":900,"bullet_speed":600,"damage":12,"pellet":7,"clip":6,"clipMax":6,"reserve":24,"reloadTime":1400,"spread":22},
        {"name":"Rifle","fire_rate":110,"bullet_speed":900,"damage":16,"clip":30,"clipMax":30,"reserve":90,"reloadTime":1100,"spread":3}
    ],
    "lastShot":0, "reloading":False, "reloadTimer":0
}

# --- Game state ---
keys = {}
mouse = {"x":WIDTH/2, "y":HEIGHT/2, "down":False}
bullets = []
zombies = []
wave = 0
wave_active = False
score = 0
gravity = 1600
groundY = HEIGHT - 60

# --- Utilities ---
def clamp(v,a,b): return max(a,min(b,v))
def rand(a,b): return random.uniform(a,b)

# --- Input ---
def keydown(e): keys[e.key.lower()]=True
def keyup(e): keys[e.key.lower()]=False
def mousemove(e):
    rect = canvas.getBoundingClientRect()
    mouse["x"] = (e.clientX - rect.left)*(canvas.width/rect.width)
    mouse["y"] = (e.clientY - rect.top)*(canvas.height/rect.height)
def mousedown(e): mouse["down"]=True
def mouseup(e): mouse["down"]=False

document.addEventListener("keydown", keydown)
document.addEventListener("keyup", keyup)
canvas.addEventListener("mousemove", mousemove)
canvas.addEventListener("mousedown", mousedown)
document.addEventListener("mouseup", mouseup)

# --- Game functions ---
def spawn_bullet(x,y,angle,speed,damage):
    bullets.append({"x":x,"y":y,"vx":math.cos(angle)*speed,"vy":math.sin(angle)*speed,"life":2000,"damage":damage})

def shoot(now):
    w = player["weapons"][player["current_weapon"]]
    if player["reloading"] or now - player["lastShot"] < w["fire_rate"] or w["clip"] <= 0:
        return
    player["lastShot"] = now
    w["clip"] -= 1
    angle = math.atan2(mouse["y"]-(player["y"]-player["h"]/2), mouse["x"]-player["x"])
    if player["current_weapon"]==1:
        for _ in range(w["pellet"]):
            spread = math.radians(rand(-w["spread"],w["spread"]))
            spawn_bullet(player["x"]+20, player["y"]-player["h"]/2+10, angle+spread, w["bullet_speed"], w["damage"])
    else:
        spread = math.radians(rand(-w["spread"],w["spread"]))
        spawn_bullet(player["x"]+20, player["y"]-player["h"]/2+10, angle+spread, w["bullet_speed"], w["damage"])

def spawn_zombie(x=None,y=None):
    if x is None: x = random.choice([-rand(40,300), WIDTH + rand(40,300)])
    if y is None: y = groundY
    zombies.append({"x":x,"y":y,"w":48,"h":64,"hp":30,"speed":50,"lastAttack":0})

def start_next_wave():
    global wave, wave_active
    wave += 1
    wave_active = True
    count = int(4 + wave*1.8)
    for _ in range(count):
        spawn_zombie()

# --- Game loop ---
def loop(timestamp):
    dt = 1/60
    now = timestamp

    # --- Player movement ---
    player["vx"] = -player["speed"] if keys.get("a") else player["speed"] if keys.get("d") else 0
    player["x"] += player["vx"]*dt
    if keys.get("w") and player["grounded"]:
        player["vy"] = -650
        player["grounded"] = False
    player["vy"] += gravity*dt
    player["y"] += player["vy"]*dt
    if player["y"] >= groundY:
        player["y"] = groundY
        player["vy"] = 0
        player["grounded"] = True
    player["x"] = clamp(player["x"],30,WIDTH-30)

    # --- Shooting ---
    if mouse["down"]: shoot(now)

    # --- Draw ---
    ctx.fillStyle = "#111"
    ctx.fillRect(0,0,WIDTH,HEIGHT)
    # player
    ctx.fillStyle = "#0af"
    ctx.fillRect(player["x"]-player["w"]/2, player["y"]-player["h"], player["w"], player["h"])
    # zombies
    ctx.fillStyle = "#6b8e23"
    for z in zombies:
        ctx.fillRect(z["x"]-z["w"]/2, z["y"]-z["h"], z["w"], z["h"])
    # bullets
    ctx.fillStyle = "yellow"
    for b in bullets:
        ctx.fillRect(b["x"]-3,b["y"]-3,6,6)

    window.requestAnimationFrame(loop)

window.requestAnimationFrame(loop)
</py-script>
</body>
</html>
