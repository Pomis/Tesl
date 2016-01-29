image bg underwater = "images/underwater.jpg"

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
    scene bg underwater with flash
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
        gen "— Ракетами с базы мы его взять не можем, слишком хорошая система ПРО. Арсенал для подводных боёв почти полностью бесполезен против эсминца. Остаётся только абордаж."
        "Что? Он серьёзно?"
        # bulka: хз, ещё в прошлый раз бросилось в глаз, что можно ракетами изблизи херачить, раз абордаж возможен. Или дно протаранить, раз лодка такая крепкая, что выдерживает падение больших кусков бетона.
        # pomis: имел ввиду ракеты на военной базе. Лодки ими не оснащены. А по поводу прочности лодок была мысль. Можно выбор сделать чисто для сохранения логичности.
        menu:
            "Поспорить":
                "— Генерал, а почему мы не можем просто протаранить корабль?"
                gen "— Я уже составил план абордажа, нет времени изменять тактику."
                "Даже так. Ну и бред. Врезался и всё, делов-то!"
            "Согласиться":
                "Что-то не хочется спорить с этим человеком..."
                # bulka: Надо тут что-нибудь сделать. Ведь мы заявляли, что каждый выбор что-нибудь делает. Да и просто делать выбор без влияния не комильфо. 
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
        jump abordaj

    #
    #   Без Марии в лодке
    #
    else:
        "И как ему ответить? Нас не инструктировали. Может, надо что-то нажать?"
        "Без толку..."
        "— Меня кто-нибудь слышит?"
        "— Эй!"
        "Без толку..."
        if yumingAlive:
            yu "— Приём, это Чайка.{w} Подкрепление через две минуты."
            "Забавный позывной. И как ей ответить?"
            gen "— Мы начнём операцию без вас. Присоединяйтесь сразу, как сможете."
            
        # TODO: какие-нибудь размышления, диалогс
        jump abordaj


