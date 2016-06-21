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
        "Когда я вернулся в комнату, Слава делал зарядку."
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
        "Обычное утро. Через пару часов нас снова собрали в квартире 39, говорят, что будет какое-то важное заявление."
        nvl clear
    gen "— Итак. До нас дошла информация о том, что завтра Инферно планирует совершить крупное нападение на Москву. Мы точно не знаем, как они это сделают, но все незанятые солдаты срочно перебрасываются."
    pi "— Откуда такая информация?"
    gen "— От нашего информатора — Рихарда Айсдена. Ему удалось перехватить и расшифровать разговоры."
    if icedenReportsCount==1:
        "Ого, тот самый Айсден, автор доклада!"
    elif icedenReportsCount>1:
        "Ого, тот самый Айсден, автор докладов!"
        # bulka: Это будет развиваться типо?
        # pomis: Будет несколько докладов, разбрасанных по всех ветвям, из которых можно будет получить полную картинку происходящего
    gen "— К сожалению, почти вся наша техника была разрушена в ангаре."
    gen "— По этому, с базы в Екатеринбурге нам отправлены пять Чёрных Стрижей. Некоторые из вас уже знакомы с этими вертолётами. Быстрее только на ракете. Прибытие через час."
    "Даже в Екатеринбурге есть база? Сколько их всего?"
    "..."
    if minoriAlive:
        "Наконец-то мы все расположились в вертолётах. Со мной из знакомых были Юминг, Иван, Минори."
    else:
        "Наконец-то мы все расположились в вертолётах. Со мной из знакомых были только Юминг и Иван."
    yu "— Как дела, солдат?"
    "— Как обычно.{w} Слушай, а с тобой Мария связывалась?"
    yu "— Хм... Нет. Рано ещё наверное. Надеюсь, с ней всё в порядке..."
    pi "— Да что с ней случится."
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
    if agressionPoints>2:# and inferno==False:
        # pomis: здесь это условие уже излишнее, сюда нельзя попасть, если inferno==True
        "Хочется поскорее убить кого-то из Инферно!"
    "Далее мы летели в молчании. Иван уснул, Минори смотрела в окно, я в очередной раз пытался переварить всю новую информацию."
    "Наконец-то мы приземлились."
