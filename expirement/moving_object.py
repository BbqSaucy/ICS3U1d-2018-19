import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

def main():
    arcade.open_window(SCREEN_HEIGHT, SCREEN_WIDTH, "moving object")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()

main()