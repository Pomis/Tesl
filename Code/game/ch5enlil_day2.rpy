label ch5enlil_day2:
    "— Эй, чего разлеглась? Пошла вон!"
    "Что происходит? Почему так холодно?"
    # открывает глаза
    "Я выбежала на улицу. Ну хоть не так холодно, как внутри. Куда идти? Что за чувство пустоты в животе?"
    if portPoints>0:
        "Кажется, тот портальщик говорил, что нужно будет постоянно кушать. А это, значит, чувство голода?"
    else:
        "Кажется, я читала, что людям приходится постоянно кушать. Они ведь не додумались до глобальных излучателей энергии.{w} А это, значит, чувство голода?"
    "Я вышла к дороге. Людей почти не было. Понятия не имею, что делать..."
    "Миссия! Нет, сначала надо утолить пустоту в животе."
    "Где-то рядом должно быть место, где люди решают эту проблему.  {w}Вот, \"продукты\", кажется, это означает место где можно взять еду!"
    # bulka: Очень тянет пошутить про азык-тулек...
    # bulka: Пожалуй, дальше продолжать не буду, ибо, скорее всего, у тебя тут своё видение сюжета, я просто попытался сдвинуть с мёртвой точки.
    "Я неуверенно вошла в помещение."
    "Продавщица" "— Чего тебе? Не местная?"
    "— Не знаю... Я хочу есть."
    if yenBalance>0:
        "— У меня есть деньги, такие подойдут?"
        "Я положила на прилавок несколько скомканных купюр."
        "Продавщица" "— Это что? Китайские? Я не знаю, какой там курс сейчас..."
        "Продавщица" "— Сейчас, поищу."
        "Она достала светящееся устройство и начала нажимать на него."
        "Продавщица" "— Так, китайский юань сейчас стоит 14 наших рублей. Разменяю как-нибудь."
        "Я не понимаю..."
        "Продавщица" "— Ты совсем не похожа на китаянку. Ладно, что ты хочешь есть?"
        "— Что-нибудь самое эффективное, а то у меня сейчас в животе дыра вырастет..."
        "Продавщица" "— Могу разогреть тебе пирожки. Правда, они вчераш... Не важно."
        "— Ну ладно."
        "Продавщица поставила в ящик-разогревашку три небольших, как она из назвала, пирожка."
        "Продавщица" "— А с тебя за них 10 китайских этих. Как их там. Юаней."
        "Я рассчиталась с продавщицей и жадно съела пирожки. Необычный вкус. Не сказать, что противно, но сильно отличается от всего, что мне приходилось есть."
        "Для нас еда не является чем-то жизненно необходимым, мы едим её редко, только ради вкуса, да и не всем это вообще нравится."
        $ hasFood = True
        # bulka: Я, конечно, не эксперт в анатомии инферно, но не уверен, что ей этого хватит/хватит надолго. Мб сделать эту переменную числовой? Или добавить другую лучше, с этим значением? Аля бы выбор похавать или что-то сделать, когда еда уже есть.
        # bulka: Да и что за хрень? Какого фига продавщица в урюпинске знает вообще, что такое юань и ещё их принимает?
        $ yenBalance -= 10;
        "Пока я думала о тщетности земной жизни я забрела в какой-то дворик. Села на скамейку, развернула упаковку пирожков."
        "Хм, выглядит съедобно."
    else:
        "Продавщица" "— Деточка, а деньги у тебя есть?"
        "— А они обязательно нужны?.."
        "Продавщица" "— Ты что, шутишь?"
        menu:
            "Попытаться украсть что-нибудь.":
                $ hasFood = True
                $ hasExtensionCord = False
                "И же это сделать?"
                "Удлинитель всё равно не особо полезен..."
                "Я кинула удлинитель в лицо продавщице, ухватила первую попавшуюся штуковину и убежала."
                "Никогда ничего не воровала. Сердце стучало как бешеное. Я неслась со всех ног и забежала в какой-то дворик."
                "Никого нет, отлично."
                "Я присела на скамью во дворике. Едва переведя дыхание, развернула украденную еду."
                "Не знаю, что это, но выглядит съедобно." #pomis: пирожочек

            "Попытаться договориться.":
                "— Я могу предложить в обмен удлинитель. Вы сможете с его помощью пользоваться электричеством вдали от стен?"
                "Продавщица" "— Да что ты несёшь? Пошла вон отсюда!"

    if hasFood:
        "Я жадно расправилась с пирожками. Пора переходить к моей основной миссии."
        "Надеюсь, я не потеряла бумажку, которую мне вручил Алилум."
        "Отлично, всё на месте. Портрет хоть и примерный, но узнать смогу. {w}Наверное."
        "Он ведь не будет в меня стрелять? Он вооружён..."
        "А мне надолго хватит этой еды?"
        # pomis: пока хз
        "Может, поспрашивать прохожих, видел ли кто человека на рисунке?"
        "А вдруг это будет кто-то из его друзей? Может, лучше самой поискать по городу?"
        menu:
            "Спросить прохожих":
                ""
            "Искать по городу":
                ""
    # pomis: тут будет немного скучного выживания. Не знаю, чем разбавить.
    "Со временем становилось всё теплее. Солнце светило всё ярче и ярче, постепенно освобождаясь от облачной завесы."
    "— Человек! Вы не видели его?"
    "Я развернула бумагу с портретом."
    if iscraPoints > 0:
        isc0 "— О, это же [playerName]. Он сейчас выйдет. Зачем он тебе?"
    else:
        isc0 "— Я так и не запомнила его имя... Он сейчас выйдет. Зачем он тебе вообще?"
    "— Нужен."
    "Стоп, не собираюсь же я выдавать себя? Пора сваливать и наблюдать издалека. Или как?"
    menu:
        "Остаться":
            ""
        "Уйти":
            "— Ладно, спасибо, я пошла."
            if iscraPoints > 2:
                isc0 "— Так, а ну стоять! Кто такая? Зачем тебе понадобился [playerName]?"
                "Ну и взгляд..."
                isc0 "— Только не говори, что случайно встретила, втюрилась, а теперь ищешь по всему городу?"
                "— Ну, примерно так и было..."
                "Плохо, плохо, что делать???"
                isc0 "— Его не интересуют идиотки вроде тебя. А теперь проваливай. Ещё раз увижу — убью."
            else:
                isc0: "— Понятие не имею, зачем он тебе сдался... Впрочем, мне всё равно."
                isc0: "— И зачем ты уходишь, если ты его ищешь?"








    "{w=10}Дальше пока ничего нет"