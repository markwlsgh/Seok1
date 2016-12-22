import platform
import  os


if platform.architecture()[0] =='32.bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"




import game_framework
import start_state
import  collision
import title_state
import pico2d

pico2d.open_canvas(425,325)
game_framework.run(start_state)
pico2d.close_canvas()