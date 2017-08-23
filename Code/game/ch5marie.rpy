# набор переменных, которые с большой вероятностью удалю
$ preferDarkBeer = False # Предпочитает тёмное пиво светлому
$ askedMarieAboutMan = False # Спросил Марию про наличие у неё мужика
$ agreedToPretendHusband = False # Согласился притворяться мужем Марии
$ sargonInsightPoints = 0 # Подозрение Саргона в том, что гг на самом деле солдат. 0 - не подозревает, 3 - уверен.
$ antiSargonPoints = 0 # Подозрение гг в том, что Саргон на самом деле инфернец. От 0 до 3.
# Естественно, выход на хорошую концовку будет, если набрать antiSargonPoints = 3, а на плохую — если sargonInsightPoints = 3.
$ pickedKnife = False # Подобрал нож. Подобрать он мог его и ранее по сюжету. (TODO: дать ему шанс подобрать нож когда-нибудь ранее)
$ needPasscard = False # Знает, что ему нужен электронный пропуск на военной базе

# рут солдата. Юминг жива, с Марией 3 или более поинтов
label ch5marie:
    call talkingAndDrinking
    call landingAlaska
    call meetNewCrew
    jump ch6marie
# TODO: проверить упоминания американских баз по тексту
# TODO: тут Мария должна будет оценить некоторые выборы пользователя в прошлом
label talkingAndDrinking:
    scene bg cabin
    show black:
        alpha 0.0
        linear 1.8 alpha 0.0
        ease 1.0 alpha 0.15
        ease 1.0 alpha 0.0
        repeat
    "И вот мы в небольшой и ужасно неудобной каюте с тусклой и холодной мерцающей лампой. Мария сидела за столиком, а я расхаживал из стороны в сторону, тем временем, за иллюминатором постепенно отдалялся берег."
    

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
    "Мария вытащила из сумки две бутылки пива и протянула одну мне. Корабль слегка пошатнуло, зато лампа перестала мерцать" 
    hide black
    with vpunch # почему-то не работает шаталка тут
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
    "— Так, ты что там за меня решила? Ты нормальная вообще?"
    if saidThatMarieCute:
        ma "— Ну чего ты... Сам говорил, что я милая."
        "Одно другому не мешает.{w} Хотел было сказать я, но вдруг ещё обидится?"
    ma "— Да ничего страшного... {w}Будут испытывать на тебе технологию загрузки памяти. Своих бойцов им жалко, а когда узнали, что..."
    "— Какого чёрта ты меня подписала быть подопытной крысой этих пиндосов?"
    if agressionPoints>2 and leadershipPoints>1:
        # Мария не особый любитель «сильной руки»
        $ mariePoints -= 1
        "— Значит так, я такой хернёй заниматься не буду. Если нужно будет как-то оправдаться перед пиндосами, сама пойдёшь на опыты."
        "Мария разочарованно посмотрела на меня. Такое чувство, что даже если бы я сказал это, угрожая оружием, взгляд был бы точно такой же."
    else:
        "Она издевается или всё же дура, несмотря на свои достижения в науке?"
    ma "— Да ладно, успокойся... {w}Нет такой технологии. У них там проблема с кадрами, нужен кто-то, кто объяснит их салагам, что к чему."
    "— Мне их координатором быть? Я же даже языка не знаю."
    ma "— А сильно он нужен? Например, когда через рацию нейронтовскую общаешься, язык вообще не важен, ты передаёшь смысл, а не слова."
    # bulka: А чё им тогда жорик ртом рассказывал?
    # pomis: Почти ничего полезного
    # bulka: В смысле почему он это ртом делал?
    menu:
        "Усомниться":
            "— Ты уверена?"
            ma "— Да! Верь мне, я учёный."
            "— Когда ты так говоришь, я как раз перестаю верить..."
            ma "— Чего-чего?"
            "— Ничего. Ясно, говорю."
        "Согласиться":
            "— Будь по твоему... На месте разберусь."
            $ mariePoints += 1
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
    # pomis: Ну, это типо абсурдный наезд. Я часто такую фигню несу.
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
        # pomis: К чему?
        # bulka: Закон равноценного обмена. Не помнишь?
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
    "Пока нас вели до автомобилей, холодный ветер успел охладить все мои кости. Дорога была спокойной, я смотрел в окно и внимательно изучал окружение. Внешне база выглядела как какая-то тюрьма: забор с колючей проволокой, предупреждающие таблички, редкие сторожевые башни. Сама же база представляла из себя три пятиэтажки и ангар. По краям расположилось несколько зенитно-ракетных комплексов. Неужели, одного было бы недостаточно? Меня с Марией заселили в довольно просторную комнату с нормальными, не искусственными окнами. И зачем нашим ребятам надо было зарываться в гору, если та гора стала могилой базы? Уверен, эта база, в отличие от нашей, выдержала бы нападение такого же масштаба."
    ma "— Ну, как тебе?"
    "— Непривычно конечно. Но в последнее время у меня всё в жизни меняется с такой скоростью, что это уже стало нормой."
    ma "— Ладно, пошли посмотрим рабочее место..."
    "Мария немного смутилась, явно пытаясь сказать что-то ещё."
    ma "— Кстати, если что, притворись моим мужем."
    "— Что?"
    ma "— У меня не было другого способа взять тебя с собой... Я пыталась раньше сказать, но это сложно..."
    menu:
        "— Да я и не против.":
            $ agreedToPretendHusband = True
            ma "— Думала, ты будешь в бешенстве."
            "— Да ладно, тем более, не самая плохая роль."
            "Мария ещё сильнее смутилась, отвернулась и села за письменный стол."
            "Неловкую паузу прервал стук в дверь."
        "— Ну уж нет, я на такое не соглашался!":
            ma "— Да я правда пыталась сказать!"
            "— Заметно. Что ещё ты от меня скрыла?"
            ma "— Хм-м...{w} Да вроде ничего."
            "— А как же наши дети, которых мы бросили?"
            "Выражение лица Марии сменилось со смущённо-виноватого на издевательский."
            ma "— Они ищут тебя."
            "Кто-то уверенно постучал в дверь."
    "Моя новоиспечённая жёнушка побежала открывать. В комнату вошёл какой-то мужчина в военной форме, но я не стал обращать на него никакого внимания. Он о чём-то дежурно рассказывал Марии, а я изучал интерьер своего нового жилища."
    "Наконец, он ушёл. Видимо, до меня ему нет никакого дела."
    "— Слушай, а что они вообще обо мне знают?"
    ma "— Да ничего. Про твои способности я им не говорила, захочешь — сам расскажешь."
    "— Хм. А чем тогда мне тут вообще заниматься? Я так и не понял."
    ma "— Будешь мне помогать в лаборатории, например. Кофе готовить умеешь?"
    "— Обойдёшься без кофе."
    ma "— Да чего ты такой злой. Совсем меня не ценишь. А на кнопки нажимать умеешь?"
    "— Ну так. Немного программировал, когда учился."
    ma "— Ну тогда поможешь мне с некоторыми расчётами. Там ничего особо сложного. Вряд ли мне тут сразу доверят ассистентов, а отчитываться о работе надо."
    "Эх, а я думал, что шутил, говоря, что в универе меня на секретаря учат..."
    "— Ладно, попробую. Я ведь не могу покидать базу?"
    ma "— Слишком ценными знаниями владеешь, никто тебя просто так не выпустит."
    "— Удручает." 
    ma "— Да ладно тебе, тут хотя бы небо есть. Нам раньше только раз в месяц разрешали выходить наружу, просто выйти ненадолго к пусковым установкам. Жили как гномы в шахте."
    ma "— Ладно, пойдём уже. Покушаем."
    return

