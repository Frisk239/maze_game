import json

SCREENSIZE = (800, 625)
HEROPICPATH = 'resources/images/hero.png'
# font
FONT = 'SegoeScript'
FONT2 = 'Consolas'
# colors
BACKGROUND = (255, 255, 255)
FOREGROUND = (0, 0, 0)
HIGHLIGHT = (255, 0, 0)
LINE = (185, 185, 185)

FPS = 30

# 迷宫相关
BLOCKSIZE = 15
MAZESIZE = [15, 10]  # num_rows * num_cols
STARTPOINT = [1, 1]
DESTINATION = [15, 10]
BORDERSIZE = ((SCREENSIZE[0] - MAZESIZE[1] * BLOCKSIZE) // 2, (SCREENSIZE[1] - MAZESIZE[0] * BLOCKSIZE) // 2)

'''写入配置'''
def write_cfg():
    cfgs = {'MAZESIZE': MAZESIZE, 'STARTPOINT': STARTPOINT, 'DESTINATION': DESTINATION}
    with open('cfg.txt', 'w') as fp:
        json.dump(cfgs, fp)

'''读出配置'''
def read_cfg():
    with open('cfg.txt', 'r') as fp:
        cfgs = json.load(fp)
    return cfgs