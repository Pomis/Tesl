# 
#  СОЛДАТСКИЙ РУТ
# 
label ch5day0:
    if sleptInIscraRoom:
        "О боже, только не утро..." with opening
        isc "— О, проснулся."
        "Как я тут вообще оказался?"
        isc "— Ты собирайся, заходил генерал Ганц, через минут 20 нужно быть у него. Какое-то очень важное заявление."
        "— Опять? Ну ладно... Пойду, умоюсь."
        "Вскоре мы уже были в 39 квартире."
    else:
        if celebratedVictory:
            "О боже, только не утро..." with opening
            call flashback5
            sl "— Вставай, ленивый кусок! Пора вершить великие дела!"
            "А, вот оно что... Но всё же, странно."
            "— Какие ещё дела? У тебя есть вода?"
            if slavaPoints>1:
                sl "— Для тебя всегда найдётся... Слава достал из сумки бутылку газировки и протянул мне."
                "— Благодарю."
            else:
                sl "— В кране есть вода. Вставай!"
                "— Да чего такой настойчивый?"
        else:
            "Вот и утро настало... {w}Похоже, Слава не смог доползти до кровати. Что же вчера произошло?"
        "Пойду, умоюсь..."
        "Когда я вернулся в комнату, Слава уже делал зарядку."
        if celebratedVictory==False:
            sl "— Зря вчера не пошёл с нами. Весело было!"
            "— Что-то сомневаюсь."
        if stoodForIscra:
            "Интересно, он злится на меня? Я заступился за его врага. {w}Или не помнит?"
            "Думаю, помнит. Не так уж и много мы выпили."
            "Да и хрен с ним, честно."
        "— Что будет сегодня?"
        sl "— А кто его знает..."
        nvl clear
        "Обычное утро. Если вообще нашу ситуацию можно назвать обычной. Через пару часов нас снова собрали в квартире 39, говорят, что будет какое-то важное заявление."
        nvl clear
    gen "— Итак. До нас дошла информация о том, что завтра Инферно планирует совершить крупное нападение на Москву. Мы точно не знаем, как они это сделают, но все незанятые солдаты срочно перебрасываются."
    pi "— Откуда такая информация?"
    gen "— От нашего информатора — Рихарда Айсдена. Ему удалось перехватить и расшифровать разговоры."
    if icedenReportsCount==1:
        "Ого, тот самый Айсден, автор доклада!"
    elif icedenReportsCount>1:
        "Ого, тот самый Айсден, автор докладов!"
        # bulka: Это будет развиваться типо?
        # pomis: Будет несколько докладов, разбросанных по всех ветвям, из которых можно будет получить полную картинку происходящего
    gen "— К сожалению, почти вся наша техника была в ангаре на базе. Кроме подводных лодок, на которых вы покинули базу, у нас ничего не осталось."
    "Иван разочарованно вздохнул."
    gen "— По этому, с базы в Екатеринбурге нам отправлены пять Чёрных Стрижей. Некоторые из вас уже знакомы с этими вертолётами. Быстрее только на ракете. Прибытие через час."
    "— Даже в Екатеринбурге есть база? Сколько их всего?"
    "Я не услышал ответ на свой вопрос, ну и ладно."
    gen "— Собирайте свои вещички. Через час жду всех на поле за домом. Опоздавшие — дезертиры. На этом всё."
    "Вещички. Были бы они... {w}Мы покинули квартиру 39. Всё стали расходиться."
    isc "— Никто в магазин не хочет?"
    "Какой кошмар, у меня же даже денег нет."
    "— Если ты купишь мне воды и что-нибудь поесть, то я пойду."
    if iscraPoints>3:
        isc "— Да без проблем."
    else:
        isc "— Я куплю себе воду и позволю тебе сделать один глоток, идёт?"
        "— Вот это щедрость."
    isc "— Погнали!"
    "Искра побежала вниз по лестнице. Она не похожа на торопливого человека, но когда дело касается её интересов, она довольно шустрая. И её интересы весьма странные."
    # code322: Тот же момент времени в ch5enlil_day2 
    # сцена — улица
    # pomis: поход в магазин нужен только чтобы объяснить, зачем Искра ждала гг на улице в ch5enlil_day2. Пока нет идей, как его полезно использовать.
    isc "— Ну ты медленный."
    "— А куда спешить? Целый час!"
    isc "— Мне надо найти виноградные конфеты! Думаешь они есть в каждом магазине в этом отстойном городе?"
    "— Зачем они тебе?"
    isc "— Уф, пошли уже. У нас реактивный вертолёт. Хочешь, чтобы тебе уши заложило перед военной операцией?"
    "— Думаешь, тебя спасут конфетки?"
    # bulka: Немножко не понял связи между конфетами, вертолётом и ушами. Жрать конфеты, чтобы не заложило уши в вертолёте?
    # pomis: Когда взлетаешь на обычном самолёте, получаешь перегрузку в ~1.3g, и уже плохо ушам. А у нас же вертолёт, к которому прикручен реактивный двигатель. Он порождает перегрузки в несколько g. Но да, в таком случае от конфет будет немного пользы.
    # сцена — магазин
    isc "— Отлично, конфетки! Возвращаемся!"
    "— Воду возьми мне."
    isc "— Ладно, ладно..."
    # сцена — улица. 
    # cцена — вертолёт
    if minoriAlive:
        "Я последним забрался в вертолёт. Со мной из знакомых были Юминг, Иван, Минори."
    else:
        "Я последним забрался в вертолёт. Со мной из знакомых были только Юминг и Иван."
    yu "— Да хватит ныть, Ваня, никто не даст тебе порулить чужим вертолётом!"
    yu "— О! Как дела, солдат?"
    "— Как обычно.{w} Слушай, а с тобой Мария связывалась?"
    yu "— Хм... Нет. Рано ещё, наверное. Надеюсь, с ней всё в порядке..."
    pi "— Да что с ней случится!"
    "— Кстати, она говорила про какую-то исследовательскую базу в Сибири, почему она не смогла в неё попасть?"
    yu "— О, она мне все уши прожужжала об этом. Вообще, это главная база изучения нейронтов."
    "— Откуда у нас вообще эта технология? Я так и не понял толком."
    yu "— Вот почему ты у меня спрашиваешь? Я похожа на того, кто знает? Вот, тут твой координатор сидит!"
    pi "— А? Чего надо?{w} Технологию позаимствовали с остывших тел лавовых титанов. "
    "— Ну, Инферно же по-другому её используют?"
    pi "— Электричество тоже по-разному можно использовать."
    pi "— На сибирскую базу очень не хотят набирать новых людей. Там уже полностью сформированный и проверенный коллектив. И высочайшая степень секретности. Мы сами о ней знаем не больше, чем я сейчас сказал."
    "— Ну ладно, а сколько всего баз?"
    pi "— У России осталось две. Сибирская и под Екатеринбургом. На последней почти нет своей боевой техники. Зато там обитают сильнейшие технари, которые и занимаются модификацией вертолётов, беспилотников, оружия для других баз со всего мира."
    pi "— А всего около 20."
    "— А у Китая сколько?"
    yu "— Совсем недавно построили две. Но они переполнены, так что, переселяться туда — не вариант. А одна я никуда не хочу."
    pi "— Я вот тоже не пойму, куда нас всех заселят? Не жить же нам всё время в этом унылом городе?"
    if minoriAlive:
        mi "— А нас могут отпустить домой?"
        pi "— Нет конечно."
        if stoodForIscra:
            "Наши с Минори взгляды случайно пересеклись и она тут же повернулась в сторону Ивана."
        mi "— Жалко..."
        pi "— Что поделать? Война же."
        mi "— Я-то тут при чём? Не я же её развязала! И я не хочу умирать за чужой город!"
        if stoodForIscra:
            "Теперь она повернулась ко мне."
            mi "— Я же не способна постоять за себя. Умру первой."
            pi "— Ну опять вы за своё. Неправильный настрой."
        yu "— Все мы когда-нибудь умрём..."
        "Странно слышать это от Юминг."
    "— А что вообще известно о предстоящей операции?"
    pi "— Почти ничего. По прибытии расскажут."
    if agressionPoints>2:
        "Хочется поскорее убить кого-то из Инферно!"
    nvl clear
    nvlc "Далее мы летели в молчании. Иван уснул, Минори смотрела в иллюминатор, я в очередной раз пытался переварить всю новую информацию."
    nvlc "Наш летающий монстр перешёл с реактивных двигателей на лопасти и стал резко снижать высоту. Мы приземлились на импровизированную вертолётную площадку где-то недалеко от жилых высоток. Вокруг разбит небольшой палаточный военный лагерь."
    nvlc "Нам выдали оружие и кратко ввели в курс дела."
    nvl clear
    $ icedenReportsCount += 1
    nvlc "*СРОЧНЫЙ ДОКЛАД Р. АЙСДЕНА ЗА ИЮЛЬ 2049. ПЛАНИРУЕМОЕ НАПАДЕНИЕ НА МОСКВУ*"
    nvlc "26 августа 2049 года нами была замечена подозрительная активность в Москве. Участились упоминания слов, свойственных только для языка Инферно. Мы почти полностью научились расшифровывать их язык. Расшифровав несколько перехваченных разговоров мы узнали о планируемом нападении. Примерное количество участников — 12. Оружие — манипулятор сознанием. Такой же, как при похищении эсминца. Нападение запланировано на вечер 28 августа. В это время будут проходить два чрезвычайно важных в политическом плане события. Кроме переговоров России и Китая, в Госдуме будет подписываться акт о взаимном ядерном разоружении. Скорее всего целью Инферно будет срыв переговоров."
    gen "— Разделитесь на две группы. Одна займётся Госдумой, другая переговорами с китайцами."
    # bulka: И тут я понял, что горстка школьников в очередной раз спасает мирXD
    # pomis: Предлагаю это обыграть. Им не получится спасти мир именно потому что они школьники. Как издевательство над классикой жанра. Не хватит физической подготовки, начнётся истерика, итд
    if leadershipPoints > 1:
        "— И как нам проникнуть туда?"
    gen "— Как вы знаете, у большинства из вас уровень доступа А. Это позволит вам попасть на особо охраняемые территории в сопровождении людей с уровнем доступа А0. Такой есть у меня и..."
    "Генерала перебил громкий голос со стороны."
    no1 "— Так значит, вы и правда способны перехватывать и переводить наши разговоры?"
    "Из-за деревьев вышло несколько десятков вооружённых до зубов людей. Или не людей. Но их в разы больше, чем нас."
    no1 "— У меня возникло такое подозрение, решили проверить. И правда. Сразу же прилетели!"
    gen "— Как вы вообще выследили нас?"
    no1 "— У нас есть заинтересованные люди на вашей базе в Екатеринбурге."
    gen "— Вы же понимаете, что не только среди нас есть предатели?"
    no1 "— Не знаю, к чему ты клонишь. А сейчас вы все последуете за нами."
    "Следом, он достал уже знакомый нам манипулятор сознания и включил. Никто даже не успел среагировать."
    no1 "— Обычные военные нам не нужны. Умрите."
    "Военнослужащие, которые принимали нас тут же упали в конвульсиях."
    "Постепенно мы стали терять даже способность свободно мыслить. Устройство получало полный контроль над нервной системой. Я с трудом понимал что происходит вокруг."
    # какой-то эффект затуманивания
    gen "...Меня таким дешёвым трюком не возьмёшь!"
    "Сознание резким рывком прояснилось."
    no1 "— Надо же, кто-то умеет сопротивляться? Вы нам нужны живыми, как минимум те, кто что-то знает о расположении баз. Так что, извольте успокоиться."
    "Действительно, у нас нет шансов бороться с ними."
    # снова затуманивание. Тем моментом Ганц отправил заранее подготовленный сигнал о том, что их ведут на базу Инферно. 
    

    # Перенос в столицу Инферно

    # pomis: продолжу как решим, что делать с no1 и no2
    # bulka: Немножко неожиданно и непонятно. Московия куда делась?
    # pomis: Они около неё приземлились. Если делать сюжет с Москвой, то это тупик, я вообще ничего придумать не могу нормального
    # bulka: Работать негр! Меня вот с Тенко заставил без тупиков обойтись, теперь страдай.
    # bulka: Непонятно как их подкараулили. Ведь они рядом с москвой приземлились, как я понял. Будто бы инферно заранее знали место посадки.




