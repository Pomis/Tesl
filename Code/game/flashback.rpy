#
#   Все флешбеки теперь тут. Вызываются оператором call
#   Почему так будет лучше?
#   Можно будет вызывать одинаковые флешбеки из любого разветвления без копирования кода
#   А также, можно редактировать флешбеки в хронологическом порядке
#

image bg cruise = "images/cruise.png"
image bg cruise crashed = "images/cruise-crashed.png"

label flashback1:
    scene bg ship crashed onlayer background with flash
    "В голове начали вспыхивать образы прошедших событий: мельтешение людей, крики, большой круизный лайнер, накренившийся и объятый огнём, яркие звёзды над головой и холодный ветер."
    #  bulka:Тут должен воспроизвестись файл с криками людей. Будет идеально. Его чуток порезать надо ток.
    "Картинки в моей голове сложились в целое и безысходность начала наполнять мою душу. "
    "\"Этого не может быть.{w} Нет-нет, это сон или всё что угодно, но это не реальность и происходит не со мной\""
    # Фон: палуба корабля
    hide bg onlayer background
    scene bg cruise
    show tonya happy:
        xalign 0.7 yalign 0.5
    sis "— Я никогда не видела столько звёзд на небе!"
    "— Ну конечно, ты всю жизнь не выезжала из Москвы. А сейчас мы где-то между Европой и Африкой..."
    sis "— Да ты тоже!"
    "— Родители уже наверное спят?"
    sis "— После такого количества коктейлей... {w}Боюсь, как бы с ними ничего не произошло. Может, проверим, как они?"
    "Ночную тишину нарушил громкий звук рассекаемого воздуха."
    # Звук взрыва
    "Что-то на огромной скорости врезалось в корабль. От столкновения корабль сильно тряхнуло, а взрыв разделил корабль на две части."
    show bg cruise crashed
    show tonya scared:
        xalign 0.7 yalign 0.5 alpha 1.0
        easeout 2 zoom 0.1
        easeout 1 alpha 0.0 zoom 0.05

    sis "— Бра-а-а-ат! "
    "Повсюду слышались крики."
    
    "Я отчаянно бросился спасать сестру, которая кувырком покатилась вниз."
    return

label flashback2:
    scene bg ship crashed onlayer background with flash
    sis "— Бра-а-а-ат! Помоги-и-и!"
    "Тоня всё сильнее удалялась от меня и вскоре скрылась в морской пучине. Я держался за выступающий  на палубе штырь."
    "Моя часть корабля уже наклонилась на столько, что я висел на этом штыре, почти как на турнике."
    "Прямо подо мной на воду спустили несколько спасательных лодок."
    "Чувство приближающейся смерти заглушило все остальные чувства, и я смог прыгнуть вниз."
    "Я не могу дышать! Я падаю! Зачем!"
    "Упал в воду и погрузился на несколько метров в глубину."
    "Отчаянно барахтаясь я выплыл на поверхность."
    "— Помогите!"
    "Никто даже не обратил на меня внимание, я залез на ближайшую лодку и обессиленно лёг."
    "— Почему именно я?"
    return

label flashback3:
    scene bg ship crashed onlayer background with flash
    "Я один в лодке. Корабль уже погрузился на дно. Кто-то смог спастись на лодках, кто-то нет. У кого-то были даже вёсла. А кто-то барахтается в воде."
    "Не хочу никого спасать. Да и не могу. Ничего не хочу."
    with vpunch
    "В лодку что-то врезалось?"
    g "— Помоги мне забраться!"
    "Что ещё за командный голос? Ещё и женщина. Пусть сама залезает."
    "А она похоже это и собралась делать. Не буду ей мешать."
    "На борт моей лодки забралась какая-то девушка, выловила из воды пару кейсов и отключилась."
    "А я вслед за ней..."
    return
