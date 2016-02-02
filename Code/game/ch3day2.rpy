init:
    image bg hangar ships = "images/hangar-ships.png"
    image bg poligon tir = "images/poligon-tir.png"
    image bg laba front = "images/laba-front.png"
    image bg laba back = "images/laba-back.png"
    image bg laba opened = "images/laba-opened.png"
    image bg zumwalt coords = "images/zumwalt-coords.jpg"
    image marie scaled smiling = im.FactorScale("images/marie-smiling.png", 0.26, 0.26)
    image marie scaled shamed = im.FactorScale("images/marie-shamed.png", 0.26, 0.26)
############## Происходит в первую очередь ###################
label ch3day2:
    co "— РОТА ПОДЪЁМ!"
    "Ох... Моё тело. {w}Почему всё так болит?"
    co "— Через 15 минут чтобы все были в учебной аудитории!"
    sl "— Так точно!"
    "Этот Слава просто светится энергией. Мне бы так..."
    if lazynessPoints>0:
        "Может, немного поспать?"
    # bulka: Эти пойнты надо откуда-то взять. Я их, вроде, не видел ещё.
    "Неспешными движениями я привёл себя в порядок."
    "Мой сосед уже вышел из комнаты, а я плетусь как овощ. Может, не пойти сегодня?"
    if promisedMarie == True:
        "Да и я обещал Марии заглянуть в лабораторию..."
    scene bg lift
    "Я сам не заметил, как зашёл в лифт."
    "Приложил палец к сканеру отпечатков."
    # Пока без тира.
    $ result = renpy.imagemap("images/karkas.jpg", "images/karkas-hover.jpg", [(437, 452,520,540, "tir"), (506, 257, 610,388, "classes"), (699, 326, 870, 605, "hungar"), (514, 604, 666, 693, "lab")], focus="imagemap")
    # $ result = renpy.imagemap("images/karkas.jpg", "images/karkas-hover.jpg", [(506, 257, 610,388, "classes"), (699, 326, 870, 605, "hungar"), (514, 604, 666, 693, "lab")], focus="imagemap")

    if result == "tir":
        scene bg poligon
        "Тир, значит. Как же это название не подходит этому помещению."
        "На этот раз тут здесь было не так людно. Всего лишь один человек кроме меня. Паренёк, лет 20, пухленький."
        show pavel tired at right
        "Стоит в защитных наушниках и стреляет из калаша по голограммам."
        "Кажется я его уже где-то видел."
        "Я взял со стены калаш, чтобы тоже пострелять. Отточу свои умения. Раньше мне максимум доводилось стрелять из пневматики по банкам. Ну и несколько выстрелов из боевого автомата на военных сборах в классе десятом. Или в девятом. Уже не помню."
        scene bg poligon tir with dissolve
        show pavel tired at left with dissolve
        pav0 "— О, кажется тебя знаю. Чего не на занятиях?"
        "Точно. Он тоже из нашего отряда."
        "— Тот же вопрос хотел бы задать тебе. Мне просто не захотелось идти."
        pav0 "— И это причина не идти? Просто не захотелось?"
        "— А у тебя какая причина? Спасение мира?"
        pav0 "— Что-то в этом роде... Да, честно говоря, тоже желанием не горю."
        "— Избегаешь компаний?"
        pav0 "— Предпочитаю проводить время наедине с собой. А тут ты пришёл..."
        "Непрозрачно намекает мне, чтобы я свалил?"
        if inferno:
            "Вот не может он просто так торчать в тире. И голос у него дрожит. Явно что-то скрывает."
            "— Уходить я не собираюсь. Тир общий."
            pav0 "— Ну как хочешь. Мне всё равно."
            "— Обиделся, что ли?"
            pav0 "— Тебе-то какое дело?"
            "— Да чего ты такой грубый?"
            "Павел явно растерялся. По нему видно, что думает он вообще о другом. Да и эта дрожь в голосе."
            "— Чего так дрожишь-то? Боишься чего-то? Из-за этого на занятия не пошёл?"
            "— Меня кстати зовут [playerName]."
            pav "— Павел. Да ничего я не боюсь, тебе кажется. Постреляй уже по мишеням, чего докопался до меня."
            "— Ну ладно. Кстати, что это за калаш такой?"
            "— Отличается от обычного?"
            pav "— Конечно. Ты попробуй пострелять."
            "Классно. Это оружие тоже использует нейроинтерфейс. Чувствую, куда полетит пуля, круто."
            pav "— Это первое оружие людей, созданное с использованием нейронтов. За основу был взят обычный АК-12."
            "— Оружие людей? А ты к кому себя причисляешь?"
            pav "— К людям конечно. Ну я не знал, как правильно сказать. Оружие людей, оружие Земли... Наше оружие."
            # pomis: Будет менее агрессивный вариант узнать инфу, но пока хз как
            # bulka: При наличии определённых очков (шпиона к примеру) появится вариант.
            "Павел побледнел, и стал говорить ещё более неуверенно. Есть одна идея, не проканает, так отшучусь."
            "Я направил автомат ему в лицо."
            show pavel afraid at right
            "— На чьей ты стороне?"
            "Стрелять я не собирался, да и не смог бы сделать этого, конечно. Но эффект устрашающий. Плюс, Павел какой-то шуганный."
            pav "— Эй, не стреляй! Я всё расскажу!"
            "Да ладно? Неужели всё настолько запущено?"
            "— Так на чьей ты стороне?"
            pav "— Я просто хочу отомстить..."
            "— Кому?"
            pav "— Организации TESL. А именно, руководству этой базы. Это они уничтожили моё село! А всё свалили на газовую аварию!"
            # pomis: Ну и дальше в том же духе, бла бла бла, я спать
            # bulka: Улыбнуло это село) Его конечно надо переделать, ибо как-то туповато звучит, но пока что, как временный вариант, сойдёт.
            pav "— Из-за их ошибки погибли все, кого я знал!"
            "Если он не врёт, то мне есть о чём с ним поговорить! Но убирать автомат я не буду. Полезная штука."
            "— Я тоже из-за этих уродов потерял семью!"
            if agressionPoints>3:
                "Убил бы каждого!" 
            # bulka: Мб это с гневом говорится
            pav "— Как ты потерял семью?"
            "— Мало того, что корабль, в котором я плыл вместе с семьёй, сделали приманкой для инферно! Так ещё в него врезалась подлодка людей! Именно из-за неё корабль и потонул!!! "
            "— Я лично убил пилота, но этого мало!"
            "И тут я понял, что сболтнул лишнего."
            "Палец на курке напрягся."
            pav "— Эй, ты чего?! Мы на одной стороне!"
            "— На одной? О чём ты?"
            pav "— Я шпионю для Инферно! Скоро произойдёт нападение на базу."
            # bulka: Расписал чуток, но павлик немножко другим выходит. Не думаю, что это толково.
            # pomis: я бы не стал предлагать сбежать вместе человеку, который направил на меня АК-12 :)
            "— А чего тогда ты в тире делаешь, а не сбежал куда подальше?"
            pav "— Я не могу покинуть базу до сигнала тревоги. Тогда все выходы разблокируются."
            "— Я с тобой. Не собираюсь умирать со всеми."
            pav "— Ладно, ладно, только ты убери автомат от моего лица!"
            "— Ну как хочешь."
            call ush1
            scene bg poligon
            pav "— И да, почему я именно в тире. На каждом оружии установлен датчик, который запретит лифту двигаться, если ты войдёшь в него с этим оружием. А когда включится тревога, все подобные ограничения будут сняты."
            "— Откуда такая уверенность?"
            pav "— Я тут уже три недели."
            "— Ладно, когда нападение?"
            pav "— Вот когда начнётся, ты сразу поймёшь. Будет со стороны океана. От первого удара сильнее всего пострадает ангар, как наименее углублённое в гору помещение. Далее под удар попадут жилой корпус и учебные классы. Дальше уже тиру достанется. Последними разрушит лабораторию и командный пункт."
            "— А как мы покинем базу? Откуда?"
            pav "— Ну кем бы я был, если бы не продумал план побега? По шахте вентиляции из жилого корпуса выползем наружу. Я изучил шахту вдоль и поперёк, знаю кратчайший путь. У тебя есть защитный шлем?"
            "— Шлем? Нет. Зачем?"
            pav "— Чтобы череп не сломать..."
            "— И как мы успеем выползти? Сколько у нас времени?"
            pav "— По моим расчётам, мы должны пройти половину пути за 4 минуты. Это метров 600 ползком. Вторую половину пути можно уже так не спешить. Ненавижу спешку, но другого выбора нет. А без оружия совсем не хочется уходить."
            pav "— Тебе ничего забрать не нужно?"
            "— Нет, я налегке." 
            call ush2
            scene bg poligon
            pav "— Ну ла..." with vpunch
            "Фразу Павлика прервал оглушающий шум, как будто гром раздался прямо в этом тире." with vpunch
            "Лампы мгновенно переключились на красный. Включились сирены"
            gen "— Всем занять боевые позиции! "
            "— Погнали, чего стоишь!"
            show bg lift with dissolve
            show pavel afraid at center
            pav "— В жилой комплекс!"
            "— Да знаю!"
            show bg coridor
            "Павел поставил стул и легко снял решётку с вентиляции. Закинул автомат и забрался в шахту. Я следом за ним."
            "Снова удар." with vpunch
            # pomis: Тут можно будет ввести сцену, где их кто-то замечает, и выбор, убивать или нет. Но сейчас нет ничем не занятых персонажей, и нет нужды вводить кого-то нового. Если только соседку Юминг, она может ещё где-то пригодится.
            # bulka: Соседка юминг, по идее, должна быть на учениях, откуда припераются юминг на цумвальт, если жива. А вот Тенко, при нужном количестве очков, мог съёбнуть с уроков, чтобы проследить.
            if stangerPoint>0:
                "Неожиданно меня кто-то резко потянул назад."
                if knowTenkoName:
                    "Это был Тенко."
                else:
                    ""
                    # TODO: Альтернативный вариант
                tenko "— Как я думал."
                "Тенко улыбнулся."
                if antiTenkoPoints>0:
                    "— Откуда ты узнал?"
                    "Надо отвлечь его внимание и придумать как от него избавиться."
                    # tenko "— Было давно ясно, что Павел не горит желаниям сражаться против Инферно, но при это он сам вызвался воевать и много времени проводит в тире и тренируется. Это явно было неспроста."
                    # tenko "— А когда я покопался в архивах и узнал, что случилось с его @чем-то@, то стало понятно он старается он явно не ради людей."
                    # tenko "— Ты тоже сразу показался мне подозрительным. Когда же ты направился в тир, то мне показалось, что родственные души найдут друг друга."
                    # tenko "— Когда же ты вместо занятий пошёл в тир"
                    # bulka: Надо это как-то без излишней болтовни расписать. Также, надо сделать получение пойнтов тенко во время разговора в классе. 
                    # bulka: Возможно Тенко получил информацию от соседки Юминг - хакера, которая взломала базу данных и узнала о прошлом гг и павла.
                else:
                    "Как же меня бесит его улыбка!"
                    "— Как же ты достал..."
                # bulka: Бля, мозг не пашет. Не могу думать над условиями. Потом. Мб диалог в классе изменю. Павел нас тут бросить может.
            pav "— Следующий выстрел нас хорошо тряхнёт! Быстрее залезай!"
            "Я нырнул в шахту следом за Павлом. Ползём."
            # TODO: какой-нибудь диаложек.
            "— А как ты связался с инферно?"
            # bulka: Этот вопрос надо с условиями задавать, наверное. Если автомат не наставляли, к примеру. Точнее возможно задать, но необязательно. После разговора он предупредит, к примеру, о выстреле.
            "Мы прибыли к выходу из шахты. Павел выстрелил из автомата по краям, удерживающим решётку."
            "— А-а! Предупреждать надо! Громко же!"
            pav "— Мне всё равно."
            "Павел достал какое-то устройство из кармана."
            pav "— Йоу! Это Павел!"
            noname "— Да я понял. Выбрался с базы?"
            pav "— А как же! Тут это... Нашёл парнишу, он тоже желает отомстить организации. Мы вместе сбежали."
            noname "— Отомстить? Уверен?"
            "Задрали."
            #"— Эй! Слышите меня там?"
            #noname "— Прекрасно тебя слышу. "
            "— Что беремен!"
            noname "— Если он будет полезен настолько, насколько умеет шутить, то лучше сразу от него избавиться."
            if agressionPoints>3:
                $ negativePoints +=1 #bulka: Хз для чего. Даже вписывать пока не буду, мб не пригодится.
                "— Слышь, ты там. Не наглей. Я тебе избавлюсь!"
            else:
                "— От полезных ресурсов вредно избавляться."
                # TODO: Расписать разницу ответов.
        else:
            "Ну не буду же я навязывать свою компанию?"
            "— Ладно, пойду я... Тебя как зовут-то?"
            pav "— Павел."
            "— А я [playerName]."
            pav "— Мне всё равно."
            "Вот как... Ну и хрен с ним. {w}Я вызвал лифт."
            "Спустя минуту лифт с грохотом приехал."
            scene bg lift
            "Так куда поехать? В лабораторию? В ангар? Опаздывать на занятия я не хочу, лучше вообще не идти."
            $ result = renpy.imagemap("images/karkas-tir.jpg", "images/karkas-tir-hover.jpg", [(699, 326, 870, 605, "hungar"), (514, 604, 666, 693, "lab")], focus="imagemap")

            if result == "lab":
                jump lab
            elif result == "hungar":
                jump hangar



    if result == "classes":
        "Ладно уж, схожу..."
        scene bg educlass center
        $ gunPoints += 1
        co "— Итак, товарищи, сегодня я расскажу основы нашей тактики подводного боя!"
        "Координатор нарисовал на доске какую-то странную схему. "
        co "— Всё понятно?"
        "В ответ все молчат. Он ожидал другой реакции?"
        co "— Основная задача подводных операций — оборона исследовательских платформ."
        co "— Враг нападает с помощью так называемых подводных титанов. Эти твари, судя по нашим данным, способны сражаться только вблизи крупных городов Инферно."
        co "— Так что, они будут их использовать, только если мы вплотную подойдём к их городам. С собой титаны транспортируют небольших демонов."
        co "— Титаны ретранслируют им энергию, получаемую из городов. Следовательно, если уничтожить титана, демоны погибнут."
        # Егэ, однако)
        co "— Титаны используют эхолот для навигации, так что вы без проблем сможете уклоняться от их атак на ваших подводных лодках в стелс режиме. Однако во время атаки вы будете открыты."
        co "— А водные демоны хоть и обладают зрением, но спокойно уничтожаются обычным оружием. Они служат для того, чтобы не подпустить вас близко к цели, в тот момент, когда она будет уничтожать платформу."
        "Я почувствовал, что мне кто-то ткнул в спину."
        menu:
            "Повернуться":
                    if knowTenkoName == False:
                        "На меня смотрел парниша со смешной причёской."
                        if playedChess:
                            "Тот самый, с которым я играл в шахматы."
                        stranger "— Эй, парень, тебя как зовут?"
                        "— [playerName], а тебя?"
                        $ knowTenkoName = True
                        ten "— Тенко. Будем знакомы."
                        "Он улыбнулся, но от такой улыбки мне стало не по себе."
                    else:
                        ten "— Эй, [playerName], тебе не кажется, что Жорик ничего не понимает в тактике?"
                        "— Отстань..."
                        # bulka: И тут я понял, что моё видение персонажа мешает работать с ним всем кроме меня. Привет когнитивный диссонанс\
                        # bulka: Ладно. Тогда моё видение персонажа будет распространяться только на изначально инферно рут. В солдатском руте пускай будет такое.
            "Проигнорировать":
                $ gunPoints += 1
                co "— Соответственно, вы должны максимально быстро нейтрализовать титана. Для этого вы будете оснащены кластерными гранатами, начинёнными жидким азотом."
                co "— Весь радиус действия этой штуковины очень быстро замораживается в ледяную сферу. {w}Кластерные осколки пускают азот только через момент, замораживая лишь поверхность сферы, оставляя ее полой внутри. Оставаясь крепкой ледяной клеткой, по закону термодинамики эта штука всплывает на поверхность, где титаны бесполезны."
                co "— Вот только вам придётся подобраться к титану на расстояние прямого выстрела, иначе гранату перехватят демоны."
                co "— И есть небольшая проблема..."
                co "— Враг каждый раз преподносит нам сюрпризы. "
        co "— А сейчас идём в ангар, покажу вам подводные лодки!"
        co "— Все за мной!"
        scene bg lift
        "Мы без проблем все разместились в лифте, Жорик приложил палец к сканеру отпечатков и выбрал изображение ангара на экране."
        if minoriPoints>0:
            mi "— [playerName], а что сейчас будет? Какие ещё подводные лодки?"
            "— Ты что, всё прослушала?"
            mi "— Мне показалось это скучным..."
        else:
            sl "— [playerName], нетерпится порулить?"
            "— В жизни не управлял транспортом!"
            sl "— Ну тут навыки управления обычными машинами совсем не пригодятся."
            sl "— Как думаешь, нас сегодня выпустят в океан?"
            "— Что-то я очень в этом сомневаюсь."
        "Спустя пару минут мы оказались в ангаре."
        co "— За мной!"

        scene bg hangar ships
        jump hangardefault

    elif result == "lab":
        jump lab

    elif result == "hungar":
        jump hangar
        
