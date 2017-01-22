# набор переменных, которые с большой вероятностью удалю
$ preferDarkBeer = False # Предпочитает тёмное пиво светлому
$ askedMarieAboutMan = False # Спросил Марию про наличие у неё мужика

# рут солдата. Юминг жива, с Марией 3 или более поинтов
label ch5marie:
    call talkingAndDrinking
    call landingAlaska
    call meetNewCrew
# TODO: проверить упоминания американских баз по тексту
# TODO: тут Мария должна будет оценить некоторые выборы пользователя в прошлом
label talkingAndDrinking:
    "И вот мы в небольшой, но довольно уютной каюте. Сидим за столиком друг напротив друга, а за иллюминатором постепенно отдаляющийся берег."
    if withMarieInHangar:
        ma "— Снова мы в одной каюте!"
        "— Ты называешь ту крохотную кабину подводной лодки каютой?"
        ma "— Хех. Ну почти. В тесноте, да не в обиде."
        "— Ну да, было бы обидно оставлять тебя там, на базе..."
    else:
        "— Слушай, а как ты выбралась тогда с базы?"
        ma "— Да как... По вентиляционной шахте выползла вместе с остальными, когда удары прекратились."
    ma "Кстати, [playerName]... {w}Тёмное или светлое?"
    menu:
        "Тёмное":
            $ preferDarkBeer = True
            ma "— Значит, любитель тёмной стороны силы?"
        "Светлое":
            "— Свет даёт мне силу!"
            # bulka: Имхо отсылку к варику больше поймут, нежели изменённую к хсу. Но если хочешь - исправь обратно.
    "Мария вытащила из сумки две бутылки пива и протянула одну мне."
    if marieSaidAboutBeer:
        "— Помнится, ты в лаборатории жаловалась, что пиво негде достать..."
        ma "— Ну да, хорошая у тебя память. И мы эту твою память будем заполнять всякими бесполезными знаниями."
        # хитрая ухмылка
        "— Это ещё зачем? Какими?"
    else:
        "— Ого, не думал, что ты серьёзно."
        ma "— А что такого?"
        "— В голову бы не пришло, что ты любитель выпить."
        ma "— О-о-о... Ты меня плохо знаешь. Вот Жорик знал, славный был парниша."
        if withMarieInHangar:
            "— Кажется, он тебя боялся..."
            ma "— Сам виноват."
        else:
            "— Жалко его..."
            ma "— Да. Но это всё-таки война."
        "— Давай не будем о грустном, лучше расскажи, как ты договорилась взять меня с собой?"
        ma "— А... Будут опыты на тебе ставить, ничего особенного."
        # bulka: Проорал на этом моментеXD
        if agressionPoints>3 or humorousPoints<2:
            "— Какие ещё к чёрту опыты?"
        else:
            "— Будут испытывать на мне новое оружие?"

    ma "— Ну никто же тебя просто так бы не взял на военную базу в Америку? Пришлось пойти на некоторые уступки..."
    "— Так, ты что там за меня решила?"
    ma "— Да ничего страшного... Будут испытывать на тебе технологию загрузки памяти. Своих бойцов им жалко, а когда узнали, что..."
    "— Какого чёрта ты меня подписала быть подопытной крысой этих пиндосов?"
    if agressionPoints>2 and leadershipPoints>1:
        # Мария не особый любитель «сильной руки»
        $ mariePoints -= 1
        "— Значит так, я такой хернёй заниматься не буду. Если нужно будет как-то оправдаться перед пиндосами, сама пойдёшь на опыты."
        "Мария разочарованно посмотрела на меня. Такое чувство, что даже если бы я сказал это, угрожая оружием, взгляд был бы точно такой же."
    else:
        "Она издевается или всё же дура, несмотря на свои достижения в науке?"
    ma "— Да ладно, успокойся... Нет такой технологии. У них там проблема с кадрами, нужен кто-то, кто объяснит их салагам, что к чему."
    "— Мне их координатором быть? Я же даже языка не знаю."
    ma "— А сильно он нужен? Например, когда через рацию нейронтовскую общаешься, язык вообще не важен, ты передаёшь смысл, а не слова."
    "— Будь по твоему... На месте разберусь."
    ma "— Хех, я бы не подписала тебя на гиблое дело!"
    ma "— За глобализацию знаний!"
    "Никогда не слышал такого тоста."
    "Мария осушила бутылку залпом и достала следующую. Я же лишь сделал пару глотков."
    "Похоже она настроена серьёзно. Не успел я опомниться, как в ход пошла уже третья бутылка."
    "— Тебе нормально будет?"
    ma "— Ты о чём вообще? Как думаешь величайшие изобретения нашей базы были созданы?"
    "Балмер бы оценил..." 
    # pomis: сложноватая отсылка, но пусть будет
    "— Так вот почему наша база развалилась как карточный домик?"
    ma "— Не говори так! Я там вообще-то много чего дорогого мне оставила!"
    "— Но факт остаётся фактом."
    ma "— Сам ты факт!"
    # bulka: Не совсем понял предложение, так что изменил, хотя всё равно попахивает идиотизмом.
    "Мария обиженно отвернулась и уставилась в стену. Спустя пару секунд потянулась за следующей бутылкой и снова заняла обиженную позу."
    menu:
        "— Но изобретения дейтсвительно неплохие.":
            $ mariePoints += 1
            "Сияющие глаза Марии в этот момент можно было использовать вместо корабельного маяка. Какая она всё-таки предсказуемая."
            ma "— А какое самое великое?"
            "— Хм-м. Думаю, лифт."
            "Первое, что пришло в голову."
            ma "— Лифт и правда восхитительный. Надо будет америкосам такой же сделать!"
            "— Да-а. Думаю, они будут в восторге."
        "— Да ладно, это просто гора слабая была.":
            ma "— Хех. Настолько слабая, что растаяла от первого же рельсотрона."
            "— Действительно. Не из тех пород сделана!"
    "Мария перестала корчить из себя обиженную и осушила третью бутылку. Тем временем, я даже первую ещё не прикончил."
    ma "— Так, это что, была последняя бутылка?"
    if marieSaidAboutBeer:
        "— Я хотел сбегать в магазин перед отправлением, но было уже слишком поздно."
    else:
        "— Тебе знать."
    if withMarieInHangar and mariePoints>3:
        ma "— Ну и ладно, не важно."
        "На щеках Марии стал проступать едва заметный румянец."
        ma "— Я так и не смогла адекватно отблагодарить тебя за твои решительные дейтствия там в ангаре..."
        "Так вот для чего она так старательно осушала бутылки!"
        ma "— Ну я всё равно не знаю, как это сделать."
        "— Ты и так вытаскиваешь меня из дыры. Спасение жизни в обмен на спасение от скуки. Равноценный обмен."
        # bulka: Более очевидная отсылочка.
        ma "— Я бы в любом случае вытащила тебя. Даже если бы не была перед тобой в долгу."
        "Румянец на щеках стал уже превращаться в багрянец."

    if visitedLabDay2==False and promisedMarie:
        ma "— А чего ты не пришёл ко мне в лабораторию? Я же звала тебя!"
        "— Ну... Я же не думал, что база разрушится, думал, загляну попозже..."
        ma "— Да конечно."

    "Надо бы что-то полезное от неё узнать. Может, под пивом она более болтливая? На вид она точно такая же, как обычно."
    menu:
        "— А мужик-то у тебя был?":
            $ askedMarieAboutMan = True
            ma "— М-мужик? В каком смысле?"
            "— Да в самом прямом."
            ma "— Ну, смотря с какой стороны подумать..."
            "— Значит, нет?"
            ma "— К чему вообще такие вопросы?"
            if withMarieInHangar:
                "— А как же Жорик?"
                ma "— Да ничего у меня с ним не было!"
            "Марии явно некомфортно общаться на такие темы, но что хотел — то я узнал. Мужика у неё точно не было."
            # bulka: Мужыг как-то жёстко. Мб парень?
        "— Что же ты обо мне думаешь?":
            ma "— Что я думаю? Ты выглядишь сложным и надёжным одновременно."
            "— Такого описания я в свой адрес ещё не слышал."
            ma "— Ну а я? Что обо мне скажешь?"
            "Если бы люди умели поворачивать ушами, как это делают собаки, то два уха Марии бы сейчас сверлили меня ожиданием комплиментов."
            menu:
                "Хвалить её интеллект":
                    "Ну да, она же всегда радуется от этого."
                    ma "— Знаешь, я это уже от многих слышала, я конечно рада, что ты так считаешь..."
                    "Очевидно, ожидала что-то поинтереснее. Промах."
                    if saidThatBotsAreTrash:
                        ma "— А ещё называл моих ботов бесполезным хламом! Я это на всю жизнь запомнила!"
                    ma "Ладно, проехали."
                "Назвать лучом света в своём мире":
                    $ mariePoints += 1
                    "— Действительно, в этом жестоком мире только ты меня выручаешь и не даёшь окончательно погрузиться в вендетту." # TODO: глуповатая фраза, переделаю
                    ma "— Хе-хе, как мило. Луч света в непроглядной тьме злости и невежества!"
                    "Её глаза засияли угрожающим огнём, а лицо приняло выражение какого-то завоевателя."
                    ma "— Так, чего-то я увлеклась."
                "Не хвалить":
                    "— А ты выглядишь сложной и... Безнадёжной."
                    "Внимательное и приготовленное к получению комплиментов лицо Марии будто бы разрядом в 220В перекосило."
                    "Спустя несколько секунд молчания она немного повеселела."
                    ma "— Да ну тебя. Все знают, что я классная!"
                    # pomis: "Итого у нас 5 ненормальных девушек в новелле"
    ma "— Вот и берег виднеется!"
    "— Выглядит так же холодно, как Россия."
    ma "— Аляска же. Ты думаешь, мы за это время в Калифорнию приплывём?"
    "— И база будет на Аляске?"
    ma "— Ну да. А какая разница, всё равно особо не погулять."
    "— Я всё ещё не понимаю, что я там буду делать."
    ma "— Да я тоже. Разберёмся."
    return

label landingAlaska:
    return

# pomis: ох, как бы сэкономить на количестве персонажей тут... Пусть Саргон умеет управлять несколькими телами-клонами. И пусть на базе количество предателей зашкаливает. А гг предлагается их вычислять и попытаться не повестись на чью-нибудь ложь.
# bulka: Ахахах. http://readmanga.me/ill_boy_ill_girl в помощь. Там автор нашёл отличный способ экономии.
label meetNewCrew:
    "После обеда мы направились на новое рабочее место Марии. Моя роль в этом военном механизме мне всё ещё не ясна. Но всё равно это будет лучше, чем торчать во всеми забытом унылом городе."
    # сцена лаба
    "К нам подошёл очень уверенной походкой мужчина лет сорока в белом халате."
    sa "— Мария, добро пожаловать в команду. Я буду ваш коллега по исследованиям. А зовут меня Саргон."
    ma "— Эм-м, приятно познакомиться."
    "— А я [playerName]."
    sa "— А, так это ты. Вот как ты выглядишь. Наслышан."
    "— Наслышан?"
    sa "— Ну как же, конечно! Операция с кораблём не осталась без внимания."
    "Какой-то подозрительный тип. Или тут все такие?"
    return