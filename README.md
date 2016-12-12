# Chompy - (Chomp Game)

Chomp is a two-player strategy game played on a rectangular chocolate bar made up of smaller square blocks (cells). The players take it in turns to choose one block and "eat it" (remove from the board), together with those that are below it and to its right. The top left block is "poisoned" and the player who eats this loses.

Chomp is a special case of a poset game where the partially ordered set on which the game is played is a product of total orders with the minimal element (poisonous block) removed.

Example game

#### This is the initial state

         0 1 2 3 4 5
        ------------
     0 | p c c c c c
     1 | c c c c c c
     2 | c c c c c c
     3 | c c c c c c
     
#### Player 1 move 3,5

         0 1 2 3 4 5
        ------------
     0 | p c c c c c
     1 | c c c c c c
     2 | c c c c c c
     3 | c c c c c x
     
#### Player 2 move 0,2

         0 1 2 3 4 5
        ------------
     0 | p c x x x x
     1 | c c x x x x
     2 | c c x x x x
     3 | c c x x x x

#### Player 1 move 2,0

         0 1 2 3 4 5
        ------------
     0 | p c x x x x
     1 | c c x x x x
     2 | x x x x x x
     3 | x x x x x x
     
#### Player 2 move 0,1

         0 1 2 3 4 5
        ------------
     0 | p x x x x x
     1 | c x x x x x
     2 | x x x x x x
     3 | x x x x x x
     
#### Player 1 move 1,0

         0 1 2 3 4 5
        ------------
     0 | p x x x x x
     1 | x x x x x x
     2 | x x x x x x
     3 | x x x x x x
     
Game Over! Player 1 won this game!

Source: [Chomp](https://en.wikipedia.org/wiki/Chomp)