label lab:
    "Лучше схожу в лабораторию, думаю, там я узнаю больше полезной информации."
    $ mariePoints += 1
    
    if inferno == True:
        "Может смогу найти что-то секретное."
    if promisedMarie == False:
        "Видимо, несмотря на то, что я отказался от её приглашения, она всё же добавила меня в список тех, кто может посещать лабораторию."
    "Я нажал на изображение лаборатории на экране и лифт тронулся."
    "С уровнем доступа \"А\" я могу попасть почти в любое помещение военной базы"
    "Не слишком ли сильно нам доверяют? Хотя, не удивлюсь, что каждый шаг отслеживается, и нам специально дали такую свободу действий."
    $ camera_reset()
    show bg laba back onlayer background
    show bg laba front onlayer forward
    if promisedMarie == True: # Если обещал Марии прийти в лабу
        $ mariePoints += 1
        "Спустя пару минут я снова оказался в этом странном футуристическом помещении. Повсюду были какие-то опытные образцы, ну и бардак."
    "Спустя пару минут я оказался в этом странном футуристическом помещении. Повсюду были какие-то опытные образцы, ну и бардак."
    
    show marie scaled smiling onlayer middle at Position(xpos=0.44, xanchor='center', ypos=0.49) with dissolve
    "Мария что-то доказывала своим коллегам, рисуя на доске маркером схемы."
    show marie scaled shamed onlayer middle at Position(xpos=0.44, xanchor='center', ypos=0.49) with dissolve
    "Увидев меня через стекло переговорной комнаты, она немного смутилась. Не думала, что я действительно приду, наверное."
    show marie scaled smiling onlayer middle at Position(xpos=0.44, xanchor='center', ypos=0.49) with dissolve
    if promisedMarie == True: # Если обещал Марии прийти в лабу
        "На этот раз мне придётся ждать. Поброжу по лаборатории, что ли..."
    else:
        "Ладно, подожду её, больше никого я тут не знаю. Поброжу по лаборатории, что ли..."
    "Учёные занимались своими делами и не обращали на меня особого внимания."
    "Я подошёл к столу и стал разглядывать оборудование"
    menu: 
        "Попытаться украсть что-нибудь":
            "Ну раз всем пофигу на меня, можно попробовать..."
            "Я осматриваюсь по сторонам.{w} Никто не смотрит на меня."
            "Оглянулся в сторону переговорной комнаты."
            if spyPoints > 0:
                "Плавным движением положил себе в карман какую-то флешку."
                $ stolenFlash = True
                if inferno==False:
                    "И зачем она мне? Может там важные данные об Инферно? Или ещё чего..."
            else:
                "Такое чувство, что этот учёный смотрит прямо на меня. Ну нет."

        "Спокойно ждать Марию":
            "Что-то не хочется рисковать..."
            if inferno==False:
                "Да и зачем??"
            "На лабораторном столе валялся разобранный пистолет Adam's Rage, какие-то странные камни, чертежи, несколько флешек и куча другой ерунды."
    show marie scaled smiling onlayer middle at Move((0.44, 0.36), (0.1, 0.36), 1.0, xanchor="center", yanchor="center")
    "Через несколько минут дверь переговорной открылась, и из неё вышло несколько людей в военной форме и двое учёных в возрасте."
    hide bg onlayer background
    hide bg onlayer forward
    hide marie onlayer middle
    scene bg laba opened
    "Вид у них был неважный. Как будто бы пенсии лишили."
    show marie smiling at left with dissolve
    "За ними вышла Мария, она сразу стала искать меня глазами, а когда увидела подбежала ко мне."
    ma "— Ну хоть кто-то нормальный!"
    "Ничего себе приветствие"
    "— Я тоже рад тебя видеть"
    ma "— Представляешь, эти нытики не хотят выделять нам средства на разработку дешёвого способа синтезировать цезий..."
    "— Нытики?"
    ma "— А ещё они называют меня сумасшедшей!"
    ma "— Ладно, не важно. Прогуливаешь?"
    "— Да, не думаю, что на занятиях интересно. Этот координатор выглядит так, будто сам ничего толком не знает."
    ma "— Он хоть и не самый умный, но он научил обращаться с оружием многих людей."
    "— Он не сильно разозлится, что я не пришёл?"
    ma "— Скажешь, что ты был срочно нужен мне для исследования! Хах!"
    "— Какого такого исследования?"
    ma "— Придумаешь что-нибудь, он всё равно не вникнет!"
    if promisedMarie == True: # Если обещал Марии прийти в лабу
        "— Да, а зачем я вообще пришёл?"
        ma "— Не знаю, мне просто надоело общаться с нытиками, а ты вроде не ноешь!"
        if inferno==True:
            ma "— Да и Юминг до сих пор не нашли..."
            "Вот ведь чёрт! Такую беседу будет сложно поддержать, лучше сменить тему!"
        "— У тебя есть... Эм...{w} Чайник?"
        ma "— Конечно есть! Ладно, ты пока присаживайся куда-нибудь."
    else:
        ma "— Что-то я не ожидала тебя здесь увидеть. Ты же зануда."
        ma "— Присаживайся, что ли?"
        "Она указала мне на стул у лабораторного стола."
        ma "— Я скоро!"
    # сюда нужен новый фон
    "..."
    "Мария пришла с двумя чашками чая, положила их на стол и села напротив меня."
    if inferno==True:
        ma "— Не очень-то ты хочешь воевать, правда?"
        "— С чего это?"
        ma "— Какой-то ты отличаешься от других новичков. Обычно, новобранца либо охватывает желание поскорее побывать в бою, либо на него всё давит и ему страшно. Тебе явно не страшно."
        ma "— А ты пацифист какой-то."
        "— Для начала я хочу узнать всю правду. Из-за чего это всё началось, зачем они нападают на нас."
        ma "— Долго же ты будешь копать до правды! А пока будешь копать, чтобы совсем скучно не стало, можешь повоевать. По рассказам, управлять транспортом через нейроинтерфейс — очень круто."
        "— Когда-нибудь докопаюсь и узнаю правду."
        menu:
            "А мне кажется, это люди во всём виноваты!":
                "Мария слегка зависла."
                ma "— Э-э."
                ma "— Ну, не ты один так считаешь. Один мой коллега был такого же мнения, только я не знаю, где он сейчас"
                # Pomis: Пусть он теперь будет в срединном союзе
                # bulka: Или у инферно, если срединный союз придётся убрать.
                ma "— А ты впредь аккуратнее с такими высказываниями!"
                if mariePoints>1:
                    ma "— Я-то к тебе хорошо отношусь, а вот кто-нибудь другой услышит..."
                "— Ладно, я просто говорю, что думаю."
            "А я могу прямо сейчас опробовать транспорт?":
                ma "— Хм. Для их старта нужно разрешения начальства. Да даже если ты сможешь стартовать, то лучше уже не возвращаться!"
                "— Угон военного транспортного средства с военной базы? Круто!"
                ma "— Да не получится угнать. Слишком хорошая система защиты. Я сама её проектировала!"
                # хз чё ещё тут написать
    else:
        ma "— Сильно хочешь воевать?"
        "— Я отомщу этим тварям за свою семью!"
        ma "— Оу... Даже так. {w}Те, кто живёт местью у нас недолго держатся."
        "— А что движет тобой?"
        ma "— Мне нравится моя работа. Я тут руковожу научным отделом, а что самое интересное, мои разработки не пылятся на полках, а используются."
        ma "— Я же тебе показывала ботов, для которых я написала улучшенный алгоритм? А как тебе лифт? Раньше была система тоннелей."
        "— Ты это всё сама сделала?"
        ma "— Ну как сама. У меня целый отдел... {w}Хотя, они бестолочи."
        ma "— Нетерпится поуправлять подводной лодкой?"   
        "— Было бы круто!"  
        "— А я могу прямо сейчас опробовать этот транспорт?"
        ma "— Хм. Для их старта нужно разрешения начальства. Да даже если ты сможешь стартовать, то лучше уже не возвращаться!"
        "— Угон военного транспортного средства с военной базы? Не вижу смысла. Для меня."
        ma "— Да всё равно не получится угнать. Слишком хорошая система защиты. Я сама её проектировала!"
        "Мария гордо вздёрнула носик."
        menu:
            "— Хаха. А ты милая":
                $ mariePoints += 1
                ma "— Конечно же я ми... Стоп, что?"
                "Мария запнулась посреди предложения и покраснела."
                "Видимо, она подумала, что я хвалю её интеллект и собиралась выдать свою коронную фразочку про свою гениальность."
                "А дразнить её довольно весело."
                if inferno==True:
                    "А влюбить её будет легко. Она совсем неопытная, так что даже не поймёт, что её будут использовать."
                            #"— Ладно, мне пора."
                            #ma "— Эй, не смей так делать"
                            #"-Что делать? Мне в самом деле пора.
            "— Спорим, я смогу найти в ней уязвимости?":
                ma "— Ты слишком самоуверен! Тем более у тебя нет доступа."
                "— Ну коли струсила, так и скажи."
                ma "— Не струсила! Просто тебе в самом деле нельзя!"
                ma "— Хотя я попробую достать копию. Но имей в виду, никому не слова!"
                "— Я могила."
                ma "— Как бы после этого, я бы могилой не стала..."
                if inferno==True:
                    "Боже, ею так легко манипулировать. Если у меня получится достать копию схемы их системы безопасности, это будет успех."
                    # bulka: Возможен вариант кражи этих схем с последующим сваливанием.
                    #"— Пожалуй я пойду."
    #ma "— Ну тогда удачи. Приходи ещё."
    #"— Обязательно".
    #ma "— Буду ждать."        
    # bulka: Это называется я начал писать сюжет, не дочитав до конца...        
    "Мария допила свой чай и встала из-за стола."
    ma "— Пошли, покажу тебе подводные лодки. Попробуем запустить, может получится."
    "— Любой может просто так взять и опробовать военное оборудование?"
    ma "— Нет конечно. У нас много военного персонала, не обладающих открытой нервной системой. Без обычных войск никакую войну не выиграть. Соответственно, их никто в ангар не пустит."
    ma "— Но ты, как будущий пилот, должен иметь доступ к тому, что пилотируешь."
    ma "— Эта база создана в большей степени учёными, а не вояками, так что и порядки тут более демократичные."
    "— А почему ты решила, что я именно пилот? Мне говорили, что после обучения будет распределение."
    ma "— 99 процентов становятся пилотами. Ладно, пошли уже!"
    if brokenFinger:
        ma "— И да... Что у тебя со средним пальцем? Очень странная травма, боюсь представить, как ты её получил."
        "— Всё именно так, как ты это себе представляешь."
    # bulka: Меня одного смущает высший уровень допуска у новичка? Мне хочется узнать, каким же надо быть лохом, чтобы у тебя уровень доступа ниже А был?
    # pomis: Сделал по логичнее
    scene bg lift with dissolve      
    "Мы вышли из лаборатории и поехали в ангар."
    scene bg hangar ships with dissolve
    $ withMarieInHangar = True
    "Моим глазам открылась уже знакомая картина: пара десятков подводных лодок, размещённых на двух этажах ангара."
    # bulka: Знакомая? Я что-то пропустил?
    ma "— Пошли!"
    "Мария уверенным шагом направилась к ближайшей."
    ma "— Эта вроде бы никому не принаджит. Как новенькая!"
    "Она погладила её по корпусу. Да уж."
    "— Как в неё залезть?"
    ma "— Тут где-то дактилоскоп... Ах, вот он!"
    "Стекло подводной лодки поднялось, и я смог забраться внутрь. Раз она открылась, значит, питание подключено."
    ma "— Ну, давай, положи руки во-о-он на те датчики."
    "— Хорошо."
    "Никакого результата. Ожидаемо."
    ma "— Эх, в другой раз!"
    "Я выбрался из лодки. Тем временем раздался шум приближающегося лифта."
    co "— За мной!"
    "Дверь распахнулась, из лифта вышел координатор, вслед за ним шесть других новичков. Странно, а где ещё один?"
    co "— Эй ты! Какого чёрта тебя не было на занятии?"
    "Упс..."
    ma "— Проблемы?"
    "Самодовольная ухмылка координатора тут же исчезла."
    co "— Никаких проблем, мэм!"
    "Он её боится, или что? Или пытается приударить? Кто кого старше по званию? {w}Сложные они."
    jump hangardefault

