import pygame
import os


def draw_text(surface, text, font, color, loc, anchor='topleft'):
    text = str(text)
    text = font.render(text, True, color)
    rect = text.get_rect()

    if anchor == 'topleft': rect.topleft = loc
    elif anchor == 'bottomleft': rect.bottomleft = loc
    elif anchor == 'topright': rect.topright = loc
    elif anchor == 'bottomright': rect.bottomright = loc
    elif anchor == 'midtop': rect.midtop = loc
    elif anchor == 'midleft': rect.midleft = loc
    elif anchor == 'midbottom': rect.midbottom = loc
    elif anchor == 'midright': rect.midleft = loc
    elif anchor == 'center':rect.center = loc

    surface.blit(text, rect)


# Resource loading functions
# Source: https://github.com/Mekire/cabbages-and-kings/
def load_all_gfx(directory,colorkey=(255,0,255),accept=(".png",".jpg",".bmp")):
    """
    Load all graphics with extensions in the accept argument.  If alpha
    transparency is found in the image the image will be converted using
    convert_alpha().  If no alpha transparency is detected image will be
    converted using convert() and colorkey will be set to colorkey.
    """
    graphics = {}
    for pic in os.listdir(directory):
        name,ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(directory,pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name]=img
    return graphics

def load_all_sfx(directory, accept=(".wav",".mp3",".ogg",".mdi")):
    """
    Load all sfx of extensions found in accept.  Unfortunately it is
    common to need to set sfx volume on a one-by-one basis.  This must be done
    manually if necessary.
    """
    effects = {}
    for fx in os.listdir(directory):
        name,ext = os.path.splitext(fx)
        if ext.lower() in accept:
            effects[name] = pygame.mixer.Sound(os.path.join(directory,fx))
    return effects

def load_all_music(directory, accept=(".wav",".mp3",".ogg",".mdi")):
    """
    Create a dictionary of paths to music files in given directory
    if their extensions are in accept.
    """
    songs = {}
    for song in os.listdir(directory):
        name,ext = os.path.splitext(song)
        if ext.lower() in accept:
            songs[name] = os.path.join(directory,song)
    return songs

def load_all_fonts(directory, accept=(".ttf", ".otf")):
    """
    Create a dictionary of paths to font files in given directory
    if their extensions are in accept.
    """
    return load_all_music(directory,accept)
