label ch6enlil:
    scene bg black
    en "— Эй, ты живой?"
    "О, знакомый голос! Вот только ответить ей у меня не получилось. Моё тело охватил паралич, будто моё тело принадлежит не мне, а я просто гость в нём. Даже глаза открыть не могу."
    "Голос" "— Да живой он. От телепортации ещё никто не умирал. Хотя, люди тут редкость!"
    en "— А что с ним?"
    "Голос" "— Это тот самый человек, за которым ты должна была следить? Кажется, он не очень удачно скомпилировался после расщипления..."
    "Скомпилировался... Разве можно так говорить про человека вообще?"
    en "— И что теперь с ним делать?"
    "Голос" "— Да шучу я... Всё нормально, со временем придёт в норму. Нервная система не до конца адаптировалась к тому, что произошло. Надо будет провести ещё одно облучение нейронтами, поможет."
    en "— Как маленького ребёнка прямо!"
    "Голос" "— Технически, по меркам нашей физиологии он действительно маленький ребёнок. Так ещё и парализованный."
    # bulka: Разве их физиология настолько отлична?
    "Почему я понимаю их речь? Я тут уже долго?"
    "Голос" "— Кстати, он нас слышит. Мозговая активность меняется когда мы говорим, взгляни!"
    en "— Ничего не понимаю... Это же значит, что ему становится лучше?"
    "Голос" "— Постепенно идёт на поправку. Ему получше, чем его товарищам. Ладно, отвезу его на облучение."
    "Товарищам? Меня действительно куда-то увезли, я слышал удивлённые голоса, шум приборов. Вот только другие органы чувств мне почти не подчинялись. Хотелось бы взглянуть, что происходит."
    "Голос" "— Если ты всё ещё в сознании, приготовься к отключке."
    "Как скажешь..."
    "..."
    # открывает глаза
    "Какая-то непропорциональная комната, площадью чуть больше кровати, но с пятиметровым потолком. Сколько я был в отключке? Надо бы попытаться встать."
    "Вместо того, чтобы встать, я перекатился с кровати на пол. Не могу пошевелить ногами, но руки в норме."
    "Думаю, смогу доползти до двери. Не открою, ну хоть постучу, привлеку внимание."
    "Что же меня вечно заносит в госпитали в разных уголках мира? {w}Если это госпиталь вообще."
    "Вопреки ожиданиям, дверь легко открылась."
    "— Есть кто живой?"
    sl "— Глазам своим не верю! Ты как тут оказался? Куда ты пропал вообще?"
    "— Слава? Что здесь вообще происходит?"
    sl "— Ну, мы провалили миссию, нас всех поймали... Сейчас нас держат в этом здании."
    "— Зачем держат?"
    sl "— Эти сволочи копались в моём сознании. Мне пришлось заново пережить все самые неприятные моменты. И приятные тоже. Так как ты сюда попал?"
    "— Сложная ситуация. Перед тем как улетать на миссию я встретил девушку из Инферно."
    sl "— Что? Вот просто так встретил на улице? Что она там вообще делала?"
    menu:
        "— Искала меня.":
            sl "— Зачем это?"
            "Действительно. Надо как-то выкрутиться. Не знаю, как они попались. Спроси я об этом первым, соврать убедительно было бы проще."
            if liePoints>2:
                $ liePoints += 1
                $ slavaPoints += 1
                "— Они как-то узнали, где мы находимся. Устроили облаву на наш городок."
                sl "— Ого! А нас по прибытии ждала облава!"
                "Как их не убило телепортом? Там же какая-то проверка. Или их перенесли как-то по другому?"
            else:
                "— Вербовала шпионов. Я подумал, что лучшей возможности внедриться в их сеть не предвидится."
                sl "— Как-то странно. И как ты собирался передавать информацию наверх?"
                "— Понятия не имею. Не было времени думать."
                sl "— Ну, судя по тому, что ты находишься здесь, то внедриться у тебя не получилось."
        "— Жила в городе. Они же внедряются в наш мир.":
            $ liePoints += 1
            "— Я сразу узнал её по необычным глазам."
            sl "— Как на том крейсере?"
            sl "— Интересно совпало, что именно в нашем городе."
            "— Да они везде расселяются."
    sl "— Тебе помочь подняться? А то в дверях валяешься всё..."
    "— Да, было бы неплохо."
    "Слава помог мне прислониться к стене в коридоре и сел напротив меня."
    sl "— И как она?"
    "— Со своими странностями. А как наши остальные товарищи?"
    sl "— Вроде бы все живы, но мало кто пришёл в себя после телепортации."
    "— Долго мы тут уже?"
    sl "— Понятия не имею. Тут время вообще по-другому ощущается. Даже по голоду не получится ориентироваться, тут есть какой-то генератор, который снабжает нас всех энергией."
    "— Да, слышал о такой штуке."
    sl "— Ах да. Ещё когда они копались в моём мозгу, мне загрузили базовые знания их языка. Так что, живыми нас точно не отпустят."
    "— Мне вроде бы тоже. Я помню некоторые моменты. Облучали какой-то штукой."
    "Слава задумчиво почесал затылок и посмотрел в сторону."
    sl "— Я так понимаю, мы нужны им для исследований. Обычных людей они всегда могут выловить, а у нас совместимость, вся фигня."
    "— А что говорит генерал?"
    sl "— Не знаю, я его не видел. Из наших видел только Ивана."
    sl "— Мужик совсем подавлен. Паникует и ноет."
    "— А казался таким пофигистом."
    if minoriPoints > 3:
        "— А как там Минори?"
        sl "— Не видел. Иван сказал, что все в отключке."
    elif iscraPoints > 3:
        "— А как там Искра?"
        sl "— Не видел. Иван сказал, что все в отключке."
        sl "— Вот серьёзно, из всех наших ты больше всего волнуешься за неё?"
    elif mariePoints > 2: # Случай когда не попал в рут Марии, но поинтов с ней было больше всего.
        "— А от Марии никаких вестей не было?"
        sl "— Это та учёная с базы? Вообще понятия не имею. А что у тебя с ней?"
        "— Да ничего... Интересный человек."
    sl "— Кстати, а тут есть и другие люди. Правда, общий язык я ни с кем найти не смог. Чухонцы всякие."
    "А вдруг... Может, Тоня тут? Есть ли такая вероятность?"
    "Хотя, если бы он её встретил, то смог бы с ней заговорить и точно бы рассказал..."
    # TODO: описание пары часов безделья
    jump exploreInferno


