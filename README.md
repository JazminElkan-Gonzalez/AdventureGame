AdventureGame
=============

Project 3  for Game Programming class
By Alex Adkins and Jazmin Gonzalez-Rivero

Part 3: Teleporters, Followers, and Tokens.
 
Teleporters are MobileThings that allow the Player to jump to different parts of the map. They can also teleport themselves.
Tokens are used to gain followers. The Player can give a token to a Person and that Person becomes a follower of the Player.
Followers lose most useful functionality of their previous Class and follow the Player around. They pick stuff up along the way and their primary function is to be as annoying as possible.
 
To get these Classes to work we had to do many overall modifications.
For example, the Clock need to have a way of removing functions from the register because Followers lose much of their previous Class's functionality. 
The use Teleporter function takes as input the room that the Player wants to be sent to so we needed our act function in verbs.py to take this into account.
Teleporters teleport themselves around and can leave the Player's inventory

Feedback:
This project was fun to work on, had plenty of room for exploration and creativity. The only problem is we ran out of time at the end because of parents weekend. That being said the time given for the project was sufficent. 


Example of Teleporter working
=============================

What is thy bidding? use Telepro! Riccardo-Office

Blubbering-Fool says -- I fiddle with the buttons on Telepro!
Blubbering-Fool says -- Oh no. What's That Rumbling Sound???
POOF
Blubbering-Fool says -- AAAAAAHHHHHHHHHHHHHH
Telepro! says -- You are now in Riccardo-Office
Telepro! says -- Thank you for using Telepro!. Have a nice day! If you experience any discomfort, such as missing atoms, please contact Olin Corp.

Example of teleporter teleporting itself
=======================================================================

(At Academic-Center-113 Telepro! says -- Poof!)
(At Dining-Hall Telepro! says -- Whoosh!)

Example of Follower Working
=======================================================================


You are in Oval
Smack in the center of Olin College.
You see: handy-radar, token, lovely-trees, grass, cs-book, math-book, FlipFlap,
done-hw-7
You see: Storm-Bringer, Trogdor, Gollum
Your inventory is empty
Exits: west, east, north, south
 
What is thy bidding? take token
 
**Blubbering-Fool says -- I take token
 
What is thy bidding? give token Trogdor
 
Blubbering-Fool says -- I drop token
Trogdor says -- Thanks, Blubbering-Fool
Blubbering-Fool says -- Trogdor has become my follower!
Trogdor says -- Yay... I'm Blubbering-Fool's follower.**
 
What is thy bidding? west
 
Blubbering-Fool moves from Oval to Academic-Center-First-Floor
Blubbering-Fool says -- Hi Frankie-Freshman
The clock ticks 1
Joe-Junior says -- Hi Frankie-Freshman, Blubbering-Fool
**Blubbering-Fool says -- Finally, I've left Trogdor behind!**
------------------------------------------------------------
You are in Academic-Center-First-Floor
Where dreams go to die.
The room is empty
You see: Frankie-Freshman, Joe-Junior
Your inventory is empty
Exits: east, north
 
What is thy bidding? wait

Example of Someone other than the main player trying to take the token
=======================================================================

You see: token, lovely-trees, grass, FlipFlap
You see: Trogdor
Your inventory is empty
Exits: west, east, north, south

What is thy bidding? wait

The clock ticks 32
FlipFlap moves from Oval to Babson-College
Sophie-Sophomore says -- Hi Blubbering-Fool, Trogdor
Sophie-Sophomore reaches for the Token but before be can reach it it mysteriously disappears
Joe-Junior says -- Hi Blubbering-Fool, Trogdor, Sophie-Sophomore
Joe-Junior says -- I take math-book
------------------------------------------------------------
You are in Oval
Smack in the center of Olin College.
You see: lovely-trees, grass