label abordaj:
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
        ten "— Там кто-то шевелился."
        "Вот это хладнокровие."
        # bulka: Ахахах. Там кто-то шевилился. Будто насекомое. Правда больше напоминает имба лолек-кудере, чем планированный архетип, ну да ладно. Мб исправлю потом. 
        # pomis: Значит, я не так понял этого персонажа
    "Тут палубу корабля сотряс запуск очередного снаряда из рельсотрона."
    "Мы в это время бежали к месту, откуда велось управление этим жутким оружием."
    "По пути мы убили троих военнослужащих в американской форме. Не ясно, люди это, или нет. По всем внешним признакам это обычные люди, вот только ведут себя как какие-то куклы."
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
            "Вслепую пытаюсь управлять солдатами как куклами."
            if slavaAlive:
                sl "— Не увлекайся, мы поняли, что может эта штука."
            "Может, это делается так? Голосовые связки находятся где-то тут. Попробую сказать \"Привет\"!"
            "Нет, не выходит..."
            "Солдат рухнул на землю. От удивления я выронил устройство и подбежал к солдату. Пульса нет."
            $ killedPeopleCount += 1
            mi "— Ты что, убил его?"
            ten "— Я сам собирался обоих убить, так что не вини себя."
            "Невинного человека убил... Просто так. Да что за монстр я такой?"
            mi "— Или он сам умер? Я ничего не могу понять!"
            "Да я сам не понимаю ничего..."
            ten "— В любом случае, это войдёт в мой отчёт."
            if inferno:
                "Да чего я переживаю из-за какого-то солдатика? Это же шикарнейшее оружие! Надо оставить себе!"
            # TODO: Взаимодействие с оставшимся солдатом
        "Хотя... Возможно, ты прав.":
            ten "— Я всегда прав!"
            # TODO: Переделаю.
            # bulka: Тенко самоуверенный, но не напыщенный.
            "Тенко без тени жалости расстрелял безоружных военнослужащих."
            # ввожу метку "TODO: " для удобства поиска мест, которые нужно расписать
            # TODO: Диалогов сюда
            # bulka: Хз, зачем эта метка. Обычных каментов хватало. Тем более в главе, которая в процессе активной разработки. 
            # pomis: чтобы поиском находить по фасту
    if slavaAlive:
        sl "— Убить всех остальных подозрительных существ! Встретимся у лодок через 20 минут!"
        "Похоже, отряд безоговорочно подчиняется ему."
    else:
        "— Думаю, наша задача выполнена. Кто-нибудь взял рацию с собой?"
        "Молчание в ответ. Отлично."
        ten "— Мы должны зачистить корабль."
        ten "— Разделимся и зачистим каждую комнату."
        ten "— А я за рацией, доложу ситуацию генералу. Встретимся у лодок через 20 минут!"
        if strangerAfraidPoints>1:
            "Отряд принял Тенко за главного, даже не знаю, хорошо это или плохо. У меня мурашки по коже от этого типа."
            # TODO: переделаю.
        else:
            "Отряд принял Тенко за главного, ну и хорошо. Он хороший стратег и способен сохранять хладнокровие. "
            "А ещё он способен убивать без колебаний."
            if inferno:
                "Мне тоже нужно стать таким."
                # bulka: Подумал, что в руте инферно гг не такой моралист.
            else:
                "Я же не такой, правда?"

        # bulka: Что-то я его всё меньше узнаю. Честно говоря этот персонаж не планировался как такой бравый парень и лидер. Скорее именно стратег, тот кто управляет из тени. Кто не возьмёт на себя ответственность. Максимум как зам. Быть лидером - это ограничевать себя, а Тенко не любит ограничений. В этом момент ещё можно оставить, но в остальном лучше будет так не делать.
        # pomis: Так лучше? Отправил товарищей зачищать, а сам ушёл прохлаждаться в лодку
    if minoriPoints>0 and inferno==False:
        "Я уже собрался побежать, как почувствовал, что кто-то держит меня за рукав" 
        mi "— Давай вместе, вдруг тебе будет страшно одному?"
        "Уж кто бы говорил... Хотя, думаю, она просто не могла по-другому сказать."
        menu:
            "Нет, каждый должен сделать это сам.":
                "Она разочарованно опустила глаза."
                if slavaAlive:
                    $ slavaPoints += 1
                    "— Он прав, ты солдат или кто?"
                mi "— Ясно..."
                # bulka: Минус пойнт минори? Или она не такая?
            "Разве что за тебя будет страшно, пошли.":
                # bulka: Это с улыбкой надо сказать наверное.
                $ minoriPoints += 1
                $ withMinoriOnZumwalt = True
        
    "Мы разделились, каждый взял на себя определённый участок. Опасная тактика, но в замкнутых помещениях наше оружие явно обладает преимуществом."
    "Открываю дверь... Никого.{w} Следующую... Никого."
    "За третьей дверью располагалась капитанская кабина."
    "Я навёл пистолет на того, кто стоял у приборной панели. Он медленно развернулся в мою сторону."
    "Вот это глаза! Жутко смотреть! Точно не человек."
    "— Ты понимаешь меня?"
    "В ответ слышу речь на неизвестном мне языке. Не могу даже различить эмоции."
    if withMinoriOnZumwalt:
        mi "— Боже, кто это?"
    "Какие всё-таки жуткие глаза. {w}Нет, по своей природе они не ужасные. Но на человеческом лице они выглядят так пугающе. Я когда-то читал гипотезу про \"зловещую долину\", когда что-то очень похожее на человека, вызывает максимально негативные эмоции, хотя, ничего жуткого в нём нет. Оно просто очень похоже на человека. Но всё же, обладает небольшими отличиями."
    if inferno:
        "Я должен заговорить с ним!"
        menu:
            "Убрать оружие":
                "Думаю, нам будет проще понять друг друга, если я уберу пушку."
                # bulka: Надо учесть минори тут.
            "Продолжать держать его на прицеле":
                "Кто знает, на что он способен? Хоть я и не считаю его врагом, а вот он может выкинуть какой-нибудь фокус против меня."
                # bulka: Нет влияния выбора.
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
            # bulka: Мб сделать как я в шахматах? Отдельное условие для инферно рута, отдельное для солдатского. В смысле требование очков.
            $ killedPeopleCount += 1
            "Отчаянно жму на спусковой крючок ещё несколько раз. {w}Сдохни! Сдохни!"
            $ ushAlive = False
        else:
            "Это же не человек. Это враг. Его можно убить. Да?"
            $ ushWonded = True
    "Надо осмотреть остальные помещения. {w}Я в спешке обошёл ещё несколько помещений, но никого в них не нашёл. Почему такой пустынный корабль?"
    if withMinoriOnZumwalt:
        "И куда пропала Минори? Совсем забыл про неё!"
        if ushAlive:
            $ minoriAlive = False
            "Я побежал в капитанскую кабинку. На полу лежала истекающая кровью Минори с рассечённой шеей. Рядом лежал нож."
            # bulka: Вторая неплохая смерть, что берёт за душу. Неплохо будет развить как-нибудь. Потом ещё каких-нибудь сожалений/кошмаров запилить.
            "Сам убийца отхаркивался кровью в углу."
            "— Ах ты тварь!" with bloodrage
            "Я в ярости изрешетил пришельца пулями."
            # bulka: Не совсем понял, это уш убил? Не думаю, что его так быстро сливать нужно, ибо он один из главных антагонистов. Во всяком случае у нас пока другие не намечаются. Разве что второй. Если же не уш, то не совсем понятно как связано ранение уша со смертью минори.
        else:
            "Я побежал в капитанскую кабинку. Она стояла неподвижно и смотрела на тело пришельца на полу."
            "— Ну чего ты встала-то? Это же не первая смерть, которую ты видишь!"
            "— Пошли уже!"
            "Я взял её за руку и повёл к месту встречи."
    else:
        "Пора идти к месту встречи..."
        jump reunion

