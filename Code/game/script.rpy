﻿# Вы можете расположить сценарий своей игры в этом файле. 

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


# Определение персонажей игры.
define yu = Character('Юминг', color="#c8ffc8")
define g = Character('Незнакомка', color="#c8ffc8")
# image yuming shamed = "images/yuming-shamed.png"
image yuming shamed = im.FactorScale("images/yuming-shamed.png",0.4,0.4)
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

# reset the camera and layers positions and allow layers position to be saved.
    $ camera_reset()
    # It takes 0 second to move layers
    $ layer_move("background", 2222)
    $ layer_move("middle", 1700)
    $ layer_move("forward", 1200)
    
    scene bg sky ocean onlayer background
    $ camera_move(0, -10000, 0, 0, 0)

    $ camera_moves( ( (160, -10030, 0, 0, 2, 'ease'),(0, -10000, 0, 0, 4, 'ease') ), loop=True)
    play music "music/123.mp3"
    # scene bg sky
    with fade
    "Я открыл глаза. Всего лишь небо и больше ничего. Слепяще белые облака. Ярко голубое пространство, простирающееся на миллиарды километров ввысь."
    "И звук ветра, затихающий и еле заметный. Я мог бы долго так лежать и любоваться красотой бесконечного космического океана, если бы не одна любопытная мысль, пришедшая мне в голову. "
    "\"А где я?\""
    "Хотя впрочем, мысль я особо развивать не стал."
    "Кругом так безмятежно, тихо и спокойно, что глаза сами закрылись. Ничего не мешает поспать ещё часок, разве что солнце припекает, да и покачивает меня почему-то.. опять качнуло. И вдруг я вспомнил."
    with vpunch
    $ camera_move(2500, -8000, 0, 0, 1, 'ease')
    show boat onlayer middle at bottom
    "Так резко вскакивать всё же не стоило: я запутался в каких-то вещах и чуть не упал за борт. "
    $ camera_move(500, -2000, 0, 0, 1, 'ease')
    "Удержав равновесие, я поднял глаза и увидел океан."
    $ camera_moves( ( (660, -2100, 0, 0, 2, 'ease'),(500, -2000, 0, 0, 4, 'ease') ), loop=True)
    "Впереди, слева, сзади — кругом вода. Всё ещё не до конца соображая, я оглядел поверхность на которой стою. "
    "Похоже это лодка. Большая старая деревянная лодка. В фильмах на таких спасаются люди, когда тонут корабли. Наш похоже как раз затонул. "
    $ camera_move(0,0,400,0,0)
    hide boat onlayer middle
    scene bg ship crashed onlayer background with flash
    "В голове начали вспыхивать образы прошедших событий: мельтешение людей, крики, большой круизный лайнер, накренившийся и объятый огнём, яркие звёзды над головой и холодный ветер."
    "Картинки в моей голове сложились в целое и безысходность начала наполнять мою душу. "
    "\"Этого не может быть. нет-нет, это сон или всё что угодно, но это не реальность и происходит не со мной\""
    scene bg sky ocean onlayer background
    show boat onlayer middle at bottom
    $ camera_move(500, -2000, 0, 0, 0)
    $ camera_moves( ( (660, -2100, 0, 0, 2, 'ease'),(500, -2000, 0, 0, 4, 'ease') ), loop=True)
    "Но внезапная волна, окатившая меня с головы до ног, смыла все мои мысли и пробудила от оцепенения. Надо что-то делать. Ведь я всё ещё жив."
    
    "Один я. Один океан. Кто кого? Я отбросил эти мысли и решил осмотреться."
    "Меня немного удивило, что лодка была завалена всяким барахлом, и при этом на ней был только я."
    "\"Обычно спасают людей, а не ценный груз. Но мне же лучше, может найду что поесть\"."
    "Однако надеждам моим не суждено было сбыться, на лодке были несколько кейсов с кодовыми замками, которые никак не открыть, валялась всякая одежда, парочка спасательных жилетов."
    "Никакой аптечки, никаких пайков. Словом, ничего, что могло бы пригодиться в экстремальной ситуации. Как-будто этот плот вообще не рассчитан на спасение людей." 
    "Ну и зачем он тогда? Я даже был немного возмущён, хотя, конечно, просто пытался таким образом подавить возросшую панику. "
    "Шансы на выживание таяли. Нет даже ракетницы, меня не заметят, если будут искать."
    "Прохаживаясь по палубе своего, похоже, последнего корабля, я задел что-то ногой. Из-под навеса торчал странный согнутый предмет, похожий на сапог." 
    "Я наклонился и попытался вытащить его, как вдруг понял, что это чья-то нога. Я не один."
    
    "Нога торчала из кучи барахла, состоящего из чемоданов, кейсов и прочего бесполезного в моей ситуации мусора."
    "Я начал раскидывать эту гору хлама, чтобы спасти того, кто был под ней. Спустя минуту упорного труда, я смог увидеть владельца ноги, точнее то, во что он был одет."
    "Это был странного вида скафандр, будто бы попавший сюда из какого-то фильма про пришельцев. "
    "Он был серого цвета, а шлем имел отражающую поверхность, что мешало увидеть лицо владельца этого странного костюма. "
    "Вдоль всего тела были странные твёрдые трубки, соединённые между собой гибкими трубками потоньше. Кажется, я видел в интернете что-то похожее."
    # "Точно! Это называется экзоскелет. На да ладно, бог с этим экзоскелетом - что с человеком внутри. "
    "По идее, шлем в таких костюмах закрепляется либо электромагнитами, либо механически с помощью вращательного движения. "
    "В первом случае я не имел шансов его снять, но если же он закреплен вручную, то проблем быть не должно. Одно движение, щелчок и готово - шлем отделился от остального костюма. "
    "Я начал потихоньку снимать шлем и через несколько секунд передо мной предстало лицо молодой девушки, на вид лет 16.\""
    show yuming shamed onlayer forward at center
    with dissolve
    "Любопытство мгновенно заглушило все мои страхи, я откинул навес и удивлённо уставился на того, кто был под ним."
    "Это определённо был человек, судя по комплекции даже наверно ребёнок, но вот одежда.. Вернее, одеждой это не назовёшь. Какой-то серый водолазный костюм с навешанной на него электроникой."
    "Но что это за шлем? Нет, это точно не водолазный костюм, слишком он странный, да и зачем дайверам сапоги?"

    "Я так увлёкся, разглядывая костюм, что не сразу подумал, что, возможно, ей нужна помощь. Что я могу сделать? Наверно, нужно снять с неё шлем. "
    "Это я и решил попробовать, но как только я протянул руки к шлему, девушка вдруг метнулась в сторону и мгновение спустя я лежал и смотрел как хрупкое создание вдруг превратилось в доминирующий вид и на нашем плоту произошла маленькая революция."
    # show yuming shamed with dissolve
    "Направленный на меня предмет я заметил не сразу, но в том что это оружие я не сомневался. Я посмотрел бы ей в глаза но мешал непрозрачный шлем. На несколько секунд наступило мёртвое молчание."

    with dissolve
    "-Ээм... привет.. то есть хэллоу, айм э френд"

    "Но похоже какой-то эффект всё-таки был, девушка сменила стойку и чуть опустила оружие."
    "Я смог повнимательнее осмотреть её костюм. Облачение моей пленительницы  выглядело немного футуристично, и было цельным, никаких замков я не разглядел. "
    "\"Странно это всё\" - подумал я и тут же осознал что мысли мои как-то совсем не соответствуют ситуации. И в этот момент она подняла одну руку и сняла шлем."

    "— Чего уставился?"
    "— Эмм... Просто ты мне кое-кого напомнила... Ну, одну знакомую... Не важно. Кто ты такая? И что это за хреновина на тебе?"

    # show yuming shamed with vpunch
    "И снова получил по голове. Незнакомка тяжело дышала, да и вообще, выглядела, мягко говоря, потрёпанно. Но это ничуть не смущало её, да и за что она меня всё время бьёт? "
    "Да и разве можно так с незнакомым человеком? Да что с ней не так? Она села и отвернулась от меня, смотря на горизонт произнесла:"

    g "— Ну ты и болван! У нас захватили исследовательскую платформу, а ты хнычешь о своих знакомых."
    "Яростный тон сменился на расстроенный. Будто бы, воспоминания только сейчас ударили ей в голову. Я, тем временем, совсем сбился с толку. Понимая, что заново озвучивать предыдущие вопросы бессмысленно, я только спросил её имя:"

    "— Имя-то у тебя есть, чудачка? "
    "Она проигнорировала насмешку в моём голосе и спокойно ответила"
    yu "Меня зовут Юминг. Товарищи называют меня Юми, но ты можешь называть меня только госпожа Юминг. — она рассмеялась. — Шучу, конечно. А ты кто такой, и как сюда попал?"


    menu:
        "Думаю, тебе это лучше известно!":
            $ agressionPoints += 1
            $ yumingPoints -= 1
            "— Как я сюда попал? Думаю, тебе это лучше известно! Я в кои-то веки получил отпуск и отправился в круизное путешествие... А потом произошло кораблекрушение, я помню взрывы. Наш корабль явно кто-то затопил! Твоя работа? "
        "Кажется, наш корабль взорвался...":
            "— Кажется, наш корабль взорвался... Я помню только яркие вспышки света и панику."


    "Юминг повернула голову в мою сторону. "

    # Грубый ответ Юминг
    if yumingPoints < 0:
        yu "— Тебе-то какое дело? Радуйся, что выжил! — она внимательно осмотрела меня. — Лучше придумай, как нам попасть на сушу. Ты хотя бы примерно понимаешь, где мы сейчас находимся?"
    # Сюда нужен негрубый ответ
    else:
        yu "— И что нам теперь делать?"

    "Тем временен моё внимание привлекло то оружие, которым она мне угрожала. Может, если удастся выхватить его, она станет чуток учтивее? Да и очень уж любопытно, что это за штуковина такая. "
    "Оружие лежало на коленях Юминг, осталось дождаться момента, когда она снова отвернётся в сторону моря. Тогда я без особого труда схвачу его за рукоятку. "
    "—А? Я задумался, о чём ты там говорила?"
    "Только я это произнёс, как понял, что сейчас снова получу по голове. Но удара не последовало, она фыркнула и отвернулась."
    "Я выхватил её странное оружие и онемел от удивления. Я чувствовал устройство этого оружия, понимал, как оно работает, оно, как будто, стало продолжением меня. А ещё я понял, что стрелять оно явно не умеет. Скорее, это какой-то передатчик."
    "Похоже, что вмятина на корпусе лишила его способности работать. Юминг сначала набросилась на меня, но заметила моё оцепенение."

    yu "—Да ладно? Только не говорите мне, что двое \"способных\" умрут от голода и жары?"
    yu "—И да, это была глубоководная рация."
    yu "—Нам нужно попасть на военную базу. Сможешь починить эту хреновину? В этих ящиках должен быть ремонтный набор."
    "Юминг окинула взглядом разбросанные по лодке кейсы."
    "Я всё ещё был в оцепенении и не понимал, что происходит. О чём она говорит, какой ремонтный набор?"

    "—Что это за штуковина?"

    yu "—Это глубоководный передатчик. Починишь его, и нас спасут. А ну, за дело!"
    "В её голосе снова появились командные нотки"
    yu "— Судя по всему, у тебя есть редкая способность управлять таким оборудованием. Я не сильна в этом, тебе всё подробно объяснят на военной базе. "

    "—Так... Стоп! Да кто ты такая, расскажи уже наконец!"
    yu "—Ну... раз мы с тобой в одной лодке, уже во всех смыслах, то нет смысла скрывать. Я пилот подводной охранной машины. Мы уже три года воюем с иной цивилизацией — Инферно. Никто пока не знает, откуда они появились, и зачем... Одно мы знаем точно — они хотят нас уничтожать. Медленно и цинично."

    "—Что? Какой ещё подводная охрана? Какое Инферно? Сама-то в это веришь?"
    "Я осмотрел её странный костюм, передатчик, и сказанное ею приобретало какой-то смысл."
    "— А с чего всё началось? "

    yu "—С того, что эти западные учёные случайно взорвали один из городов Инферно..."
    menu:
        "Как можно было случайно взорвать город?":
            $ agressionPoints += 1
            "Я уже терял самообладание."
            "—Я сама толком не знаю... Да и это не важно. С тех пор они нападают на нас. Давай, выберемся отсюда, и тебе всё расскажут. Почини только эту штуку..."
        "Впервые слышу об этом... Расскажи больше!":
            $ yumingPoints += 1
            show yuming smiled
            "Юминг едва заметно улыбнулась."
            "—Я сама мало что знаю... Давай, выберемся отсюда, и тебе всё расскажут. Почини только эту штуку..."
    "—А как ты поняла, что можешь управлять таким оборудованием?"
    if agressionPoints > 0:
        yu "—Да сколько можно спрашивать?? Ну ладно..."
    yu "Всех, кто моложе 25 лет в нашей провинции проверяли на какой-то там вирус... Но на самом деле проверяли нашу совместимость с этими разработками. "
    yu "Ну и после эксперимента со мной сразу же связались военные. Выбора у меня особого не было, да и оставаться в своём обедневшем поселении мне не хотелось."
    yu "Всё, хватит. Чини!"
    if agressionPoints>1:
        menu:
            "Зачем мне это делать?":
                $ agressionPoints += 1;
                jump rootInferno
            "—Хм... Ладно, попробую. С чего начать?":
                jump rootSoldier
    else:
        "—Хм... Ладно, попробую. С чего начать?"
        jump rootSoldier

                                                                                                                                                                                                                

    return
