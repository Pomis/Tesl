label ch4:
    scene bg sky ocean with flash
    alil "— Капитан, как и ожидалось, земная авиация в пути. Расчётное время до нападения — 15 минут."
    ush "— У этого корабля нет никаких шансов в одиночку противостоять авиации. Хоть тут и есть средства ПВО и ПРО, толку от них против будет мало. Разве что ракетный залп отразить сможем. Ломаем базу и сваливаем."
    # bulka: против чего?
    "Уш медленно ходил из стороны в сторону. Алилум тем временен нервно стучал пальцами по столу."
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
    scene bg sky ocean with flash
    "Меня с огромной скоростью выбросило из пускового тоннеля. Интересное ощущение, как в аквапарке. Я действительно чувствую эту машину как продолжение своего тела. Мои размышления прервал голос, прозвучавший у меня прямо в ушах."
    gen "— Ваша боевая задача уничтожить эсминец класса \"Zumwalt\", атакующий нашу базу из рельсотрона. Передаю координаты."
    if usedDirectRadio:
        "Ах да, этот передатчик транслирует прямо в ухо."
    else:
        "Какого чёрта? Почему он говорит как-будто бы прямо у меня в голове?"
        $ usedDirectRadio = True
        # bulka: Эта переменная будет ещё использоваться? Будет вариант не вступать в битву?
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
        # bulka: хз, ещё в прошлый раз бросилось в глаз, что можно ракетами изблизи херачить, раз абордаж возможен. Или дно протаранить, раз лодка такая крепкая, что выдерживает падение больших кусков бетона.
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
            stranger "— Там кто-то шевелился."
            "Вот это хладнокровие."
            # bulka: Ахахах. Там кто-то шевилился. Будто насекоме. Правда больше напоминает имба лолек-кудере, чем планнированый архетип, ну да ладно. Мб исправлю потом. 
        "Тут палубу корабля сотряс запуск очередного снаряда из рельсотрона."
        "Мы в это время бежали к месту, откуда велось управление этим жутким оружием."
        "По пути мы убили троих военнослужащих в американской форме. Не ясно, люди это, или нет. По всем внешним признакам это обычные люди, вот только ведут себя как какие-то куклы."
        "Мы выбили дверь в помещение управления рельсотроном. Несколько человек в военной форме сидело за компьютерами, а некто, держащий в руках неизвестный мне предмет тут же словил пулю от Тенко."
        "Люди в военной форме резко вскочили и подняли руки. Теперь они хотя бы похожи на живых людей, а не на кукол."
        "Один из них начал говорить на ужасном русском."
        usa "— Не стрелять! Они управляет нами!"
        "Так и думал."
        stranger "— Чем докажешь?"
        "Тенко не отводил свой пистолет с военных."
        "А они даже и не знали, что ответить."
        "— Не похоже, что они врут..."
        stranger "— А вдруг они в сговоре?"
        menu:
            "Осмотреть неизвестный предмет, выпавший из рук застреленного.":
                "— Я гляну, что это за предмет был..."
                if slavaAlive:
                    sl "— Зачем тебе это нужно?"
                "— Может, пригодится для исследований..."
                if withMarieInHangar:
                    "Марию обрадую, хех."
                "Я подобрал эту штуковину. {w}Твою же...{w} Круто!"
                "— Я управляю ими как куклами!"
                "А получится заставить их говорить? Так, как получить доступ к голосовым связкам?"
                "Вслепую пытаюсь управляться солдатами как куклами."
                if slavaAlive:
                    sl "— Не увлекайся, мы поняли, что может эта штука."
                "Может, это делается так? Голосовые связки находятся где-то тут. Попробую сказать \"Привет\"!"
                "Нет, не выходит..."
                "Солдат рухнул на землю. От удивления я выронил устройство и подбежал к солдату. Пульса нет."
                $ killedPeopleCount += 1
                mi "— Ты что, убил его?"
                stranger "— Я сам собирался обоих убить, так что не вини себя."
                "Невинного человека убил... Просто так. Да что за монстр я такой?"
                mi "— Или он сам умер? Я ничего не могу понять!"
                "Да я сам не понимаю ничего..."
                stranger "— В любом случае, это войдёт в мой отчёт."
                if inferno:
                    "Да чего я переживаю из-за какого-то солдатика? Это же шикарнейшее оружие! Надо оставить себе!"
                # TODO: Взаимодействие с оставшимся солдатом
            "Хотя... Возможно, ты прав.":
                stranger "— Я всегда прав!"
                "Тенко без тени жалости расстрелял безоружных военнослужащих."
                # ввожу метку "TODO: " для удобства поиска мест, которые нужно расписать
                # TODO: Диалогов сюда
                # bulka: Хз, зачем эта метка. Обычных каментов хватало. Тем более в главе, которая в процессе активной разработки. 
        if slavaAlive:
            sl "— Убить всех остальных подозрительных существ!"
            "Похоже, отряд безоговорочно подчиняется ему."
        else:
            "— Думаю, наша задача выполнена. Кто-нибудь взял рацию с собой?"
            "Молчание в ответ. Отлично."
            stranger "— Мы должны зачистить корабль."
            stranger "— Разделимся и зачистим каждую комнату."
            if strangerAfraidPoints>1:
                "Отряд принял Тенко за главного, даже не знаю, хорошо это или плохо. У меня мурашки по коже от этого типа."
            else:
                "Отряд принял Тенко за главного, ну и хорошо. Он хороший стратег и способен сохранять хладнокровие. "
                "А ещё он способен убивать без колебаний."
            # bulka: Что-то я его всё меньше узнаю. Честно говоря этот персонаж не планировался как такой бравый парень и лидер. Скорее именно стратег, тот кто управляет из тени. Кто не возьмёт на себя ответственность. Максимум как зам. Быть лидером - это ограничевать себя, а Тенко не любит ограничений. В этом момент ещё можно оставить, но в остальном лучше будет так не делать.
            if inferno == False:
                "Я же не такой, правда?"
                # bulka: Подумал, что в руте инферно гг не такой моралист.
        "Мы разделились, каждый взял на себя определённый участок. Опасная тактика, но в замкнутых помещениях наше оружие явно обладает преимуществом."
        "Открываю дверь... Никого.{w} Следующую... Никого."
        "За третьей дверью располагалась капитанская кабина."
        "Я навёл пистолет на того, кто стоял у приборной панели. Он медленно развернулся в мою сторону."
        "Вот это глаза! Жутко смотреть! Точно не человек."
        "— Ты понимаешь меня?"
        "В ответ слышу речь на неизвестном мне языке. Не могу даже различить эмоции."
        "Какие всё-таки жуткие глаза. {w}Нет, по своей природе они не ужасные. Но на человеческом лице они выглядят так пугающе. Я когда-то читал гипотезу про \"зловещую долину\", когда что-то очень похожее на человека, вызывает максимально негативные эмоции, хотя, ничего жуткого в нём нет. Оно просто очень похоже на человека. Но всё же, обладает небольшими отличиями."
        if inferno:
            "Я должен заговорить с ним!"
            menu:
                "Убрать оружие":
                    ""
                "Продолжать держать его на прицеле":
                    ""
            "Я навёл на себя палец и назвал своё имя."
            "Ну уж имена-то у них должны быть?"
            "Персонаж кажется понял меня. Он показал на себя и представился."
            ush "— Уш. [playerName]?"
            
            if stolenFlash:
                "— Держи, пригодится. Я не знаю, что там... Но я украл это в лаборатории."
                "— А ты же всё равно не понимаешь меня..."
                "Я швырнул ему украденную флешку. "
            "Так, этот товарищ обязан выжить. Как его спасти и не вызвать подозрение у отряда?"
            "Просто скажу своим, что всё чисто. А Ушу попытаюсь объяснить жестами, что нужно подождать минут десять и никуда не вылезать."
        else:
            "Это враг. Я должен убить его. Должен."
            if killedPeopleCount>0:
                "Мне уже не впервой убивать людей. Хотя, это даже не человек."
            else:
                if slavaAlive == False:
                    "Почему я не могу это сделать так же легко, как, например, Тенко?"
                else:
                    "Из-за этих тварей погибла моя семья!" with bloodrage
            # Звук выстрела
            "Я проделал в его груди дыру.{w} Контрольный в голову."
            # bulka: Контрольный слишком хладнокровно. Мб при сомнениях только один выстрел с возможностью выживания уша? 
            $ killedPeopleCount += 1
        # Pomis: Так, я примерно понял как вывести на Инферно
        # Pomis: Зачищая корабль, гг, откроет комнату и столкнётся с Ушем, не станет в него стрелять и вручит украденную флешку, если она у него есть. Попытается заговорить, но Уш не владеет русским. Тот спасётся и запросит шпионаж на гг.
        # bulka: В смысле запросит? У начальства или что?
        # pomis: что-то в этом роде, да
    #
    #   Один в лодке (без Марии)
    #
    else:
        ""
