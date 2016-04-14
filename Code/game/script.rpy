# Вы можете расположить сценарий своей игры в этом файле. 

# Объявляйте изображения здесь, используя оператор image.
# например, image eileen happy = "eileen_happy.png"

init python:
    # Слои камеры
    register_3d_layer('background','middle', 'forward')
    # Автоподгрузка изображений
    import os
    def define_characters(characterImageFolder, excludeFirstXFolders=0, flip=True):
        for path in renpy.list_files():
            if path.startswith(characterImageFolder + "/"):
                path_list = path.split("/")
                path_list[-1] = os.path.splitext(path_list[-1])[0]
                path_list = tuple(path_list[excludeFirstXFolders:])
                renpy.image(path_list, path)
                if flip:
                    renpy.image(path_list + ("flip", ), im.Flip(path, horizontal=True))
    define_characters("images", 1, False)



# Определение персонажей игры.
define yu0 = Character('Азиатка', color="#a78ddf")
define yu = Character('Юминг', color="#a78ddf")
define g = Character('Незнакомка', color="#a78ddf")
define sis = Character('Тоня', color='#d27a1c')
define co0 = Character('Парень со странной причёской', color="#c8ffc8") # Координатор до знакомства
define co = Character('Координатор', color="#c8ffc8")
define nn2 = Character('sa2', color="#c8ffc8")
define mi = Character('Минори', color="#fbc072")
define man = Character('Чувак', color="#c8ffc8")
define sl = Character('Слава', color="#c8ffc8")
define pav0 = Character('Пухлый парень', color='#baae93')
define pav = Character('Павел', color="#baae93")
define ten = Character('Тенко', color='#8c8c8c')
define en = Character('Энлиль', color='#0eb305')
define es = Character('Эсхалия')
define ra = Character('Голос из рации', color="#e4e4e4")
define pi0 = Character('Пилот вертолёта', color="#e1e4e1")
define pi = Character('Иван', color="#e1e4e1")
define ma = Character('Мария', color="#faf0b8")
define sl = Character('Слава', color="#faf0b8")
define stranger = Character('Странный', color="#8c8c8c")
define str_nvl = Character('Странный', color="#8c8c8c", kind=nvl)
# bulka: Цвет можно заменить, просто скопировал, имя временное, пока не придумал
define golos = Character('Голос', color="#f8349f")
define regf = Character('Офицер', color="#f8349f")
define nvlc = Character('', kind=nvl)
define alil0 = Character('Надоедливый самозванец', color="#c8ffc8")
define alil = Character('Алулим', color="#c8ffc8")
define ush = Character('Уш', color="#c8ffc8")
define usa = Character('Военнослужащий США', color="#c9ffc8")
define sa = Character('Саргон')
define port = Character('Портальщик')
define isc0 = Character('Длинноволосая')
define isc = Character('Искра')

# Спрайты персонажей

# Плейсхолдеры

image slava smiling = "images/placeholder/boy.png"
image slava serious = "images/placeholder/boy.png"
image slava laughing = "images/placeholder/boy.png"

image gantz serious = "images/placeholder/tall.png"

image tenko = "images/placeholder/boy.png"
image tenko thinking = "images/placeholder/boy.png"

image pavel tired = "images/placeholder/boy.png"
image pavel afraid = "images/placeholder/boy.png"

image ush serious = "images/placeholder/tall.png"

image alil bored = "images/placeholder/tall.png"
image alil serious = "images/placeholder/tall.png"


#image yuming shamed = im.FactorScale("images/yuming-shamed.png",0.4,0.4)
image yuming = "images/yuming.png"
image yuming night = im.MatrixColor("images/yuming.png",im.matrix.tint(0.4, 0.4, 0.6))

# Разное
image point = "images/point.png"
image boat = im.FactorScale("images/boat.png",0.8,0.8)
image text start = Text("{cps=18}{size=28}{color=#92f8ff}2049 год. Июнь. Где-то в Средиземном море. {/color}{/size}{/cps}", slow=3)
image text zumwalt = Text("{cps=18}{size=28}{color=#92f8ff}В это же время. Где-то в Тихом океане.{/color}{/size}{/cps}", slow=3)


