label ch4:
    scene bg sky ocean with flash
    alil "— Капитан, как и ожидалось, земная авиация в пути. Расчётное время до нападения — 15 минут."
    ush "— У этого корабля нет никаких шансов в одиночку противостоять авциации. Хоть тут и есть средства ПВО, толку от них будет мало. Ломаем базу и сваливаем."
    alil "— Осталось примерно четыре выстрела рельсотрона до полного уничтожения базы, а это около девяти минут."
    ush "— Меня больше пугает возможная контратака со стороны базы. Мы не можем обеспечить себе подводное прикрытие на таком расстоянии от городов."
    ush "— Есть какие-нибудь данные с радаров? Если мы будем знать точное местоположение врага, то откроем огонь торпедами на поражение."
    alil "— Никаких данных, капитан!"
    ush "— Тогда начните подготовку обратного портала. Через девять минут уходим."
    alil "— Эх, ни разу не перемещался на обратных порталах."
    ush "— А мне как-то довелось использовать его. Было приказано навести шуму в самом оживлённом земном городе — Гонконге."
    ush "— Мы телепортировались туда на пару минут, расстреляли толпу. Не успели люди хоть-что то понять, как мы уже были у себя на базе."
    alil "— Люди кричали?"
    ush "— Конечно. Люди всегда кричат, когда им страшно."
    alil "— Они заслужили это."
    alil "— Ладно. А что делать с экипажем судна, капитан?"
    ush "— Они придут в себя как только мы уйдём. Кстати, назревает неплохой международный скандал!"
    scene bg sky ocean with flash
    "Меня с огромной скоростью выбросило из пускового тоннеля. Интересное ощущение, как в аквапарке. Я действительно чувствую эту машину как продолжение своего тела. Мои размышления прервал голос, прозвучавший у меня прямо в ушах."
    gen "— Ваша боевая задача уничтожить эсминец класса \"Zumwalt\", атакующий нашу базу из рельсотрона. Передаю координаты."
    if usedDirectRadio:
        "Ах да, этот передатчик транслирует прямо в ухо."
    else:
        "Какого чёрта? Почему он говорит как-будто бы прямо у меня в голове?"
        usedDirectRadio = True
    "— И как уничтожать этот корабль? Чем?"
    "Ну хоть координаты передались прямо в сознание, удобно. Что-то вроде компаса."
    gen "— Ещё четыре выстрела, и базе конец."
    "А вот и следующий выстрел. Даже отсюда слышен шум."
    gen "— Ещё три выстрела. У вас шесть минут."
    if withMarieInHangar:
        ma "— Какой ещё корабль?"
        "— Генерал сказал, что надо уничтожить какой-то эсминец."
        ma "— А... По этой рации. Кстати, чтобы ответить, попытайся представить того, кому хочешь обратиться. Если хочешь сказать всем, то представь лидера операции."
        "— Анонимно лидеру ничего сказать нельзя?"
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
                "Думаю, они бы тут особо и не помогли."
                    ma "— Именно! Они не рассчитаны для такого!"
        "Что, правда будем брать на абордаж..."
        # Так, я примерно понял как вывести на Инферно
        # Зачищая корабль, гг, откроет комнату и столкнётся с Ушем, не станет в него стрелять и вручит украденную флешку, если она у него есть. Попытается заговорить, но Уш не владеет русским. Тот спасётся и запросит шпионаж на гг.

    #
    #   Один в лодке (без Марии)
    #
    else:
