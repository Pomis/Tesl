﻿label ch3day3:
    nvl clear
    nvlc "Остров уплывал всё дальше и дальше. {w}Точнее это мы уплывали от острова, хотя казалось и наоборот."
    nvlc "Мы оказались в открытом море. Собственно, после крушения я ни разу не оказывался в море. {w}Прошло всего лишь несколько дней, но кажется, что пролетели года с того дня, когда всё поменялось.{w} Я столько пережил, столько узнал, столько увидел."
    nvlc "Я окинул взглядом бескрайний океан. {w}Оно того стоило? {w}Я столько сотворил, ещё не поздно остановиться."
    nvl clear
    call flashback4
    nvlc "Какой же мразью я был... {w}Именно поэтому, хотя бы это я должен для неё сделать. Хотя бы в этом я должен быть хорошим братом!"
    # bulka: Хз, какой глагол подойдёт.
    # pomis: Наверное, всё-таки быть
    nvlc "Крепко сжав кулаки, я посмотрел вперёд."
    nvlc "Я отомщу за тебя. И за родителей. За всех, кто умер из-за действий этих военных."
    nvlc "Хотя. Плевать на остальных. Я готов пожертвовать чужими жизнями ради своей цели. На горизонте, по правой стороне, показался корабль."
    nvl clear
    
    "— Что-то не больно-то похоже на технологии Инферно!"
    pav "— Вот чёрт!"
    "Павел резко развернул лодку в противоположную сторону."
    pav "— Это обманка для отвлечения внимания. И мы рядом с ней!"
    # pomis: что за обманка? Вкурить не могу
    # bulka: Корабль, который эсминец. Я тут думаю, что как-то по-другому фразу нужно обозначить.
    # bulka: По сути это нихера не обманка. Они же базу расхерачить пытались этим. Мб оставить, мол это Павел так просто считает?
    "Чудесно. Только в центр сражения угодить не хватало. Сусанин, вашу ж мать!"
    # bulka: Тут они катятся к чертям собачьим
    # bulka: Их подстреливают из отряда юминг
    # bulka: Дальше их спасает советский, тьфу ты, срединный союз. СС
    # bulka: Павел, в зависимости от местоположения звёзд на небе (от мистических условий, которые я ещё не придумал) может выжить, а может нет.
    #"Корабль скорее напоминал цельный кусок металла, чем корабль."
    #"Понятия не имею, чьи это технологии. Не думаю, что люди способны изготовить такой уродливый корабль."
    # pomis: тем временем, на корабле происходит резня.
    # bulka: Резня с натяжкой. Даже с натяжкой не резня. Там же только одну зарезать могу, не более.
    "Мы же уплывали в открытое море. Надеюсь, на корабле нас не заметили."
    if PavelUseless:
        "— Ты знаешь, куда плыть?"
        pav "— Примерно."
        "— Может тогда достанешь карту? А то не хочется проверять своё везение дважды."
        pav "— Посмотри в бардачке."
        "Я достал обычную карту области, в которой мы находились, с непонятными отметками на ней."
        "Пытаясь разобраться в карте, я попутно поинтересовался:"
    "— Ты настолько ценен для Инферно, что ради тебя организовали такую спасательную операцию?"
    pav "— Просто они не бросают своих. У них другой менталитет."
    "Кажется, он их идеализирует."
    if PavelHelp:
        menu:
            "Съёрничать" if PavelHelped:
                # bulka: Мб тут переделать? Он помог нам, а мы выёживаемся. Хотя он вроде тогда выпендрился.
                "— Своих-то может быть и не бросают. Только вот не думаю, что ты для них свой."
                pav "— Тебе никто не говорил, что молчание золото?"
                "Кажется, его это задело."
                menu:
                    "Замолчать":
                        pav "— Так вот, им чуждо понятие предательства. Они ни за что не бросят меня."
                        $ agressionPoints -=1
                    "Продолжить разговор":
                        "— Говорили и не раз. Только я вот всегда отвечаю, что болтовня это серебро. И оно мне больше импонирует, ибо оно отражает всё так, как есть, когда золото есть грязный металл."
                        $ liePoints += 1
            "Узнать поподробнее":
                "— А я за своего считаюсь? Или меня, если что, бросят?"
                pav "— Простого изъявления желания недостаточно.{w} Вот ты сразу стал бы считать другом человека, сказавшего, что хочет быть твоим другом? Стал бы рисковать жизнью ради него?"
                "Ну вполне логично. Хотя и обидно."
                pav "— Однако, если твоё спасение не доставит проблем, то тебя вряд ли бросят."
                # bulka: Что-то инферно слишком хорошими получаются...
            "Промолчать":
                $ agressionPoints -=1
                pav "— Им чуждо понятие предательства. Они ни за что не бросят меня."
                "Надеюсь, меня это тоже касается."
    # bulka: Но мне жалко гробить весь этот пиздатый диаложек. Может их расхуячит в отряд юминг в зависимости от местоположения звёзд на небе (от мистических условий, которые я ещё не придумал). Диаложек происходит, если их не атакуют и не выживает, если атакуют. Правда нахер мне нужен павел дальше? Будет лишней величиной. Может он против гг станет, если гг мирный рут выберет? Тебе павел не нужен? Кому нужен павел, налетай, пока бесплатно.
    # bulka: Я придумал местоположение звёзд на небе (мистическия условия, которые нифига не(ни?) мистические). Какой я классный!
    pav "— Итак, до цели назначения примерно 20 минут."
    "— И что будет дальше?"
    if PavelHelp:
        pav "— Скорее всего нам дадут новое задание."
        "— Новое задание?"
        pav "— А ты что думал? Иждивенцы никому не нужны. Либо будем гражданскими специалистами и обучать их жизни людей, либо отправят на новое задание как шпионов. Как повезёт."
        "Что из этого будет везением, я уточнять не стал."
    else:
        "Этот вопрос остался без ответа."
    "Я решил оглядеться в лодке и обнаружил странный чёрный куб. {w}Он явно был связан с технологией нейроинтов."
    menu:
        "Попробовать активировать его.":
            "Я попробовал активировать его. Он явно работал, но не выполнял своей функции.{w} Такой ощущение, будто звонишь по телефону, но никто не берёт трубку. Видимо, это средство связи."
            "Ну и чёрт с ним. Положу на место раз не работает."
            jump debil
            # bulka: Тута они короч получают пиздюлей от юминг и ко, которые без юминг. Павел тут окочурится скорее всего.
            # bulka: Тут хотел поставить выбор - спросить павла или просто положить на место, но что делать в случае вопроса хз.
        "Спросить Павла.":
            "Я повернулся к Павлу:"
            "— Что это такое?"
            pav "— Положи на место. {w}Аккуратно."
            pav "— Если случайно активируешь, то нам несдобровать. {w}Это передатчик старого типа - их давно научились отслеживать, а потому, если его активировать, с базы кого-нибудь пришлют по наши души. {w}Понятия не имею, что он тут делает."
            "Я аккуратно положил передатчик на места. {w}Хорошо, что я не стал проверять что это."
        "Положить обратно":
            $ nedebil = True
            # bulka: Не знаю зачем это. Может дальше использую... Или нет...
            "Я положил куб на место. {w}Я же не маленький ребёнок, чтобы играть с чем-то непонятным в конце концов."
        # bulka: Надо бы сделать какую-то разницу между вариантами 2 и 3. Ибо разницы выбора нет, а два варианта слишком скучно.
    pav ""
    "До конца пути мы не разговаривали."
    "Наконец показалась земля. Остров или материк это был, я не знал. У меня с детства с географией было туго. А вот у моего соседа по парте и друга с этим проблем не было."
    # pomis: пусть это будет, например, искусственный передвижной остров с ретрансляторами энергии, транспортом под землю, несколькими кораблями.
    call flashback6
    "Мда. Как говорится: пятёрка в школе — тройка по жизни. Вот мне это и аукнулось."
    # bulka: Или "оценки в жизни не помогут". Хз какой вариант лучше.
    "Ну да ладно, сожжённого не восстановить, а мёртвого не воскресить. Поздно думать о том, что уже не поменять. Надо исходить из того, что есть."
    "А есть вот что — неизвестный географический объект. НГО. {w}Так и буду его называть."
    "— Итак, где мы?"
    pav "— Это остров, где находится портал под землю. Из него можно попасть в любой город Инферно. Но нам нужно в столицу."
    # bulka: Первое, что пришло в голову. Можно потом изменить
    # pomis: Я уже расположил столицу Инферно в Умме
    # pomis: А на карте она довольно далеко от мест, где разворачиваются события. Пусть уж лучше они приедут в Ниппур, а из него по телепорту в столицу. Заодно можно будет сделать беседу с портальщиком из рута Энлиль. Reusable персонаж. Так что, поменяю. Но если тебе принципиально, оставь столицу, но до неё реально долго плыть. Или можно сделать так, что из Ниппура портал перенаправит в столицу без необходимости "высаживаться".
    # bulka: Думаю, система порталов будет подразумевать локальную сеть. То из одной точки можно в любую. Тут уже надо рассматривать устройство порталов, а именно способ телепортации. Разборка, перенос сборка. Копирование, уничтожение воссоздание. Абсолютный перенос. Переход через подпространство.
    "Столица? Не слишком ли много чести? Да и разумно ли, пускать людей в свой центр?"
    "Ну да ладно. Мне же лучше. Не очень-то хочется торчать в каком-нибудь захолустье."
    "— Ты знаешь куда идти?"
    pav "— Да, мы обсуждали это заранее."
    "Мы? Он уже полностью ассоциирует себя с Инферно? {w}Ну и чёрт с ним. Просто возьму на заметку на всякий пожарный."
    "Мы направились в глубь острова по еле заметной тропинке."
    "Довольно непримечательный остров. Попади я на такой после кораблекрушения, не подумал бы, что тут что-то есть."
    "Спустя пару минут мы дошли до пещеры в скале. Павел, не замедляя шага, направился внутрь. Я последовал за ним."
    "В глубине пещеры обнаружилась площадка со странным экраном. {w}Точнее, мне подумалось, что это экран. Технология нейронтов?"
    pav "— Дотронься до этой штуки."
    "Ну ладно."
    "Высветились голубые буквы, которые позже сложились в слова, из которых в свою очередь сложилось стихотворение."
    "{color=#00CDFF}{i}От колыбели до могилы \nНе нам решать, что забывать.\nПокуда есть в нас ещё силы, \nНам не дано врагов прощать.{/i}{/color}" 
    "Эм, что? {w}Они этим хотели меня поразить? Или что?"
    "— И что они этим хотели сказать?"
    pav "— Можешь считать это испытанием. {w}Или ты думал, что они пустят тебя в свою столицу просто так?"
    pav "— Система, с помощью нейронтов проверила тебя на схожие с Инферно ценности — не предашь ли ты их. Каждому высвечивается что-то своё, на языке доступном для понимания."
    "Так вот почему не было адекватных разведданных о внутреннем устройстве городов Инферно... {w}Довольно умно, однако."
    "— А что высветилось тебе?"
    "Вопрос остался без ответа, ибо в это мгновение мы провалились в тьму."
    # TODO: Где-то выше надо заебашить знакомство со срединным союзом. Ибо он тут скоро понадобится, если вообще будет."
    # pomis: можно впихнуть их представителей в пещеру. Типо они выследили гг с Павлом и ждали
    # bulka: Немножко странно, когда тот, кто следит, оказывается на месте раньше. Вообще, в планах было убить павла по дороге (необязательно с помощью гг, даже скорее без его помощи), а его бы спас этот союз. Но пока я не уверен в его надобности, ибо, когда уже обрисовался сюжет, эфемерная организация с эфемерными целями кажется нахуй не нужной. Хотя К`тун его знает.
label debil:
    "Через пару минут произошло что-то странное..."
    # bulka: А что произошло дальше, вы узнаете в следующей серии. До скорых встреч по ту сторону сетевого кабеля!
    # bulka: Ну или не в следующей. Филеры никто не отменял.
    "Всё происходило будто в полусне. {w}Сначала что-то громко запищало на приборной панели."
    pav "— Какого чёрта? Как они нас выследили?"
    # bulka: Тут можно будет вхерачить миниигру, где на лодке с видом сверху игрок уворачивается от летящих снизу экрана торпед.
    # bulka: Хз, что тут делать.