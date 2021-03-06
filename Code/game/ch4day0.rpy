label ch4:
    scene bg ocean day with flash
    alil "— Капитан, как и ожидалось, земная авиация в пути. Расчётное время до нападения — 15 минут."
    ush "— У этого корабля нет никаких шансов в одиночку противостоять авиации. Хоть тут и есть средства ПВО и ПРО, толку от них против группы истребителей будет мало. Разве что ракетный залп отразить сможем. Ломаем базу и сваливаем."
    "Уш медленно ходил из стороны в сторону. Алилум тем временем нервно стучал пальцами по столу."
    alil "— Осталось примерно четыре выстрела рельсотрона до полного уничтожения базы, а это около девяти минут."
    ush "— Меня больше пугает возможная контратака со стороны базы. Мы не можем обеспечить себе подводное прикрытие на таком расстоянии от городов."
    ush "— Есть какие-нибудь данные с радаров? Если мы будем знать точное местоположение врага, то откроем огонь противолодочными ракетами на поражение."
    alil "— Никаких данных, капитан!"
    "Уш разочарованно вздохнул."
    ush "— Тогда начните подготовку обратного портала. Через девять минут уходим."
    alil "— Эх, ни разу не перемещался на обратных порталах."
    ush "— А мне как-то довелось использовать его. Было приказано навести шуму в самом оживлённом земном городе — Гонконге."
    ush "— Мы телепортировались туда на пару минут, расстреляли толпу. Не успели люди хоть что-то понять, как мы уже были у себя на базе."
    alil "— Люди кричали?"
    ush "— Конечно. Люди всегда кричат, когда им страшно."
    alil "— Они заслужили это."
    alil "— Ладно. А что делать с экипажем судна, капитан?"
    ush "— Они придут в себя как только мы уйдём. Кстати, назревает неплохой международный скандал!"
    # bulka: Когда читал тогда, думал, что это воспоминания координатора. Немножко странно с таким стилем повествования (от первого лица) делать такие перескоки на другую сторону. Другое дело, когда повествование идёт от третьего лица.
    # pomis: я вообще хотел в своём руте сделать рассказ от 1 лица Энлиль с перескоками на гг ровно до того момента, как они встретятся. А тут я делал от третьего, ну по крайней мере, я думал, что делаю от третьего.
    # bulka: Неплохая идея кстати. Мб, в будущем можно запилить руты от лица других персов?
    # pomis: будет видно
    scene bg underwater with flash
    play music vision
    "Меня с огромной скоростью выбросило из пускового тоннеля. Интересное ощущение, как в аквапарке. Я действительно чувствую эту машину как продолжение своего тела. Мои размышления прервал голос, прозвучавший у меня прямо в ушах."
    show gantz serious onlayer master:
        xpos -0.06 ypos 0.34 zoom 1.44 alpha 0.2 
        ease 1.8 alpha 0.35
        ease 1.8 alpha 0.2
        repeat
    gen "— Ваша боевая задача уничтожить эсминец класса «Zumwalt», атакующий нашу базу из рельсотрона. Передаю координаты."
    if usedDirectRadio:
        "Ах да, этот передатчик транслирует прямо в ухо."
    else:
        "Какого чёрта? Почему он говорит как-будто бы прямо у меня в голове?"
        $ usedDirectRadio = True
        # bulka: Эта переменная будет ещё использоваться? Будет вариант не вступать в битву?
        # pomis: думаю, что не будет такого варианта. Переменная пригодится с вероятностью 10%
    "— И как уничтожать этот корабль? Чем?"
    "Ну хоть координаты передались прямо в сознание, удобно. Что-то вроде компаса."
    show gantz shouting onlayer master:
        xpos -0.06 ypos 0.34 zoom 1.44 alpha 0.2 
        ease 1.8 alpha 0.35
        ease 1.8 alpha 0.2
        repeat
    gen "— Ещё четыре выстрела, и базе конец."
    "А вот и следующий выстрел. Даже отсюда слышен шум."
    show gantz serious onlayer master:
        xpos -0.06 ypos 0.34 zoom 1.44 alpha 0.2 
        ease 1.8 alpha 0.35
        ease 1.8 alpha 0.2
        repeat
    gen "— Ещё три выстрела.{w} У вас шесть минут."
    if withMarieInHangar:
        ma "— Какой ещё корабль?"
        "— Генерал сказал, что надо уничтожить какой-то эсминец."
        ma "— А... По этой рации. Кстати, чтобы ответить, попытайся представить того, кому хочешь обратиться. Если хочешь сказать всем, то представь лидера операции."
        "— Приватно лидеру ничего сказать нельзя?"
        # bulka: Мб, не анонимно, а только лидеру?
        # pomis: исправил
        ma "— Нет, такие правила."
        "Так... Представляю генерала Ганца.{w} О, вроде получилось настроиться."
        "— Генерал, а как нам топить этот корабль?"
        gen "— Ракетами с базы мы его взять не можем, слишком хорошая система ПРО. Арсенал для подводных боёв почти полностью бесполезен против эсминца."
        gen "— Отменяю приказ уничтожения корабля. Мы связались с Пентагоном, корабль был угнан. Захватить путём абордажа. По возможности, не убивать военнослужащих США, они взяты в заложники."
        "Что? Он серьёзно?"
        # bulka: хз, ещё в прошлый раз бросилось в глаз, что можно ракетами изблизи херачить, раз абордаж возможен. Или дно протаранить, раз лодка такая крепкая, что выдерживает падение больших кусков бетона.
        # pomis: имел ввиду ракеты на военной базе. Лодки ими не оснащены. А по поводу прочности лодок была мысль. Можно выбор сделать чисто для сохранения логичности.
        menu:
            "Поспорить":
                $ leadershipPoints += 1
                "— Генерал, а почему мы не можем просто протаранить корабль?"
                gen "— Я уже составил план абордажа, нет времени изменять тактику."
                "Даже так. Ну и бред. Врезался и всё, делов-то!"
                "— Почему нет? Просто врежемся! Эти подлодки очень прочные!"
                gen "— Угробишь всю команду. Да и хотелось бы обойтись без уничтожения корабля, если есть такая возможность. Обострять отношения с американцами совсем не хочется."
                "Нас могут всех убить, а он думает о каких-то отношениях с америкосами!"
            "Согласиться":
                "— Хорошая идея!"
                "На самом деле, я в этом не уверен..."
                $ liePoints += 1
                $ gantzPoints += 1
                "Что-то не хочется спорить с этим человеком..."
                # bulka: Надо тут что-нибудь сделать. Ведь мы заявляли, что каждый выбор что-нибудь делает. Да и просто делать выбор без влияния не комильфо. 
                # pomis: делал как заглушку, чтобы потом расписать.
        gen "— На борту каждой подлодки есть экземпляр пистолета Adam's Rage. Он многократно превосходит обычное стрелковое оружие, и даже в руках неопытных бойцов выдаёт отличную точность благодаря нейроинтерфейсу."
        ma "— Что он говорит?"
        "Я отрубил соединение с генералом."
        "— Будем брать на абордаж."
        "Марии это явно не понравилось."
        ma "— Нет, мы не будем этого делать!"
        ma "— Я не буду."
        if inferno:
            "Мне тоже не особо нравится эта идея."
            "— Предлагаешь не атаковать со всеми?"
            ma "— Такого генерал точно не потерпит. И да, он может блокировать лодки удалённо."
            "— И что теперь делать?"
            ma "— Не знаю я."
        elif yumingAlive:
            yu "— Приём, это Чайка.{w} Подкрепление через две минуты."
            "— Откуда вы движетесь?"
            "Так, стоп, забыл её представить."
            ma "— Кто движется?"
            "— А, подкрепление. Там Юминг."
            ma "— О, точно, она выполняла учения со своим отрядом неподалёку."
            ma "— Как же полегчало-то!"
            ma "— Но это не отменяет того факта, что я не буду участвовать в абордаже!"
        "Мы уже подплывали к отмеченной координате. Там действительно был корабль."
        if visitedLab:
            "— Мария, и где твои боты!?"
            ma "— Утонули."
            "— Как утонули?"
            ma "— Судя по всему, хранилище ботов затопило водой после первого удара, иначе они сразу же бы погрузились в пусковые тоннели."
            "Что-то в последнее время вокруг меня постоянно всё тонет..."
            menu:
                "Бесполезный хлам!":
                    $ saidThatBotsAreTrash = True
                    $ mariePoints -= 1
                    "Мария сделала обиженное лицо и ничего не ответила."
                # bulka: внедрил мою идею с минус пойнтами? Или я слоупок? 
                # pomis: не помню. 
                "Думаю, они бы тут особо и не помогли.":
                    ma "— Именно! Они не рассчитаны на такое!"
        "Что, правда будем брать на абордаж?.."
        # bpaw: Предложение выглядело как вопрос. Алсо, !.. и ?..
        "И как вообще это сделать? Этот корабль больше похож на цельный кусок металла, чем на доступную цель для абордажа."
        gen "— Итак, вы должны запрыгнуть из воды на палубу эсминца."
        "— ЧТО!"
        gen "— Затем, сразу же выбраться и открыть огонь на поражение. Далее, вы должны уничтожить персонал, управляющий рельсотроном. Судя по проектной документации, которую мы когда-то украли у американцев, она находится довольно недалеко от палубы. Координаты отправил."
        "И почему никто кроме Ганца и Юминг не выходит на связь? Не разобрались, как пользоваться?"
        "Мы вплотную подобрались к кораблю."
        gen "— Высылаю траектории для совершения прыжка."
        "О, это значительно облегчает задачу."
        ma "— Что мы делаем?"
        "— Прыгаем!"
        if mariePoints>1:
            "Мария в страхе прижалась ко мне. Я настроился на траекторию и разогнался."
        else:
            "Мария зажмурила глаза и прижала к себе свои коленки."
        jump abordaj

    #
    #   Без Марии в лодке
    #
    else:
        hide gantz onlayer master
        "И как ему ответить? Нас не инструктировали. Может, надо что-то нажать?"
        "Без толку..."
        "— Меня кто-нибудь слышит?"
        "— Эй!"
        "Без толку..."
        if yumingAlive:
            
            show yuming onlayer master:
                xpos -0.13 ypos 0.21 zoom 1.44 alpha 0.2
                ease 1.8 alpha 0.35
                ease 1.8 alpha 0.2
                repeat
            yu "— Приём, это Чайка.{w} Подкрепление через две минуты."
            "Забавный позывной. И как ей ответить?"
            show gantz serious onlayer master:
                xpos 0.26 ypos 0.34 zoom 1.44 alpha 0.2 
                ease 1.8 alpha 0.35
                ease 1.8 alpha 0.2
                repeat
            gen "— Мы начнём операцию без вас. Присоединяйтесь сразу, как сможете."
            yu "— Вас поняла."

        else:
            "Что же. Инструкции дали и ладно. Можно и молча плыть."
        hide gantz with dissolve
        hide yuming with dissolve
        "Какое-то время никто не нарушал тишину эфира."
        if yumingAlive:
            show yuming onlayer master:
                xpos -0.13 ypos 0.21 zoom 1.44 alpha 0.2
                ease 1.8 alpha 0.35
                ease 1.8 alpha 0.2
                repeat
            yu "— Эй, солдат, ты тоже тут?"
            "Это она лично мне говорит? Как ответить!?"
            yu "— Ну и чего молчишь? Не умеешь пользоваться?"
            "Да, чёрт тебя побери, не умею!"
            hide yuming with dissolve
        if iscraPoints>0:
            $ usedDirectRadio = True
            show iscra smiling onlayer master:
                xpos 0 ypos 0.21 zoom 1.44 alpha 0.2
                ease 1.8 alpha 0.35
                ease 1.8 alpha 0.2
                repeat
            isc "— О, кажется я разобралась, как пользоваться! Парниша, ты меня слышишь? Представь меня и попытайся мысленно мне что-то сказать."
            "Что? Эта штука и правда так работает? Представить Искру не трудно, эту выскочку тяжело забыть."
            "— Приём."
            show iscra sad onlayer master:
                xpos 0 ypos 0.21 zoom 1.44 alpha 0.2
                ease 1.8 alpha 0.35
                ease 1.8 alpha 0.2
                repeat
            isc "— Я так и не поняла, как говорить всем. А ты первый в голову пришёл. Расскажем другим, как пользоваться? Или ну их?"
            "— Мы же не враги, чтобы что-то утаивать?"
            show iscra angry onlayer master:
                xpos 0 ypos 0.21 zoom 1.44 alpha 0.2
                ease 1.8 alpha 0.35
                ease 1.8 alpha 0.2
                repeat
            isc "— А кто знает. Враг может быть рядом."
            show iscra sad onlayer master:
                xpos 0 ypos 0.21 zoom 1.44 alpha 0.2
                ease 1.8 alpha 0.35
                ease 1.8 alpha 0.2
                repeat
            "— Опять ты за своё..."
            isc "— А ты на удивление спокоен для такой ситуации."
            menu:
                "— Да ты вроде бы тоже не паникуешь":
                    $ iscraPoints += 1
                    isc "— Да будь что будет. Я уже не понимаю, что происходит. Все чувства как отшибло."
                    "— Тебе так важно докопаться до правды? Почему?"
                    isc "— Не люблю, когда меня используют."
                    "— Я тоже хочу знать всю правду. Я потерял свою семью из-за этой войны."
                    "— Я хочу знать кто именно виноват в этом и заставить его пожалеть о том, что появился на свет."
                    isc "— Или на тьму. Эти Инферно же под землёй живут."
                    isc "— Ладно, дай послушать пустоту в моей голове."
                "— Кто-то же должен.":
                    $ leadershipPoints+=1;
                    isc "— Взять контроль? Думаю, Слава справится с этим лучше тебя. Хоть он и придурок."
                    isc "— А тебя я мало знаю. Просто первым вспомнился. Ладно, дай послушать тишину в моей голове."
                    # bulka: Пустота звучит как-то оскорбительно
            hide iscra with dissolve
            "— Как хочешь."
            "Но генерал не дал ей этой возможности."
        show gantz serious onlayer master:
            xpos -0.06 ypos 0.34 zoom 1.44 alpha 0.2 
            ease 1.8 alpha 0.35
            ease 1.8 alpha 0.2
            repeat
        gen "— Ракетами с базы мы его взять не можем, слишком хорошая система ПРО. Арсенал для подводных боёв почти полностью бесполезен против эсминца."
        gen "— Отменяю приказ уничтожения корабля. Мы связались с Пентагоном, корабль был угнан. Захватить путём абордажа. По возможности, не убивать военнослужащих США, они взяты в заложники."
        "Что? Он серьёзно?"
        show gantz resolute onlayer master:
            xpos -0.06 ypos 0.34 zoom 1.44 alpha 0.2 
            ease 1.8 alpha 0.35
            ease 1.8 alpha 0.2
            repeat
        gen "— Итак, вы должны запрыгнуть из воды на палубу эсминца."
        if usedDirectRadio == False:
            "— ЧТО! Да как тебе ответить! Мне не нравится эта идея!"
        gen "— Затем, сразу же выбраться и открыть огонь на поражение. Далее, вы должны уничтожить персонал, управляющий рельсотроном. Судя по проектной документации, которую мы когда-то украли у американцев, она находится довольно недалеко от палубы. Координаты отправил."
        if usedDirectRadio == False:
            "И почему никто кроме Ганца и Юминг не выходит на связь? Тоже не разобрались, как пользоваться?"
        "Мы вплотную подобрались к кораблю."
        gen "— Высылаю траектории для совершения прыжка."
        # TODO: какие-нибудь размышления, диалоги
        # bulka: Мб она ему скажет как пользоваться этим и тд?
        jump abordaj


