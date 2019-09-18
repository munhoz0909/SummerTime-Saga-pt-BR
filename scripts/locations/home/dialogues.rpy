label home_diane_checkup_results:
    scene expression "backgrounds/location_home_entrance_night_blur.jpg"
    show player 13 at left
    show diane b_casual a_casual_sides f_normal_talk
    with dissolve
    dia "Obrigado por ir comigo, {b}[firstname]{/b}."
    dia "Você foi tão bom hoje!"
    show diane f_normal
    show player 14
    player_name "Sem problemas."
    player_name "Estou feliz por termos boas notícias."
    show player 13
    show diane f_normal_talk
    dia "Eu também."
    hide player
    show diane kiss_casual
    with dissolve
    pause
    show player 13 at left
    show diane b_casual a_casual_sides f_normal_talk
    with dissolve
    dia "Nós vamos começar amanhã, ok?"
    show diane f_normal
    show player 14
    player_name "Tudo bem."
    show player 13
    show diane f_normal_talk
    dia "É melhor você ir dormir e ter uma boa noite de sono."
    show diane f_wink
    pause
    show diane f_smirk_talk
    dia "Muito trabalho duro esperando por você amanhã, garanhão."
    show diane f_smirk
    show player 29 with dissolve
    player_name "{b}*Gulp*{/b} Sim, ok."
    hide player
    hide diane
    with dissolve
    return

label home_front_mom_mrsj_visit:
    scene home_front
    show debbie 164f zorder 2 at left
    show mrsj 17 at right
    with dissolve
    mrsjo "Ei, {b}[deb_char_name]{/b}!"
    show debbie 165f
    show mrsj 14
    deb "Oh olá, {b}Tammy{/b}."
    show debbie 164f
    show mrsj 17
    mrsjo "Eu queria parar e dar minhas condolências pela sua perda. Eu sei que ele era seu amigo íntimo..."
    show debbie 165f
    show mrsj 14
    deb "Obrigado. Isso é muito ... atenciosa de você."
    show debbie 169f
    show mrsj 19
    mrsjo "Eu só quero que você saiba disso, {b}Erik{/b} E eu estamos por perto se você precisar de alguma coisa."
    mrsjo "... Mesmo que você só precise conversar."
    show debbie 168f
    show mrsj 14
    deb "Isso é muito generoso."
    show debbie 169f
    show mrsj 17
    mrsjo "Eu sei que esta é uma situação completamente diferente para você, mas eu posso relacionar você sabe?"
    show debbie 168f
    show mrsj 14
    deb "Quer dizer, por causa do seu marido?"
    show debbie 169f
    show mrsj 17
    mrsjo "Claro!"
    show mrsj 20
    mrsjo "Quer dizer, meu marido saiu a muito tempo ... Então é um pouco diferente."
    show mrsj 18
    mrsjo "... Mas eu já estava sozinha há muito tempo!"
    show debbie 168f
    show mrsj 14
    deb "Fica solitária, não é facil?"
    deb "Não é fácil estar sozinha."
    show debbie 169f
    show mrsj 20
    mrsjo "Sim, eu passei por tempos dificieis..."
    show mrsj 17
    mrsjo "... Mas então eu decidi Relocar minha casa e acabei morando com {b}Erik{/b}"
    mrsjo "Ele tem sido uma benção!"
    show debbie 168f
    show mrsj 14
    deb "Como assim?"
    show debbie 169f
    show mrsj 17
    mrsjo "Ele é um jovem tão doce e ele precisa de mim para cuidar dele!"
    show debbie 169bf
    mrsjo "É bom ser utíl novamente. Isso realmente me dá um senso de propósito, sabe?"
    show debbie 169f
    mrsjo "Eu cozinho para ele e faço a roupa dele. Pergunto sobre o seu dia, E dou carinho quando ele precisa."
    show debbie 168f
    show mrsj 14
    deb "Entendo..."
    show debbie 169f
    show mrsj 18
    mrsjo "Eu acho que está ajudando ele a sair da sua concha também! Então, é benéfico!"
    show debbie 168f
    show mrsj 14
    deb "Eu só não sei como falar com {b}[firstname]{/b}. Quer dizer, Eu sei que ele precisa de orientação, Mas não sou a mãe dele..."
    show debbie 169f
    show mrsj 17
    mrsjo "Bem, continue assim, querida. Não vai se resolver da noite para o dia."
    mrsjo "Apenas se concentre nele e em como ele está se sentindo. Foi o que eu fiz!"
    mrsjo "O resto vai se encaixar em breve."
    show debbie 168f
    show mrsj 14
    deb "Eu espero que você esteja certo."
    show debbie 169f
    pause
    show player 1 zorder 1 at Position(xpos=300) with dissolve
    show debbie 165f
    deb "Oi docinho!"
    show debbie 164f
    show player 14
    player_name "Oi, {b}[deb_name]{/b}... Oi, {b}Sra. Johnson{/b}!"
    show player 1
    show mrsj 17
    mrsjo "Olá, {b}[firstname]{/b}."
    mrsjo "{b}[deb_char_name]{/b} estava apenas me dizendo o quanto ela está feliz por você morar com ela..."
    show mrsj 14
    show player 14
    player_name "Sim? Eu sou muito grato por ela me levar pra morar na casa."
    show mrsj 17
    show player 13
    mrsjo "Ela é uma boa mulher, então é melhor cuidar bem dela!"
    show mrsj 14
    show player 14
    player_name "Eu vou concerteza!"
    show player 1
    show mrsj 17
    mrsjo "Hehe, Vejo você depois {b}[deb_name]{/b}? Vocês vão ficar bem!"
    mrsjo "Bem, e melhor eu voltar pra casa."
    show mrsj 14
    show debbie 165f
    deb "Tem certeza que você não quer entrar?"
    show debbie 164f
    show mrsj 17
    mrsjo "Não, obrigada! Eu realmente preciso ir ver se {b}Erik{/b} precisa de alguma coisa..."
    show mrsj 14
    show debbie 165f
    deb "Bem, obrigado pela conversa {b}Tammy{/b}. Venha nos ver novamente em breve!"
    show debbie 164f
    show mrsj 17
    mrsjo "Eu farei isso! Vocês dois cuidam um do outro agora?"
    hide mrsj
    hide debbie
    hide player
    with dissolve
    return

