AdventureGame
=============

Project 3  for Game Programming class

Part 3: Teleporters, Followers, and Tokens.
 
Teleporters are MobileThings that allow the Player to jump to different parts of the map. They can also teleport themselves.
Tokens are used to gain followers. The Player can give a token to a Person and that Person becomes a follower of the Player.
Followers lose most useful functionality of their previous Class and follow the Player around. They pick stuff up along the way and their primary function is to be as annoying as possible.
 
To get these Classes to work we had to do many overall modifications.
For example, the Clock need to have a way of removing functions from the register because Followers lose much of their previous Class's functionality. 
The use Teleporter function takes as input the room that the Player wants to be sent to so we needed our act function in verbs.py to take this into account.
Teleporters teleport themselves around and can leave the Player's inventory
