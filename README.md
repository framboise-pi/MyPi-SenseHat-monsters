# MyPi SenseHat Monsters
<h3>USAGE EXAMPLE:</h3>
<code>
<br>
from sense_hat import SenseHat
from mpsm import *
<br>
sense = SenseHat()
DisplayOneRandomMonster(sense)
</code>
<br>
<small>>>> to add a random-colored background:</small>
<code>DisplayOneRandomMonster(sense, True)</code>
<br>
<h3>and for a non-random-colored</h3>
<code>
<br>
from sense_hat import SenseHat
from mpsm import *
<br>
background = (255,0,0)
foreground = (255,255,255)
other = (0,0,0)
<br>
sense = SenseHat()
DisplayOneRandomMonsterWithMyColors(sense, background, foreground, other)
</code>
<br>
<br>
Duotones pixelarts are colored-made this way:
<ul>
  <li>background is for the background color</li>
  <li>foreground is the duotone monster main color</li>
  <li>other is the duotone monster secondary color (eyes, accessories,...)</li>
</ul>