label reunion:
    if withMinoriOnZumwalt and minoriAlive:
        "Мы вышли на палубу. Ого, сколько народу!"
    else:
        "Я выбежал на палубу. Ого, сколько народу!"

    if yumingAlive:
        yu "— Давно не виделись!"
        "Да вроде бы недавно виделись..."

    if slavaAlive:
        sl "— Как ситуация?"
    else:
        stranger "— Ну, как успехи?"

    if minoriAlive == False:
        "— Эти твари убили Минори!"
        "Я изрешетил пришельца в ответ."
        # bulka: не понял к чему эта строчка. Тут уже их нет вроде.
    elif inferno==False and withMinoriOnZumwalt and ushAlive==False:
        "— Был обнаружен и убит один пришелец."
    elif inferno:
        "— Никого не обнаружил... Как-будто корабль-призрак."
        stranger "— Как мы поняли, большая часть экипажа погибла от несовместимости с устройством управления сознания."
    else:
        "!Если этот вариант выполнился, то где-то ошибка."

    # TODO: диалогов и объяснений

    #
    #   РАЗВИЛКИ.
    #
    if inferno and ushAlive: # Один из вариантов инферно-сценария
        jump ch5enlil
    elif mariePoints>3: # Не зависит от того, брал ли игрок Марию с собой в лодке. Она в любом случае жива на этот момент. Глава для солдата.
        jump ch5marie
    else:
        ""


        # Pomis: Так, я примерно понял как вывести на Инферно
        # Pomis: Зачищая корабль, гг, откроет комнату и столкнётся с Ушем, не станет в него стрелять и вручит украденную флешку, если она у него есть. Попытается заговорить, но Уш не владеет русским. Тот спасётся и запросит шпионаж на гг.
        # bulka: В смысле запросит? У начальства или что?
        # pomis: что-то в этом роде, да
    
