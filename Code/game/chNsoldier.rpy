label chNsoldier:
    "Со мной в помещении остался один представитель Инферно. Его черты лица выглядели настолько искажёнными, а кожа была настолько иссушена, что он был скорее похож на паутину, чем на живой организм."
    "Тем не менее, это существо весьма бодро двинулось навстречу мне. Я схватил свой пистолет ещё крепче, но что-то мне подсказывало, что это существо гораздо опаснее всего, с чем мы сталкивались до этого."
    sa "— Добро пожаловать в Сенат Инферно! Правда, все остальные сенаторы в ужасе сбежали. Жалкие трусы. Кстати, я Саргон. Верховный сенатор."
    "— Чего сам не сбежал? У нас армия. А у тебя полупустой город, разбежавшийся в панике."
    sa "— Хотелось пообщаться с вами в такой обстановке. До этого разговаривал только с перебежчиками и подопытными людьми."
    "— Рискованно."
    sa "— Ничуть. Может, у тебя будут вопросы поинтереснее?"
    "— Как вы вообще появились на Земле?"
    sa "— Пришлось заселиться. Спасались от гибели."
    sa "— Телепортировали столицу, остальные города уже построили будучи на вашей планете."
    "— У вас такой мощный телепорт?"
    sa "— Задействовали всю имевшуюся энергию."
    # bulka: Тут что-то должно быть. Слишком резкая смена темы.
    # pomis: А так?
    "Впечатляющие технологии, всё таки."
    sa "— Тебе, правда, это интересно? Ты довольно любопытный."
    sa "— Тогда позволь мне тоже полюбопытствовать: зачем же ты воюешь? Что тобой движет?"
    "— Месть. Вы убили мою семью! В июне 2049 года! На лайнере..."
    sa "— Однако ты сомневаешься. Ты же не набросился на меня сразу, как увидел. Тебе интересно узнать всю правду, да?"
    sa "— А, кажется, вспомнил тот случай. Как думаешь, какой самый верный способ настроить кого-то против другого?"
    # bulka: А вот тут меня посетила идея, что всё это спланировано. Что кто-то уже знал, что гг способный и всё это подстроил.
    "Риторический вопрос?"
    sa "— Сделать так, чтобы кто-то винил другого в смерти близких."
    sa "— Вы убили два миллиона наших жителей, разрушив город бомбой. Тогда мы поклялись убить два миллиона ваших жителей в их же городах."
    "— К чему ты клонишь?"
    sa "— Нас спровоцировали напасть на лайнер."
    "— Звучит глупо. Как оправдание."
    sa "— Знаешь, мне нравятся люди. Ваши изобретения, мысли, поступки... Однако, есть в вас и то, что меня раздражает. Крайне дурaцкaя людскaя мaнeрa — пытaться втиснуть вeсь многообрaзный мир в узкиe рaмки своeго понимaния."
    "Я навёл пистолет на Саргона. Сомнения всё ещё терзали меня. Если всё, что он говорит, правда, то я совершаю огромную ошибку. Но мы зашли так далеко... Стольких потеряли..."
    # по рации:
    gen "— Ну же, чего ты медлишь? Открывай огонь!"
    if agressionPoints>4 and doubtPoints<=3:
        "— УМРИ, УРОД!"
        "Я нажал на курок, но ничего не произошло."
        sa "— Не получается? А ничего, что это я изобрёл нейронты? Я их создал на основе своего тела. У меня идеальная совместимость с этой технологией."
        "— Создателя медного быка казнили с помощью его же изобретения. Наивно полагаешь, что не повторишь его судьбу?"
        sa "— Какие громкие слова, но какова же их цена? У таких ничтожеств, как ты, я могу перехватить управление нейронтами даже на расстоянии в несколько метров."
    else:
        sa "— Слушай своего главного!{w} Да, я могу перехватить твоё переговорное устройство. Могу взять под контроль все нейронты, которые ты используешь."
        "— Какого чёрта!"
        sa "— Я создал эту технологию на основе своего тела. У лучших из вас совместимость с нейронтами не более 50\%. У тебя, судя по всему, около 15\%."
        # bulka: Имхо, слишком маловато.
        # pomis: ok
        sa "— У таких, как ты, я могу перехватить управление нейронтами даже на расстоянии в несколько метров. А возможно, даже подчиню нервную систему."
    sa "— Ты даже не сопротивляешься! Я так возьму под контроль и тебя самого!"
    "Он правда на это способен? Блеф?"
    sa "— Хотя, ты довольно интересный человек."
    sa "— В курсе, что моя технология губительна для людей? Вы разрушаете свою нервную систему. Ты проживёшь ещё года два, не больше. Кто-то вообще больше недели не выдерживает."
    "По моему телу пробежала холодная дрожь."
    "— Есть люди, которые в строю уже несколько лет."
    # кадры, где Ганц жрёт колёса
    gen "— Выбрось пистолет немедленно! И рацию! И атакуй его ножом!"
    if doubtPoints>3:
        jump ending1
    else:
        jump ending2

