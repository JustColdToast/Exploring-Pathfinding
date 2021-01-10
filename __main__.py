# Kanwarpal Brar
# This project is intended to explore pathfinding algorithms
# Pyglet is used to provide an interface

import pyglet
import time


# Below are objects required for application
class Player:
    def __init__(self, spriteshape):
        self.sprite = spriteshape
        self.vx, self.vy = 0, 0  # Set the initial velocity of the player object
        self.target = None  # Represents a target which can be set

    def update(self, dt):  # Houses functions responsible for modifying the player
        if self.target is not None:  # if the target exists
            if not ((self.target.x == self.sprite.x) and (self.target.y == self.sprite.y)):
                # Check that the target is not on the player location At this point, I would execute the function to
                # pathfind to the correct location, for now that does not exist
                self.pathfind(dt)

    def move_sprite(self, dt):  # Move the sprite shape
        self.sprite.x += self.vx * dt * 2
        self.sprite.y += self.vy * dt * 2

    def pathfind(self, dt):
        # The pathfind function should manage movement itself
        return

class Wall:  # Represents a wall that the player cannot move through
    def __init__(self, posX, posY, spriteShape):
        self.sprite = spriteShape
        self.sprite.x, self.sprite.y = posX, posY

    def update(self):  # Represents the update function
        # For the wall object there isn't really much to update
        pass

# Useful functions below
def center_image(image):
    if isinstance(image, pyglet.shapes.Circle):
        image.anchor_x = image.radius // 2
        image.anchor_y = image.radius // 2
    else:
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2

    # Resets an image's anchor x,y to be it's center



def update(dt):
    for item in appObjects:
        item.update(dt)  # Updates all objects

def set_target(x,y):  # This function places a target at a specific x-y coordinate
    # Currently, the 600 by 600 space is split into quadrants of 25 x 25 within a 500 x 500
    # For the x-y coordinates, they are rounded to the nearest multiple of 25 in the coordinate space
    x,y = modify_coordinates_to_grid(x,y)
    tar = pyglet.shapes.Circle(x,y, 10, color=(255,51,51), batch=batch)
    center_image(tar)
    player.target = tar

def place_wall(x,y):
    x,y = modify_coordinates_to_grid(x,y)
    rect = pyglet.shapes.Rectangle(x,y, 25, 25, color=(176,176,176), batch=batch)
    center_image(rect)
    walls.append(Wall(x,y,rect))

def modify_coordinates_to_grid(x,y):
    if x < 100:
        x = 100
    elif x > 500:
        x = 500
    if y < 100:
        y = 100
    elif y > 500:
        y = 500
    # The below operation lines the number to the nearest multiple of 25
    x = int(x/25)*25
    y = int(y/25)*25

    return x,y

# Setup screen size for application, as well as the pyglet window. Other setup
screen_width = 600
screen_height = 600
window = pyglet.window.Window(screen_width, screen_height)
pyglet.resource.path = ['../src']
batch = pyglet.graphics.Batch()  # Represents a batch of shapes to be drawn
playCirc = pyglet.shapes.Circle(int(screen_width/2), int(screen_height/2), 15, color=(233,41,41), batch=batch)
center_image(playCirc)
player = Player(playCirc)
walls = []  # represents all the wall objects
appObjects = []  # Represents all objects that need to be updated. Walls don't, so they are excluded




# Below is all the pre-launch setup


# Events an application run
@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    print(player.sprite.position)
    print(x,y)
    # Gets mouse button presses for placing of walls and targets
    if button is pyglet.window.mouse.LEFT:
        place_wall(x,y)
    else:
        set_target(x,y)



pyglet.clock.schedule_interval(update, 1 / 120)  # Movement is checked 120 times a second
pyglet.app.run()  # Starts the pyglet application
