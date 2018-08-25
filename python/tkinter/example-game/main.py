"""
JumpyGuy: An Example Tkinter Canvas Game

Requirements:
    Keyboard input
    Game loop
    Gravity
    Splash Screen, play button
    Score
    Save data to text file
"""

import tkinter as tk
import GameObjects
from Vector import Vector
from random import randint


class Game(tk.Canvas):
    def __init__(self, master, **kwargs):
        tk.Canvas.__init__(self, master, width=600, height=800, bg="#a3c6ff", **kwargs)
        self.master = master

        self.width = int(self.cget("width"))
        self.height = int(self.cget("height"))

        self.mode = "splash"

        self.player = GameObjects.Player(self.width / 2, self.height / 2, 74, 100, "assets/player.gif")
        self.player.velocity.y = -20

        self.platforms = []

        self.keys_down = set()

        self.master.bind("<KeyPress>", self.handle_key_press)
        self.master.bind("<KeyRelease>", self.handle_key_release)

        self.game_loop()

    def handle_key_press(self, event):
        self.keys_down.add(event.keysym)

        if self.mode == "splash":
            self.start_game()

    def handle_key_release(self, event):
        try:
            self.keys_down.remove(event.keysym)
        except KeyError:
            pass

    def key_is_down(self, keysym):
        return keysym in self.keys_down

    def splash_screen(self):
        # Title
        self.create_text((self.width / 2, 100), text="JumpyGuy!", font=("Comic Sans MS", 32, "bold"))
        self.create_text((self.width / 2, 200), text="Press any key to continue.", font=("Comic Sans MS", 16, "bold"))

        # TODO: High scores

    def start_game(self):
        # Runs once at beginning of game
        for i in range(10):
            new_platform = GameObjects.get_new_platform(self)
            self.platforms.append(new_platform)

        self.mode = "game"

    def play_game(self):
        # The primary loop for gameplay
        self.player.update()
        self.player.position.y = self.height / 2

        self.create_rectangle((0, 0, 20, 20), fill="red")

        for platform in self.platforms:
            if platform.position.y > self.height + platform.height / 2:
                self.platforms.remove(platform)
                self.add_platforms()
            else:
                platform.velocity.y = -1 * self.player.velocity.y
                platform.update()
                platform.draw(self)

        self.player.draw(self)

        if self.key_is_down("Left"):
            self.player.velocity.x = -20
        elif self.key_is_down("Right"):
            self.player.velocity.x = 20
        else:
            self.player.velocity.x = 0

        # Gravity
        gravity_vector = Vector(0, 1.5)
        self.player.velocity.add(gravity_vector)

        # Collision (only if player is falling down)
        if self.player.velocity.y > 0:
            for platform in self.platforms:
                if self.player.check_collide(platform):
                    # BOUNCE
                    self.player.velocity.y = -35

    def add_platforms(self):
        new_platforms = []
        num_new_platforms = randint(1, 1)
        print(num_new_platforms)
        while len(new_platforms) < num_new_platforms:
            platform = GameObjects.get_new_platform(self)
            platform.position.y -= self.width
            collides = False
            for p in self.platforms:
                if platform.check_collide(p):
                    collides = True
            if not collides:
                new_platforms.append(platform)

        self.platforms += new_platforms

    def game_over(self):
        # The game over loop
        print("GAME OVER")

    def game_loop(self):
        # The loop to run them all, and in the darkness bind them
        self.delete("all")

        if self.mode == "splash":
            self.splash_screen()

        elif self.mode == "game":
            self.play_game()

        self.after(40, self.game_loop)  # 25 FPS


root = tk.Tk()
root.title("JumpyGuy")
game = Game(root)
game.pack()
root.mainloop()

