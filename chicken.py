#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

speed = 0.05
message = '''Gimme gimme chicken tendies,
Be they crispy or from Wendys.
Spend my hard-earned good-boy points,
on Kid's Meal ball pit burger joints.
Mummy lifts me to the car,
To find me tendies near and far.
Enjoy my tasty tendie treats,
in comfy big boy booster seats.
McDonald's, Hardee's, Popeye's, Cane's,
But of my tendies none remains.

She tries to make me take a nappy,
But sleeping doesn't make me happy.
Tendies are the only food,
That puts me in the napping mood.
I'll scream and shout and make a fuss,
I'll scratch, I'll bite, I'll even cuss!
Tendies are my heart's desire,
Fueled by raging, hungry fire.
Mummy sobs and wails and cries,
But tears aren't tendies, nugs or fries.

My good-boy points were fairly earned,
To buy the tendies that I've yearned.
But there's no tendies on my plate!
Did mummy think that I'd just ate?
"TENDIES TENDIES GET THEM NOW,
YOU FAT, UNGRATEFUL, SLUGGISH SOW!"
I screech while hurling into her eyes,
My foul-smell bowel-dwelling diaper surprise.
For she who is un-pooped on is she who remembers:
Never forget my chicken tenders.'''

sense.show_message(message, speed)
