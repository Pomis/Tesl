# bulka: Тут всякие имейджи и тд...
label ch4.9:
    # bulka: Пока пишу под рут солдата. Возможны исправления для инферно.
    # bulka: И вообще, пока это спинофф/ова/тайная глава/хз что.
    "После битвы мы решили отметить победу."
    "Для этого выбрали бар в городке недалеко от базы."
    # "Фактически, он являлся посёлком городского типа для персонала базы."
    # bulka: Мб, это как-то пригодится для рутов с энлиль или просто. А может и нет. Потом в каментах.
    "Здесь было большинство моих знакомых с базы, а, учитывая со скольки людьми я успел познакомится, то компания вышла небольшой."
    # Действующие персонажи: Юминг, Минори, Слава, Мария. Тенко сюда добавлять не буду пожалуй, ибо это не соотвествует персонажу пожалуй. Мб зависит от знакомства в классе. Посмотрим. Альфа версия это короч.
    "Ну и ладно. Я никогда не любил большие компании, ибо чувствовал себя лишним. Тут же вышло довольно лампово."
    # bulka: Не уверен насчёт слова "лампово"
    # bulka: Пока что буду вести повествование. Диалогов тут будет мало, так что их надо будет добавить.
    "Мы сели за столик и начали выбирать напитки."
    "Я никогда не бывал в подобных заведениях, а потому выбрать что-то конкретное я не мог. Я просто листал меню и не мог выбрать выпивку."
    "А вот для Юминг со Славой таких проблем не было. Судя по всему, они частые гости в подобных заведениях."
    "Однако, похоже я не один такой. Минори и Мария испытывали похожие трудности. Это утешает. Не люблю выделяться."
    "Я остановил выбор на молочном коктейле с алкоголем. Минори заказала тоже самое.Марии же помогла выбрать Юминг."
    "Слава выбрал себе достаточно большую порцию тёмного пива и глушил её большими глотками. Вот это он даёт!"
    "Во время застолья зашёл разговор о бое."
    sl "— Я его так, а он меня так, потом я его так!"
    "Какой интересный рассказ. Аж дух захватывает (нет)."
    "И тут я вспомнил о том, что убил человека. Ком подкатил к горлу. Я глотнул коктейля."
    "Не сказать, что я очень чувствительный человек, но, видимо, меня разморило от выпивки. Мда, на пустой желудок пить было не лучшей идеей. Ну да ладно."
    "Юминг болтала с Марией, а Минори разговорилась со Славой. Вот уж не думал, что они смогут так легко общаться."
    "Из-за того, что все разбились на пары и болтали на скучные темы, я лёг на руки и ушёл в себя."
    "Всего лишь из-за праздного любопытства я убил человека."
    "Из-за того, что, как маленький ребёнок, стал играться с тем, чего не понимаю."
    "От самобичевания меня отвлекла Юминг, настырно тыкая меня в плечо пальцем. Больно однако."
    "Я приподнялся и огляделся."
    "Прислушавшись к их разговору, я понял, что ничего интересного в их репликах не появилось, но Юминг стало скучно. Я ей что, клоун что ли, чтобы развлекать? Потерпишь, не маленькая."
    "Я лёг обратно."
    "Тычки продолжились."
    "Да сколько можно?!"
    "Надо что-то придумать, чтобы она от меня отстала. Что-то интересное."
    "Я приподнялся и увидел, что Юминг болтает по телефону. Ей что, двоих собеседников не хватает, раз она меня достаёт?"
    "О, эврика! Придумал."
    "— Если ты опять начнёшь меня тыкать, то я начну лапать тебя за грудь."
    "Как не посмотри, отличная идея. Если она отстанет, то я смогу отдохнуть. А если нет, то можно будет насладиться её реакцией."
    "Отличный способ отомстить за историю в море."
    sl "— О, а ты мужик!"
    "Слава показал большой палец."
    "М, причём тут мужик? Никогда не понял этого фетиша. Я ещё понимаю, что девушку на это реагируют, но в чём кайф для парня? Самоутвердиться? Такое себе."
    "Минори залилась краской. Как же это мило."
    if mariePoints<3:
        ma "— Она тебя не слышит."
        "Мария, видимо, перебрала с алкоголем, но ей явно было интересно, что будет дальше."
    yu "— Помнишь сон, о котором ты мне говорила... *шёпотом* о мужике!"
    "Это выглядело очень мило, когда Юминг понижала голос, обсуждая эротические сны своей подруги, чтобы её никто не слышал."
    "Да, конечно мы тебя не слышим. Особенно я."
    "Я дождался пока она договорит и повторил угрозу."
    yu "— Я тебе полапую!"
    "Отлично, кажется это подействовало. Пора ложиться обратно."
    "Только я лёг, как потыкивания продолжились."
    "Твою ж дивизию, да сколько можно! Тебе совсем что ли делать нечего?!"
    "Что ж, пора приводить в исполнение план Б."
    if mariePoints<3:
        menu:
            "Обдумать":
                "Хотя нет. Что если это не она меня тыкает. Весьма неловоко получится. Надо убедиться."
                "Я решил прислушаться к их разговору."
                "Всё-таки это она! Мало того, она меня теперь тыкает не пальцем!"
                menu:
                    "Быстро схватить за грудь":
                        "Виновна! Зажигай костёр!"
                        "Я приподнялся. Кажется, она забыла о моей угрозе. А я вот не забыл."
                        "Что ж. Тем интереснее."
                        "Быстрым движением я схватил её за грудь. Как-то жестковато. Она там что, бронелифчик носит?"
                        "Вот это она подпрыгнула!" 
                        "Я, конечно, ожидал, что реакция будет интересной, но это превзошло мои ожидания."
                        "— Это будет тебе уроком на будущее!"
                        "Хотел сказать я, но мощный удар по челюсти не дал мне сказать и слова."
                    "Медленно потянуться к груди":
                        "Я медленно потянул руку в сторону Юминг."
                        "Зато быстро полетел под стол."
                        $ neutral = True
            "Схватить за грудь.":
                $ marieJoke = True
                "Быстрым движением я приподнялся и схватил её за грудь."
                "Упс, кажется, это Мария тыкала в меня трубочкой. Неловко получилось."
                yu "— Ах, да как ты смеешь?"
                "— Извини!"
                "Хотел было сказать я, но мощный удар в челюсть не дал и шанса мне на оправдания."
    else:
        "Хотя нет. Что если это не она меня тыкает. Весьма неловоко получится. Надо убедиться."
        "Я решил прислушаться к их разговору."
        "Всё-таки это она! Мало того, она меня теперь тыкает не пальцем!"
        menu:
            "Быстро схватить за грудь":
                "Виновна! Зажигай костёр!"
                "Я приподнялся. Кажется, она забыла о моей угрозе. А я вот не забыл."
                "Что ж. Тем интереснее."
                "Быстрым движением я схватил её за грудь. Как-то жестковато. Она там что, бронелифчик носит?"
                "Вот это она подпрыгнула!" 
                "Я, конечно, ожидал, что реакция будет интересной, но это превзошло мои ожидания."
                "— Это будет тебе уроком на будущее!"
                "Хотел сказать я, но мощный удар по челюсти не дал мне сказать и слова."
            "Медленно потянуться к груди":
                "Я медленно потянул руку в сторону Юминг."
                "Зато быстро полетел под стол."
                $ neutral = True
    "Вашу ж мать, а я и забыл, что она солдат!"
    "Как же больно!"
    if yumingPoints >= 1:
        "Я повернулся и увидел раскрасневшееся лицо Юминг, что обхватила свою грудь левой рукой."
        "— Знаешь, тебя корабли не выдерживают, а ты тут людей со всей дури бьёшь..."
        "Резкая боль в щеке прервала моё негодование."
        "Пощёчина? Не удар?"
        "Юминг повернулась и со слезами на глазах убежала прочь."
        "Кажется, я перегнул палку.
        if marieJoke:
            "Мария с укором посмотрела на меня."
            "Что ты на меня пялишься? Это всё из-за тебя так получилось!"
        else:
            sl "— Не, ну так нельзя..."
            "Слава посмотрел на меня с укором."
            "А кто только что про мужика разглагольствовал?"
        menu:
            "Побежать за Юминг":
                ""
            "Остаться за столиком":
                ""
                # bulka: Тут её мария пойдёт утешать.
    elif yumingPoints >= 0:
        ""
    elif neutral == True:
        yu "— Будет тебе уроком на будущее!"
        "Мда. Надо было действовать быстрее."
    else:
        "Я повернулся и увидел разгневанное лицо Юминг с занесённым кулаком для второго удара."
        "Надо срочно что-то делать."
    # bulka: Тут, наверное, Славик сотворит какую-то херню и всё обойдётся. А в первом варианте Юминг убежит обиженная, а гг пойдёт извиняться. Возможно полапать грудь/ещё что-то будет зависеть от выбора игрока. В любом случае, я что-то сделал по сюжету наконец.
    # bulka: История выдумана. Все совпадения с реальными персонажами случайны. Хотя первая часть не абсолютна, то вторая верна.
