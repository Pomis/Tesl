label ch4:
    scene bg sky ocean with flash
    alil "— Капитан, как и ожидалось, земная авиация в пути. Расчётное время до нападения — 15 минут."
    ush "— У этого корабля нет никаких шансов в одиночку противостоять авиации. Хоть тут и есть средства ПВО и ПРО, толку от них против будет мало. Разве что ракетный залп отразить сможем. Ломаем базу и сваливаем."
    "Уш медленно ходил из стороны в сторону. Алилум тем временен нервно стучал пальцами по столу."
    alil "— Осталось примерно четыре выстрела рельсотрона до полного уничтожения базы, а это около девяти минут."
    ush "— Меня больше пугает возможная контратака со стороны базы. Мы не можем обеспечить себе подводное прикрытие на таком расстоянии от городов."
    ush "— Есть какие-нибудь данные с радаров? Если мы будем знать точное местоположение врага, то откроем огонь противолодочными ракетами на поражение."
    alil "— Никаких данных, капитан!"
    "Уш разочарованно вздохнул."
    ush "— Тогда начните подготовку обратного портала. Через девять минут уходим."
    alil "— Эх, ни разу не перемещался на обратных порталах."
    ush "— А мне как-то довелось использовать его. Было приказано навести шуму в самом оживлённом земном городе — Гонконге."
    ush "— Мы телепортировались туда на пару минут, расстреляли толпу. Не успели люди хоть-что то понять, как мы уже были у себя на базе."
    alil "— Люди кричали?"
    ush "— Конечно. Люди всегда кричат, когда им страшно."
    alil "— Они заслужили это."
    alil "— Ладно. А что делать с экипажем судна, капитан?"
    ush "— Они придут в себя как только мы уйдём. Кстати, назревает неплохой международный скандал!"
    # bulka: Когда читал тогда, думал, что это воспоминания координатора. Немножко странно с таким стилем повествования (от первого лица) делать такие перескоки на другую сторону. Другое дело, когда повествование идёт от третьего лица.
    # pomis: я вообще хотел в своём руте сделать рассказ от 1 лица Энлиль с перескоками на гг ровно до того момента, как они встретятся. А тут я делал от третьего, ну по крайней мере, я думал, что делаю от третьего.
    scene bg sky ocean with flash
    "Меня с огромной скоростью выбросило из пускового тоннеля. Интересное ощущение, как в аквапарке. Я действительно чувствую эту машину как продолжение своего тела. Мои размышления прервал голос, прозвучавший у меня прямо в ушах."
    gen "— Ваша боевая задача уничтожить эсминец класса \"Zumwalt\", атакующий нашу базу из рельсотрона. Передаю координаты."
    if usedDirectRadio:
        "Ах да, этот передатчик транслирует прямо в ухо."
    else:
        "Какого чёрта? Почему он говорит как-будто бы прямо у меня в голове?"
        $ usedDirectRadio = True
    "— И как уничтожать этот корабль? Чем?"
    "Ну хоть координаты передались прямо в сознание, удобно. Что-то вроде компаса."
    gen "— Ещё четыре выстрела, и базе конец."
    "А вот и следующий выстрел. Даже отсюда слышен шум."
    gen "— Ещё три выстрела. У вас шесть минут."
    if withMarieInHangar:
        ma "— Какой ещё корабль?"
        "— Генерал сказал, что надо уничтожить какой-то эсминец."
        ma "— А... По этой рации. Кстати, чтобы ответить, попытайся представить того, кому хочешь обратиться. Если хочешь сказать всем, то представь лидера операции."
        "— Приватно лидеру ничего сказать нельзя?"
        # bulka: Мб, не анонимно, а только лидеру?
        # pomis: исправил
        ma "— Нет, такие правила."

        "Так... Представляю генерала Ганца. {w}О, вроде получилось настроиться."
        "— Генерал, а как нам топить этот корабль?"
        gen "— Ракеты его не берут, слишком хорошая система ПРО. Арсенал для подводных боёв почти полностью бесполезен против эсминца. Остаётся только абордаж."
        "Что? Он серьёзно?"
        gen "— На борту каждой подлодки есть экземпляр пистолета Adam's Rage. Он многократно превосходит обычное стрелковое оружие, и даже в руках неопытных бойцов выдаёт отличную точность благодаря нейроинтерфейсу."
        ma "— Что он говорит?"
        "Я отрубил соединение с генералом."
        "— Будем брать на абордаж."
        "Марие это явно не понравилось."
        ma "— Нет, мы не будем этого делать!"
        ma "— Я не буду."
        if inferno:
            "Мне тоже не особо нравится эта идея."
            "— Предлагаешь не атаковать со всеми?"
            ma "— Такого генерал точно не потерпит. И да, он может блокировать лодки удалённо."
            "— И что теперь делать?"
            ma "— Не знаю я."
        else:
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
            "— Мария, и где твои боты?!"
            ma "— Утонули."
            "— Как утонули?"
            ma "— Судя по всему, хранилище ботов затопило водой после первого удара, иначе они сразу же бы погрузились в пусковые тоннели."
            menu:
                "Бесполезный хлам!":
                    $ mariePoints -= 1
                    "Мария сделала обиженное лицо и ничего не ответила."
                # bulka: внедрил мою идею с минус пойнтами? Или я слоупок? 
                # pomis: не помню. 
                "Думаю, они бы тут особо и не помогли.":
                    ma "— Именно! Они не рассчитаны для такого!"
        "Что, правда будем брать на абордаж..."
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
            "Мария в страхе прижалась ко мне. Я настроился на траекторию и разогнался. "
        else:
            "Мария зажмурила глаза и прижала к себе свои коленки."
        "Мы взлетели над водой и чётко приземлились на палубу."
        gen "— Вылезайте и открывайте огонь! Живо!"
        if slavaAlive:
            "На деле приказ выполнили только я и Слава."
            sl "— Вылезайте! Быстро!"
            "Похоже, это подействовало, и оставшийся отряд отошёл от шока и выполз из своих подлодок."
        else:
            "Я вылез из кабины с пистолетом. А стрелять-то не в кого! "
            "Остальные сделали это медленнее."
            "В другом бою нас бы уже убили!"
        "— Минори! Пистолет!"
        mi "— Где?"
        "— Возьми! В лодке!"
        mi "— Ой... Прости."

        "Боже..."
        "— Будьте начеку, стрелять сразу! Это не люди!"
        "Сомневаюсь, что они смогут без колебаний открыть огонь..."
        if slavaAlive:
            "Внезапно Слава направил своё оружие и выпустил несколько пуль в сторону."
            sl "— Минус один!"
            "Ну хоть в нём не сомневаюсь."
            sl "— Все, за мной!"
            "Да, пусть он управляет этим стадом."
        else:
            "— И что вы все стоите! Координаты у вас есть."
            "Тенко поднял своё оружие и выстрелил в сторону."
            stragner "— Там кто-то шевелился."
            "Вот это хладнокровие."
        "Тут палубу корабля сотряс запуск очередного снаряда из рельсотрона."
        "Мы в это время бежали к месту, откуда велось управление этим жутким оружием."
        "По пути мы убили троих военнослужащих в американской форме. Не ясно, люди это, или нет. По всем внешним признакам это обычные люди, вот только ведут себя как какие-то куклы."
        "Мы выбили дверь в помещение управления рельсотроном. Несколько человек в военной форме сидело за компьютерами, а некто, держащий в руках неизвестный мне предмет тут же словил пулю от Тенко."
        "Люди в военной форме резко вскочили и подняли руки. Теперь они хотя бы похожи на живых людей, а не на кукол."
        "Один из них начал говорить на ужасном русском."
        "— Не стрелять! Они управляет нами!"
        "Так и думал."
        if slavaAlive:
            sl "— Убить всех остальных подозрительных существ!"
            "Похоже, отряд безоговорочно подчиняется ему."
        else:
            "— Думаю, наша задача выполнена. Кто-нибудь взял рацию с собой?"
            "Молчание в ответ. Отлично."

        # Pomis: Так, я примерно понял как вывести на Инферно
        # Pomis: Зачищая корабль, гг, откроет комнату и столкнётся с Ушем, не станет в него стрелять и вручит украденную флешку, если она у него есть. Попытается заговорить, но Уш не владеет русским. Тот спасётся и запросит шпионаж на гг.
        # bulka: В смысле запросит? У начальства или что?
        # pomis: что-то в этом роде, да
    #
    #   Один в лодке (без Марии)
    #
    else:
        ""
