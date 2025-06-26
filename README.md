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
rouge = (255,0,0)
blanc = (255,255,255)
vide = (0,0,0)
<br>
sense = SenseHat()
DisplayOneRandomMonsterWithMyColors(sense, rouge, blanc, vide)
</code>