label abordaj:
    scene bg zumwalt attacked with dissolve
    "Мы взлетели над водой и чётко приземлились на палубу."
    scene bg zumwalt boarting with dissolve
    gen "— Вылезайте и открывайте огонь! Живо!"
    "Я вылез из кабины с пистолетом. А стрелять-то не в кого!"
    if slavaAlive:
        "Со мной вылез только Слава. Остальные, судя по всему, в шоке."
        sl "— Вылезайте! Быстро!"
        "Похоже, это подействовало, и оставшийся отряд отошёл от шока и выполз из своих подлодок."
    else:
        "Остальные сделали это медленнее."
        "В другом бою нас бы уже убили!"
    "— Минори! Пистолет!"
    mi "— Где?"
    "— Возьми! В лодке!"
    mi "— Ой... Прости."

    "Боже..."
    "— Будьте начеку, стрелять сразу! Это не люди!"
    "Сомневаюсь, что они смогут без колебаний открыть огонь..."
    "Внезапно Слава направил своё оружие и выпустил несколько пуль в сторону."
    sl "— Минус один!"
    "Ну хоть в нём не сомневаюсь."
    sl "— Все, за мной!"
    if inferno:
        "Да, пусть он управляет этим стадом."
    "Тут палубу корабля сотряс запуск очередного снаряда из рельсотрона." with vpunch
    "Мы в это время бежали к месту, откуда велось управление этим жутким оружием."
    "По пути мы убили троих военнослужащих в американской форме. Не ясно, люди это, или нет. По всем внешним признакам это обычные люди, вот только ведут себя как какие-то куклы."
    # bpaw: Американская форма выглядит как папин рыбацкий костюм.
    "Мы выбили дверь в помещение управления рельсотроном. Несколько человек в военной форме сидело за компьютерами, а некто, держащий в руках неизвестный мне предмет тут же словил пулю от Тенко."
    "Люди в военной форме резко вскочили и подняли руки. Теперь они хотя бы похожи на живых людей, а не на кукол."
    "Один из них начал говорить на ужасном русском."
    usa "— Не стрелять! Они управляет нами!"
    "Так и думал."
    ten "— Чем докажешь?"
    "Тенко не отводил свой пистолет с военных."
    "А они даже и не знали, что ответить."
    "— Не похоже, что они врут..."
    ten "— А вдруг они в сговоре?"
    "— Генерал же вроде сказал, что их взяли в заложники..."
    menu:
        "Осмотреть неизвестный предмет, выпавший из рук застреленного.":
            $ debilPoints += 1
            "— Я гляну, что это за предмет был..."
            sl "— Зачем тебе это нужно?"
            "— Может, пригодится для исследований..."
            if withMarieInHangar:
                "Марию обрадую, хех."
            "Я подобрал эту штуковину.{w} Твою же...{w} Круто!"
            "— Я управляю ими как куклами!"
            "А получится заставить их говорить? Так, как получить доступ к голосовым связкам?"
            "Вслепую пытаюсь управлять солдатами как куклами."
            sl "— Не увлекайся, мы поняли, что может эта штука."
            "Может, это делается так? Голосовые связки находятся где-то тут. Попробую сказать \"Привет\"!"
            "Нет, не выходит..."
            "Солдат рухнул на землю. От удивления я выронил устройство и подбежал к солдату. Пульса нет."
            "Второй солдат в ужасе смотрел на меня и боялся пошевелиться."
            $ killedPeopleCount += 1
            $ slavaPoints -= 1
            mi "— Ты что, убил его?"
            ten "— Я сам собирался обоих убить, так что ничего страшного."
            if inferno == False:
                "Невинного человека убил... Просто так. Да что за монстр я такой?"
            mi "— Или он сам умер? Я ничего не могу понять!"
            "Да я сам не понимаю ничего..."
            ten "— В любом случае, об этом надо будет составить отчёт."
            $ tenkoSaidAboutReport = True
            if antiTenkoPoints>1:
                "Какой ещё отчёт?"
            if inferno:
                "Да чего я переживаю из-за какого-то солдатика? Это же шикарнейшая вещь! Надо оставить себе!"
                if spyPoints>0:
                    "Осторожно положил предмет себе в карман, вроде никто не обратил на это внимание."
                    $ pickedManipulator = True
                    "Кажется, Тенко заметил и хитро улыбнулся."
                    if antiTenkoPoints>1:
                        "Зная этого хитреца, могу предположить, что он захочет стырить у меня. Или сделать какую-то гадость. Не буду спускать с него глаз."
                    # pomis: Я правильно понял персонажа? Он же скучающий. А то, что гг возьмёт себе такую штуку в карман предвещает нескучное развитие событий, вот он и не против.
                    # bulka: Практически идеально. Тут во всяком случае.
                else:
                    "Только я попытался положить эту штуковину себе в карман, как Минори сразу же заметила это."
                    mi "— Брось эту штуку, она опасна!"
                    "Твою же мать... Бесишь."
                    if slavaAlive:
                        sl "— Она права, пусть лучше учёные займутся изучением всего, что здесь произошло."
        "Согласиться с Тенко":
            $ tenkoKilledNavy = True
            "— Хотя, пожалуй ты прав."
            ten "— Лучше лишний раз перестраховаться, чем лишний раз пожалеть."
            "Тенко без тени жалости расстрелял безоружных военнослужащих."
            "Вся остальная команда в шоке наблюдала за его действиями."
            "Ладно, не время поддаваться своим чувствам."

    if leadershipPoints>0 or killedPeopleCount>0: #  pomis: Почему использовал эту (killedPeopleCount) переменную в условии? Мне кажется, что человек, который убивал, более убедительно сможет отдать команду убивать.
        $ leadershipPoints += 1
        "— Мы должны зачистить корабль."
        "— Разделимся и зачистим каждую комнату."
        "Кажется, отряд принял меня за лидера, круто!"
        if inferno:
            "Вот только зачем мне это нужно? Потренируюсь командовать на них, что ли."
        if slavaAlive:
            sl "— Встретимся у лодок через 20 минут!"
            sl "— Так. Кто-нибудь взял рацию с собой?"
            "Молчание в ответ. Отлично."
            # bpaw: Он вроде мог быть убитым к этому моменту
            # bulka: Не мог. Рома понял, что играть в Джорджа Мартина слишком сложно, а потому отменил возможность его смерти.
    else:
        ten "— Мы должны зачистить корабль."
        ten "— Разделимся и зачистим каждую комнату."
        ten "— А я за рацией, доложу ситуацию генералу. Встретимся у лодок через 20 минут!"
        
        if inferno:
            if antiTenkoPoints>1:
                "Отряд принял Тенко за главного, ну и хорошо. Мне влом командовать, а так я не буду привлекать внимания."
                "Он хороший стратег и способен сохранять хладнокровие."
            else:
                # bulka: Твою ж мать. Опять условия.
                "Отряд принял Тенко за главного. Какого чёрта?"
                "Я тоже хочу командовать всеми!"
                if antiTenkoPoints>0:
                    "Хотя таланта управлять людьми у него не отнять."
                else: 
                    "Подчиняться такому дураку? Вот до чего я докатился."
                    "Ну да ладно. Выделяться — это последнее, что мне нужно. Тем более остальные ему подчиняются."
        else:
            "Отряд принял Тенко за главного, даже не знаю, хорошо это или плохо. У меня мурашки по коже от этого типа."
        "А ещё он способен убивать без колебаний."
        if inferno:
            "Мне тоже нужно стать таким."
        else:
            "Я же не такой, правда?"
            # bpoint
        
        # bulka: Что-то я его всё меньше узнаю. Честно говоря этот персонаж не планировался как такой бравый парень и лидер. Скорее именно стратег, тот кто управляет из тени. Кто не возьмёт на себя ответственность. Максимум как зам. Быть лидером — это ограничивать себя, а Тенко не любит ограничений. В этом момент ещё можно оставить, но в остальном лучше будет так не делать.
        # pomis: Так лучше? Отправил товарищей зачищать, а сам ушёл прохлаждаться в лодку.
        # bulka: Думаю, вот так будет оптимально.
    if minoriPoints>0 and inferno==False:
        "Я уже собрался побежать, как почувствовал, что кто-то держит меня за рукав" 
        mi "— Давай вместе, вдруг тебе будет страшно одному?"
        "Уж кто бы говорил... Хотя, думаю, она просто не могла по-другому сказать."
        menu:
            "— Нет, каждый должен сделать это сам.":
                "Она разочарованно опустила глаза."
                $ slavaPoints += 1
                "— Он прав, ты солдат или кто?"
                mi "— Ясно..."
                # bulka: Минус пойнт минори? Или она не такая?
                # pomis: Минусы это слишком жёстко
            "— Разве что за тебя будет страшно, пошли.":
                # bulka: Это с улыбкой надо сказать наверное.
                $ minoriPoints += 1
                $ withMinoriOnZumwalt = True
        
    "Мы разделились, каждый взял на себя определённый участок. Опасная тактика, но в замкнутых помещениях наше оружие явно обладает преимуществом."
    "Открываю дверь... Никого.{w} Следующую... Никого."
    "За третьей дверью располагался капитанский мостик."
    "Я навёл пистолет на того, кто стоял у приборной панели. Он медленно развернулся в мою сторону."
    "Вот это глаза! Жутко смотреть! Точно не человек."
    "— Ты понимаешь меня?"
    "В ответ слышу речь на неизвестном мне языке. Не могу даже различить эмоции."
    if withMinoriOnZumwalt:
        mi "— Боже, кто это?"
    "Какие всё-таки жуткие глаза.{w} Нет, по своей природе они не ужасные. Но на человеческом лице они выглядят так пугающе. Я когда-то читал гипотезу про «зловещую долину», когда что-то очень похожее на человека, вызывает максимально негативные эмоции, хотя, ничего жуткого в нём нет. Оно просто очень похоже на человека. Но всё же, обладает небольшими отличиями."
    if inferno:
        "Я должен заговорить с ним!"
        menu:
            "Убрать оружие":
                $ debilPoints += 1
                "Думаю, нам будет проще понять друг друга, если я уберу пушку."
                # bulka: Не думаю, что в этом руте за это можно дать тут очки.

            "Продолжать держать его на прицеле":
                "Кто знает, на что он способен? Хоть я и не считаю его врагом, а вот он может выкинуть какой-нибудь фокус против меня."
                # bulka: Нет влияния выбора.
                # pomis: пока хз что тут сделать
                # bulka: Есть вариант застрелить минори при первом варианте. Мол мешала. Офк, условий при это много учтено должно быть, ибо убийство хладнокровное.
                # pomis: не нужна она тут
        "Попытаюсь как-то наладить с ним контакт."
        "Я навёл на себя палец и назвал своё имя."
        "Ну уж имена-то у них должны быть?"
        "Персонаж кажется понял меня. Он показал на себя и представился."
        ush "— Уш. [playerName]?"
        
        if stolenFlash:
            "— Держи, пригодится. Я не знаю, что там... Но я украл это в лаборатории."
            "— А, ты же всё равно не понимаешь меня..."
            "Я швырнул ему украденную флешку. "
            "Уш схватил её, подозрительно осмотрел, положил в карман и швырнул мне что-то в ответ."
            "Я не смог поймать, плохая реакция. Оно ударилось об моё тело и упало на пол."
            "Похоже на какой-то камень с резьбой. Я поднял его и вопросительно посмотрел на Уша."
            # pomis: Нет, это не устройство для связи. Было бы слишком рискованно давать такую вещь случайному человеку, так как есть риск исследования и взлома. И жучок тоже. Подаёт сигнал -> можно отследить в обратную сторону. Будет носитель информации. Считывается напрямую при контакте с головой. 
            "— Что это?"
            "Уш попытался что-то изобразить жестами, но я не понял. Ладно, разберусь."
        "Так, этот товарищ обязан выжить. Как его спасти и не вызвать подозрение у отряда?"
        "Просто скажу своим, что всё чисто. А Ушу попытаюсь объяснить жестами, что нужно подождать минут десять и никуда не вылезать."
    else:
        "Это враг. Я должен убить его. Должен."
        if withMinoriOnZumwalt:
            "Минори тоже направила на него оружие."
        if killedPeopleCount>0:
            "Мне уже не впервой убивать людей. Хотя, это даже не человек."
        else:
            if slavaAlive == False:
                "Почему я не могу это сделать так же легко, как, например, Тенко?"
            else:
                "Из-за этих тварей погибла моя семья!" with bloodrage
        # Звук выстрела
        "Я проделал в его груди дыру."
        if killedPeopleCount>0:
            # bulka: Контрольный слишком хладнокровно. Мб при сомнениях только один выстрел с возможностью выживания уша? 
            # pomis: пусть будет условие. А для заполнения счётчика убийств в солдатском руте потом что-нибудь придумаю.
            # bulka: Мб сделать как я в шахматах? Отдельное условие для Инферно рута, отдельное для солдатского. В смысле требование очков.
            # pomis: тут и так отдельно для рутов сделано. Инферно — пытается заговорить, солдат — пытается убить
            # bulka: Ну всё равно как-то надо разницу между хладнокровным и попытком убийства. Считать первое убийство в руте солдата тут не оч — ток убил, осознание толком не пришло. Опираться на это не лучшая идея имхо.
            # pomis: ок
            $ killedPeopleCount += 1
            "Отчаянно жму на спусковой крючок ещё несколько раз.{w} Сдохни! Сдохни!"
            "Его голова стала похожа на фарш. Ну и гадость! Меня вырвало прямо на пистолет."
            $ ushAlive = False
        else:
            "Это же не человек. Это враг. Его можно убить. Да?"
            "Не время переживать об этом. Сейчас главное — миссия."
            "Как бы я себе не внушал, что я должен был это сделать, меня не отпускало чувство, что я совершаю ошибку. Мог бы быть кем угодно, а стал убийцей."
            $ ushWonded = True
    "Надо осмотреть остальные помещения.{w} Я в спешке обошёл ещё несколько помещений, но никого в них не нашёл. Почему такой пустынный корабль?"
    if withMinoriOnZumwalt:
        "И куда пропала Минори? Совсем забыл про неё!"
        if ushAlive:
            $ minoriAlive = False
            # bulka: Вот за смерть Минори можно дебилпойнтов откинутьXD
            "Я побежал на капитанский мостик. На полу лежала истекающая кровью Минори с рассечённой шеей. Рядом лежал нож."
            # bulka: Вторая неплохая смерть, что берёт за душу. Неплохо будет развить как-нибудь. Потом ещё каких-нибудь сожалений/кошмаров запилить.
            "Самого убийцы рядом не было."
            "— Ах ты тварь!" with bloodrage
            "— Я найду тебя и отрублю голову!"
            $ agressionPoints += 1
            # bulka: Не совсем понял, это уш убил? Не думаю, что его так быстро сливать нужно, ибо он один из главных антагонистов. Во всяком случае у нас пока другие не намечаются. Разве что второй. Если же не уш, то не совсем понятно как связано ранение уша со смертью минори.
            # bulka: То есть если мы берём минори с собой, то в случае живого уша в обоих рутах минори умирает? А в руте Инферно мы хороним её просто беря с собой? З.ы. Хз, но может в руте солдата она умрёт если не взять её с собой? Более логично выглядит. 
            # pomis: мы не берём её с собой в руте Инферно. Там условие. А строчку, где Минори вместе с гг убирает пистолет случайно добавил.
        else:
            "Я побежал на капитанский мостик. Она стояла неподвижно и смотрела на тело пришельца на полу."
            "— Ну чего ты встала-то? Это же не первая смерть, которую ты видишь!"
            "— Пошли уже!"
            "Я взял её за руку и повёл к месту встречи."
    else:
        "Пора идти к месту встречи..."
        jump reunion

