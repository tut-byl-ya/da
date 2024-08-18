# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Чай', color="#FF8C00")
define a = Character('???', color="#FFFFE0")
define n = Character('Никита', color="#4B0082")
define c = Character('Арменчик', color="#8B0000")
define g = Character('Дядя Адя',color="#000000")
define m = Character('Мысли Чая',color="#FFFFFF")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
scene bg empty

play music "myzika dla chaa.mp3"

#voice "voice/1587065282.ogg" #Можно использовать и мп3 файлы -озвучка:( 
a "15 августа 2023 год..."

scene bg room
with fade

show chai normal at center:
    zoom 1.5

e "Ух...Наконец-то я пришел с качалочки!"

e "Самое время сесть за код!"

hide chai normal

a "Чай зашел в комнату и увидел, что кто-то сидит за его ПК..."

show saster happy at center:
    zoom 1.5

n "ух блять какой сочный код, надо бы его спиздить"

e "Это чё, Никита?!"

e "Хули он тут забыл???????"

hide saster normal

a "Никита продолжал пиздить код не замечая, как за его спиной оказался чай..."

a "И тут перед Чаем появился выбор.."

menu:

    "Трахнуть":
        jump trax

    "Заставить качать немцев в тундре":
        jump nemci

label trax:

    e "Че, сука, попался?"

    n "НЕЕЕЕЕЕЕТТТ!!!"

    a "А дальше у них было много секса.. Но мы вам этого не покажем"
    
    jump trax2

label nemci:
    e "Че, сука, попался?"

    n "Чай, не надо!.. Только не насилуй! Я случайно украл твой код..."

    e "Ой не... В этот раз я насиловать тебя не буду"

    e "Я заставлю тебя качать танки немцев на моем аккаунте до Leopard 2A6"

    e "*Злой смех*"

    n "НЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕТ!!!"

    a "Спустя 2 часа..."

    jump marry

label trax2:

    a "Спустя пол часа..."

    show chai normal at left:
        zoom 1.5

    show saster happy at right:
        zoom 1.5

    n "ах, Чай.. прости, я больше никогда так не буду делать.."

    e "Не бойся, я уже придумал твое следующее наказание >:)"

    n "пора тiкать..."

    hide chai normal
    hide saster happy

label marry:

e "Ну наконец-то я от него избавился!.."

e "Надо теперь сесть за код и посмотреть, что за хуйню Никита там натворил..."

a "Чай садиться за компьютер, надевает наушники, и тут..."

stop music

play music "nemci.mp3"

scene bg parad
with fade 

a "На весь экран вылазит Свастика и начинают маршировать немцы под какую то перепевку на 'Руки Вверх'"

e "Это что за хуйня блять??"

e "Хотя звучит прикольно, но мне кажется оно меня скоро заебёт..."

a "Прошло 30 минут, а чай так и не смог убрать эту дичь"

e "Scheiße!"

a "Чай от злости ебнул по компу и все починилось"

stop music
scene bg rab stol2
with fade

a "И вот на экране появился уже привычный чаю рабочий стол."

play music "magic.mp3"

e "Чайная магия ебать!"

e "Ну охуеть можно..."
stop music

play music "war thunder.mp3"

a "И тут чай краем глаза замечает иконку вар тандера.."

scene bg war thunder
with fade

e "Пора оформлять пробития!"

e "Вкинулся чаем и погнал!"

scene bg polsha 
with fade

e "Эти поляки просто малыши!"

scene bg umer
with fade

e "Блять..."

scene bg room
with fade

stop music

play music "myzika dla chaa.mp3"

show chai normal at center:
    zoom 1.5

e "Заебал меня этот вар тандер."

a "Тут вдруг у Чая раздался звонок.."

e "О, ебать! Арменчик звонит, в качалочку зовёт походу!"

a "Чай отвечает на звонок"

c "Ало это Пригожин Женя"

e "Это Пригожин Женя"

c "Оооо бляя а мы и не думали"

e "Аче StwBot3 то не берете?"

c "А мы в Качалке ебашимся"

e "Оооо бляя а мы и не думали"

e "Ладно, выезжаю!"

hide chai normal

scene bg les naxui
with fade

show chai normal at center:
    zoom 1.5

e "Ебать, свет..."

e "Ненавижу свет..."

e "Кхм. Такс.. тут есть две тропинки одна ведет в качалку, другая..?"
label les:

menu:

    "Пойти в Качалку":
        jump kachalka

    "???":
        jump nemci2

label les2:

menu:

    "Пойти в Качалку":
        jump kachalka


label nemci2:
    e "И куда же она ведет??"

    hide chai normal

    a "Чай все дальше продолжал углубляться в лес..."

    scene bg parad
    with fade
    play music "erika.mp3"

    show chai normal at center:
        zoom 1.5

    e "Что блять?? Как я здесь оказался?"

    a "Чай вспоминает, что примерно точно такая же картина происходила на его ПК после Никиты."

    e "Вот никита, вот пидарас..."

    e "Погодите, это кто там такой?"

    a "И тут на сцену поднимается мужчина."

    show chai normal at left:
        zoom 1.5

    show gitler normal at right:

    g "Мы приведем великую Германию к процветанию!"

    e "Чё за хуйня??"

    a "И тут взор художника падает на странного мужчину в желтом костюме."

    g "Вы кто?"

    a "Обращается художник к Чаю"
