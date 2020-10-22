import os

IMG_SIZE = 128
SCREEN_SIZE = 512
NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 16
MARGIN = 8

ASSET_DIR = 'assets'
#making a list of all pics in assets with the finish of png file
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']
assert len(ASSET_FILES) == 8 #check if all 8 pics are there
