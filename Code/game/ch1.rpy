label ocean:
    
    
    scene bg sky ocean onlayer background
    $ camera_move(0, -10000, 0, 0, 0)
    $ camera_moves( ( (160, -10030, 0, 0, 2, 'ease'),(0, -10000, 0, 0, 4, 'ease') ), loop=True)
    play music "music/123.ogg"
    # scene bg sky
    with fade
    "Я открыл глаза.{w} Всего лишь небо и больше ничего.{w} Слепяще белые облака.{w} Ярко голубое пространство, простирающееся на миллиарды километров ввысь."
    "И звук ветра, затихающий и еле заметный.{w} Я мог бы долго так лежать и любоваться красотой бесконечного космического океана, если бы не одна любопытная мысль, пришедшая мне в голову. "
    "\"А где я?\""
    "Хотя впрочем, мысль я особо развивать не стал."
    "Кругом так безмятежно, тихо и спокойно, что глаза сами закрылись. Ничего не мешает поспать ещё часок, разве что солнце припекает, да и покачивает меня почему-то..{w} опять качнуло. {w}И вдруг я вспомнил."
    with vpunch
    $ camera_move(2500, -8000, 0, 0, 1, 'ease')
    show boat onlayer middle at bottom
    "Так резко вскакивать всё же не стоило: я запутался в каких-то вещах и чуть не упал за борт. "
    $ camera_move(500, -2000, 0, 0, 1, 'ease')
    "Удержав равновесие, я поднял глаза и увидел океан."
    $ camera_moves( ( (660, -2100, 0, 0, 2, 'ease'),(500, -2000, 0, 0, 4, 'ease') ), loop=True)
    "Впереди, слева, сзади — кругом вода. Всё ещё не до конца соображая, я оглядел поверхность на которой стою. "
    "Похоже это лодка. Большая старая деревянная лодка. В фильмах на таких спасаются люди, когда тонут корабли. {w}Наш похоже как раз затонул. "
    $ camera_move(0,0,400,0,0)
    hide boat onlayer middle
    call flashback1
    scene bg sky ocean onlayer background
    show boat onlayer middle at bottom
    $ camera_move(500, -2000, 0, 0, 0)
    $ camera_moves( ( (660, -2100, 0, 0, 2, 'ease'),(500, -2000, 0, 0, 4, 'ease') ), loop=True)
    "Но внезапная волна, окатившая меня с головы до ног, смыла все мои мысли и пробудила от оцепенения. Надо что-то делать. Ведь я всё ещё жив."
    # bulka: И тут мне пришла в голову гениальная идея - сестра выживает, её подбирают инферно и она становится за них. В руте солдата они встречаются (на поле боя?) и она обвиняет его в том, что он её бросил и тд и тп. В общем, полноценный синдром обиженного. В руте инферно они же радостно встречаются и объединяются ради мести человечеству. В одной из концовок они красиво под печальную музыку вместе дохнут. В другой мб инцест замутить (это уже сомнительно)

    with flash
    "Тоня... {w}И мама с папой."
    "Я остался один?"
    "— Не может этого быть, они выжили. {w} Я должен выбраться и найти их - сказал я вслух, успокаивая себя."
    "Но в голове всё мелькали мысли. Взрыв почти расколол корабль надвое, он затонул очень быстро."
    " Наша каюта была внизу. Никаких шансов."
    "— Не может быть..."
    "Я не верил и искал хоть какую-то надежду."
    "— Тоня не была в каюте, она могла спастись."
    "В памяти ожил её образ, последний разговор."
    "— Не последний.{w} Не последний разговор. {w}Она жива. Все мы живы."
    "Нужно взять себя в руки. {w}Что я могу сейчас сделать? Нужно выбраться отсюда."
    "Я попытался отбросить все мысли и решил осмотреться."

    # может тут ещё какой фон?


    "Лодка была завалена всяким барахлом и это не были вещи первой необходимости"
    "Кругом валялись сумки, чемоданы, были несколько кейсов с кодовыми замками, валялась всякая одежда, парочка спасательных жилетов."
    "Как будто в той суматохе кто-то пытался спасти свой багаж. "
    "Обычно спасают людей, а не ценный груз. Но мне же лучше, может найду что поесть."
    "Однако надеждам моим не суждено было сбыться, всё оказалось бесполезным хламом."
    "Никакой аптечки, никаких пайков. Словом, ничего, что могло бы пригодиться в экстремальной ситуации.{w} А я то думал, что это спасательный плот." 
    "Ну и зачем он тогда? Неужели они правда спасали груз?! Я даже был немного возмущён, хотя, конечно, просто пытался таким образом подавить свою панику. "
    "Шансы на выживание таяли. Нет даже ракетницы, меня не заметят, если будут искать."

    "Прохаживаясь по палубе своего, похоже, последнего корабля, я задел что-то ногой. Из-под навеса торчал странный согнутый предмет, похожий на сапог." 
    "Я наклонился и попытался вытащить его, как вдруг понял, что это чья-то нога. Я не один."
    
    "Нога торчала из кучи барахла, состоящего из чемоданов, кейсов и прочего бесполезного мусора."
    "Я начал раскидывать эту гору хлама, чтобы спасти того, кто был под ней. Спустя минуту упорного труда, я смог увидеть владельца ноги, точнее то, во что он был одет."
    "Это был странного вида водолазный костюм, или даже скафандр."
    "Он был серого цвета, и у него был шлем с отражающей поверхностю, что мешало увидеть лицо владельца этого странного костюма. "
    "Вдоль всего тела были странные гибкие трубки, но баллонов с кислородом не было. Никогда не видел ничего похожего."
   
    "Я так увлёкся, разглядывая костюм, что не сразу подумал, что, возможно, человеку нужна помощь."
    "Наверно, нужно снять с него шлем."
    "Это я и решил попробовать, но как только я протянул руки к шлему, человек вдруг метнулся в сторону и мгновение спустя я уже лежал придавленный ногой."
    
    "Направленный на меня предмет я заметил не сразу, но в том что это оружие я не сомневался. "
    "На несколько секунд наступило мёртвое молчание."

    with dissolve
    "-Ээм... привет.."
    "Не реагирует.{w} Может не знает русский? Да и что я вообще несу?"
    "— Хэллоу? Айм э френд."
    "Или ве френд? Хоть я и учился в школе с английским уклоном, но разницу так и не понял. К чертям эти артикли! Сейчас не до них..."
    "Но похоже какой-то эффект всё-таки был, человек сменил стойку и чуть опустил оружие."
    "Я смог повнимательнее осмотреть костюм. Облачение выглядело немного футуристично, и было цельным, никаких замков я не разглядел. "
    "\"Странно это всё\"  - подумал я и тут же осознал что мысли мои как-то совсем не соответствуют ситуации. И в этот момент он поднял одну руку и снял шлем."

    show yuming onlayer forward at center
    "Девушка?"
    "— Чего уставился?"
    "— Ничего."
    "Спина немного болела после внезапного падения."
    "— Ты кто такой? Как тебя зовут?"

    #Тут можно ввести имя!

    "— [playerName]. Я плыл на корабле. "

    yu "— Ааа.. На том самом."

    "— Что произошло? Ты что-то знаешь?"
    "Я с надеждой посмотрел на неё."

    "Она убрала с меня ногу и отошла на другой край лодки."
    yu "— Меня зовут Юминг."
    "Она замолчала. Видно, что она обдумывает ответ."
    yu "— Вчера нашими вооружёнными силами была проведена операция."
    "Вооружёнными силами? Она пилот?"
    "Девушка не торопилась говорить."
    "— Что произошло с кораблём?"
    yu "— Я не могу посвятить тебя во все детали операции.{w} Мы ведём борьбу с террористической организацией Инферно."
    yu "— Вчера мы уничтожили их соединение."
    "Террористы? Операция?"
    "— Что произошло с кораблём?"
    yu "— Он был уничтожен."
    "Она говорит это так спокойно, как будто ничего не произошло. Ещё бы улыбнулась..."
    # Отсылочка к Курску 

    "— Что? Вы уничтожили корабль?"
    yu "Нет.. Это не совсем так."
    yu "В ваш корабль врезалась я. {w} Меня отшвырнуло в вашу сторону."
    "— Отшвырнуло самолёт?"
    yu "— Не самолёт, у меня был другой транспорт... У Инферно продвинутые технологии... В общем вы оказались в гуще сражения. Вряд ли кто-то выжил кроме тебя."
    "Нет. {w}Они выжили. {w}Они должны были выжить..."
    "— Там ведь идёт спасательная операция, да?"
    "Юминг внимательно посмотрела на меня."
    yu "— У тебя были там друзья? Я думаю, наши уже всех нашли, не беспокойся."
    yu "— Дай мне тот кейс. Сейчас и нас заберут."

    "Всё будет хорошо. Всех найдут."
    "Я протянул руку к кейсу и вдруг замер."
    "Там внутри было какое-то устройство, но меня впечатлило не это."
    "Я чувствовал структуру этого устройства, понимал, как оно работает, оно, как будто, стало продолжением меня."
    "— Что это за штуковина?"

    yu "— Это глубоководный передатчик. Запустишь его, и нас спасут."
    "Но я её даже не услышал. Чёрт побери, да что это такое? "
    yu "— А ты похоже не так прост как кажешься. Почуствовал что-то?"
    "Я не выпускал устройство из руки. Постепенно я смог справиться с потоком новой информации, поступающей мне в мозг из этой хрени."
    "Создаётся такой ощущение. {w}Не знаю. Сравнимо с ощущением, когда на глазах повязка. Или насморк. Или беруши в ушах."
    "Понять бы."
    yu "— Ты меня слышишь вообще?"
    "У каждого органа есть предназначение. У этой штуки, очевидно, тоже. Но такое чувство, что она не может справиться с этим."
    "Первый вывод:{w} — Оно сломано!"
    "Вслух? Я это вслух сказал? Или показалось?"
    yu "— Ну конечно сломано, ты посмотри на вмятину! Ничто не вечно при крушении."
    yu "— Таких так ты у нас называют \"способными\". Раз ты такой, то тогда ты имеешь право знать побольше информации."
    "— Какой информации?"
    yu "— Об инферно. Я ведь не всё тебе рассказала. Про тех террористов."
    yu "— В общем, мы на войне. И воюем мы не с террористами. И даже не с людьми."
    "Я всё больше чувствовал, что это сон. Бредовый кошмар, с кораблекрушением и странными людьми."
    yu "— Инферно - это раса. Мы мало чего знаем о них, но их технологии очень продвинуты."
    yu "— Некоторые люди тоже могут ими управлять. Такие как мы. Способные."
    yu "— Но мы воюем и пытаемся уничтожить друг друга. Вчера мы брали их на живца. "
    yu "— Эти кейсы были на корабле и оказались для инферно приманкой."
    "Приманкой? Да что она несёт?"
    menu:
        "— Вы использовали нас как приманку!?":
            "Я уже терял самообладание." 
            with bloodrage
            $ agressionPoints += 1
            yu "— Нет! Я не знала о передатчиках на корабле!"
        "— Что значит \"оказались для Инферно приманкой\" ?":
            yu "— Я не знала о передатчиках на корабле, этого не было в плане операции."
    menu:
        "— Но ты уничтожила корабль!":
            
            $ agressionPoints += 1

        "— Инферно уничтожили корабль?":
            $ agressionPoints += 0
            # bulka: Это обнуление? Или просто +0?

    yu "— Видимо они решили, что на том корабле у нас был коммандный пункт и попробовали пробиться к нему."
    yu "— Но они не смогли, и попробовали отшвырнуть меня."
    yu "— Я не пыталась уничтожить корабль!"


    if agressionPoints>1:
        with bloodrage
        $ camera_move(500, -4000, 400, 0, 1, 'easein') 
        "— Но ты пытаешься оправдаться!"
        $ camera_move(500, -2000, 0, 0, 1, 'ease')
        yu "— Что ты на меня так смотришь? Остынь."
        $ camera_moves( ( (660, -2100, 0, 0, 2, 'ease'),(500, -2000, 0, 0, 4, 'ease') ), loop=True)
        # bulka: Имхо, в старой версии убийства было как-то гармоничнее. А тут слишком быстро как-то получилось. Слишком быстро до этого дошли. Слишком быстро гг разозлися. Слишком быстро убил. Слишком быстро избавился от трупа. Когда она такая весёлая была, а гг её резко ударил, какой-то вопрос о морали сразу возникал, ещё что-то. Как она доставала сырок, которым хотела поделиться. Как гг смотрел на этот сырок и ему было тошно. Как тяжело ему было. Это всё опущено как-то. Го лучше обратно вернём, а то какое-то уг получилось. Ей богу.
    
    "— Расскажи мне про войну."
    "Юминг облегчённо вздохнула. Похоже она давно хотела сменить тему разговора."
    yu "— Думаю, на базе тебе всё гораздо лучше обьяснят. А сейчас мы вызовем спасателей."
    "Юминг стала рыться в вещах, разбросанных по лодке."
    yu "— Стоп. Как так? Мой ноутбук где-то утонул..."
    "Я всё не мог отвлечь своё внимание от чуда техники в моих руках."
    "— Ты говорила, что нас могут спасти, если включить эту штуку."
    yu "— А ты сможешь починить её? {w}Хотя, если у тебя есть небольшие познания в технике, то, будучи \"способным\", ты спокойно сможешь починить практически любую вещь с подобной архитектурой."

    if agressionPoints>1:
        jump rootInferno


    yu "Инферно очень жестоки. Мы все кого-то потеряли на этой войне. "
    "— Хорошо."
    # bulka: Что гг слишком похуистичен выходит. Убил? Хладнокровно избавился. Не убил? И просто хорошо? Мб хотя бы кулаком ударит по кейсу какому-нибудь?
    " Мне не важно, что это за война. Я даже не слышал, что мы воюем с кем-то. Но я найду тех, кто забрал мою семью."
    " Найду. {w}И уничтожу."

    jump rootSoldier


    # "— Эмм... Просто ты мне кое-кого напомнила... Ну, одну знакомую... Не важно. Кто ты такая? И что это за хреновина на тебе?"

    # # show yuming shamed with vpunch
    # show yuming onlayer forward at center
    # with dissolve
    # "И снова получил по голове. Незнакомка тяжело дышала, да и вообще, выглядела, мягко говоря, потрёпанно. Но это ничуть не смущало её, да и за что она меня всё время бьёт? "
    # "Да и разве можно так с незнакомым человеком? Да что с ней не так? Она села и отвернулась от меня, смотря на горизонт произнесла:"

    # g "— Ну ты и болван! У нас захватили исследовательскую платформу, а ты хнычешь о своих знакомых."
    # "Яростный тон сменился на расстроенный. Будто бы, воспоминания только сейчас ударили ей в голову. Я, тем временем, совсем сбился с толку. Понимая, что заново озвучивать предыдущие вопросы бессмысленно, я только спросил её имя:"

    # "— Имя-то у тебя есть, чудачка? "
    # "Она проигнорировала насмешку в моём голосе и спокойно ответила"
    # yu "Меня зовут Юминг. Товарищи называют меня Юми, но ты можешь называть меня только госпожа Юминг. — она рассмеялась. — Шучу, конечно. А ты кто такой, и как сюда попал?"


    # menu:
    #     "Думаю, тебе это лучше известно!":
    #         $ agressionPoints += 1
    #         $ yumingPoints -= 1
    #         "— Как я сюда попал? Думаю, тебе это лучше известно! Я в кои-то веки получил отпуск и отправился в круизное путешествие... А потом произошло кораблекрушение, я помню взрывы. Наш корабль явно кто-то затопил! Твоя работа? "
    #     "Кажется, наш корабль взорвался...":
    #         "— Кажется, наш корабль взорвался... Я помню только яркие вспышки света и панику."


    # "Юминг повернула голову в мою сторону. "

    # # Грубый ответ Юминг
    # if yumingPoints < 0:
    #     yu "— Тебе-то какое дело? Радуйся, что выжил! — она внимательно осмотрела меня. — Лучше придумай, как нам попасть на сушу. Ты хотя бы примерно понимаешь, где мы сейчас находимся?"
    # # Сюда нужен негрубый ответ
    # else:
    #     yu "— И что нам теперь делать?"

    # "Тем временен моё внимание привлекло то оружие, которым она мне угрожала. Может, если удастся выхватить его, она станет чуток учтивее? Да и очень уж любопытно, что это за штуковина такая. "
    # "Оружие лежало на коленях Юминг, осталось дождаться момента, когда она снова отвернётся в сторону моря. Тогда я без особого труда схвачу его за рукоятку. "
    # "—А? Я задумался, о чём ты там говорила?"
    # "Только я это произнёс, как понял, что сейчас снова получу по голове. Но удара не последовало, она фыркнула и отвернулась."
    # "Я выхватил её странное оружие и онемел от удивления. Я чувствовал устройство этого оружия, понимал, как оно работает, оно, как будто, стало продолжением меня. А ещё я понял, что стрелять оно явно не умеет. Скорее, это какой-то передатчик."
    # "Похоже, что вмятина на корпусе лишила его способности работать. Юминг сначала набросилась на меня, но заметила моё оцепенение."

    # yu "—Да ладно? Только не говорите мне, что двое \"способных\" умрут от голода и жары?"
    # yu "—И да, это была глубоководная рация."
    # yu "—Нам нужно попасть на военную базу. Сможешь починить эту хреновину? В этих ящиках должен быть ремонтный набор."
    # "Юминг окинула взглядом разбросанные по лодке кейсы."
    # "Я всё ещё был в оцепенении и не понимал, что происходит. О чём она говорит, какой ремонтный набор?"

    # "—Что это за штуковина?"

    # yu "—Это глубоководный передатчик. Починишь его, и нас спасут. А ну, за дело!"
    # "В её голосе снова появились командные нотки"
    # yu "— Судя по всему, у тебя есть редкая способность управлять таким оборудованием. Я не сильна в этом, тебе всё подробно объяснят на военной базе. "

    # "—Так... Стоп! Да кто ты такая, расскажи уже наконец!"
    # yu "—Ну... раз мы с тобой в одной лодке, уже во всех смыслах, то нет смысла скрывать. Я пилот подводной охранной машины. Мы уже три года воюем с иной цивилизацией — Инферно. Никто пока не знает, откуда они появились, и зачем... Одно мы знаем точно — они хотят нас уничтожать. Медленно и цинично."

    # "—Что? Какой ещё подводная охрана? Какое Инферно? Сама-то в это веришь?"
    # "Я осмотрел её странный костюм, передатчик, и сказанное ею приобретало какой-то смысл."
    # "— А с чего всё началось? "

    # yu "—С того, что эти западные учёные случайно взорвали один из городов Инферно..."
    # menu:
    #     "Как можно было случайно взорвать город?":
    #         $ agressionPoints += 1
    #         "Я уже терял самообладание."
    #         "—Я сама толком не знаю... Да и это не важно. С тех пор они нападают на нас. Давай, выберемся отсюда, и тебе всё расскажут. Почини только эту штуку..."
    #     "Впервые слышу об этом... Расскажи больше!":
    #         $ yumingPoints += 1
    #         show yuming
    #         "Юминг едва заметно улыбнулась."
    #         "—Я сама мало что знаю... Давай, выберемся отсюда, и тебе всё расскажут. Почини только эту штуку..."
    # "—А как ты поняла, что можешь управлять таким оборудованием?"
    # if agressionPoints > 0:
    #     yu "—Да сколько можно спрашивать?? Ну ладно..."
    # yu "Всех, кто моложе 25 лет в нашей провинции проверяли на какой-то там вирус... Но на самом деле проверяли нашу совместимость с этими разработками. "
    # yu "Ну и после эксперимента со мной сразу же связались военные. Выбора у меня особого не было, да и оставаться в своём обедневшем поселении мне не хотелось."
    # yu "Всё, хватит. Чини!"
    # if agressionPoints>1:
    #     menu:
    #         "Я не буду этого делать.":
    #             $ agressionPoints += 1;
    #             jump rootInferno
    #         "—Хм... Ладно, попробую. С чего начать?":
    #             jump rootSoldier
    # else:
    #     "—Хм... Ладно, попробую. С чего начать?"
    #     jump rootSoldier