label home_front_mom_mow_lawn:
    show expression "backgrounds/location_home_grass_cutscene_01.jpg"
    show expression FilteredText("Isso é muito mais difícil do que eu esperava. Eu deveria ter prestado mais atenção em como {b}Dad{/b} costumava fazer isso.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    show expression "backgrounds/location_home_grass_cutscene_02.jpg"
    show expression FilteredText("Não parece nada mal. Eu espero {b}[deb_name]{/b} pensa o mesmo.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    show expression "backgrounds/location_home_grass_cutscene_03.jpg"
    show expression FilteredText("Hmm, Eu me pergunto há quanto tempo ela está parada aí? Eu estava tão focado que não notei ela sair.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    pause 0.5

    scene home_front
    show player 2 at left
    show xtra 15 zorder 2 at Position(xpos=170,ypos=754)
    show debbie 1 at right
    with dissolve
    player_name "{b}[deb_name]{/b}, Eu terminei o gramado."
    show player 203
    show debbie 2
    deb "Eu vi tudo. Parece ótimo, querido!"
    show debbie 3
    deb "Você fez um trabalho maravilhoso!"
    show debbie 2
    deb "Estou orgulhosa de você."
    show player 2
    show debbie 1
    player_name "Eu estava apenas fazendo e pensando se meu {b}pai{/b} estivesse aqui como seria."
    show player 11
    show debbie 2
    deb "Bem, tenho certeza que ele ficaria orgulhoso também."
    deb "Ele sempre arrumava um jeito para me ajudar por aqui."
    show player 21
    show debbie 1
    player_name "eu irei também, {b}[deb_name]{/b}. Eu sinto que é o que ele quer."
    show player 2
    player_name "Devemos entrar agora?"
    show debbie 1
    deb "Certo!"
    scene home_front with None
    show xtra 15 zorder 2 at Position(xpos=520,ypos=754)
    show player 10 zorder 1
    with dissolve
    player_name "{b}*Ofegante*{/b}"
    show player 14
    player_name "Uau, isso foi muito trabalho!"
    show player 24
    player_name "Eu preciso tirar essas roupas fedorentas e tomar banho agora..."
    show player 4 at Position(xoffset=5)
    player_name "Eu deveria ir {b}lá embaixo para colocar essas roupas na lavagem{/b}."
    hide player with dissolve
    return

label home_front_mom_car_fixed:
    scene expression game.timer.image("home_front_mechanic{}_b")
    show jai 2 at left
    show debbie 1 at right
    with dissolve
    jaing "Tudo está como novo, senhora."
    show jai 1
    show debbie 3
    deb "Mesmo? Isso foi rápido!"
    show debbie 1
    show jai 2
    jaing "Pode apostar!"
    jaing "Eu sempre trabalho duro quando uma mulher bonita está envolvida!"
    jaing "Você pode me ligar se tiver mais problemas."
    jaing "Eu amo fazer RON RONAR pequenos motores de senhoras. Sabe o que eu quero dizer?"
    show jai 1
    show debbie 3
    deb "Pare. Você é hilario!"
    deb "Ha Ha Ha."
    show jai 2
    jaing "Huck Huck Huck."
    show jai 1
    show debbie 1
    show player 14 zorder 1
    player_name "Oi, {b}[deb_name]{/b}."
    show player 13
    show debbie 2
    deb "Oi Docinho!"
    show debbie 1
    show player 10f with dissolve
    player_name "Conserto do motor està terminado?"
    show player 5f
    show jai 2
    jaing "Bem, eu tive que substituir muitas peças, mas sim. Está tudo terminado."
    jaing "Apenas mais um dia na vida de {b}Jiang{/b} consertando carros. Não precisa me agradecer."
    show player 11f
    jaing "Huck Huck."
    jaing "Acho melhor eu deixar vocês vou indo!"
    show player 5f
    jaing "Só vou dar uma espiada no seu capô para ter certeza de que não deixei minha ferramenta dentro dela. Sabe o que eu quero dizer?"
    show jai 1
    show debbie 2
    deb "{b}*Corar*{/b} Sim, bem. Obrigada novamente!"
    show debbie 1
    show jai 2
    jaing "Sem poblema, senhora."
    hide jai with dissolve
    show player 13 with dissolve
    show debbie 2
    deb "Quer fazer um test drive?"
    show debbie 1
    show player 14
    player_name "Certo!"
    show player 12
    player_name "Espero que ele não esteja tentando nos ferrar."
    show player 5
    show debbie 14
    deb "( Ele estava tentando ferrar alguém bem... )"
    hide player
    hide debbie
    with dissolve
    return

label home_front_mom_car_fixed_check_car:
    scene car_interior
    show debbie car 2b at right
    show player car 1b
    show player_arms car 1
    show debbie_arms_car 1
    show xtra 30 at right
    with dissolve
    deb "Vamos ver..."
    show player car 2b
    show debbie car 1
    hide debbie_arms_car
    with dissolve
    deb "Hmm..."
    show debbie car 2b
    show debbie_arms_car 1
    with dissolve
    deb "Funciona!"
    show debbie car 3
    show player car 2
    player_name "Ótimo!"
    show player car 1
    show debbie car 2
    player_name "Parece está muito bom o concerto."
    show player car 2b
    show debbie car 3b
    deb "Como você conseguiu Chamar eles tão rapidamente?"
    show debbie car 3
    show player car 2
    player_name "Não foi nada {b}[deb_name]{/b}."
    show player car 5
    player_name "Eu acho que posso ser bastante persuasivo..."
    player_name "Estou aliviado em ver você sorrindo de novo..."
    show player car 6
    pause
    show player car 5b
    show debbie car 3b
    show debbie_arms_car 2 with dissolve
    deb "Ah..."
    deb "Obrigado querido."
    scene car_interior kiss
    hide player car
    hide debbie_arms_car
    hide player_arms car
    show debbie car 6 at right
    show xtra 30 at right
    with dissolve
    pause
    show player_boner car 1 with dissolve
    pause
    scene car_interior
    show player car 3b
    show player_arms car 2
    show debbie car 3 at right
    show debbie_arms_car 2
    show xtra 30 at right
    show player_boner car 1
    with dissolve
    pause
    show debbie car 4c
    show debbie_arms_car 4 with dissolve
    deb "( !!! )"
    show debbie car 5b
    deb "Oh!"
    show debbie car 4c
    show player car 4c
    player_name "Desculpa, {b}[deb_name]{/b}..."
    show player car 3
    show debbie car 5b
    deb "Está tudo bem querido."
    deb "Você parece estar sentindo isso com bastante, frequência quando estou por perto."
    show debbie car 4b
    show debbie_arms_car 2 with dissolve
    deb "Eu não tenho certeza Se eu deveria estar preocupado de ficar lisonjeado?"
    show debbie car 3
    show player car 4c
    show player_arms car 1 with dissolve
    player_name "Desculpe ... Eu estou realmente tentando evitar, mas você é tão bonita."
    show player car 3
    show debbie car 4
    deb "..."
    show debbie car 5b
    deb "Querido..."
    hide player_boner car
    show debbie_arms_car 5b at Position(xalign = 0.357, yalign = 0.558)
    with dissolve
    deb "Eu suponho que não é uma coisa tão ruim."
    show debbie car 5
    show player car 4c
    player_name "{b}[deb_name]{/b}?"
    show player car 3
    show debbie car 3b
    deb "Shhh."
    show debbie car 5b
    show debbie_arms_car 5 with dissolve
    deb "É normal que os jovens da sua idade fiquem assim o tempo todo."
    show debbie car 5
    show player car 3b
    player_name "{b}*Gole*{/b}"
    show player car 3
    show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_mom) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558) with dissolve
    pause 1.2
    show debbie_arms_car 5 with dissolve
    show debbie car 5b
    deb "Eu realmente gostaria de poder te ajudar com isso, querido."
    deb "... Mas isso simplesmente não estaria certo."
    show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_mom) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558) with dissolve
    show debbie car 3b
    deb "Você precisa encontrar alguém da sua idade..."
    deb "Alguém  para ser sua namorada. Isso não seria legal?"
    show debbie car 3
    show debbie_arms_car 5c with dissolve
    show player car 5
    player_name "Hum sim, Acho que você estar certa..."
    show player car 5b
    show debbie car 3b
    deb "Isso é bom."
    show debbie_arms_car 5 with dissolve
    deb "Você quer que eu continue?"
    show debbie car 3
    return