# pomis: ох, как бы сэкономить на количестве персонажей тут... Пусть Саргон умеет управлять несколькими телами-клонами. И пусть на базе количество предателей зашкаливает. А гг предлагается их вычислять и попытаться не повестись на чью-нибудь ложь.
# bulka: Ахахах. http://readmanga.me/ill_boy_ill_girl в помощь. Там автор нашёл отличный способ экономии.
label meetNewCrew:
    "После обеда мы направились на новое рабочее место Марии."
    #" Моя роль в этом военном механизме мне всё ещё не ясна. Но всё равно это будет лучше, чем торчать во всеми забытом унылом городе."
    # сцена лаба
    "К нам очень уверенной походкой подошёл мужчина лет сорока в белом халате."
    sa "— Мария, добро пожаловать в команду. Я буду ваш коллега по исследованиям. А зовут меня Саргон."
    ma "— Эм-м, приятно познакомиться."
    "— А я [playerName]."
    sa "— А, ты муж Марии?"
    if agreedToPretendHusband:
        "— Да, он самый."
    else:
        "Ладно, придётся подыгрывать, а то вызову лишние вопросы."
        "— Угу."
    "Саргон пропустил мой ответ мимо ушей и внимательно меня рассмотрел. Как будто нашёл какую-то любопытную деталь."
    # Саргон сразу заметил, что гг не простой лабораторный ассистент. Но он не понимает, знает ли гг о своей способности. Пытается тактично это выведать.
    sa "— А как вы познакомились с Марией?"
    "Какая ему вообще разница? Придётся на ходу что-нибудь придумать."
    if liePoints>2:
        "— Работали в одной лаборатории ещё до истории с Инферно."
    else:
        $ sargonInsightPoints += 1
        "— Учились вместе."
        sa "— Ты вроде бы помладше?"
        "— Ну, не на одном курсе..."
    sa "— Хм-м. Ну и ладно."
    "Довольно жуткий человек. Мне будет с ним неуютно работать, хоть он и знает русский."
    "— А что мы будем исследовать-то? Мне так никто и не сказал."
    sa "— Массовое разрушение связей нейронтов на расстоянии. Так мы сможем уничтожать боевые тела Инферно."
    # Технология интересна Инферно, но сами они не смогли такое создать.
    "— Так вот как они называются."
    ma "— У меня совсем маленький опыт работы с нейронтами..."
    sa "— У меня есть несколько гипотез, нужно будет их проверить, но я не силён в схемотехнике и программировании."
    "Мария заметно повеселела. Кажется, ей Саргон пришёлся по душе."
    ma "— Ну в этом мы хороши!"
    sa "— [playerName], как думаешь, можно ли вообще управлять нейронтами или нервной системой на расстоянии?"
    menu:
        "Конечно, да":
            sa "— Почему же?"
            "— У Инферно даже есть такое устройство. С ним они берут контроль над человеком."
            sa "— Я что-то слышал об этом, но не довелось видеть вживую. Думаю, с такой штукой мы бы сильно продвинулись в исследовании."
            "— Ну оно, к сожалению, на главной исследовательской базе."
            # Откуда же ему, простому лаборанту, знать об этом. Подозрение.
            $ sargonInsightPoints += 1
            "Саргон ухмыльнулся."
        "Даже не знаю. Может быть.":
            sa "— Ну да, звучит бредово."
            "— Хотя подожди. Инферно же управляют какими-то титанами. Издалека."
            sa "— А, точно, забыл. Сегодня сам не свой."
            "Какой-то он очень странный."
            $ antiSargonPoints += 1
    "Тем временем Мария расположилась на своём рабочем месте и запустила какой-то мессенджер"
    ma "— Наконец-то интернет! Ох, надо бы сообщить Юминг, что я в порядке!"
    if yumingPoints>2:
        "Я ведь так почти ничего не узнал об этой китаянке..."
    ma "— Чего-то не проходит звонок."
    nvl clear
    nvlc "Остаток дня Мария ставила какие-то программы на компьютер и пыталась связаться с кем-нибудь из базы. Не то чтобы я к кому-то там сильно привязался, но я немного переживаю за них. {w}Да что с ними вообще могло случиться? {w}Итак, очередной день подошёл к концу, а я так и не приблизился к своей цели отомстить за семью... Я уже сомневаюсь, что это возможно. Да и как мне вообще выяснить, кто именно за этим стоит? Уничтожить Инферно полностью? Не думаю, что это возможно, даже если всё человечество приложит для этого все свои силы. А от меня-то уж это и подавно не зависит.{w} Может...{w} Создать новую семью? С Марией. Мне кажется, она этого хочет. Уже давно стемнело, а эта сумасшедшая читает какую-то научную статью. Я слегка провёл рукой по её светлым локонам и вышел из рабочего кабинета."
    nvl clear
    "Куда пойти перед сном?"
    menu:
        "Слоняться по коридорам":
            $ pickedKnife = True
            nvlc "Пустынные коридоры. Идеально. На меня, наверное, не распространяется военный распорядок дня. Я ведь даже не числюсь как сотрудник исследовательского отдела базы? К моему счастью, все организационные вопросы решала Мария, а моя голова свободна от всей этой ерунды. Чем мне вообще заниматься? Если я не солдат, то я никак не смогу реализовать свою месть по отношению к Инферно. Да и тупой местью я ничего не добьюсь. {w}Пока я бродил по коридорам, моё внимание привлёк предмет в углу. Видимо, кто-то из солдат выронил нож. В хозяйстве пригодится. А теперь, спать."
        "Попробовать выбраться на улицу":
            $ needPasscard = True
            nvlc "Выйти на улицу оказалось не так просто. На выходе нужно было приложить электронный пропуск, которого у меня конечно же, не было. Буду знать, чем завтра заняться. А теперь, пойду спать."
    # TODO: Расписать ситуацию. пока до сих пор не понятно, что происходит с теми персонажами.
    # bulka: Надо бы сделать схему-рисунок, где обозначалась сетка действий для гг, при этом описывались действия и местоположение других персонажей на каждый день, по которой можно было ориентироваться. Иначе довольно сложно каждый раз возвращаться к сюжету после простоя. Аля день первый - гг едет в госпиталь, юминг мертва. Либо гг с юминг летят на базу. И так для каждой развилки. Причём эту хрень желательно в псдшке хранить, ибо редактировать надо будет.
    # pomis: сложно
    # bulka: сложно, но нужно. Ибо как-то кабзец со вложенностью и прочим. Поможет избежать сюжетных дыр.


    # sa "— А, так это ты. Вот как ты выглядишь. Наслышан."
    # "— Наслышан?"
    # sa "— Ну как же, конечно! Операция с кораблём не осталась без внимания."
    # "Какой-то подозрительный тип. Или тут все такие?"
    return