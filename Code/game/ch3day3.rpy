﻿label ch3day3:
    "Остров уплывал всё дальше и дальше. {w}Точнее это мы уплывали от острова, хотя казалось и наоборот."
    "Мы оказались в открытом море. Собственно, после крушения я ни разу не оказывался в море. {w}Прошло всего лишь несколько дней, но кажется, что пролетели года с того дня, когда всё поменялось.{w} Я столько пережил, столько узнал, столько увидел."
    "Я окинул взглядом бескрайний океан. {w}Оно того стоило? {w}Я столько сотворил, ещё не поздно остановиться."
    call flashback4
    "Какой же мразью я был... {w}Именно поэтому, хотя бы это я должен для неё сделать. Хотя бы в этом я должен быть хорошим братом!"
    # bulka: Хз, какой глагол подойдёт.
    # pomis: Наверное, всё-таки быть
    "Крепко сжав кулаки, я посмотрел вперёд."
    "Я отомщу за тебя. И за родителей. За всех, кто умер из-за действий этих военных."
    "Хотя. Плевать на остальных. Я готов пожертвовать чужими жизнями ради своей цели."
    "На горизонте, по правой стороне, показался корабль."
    "— Что-то не больно не больно похоже на технологии Инферно!"
    pav "— Вот чёрт!"
    "Павел резко развернул лодку в противоположную сторону."
    pav "— Это обманка для отвлечения внимания. И мы рядом с ним!"
    # pomis: что за обманка? Вкурить не могу
    # bulka: Корабль, который эсминец. Я тут думаю, что как-то по-другому фразу нужно обозначить.
    # bulka: УУУУууу, я плывуууууу.
    # bulka: Сложна в таком состоянии думать, ааааааааа
    "Чудесно. Только в центр сражения угодить не хватало. Сусанин вашу ж мать!"
    "Корабль скорее напоминал цельный кусок металла, чем корабль."
    "Понятия не имею, чьи это технологии. Не думаю, что люди способны изготовить такой уродливый корабль."
    # pomis: тем временем, на корабле происходит резня.
    # bulka: Резня с натяжкой. Даже с натяжкой не резня. Там же только одну зарезать могу, не более.
    "Мы же уплывали в открытое море. Надеюсь, на корабле нас не заметили."
    "— Ты знаешь, куда плыть?"
    pav "— Примерно."
    "— Ты настолько ценен для Инферно, что ради тебя организовали такую спасательную операцию?"
    pav "— Просто они не бросают своих. У них другой менталитет."
    "Кажется, он их идеализирует."
    if PavelHelp:
        menu:
            "Съёрничать" if PavelHelped:
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
    # TODO: Выставить переменных/ещё чего. Ибо тут ни одна менюшка ни на что ни влияет...
    # pomis: вообще хз какое влияние тут сделать
    pav "— Итак, нам плыть примерно 20 минут."
    "— И что будет дальше?"
    pav "— Плыть."
    "С этими словами он посмотрел на меня как дурака. {w}Пожалуй вопрос в самом деле был глуповат."
    #bulka: Честно говоря, я не знаю как они доберутся до портала. Хотя как они переместятся в город и события перед этим я представляю. Похуй, посмотрим в общем.
    "До конца пути мы не разговаривали."
    "Наконец показалась земля. Остров или материк это был, я не знал. У меня с детства с географией было туго. А вот у моего соседа по парте и друга с этим проблем не было."
    # pomis: пусть это будет, например, искусственный передвижной остров с ретрансляторами энергии, транспортом под землю, несколькими кораблями.
    call flashback6
    "Мда. Как говорится: пятёрка в школе - двойка в жизни. Вот мне это и аукнулось."
    # bulka: Или "оценки в жизни не помогут". Хз какой вариант лучше.
    "Ну да ладно, сожённого не восстановить, а мёртвого не восскресить. Поздно думать о том, что уже не поменять. Надо исходить из того, что есть."
    "А есть вот что - неизвестный географический объект. НГО. {w}Так и буду его называть."
    "— Итак, где мы?"
    pav "— Это остров, где находится портал под землю. Фактически, он находится над их столицей - Кагонес."
    # bulka: Первое, что пришло в голову. Можно потом изменить
    "Столица? Не слишком ли много чести? Да и разумно ли, пускать людей в свой центр?"
    "Ну да ладно. Мне же лучше. Не очень-то хочется торчать в каком-нибудь захолустье."
    "— Ты знаешь куда идти?"
    pav "— Да, мы обсуждали это заранее."
    "Мы? Он уже полностью ассоциирует себя с инферно? {w}Ну и чёрт с ним. Просто возьму на заметку на всякий пожарный."
    "Мы направились в глубь острова по еле заметной тропинке."
    # bulka: Вроде тут в глубь пишется раздельно. Не уверен.
    "Довольно непримечательный остров. Попади я такой после кораблекрушения, не подумал бы, что тут что-то есть."
    "Спустя пару минут мы дошли до пещеры в скале. Павел, не замедляя шага, направился внутрь. Я последовал за ним."
    "В глубине пещеры обнаружилась площадка со странным экраном. {w}Точнее мне подумалось, что это экран. Технология нейронтов?"
    "Высветились голубые буквы, которые позже сложились в слова, из которых в свою очередь сложилось стихотворение."
    "{color=#00CDFF}{i}От колыбели до могилы \nНе нам решать, что забывать.\nПокуда есть в нас ещё силы, \nНам не дано врагов прощать.{/i}{/color}" 
    "Эм, что? {w}Они этим хотели меня поразить? Или что?"
    "— И что они этим хотели сказать?"
    pav "— Можешь считать это испытанием. {w}Или ты думал, что они пустят тебя в свою столицу просто так?"
    pav "— Система, с помощью нейроинтов проверила тебя на схожие с Инферно ценности- не предашь ли ты их. Каждому высвечивается своё на языке доступном для понимания."
    "Так вот почему не было адекватных разведданных о внутреннем устройстве городов Инферно... {w}Довольно умно, однако."
    "— А что высветилось тебе?"
    "Вопрос остался без ответа, ибо в это мгновение мы провалились в тьму."
    # TODO: Где-то выше надо заебашить знакомство со срединным союзом. Ибо он тут скоро понадобится, если вообще будет."