from Life.LifeViewer import *
from Life.LifeGenerator import *
from Life.TurtleViewer import *
import time



#hash = hashlib.md5("whatever your string is".encode('utf-8')).hexdigest()
dic = {}

world = LifeWorld(20, True)
viewer = LifeViewer()
#viewer = TurtleViewer(800, 800)
while world.next_generation():
    _hash = world.get_hash()
    val = dic.get(_hash)
    if val is None:
        dic[_hash] = world.get_generation()
    else:
        break
    viewer.show_world(world,  False, '')
    #    viewer.show_world(world)
    time.sleep(0.01)

legend = ''
print("-------------COMPLETION OF EVOLUTION  {}-----------------".format(world.get_generation()))


if world.get_empty():
    legend = "-------------EXTINCTION IN GENERATION {}-----------------".format(world.get_generation())
else:
    _hash = world.get_hash()
    gen = dic.get(_hash)
    if gen is not None:
        if world.get_generation() - gen == 1:
            legend = "-------------STABLE CONFIGURATION IN GENERATION {}-----------------".format(gen)
        else:
            legend = "-------------REPEAT CONFIGURATION FROM GENERATION {}-----------------".format(gen)

viewer.show_world(world, True, legend)
print(legend)