# Осматривает военную технику. Потом в ангар приходит координатор и остальные новички
label hangar:
    "Осмотрю лучше наши подводные лодки в одиночестве."
    "Я нажал на соответствующее изображение на экране и лифт тронулся."
    scene bg hangar ships
    "Спустя несколько минут моим глазам открылась знакомая картина. Пара десятков крохотных подводных лодок расположенных на двух этажах ангара."
    "И ни души вокруг. Могли быть хоть поремонтировать что-нибудь для приличия."
    "Я обошёл ангар, прошёлся по второму этажу. В общем-то, ничего интересного, кроме подводных лодок. Но не могу же я просто взять и залезть в неё?"
    "Или могу?"
    "Мои размышления прервал шум приезжающего лифта. Да уж, точно как метро."
    co "— За мной!"
    "Дверь распахнулась, из лифта вышел координатор, вслед за ним шесть других новичков. Странно, а где ещё один?"
    co "— Эй ты! Какого чёрта тебя не было на занятии?"
    menu:
        "Мне было плохо... Меня пугает это всё...":
            $ lazynessPoints += 1
            co "— С поля боя тоже смотаешься? Пугает его!"
            co "— Как минимум, нужно предупредить. Для такого зелёного новичка как ты, такое один раз простительно, но впредь..."
            "— Да, да, я понял."
            sl "— Эй, ты чего такой кислый? Утром же нормальный был!"
        "Не люблю школу. Лучший способ усвоить материал — на практике": 
            $ liePoints += 1
            $ minoriPoints += 1
            co "— И поэтому ты пришёл в ангар, чтобы испробовать подводные лодки?"
            co "— А ты мне нравишься!"
            co "— Их нельзя запустить без разрешения командования."
            "— Понял, товарищ координатор!"
            co "— Зови меня просто Жорик!"
    jump hangardefault