label vibor:
    show chai normal at left:
        zoom 1.5
    show gitler normal at right:
menu:

    "Это вы кто блять и как я вообще здесь оказался?":
        jump rasstrel

    "Слава Фюреру!":
        jump nemci3

label rasstrel:
    e "Это вы кто блять и как я вообще здесь оказался?"

    g "Убить врага Рейха!"

    a "И тут все синхронно поднимаются со своих мест и идут в сторону чая!"

    m "Никита, я тебя убью..."

    $renpy.notify("Вас расстреляли.")

    scene bg parad
    with fade
    jump vibor

label nemci3:
    e "Слава Фюреру!"

    g "Gute Arbeit, Oleg"

    a "Дядя Адя продолжил дальше толкать свою речь."

    m "Кажется, он ничего не заподозрил."

    m "Надо валить отсюдова пока при памяти..."

    a "Чай в спешке покидает это странное место."
    scene bg les naxui
    with fade
    hide gitler normal 
    stop music
    hide chai normal
    show chai normal at center:
        zoom 1.5
    stop music
    a "Чай выбрался из этого странного места и очутился в том же месте в лесу."

    e "Фухх.. Блять, что это вообще было??"

    e "Ладно, хуй с ним. Надо идти в качалку к Армену"

    jump les2

label kachalka:

    e "Ладно лучше в качалку пойду, а то Арменчик меня уже заждался поди."

    hide chai normal 

    a "Чай направился в качалку."
    
    scene bg kachalkaa
    with fade
    play music "kachalka.mp3"
    show chai normal at center:
        zoom 1.5
    e "Ну вот я и в Качалочке, где Ара?"

    show armen at right:
        zoom 1.2
    show chai normal at left:
        zoom 1.5

    c "Дарова пиздюк! Я тебя минут 20 здесь ждал"

    e "Ебать, Ара, ты не представляешь что я был и где я там видел..."

    c "Да ты всегда в какую-то пизду попадаешь."

    e "Кароче.."

    play music "peregovori.mp3"

    a "И Чай начинает рассказывать Армену про то, как он гулял в лесу"

    a "И про то, как он встретил какую то очень странную тропинку"

    a "Арменчик слушал и делал вид что ему не похуй"

    a "И вот, спустя 5 минут увлекательного рассказа Чай закончил и они начали качаться"

    a "И вот во время качалки чай вспоминает что хотел рассказать Аре о своем новом титуле"

    e "Ара кстати а ты знаешь кем я стал?)"

    c "И кем же?"

    e "Я стал Femboy king"

    c "King???!"
    scene bg king
    with fade
    play music "king.mp3"
    
    c "You Are King!"

    e "You Are King!"
    hide chai normal
    hide armen 

    m "И тут вдруг чай просыпается.."

    scene bg kachalkaa
    with fade
    stop music
    play music "kachalka.mp3"
    show chai normal at left:
        zoom 1.5
    show armen at right:
        zoom 1.2

    m "Какого черта это сейчас было?"

    hide chai normal
    hide armen

    a "Прошел 1 час..."

    a "И вот чай закончил заниматься с Арой и самое время пойти домой."

    show chai normal at left:
        zoom 1.5

    e "Уф... Хорошо сегодня позанимались."


    e "Этот тренажер просто имба!"

    hide chai normal
    show armen at right:

    c "Я сидел в качалке и занимался до 6 утра!!"

    hide armen
    show chai normal at left:
        zoom 1.5

    e "Эти курильщики просто малыши!"

    show armen at right:

    c "Ладно, Чай, давай я уже пойду домой"

    e "Я тоже тогда."

    a "И вот, Чай, попрощавшись с Арой, выходит из качалки, и тут..."

    scene bg wagner 
    with fade
    play music "vagner.mp3"

    e "Так стоп.. Где это я?"

    show chai normal at left: 
        zoom 1.5 
    

    e "че за хуйня?"

    show chai normal at center:
        zoom 1.5

    a "Чай огляделся и понял что он находится на границе Литвы и Беларуси"

    show chai normal at right:
        zoom 1.5

    e "Так, а че я здесь забыл блять? Где качалка, где лес?"

    a "Вдруг перед чаем появилась какая-то неизвестная дверь."

    e "Блять, я видел порно которое начиналось точно также..."

    a "Но в итоге пересилив себя он заходит в эту дверь."

    a "Появляется ослепительная вспышка и он оказывается..."

    scene bg room
    with fade
    stop music 
    play music "myzika dla chaa.mp3"

    a "В своей комнате?.."

    e "Так блять... Какого черта здесь происходит?"

    a "И тут чай замечает в своей комнате никиту сидящего за его компьютером"

    hide chai normal

    show saster happy at center:
        zoom 1.5

    n "ух блять какой сочный код, надо бы его спиздить"

    m "Вот Никита сука.."

    m "Так стоп. Это же уже было со мной утром"

    m "Я че блять? Во временной петле оказался?"

label ending:
    stop music
    scene black_screen  # Отображение черного экрана с изображением
    image black_screen = "images/end.png"
    with Dissolve(1.0)  # Плавный переход к черному экрану
    $ renpy.pause(10.0)