label home_front_mom_car_fixed_check_car_little_longer:
    show player car 5
    player_name "Pode ... você pode continuar um pouco mais?"
    show player car 2
    player_name "Isso é tão bom!"
    show player car 2b
    show debbie car 3b
    deb "Tudo bem, {b}[firstname]{/b} mas eu não vou terminar se é isso que você está pensando..."
    show debbie car 3
    return

label mom_car_jerk_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_mom) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
                $ animated = True
        else:

            $ pose_counter = 0
            $ pose_list = [5,"5b","5c","5b"]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbie_arms_car {}".format(pose_list[pose_counter]) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1

        if animcounter == 1 or M_mom.get("jerk count") == 1:
            show debbie car 3
        else:
            show debbie car 4
            show player car 4b
        pause 2

        if animcounter == 3 and M_mom.get("jerk count") >= 1:
            show player car 4c
            pause 1
        $ animcounter += 1

    $ M_mom.set("jerk count", M_mom.get("jerk count") + 1)

    if M_mom.get("jerk count") == 2:
        jump expression game.dialog_select("home_front_mom_car_fixed_check_car_finished")
    call screen car_mom_jerk_options

label home_front_mom_car_fixed_check_car_finished:
    if M_mom.get("jerk count") == 2:
        call expression game.dialog_select("home_front_mom_car_fixed_check_car_finished_too_much")
    else:
        call expression game.dialog_select("home_front_mom_car_fixed_check_car_finished_not_enough")
    call expression game.dialog_select("home_front_mom_car_fixed_check_car_finished_after")
    $ M_mom.trigger(T_mom_car_fun)
    $ game.timer.tick()
    $ game.main()

label home_front_mom_car_fixed_check_car_finished_too_much:
    show player car 3
    show player_boner car 1
    hide debbie_arms_car
    show debbie_arms_car 4
    with dissolve
    show debbie car 5b
    deb "Eu não acho que deveria continuar fazendo isso..."
    show debbie car 5
    show debbie_arms_car 1 with dissolve
    show player car 5
    player_name "mas, {b}[deb_name]{/b}"
    show player car 3
    return

label home_front_mom_car_fixed_check_car_finished_not_enough:
    show player car 4c
    player_name "Eu acho que devemos parar, né?"
    show player car 4b
    show debbie car 5
    deb "..."
    show player_boner car 1
    hide debbie_arms_car
    show debbie_arms_car 4
    with dissolve
    show debbie car 5b
    deb "É uma boa ideia, querido."
    show debbie car 5
    show debbie_arms_car 1 with dissolve
    show player car 5
    player_name "... Sim."
    show player car 5b
    return

label home_front_mom_car_fixed_check_car_finished_after:
    show debbie car 5b
    deb "Se você sentir ereção, você deve ir até o seu quarto, E da uma aliviada."
    show debbie car 3b
    deb "...Certo, docinho?"
    show debbie car 3
    show player car 4c
    player_name "... Sim, senhora."
    scene black with fade
    hide debbie
    hide debbie_arms_car
    hide xtra
    hide player
    hide player_arms car
    hide player_boner car
    return