############## Происходит во вторую очередь ###################
label hangardefault:
    co "— Ладно, а теперь я покажу вам эти подводные лодки."
    # фон : подводная лодка вблизи
    if withMarieInHangar==True:
    # Советую определиться hangar или hungar, ибо потом это аукнется.
        "Координатор повёл за собой группу и направился в нашу сторону. Он подошёл к нашей лодке, а группа расступилась и окружила это чудо техники."
    else:
        "Мы подошли к ближайшей. Координатор встал прямо у кабины, а мы окружили это чудо техники со всех сторон."
    "Координатор постучал по корпусу."
    co "— Композитная броня! Под водой эта машинка необнаружима эхолотом и абсолютно всеми типами земных радаров."
    co "— У меня было 14 боевых заданий на ней, это невероятное оружие! Ты чувствуешь машину как своё тело!"
    "Боже, да ему бы на рынке её продавать."
    if knowTenkoName == False:
        "Ко мне подошёл парниша со смешной причёской."
        if playedChess:
            "Тот самый, с которым я играл в шахматы."
        stranger "— Эй, тебя как зовут?"
        $ knowTenkoName = True
        "Как-то не очень вежливо он спрашивает."
        "— [playerName], а тебя?"
        ten "— Тенко. Будем знакомы."
    
    call ush1
    scene bg hangar ships with flash
    "Координатор рассказывал про свои боевые заслуги. Не очень-то интересно."
    "Какой-то новобранец, которого я не знаю, пытался спорить, упрекая Жорика в научной некомпетентности."
    "Скучно."
    if withMarieInHangar==True:
        "— Маш, может, пойдём?"
        ma "— Ещё раз меня так назовёшь, будешь как Жорик меня бояться."
        "Ого."
        ma "— Ну да. Пожалуй я пойду. А ты оставайся, он хоть и хвалится, но как наставник он хорош."
        ma "— Спасибо за компанию! Пока!"
    elif minoriPoints>1:
        "— Минори, тебе интересно?"
        mi "— Да-а-а! Оказывается, он такой классный и сильный!"
        "— Кто?"
        mi "— Жорик!"
    call ush2
    scene bg hangar ships with flash
    co "— А на последне..."
    "Бахвальство Жорика прервал оглушающий шум, как будто гром раздался прямо в этом ангаре." with vpunch
    "По стенам пошли трещины."
    "Лампы мгновенно переключились на красный. Включились сирены"
    gen "— Всем занять боевые позиции! "
    "Ещё один удар. Стены стали крошиться, с потолка посыпалась бетонная крошка."
    mi "— Что происходит?"
    co "— Берегитесь! "
    $ jorikAlive = False
    "Он оттолкнул нас от лодки. В тот же момент сверху упал кусок бетона и арматуры, превративший нашего координатора в фарш."
    "Нескольких новобранцев стошнило."
    # bulka: А вот это уже не очень цепляет. И зачем вводить переменную о смерти жорика? Он же дохнет в любом случае. Независимо от выбора игрока.
    if withMarieInHangar==True:
        ma "— Боже..."
    if inferno==True:
        "Мне не впервой видеть смерть... Неужели каждый раз мне будет всё меньше жалко?"
        "Не время думать об этом!"
    else:
        "Ну почему я всегда попадаю в какой-то ад?!"
        "— Ненавижу! Свою! Судьбу!"
    if withMarieInHangar==True:
        "Я схватил Марию за руку и побежал к соседней подводной лодке."
        "Запрыгнул и потянул Марию за собой."
        ma "— Что ты делаешь??"
        "В её голосе чувствалась паника, чуть ли не плач. Я и сам в ужасе, но хотя бы могу действовать."
        "Мы вместимся. Залезай!"
        "А что с остальными?"
        if inferno == True:
            "А плевать на остальных!"
        else:
            "— Эй вы! Быстро занимайте подводные лодки! Живо!"
        "Раздался третий удар, часть второго этажа обружилась, да и весь ангар выглядел так, что я в панике запустил лодку."
        "Шлюзовое отверстие перед моей лодкой открылось, а пусковой механизм отправил лодку в открывшийся тоннель."
        jump ch4
    elif minoriPoints>1:
        "Минори закрыла лицо руками и громко рыдала. Настолько громко, что это пугало меня даже больше, чем обваливающиеся стены."
        "— За мной!"
        "Я посадил её в соседнюю подводную лодку и включил пусковое устройство. Шлюзовое отверстие открылось, а пусковой механизм отправил лодку в открывшийся тоннель."
        "А что с остальными?"
        if inferno == True:
            "А плевать на остальных!"
        else:
            "— Эй вы! Быстро занимайте подводные лодки! Живо!"
        "Раздался третий удар, часть второго этажа обружилась, да и весь ангар разрушался так стремительно, что я в панике подбежал к свободной лодке и запрыгул в неё."
        "— Успею! Успею!"
        "Кусок бетона упал прямо на мою лодку, поцарапав один двигатель. Прочная штука!"
        "Я запустил лодку и погрузился на ней в пусковой тоннель."
        jump ch4
    else:
        sl "— А ну все заткнулись! Вы не слышали приказ генерала? Все по боевым позициям! На корабли!"
        "Его голос ужасно дрожал, некоторые слова звучали как бессмысленный набор звуков, но всё сказанное было услышано отрядом."
        sl "— [playerName], мы как самые сильные, должны помочь другим забраться!"
        if inferno == False:
            "— Да, ты прав!"
            "Или всё таки не прав... Но я уже согласился."
            "Мы помогли новобранцам залезть и запустить их боевые машины, однако когда мы закончили, прогремел уже четвёртый удар. "
            sl "— Быстрее!"
            $ slavaAlive = False
            "В эту же секунду голову Славы размозжило куском стены."
            "Я в панике залез в лодку, но как только я закрыл кабину, со второго этажа свалилась другая лодка, ударившись носом в бок моего спасательного судна. "
            "Вот чёрт! Она отказывалась включаться!"
            "— Да что с тобой! Давай же!"
            "Ошибка доступа!"
            "—Ах ты тварь!"
            "Лодка достаточно прочная, чтобы выдержать ещё несколько попаданий, но оставаться тут я не собираюсь!"
            "О. А рука-то болит!"
            "Мою руку настолько стёрло в кровь, что дактилоскоп просто не смог меня опознать. Попробую другой рукой включить."
            "— Давай!"
            "Полчилось! Пусковой механизм отправил мою лодку в тоннель."
            jump ch4
        else:
            $ slavaPoints -= 1
            # bulka: хз, могут ли быть отрицательными переменные (должны мочь), но плюсов вроде этих пойнтов не было, а поведение по отношению к славе оставляет желать лучшего.
            "— Чёрта с два! Я сваливаю!"
            "Я побежал к ближайшей свободной лодке, панически нащупал дактилоскоп, открывающий кабину и забрался внутрь. "
            "Раздался третий удар, часть второго этажа обружилась, да и весь ангар разрушался так стремительно, что я в панике подбежал к свободной лодке и запрыгул в неё."
            "— Успею! Успею!"
            "Кусок бетона упал прямо на мою лодку, поцарапав один двигатель. Прочная штука!"
            "Я запустил лодку и погрузился на ней в пусковой тоннель."
            jump ch4
    # Тут можно показать нападение на базу от лица инферно
    # Юзер запрыгивает в лодку и принимает участие в бою
    # bulka: Эх, а я тут идею о побеге с базы делал. Слишком быстро развивается сюжет. Ну да ладно, сойдёмся на том, что будет возможность вернуться на базу. Правда всё равно не понимаю, как в таком случае он присоединиться к инферно. Начнёт из своей лодки палить по другим? Или просто свалит? Как я понял лодка может быть заблокированна удалённо.
    # pomis: я сам пока не понимаю

label ush1:
    scene bg zumwalt coords with dissolve
    show point:
        alpha 0.0 xalign 0.4 yalign 0.7
        linear 1.0 alpha 1.0
        repeat
    show text zumwalt:
        xalign 0.5 yalign 0.9
    with dissolve
    $ renpy.pause()
    scene bg sky ocean with flash
    ush "— Алулим! Ты где?!"
    "Из-за двери послышался голос"
    alil "— Старший Уш, вы меня потеряли?"
    ush "— Ну как видишь. Сколько ещё плыть?"
    alil "— Десять минут, Старший."
    ush "— Как же я ненавижу это \"Старший\". Может, лучше \"капитан\"?"
    alil "— Нельзя нарушать традиции!"
    ush "— Ты мне запрещать что-то собрался?"
    alil "— Нет, простите, {w}капитан."
    ush "— Вот и хорошо. До сих пор не могу поверить, что нам удалось провернуть такое всемером! Я сильно переоценивал врага."
    return

label ush2:
    scene bg sky ocean with flash 
    alil "— Капитан, всё готово. По вашему приказу!"
    ush "— Огонь!"
    return
