# Pong in Pygame
This game is meant to demonstrate the `GameObject` class I am currently working on. Pygame `Sprite`s can be tough to deal with --- for students, figuring out how to use `Sprite`s in a game can be the hardest part of learning the Pygame library. The `GameObject` class abstracts some of the hard work away. Some of its features are inspired by the Sprite object from [p5.play](http://molleindustria.github.io/p5.play/), a JavaScript library.
## GameObject
Check out GameObject.py. I have comments in the code documenting each function. The `GameObject` uses vectors from Vector.py to track position, velocity, and acceleration. The `update()` method should be called once per frame for each `GameObject` instance. (Fun fact: if you put your `GameObject` instances in a group, say `all_sprites`, then you can say `all_sprites.update()` in your game loop to run the `update()` method on each of the sprites in the group!)
## Other Helpful Pygame Functions
I added some functions to the top of pong.py, in the template section of the code, which are useful for making games. The `map_range()` function linearly maps a value from one range to another. The `text()` function can easily draw text on the screen; drawing text is a non-trivial task in Pygame, so check out the source code to see how it works.
## Pre-reqs
Coaches who want to teach their students Pygame using the GameObject class should make sure their students have a good understanding of object-oriented programming, including inheritance. I would recommend Coaches go through the GameObject class to see how it works, and I encourage students to add their own features to GameObject for their games.
## Contact
Email me, Andrew, at adelapo@berkeley.edu. I do Code Coaching on Saturdays!