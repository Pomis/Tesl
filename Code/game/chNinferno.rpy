label chNinferno:
    # bulka: Они переместились в какой-то условный город Инферно, который не является столицей. Ибо контроль за перемещением в столицу с поверхности жёстче чем где бы то ни было. Однако, контроль в случае перемещений между городами гораздо меньше. Однако (ахуеть их много, этих однако), люди слишком палевные. А потому для убийства в столицу они проникнут через другой город маскируясь под инферно. Ну или гг проникнет. В этом городе как раз эта сцена и происходит. Эта сцена будет включать описание плана и тд. Разработка плана тут будет излишней пожалуй. Действие происходит после ch3day3 или во время. Посмотрим по размерам и тд.
    # pomis: я так понимаю, no1 более уравновешанный персонаж. Всё таки, давай хотя бы одного из них заменим уже существующим. Или одного из них сделаем девушкой вообще. А то получается уже 6 инферно-мужиков, дело даже не в спрайтах, а в том, что каждый из этих персонажей играет не особо значимую роль в сюжете. Они получатся довольно серыми. Чем делать такую толпу, лучше выделить конкретных персонажей и развивать их. No1 в целом похож на Алилума, а no2 можно сделать бабой-жуткой патриоткой. Что-то вроде легионки, только не негр. В общем-то, персонажи твои, делай что хочешь, я лишь за то, чтобы не размножать серость.
    # bulka: no1 да. no2 потерял семью в уничтоженном городе, а потому такой бешенный и неадекватный. Я это в предыдущих апейдтах случаем не писал? Или только в диалоге? Ибо вроде описывал, а тут этого нет. Ну 6 инферно-мужиков и 3 инферно-бабы. Ничего особого. Просто характер no2 больше подходит мужчине, нежели женщине. Их прорисовывать, имхо, не надо. Просто такие мимолётные персонажи. По поводу серости — это такое, не размножая её, мы сталкиваемся с другой проблемой: вот щас конкретно, у меня возникло впечатление, что этих инферно не десятки/сотни милионнов, а штук 10, не более. Если посчитать их всех, то примерно так и выйдет. С другой стороны, в случае с людьми такого впечатления нет, ибо не только важный для сюжета персонажей достаточно, но и немало всяких левых. Аля продавщица, доктор, сосед по палате.
    # pomis: пнятненько. Имена у них хоть будут?
    # bulka: Интересный вопрос. А нужны?
    no1 "— Одной проверки при входе недостаточно.{w} Конечно, у тебя схожие с нами идеалы, однако это не значит, что мы можем тебе доверять."
    no2 "— Павел уже доказал свою преданность нашему делу. Теперь твоя очередь."
    "— Что я должен сделать?"
    # bulka: Мб, тут забабахать выбор вариантов вопроса
    no1 "— Ты должен кое-кого убить."
    "Убить? Конечно, я уже убивал, однако, это было в порыве гнева. Не уверен, что смогу хладнокровно убить кого-то."
    "Первый положил передо мной что-то вроде планшета с изображением красивой девушки с длинными чёрными волосами в каком-то средневековом платье."
    no1 "— Это твоя цель."
    "Что-то с ней не так. Конечно, странно, что им нужна смерть обычной девушки, однако что-то ещё не давало мне покоя."
    "— Стойте! Она же...{w} Она же из Инферно!"
    "Вот что было не так. Вот что не давало мне покоя. Зачем им убивать своих?"
    no1 "— С этим какие-то проблемы?"
    "— Не совсем. То есть зачем вам убивать своих?"
    no2 "— Она не своя! Она предала всё, к чему мы стремимся, и продолжает втаптывать в грязь наши цели, называя это ненужной бойней!"
    "Этот парень явно нешуточно зол на неё."
    no1 "— Эта девушка — глава фракции, выступающей за мир. За то, чтобы простить землянам их грехи и начать мирное сосуществование, а то и сотрудничество."
    no1 "— Ты, потерявший по чужой вине близких тебе людей, как никто должен понимать наш гнев."
    menu:
        "— Да, такое прощать нельзя.":
            "Я с гневом стукнул по столу."
            "— Это сродни предательству!"
            "Один из них одобрительно кивнул, соглашаясь с моими словами."
            no2 "— Потому она должна умереть!"
        "— Нельзя застилать свои глаза гневом":
            "Один из них схватился за пистолет и направил его на меня."
            no2 "— Ты что, решил стать на сторону этой сучки?!"
            "Ох, плохо дело. Надо быть аккуратнее со словами."
            "— Н-нет, это я к тому, что к делу нужно подходить с холодной головой. Иначе, всё может наперекосяк."
            no2 "— Ах, вот ты о чём. Ну тогда пардон. Я неправильно тебя понял."
            "Фух, пронесло/выкрутился. В следующий раз буду знать, что говорить, а что нет."
        "— А обязательно ли её убивать?":
            $knowEshaliaName = True
            no2 "— Принцесса Эсхалия — глава фракции мира и её движущая сила. Все остальные из её фракции там скорее не из-за стремления к миру, а из-за самой принцессы. Она слишком харизматична и умело это использует для привлечения сторонников. Если бы она просто тихо сидела, то мы бы её не трогали."
            # bulka: Предпоследнее предложение не совсем подходит персонажу, но без него тоже нельзя. Надо как-то адаптировать. Аля умелый лидер и тд.
            no1 "— Однако, она слишком активна в последнее время. Мы не хотим рисковать и оставлять возможность мирного урегулирования. А потому тебе нужно от неё избавиться."
            # TODO: Слишком много "однако", однако.
    # bulka: Оба варианта не являются решением по убийству принцессы. Это скорее пойнты. Думаю, в случае убийства, оставить вероятность использования главного героя для убийства принцессы, что мол это люди сделали, что они не хотят мира и тд. То есть в качестве пропаганды. Хотя это не совсем вяжется с преданностью инферно. Не помню, была ли эта преданность ещё где-то, кроме рассуждений Павла об Инферно, на которые можно забить болт как на слишком идеалистические.
    # bulka: Придумал. Когда он будет спрашивать почему именно я — они ему ответят, что если человек сфейлится, то ничего страшного, цель всё равно будет частично достигнута. Однако, если спалят на этом инферно, то кирдык. Этот вопрос будет тут же наверное. Надо, чтобы тут второй круг был и можно было задать два вопроса.
    # bulka: Это не концовка, это происходит после проникновения в город инферно, где они попадают штаб фракции войны, ну или отделение так сказать. 