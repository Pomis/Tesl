# Вы можете расположить сценарий своей игры в этом файле. 

# Объявляйте изображения здесь, используя оператор image.
# например, image eileen happy = "eileen_happy.png"

init python:
    # Слои камеры
    register_3d_layer('background', 'middle', 'forward')

# Определение сцен
image bg ocean = "images/ocean.jpg"
image bg sky = "images/sky.jpg"
image bg sky ocean = "images/sky-ocean.jpg"
image bg ship crashed = "images/ship-crashed.jpg"
image bg bus = "images/0575_BG35_BB.png"
image bg hospital room day = "images/012_BG_005A.jpg"
image bg hospital room sunset = "images/013_BG_005B.jpg"
image bg hospital reg = "images/rega.jpg"
image bg hospital = "images/buildings_107.jpg"

# Определение персонажей игры.
define yu = Character('Юминг', color="#c8ffc8")
define g = Character('Незнакомка', color="#c8ffc8")
image yuming shamed = "images/yuming-shamed.png"
image yuming angry = "images/yuming-angry.png"
#image yuming shamed = im.FactorScale("images/yuming-shamed.png",0.4,0.4)
image yuming stupid = "images/yuming-stupid.png"
image yuming sleepy = "images/yuming-sleeping.png"
image yuming smiled = "images/yuming-smiled.png"
image boat = im.FactorScale("images/boat.png",0.8,0.8)


init:
    # Характеристика игрока
    $ agressionPoints = 0
    $ lazynessPoints = 0
    $ humorousPoints = 0
    $ brokenFinger = False
    $ inferno = True

    # Статы с девушками
    $ yumingPoints = 0

    # Позиции
    $ center = Position(xpos=0.5, xanchor='center', ypos=0.7)
    $ bottom = Position(xpos=0.4, xanchor='center', ypos=0.8)

    # Эффекты
    $ flash = Fade(.25, 0, .45, color="#fff")
    

# Игра начинается здесь.
label start:

    jump ocean
                                                                                                                                                                                                                

    return
