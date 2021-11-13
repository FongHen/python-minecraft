import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hits = mc.events.pollProjectileHits()
    if len(hits) > 0:
        hit = hits[0]
        x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(x,y,z)
        mc.setSign (x, y, z, 63, 2, ["第1行","第2行","第3行","第4行"])
        mc.spawnEntity(x,y,z,93)
        print("恭喜你獵到了"+str(block))
