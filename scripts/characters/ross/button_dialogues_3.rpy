label button_ross_ask_model:
    scene location_school_art_closeup
    show ross 25 at left
    show player 1f at right
    ross "Alguma sorte?"
    show player 2f
    show ross 24
    player_name "Ainda não."
    show player 1f
    show ross 25
    ross "Bem, certifique-se de {b}pergunte a todos os seus colegas de classe{/b}."
    show ross 25b
    ross "Felizmente, alguém será corajoso o suficiente para modelar para nós ... "
    return

label button_ross_found_model:
    scene location_school_art_closeup
    show player 2f zorder 1 at right
    show judith 1 zorder 2 at Position(xpos=0.65, ypos=1.0)
    show ross 10 zorder 2 at left
    with dissolve
    player_name "estou de volta {b}Miss Ross{/b} e eu achei um modelo pra gente! "
    show player 1f
    show ross 11
    ross "{b}*Suspiro* Judith{/b}!"
    show ross 27 with dissolve
    ross "Isto é perfeito! Ela tem um corpo maravilhoso para isso! "

    show ross 26
    show judith 4
    pause
    show judith 5
    jud "Oh umm, {b}Miss Ross{/b} vai estar aqui também hein? "
    show player 10f
    show judith 1
    player_name "Sim, está tudo bem. "
    show player 11f
    show judith 3
    jud "Não sei..."
    show judith 6
    show ross 27
    ross "Oh, olhe para ela ficando vermelha, que delicia! "
    show ross 60 with dissolve
    ross "Aqui, querida, pegue isso e vá trocar de roupa. "

    ross "Vamos esperar aqui por você. "
    show ross 59
    show judith 3
    jud "Umm..."
    show ross 60
    show judith 6
    ross "Não demore, queremos o máximo de tempo possível com você. "

    hide judith
    show ross 11
    with dissolve
    ross "Bom trabalho, {b}[firstname]{/b}! Ela vai ser uma excelente modelo! "
    show ross 10
    show player 1f
    pause
    show mia 8b zorder 0 at Position(xpos=0.65, ypos=1.0) with dissolve
    pause
    show ross 11

    ross "... E aqui está nossa pequena torta fofa, bem a tempo! "
    show ross 10
    show mia 12b
    mia "Sim, eu não consegui encontrar ninguém. Desculpe pessoal ... "
    show ross 11
    show mia 8b
    ross "Oh, não se preocupe! {b}[firstname]{/b} resolveu como ele sempre faz. "
    show ross 10
    show mia 10b
    mia "Realmente? Você realmente tem alguém para ser voluntário? "
    show mia 9
    mia "Isso é incrível, {b}[firstname]{/b}!"
    show mia 11
    show player 2f
    player_name "... Sim, {b}Judith{/b} concordou em-"
    show judith 59f zorder 0 at Position(xpos=0.35, ypos=1.0)
    show player 11f
    with dissolve
    pause
    show judith 44f
    show judithr 1f zorder 1 at Position(xpos=0.35, ypos=1.0)
    with dissolve
    show mia 7
    pause
    show judith 45f
    jud "... O que é {b}Mia{/b} fazendo aqui?!"
    show judith 44f
    show ross 11
    ross "Ela vai desenhar você também, querida. "
    show judith 45f
    show ross 10
    jud "Estou pensando melhor sobre tudo isso ... "
    show judith 52f
    jud "Eu pensei que seria apenas você e eu, {b}[firstname]{/b}!"
    show judith 51f
    show ross 25
    ross "Acalme-se, {b}Judith{/b}... Tudo vai ficar bem, querida. "
    show ross 11
    ross "Você não tem nada para se envergonhar dela. "
    show ross 10
    show player 2f
    player_name "De modo nenhum."
    show player 1f
    show mia 10
    mia "Sim, não se preocupe, {b}Judith{/b}. {b}Miss Ross{/b} tem nos ensinado que o corpo de todos é bonito."
    show mia 7
    show ross 11
    ross "Está certo, {b}Mia{/b}. Eles são todos bonitos de uma maneira única. "
    ross "Você deve se orgulhar do seu corpo, {b}Judith{/b}."
    show ross 10
    show judith 52f
    jud "Não sei..."
    show judith 51f
    show ross 58 with dissolve
    ross "Eu tive uma ideia!"
    hide ross with dissolve
    pause
    show ross 40 zorder 2 at left with dissolve

    ross "Eles sempre me acalmam quando estou me sentindo ansioso ... "
    ross "Todo mundo pega um. "
    show ross 41
    show player 2f
    player_name "Oh, eu ouvi você fazer os melhores brownies! "
    show player 1f
    show ross 40
    ross "Hehe, é melhor você acreditar! "
    ross "É a minha receita secreta ... "
    show ross 44 with dissolve
    pause
    show ross 43 with dissolve
    ross "... Cem por cento, tudo natural. "
    hide player
    show player 602 zorder 4 at right
    with dissolve
    show ross 42
    pause
    show player 599f with dissolve
    pause
    show player 600f
    show mia 73 zorder 3 at Position(xpos=0.55, ypos=1.0)
    with dissolve
    pause
    hide judith
    hide judithr
    show mia 71
    show judith 60 zorder 5 at Position(xpos=0.60, ypos=1.0)
    with dissolve
    pause
    hide judith
    show mia 71 at Position(xpos=0.65, ypos=1.0)
    show judith 47f zorder 0 at Position(xpos=0.35, ypos=1.0)
    show judithr 1f zorder 1 at Position(xpos=0.35, ypos=1.0)
    with dissolve
    pause
    show mia 72

    mia "Yum !! Estes são deliciosos! "
    show mia 71
    show judith 48f
    jud "Nom Nom Nom."
    show ross 43
    show judith 47f
    ross "Vá devagar, {b}Judith{/b}. Você não quer comer isso muito rápido. "
    show ross 42
    show judith 48f
    jud "Oh meu Deus! Eles são tão bons! "
    show judith 49f
    jud "Mmm..."
    show mia 74f
    show player 26f
    player_name "Heh, eles tinham um tipo ... sabor de terra. "
    show player 13f
    show ross 13
    ross "Como estão todos? "
    show ross 12
    show player 26f
    player_name "Bem realmente bem"
    show player 13f
    show judith 50f
    jud "Eu também."
    show judith 49f
    show mia 75bf at Position(xpos=0.63, ypos=1.0) with dissolve
    mia "Heheheheheheheehee!"
    show judith 50f
    show mia 74f at Position(xpos=0.65, ypos=1.0) with dissolve
    jud "Este roupão é super fofo!"
    show judith 49f
    show ross 13
    ross "Bem, agora que você está se sentindo mais relaxada, por que não tira, querida? "
    ross "Podemos colocar esse show na estrada. "
    show ross 12
    show judith 50f
    jud "Mmm, sim, ok..."
    hide judith
    hide judithr
    show judith 56f zorder 0 at Position(xpos=0.35, ypos=1.0)
    with dissolve
    pause
    show judith 49f with dissolve
    pause
    show ross 13
    ross "Muito bom querida."
    show ross 11
    ross "Agora, então, {b}[firstname]{/b} e {b}Mia{/b}, por que vocês dois não se sentam e encontram seu carvão? "
    show ross 10
    show mia 75bf at Position(xpos=0.63, ypos=1.0) with dissolve
    mia "Heheheheeahahaaha!"
    mia "Tudo é tão twirly !! "
    show mia 74f at Position(xpos=0.65, ypos=1.0) with dissolve
    show ross 11
    ross "Sim, com certeza, torta fofa. "
    show ross 13
    ross "{b}Judith{/b} você precisa tirar sua calcinha também, querida. "
    show ross 12
    show judith 51f
    jud "Hmm?"
    show judith 52f
    jud "Você quer dizer que eu tenho que mostrar minha ... "
    jud "Minha..."
    jud "... Buceta?"
    show judith 51f
    show mia 75bf at Position(xpos=0.63, ypos=1.0) with dissolve
    mia "Pffftt!!! AHahahaah! Essa é uma palavra tão engraçada! "
    mia "buuuceeeetaaaa! HahahaaH!"
    show mia 74f at Position(xpos=0.65, ypos=1.0) with dissolve
    show ross 11
    ross "Heh, acalme-se, {b}Mia{/b}!"
    show ross 25
    ross "Você ainda está se sentindo consciente, {b}Judith{/b}?"
    show ross 24
    jud "Mmmhmm..."
    show ross 11
    ross "Bem, e se o resto de nós também nos despisse? "
    show ross 10
    show judith 54f
    pause
    show judith 55f
    jud "... sim! Essa é uma boa ideia!"
    show judith 54f
    show player 26f
    player_name "Você quer que fiquemos nus também? "
    show player 13f
    show ross 11
    ross "Vamos tirar a roupa de baixo. "
    ross "Isso deve ser bom o suficiente, certo {b}Judith{/b}?"
    show ross 10
    show judith 55f
    jud "... sim! Eu quero ver as roupas íntimas de {b}[firstname]'s{/b}"
    show judith 54f
    show ross 11
    ross "Muito bom então..."
    hide ross
    show ross 14 at Position(xpos=0.15, ypos=1.0)
    with dissolve
    pause
    show ross 15 at Position(xpos=0.14, ypos=1.0) with dissolve
    pause
    show ross 16 at Position(xpos=0.13, ypos=1.0) with dissolve
    pause
    show ross 17 with dissolve
    pause
    show ross 36 at Position(xpos=0.15, ypos=1.0) with dissolve
    ross "Vá em frente vocês dois ... "
    show ross 37
    show mia 75f with dissolve
    mia "... Espera! Eu?"
    show mia 74f
    show ross 36
    ross "Especialmente você, fofa torta! "
    show ross 37
    show mia 75bf at Position(xpos=0.63, ypos=1.0) with dissolve
    mia "Heheheheheeeh, tudo bem"
    show mia 76f at Position(xpos=0.62, ypos=1.0) with dissolve
    pause
    show mia 77f at Position(xpos=0.64, ypos=1.0) with dissolve
    pause
    show mia 78f at Position(xpos=0.66, ypos=1.0) with dissolve
    pause
    show mia 79f at Position(xpos=0.66, ypos=1.0) with dissolve
    pause
    show mia 80f at Position(xpos=0.66, ypos=1.0) with dissolve
    pause
    show mia 81f at Position(xpos=0.65, ypos=1.0) with dissolve
    show ross 36
    ross "Você não teve que tirar o sutiã torta fofa"
    show mia 82f
    show ross 37
    mia "Eu não? "
    show mia 81f
    show ross 36
    ross "Hehe, não, eu disse, 'até nossas roupas íntimas'. "
    show mia 82f
    show ross 37
    mia "Ooooh..."
    mia "Tudo bem então!"
    show mia 82bf at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "Isto é divertido!"
    show mia 81f at Position(xpos=0.65, ypos=1.0) with dissolve
    show ross 36
    ross "Sim, certamente é, querida. "
    ross "Nós estamos esperando, {b}[firstname]{/b}."
    show ross 37
    show player 21f
    player_name "Sim. Ok!"
    show player 8f with dissolve
    pause
    show player 265f with dissolve
    pause
    show judith 53f
    pause
    show player 267f
    player_name "( !!! )" with hpunch
    jud "... Wow!"
    show mia 82bf at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "Parece meio zangado! Pffft, hahahahaa!!!"
    show mia 81f at Position(xpos=0.65, ypos=1.0) with dissolve
    show judith 55f
    jud "É tão grande..."
    show judith 54f
    show player 265bf
    show ross 36
    ross "Com certeza é, querida. "
    ross "... Você ainda tem que tirar a calcinha antes que possamos desenhá-la. "
    show ross 37
    show judith 55f
    jud "... E rosa. "
    show judith 54f
    show ross 36
    ross "Aqui, eu ajudo! "
    hide ross
    show judith 61f at Position(xpos=0.22, ypos=1.0) with dissolve
    pause 
    show judith 62f with dissolve
    pause
    hide judith
    show judith 66f zorder 1 at Position(xpos=0.35, ypos=1.0)
    show ross 36 zorder 0 at left
    with dissolve
    ross "Há uma boa garota. "
    ross "Agora, fique lá no pedestal para mim, ok? "
    show ross 37
    show judith 66f
    jud "..."
    show ross 36
    hide judith with dissolve

    ross "Vocês dois começam a desenhar. "
    show ross 37
    show player 265cf
    player_name "Sim, senhora."


    scene location_school_art_cutscene08
    with fade
    show text "eu poderia dizer {b}Judith{/b}  ainda estava muito nervosa como {b}Miss Ross{/b} ajudou-a a subir no pedestal." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Foi muito corajoso da parte dela modelar para uma audiência." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... Mas ela não estava exatamente fazendo uma pose inspiradora lá em cima." at Position (xpos=512, ypos=700) with dissolve
    pause
    hide text
    with dissolve

    scene location_school_art_closeup
    show judith 65b zorder 1 at Position(xpos=0.5, ypos=1.0)
    show ross 37 zorder 0 at left
    with dissolve
    pause
    show ross 36
    ross "Querida? Você tem que relaxar um pouco ... "
    show ross 37
    show judith 66
    jud "Eu não..."
    jud "Digo, eu..."
    hide ross
    show ross 36f zorder 0 at Position(xpos=0.7, ypos=1.0)
    with dissolve
    show judith 65b
    ross "Shhh."
    ross "Está tudo bem, {b}Judith{/b}."
    hide ross
    show judithross 2 zorder 0 at Position(xpos=0.685, ypos=1.0)
    with dissolve
    ross "Apenas respire profundamente ... "
    show judith 66
    pause
    show judith 65b
    ross "... É isso aí."
    show judithross 1
    pause
    show judithross 2
    ross "Você é um anjo lindo, {b}Judith{/b}."
    show judithross 1
    show judith 66
    jud "... Eu sou?"
    show judithross 2
    show judith 65b
    ross "Ai sim! Você é de tirar o fôlego, querida! "
    show judithross 1
    pause
    hide judithross
    show judith 67 at Position(xpos=0.4, ypos=1.0)
    with dissolve
    ross "Spread your wings, {b}Judith{/b}."
    ross "Let the world see you fly!"
    show judith 68b
    show ross 36f at Position(xpos=0.65, ypos=1.0)
    with dissolve
    ross "{b}*Gasp*{/b} Perfection!"
    show judith 69
    show ross 37f
    jud "... You think I'm perfect?"
    show judith 68
    show ross 36f
    ross "Of course, sweetie!"
    ross "Just look at that curvaceous body..."
    ross "How could anyone resist it?"
    show ross 37f
    pause
    show ross 36f
    ross "Now, don't you move an inch!"
    ross "Give the artists a chance to capture your beauty!"
    show ross 37f
    show judith 69b
    jud "O-Okay..."



    scene location_school_art_cutscene07
    with fade
    show text "{b}Miss Ross{/b} had definitely made {b}Judith{/b} more comfortable." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... And she had given me the perfect inspiration for my drawing!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Though it was little hard to concentrate on my work with {b}Miss Ross{/b} hovering over my shoulder..." at Position (xpos=512, ypos=700) with dissolve
    pause
    hide text
    with dissolve

    scene location_school_art_closeup
    show judith 68 zorder 1 at Position(xpos=0.4, ypos=1.0)
    show ross 36f zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    ross "It's very good, {b}[firstname]{/b} but I think you could do better."
    ross "I'm not sure you're really capturing the curves of her delicious body."
    show ross 37f
    player_name "What do you mean?"
    show ross 36f
    ross "Well have a look!"
    ross "Sometimes you have to really get hands on with your subject and feel the shapes."
    ross "... And {b}Judith{/b} here has such great contours!"
    hide ross
    show judith 70
    with dissolve
    pause
    show judith 71 with dissolve
    pause
    show judith 72 with dissolve
    pause
    show judith 72b
    jud "( !!! )" with hpunch
    jud "AAAhh!"
    show judith 72e
    ross "... Well look who came out to play!"
    show judith 72c_72d
    pause
    jud "Mmm..."
    show judith 72e
    ross "How does that feel, sweetie?"
    show judith 72
    jud "Really..."
    jud "Ahh, really good!"
    show judith 72e
    ross "Yes, you just enjoy, Dear."
    show judith 72c_72d
    jud "NNGGHH!"
    pause
    show judith 72
    jud "Haaaah!"
    show judith 72e
    ross "Beautiful!"
    show judith 72
    jud "OH, I CAN'T!"
    show judith 73 zorder 1 at Position(xpos=0.45, ypos=1.0)
    show ross 37f zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    jud "( !!! )" with hpunch
    jud "AAAHHH!"
    show judith 66
    jud "Haaah... Haaah..."
    show judith 65
    show ross 36f
    ross "Very good, sweetie!"

    show judith 58f zorder 0 at left
    show ross 37f
    with dissolve
    jud "That was..."
    show judith 57f
    jud "..."
    show judith 58f
    jud "... Can we do that again?"
    show judith 57f
    show ross 36f
    ross "... Maybe later, sweetie."
    show ross 36 at Position(xpos=0.60, ypos=1.0)
    with dissolve
    ross "Do you understand now, what I mean about feeling the shapes, {b}[firstname]{/b}?"
    show ross 37
    player_name "I'm not sure..."
    show mia 82 zorder 1 at Position(xpos=0.35, ypos=1.0) with dissolve

    mia "I think I get it, {b}Miss Ross{/b}!"
    show mia 81
    show ross 36f with dissolve
    ross "Good, you can help me show him then."
    show ross 36 with dissolve
    ross "Come up here and join us, {b}[firstname]{/b}!"
    show ross 37
    player_name "Really?"
    show ross 36
    ross "Yes, this is something every good artist needs to understand."
    hide mia
    hide ross
    show rossg 3 at Position(xpos=0.60, ypos=1.0)
    with dissolve
    player_name "O-okay."
    show rossg 1
    ross "Now, go ahead."
    show rossg 2
    ross "Both of you..."
    show rossg 1
    ross "... Feel the shapes."
    show rossg 4
    mia "Hehehe, okay!"
    show rossg 5_6 with dissolve
    pause
    show rossg 3 with dissolve
    player_name "... Like that?"
    show rossg 1
    ross "Mmmhmm... Just like that..."
    show rossg 4
    mia "Hehehee, I hope God isn't watching..."
    show rossg 2
    ross "You're both doing a great job!"
    show rossg 1
    ross "Keep going."
    show rossg 5_6 with dissolve
    pause
    ross "Mmm..."
    pause
    show rossg 1 with dissolve
    ross "Very good, {b}[firstname]{/b}!"
    show rossg 2
    ross "Now try feeling, {b}Mia's{/b} shapes."
    show rossg 3
    player_name "I uhh..."
    show rossg 4
    mia "It's okay!"
    mia "Feel the shapes, {b}[firstname]{/b}!"
    show rossg 7_8 at Position(xpos=0.59, ypos=1.0) with dissolve
    pause
    show rossg 4 at Position(xpos=0.6, ypos=1.0) with dissolve
    mia "Honk Honk!"
    show rossg 9 with dissolve
    mia "Pfft, Hahahahaha!!!!"
    show rossg 2 with dissolve
    ross "Oh, isn't she just the most adorable thing ever?!"
    ross "Alright, now feel mine again..."
    show rossg 5_6 with dissolve
    pause
    show judith 58f
    jud "... You guys can feel my shapes if you want."
    show judith 57f
    show rossg 2 with dissolve
    ross "Well, goodness! Look who's finally coming out of her shell!"
    ross "We'll get to you in a second, sweetie. Why don't you go check the supply cabinet for me..."
    ross "There should be some incense and candles in there to help us set the mood."
    show judith 58f
    show rossg 5_6 with dissolve
    jud "... Yes, Ma'am."
    hide judith
    with dissolve
    pause
    show rossg 10 with dissolve
    smi "WHAT IN THE WORLD IS GOING ON IN HERE!?" with hpunch
    smi "WHY ARE YOU ALL NAKED?!"
    hide rossg
    show mia 83 zorder 2 at left
    show ross 39 zorder 1 at Position(xpos=0.25, ypos=1.0)
    show player 100 zorder 0 at Position(xpos=0.35, ypos=1.0)
    show principal 3 at right
    with dissolve
    ross "{b}Principal Smith{/b}! I was just teaching the students some art techniques..."
    show ross 38
    show principal 38
    smi "ART TECHNIQUES?!?! DO I LOOK LIKE AN IDIOT TO YOU?!"
    show ross 39
    show principal 3
    ross "Of course not, we were just-"
    show principal 28
    show ross 38
    smi "DO I NEED TO REMIND YOU THAT THIS IS A SCHOOL AND NOT A BROTHEL!"
    show ross 39
    show principal 3
    ross "You're being ridiculous, I'm just trying to help them improve their art."
    hide principal
    show principal 34 zorder 3 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    show ross 38
    smi "JUST GET SOME CLOTHES ON, ALL OF YOU!" with hpunch

    hide mia
    hide player
    show principal 29 at right
    show ross 17 at Position(xpos=0.25, ypos=1.0)
    with dissolve
    pause
    show ross 16 at Position(xpos=0.25, ypos=1.0) with dissolve
    pause
    show ross 15 at Position(xpos=0.26, ypos=1.0) with dissolve
    pause
    show ross 14 at Position(xpos=0.26, ypos=1.0) with dissolve
    pause
    show ross 24 zorder 1 at Position(xpos=0.25, ypos=1.0)
    show mia 41 zorder 2 at left
    show player 8 zorder 0 at Position(xpos=0.35, ypos=1.0)
    with dissolve
    show principal 27
    smi "You had better have a damn good explanation for this, {b}Barbara{/b}!"
    show mia 45
    show player 11 at Position(xpos=0.38, ypos=1.0)
    with dissolve
    show ross 25
    show principal 29
    ross "{b}Mia{/b} and I were helping {b}[firstname]{/b} here practice."
    ross "Trying to prepare him for-"
    show ross 24
    ross "..."
    show principal 27
    smi "Prepare him for what?!"
    show principal 29
    show mia 46
    mia "This ar-"
    show mia 45
    show ross 25
    ross "A gift!"
    ross "... He was going to paint something for you, {b}Principal Smith{/b}!"
    show ross 24
    pause
    show ross 25
    ross "A gift, to hang up in your office!"
    show ross 24
    show principal 27
    smi "A gift?! For me?! What, like a portrait?"
    show principal 29
    show ross 25
    ross "Well, sure! If that's what you want..."
    show principal 27
    show ross 24
    smi "Is he any good?"
    show ross 25
    show principal 29
    ross "Very good, come have a look for yourself!"
    show principal 41 with dissolve
    pause
    show principal 42
    smi "What the hell is this?"
    show principal 41
    show mia 46
    mia "Oh, that's umm... That's mine, Ma'am."
    mia "... I'm not very good."
    show mia 45
    smi "..."
    show principal 42
    smi "Then why are you here, after school, taking private courses?"
    show principal 41
    show ross 25
    ross "My classes aren't just for talented artists."
    ross "They are open to anyone with a desire to express themselves through art."
    ross "... And {b}Mia{/b} here has a great love for art."
    show ross 24
    show principal 42
    smi "Uh huh..."
    smi "In reality, you just found yourself a cute little package didn't you?"
    show principal 41
    show ross 25b
    ross "That's not..."
    show ross 24
    show principal 42
    smi "... And now you're just working to unwrap it, huh?"
    smi "Have youself a little taste?"
    smi "... I'm well aware of your methods {b}Barbara{/b}."
    hide principal
    show principal 43 at Position(xpos=0.7, ypos=1.0)
    with dissolve
    pause
    show principal 44 at Position(xpos=0.72, ypos=1.0) with dissolve
    smi "Hmm."
    show principal 45
    smi "The boy painted this?"
    show principal 44
    show player 10
    player_name "Yes, Ma'am."
    show player 11
    show principal 45
    smi "Well, I guess I was wrong about you, {b}[firstname]{/b}."
    smi "You're actually good for something, after all..."
    show principal 44
    show ross 11
    ross "He is very talented, isn't he?"
    show ross 24
    hide principal
    show principal 27 at right
    with dissolve
    smi "Oh, shut up!"
    smi "I should fire you, right here and now!"
    smi "In here getting groped by naked students..."
    hide principal
    show principal 35b at Position(xpos=0.83, ypos=1.0)
    with dissolve
    smi "..."
    show principal 35c
    smi "This is impressive work though."
    show principal 35
    smi "Hmm..."
    hide principal
    show principal 27 at right
    with dissolve
    smi "I'm feeling generous so I {b}-MIGHT-{/b} let this incident slide!"
    show ross 25
    show principal 26
    ross "That would be wond-"
    show ross 24
    show principal 27
    smi "... But only if your student here can recreate this quality on a portrait of me!"
    show principal 26
    show ross 25
    ross "Oh, that's shouldn't be a problem. Right, {b}[firstname]{/b}?"
    show ross 24
    show player 10
    player_name "Uhh..."
    show player 11
    show principal 27
    smi "And it has to be to my exact specifications!"
    smi "No funny business!"
    show principal 29
    show ross 25
    ross "Oh, of course! Anything you want, Ma'am."
    show principal 27
    show ross 24
    smi "Damn right, anything I want!"
    show principal 27
    smi "Now you kids get your asses home before I change my mind and expel you both!"
    show principal 29
    show ross 25
    ross "Go on you two. I'll see you tomorrow."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
