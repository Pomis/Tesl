# Вы можете расположить сценарий своей игры в этом файле. 

# Объявляйте изображения здесь, используя оператор image.
# например, image eileen happy = "eileen_happy.png"

init python:
    # Слои камеры
    register_3d_layer('background','middle', 'forward')

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
image yuming = "images/yuming.png"
image boat = im.FactorScale("images/boat.png",0.8,0.8)


init:
    # Характеристика игрока
    $ playerName = "гг"
    $ playerFullName = "гг ггхович"
    $ agressionPoints = 0
    $ lazynessPoints = 0
    $ humorousPoints = 0
    
    $ killPoints = 0
    $ spyPoints = 0

    # Логические переменные
    $ brokenFinger = False # Сосед по палате сломал палец
    $ inferno = True # Сценарий Инферно
    $ visitedLab = False # Посетил лабораторию
    $ promisedMarie = False # Обещал Марии заглянуть в лабораторию

    # Статы с девушками
    $ yumingPoints = 0
    $ mariePoints = 0
    $ minoriPoints = 0

    # Отношения с другими персонажами
    $ slavaPoints = 0
    $ gantzPoints = 0

    # Позиции
    $ center = Position(xpos=0.5, xanchor='center', ypos=0.7)
    $ center2 = Position(xpos=0.5, xanchor='center')
    $ bottom = Position(xpos=0.4, xanchor='center', ypos=0.8)

    # Эффекты
    $ flash = Fade(.25, 0, .45, color="#fff")

    # Тестирование
    $  testing = True;


    

# Игра начинается здесь.
label start:

# reset the camera and layers positions and allow layers position to be saved.
    $ camera_reset()
    # It takes 0 second to move layers
    $ layer_move("background", 2222)
    $ layer_move("middle", 1700)
    $ layer_move("forward", 1500)
    if testing==True:
        menu:
            "ch1 - ocean":
                jump ocean
            "ch2 - inferno":
                jump rootInferno
            "ch2 - soldier":
                jump rootSoldier
            "ch3 - warBase":
                jump warBase
            "ch3 - day1":
                jump ch3day1
            "ch3 - day2":
                jump ch3day2
    else:
        jump ocean


                                                                                                                                                                                                                

    return
