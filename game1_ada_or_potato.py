import arcade

# Constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "INTRODUCTION"
GAME_SPEED = 1/60

TIMER_MAXIMUM = 60

# Map phases
NEXT_PHASE = {
    "Ada": "Potato",
    "Potato": "Ada"
}

class Picture(arcade.Sprite):
    phase: str

    def __init__(self, image: str):
        if image == "alpha":
            super().__init__("images/ada.png")
            self.phase = "Ada"
            self.timer = 0
            self.scale = .5
            self.center_x = WINDOW_HEIGHT / 2
            self.center_y = WINDOW_WIDTH / 2
        if image == "beta":
            super().__init__("images/potato.png")
            self.phase = "Potato"
            self.timer = 0
            self.scale = .1
            self.center_x = WINDOW_HEIGHT / 2
            self.center_y = WINDOW_WIDTH / 2

    def update_timer(self):
        if self.timer < TIMER_MAXIMUM:
            self.timer += 1
        else:
            self.timer = TIMER_MAXIMUM

    def update(self):
        self.update_timer()

class OpenGame(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.logo_list = None
        self.points = 0

    def setup(self):
        arcade.set_background_color(BACKGROUND_COLOR)
        self.logo_list = arcade.SpriteList()
        self.logo_list.append(Picture("alpha"))

    def on_draw(self):
        arcade.start_render()
        self.logo_list.draw()
        arcade.draw_text(str(self.points), 10, 10, arcade.color.ALMOND, 10)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.logo_list[0].phase == "Potato":
            if self.points == 0:
                self.points = 0
            else:
                self.points -= 1
        if self.logo_list[0].phase == "Ada":
            self.points += 1

    def on_update(self, delta_time):
        self.logo_list.update()
        if self.logo_list[0].timer == TIMER_MAXIMUM:
            if self.logo_list[0].phase == "Potato":
                self.logo_list.pop()
                self.logo_list.append(Picture("alpha"))
            elif self.logo_list[0].phase == "Ada":
                self.logo_list.pop()
                self.logo_list.append(Picture("beta"))


def main():
    window = OpenGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()