# Base project format.
# put this on the desktop : git clone https://github.com/tritechsc/mcpi
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    x, y, z = mc.player.getPos()		
    return mc
    
def pyramid(mc,x,y,z):
	h,l = 15,15
	for k in range (0,16):
		mc.setBlocks(x+h,y+k,z-l,x-h,y+k,z+l,35,k)	
		print(x,y,z,h,k,l)
		l = l-1
		h = h-1

def clear_with_air_up(mc, x, y, z,h,k,l):
	air = 0;
	mc.setBlocks(x-h,y,z-l,x+h,y+k,z+l,air)	
	

		
	
def main():
	mc = init()
	xx,yy,zz,h,k,l = 0,0,0,10,100,10 # comment out when design is good
	clear_with_air_up(mc,xx, yy, zz,h,k,l) # comment out when design is good
	x,y,z = 0,0,0
	for d in range (0,60):
		mc.setBlocks(x-5, y, z,x+5,y + 5, z+5, 35,d)
		mc.setBlocks(x-5, y+6, z,x+5,y + 11, z+5, 35,d+1)
		mc.setBlocks(x-4, y+1, z+1,x+4,y + 12, z+4,0)# clear with air
		mc.player.setPos(x, y+2, z+3)
		mc.setBlock(x, y, z,35,d)
		#mc.setBlock(x-5, y+2, z, 64, d)
		mc.setBlock(x, y+1, z, 64, 4)
		mc.setBlock(x, y+2, z, 64, 8)
		pyramid(mc,x,y+12,z+2.5)
		
		sleep(0.25)
		print("d ",d)
	mc.player.setPos(x, y+2, z-5)
	
		
main()

# multiple line comment
"""
https://www.raspberrypi.org/learning/minecraft-whac-a-block-game/worksheet/
#write 'Hello Minecraft World' to the chat window
mc.postToChat("Hello Minecraft World")

#get block event hits that have occured since the last time the function was run
blockEvents = mc.events.pollBlockHits()
for blockEvent in blockEvents:
    print blockEvent


AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71 w
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