init:
    # Характеристика игрока
    $ playerName = "Грег"
    $ playerFullName = "Грег Гильдин"
    $ agressionPoints = 0
    $ lazynessPoints = 0
    $ humorousPoints = 0
    $ negativePoints = 0 # Разочарование в Инферно.
    # bulka: Изначально планировалось, что это к нему отношение Инферно какое иметь будет. Хотя не уверен. Надо бы эти ифки с агрессией заменить на менюшки, ибо как-то не комильфо, что из-за выбора нагрубить или нет в первой/второй главе все меняется абсолютно.
    $ killedPeopleCount = 0 # Количество людей, убитых гг
    $ antiTenkoPoints = 0 # bulka: Эти пойнты означают качество противостояния Тенко и ответа на его действия. Они не означают положительное/негативное отношение к нему.
    $ tenkoAttention = 0  # Подозрение Тенко по поводу убийства Юминг. 1 - смутные подозрения 2 - конкретные подозрения 3 - уверенность. По игре понадобяться в Инферно руте, когда гг встретиться со Славой.
    # bulka: Скорее всего уникальная переменная для рута Инферно. Вряд ли пригодится в солдатском руте.
    
    # Названия, которые могут подвергнуться редактуре.
    $ cityName = "Златогномск"

    # Очки, влияющие на качество выполнения действий, требующих специальных знаний
    $ gunPoints = 0 # Умение обращаться с оружием
    $ spyPoints = 0 # Умение подслушивать, воровать, следить
    $ liePoints = 0 # Умение врать, льстить
    $ leadershipPoint = 0 # Навык лидерства, убедительность отдаваемых приказов, уверенность высказываний

    # Логические переменные
    $ chesspoints = False # bulka: Я просто заебался работать с этими условиями для одного выражения. Рабочая переменная. Символизирует признание уровня игры.    
    $ brokenFinger = False # Сосед по палате сломал гг палец
    $ inferno = False # Сценарий Инферно
    $ visitedLab = False # Посетил лабораторию
    $ promisedMarie = False # Обещал Марии заглянуть в лабораторию
    $ withMarieInHangar = False # Вместе с Марией в ангаре
    $ stolenFlash = False # Украл флешку из лаборатории
    $ heardAboutTitan = False # Слышал о титанах до лекции в классе
    $ wantToAskAboutSignal = False # Хочет спросить Марию о сигнале на передатчике
    $ knowYumingRoom = False # Знает комнату Юминг.
    $ visitedYumingRoom = False # Был в комнате Юминг
    $ playedChess = False # Играл в шахматы с Тенко
    $ seenChessGame = False # Видел, как Тенко играет в шахматы
    $ usedDirectRadio = False # Уже использовал передатчик с нейроинтерфейсом
    $ wonchess = False # результат игры
    $ useless = False # Очередная переменная для избежания сотни условий (pomis: опять же, странное название) (bulka: первое что пришло в голову. Юзлесс, ибо, скорее всего, одноразовая. Если что, то с помощью нотпада++ можно будет сразу везде заменить.)
    $ knowTenkoName = False # ГГ уже знает имя Тенко. 
    $ withMinoriOnZumwalt = False # Зачищает помещения Zumwalt вместе с Минори
    $ ushWonded = False # Уш ранен из пистолета
    $ pickedManipulator = False # подобрал манипулятор сознанием
    $ neutral = False # отношение юминг в доп главе.
    $ marieJoke = False # шутка марии в доп главе
    $ PavelHelp = False # способ узнать инфу от павла
    $ tenkoInterested = False # Тенко заинтересовался в случае с кораблём. Возможно, эта переменная будет задействована при переходе из Инферно в рут людей. Изначально создал её, чтобы выбор влиял хоть сколько-то.
    $ PavelHelped = False # Вылазил ли Павел из вентиляции
    $ knowIvanName = False # Знает имя пилота вертолёта.
    $ wantToDrink = False # Согласился отметить победу со Славой.
    $ walkedWithSlava = False # Прогулялся со Славой по городу.
    $ underVine = False # Под вином или протрезвел от него
    $ enlilHasFood = False # У Энлиль есть еда (купила пирожки или стырила батоничики)

    # Жив ли персонаж
    $ yumingAlive = True # Я так понимаю, будут возможны переходы из солдатского рута в Инферно, то есть, возможна ситауация, когда игрок в руте Инферно, а юминг жива, так что, эта переменная пригодится.
    $ jorikAlive = True
    $ slavaAlive = True
    $ ushAlive = True
    $ minoriAlive = True
    $ tenkoAlive = True # bulka: И сей строчкой я лишаю его бессмертия, коим он был наделен с рождения по праву сына божьего... Ой, кажется, это из другой поэмы.

    # Статы с девушками
    $ yumingPoints = 0
    $ mariePoints = 0
    $ minoriPoints = 0
    $ iscraPoints = 0

    # Отношения с другими персонажами
    $ slavaPoints = 0
    $ gantzPoints = 0
    $ strangerPoints = 0

    # Позиции
    $ center = Position(xpos=0.5, xanchor='center', ypos=0.7)
    $ center2 = Position(xpos=0.5, xanchor='center')
    $ bottom = Position(xpos=0.4, xanchor='center', ypos=0.8)
    $ left2 = Position(xpos=0.1, ypos=1.1)

    # Эффекты
    $ flash = Fade(.25, 0, .45, color="#fff")
    $ bloodrage = Fade(.25, 0, .45, color="#f00")

    # Тестирование
    $ testing = True;


    # Imagedissolve Transitions. 
    $ opening = ImageDissolve("images/eye.png", 0.8, 8) 
    $ closing = ImageDissolve("images/eye.png", 0.8, 8, reverse=True) 

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
            "ch3 - day0":
                jump warBase
            "ch3 - day1":
                jump ch3day1
            "ch3 - day2":
                jump ch3day2
            "ch4 - day0":
                jump ch4
            "ch4 - day1":
                jump ch4day1
            "ch5enlil":
                jump ch5enlil
    else:
        jump ocean


                                                                                                                                                                                                                

    return
