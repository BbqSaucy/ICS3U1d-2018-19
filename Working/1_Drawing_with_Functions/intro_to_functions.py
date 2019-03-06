import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



# define your draw functions
def draw_cloud():

    arcade.draw_circle_filled(200, 500, 50, arcade.color.ANTIQUE_WHITE)
    arcade.draw_circle_filled(250, 550, 50, arcade.color.ANTIQUE_WHITE)
    arcade.draw_circle_filled(300, 500, 50, arcade.color.ANTIQUE_WHITE)

def draw_rollinghills():
    arcade.draw_circle_filled(50, -50, 300, arcade.color.GREEN)
    arcade.draw_circle_filled(750, -50, 400, arcade.color.GREEN)
    arcade.draw_circle_filled(400, 100, 150, arcade.color.GREEN)

def draw_tree(x_pos, y_pos):

    arcade.draw_rectangle_filled(x_pos, y_pos - 50, 40, 80, arcade.color.BROWN)
    arcade.draw_circle_filled(x_pos, y_pos, 60, arcade.color.APPLE_GREEN)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

   # call your draw functions
    draw_cloud()
    draw_rollinghills()
    draw_tree(400, 250)
    draw_tree(500, 250)
    draw_tree(300, 200)
    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()