label home_front_mom_bad_guys_revisit:
    scene home_front_car
    $ playMusic("<loop 73.5>audio/music_villain.ogg", 1.0)
    show player 11f at right with dissolve
    player_name "!!!"
    player_name "( É aquele carro de novo! )"
    player_name "( ... Ele tem ameaçado {b}[deb_name]{/b} muitas vezes. )"
    hide player
    $ playSound()
    show expression "backgrounds/location_home_entrance_cutscene01.jpg"
    show expression FilteredText("Quando olhei pela janela, vi o cara que estava entregando todas as ameaças.\nParece que ele trouxe de volta desta vez.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    show expression "backgrounds/location_home_entrance_cutscene02.jpg"
    show expression FilteredText("Eu não pude ouvir o que eles estavam dizendo, mas {b}[deb_name]{/b} Parecia apavorada.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    play audio smack
    hide cutscene
    show expression "backgrounds/location_home_entrance_cutscene03.jpg"
    show expression FilteredText("... Então um dos valentões a derrubou no chão!") as cutscene at Position (xpos= 512, ypos= 700)
    with hpunch
    pause
    hide cutscene
    show expression FilteredText("Não havia como eu ficar ali parado e assistir...\nI {b}tive{/b} que fazer alguma coisa!") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene

    scene home_entrance_fight
    show debbie 40 at Position(xpos=156,ypos=768)
    show henchman2 1 at right
    with dissolve
    python:
        tmp = deb_name.upper()
    player_name "{b}[tmp]{/b}!!"
    show player 205 at Position(xpos=350,ypos=768) with dissolve
    player_name "Qual o problema com você?!"
    show player 204
    deb "{b}[firstname]{/b}, Deixe que resolvo tudo..."
    show player 205
    player_name "Que tipo de homem bate em uma mulher indefesa?!"
    show player 204
    show henchman2 2
    henchman2 "Não seja idiota, garoto. Isso não lhe diz respeito."
    show player 205
    show henchman2 1
    player_name "Saia de perto! Se você tocá-la novamente eu vou!"
    show player 204
    show henchman2 3
    henchman2 "Hã! O que você vai fazer?!"
    show henchman2 1
    player_name "..."
    show player 205
    player_name "Eu vou chamar a polícia e você vai responder por isso!"
    show player 204
    show henchman2 3
    hide debbie with dissolve
    henchman2 "Acho que não."
    show henchman2 1
    hide player
    show henchman1 7 at Position(xpos=350,ypos=768) with hpunch
    player_name "Ei! Me solte!"
    show henchman1 8
    hide henchman2
    show henchman2 3 at right
    henchman2 "Hahah, fácil , assassino..."
    henchman2 "Seu {b}Pai{/b} nos devia {b}MUITO{/b}dinheiro..."
    henchman2 "A {b}dívida{/b} que agora pertence a vocês dois!"
    show henchman2 2
    henchman2 "... E você vai pagar. De Qualquer forma..."
    show henchman1 9
    show henchman2 5
    with hpunch
    deb "{b}[firstname]{/b}!!!"
    show henchman2 3
    show henchman1 10 at Position(xpos=340,ypos=768)
    henchman2 " E Quanto às autoridades..."
    show henchman2 2
    henchman2 "... Eu os deixaria de fora a menos que você queira que isso aconteça {b}realmente{/b} e vire uma bagunça!"
    henchman2 "Se você se preocupa com suas vidas, você vai{b} trazer o dinheiro{/b} ao {b}armazém{/b} como você foi dito!"
    show henchman2 4
    henchman2 "Você não nos quer voltando aqui! {b}certo{/b}, Senhora?!"
    show player 184
    show henchman1 6f at left
    show henchman2 2
    with vpunch
    henchman2 "Vamos, vamos sair desse lixo."
    $ playMusic()
    hide henchman1
    hide henchman2
    with dissolve
    pause
    hide player
    show debbie 41 at left
    with dissolve
    deb "Docinho você estar bem?"
    show debbie 44 at left
    show jenny f_sad_talk
    with dissolve
    jen "O que diabos está acontecendo?"
    jen "Eu ouvi gritos!"
    show jenny f_surprised a_dressed_up_surprised with dissolve
    jen "( !!! )"
    jen "Oh Deus, ele está bem?!"
    show debbie 43
    show jenny f_sad a_dressed_side with dissolve
    deb "Ele ficará bem. Se acalme..."
    deb "Eles foram embora."
    show debbie 44
    show jenny f_sad_talk
    jen "Precisamos ligar para alguém!"
    show jenny f_sad
    show debbie 43
    deb "NÃO! Nós não podemos fazer isso!"
    show debbie 44
    show jenny f_sad_talk
    jen "O que?! {b}[deb_name]{/b} aqueles homens invadiram aqui e agrediram vocês!"
    jen "Nós não podemos simplesmente deixá-los"
    show jenny f_sad
    show debbie 45
    deb "eu disse {b}NÃO{/b}, {b}[jen_name]{/b}!"
    show debbie 43
    deb "... Somente..."
    deb "Volte para o seu quarto e deixe-me lidar com isso. OK?"
    show debbie 44
    show jenny f_sad_talk
    jen "Eu... Ok..."
    hide jenny
    with dissolve
    show debbie 41
    deb "Vai ficar tudo bem, querido."
    show debbie 42
    player_name "Desculpa. Eu não pude pará-los, {b}[deb_name]{/b}..."
    show debbie 41
    deb "Não se desculpe. Foi muito corajoso da sua parte tentar!"
    deb "Você estava tentando nos proteger."
    show debbie 42
    player_name "O que nós vamos fazer?"
    show debbie 41
    deb "Não se preocupe com isso agora; Estamos a salvo."
    show debbie 42
    deb "..."
    show debbie 41
    deb "Como está seu rosto?"
    show debbie 42
    player_name "Meu nariz dói..."
    player_name "... E estou sangrando em todos os lugares."
    show debbie 41
    deb "Vamos, vamos te limpar."
    hide debbie with dissolve
    scene shower2
    show debbie 39f at left
    show player 209f
    with dissolve
    deb "Parece que o sangramento parou..."
    show debbie 63f
    deb "Você deveria tomar um banho, querido."
    deb "Ajudará com o inchaço."
    show player 210
    deb "Eu vou buscar algumas roupas limpas."
    show debbie 38f
    hide debbie
    hide player
    scene hallway
    show debbie 38
    with fade
    deb "( ... )"
    deb "( Eu sinto que deveria estar lá com ele ... Certificando-se de que ele está bem. )"
    deb "( Talvez seja melhor que eu lhe dê um pouco de privacidade... )"
    deb "( Vou deixar suas roupas do lado de fora da porta. )"
    pause
    show debbie 125 with fastdissolve
    deb "( Pobre Garoto. )"
    deb "( Eu não posso acreditar que ele enfrentou aqueles homens ... Por minha causa. )"
    deb "( Essa foi a coisa mais corajosa que eu já vi! )"
    deb "( Hmm... )"
    deb "( ... Talvez eu deva entrar e verificar ele. )"
    deb "( Só para ter certeza que ele não precisa da minha ajuda. )"
    scene shower_closeup
    show debbies 26 zorder 2
    with fade
    player_name "Cara ... Então é isso que levar um soco no rosto isso doi muito..."
    show debbies 27 with dissolve
    pause
    show debbies_b zorder 1 at Position(xpos=350,ypos=768) with dissolve
    pause
    hide debbies_b
    show debbies 28 at Position(xpos=487,ypos=768)
    with dissolve
    pause
    show debbies 29 at Position(xpos=492,ypos=768)
    player_name "... Meu nariz deveria ser tão macio?"
    show debbies 31 at Position(xpos=484,ypos=768) with vpunch
    player_name "{b}[deb_name]{/b}??"
    player_name "Por que você"
    show debbies 30
    deb "Shhh, Tudo bem querido."
    deb "Deixe-me ajudá-lo..."
    show debbies 34
    deb "Você merece, depois do que fez para me proteger."
    show debbies 37_36
    pause 4
    show debbies 34
    deb "Como está seu rosto?"
    show debbies 35
    player_name "Melhor."
    show debbies 34
    deb "Fico feliz em ouvir isso."
    deb "Eu não quero que nada aconteça com meu valente homenzinho..."
    show debbies 36
    show debbies 76 with dissolve
    show debbies 41_76
    pause
    show debbies 42 with hpunch
    with dissolve
    deb "Aqui, querido, deixe-me ajudá-lo."
    show debbies 72
    player_name "... Você tem certeza?"
    show debbies 43
    deb "Tenho certeza, querido. Deixe-me cuidar de você..."
    show debbies 44
    deb "Você foi tão corajoso lá embaixo. enfrentando aqueles homens para nós."
    show debbies 45 with dissolve
    deb "estou muito orgulhosa de você..."
    show debbies 74
    player_name "... Ohh, isso é muito bom, {b}[deb_name]{/b}!"
    show debbies 73_74
    pause 4
    show debbies 73
    player_name "{b}[deb_name]{/b}, Eu vou gozar..."
    show debbies 46
    deb "Tudo bem, querido, apenas deixe sair!"
    show debbies 47 at Position(xpos=498,ypos=768)
    player_name "!!!"
    show white zorder 4 with dissolve
    show debbies 47 at Position(xpos=498,ypos=768)
    show playersex 33 zorder 3 at Position(xpos=610,ypos=880)
    hide white with dissolve
    pause
    show debbies 48
    hide playersex
    with dissolve
    deb "Nossa, isso foi muito esperma..."
    show debbies 44 at Position(xpos=484,ypos=768) with dissolve
    deb "Bom menino..."
    show debbies 34 at Position(xpos=447,ypos=768) with dissolve
    deb "Agora, isso não parece melhor?"
    show debbies 35 at Position(xpos=447,ypos=768)
    player_name "Oooh, você não tem ideia..."
    player_name "... Obrigado, {b}[deb_name]{/b}!"
    show debbies 34
    deb "Agora vamos te limpar."
    scene shower2
    with fade
    show player 261f at left with dissolve
    show debbie 35b with dissolve
    pause
    show player 8 with dissolve
    show debbie 35c with dissolve
    pause
    show player 21 with dissolve
    show debbie 34 with dissolve
    with dissolve
    player_name "{b}[deb_name]{/b}, Isso foi apenas desta vez?"
    show player 1
    show debbie 34
    deb "..."
    show debbie 35
    deb "Oh, querido ... eu não sei."
    show debbie 34
    deb "..."
    show debbie 35
    deb "Suponho que podemos fazer isso de novo."
    show debbie 36
    deb "Mas você não pode dizer {b}A NINGUÊM{/b} e não podemos levar as coisas longe demais!"
    show debbie 34
    deb "..."
    show debbie 36
    deb "... E nós {b}NÃO PODEMOS{/b} deixar {b}[jen_name]{/b} descobrir também!"
    deb "Você {b}entendeu{/b}?"
    show debbie 34
    show player 21
    player_name "Sim, {b}[deb_name]{/b}."
    show debbie 35
    show player 1
    deb "Tudo bem..."
    deb "Eu tenho que limpar a bagunça no andar de baixo..."
    show debbie 36
    deb "Eu quero que você espere alguns minutos antes de sair do banheiro."
    deb "De outra forma {b}[jen_name]{/b} vai suspeitar de algo. OK?"
    show debbie 32
    show player 28
    player_name "Ok, {b}[deb_name]{/b}."
    show debbie 33
    show player 1
    deb "Bom menino."
    hide debbie with dissolve
    pause
    show player 21f at Position(xpos=0.4, ypos=1.0) with dissolve
    player_name "... Uau!"
    player_name "Isso valeu totalmente um soco na cara!"
    hide player
    with dissolve
    show popup_debbieshower at truecenter with dissolve
    pause
    hide popup_debbieshower with dissolve
    return

label player_mailbox:
    $ player.go_to(L_home_mailbox)
    $ player.location.call_screen(False)

label player_mailbox_dialogue:
    $ player.go_to(L_home_mailbox)
    scene expression game.timer.image("player_mailbox{}")

    if erik.completed(erik_orcette) and not player.has_item("orcette") and not erik.known(erik_orcette_2) and orcette_mail_lock:
        call expression game.dialog_select("player_mailbox_erik_orcette_completed_pre")
        menu:
            player_name "O pacote é endereçado a mim. Isto deve ser {b}Erik's{/b} Brinquedo."
            "Deixe sozinho.":
                pause
            "Abra.":


                call expression game.dialog_select("player_mailbox_erik_orcette_completed_open")

        $ player.get_item("orcette")
        $ game.mail["player"] = ""
        call expression game.dialog_select("player_mailbox_erik_orcette_completed_after")

    elif game.mail["player"] == "m_pizza_pamphlet":
        call expression game.dialog_select("player_mailbox_pizza_pamphlet")
        $ L_pizzeria_exterior.unlock()
        $ L_dealership_front.unlock()

    elif game.mail["player"] == "m_newspaper":
        call expression game.dialog_select("player_mailbox_newspaper")
    $ player.location.call_screen(False)

label player_mailbox_erik_orcette_completed_pre:
    player_name "( Legal! Parece que sou o primeiro a receber o correio! )"
    return

label player_mailbox_erik_orcette_completed_open:
    show mailbox_item04_c at truecenter
    with dissolve
    pause
    player_name "( Então é isso que ela está esperando... )"
    player_name "( a {b}Orcette{/b}. )"
    player_name "( É melhor eu colocar isso de volta na caixa. )"
    return

label player_mailbox_erik_orcette_completed_after:
    show unlock38 at truecenter with dissolve
    pause
    hide unlock38
    hide mailbox_item04_c
    with dissolve
    player_name "( Hora de fazer isso {b}Erik{/b} antes que alguém me pegue carregando essa coisa. )"
    return

label player_mailbox_pizza_pamphlet:
    player_name "( Isso provavelmente é lixo eletrônico.)"
    show expression "objects/object_mailbox_item02_closeup.png" with dissolve
    player_name "( {b}Tony's Pizza{/b}? Eu não fui a esse lugar há algum tempo. )"
    player_name "( É melhor eu colocar isso de volta. )"
    hide expression "objects/object_mailbox_item02_closeup.png" with dissolve
    return

label player_mailbox_newspaper:
    player_name "( Notícias locais. Isso deve ser interessante... )"
    show expression "objects/object_newspaper.png" with dissolve
    player_name "( O ladrão ainda está solto? Você pensaria que eles teriam pegado ele agora... )"
    player_name "( É melhor eu colocar isso de volta. )"
    hide expression "objects/object_newspaper.png" with dissolve
    return

label bad_guys_driveby:
    $ player.go_to(L_home)
    call expression game.dialog_select("bad_guys_driveby_dialogue")
    $ M_mom.trigger(T_mom_bad_guys_watching)
    $ game.main()

label bad_guys_driveby_dialogue:
    scene location_home_driveby_cutscene1
    with fade
    show text "Hmm, Por que esse carro está dirigindo tão devagar?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Espere um segundo..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene location_home_driveby_cutscene2
    with fade
    show text "É aquele homem estranho que estava aqui fazendo ameaças outro dia!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Qual é o problema dele..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene location_home_front_day_blur
    show player 11
    player_name "..."
    show player 10
    player_name "eu sei que, {b}[deb_name]{/b} disse para não se preocupar com isso..."
    player_name "... Mas esse cara realmente me assusta!"
    show player 11
    player_name "..."
    hide player with dissolve
    return

label home_roxxy_studying_at_mcs:
    scene expression L_home_entrance.background
    show player 13 at left
    show roxxy 1f f at Position (xpos=400)
    show debbie 2 at right
    with dissolve
    deb "Olá docinho!"
    deb "Como foi "
    show debbie 13
    deb "... Oh."
    deb "Quem é?"
    show debbie 14
    show player 14
    player_name "{b}[deb_name]{/b}, essa é {b}Roxxy{/b}."
    player_name "Eu estou ajudando ela a estudar para a aula de francês."
    show player 13
    show debbie 3
    deb "Bem, isso é legal!"
    show debbie 2
    deb "estou feliz em te conhecer, {b}Roxxy{/b}."
    show debbie 1
    show roxxy 1bf
    rox "... Obrigada."
    rox "Prazer em conhece-la também."
    show roxxy 1f f
    show debbie 2
    deb "Eu estava terminando o jantar."
    deb "Você quer que eu traga o jantar ?"
    show debbie 1
    show player 14
    player_name "Sim, isso seria ótimo!"
    show player 13
    show roxxy 1bf
    rox "Eu não quero incomodar..."
    show roxxy 1f f
    show debbie 3
    deb "Não se preucupe querida!"
    show debbie 2
    deb "Vocês, crianças, sobem lá e se divertem!"
    deb "Vou levar o jantar assim que estiver pronto."
    show debbie 1
    show player 14
    player_name "Obrigado, {b}[deb_name]{/b}!"
    hide player
    hide roxxy
    hide debbie
    with dissolve
    scene expression game.timer.image("bedroom{}")
    show player 13 at left
    show roxxy 2 at right
    with dissolve
    rox "Sua Landlady é muito legal..."
    show roxxy 1
    show player 33
    player_name "Sim, tenho muita sorte."
    show player 13
    show roxxy 30
    rox "Então este é seu quarto?"
    show roxxy 1
    show player 10
    player_name "Uh Hã..."
    show player 5
    show roxxy 2
    rox "Bem, é bem idiota..."
    rox "... Mas eu acho que é legal também."
    show roxxy 1
    show player 14
    player_name "Heh, isso foi um elogio?"
    show player 13
    show roxxy 2
    rox "Não, não seja idiota."
    show roxxy 1
    show player 10
    player_name "Tudo bem, desculpe."
    player_name "Você está bem estudando aqui?"
    show player 5
    show roxxy 1b
    rox "A cama parece confortável."
    show roxxy 1
    show player 10
    player_name "... Você quer estudar na minha cama?"
    show player 11
    show roxxy 2
    rox "Certo. Por que não?"
    show roxxy 1
    show player 29 with dissolve
    player_name "Por mim tudo bem."
    hide player
    hide roxxy
    with dissolve
    scene expression "backgrounds/location_home_bedroom_bed_dialogue.jpg"
    show player bed 1 at right
    show roxxy 36b at left
    show roxxy_outfit at left
    with dissolve
    rox "So..."
    show roxxy 35b
    rox "..."
    show roxxy 35e
    rox "Você tem meninas aqui com freqüência?"
    show roxxy 35d
    show player bed 3
    player_name "Hã?"
    player_name "... Não, não realmente."
    show player bed 2
    show roxxy 35e
    rox "É a primeira vez que você teve uma menina na sua cama?"
    show roxxy 35d
    player_name "..."
    show player bed 3
    player_name "... Não?"
    show player bed 2
    show roxxy 35e
    rox "Você não é virgem você è?"
    show roxxy 35d
    show player bed 6
    player_name "!!!" with hpunch
    show player bed 3
    player_name "O que?!"
    player_name "Isso não é... quero dizer, eu não estou muito confortável..."
    show player bed 2
    player_name "..."
    show player bed 5
    player_name "Você está?"
    show player bed 4
    show roxxy 35c
    rox "Pfft!"
    show roxxy 37 at Position (xoffset=120, yoffset=-100)
    rox "Haha, como se eu dissesse a você! Eu estou apenas rindo!"
    show roxxy 35e at left
    rox "Eu te disse, estudar não é realmente o meu forte."
    show roxxy 35d
    show player bed 5
    player_name "O Vamos lá. Você não está nem tentando."
    player_name "Eu acho que você é mais esperta porque você não se esforça {b}Roxxy{/b}."
    show player bed 4
    show roxxy 38b
    rox "..."
    show roxxy 36 at Position (xoffset=120, yoffset=-100)
    rox "tanto faz..."
    show roxxy 35b
    show player bed 5
    player_name "Estou falando sério!"
    show player bed 4
    rox "..."
    show roxxy 35c
    rox "Você já teve namorada?"
    show roxxy 35b
    show player bed 6
    player_name "!!!" with hpunch
    player_name "..."
    show player bed 3
    player_name "Por que você me perguntaria isso?"
    show player bed 2
    show roxxy 37 at Position (xoffset=120, yoffset=-100)
    rox "Haha, que tédio..."
    show roxxy 35b
    show player bed 5
    player_name "Aqui olha, eu vou te mostrar um truque para tornar isso mais interessante..."
    show player bed 4
    show roxxy 40 at Position (xoffset=120, yoffset=-100)
    rox "Pfft, Ok, certo."
    show roxxy 35b
    show player bed 5
    player_name "Apenas olhe!"
    hide player
    hide roxxy
    hide roxxy_outfit
    with dissolve
    scene expression "backgrounds/location_home_bedroom_cutscene10.jpg"
    with fade
    show text "Passei horas tentando persuadir {b}Roxxy{/b} em estudar.\nEla na maior parte apenas me viu trabalhar e fez perguntas estranhas sobre a minha experiência com as meninas.\n... Mas finalmente consegui ensinar o que ela precisava saber." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene expression L_home_entrance.background
    show roxxy 1 at right
    show player 10 at left
    with dissolve
    player_name "Então, acho que podemos ter que fazer isso de novo algum dia, né?"
    show player 5
    show roxxy 2
    rox "Espero que não!"
    show roxxy 1
    show player 12
    player_name "O Vamos lá ... Não foi tão ruim assim!"
    show player 5
    rox "..."
    show roxxy 1b
    rox "... Não, não foi tão ruim assim."
    rox "Somente..."
    show roxxy 1
    rox "..."
    show roxxy 1b
    rox "Obrigada ... Por ser legal sobre tudo isso..."
    show roxxy 1
    show player 13
    player_name "..."
    rox "..."
    show roxxy 2
    rox "... Por que você está olhando assim para mim?"
    show roxxy 1
    show player 29 with dissolve
    player_name "Desculpe ... É só que ... eu não estou acostumado com você, ser legal, assim..."
    show player 3
    show roxxy 2
    rox "... Bem, não se acostume com isso!"
    rox "Você ainda é um idiota e eu vou te tratar como idiota na escola!"
    show roxxy 28 with dissolve
    rox "... Mas."
    show roxxy 27
    rox "..."
    hide player
    show roxxy 59 at left with dissolve
    player_name "!!!" with hpunch
    show player 11 at left
    show roxxy 1e at right
    with dissolve
    player_name "..."
    show player 10
    player_name "Para o que foi aquilo?"
    show player 11
    show roxxy 1b
    rox "... Apenas um pequeno show de gratidão."
    show player 13
    rox "Nada mais!"
    show roxxy 2
    rox "Não pense que significa alguma coisa!"
    show roxxy 1
    player_name "..."
    show player 29 with dissolve
    player_name "... Certo."
    player_name "Eu vou te levar pra casa então."
    show player 3
    show roxxy 1b
    rox "Não, eu vou ficar bem."
    rox "Atè Mais tarde, nerd!"
    hide roxxy with dissolve
    pause
    show player 34 with dissolve
    player_name "..."
    show player 35
    player_name "Porcos devem estar voando em algum lugar..."
    hide player with dissolve
    return

label home_front_roxxy_cookies_and_milk:
    scene expression L_home_entrance.background
    show player 5 at Position (xpos=400)
    show roxxy 32f at left
    show debbie 13 at right
    with dissolve
    deb "{b}[firstname]{/b}?"
    deb "O que na terra você está fazendo em casa tão cedo?"
    show debbie 14
    show player 10
    player_name "Ei, {b}[deb_name]{/b}."
    player_name "Minha amiga está tendo um dia muito difícil."
    show player 5
    show debbie 13
    deb "Oh!"
    show debbie 2
    deb "Olá de novo, querido..."
    show debbie 1
    show player 10
    player_name "Eu a trouxe aqui para conversar sobre as coisas."
    player_name "... E eu ofereci o almoço dela."
    player_name "Espero que esteja bem?"
    show player 5
    show debbie 3
    deb "Claro, tudo bem!"
    show debbie 2
    deb "... você è {b}Roxxy{/b}, não é isso?"
    show debbie 1
    show roxxy 33f
    rox "Sim, senhora."
    rox "Desculpe incomodar você novamente..."
    show roxxy 32f
    show debbie 3
    deb "Não é nenhum problema, querida!"
    show debbie 2
    deb "Por que vocês dois não subam as escadas e eu vou preparar algo para você?"
    show debbie 1
    show player 14
    player_name "Obrigado, {b}[deb_name]{/b}."
    scene black with fade
    pause

    scene expression game.timer.image("backgrounds/location_home_bedroom_day{}.jpg")
    show player 5 at left
    show roxxy 1l
    with dissolve
    rox "Sua {b}Landlady{/b} usa roupas?"
    show roxxy 1k
    show player 10
    player_name "Hã?"
    player_name "O que você quer dizer?"
    show player 5
    show roxxy 1i
    rox "..."
    show roxxy 1l
    rox "... deixa pra lá."
    show roxxy 30 at Position (xoffset=-33) with dissolve
    rox "Ugh, isso é um desastre..."
    rox "O que diabos eu vou fazer!"
    show roxxy 29 at Position (xoffset=-33)
    show player 10
    player_name "Acalme-se, {b}Roxxy{/b}."
    player_name "Não faz sentido fazer todo trabalhado antes de termos todos os detalhes."
    show player 5
    show roxxy 3c at Position (xoffset=-33)
    rox "O que você quer dizer?"
    show roxxy 3d at Position (xoffset=-33)
    show player 10
    player_name "Tudo o que sabemos é que {b}sua mãe{/b} foi presa por posse e que a polícia está investigando."
    player_name "Ainda pode haver uma maneira de salvar a situação."
    show player 5
    show roxxy 1k with dissolve
    rox "..."
    show roxxy 1l
    rox "Você realmente acha isso?"
    show roxxy 1k
    show player 10
    player_name "... Talvez."
    player_name "Devemos ir até a {b}Delegacia de polícia{/b} e descubrir exatamente o que está acontecendo."
    show player 5
    show roxxy 27
    rox "..."
    show roxxy 1l
    rox "Você está certo..."
    show roxxy 1k
    rox "..."
    show player 10
    player_name "Por enquanto, apenas respire e relaxe."
    player_name "Tenho certeza de que podemos encontrar uma maneira de corrigir isso."
    show player 5
    show roxxy 1l
    rox "... Por que você está sendo tão legal comigo?"
    show roxxy 1k
    show player 10
    player_name "Hã?"
    player_name "Eu..."
    show player 5
    show debbie 218 at right with dissolve
    deb "Eu trouxe lanches!"
    show roxxy 1kf at Position (xpos=400) with dissolve
    show player 13
    show debbie 217
    deb "Alguns leite fresco e biscoitos assados no forno..."
    deb "É a coisa perfeita para você se sentir melhor depois de um dia difícil, {b}Roxxy{/b}!"
    show debbie 219 with dissolve
    show roxxy 27f at Position (xoffset=33)
    show player 428
    pause
    show roxxy 1bf with dissolve
    rox "{b}*chorando*{/b} Oh, Uau!"
    show debbie 1 with dissolve
    show player 11
    rox "Isso parece maravilhoso, senhora!"
    show roxxy 1f f
    show debbie 3
    deb "Ah, bem obrigada, querida."
    show roxxy 32f at Position (xoffset=-34)
    show player 13
    with dissolve
    deb "A receita está na minha família há gerações!"
    show debbie 14b
    show roxxy 27f at Position (xoffset=33)
    deb "..."
    show debbie 13
    deb "Seu rímel está correndo, querida..."
    show player 5
    show debbie 14b
    show roxxy 33f at Position (xoffset=-34)
    rox "{b}*Chorando*{/b} Oh, desculpe..."
    show roxxy 33bf with dissolve
    pause
    show debbie 13
    deb "Não há nada para se desculpar!"
    show roxxy 32f at Position (xoffset=-34)
    deb "Vocês apenas comem e me avisam se há mais alguma coisa que eu possa fazer por você."
    deb "Eu odeio ver uma coisa bonita como você toda chateada..."
    show debbie 14
    show player 13
    show roxxy 33f at Position (xoffset=-34)
    rox "... Obrigada, senhora."
    show roxxy 32f at Position (xoffset=-34)
    show debbie 2
    deb "Por favor ligue para mim {b}[deb_name]{/b}, querida."
    hide debbie with dissolve
    rox "..."
    show roxxy 33 at center with dissolve
    rox "Obrigada por tudo isso {b}[firstname]{/b}..."
    show roxxy 32
    show player 14
    player_name "A qualquer momento!"
    show player 13
    show roxxy 33b
    rox "{b}*Chorando*{/b}."
    show roxxy 32
    show player 10
    player_name "Vamos comer e depois vamos para  {b}Delegacia de polícia{/b} e resolver as coisas."
    show player 13
    show roxxy 33
    rox "... Sim, ok."
    hide roxxy
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
