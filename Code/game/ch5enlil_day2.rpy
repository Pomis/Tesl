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
    "Где-то рядом должно быть место, где люди решают эту проблему. {w} Вот, «продукты», кажется, это означает место где можно взять еду!"
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
                $ enlilHasFood = True
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

    if enlilHasFood:
        "Я жадно расправилась с пирожками. Пора переходить к моей основной миссии."
        "Надеюсь, я не потеряла бумажку, которую мне вручил Алилум."
        "Отлично, всё на месте. Портрет хоть и примерный, но узнать смогу.{w} Наверное."
        "Он ведь не будет в меня стрелять? Он вооружён..."
        "А мне надолго хватит этой еды?"
        # pomis: пока хз
        # "Может, поспрашивать прохожих, видел ли кто человека на рисунке?"
        # "А вдруг это будет кто-то из его друзей? Может, лучше самой поискать по городу?"
        # menu:
        #     "Спросить прохожих":
        #         ""
        #     "Искать по городу":
        #         ""
        # TODO: что-то сделать с этим. Какую-нибудь неприятную сценку.
        # bulka: В каком плане неприятную? Она встретит гопников и её по кругу пустя.. точнее отпинают?
        # pomis: как вариант. Неприятную для персонажа
    # pomis: тут будет немного скучного выживания. Не знаю, чем разбавить.
    "Со временем становилось всё теплее. Солнце светило всё ярче и ярче, постепенно освобождаясь от облачной завесы."
    "— Человек! Вы не видели его?"
    # code322: Тот же момент времени в ch5day0
    "Я развернула бумагу с портретом."
    if iscraPoints > 1:
        isc0 "— О, это же [playerName]. Он сейчас выйдет. Зачем он тебе?"
    else:
        isc0 "— Я так и не запомнила его имя... Он сейчас выйдет. Зачем он тебе вообще?"
    "— Нужен."
    "Стоп, не собираюсь же я выдавать себя? Пора сваливать и наблюдать издалека. Или как?"
    menu:
        "Остаться":
            isc0 "— Странно это. И ты странная. Ещё линзы нацепила какие-то."
        "Уйти":
            "— Ладно, спасибо, я пошла."
            if iscraPoints > 3:
                isc0 "— Так, а ну стоять! Кто такая? Зачем тебе понадобился [playerName]?"
                "Ну и взгляд..."
                isc0 "— Только не говори, что случайно встретила, втюрилась, а теперь ищешь по всему городу?"
                "— Ну, примерно так и было..."
                "Плохо, плохо, что делать???"
                isc0 "— Его не интересуют идиотки вроде тебя. А теперь проваливай. Ещё раз увижу — убью."
            else:
                isc0 "— Понятие не имею, зачем он тебе сдался... Впрочем, мне всё равно."
                isc0 "— И зачем ты уходишь, если ты его ищешь?"
    isc0 "— Как тебя зовут, чудачка?"
    "— Энлиль, а что?"
    "Открылась дверь и из неё выскочил парень очень похожий на того, что был нарисован."
    if iscraPoints>1:
        isc0 "— [playerName], ну наконец-то. Тебя тут какая-то чудачка Энлиль ищет."
    else:
        isc0 "— Ну наконец-то. Тебя тут какая-то чудачка Энлиль ищет."
    "И показала на меня пальцем."
    "[playerName]" "— Зачем меня искать..."
    "Мы пересеклись взглядами."
    # анимация смены POV в героя
    "Она точно из Инферно. Эти глаза я ни с чем не спутаю. Да и выглядит странно в целом."
    isc "— Ты знаешь её?"
    "— Давняя знакомая."
    isc "— Как её зовут?"
    # TODO: интерактивности
    "Засада."
    "— Я так и не узнал... Всё было быстро. Подожди немного, мы поговорим наедине."
    if iscraPoints>2:
        isc "— Что там у вас было? А?"
        "— Да не важно, погоди..."
    "Я отвёл эту загадочную девушку в сторону. Заметно, что она сильно нервничает."
    # сцена — дорога
    "— Ну и зачем ты меня ищешь?"
    en "— Захотелось найти. Что такого?"
    "— Знаешь, ничего особенного. Просто не каждый день встречаюсь с наблюдателями из Инферно."
    en "— О чём ты вообще говоришь?"
    "— Ну а кем ты ещё можешь быть? Никто не знает, что я тут. Да ещё и эти глаза. Я уже видел такие. И вообще ты странная, хватит притворяться."
    en "— Что глаза? Это линзы!"
    "— Ну раз ты не та, за кого я тебя принимаю, ответь мне на один вопрос, на который сможет ответить только человек. Ответит сразу, не задумываясь."
    en "— Спрашивай всё что угодно!"
    "Энлиль напряглась и внимательно меня слушала."
    "— Столица Инферно."
    en "— Умма.{w} Ой..."
    # bulka: Вот это было эпичноXD
    "Боже, неужели это сработало?"
    "— Ты самый бесполезный шпион из всех, которые только возможны. Вот прямо самый."
    "Энлиль виновато опустила голову."
    "— Только извиняться не вздумай. Так зачем ты меня ищешь?"
    en "— Алилум сказал, что ты потенциальный сторонник. Мне нужно было следить за тобой и докладывать любую ценную информацию."
    "— Думаешь, я знаю Алилума? Неужели у вас нет нормальных шпионов?"
    en "— Прости... Я старалась..."
    "— Да зачем ты передо мной-то извиняешься?"
    en "— Действительно. Кстати, ты ведь и вправду потенциальный сторонник?"
    "— Возможно... Я просто хочу найти тех, кто виноват в гибели моей семьи. И я склоняюсь к тому, что это не вы."
    en "— Понятия не имею о твоей семье. Если это произошло во время одной из карательных вылазок, то это точно наши постарались."
    "— Карательных вылазок?"
    en "— Наши правители поклялись убить два миллиона ваших жителей в ваших же городах."
    "— Нет, это было в океане."
    en "— Тогда не знаю... Не слежу за новостями."
    "— Я могу попасть в ваш город? Хочу узнать всю правду."
    en "— Хм... Думаю, да. Сейчас, я сообщу Алилуму."
    if iscraPoints>3:
        isc "— Куда собрался? А меня одну с теми придурками оставишь?"
        "Она что, всё время нас подслушивала?"
        en "— А вот тебя я с собой не возьму!"
        isc "— Пошла вон, инопланетная сучка!"
        "Судя по всему, Искра хоть и ругается, но не агрессивно на неё настроена."
        isc "— Значит, уходишь?"
        "— Должен же я докопаться до правды."
        isc "— Верно... Будешь дезертиром, кстати."
        "— Да пофигу."
        isc "— Вот совсем не хочется отпускать тебя, да ещё и с какой-то идиоткой. Но это ради общего дела! Добудь как можно больше информации!"
        "— И как я тебе её потом передам?"
        isc "— Найди способ. Чудная, у вас там интернет есть?"
        en "— Интернет? Глобальная информационная сеть? У меня на работе есть устройство для доступа, но оно не работает..."
        "— Ну ещё бы, под землёй-то!"
        # bulka: Не знаю почему, но проржался.
        "Искра нацарапала мне на руке адрес своей электронной почты. Она что, затачивала свои ногти?"
        isc "— Ладно, не буду задерживать. Оставайся на связи!"

    "— Ну так, как мне попасть к вам?"
    en "— Я сама не знаю, надо спросить Алилума. Да ты погоди. Я же вряд ли когда-нибудь снова попаду на поверхность. Покажи мне, как у вас тут всё устроено."
    "— Ты же тут не первый день?"
    en "— Так-то да. Но меня тут встретили холодно."
    "Как порадовать пришельца в самом унылом городе в мире?"
    "Думаю, для неё будет в радость то, чего нет у них самих. Может, к берегу её сводить?"
    "Я спросил путь у прохожего. Идти, как оказалось, несколько километров."
    en "— А нам не придётся голодать в пути?"
    "— Кстати, да. У тебя денег не найдётся?"
    if yenBalance>0:
        en "— Да, есть какие-то."
        "Энлиль протянула скомканные иностранные купюры. На вид японские."
        "Мы дошли до ближайшего банка и разменяли их. На полученные рубли купили перекусить и направились к океану."
    else:
        en "— Нет, совсем..."
        "— Ты самый бесполезный шпион из всех, которые только возможны! Как ты собиралась выживать в нашем мире?"
        en "— Я не думала, что это так важно... А у тебя самого есть деньги?"
        "— Хм. Нет."
        "— О, смотри, тут во дворе есть яблоня. Лучше, чем ничего!"
        "Энлиль с любопытством пошла за мной."
        "Нарвав кислых зелёных яблок, мы пошли к океану."
    "Мы идём уже почти час. За это время Энлиль рассказала в подробностях свои три последних дня вплоть до встречи со мной."
    # pomis: а это — логическое объяснение происходящему ранее
    "Внизу виднелась бескрайняя гладь океана. Не самые приятные воспоминания."
    "Мы кое-как спустились по крутому склону к берегу. Благо, склон каменистый, спускаться перешагивая с камня на камень гораздо проще, чем пытаться удержать равновесие, спускаясь по земле. Да уж, странно, что эта недошпионка не разбилась."
    en "— Ого! А мы можем войти в него? Он такой шумный!"
    play music chaiki
    "Океан действительно был довольно шумный: волны не на шутку разыгрались. Весь берег был усыпан вулканическим песком."
    "— Не думаю, что стоит это делать."
    en "— Да ладно, пошли!"
    "Энлиль побежала навстречу стихии."
    menu:
        "Попытаться остановить.":
            $ leadershipPoints += 1
            $ triedToStopEnlil = True
            "— Остановись!"
            "Я побежал следом за ней, но расстояние между мной и Энлиль больше, чем между ней и океаном."
            en "— Смотри сколько воды!"
            "Отвлекается вообще на всё. Точно догоню.{w} Схватил её за руку."
            # pomis: пробелы после {w} по канону
            "— Ну и куда ты побежала? Ты представляешь, какой он холодный?"
            en "— Есть только один способ узнать!"
            "Она попыталась силой вырваться, но бесполезно."
            "— Нет, на самом деле, есть два способа. Не обязательно забегать в него, можешь просто окунуть в него руку."
            en "— Хм, и правда. Отпусти!"
            "Энлиль выждала момент между бушующими волнами и проверила температуру океана."
            en "— Прохладно. Ну и ладно."
        "Наблюдать.":
            $ lazynessPoints += 1
            $ enlilPoints += 1 
            # Любопытство Энлиль удовлетворено
            "Забавная картина."
            en "— Смотри сколько воды!"
            en "— Холодно!"
            "Энлиль сбила с ног первая же волна, а мне же пришлось вытаскивать её из воды."
            "Да уж, этот океан намного холоднее Средиземного моря, где затонул мой корабль..."
            "— Ну как?"
            en "— Круто! Т-только зубы стучат."
            "И как её отогревать теперь? Не собой же? Отдал ей Славину толстовку."
            "Мы отошли от берега и укрылись от ветра между деревьями."
            "Энлиль присела около старой ели и обхватила ноги руками."
            "— Какой ты себе представляла «поверхность»?"
            en "— Более тёплой во всех отношениях. Но мне тут нравится. Столько всего нового."
            "— Я даже не знаю, что тут тебе ещё показать, это очень унылое место, да и у меня нет никаких средств для существования и, тем более, путешествий."
            en "— Я поняла, сейчас попробую выйти на связь со своими."
    "Энлиль достала какую-то штуку, внешне похожую на гранёный булыжник."
    en "— Алилум, приём-приём!"
    alil "— Да, знакомы?"
    if enlilRude>0:
        en "— Что за вопросы? Ты мне поручил шпионить за человеком!"
    else:
        "Энлиль явно растерялась от такого вопроса и не сразу нашла, что ответить."
        en "— Эм... Да. Ты мне поручил шпионить за человеком!"
    alil "— А, точно. И как успехи? И почему ты говоришь по-русски?"
    # pomis: вот не могу вспомнить, знает Алилум русский, или нет, потом поищу.
    en "— Он сейчас сидит рядом со мной и хочет попасть в Инферно. Пусть понимает, о чём мы говорит. Он точно на нашей стороне!"
    alil "— Как ты это поняла? В прочем, не важно. Отправлю вам транспорт, тут уже решат, что с ним делать. У меня своих дел полно."
    en "— А что за транспорт?"
    alil "— Лодка. На ней доплывёте по островка с порталом в Умму."
    en "— А как мы найдём островок?"
    alil "— А эта лодка сама вас довезёт. Если вы не додумаетесь включить ручное управление."
    alil "— А если додумаетесь, то там где-то валялся атлас. Разберётесь."
    en "— Кажется, вспомнила! У нас в центре работали над улучшением какой-то людской лодки!"
    alil "— Всё, не отвлекай меня больше."
    "Я не стал вмешиваться в их разговор. Лодка на автопилоте? Значит, не мы одни позаимствовали технологии."
    "Минут через 20 к берегу приплыла лодка. Как в неё забраться и снова не промокнуть?"
    "Энлиль, не задумываясь, побежала к лодке. Сильные волны прибили лодку к берегу и Энлиль без проблем в неё залезла."
    "— И как мы её на воду спустим?"
    en "— Так вытолкай её!"
    "— Ты не заметила, какие там волны? И какая там холодная вода!"
    "Энлиль даже не дослушала меня и стала изучать лодку."
    "— Ладно, подождём, пока утихнет."
    "Я залез в лодку, улёгся в уголке и вздремнул."
    call flashback7
    # pomis: а дальше будет аналогия твоему путешествую в лодке с Павлом. 
        # bulka: Иииииииииииииииииии зачем? Хотя в случае Павла это тоже не очень расписано, однако, там была возможность, что его скомпромитировали. Да цель, в принципе, была выполнена. Тут же действия инферно вообще непонятны. Нах он им сдался? Просто выход в тот же рут, что с Павлом?
        # pomis: вербовка шпионов, все дела.
        # bulka: Ну такое. Слишком палевно выводить человека из организации такой, чтобы просто шпионом сделать.
        # pomis: Не знаю. Придумаю что-нибудь.
    en "— Просыпайся уже! Нам надо плыть!"
    "Волны действительно утихли, ладно. Я выполз из лодки и вытолкал её на воду. Что за чертовщина с моим сознанием? Мне становится сложнее вспомнить лицо сестры, вместо этого появляются другие образы. Да ещё и в таком виде, будто бы они реально происходили."
    "Пришлось немного промокнуть, пока залезал обратно."
    "Спустя минуту, зажужжал мотор лодки. Действительно, автопилот!"
    nvl clear
    nvlc "Берег уплывал всё дальше и дальше.{w} Точнее это мы уплывали от берега, хотя казалось наоборот."
    nvlc "Я снова в лодке. Прямо как после кораблекрушения.{w} Прошло всего лишь несколько дней, но, кажется, что пролетели годы с того дня, когда всё поменялось.{w} Я столько пережил, столько узнал, столько увидел."
    nvlc "Я окинул взглядом бескрайний океан. Эта гладь, расстилающаяся на тысячи километров, стала частым гостем моих ночных кошмаров.{w} Подумать только! Я убивал людей! Я столько всего сотворил! Оно того стоило?{w} Ещё ведь не поздно остановиться?"
    # bulka: "Какие громкие слова, но какова же им цена?" Убивал людей? Тут счётчик как и там, откуда скопировано, надо поставить. Точнее проверку на него. Хотя такие самобичевания как-то унылы. Особенно, учитывая то, что если убил соседа, то совесть не должна мучить, а без него не так уж много. А ещё учитывая то, что он продолжает за "плохих" играть.
    nvl clear
    call flashback4
    nvlc "Какой же мразью я был...{w} Именно поэтому, хотя бы это я должен для неё сделать. Хотя бы в этом я должен быть хорошим братом!"
    nvlc "Крепко сжав кулаки, я посмотрел вперёд."
    nvlc "Я отомщу за тебя. И за родителей. За всех, кто умер из-за действий этих военных."
    nvlc "Хотя. Плевать на остальных. Я готов пожертвовать чужими жизнями ради своей цели."
    # bulka: Да мля, он же только что самобичеванием по поводу чужих смертей занимался. Совесть гг ветренней куртизанок столичных...
    nvlc "Чем я вообще могу быть полезен Инферно? Зачем они организовали за мной слежку? Я же сейчас даже не смогу вернуться в строй."
    nvl clear
    en "— О! Мы почти приплыли!"
    "На горизонте виднелся маленький островок, а лодка плыла прямиком к нему. Спустя минут 5 мы уже выбрались на берег."
    en "— И куда идти?"
    # bulka: 50/50, звонок другу, помощь аудитории?
    "— Звонок другу!"
    en "— Точно... Но ведь он просил не беспокоить. Да и не друг он мне!"
    "— Звони давай."
    en "— Ладно-ладно..."
    "Энлиль, выражая явное недовольство и нежелание вытащила свой странный телефон."
    en "— Алилум, это снова я. Куда идти на острове?"
    alil "— От лодки напрямую иди по тропинке."
    "Мы направились в глубь острова по еле заметной тропинке.{w} Не знай мы о ней, мы бы вряд ли ещё увидели."
    "Довольно непримечательный остров. Попади я на такой после кораблекрушения, не подумал бы, что тут что-то есть."
    "Спустя пару минут мы дошли до пещеры в скале. Энлиль слегка смутилась и предложила мне войти первым."
    "В глубине пещеры обнаружилась площадка со странным экраном.{w} Точнее, мне подумалось, что это экран. Технология нейронтов?"
    en "— О, это же людской проверятор! Дотронься для него!"
    "— Он правда так называется?"
    "Ну ладно."
    play music pixel
    "Высветились голубые буквы, которые позже сложились в слова, из которых в свою очередь сложилось стихотворение."
    "{color=#00CDFF}{i}От колыбели до могилы \nНе нам решать, что забывать.\nПокуда есть в нас ещё силы, \nНам не дано врагов прощать.{/i}{/color}" 
    "Эм, что?{w} Они этим хотели меня поразить? Или что?"
    "— И что они этим хотели сказать?"
    en "— Что-то вроде испытания.{w} Проверяет, что твои ценности схожи с нашими. Забыла сказать, что если бы ты не прошёл тест, то тебя бы..."
    "— Убило?"
    en "— Ну да."
    "Она серьёзно? Так вот почему не было адекватных разведданных о внутреннем устройстве городов Инферно...{w} Довольно умно, однако."
    "— Что дальше?"
    "Вопрос остался без ответа, ибо в это мгновение мы провалились в тьму."
    call nightmare_teleport
    # jump ch6enlil
    # pomis: попробую набросать план, не могу без ориентира
    # гг и энлиль попадают в Инферно.
    # гг изучает город
    # узнаёт историю инферно
    # при наличии поинтов с Искрой поддерживает с ней связь, далее обнародовают всю информацию об Инферно
    # широкий общественный резонанс вынуждает мировых лидеров провести переговоры с инферно
    # всплывают личные дела сотрудников tesl. ГГ узнаёт всю правду о битве в первой главе.
    # Если поинтов с бабами недостаточно, идёт наказывать организаторов. Далее, например, умирает от рук Славы. (Каратель. Плохая концовка)
    # б) ГГ мутит с Энлиль если хватает поинтов. (Замутить с инопланетянкой. Хорошая концовка.)
    # в) ГГ мутит с Искрой, вместе с ней организовывает топовую кару для лидеров tesl (Каратель. Хорошая концовка.)









    "{w=10}Дальше пока ничего нет"