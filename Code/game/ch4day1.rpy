label ch4day1:
    sl "— Эй, [playerName], давай, вставай! Генерал выступит с заявлением через 5 минут в квартире 39. Подъём!"
    "— Что? Какой генерал ещё?{w} А..."
    "Слава вытащил подушку из-под моей головы и потянул меня за руку."
    sl "— Подъём!"
    "— Да встаю я... Есть перекусить чего?"
    sl "— Потом покушаешь! Ты не понимаешь, что мы выполнили своё первое боевое задание?"
    menu:
        "— Мы базы лишились...":
            sl "— Зато мы получили бесценный опыт!"
            if minoriAlive==False:
                "— И не только базы..."
                # На экране полупрозрачно всплывает фейс минори
            else:
                "— Дороговата цена такого опыта..."
                sl "— Хватит ныть! {w}Ладно, я побежал!"
        "— Это надо отметить!":
            sl "— Точно! Ты прав! {w}Одевайся давай, я побежал..." 
            $ slavaPoints += 1
            # pomis: Пока хз где делать проверку этих очков. Может в какой-то сюжетной развязке нам будет нужно хорошее отношение Славы
    "Побежал... Откуда в нём столько энергии? {w}Я неспешно собрался и поплёлся на лестничную клетку."
    if pickedManipulator:
        "По привычке засунул руки в карманы.{w} Ох, совсем забыл!"
        "Та штуковина, которой можно управлять людьми. Надо как-нибудь воспользоваться!"
        "Но не сейчас... Да и очень много жертв она производит. И семью мне это не вернёт..."
    "Дверь открыта. {w}В довольно большой комнате собралось человек 10. Из нашего отряда был только Слава."
    if yumingAlive:
        yu "— О, привет, солдат."
        "— Ага..."
    gen "— Итак, раз все собрались."
    "Все? По какому принципу нас тут собрали?"
    gen "— Как вы уже знаете, база разрушена. Выжившая часть персонала эвакуирована."
    # Звук: стук сердца
    gen "— Потери составили около 50%. Большую часть погибших завалило."
    if mariePoints>3 and leadershipPoints>0:
        "— А как там Мария из лаборатории, генерал?"
        "Довольно дерзко было вот так прерывать речь генерала."
        if yumingAlive:
            "Судя по реакции Юминг, её этот вопрос тоже волнует."
        gen "— Научный персонал будет отправлен вместе с оборудованием на базу в Америке. Они дико извиняются за инцидент с кораблём и предоставили нам помещение в своей лучшей базе TESL."
        "— А с нами что будет? Почему нас не отправят туда же?"
        gen "— Вас тоже распределят по базам, скорее всего. Никто не готов принять сразу столько людей. Так что, подождёте немного в этом городе."
    else:
        gen "— По поводу продолжения военной службы. Вам придётся немного подождать в этом городе, пока какая-нибудь база не сможет вас всех принять. Научный персонал вместе с оборудованием отправляется в Америку."
        gen "Американцы дико извиняются за инцидент с кораблём и предоставили нам помещение в своей лучшей базе TESL под лабораторию." 
        sl "— Почему мы отдаём учёных америкосам?"
        gen "— Ты забыл, что мы внеполитическая структура? Что в Америке, что в России, у нас одна цель, один враг."
    gen "— Вопросы?"
    if yumingAlive:
        yu "— Когда отправляются учёные?"
        gen "— Сегодня вечером."
    elif mariePoints>3 and leadershipPoints>0:
        "— Когда отправляются учёные?"
        gen "— Сегодня вечером."

    #     "Наутро я бросился узнавать, как прошла эвакуация."

    

    #
    #   РАЗВИЛКИ.
    #   pomis: Предлагаю в одной из развилок добавить перемещение в прошлое
    #   bulka: Я-то не против. Но что-то мы начинаем слишком далеко от идеи научного реализма отходить.
    if inferno and ushAlive: # Один из вариантов инферно-сценария. Другой вариант будет, если гг пойдёт в тир, вместо ангара в ch3day2
        jump ch5enlil
    elif inferno==False and mariePoints>3: # Не зависит от того, брал ли игрок Марию с собой в лодке. Она в любом случае жива на этот момент. Глава для солдата.
        jump ch5marie
    else:
        jump ch4_9
        "{w=10}Дальше пока ничего нет"