label ending1:
        "Как скажешь..."
        "Я швырнул пистолет и рацию подальше."
        "— Расскажи мне всё. Почему потонул лайнер. Почему вы воюете с людьми."
        sa "— Кто-то установил на ваш лайнер маячок, который воспроизводил ту же комбинацию электромагнитных частот, как и те, кто нас истреблял дома."
        sa "— Я не знаю, откуда у вас это, возможно вы вышли с ними на связь."
        sa "— Мы уничтожили корабль как крайне опасную для нас цель. Однако, обыскав его, не нашли ничего особенного. Не нашли источник сигнала."
        # а источник гг расфигачил об лодку. 
        "—  То есть, мы были приманкой для вас?"
        sa "— Да."
        "— Но зачем? Если кому-то выгодно настроить население против вас, то почему ваше существование строжайшая тайна?"
        sa "— Мы исследовали этот вопрос. Пришли к выводу, что способность управлять нейронтами у людей чаще всего пробуждается при непосредственной близости с нашими боевыми телами."
        # bulka: Во-первых, он слишком болтлив. А во-вторых, меня что-то смущает в способе пробуждения этих сил.
        sa "— Для их питания мы отправляем огромное количество энергии из городов, эта энергия также пронизывает ваши тела, и если есть предрасположенность к управлению нейронтами, то, с большой вероятностью, эта способность проявится."
        "— Что-то вроде излучения?"
        sa "— Да. Чем дольше ты под этим излучением, тем больше вероятность пробуждения способности. А совместимость зависит уже от организма."
        # bulka: Может это будет аля излучение — чем дольше под ним, тем выше совместимость и тем выше риск "перегореть" (сдохнуть).
        # pomis: Как-то так
        sa "— Думаю, на том корабле многие выжившие вошли в ряды вашей армии."
        "— Я бы поверил тебе, если бы последний факт был документально подтверждён."
        sa "— Хм... У нас есть досье на почти всех ваших. Почти на каждой базе есть по шпиону. Хочешь ознакомиться?"
        "— Вы его на русском составляли?"
        sa "— Нет, конечно, могу зачитать."
        "Пожалуй, тут он сможет меня одурачить?"
        sa "... База №4. Евросоюз. \n1. Дональд Круш [погиб в тренировочном бою], \n2. Джон Айлс [жив]..."
        "Одни буржуи."
        sa "...{w}\n23. Тоня [playerFamilyName]a. [погибла из-за слабой совместимости]."
        "— ТВОЮ МАТЬ, ЧТО?"
        # sa "— А? Знаешь её? Ох, лол. Это твоя сестра. Копать ты лох."
        # bulka: Не удержался.
        # pomis: xD
        sa "— А? Знаешь её? Ах, да. У тебя же есть сестра.{w} Точнее была."
        # bulka: Щас бы иметь досье на двух человек и не знать, что они родные брат и сестра... Алилум там Санта-барбару смотрит?
        # pomis: Кек, не знаю, что тут сделать.
        # шутка про харакири
        sl "— Вот ты где!"
        "Слава навёл на меня пистолет."
        sl "— Генерал приказал убить тебя."
        "— Слава, подожди..."
        if slavaPoints>5:
            sl "— Да я жду! Так что происходит? Я верю тебе, не может быть, что ты предал нас!"
            "— Что тебе сказал этот генерал?"
            sl "— Что ты примкнул к Инферно. И приказал стрелять на поражение."
        else:
            sl "— Предатель."
            "Слава нажал на курок, но ничего не произошло."
            sa "— Ничего, что я тут? Ты не сможешь выстрелить, если я этого не захочу."
            sl "— Что за чертовщина?! Плевать. Приказ есть приказ."
            sa "— А твоя совместимость ещё ниже. Как и интеллект. Просто умри."
            "Слава вытащил нож и сделал рывок в мою сторону."
            "Я отпрыгнул в сторону Саргона."
            "Слава остановился как вкопанный. Дрожащей рукой он медленно приближал нож к своей шее."
            sl "— Что происходит? Я не управляю собой!"
            menu: 
                "— Брось пистолет и рацию, немедленно!":
                    sa "— Уже поздно."
                "— Ты даже не захотел меня выслушать. Прощай.":
                    ""
                    # bulka: Имхо, слишком дикая фраза для рута солдата. Хотя хз.
                    # pomis: Игрок же сам выберет эту фразу. Хотя хз[2].

label ending2:
    ""