label reunion:
    if withMinoriOnZumwalt and minoriAlive:
        "Мы вышли на палубу. Ого, сколько народу!"
    elif minoriAlive:
        "Я выбежал на палубу. Ого, сколько народу!"
    else: 
        "Я выбежал на палубу. Там собралось много людей."
    if yumingAlive:
        yu "— Давно не виделись!"
        "Да вроде бы недавно виделись..."

    if slavaAlive:
        sl "— Как ситуация?"
    else:
        stranger "— Ну, как успехи?"

    if minoriAlive == False:
        "— Эти твари убили Минори!"
        if yumingAlive:
            yu "— Как это произошло??"
            "— Я нашёл её тело на капитанском мостике..."
    elif inferno==False: 
        "— Был обнаружен и убит один пришелец."
        # pomis: Но гг не знает, убил ли он его. Если он выстрелил только один раз, Уш выжил.
        yu "— Только один и всё?"
        "— Ну да. А ты успела кого-нибудь найти вообще?"
        yu "— Нет, вы на удивление быстро справились."
        # bulka: Это вариант не выполняется никогда, ибо Юминг до этого момента всегда жива в руте солдата.
        # pomis: fixed
        sl "— Неплохо! А я двоих обезвредил! А третий растворился прямо в воздухе."
        ten "— Я так понимаю, это та же технология, что использовалась для нападения на Гонконг."
        mi "— А что там было?"
        ten "— Что-то вроде телепорта. Группа пришельцев появилась прямо из воздуха, расстреляла толпу и так же исчезла."
    elif inferno:
        "— Никого не обнаружил... Как-будто корабль-призрак."
        ten "— Как мы поняли, большая часть экипажа погибла от несовместимости с устройством управления сознания."
        # bulka: Он не может выполниться никак. Ибо идёт проверка на оба рута, если минори жива. В любом случае Инферно или тру или фальс.
        # pomis: Один раз выполнялся, что помогло мне найти ошибку. Сейчас уже не выполнится, да
    # pomis: сцуко, меня бесит, что поубивал половину персонажей, и диалоги составлять — головная боль.
    # bulka: Нехрен было в Мартина Джордана играть. Воскрешай теперь что ли.
    # pomis: Джорджа
    gen "— Итак, новобранцы, поздравляю с первым успешно выполненным боевым заданием."
    gen "— Вас довезут до берега прямо на этом корабле. База для базирования более непригодна."
    if yumingAlive:
        yu "— И где мы теперь будем жить?"
        if withMarieInHangar == False:
            yu "— И как там Мария?"
    elif slavaAlive:
        sl "— И где разместить подлодки?"
    elif minoriAlive: # Она точно жива, если Юминг не жива.
        mi "— Спросите его, что теперь с нами будет? Я так и не разобралась, как этим пользоваться..."
        "— Генерал, где же теперь мы будем базироваться?"
        if withMarieInHangar == False:
            "— И как там лаборатории?"
    gen "— Вы будете временно поселены в [cityName]. Вы продолжите своё обучение. Правда, вместо Жорика вас будет инструктировать Иван Крылов"
    # bulka: Чё-то маловато персов выходит в итоге.
    # pomis: Чует моя жопа, смерть Славы на данном этапе не слишком нужна. Воскрешу. Надо ещё кого-то добавить
    gen "— Сейчас проводится эвакуация персонала. О том, кто выжил, узнаете по прибытии в город."
    "Ничего себе, интрига."
    if withMarieInHangar==False and mariePoints>3:
        "Надеюсь, с Марией всё в порядке..."
    show iscra smiling at left
    isc "— Ты. Вроде не самый глупый здесь?"
    "— Мне тоже так кажется."
    isc "— Как тебя зовут-то?"
    "— [playerName]."
    isc "— А я Искра. Можно просто Иса. Как тебе удобно."
    "— Да я в курсе."
    show iscra sad at left
    isc "— Я совсем запуталась во всём этом. Пока что всё происходящее лишь подтверждает слова, которыми нас кормили на базе и нет никаких противоречий. Ты же не думаешь, что с нами честны на все сто?"
    if inferno:
        "— Думаю, с нами честны только в том, что поможет настроить нас против Инферно."
        isc "— Ух ты, даже так."
    else:
        "— Честно, даже не знаю. А что ты предлагаешь?"
        isc "— Не знаю, я запуталась... Вот смотри. "
    isc "— Почему напали именно на нашу базу?"
    isc "— Да ещё и таким сложным способом. Базы разбросаны по всему миру. Почему именно эта?"
    "— Может они не знают расположение остальных?"
    isc "— Почему тогда они знают расположение нашей?"
    sl "— Серьёзно, тебя сейчас волнует именно это?"
    isc "— А ты чего в чужой разговор лезешь?"
    if yumingAlive:
        yu "— Солдат, как себя чувствуешь?"
        if minoriAlive:
            "— Да в порядке."
            yu "— Ага, неплохо справляешься."
        else:
            "— Ужасно. Даже не знаю, что может сделать этот день ещё хуже."
            isc "— Уж найдутся способы."
            yu "— Привыкайте."
    hide iscra
    # pomis: я тут распишу, ниже просто план
    # pomis: хотя, в этом нет смысла.
    nvl clear
    nvlc "Нас поселили в ближайшем городке — [cityName]. Классическая российская глубинка. Видимо, кто-то предусмотрел возможность разрушения базы, и нас разместили в нескольких заранее подготовленных служебных квартирах. Пока нас расселяли, происходила эвакуация людей с базы. Квартира, конечно, так себе. И тесновато. Сойдёт. Моим соседом по комнате снова оказался Слава."
    # if antiTenkoPoints>0:
    #    "Хорошо, что не Тенко, например."
    # bulka: Эти пойнты означают качество противостояния Тенко и ответа на его действия. Они не означают положительное/негативное отношение к нему.
    hide nvl
    # pomis: OK
    scene bg city street night with dissolve
    scene bg city street dvor night with dissolve
    scene bg city room night with dissolve
    scene black with closing
    if killedPeopleCount>1:
        "Мне снились те люди, которые умерли от моей руки."
        if yumingAlive == False:
            "Я сбрасывал тело Юминг из лодки снова и снова... "
    else:
    # TODO: Расписать надо бы сон.
        "Бессоница — неумение заткнуть свой мозг?"
    jump ch4day1
        #Если за солдата, и не набрано достаточного количества поинтов с Марией. 


        # Pomis: Так, я примерно понял как вывести на Инферно
        # Pomis: Зачищая корабль, гг, откроет комнату и столкнётся с Ушем, не станет в него стрелять и вручит украденную флешку, если она у него есть. Попытается заговорить, но Уш не владеет русским. Тот спасётся и запросит шпионаж на гг.
        # bulka: В смысле запросит? У начальства или что?
        # pomis: что-то в этом роде, да
    