label exploreInferno:
    en "— Ты всё ещё не можешь ходить?"
    "— Да, как видишь. Целыми днями сижу в комнате и ничего не делаю, я так с ума сойду! Зачем это всё?"
    "— Почему я тут?"
    en "— В тебе сомневаются, вроде что-то такое я услышала."
    "— Тогда зачем меня искали?"
    en "— Да не знаю я, сам спросишь у них. Поехали."
    "Энлиль затащила в мою комнатку некое подобие кресла, парящего над полом."
    en "— Залезай! Только учти, что оно умеет парить на небольшой высоте. А то были случаи. С управлением разберёшься?"
    "Я залез в это кресло. Прикоснувшись ладонями подлокотников я ощутил привычное ощущение подключения к нейроинтерфейсу."
    en "— Погнали!"
    "Мы вышли на улицу. Хоть мы и под землёй, тут довольно ярко. Видимо, реактор работает на полную. Что-то вроде аналога земного дня."
    en "— Тебя ждут в сенате. Я провожу тебя, а дальше сам."
    # TODO: описание города
    jump infernoSenate

label infernoSenate:
    # pomis: Не хочу тут делать историю с Эсхалией.
    # bulka: Не хочешь тут или не хочешь делать сам?
    alil "— [playerName], да? Я Алилум. Мне поручили вести твоё дело."
    "Тот самый Алилум?"
    "— И зачем же его вообще вести?"
    alil "— Я тоже задаюсь этим вопросом, мне это совсем не интересно. Но что поделать."
    alil "— Когда ты был в отключке, твоё сознание перешерстили и убедились, то ты не на 100% лоялен нам."
    alil "— Мы пока не способны полностью прочитать все мысли, но общую картину составили."
    alil "— Тобою движет месть, хочешь отомстить руководству людской самообороны. Правильно?"
    "— Да, всё так."
    alil "— Однако, с нас с тобой объединяет только лишь общий враг. И я совсем не понимаю, как ты можешь быть полезен."
    alil "— Один из руководителей базы сейчас у нас. Остальных ты никак не найдёшь."
    "В кабинет вошёл ещё один представитель их расы."
    # bulka: Один из руководителей базы? Тут как-то по-другому надо. Руководителей комплекса там или ещё что. Ибо он вроде руководил-то базой один, а базы уже нет.
    alil "— О, привет, спецагент-как-тебя-там-зовут?"
    "Спецагент проигнорировал Алилума и обратился ко мне."
    no1 "— Ты всё ещё в их доверии?"
    "— Да, они думают, что я попал сюда случайно."
    no1 "— Боюсь представить, как ты это объяснил. {w}Ладно, к делу. Ты должен доказать свою верность."
    no1 "— Поможешь нам в одном крупном деле. Нужно настроить земное население против правительств."
    "Ничего себе миссия!"
    "— Как вы себе это представляете???"
    alil "— Ладно, я пойду. Ерундой какой-то занимаетесь."
    no1 "— Ваши правительства выделяют слишком много средств на самооборону, а скоро вообще перейдут в наступление. Надо бы развязать протесты, или даже войны, чтобы они отвлеклись."
    "— А я как тут могу помочь?"
    no1 "— Такая крупная операция требует поддержки хотя бы 50% населения Инферно. Будешь выступать с речами о том, какие люди опасные, и будешь пачкать руки уничтожением всяких пацифистов. Один твой товарищ прямо сейчас отправился убивать одну аристократку, выступающую за мир."
    "— А почему именно люди должны убивать этих ваших пацифистов?"
    no1 "— В случае провала получится интересная картина: человек убивает тех, кто за мир с людьми."
    no1 "— Это отразится на общественных настроениях в нашу пользу."
    if leadershipPoint == 0:
        "Я так понимаю, в итоге меня подставят, чтобы как раз это и спровоцировать? Думаю, выбора у меня особо нет."
        "— Ладно, пусть будет так."
    else:
        "— Я так понимаю, в итоге меня подставят, чтобы как раз это и спровоцировать?"
        no1 "— Нет, зачем, это ваш стиль. Мы так никогда не поступаем со своими союзниками."
        "— Как-то неубедительно..."
    "— А про какого товарища вы говорили?"
    no1 "— А... Павел. Вроде с твоей базы."
    if celebratedVictory:
        "Тот самый засранец, который свалил с базы под шумок..."
    else:
        "Тот самый, который скрылся при нападении?.."
    "— Ладно, я согласен на это дело. Но мне нужно время, чтобы освоиться здесь. Я же совсем не понимаю ваши устои..."
    "Надо выйграть время. Может, смогу раствориться в этом обществе."
    no1 "— Даю тебе двое суток. Кстати, наши сутки синхронизированы с тем, что там у вас на поверхности!"
    "— Может хотя бы неделю? И почему я знаю ваш язык?"
    no1 "— О, это наша экспериментальная разработка! Позволяет загружать основы нашего языка прямо в мозг!"
    no1 "— Планируется, что после успешного тестирования разработки, мы будем применять её на всех новорожденных. Вот только мало кто даёт своих младенцев на эксперименты. А большинство людей несовместимы."
    "Да уж. Всегда мечтал стать подопытным кроликом."
    "Интересно, а этот спецагент какого тут звания вообще? Может, его слова вообще ничего не значат?"



    # bulka: Нет. Какой-то бред. Взяли, а теперь мозг парят с лояльностью. Понял бы там вместе с Павлом отправили. Откуда гг знает no1? Или это Уш? Какого фига те, кто так за своих борется, хочет своих же и убивать? Весьма сомнительные развития событий. А зачем его кинули в какой-то домик, где они все свободно перемещаются, раз Слава к нему зашёл? Нах его так корёжить, чтоб он ничё не мог? И тд.
