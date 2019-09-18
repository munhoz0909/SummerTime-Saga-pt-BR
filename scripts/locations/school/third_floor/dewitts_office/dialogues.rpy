label dewitts_office_first_visit:
    scene school_office2_b with fade
    show player 14 with dissolve
    player_name "Uau... {b}Miss Dewitt's{/b} escritório tem uma configuração doce!"
    player_name "Parece que ela traz estudantes para gravações privadas..."
    player_name "...E ela tem um sofá!!"
    hide player with dissolve
    return

label dewitts_office_dewitt_office_reward:
    scene expression game.timer.image("dewitt_office_c{}"):
    show player 55f at right
    show tyrone 6f at Position (xpos=500)
    show eve 5f at Position (xpos=400)
    show dewitt 28 at left
    with dissolve
    player_name "*Tosse*"
    show player 10f with dissolve
    player_name "Eita, o que está acontecendo aqui?!"
    show player 11f
    show eve 6f
    eve "Caixa quente!"
    show eve 5f
    show tyrone 7f
    tyrone "Feche a porta, honky! Você está deixando toda a fumaça sair!"
    show tyrone 8f at Position (xoffset=16) with dissolve
    show dewitt 30
    dewitt "Ei, seja legal em {b}[firstname]{/b}! Ele é meu pequeno docinho!"
    show dewitt 28
    show tyrone 7f with dissolve
    tyrone "Pfft, hahaha!"
    show tyrone 6f
    show player 10f
    player_name "{b}Miss Dewitt{/b}?"
    player_name "O que aconteceu com suas roupas?!"
    show player 11f
    pause
    show dewitt 29
    dewitt "Hmm?"
    dewitt "Oh! Sim, eu não sei. Elas estão em algum lugar por aqui."
    show dewitt 28
    show tyrone 8f at Position (xoffset=16) with dissolve
    show player 212f
    player_name "..."
    show dewitt 30
    dewitt "Venha dançar comigo!"
    show dewitt 28
    show tyrone 6f with dissolve
    show player 29f with dissolve
    player_name "Hehe, Eu não sou muito dançarino."
    show player 3f at Position (xoffset=-8)
    show dewitt 29
    dewitt "Bem, está tudo bem, querido."
    show dewitt 30
    dewitt "Apenas sente-se e eu dançarei para você!"
    show dewitt 28
    show player 29f
    player_name "Ok..."
    hide player
    hide dewitt
    hide eve
    hide tyrone
    with dissolve

    $ M_dewitt.set("sex speed", 0.125)
    scene expression game.timer.image("dewitt_office_twerk{}")
    show dewitts 1
    show dewitt cloths 1c
    show player dewitts 1 zorder 2 at left
    dewitt "Veja isso!"
    hide dewitts
    hide dewitt
    show expression AnimatedImage("dewitt_twerk", ["1c","2c","3c","4c","5c","6c","7c","8c","9c","10c"], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    with dissolve

    tyrone "Dayum! Você realmente sabe como agitar essa coisa, {b}Miss Dewitt{/b}."
    eve "Não brinca! Você acha que pode me ensinar a fazer isso?"
    tyrone "Oh por favor, você precisa ter um pouco de lixo no seu porta-malas para fazer esses movimentos!"
    eve "Ei, pau! Não fique falando merda ou eu vou gritar na sua bunda!"
    tyrone "Você tem que me pegar primeiro, pão maravilhoso!"
    eve "... Filho da puta!"
    scene expression game.timer.image("dewitt_office_sex{}")
    show expression AnimatedImage("dewitt_twerk", ["1c","2c","3c","4c","5c","6c","7c","8c","9c","10c"], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    show player dewitts 1 zorder 2 at left
    with fastdissolve
    pause
    hide dewitt_twerk
    show dewitts 1
    show dewitt cloths 1c zorder 1
    with dissolve
    dewitt "Graças a Deus eles se foram."
    dewitt "Então, que tal, {b}[firstname]{/b}? Você gosta da minha dança?"
    show dewitts 2
    player_name "Sim!"
    player_name "Você tem uma bunda muito sexy!"
    show dewitts 1
    dewitt "Hehe, bom que você gostou."
    dewitt "Está tudo bem, querido. Você pode tocar se quiser."
    show dewitts 2
    player_name "Mesmo?"
    hide player
    show dewitts 3b at left
    with dissolve
    pause
    show dewitts 4b
    dewitt "Mmmhmm."
    show dewitts 3b
    pause
    show dewitts 4b
    pause
    show player dewitts 1 zorder 2 at left
    hide dewitts
    show dewitts 1
    with dissolve
    dewitt "Você gosta daquele saque suculento?"
    show dewitts 2
    player_name "..."
    show player dewitts 1b with hpunch
    show dewitts 2b
    dewitt "Eep!{p=1}{nw}"
    show player dewitts 1 with dissolve
    show dewitts 1
    dewitt "Oh Meu Deus, seu menino travesso!"
    show dewitts 2
    show player dewitts 1b with hpunch
    pause 1
    show player dewitts 1 with dissolve
    show dewitts 1
    dewitt "Mmm."
    hide player
    show dewitts 3b at left
    with dissolve
    pause
    show dewitts 4b
    dewitt "..."
    show dewitts 3b
    pause
    show dewitts 4b
    pause
    show player dewitts 1 zorder 2 at left
    hide dewitts
    show dewitts 1
    with dissolve
    dewitt "Tudo bem, é melhor pararmos. Você está me deixando toda molhada!"
    show dewitts 2
    player_name "Oh, sim. OK."
    player_name "Suponho que esteja ficando tarde."
    show dewitts 1
    dewitt "O tempo voa quando você está se divertindo!"
    dewitt "Mais uma vez obrigada por hoje, {b}[firstname]{/b}. Foi realmente uma surpresa incrível!"
    show dewitts 2
    player_name "O prazer é meu, {b}Miss Dewitt{/b}."
    player_name "Ate amanha."
    show dewitts 1
    dewitt "Boa noite amor."
    hide dewitts
    hide dewitt cloths
    hide player
    with dissolve
    return

label dewitt_office_dewitt_night_visit:
    scene expression game.timer.image("dewitt_office_c{}")
    show dewitt 18 at left
    show player 14f at right
    with dissolve
    player_name "Ei {b}Miss Dewitt{/b}."
    player_name "O que está rolando?"
    show player 13f
    show dewitt 19
    dewitt "Me diga sobre a {b}Melodia{/b}, Docinho."
    dewitt "Eu estava apenas ouvindo essa nova faixa aqui."
    dewitt "O que você acha disso?"
    show dewitt 18
    show player 17f
    player_name "Hmm, é legal! Eu gosto da batida!"
    show player 14f
    player_name "Quem é esse?"
    show player 13f
    show dewitt 19
    dewitt "Hehe, é um dos meus!"
    show dewitt 18
    show player 14f
    player_name "Mesmo?!"
    player_name "I didn't know you made your own music!"
    show player 13f
    show dewitt 19
    dewitt "Bem, eu tento..."
    dewitt "Eu fiz essa para alguém especial."
    show dewitt 18
    show player 14f
    player_name "Oh sim?"
    player_name "Alguém que eu conheço?"
    show player 13f
    show dewitt 19
    dewitt "Mmm, Sim. Eu acho que você deve ter ouvido falar dele..."
    dewitt "Ele realmente me ajudou a sair do congestionamento recentemente."
    show dewitt 18
    show player 14f
    player_name "Soa como um cara legal..."
    show player 13f
    show dewitt 19
    dewitt "Hehe, oh docinho. Ele é um cara muito legal."
    dewitt "... E ele precisa sentar aqui..."
    show dewitt 18
    show player 10f
    player_name "O que está acontecendo, {b}Melody{/b}?"
    show player 5f
    show dewitt 19
    dewitt "Bem, você fez um show tão bom para mim..."
    dewitt "É justo eu devolver o favor."
    show dewitt 20 with dissolve
    show player 26f
    pause
    show dewitt 31f with dissolve
    pause
    show dewitt 32f with dissolve
    pause
    show dewitt 18b with dissolve
    pause
    show player 435f
    player_name "... Uau puta merda!"
    player_name "Você está bonita, {b}Miss Dewitt{/b}!"
    show dewitt 19b
    dewitt "Hehe, Eu tenho curvas nos lugares certos, querido!"
    dewitt "... Mas eu sei o que você quer."

    $ M_dewitt.set("sex speed", 0.125)
    scene expression game.timer.image("dewitt_office_sex{}"):
    show dewitts 1
    show player dewitts 1 zorder 2 at left
    with dissolve
    dewitt "O que você acha dessa bunda, {b}[firstname]{/b}?"
    player_name "{b}*Gole*{/b}"
    player_name "Eu..."
    player_name "É incrível!"
    player_name "Eu amo o jeito que ela balança!"
    dewitt "Mmm, então você vai adorar isso, docinho!"
    hide dewitts
    show expression AnimatedImage("dewitt_twerk", ["1b","2b","3b","4b","5b","6b","7b","8b","9b","10b"], M_dewitt) as dewitt_twerk at top
    with dissolve
    player_name "!!!"
    pause
    player_name "Isso é tão sexy, {b}Miss Dewitt{/b}!"
    dewitt "{b}Melodia{/b}, {b}[firstname]{/b}..."
    player_name "Desculpa. Isso é tão sexy, {b}Melody{/b}!"
    dewitt "Hehe, bem, eu estou feliz que você gostou..."
    dewitt "Por que você não tira esse seu pau grande?"
    player_name "Mesmo?"
    dewitt "Mmmhmm..."
    scene black with fade
    pause 0.25
    scene expression game.timer.image("dewitt_office_sex{}"):
    show dewitts 1
    show player dewitts 2 zorder 2 at left
    with dissolve
    dewitt "Merda, isso é legal!"
    dewitt "Gostaria de saber se é tão bom quanto o gosto?"
    show dewitts 2
    player_name "Você quer dizer que eu posso-"
    player_name "... Você quer que eu..."
    hide player
    show dewitts 3 at left
    with dissolve
    dewitt "Mmm, Eu quero que você me dê isso, {b}[firstname]{/b}!"
    show dewitts 4
    dewitt "Bem Aqui, docinho..."
    show dewitts 5 with dissolve
    pause
    show expression AnimatedImage("dewitts", [5,6,7,8,9,10,11,12,13,14], M_dewitt) as dewitts
    jump expression game.dialog_select("dewitt_sex_loop")

label dewitt_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("dewitts", [5,6,7,8,9,10,11,12,13,14], M_dewitt) as dewitts
                $ animated = True
            pause 1
            call expression game.dialog_select("dewitt_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [5,6,7,8,9,10,11,12,13,14]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "dewitts {}".format(pose_list[pose_counter]) as dewitts
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("dewitt_hscene_dialog")
        $ animcounter += 1
    call screen dewitt_sex_options

label dewitt_bj_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("dewitts_bj", [1,2,3,4,5,6,7,8,9,10,11,12], M_dewitt) as dewitts_bj
                $ animated = True
            pause 1
            call expression game.dialog_select("dewitt_bj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10,11,12]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "dewitts_bj {}".format(pose_list[pose_counter]) as dewitts_bj
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("dewitt_bj_hscene_dialog")
        $ animcounter += 1
    call screen dewitt_office_bj_options

label dewitt_twerk_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("dewitt_twerk", ["1b","2b","3b","4b","5b","6b","7b","8b","9b","10b"], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
                $ animated = True
            pause 1
            call expression game.dialog_select("dewitt_twerk_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = ["1b","2b","3b","4b","5b","6b","7b","8b","9b","10b"]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "dewitt_twerk {}".format(pose_list[pose_counter]) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("dewitt_twerk_hscene_dialog")
        $ animcounter += 1
    call screen dewitt_twerk_options

label dewitt_hscene_dialog:
    if animcounter == 0:
        if randomizer() <= 50:
            dewitt "Oh, foda sim!{p=2}{nw}"
            dewitt "Isso grande garoto!{p=2}{nw}"
            dewitt "Mmm...{p=1}{nw}"

        elif not M_dewitt.is_state(S_dewitt_office_night_visit):
            dewitt "Oh sim amor!{p=2}{nw}"
            dewitt "Isso é exatamente o que eu precisava!{p=2}{nw}"
        else:

            player_name "Oh, Uau!{p=1}{nw}"
            player_name "{b}Melody{/b}! Isso é incrível!{p=2}{nw}"
            dewitt "Mmmhmm...{p=1}{nw}"

    elif animcounter == 2:
        if randomizer() <= 50:
            dewitt "Come essa buceta, Docinho!{p=2}{nw}"
            dewitt "Me dê isto, {b}[firstname]{/b}!{p=2}{nw}"
            dewitt "Ahhh!{p=1}{nw}"

        elif not M_dewitt.is_state(S_dewitt_office_night_visit):
            dewitt "Porra, esse pau é tão bom!{p=2}{nw}"
            player_name "Eu amo assistir você cavalgando {b}Miss Dewitt{/b}...{p=3}{nw}"
            dewitt "Heh, Mmm...{p=1}{nw}"

    elif animcounter == 3:
        if randomizer() <= 50:
            dewitt "Foode, mais fundo!!{p=2}{nw}"
            dewitt "É isso aí, baby! Eu vou gozar por todo esse pau grande!{p=3}{nw}"
            dewitt "Mmmm!!{p=1}{nw}"

        elif not M_dewitt.is_state(S_dewitt_office_night_visit):
            dewitt "Ahhh!{p=1}{nw}"
            dewitt "Me dê mais rapido, baby!{p=2}{nw}"
            dewitt "Fuuuuuu!!!{p=1}{nw}"
    return

label dewitt_bj_hscene_dialog:
    if animcounter == 1:
        if randomizer() <= 50:
            player_name "Ohh...{p=1}{nw}"
        else:

            player_name "Uhh!{p=1}{nw}"

    elif animcounter == 3 and randomizer() <= 50:
        dewitt "Mmmmm!{p=1}{nw}"
    return

label dewitt_twerk_hscene_dialog:
    if animcounter == 0:
        if randomizer() <= 50:
            player_name "Ohh...{p=1}{nw}"
        else:
            player_name "Uhh!{p=1}{nw}"

    elif animcounter == 2 and randomizer() <= 50:
        dewitt "Mmm!!!{p=1}{nw}"

    elif animcounter == 3 and randomizer() <= 50:
        show player dewitts 1b with hpunch
        show player dewitts 1 with dissolve
        dewitt "Nnnggh!{p=1}{nw}"
        dewitt "Você vai me fazer implorar por isso, {b}[firstname]{/b}?{p=2}{nw}"
    return

label dewitt_sex_cum_first:
    player_name "{b}Melody{/b}, Eu vou..."
    player_name "Eu não vou durar muito tempo!!"
    dewitt "Faça isso, baby!"
    dewitt "estou pronta!"
    $ M_dewitt.set("sex speed", 0.4)
    show dewitts 15_16 at left with flash
    player_name "HNNGGG!!!"
    dewitt "AH, FUCK YEEEEAAAHHH!!"
    player_name "{b}Miss Dewitt{/b}!!"
    dewitt "NNGGHH!!!"
    player_name "Haaah... Haaah..."
    show dewitts 17 with dissolve
    dewitt "{b}*Ufa*{/b}."
    show dewitts 18 with dissolve
    dewitt "Porra, isso foi bom!"
    dewitt "Você e muito especial , Docinho!"
    player_name "Sim! Você também, {b}Melody{/b}..."
    hide dewitts with dissolve

    scene expression game.timer.image("dewitt_office_c{}")
    show player 13f at right
    show dewitt 19b at left
    with dissolve
    dewitt "Você tem que voltar e fazer isso de novo!"
    show dewitt 18b
    show player 14f
    player_name "Sério?!"
    show player 13f
    show dewitt 19b
    dewitt "absolutamente!"
    dewitt "Eu não vou deixar você fugir!"
    dewitt "Eu quero esse pau no regular!"
    show dewitt 18b
    show player 17f
    player_name "Hehe, Estou apaixonado por isso."
    show player 13f
    show dewitt 19b
    dewitt "Bom! Você vem me ver a qualquer momento, docinho!"
    dewitt "Minhas portas estrão abertas para você."
    show dewitt 18b
    show player 14f
    player_name "Obrigado, {b}Melody{/b}."
    show player 434f
    pause
    hide player
    hide dewitt
    with dissolve
    $ renpy.end_replay()
    return

label dewitt_sex_cum_repeat:
    player_name "OH! Aqui vem!"
    dewitt "Me preencha, docinho!"
    dewitt "Mmm!"
    dewitt "Eu vou gozar por todas essas bolas!"
    $ M_dewitt.set("sex speed", 0.4)
    show dewitts 15_16 at left with flash
    player_name "HNNGGG!!!"
    dewitt "NNGGHH!!!"
    dewitt "Fuck!!"
    player_name "Haaah... Haaah..."
    show dewitts 17 with dissolve
    dewitt "{b}*Ufa*{/b}."
    show dewitts 18 with dissolve
    dewitt "Mmm..."
    dewitt "Bom garoto."
    hide dewitts with dissolve

    scene expression game.timer.image("dewitt_office_c{}")
    show player 13f at right
    show dewitt 19b at left
    with dissolve
    dewitt "Obrigado pelo bom tempo, docinho."
    dewitt "Vejo você em breve?"
    show dewitt 18b
    show player 14f
    player_name "Claro!"
    show player 434f
    pause
    show dewitt 19b
    dewitt "Hehe, Bons sonhos, bebê!"
    show dewitt 18b
    show player 14f
    player_name "Boa noite, {b}Melody{/b}!"
    hide player
    hide dewitt
    with dissolve
    $ renpy.end_replay()
    return

label dewitt_sex_cum:
    if M_dewitt.is_state(S_dewitt_office_night_visit):
        call expression game.dialog_select("dewitt_sex_cum_first")
        $ persistent.cookie_jar["Dewitt"]["gallery"]["03_unlocked"] = True
        $ M_dewitt.trigger(T_dewitt_sex_it_up)
        $ M_dewitt.set_default_locations([[L_school_musicclassroom, L_school_dewittoffice, L_school_dewittoffice, L_NULL],
                                          [L_NULL, L_NULL, L_NULL, L_NULL]])
    else:

        call expression game.dialog_select("dewitt_sex_cum_repeat")
    $ player.go_to(L_school_floor3)
    $ game.timer.tick()
    $ game.main()

label dewitt_bj_cum:
    hide dewitts_bj
    show dewitt bj 5 at left
    with flash
    player_name "OHHH!!!"
    show dewitt bj 6
    player_name "{b}Miss Dewitt{/b}!"
    show dewitt bj 7
    dewitt "Mmmmm..."
    scene black with fade

    scene expression game.timer.image("dewitt_office_c{}")
    show player 13f at right
    show dewitt 19 at left
    with dissolve
    dewitt "Eu estava esperando ouvir outro discurso empolgante!"
    dewitt "Ou meu bis foi tão bom que deixou você sem palavras?"
    show dewitt 18
    show player 14f
    player_name "Hehe. Você é maravilhosa."
    show player 13f
    show dewitt 19
    dewitt "Volte mais! Vou tocar essa flauta a qualquer dia!"
    hide player
    hide dewitt
    with dissolve
    $ player.go_to(L_school_floor3)
    $ game.timer.tick()
    $ game.main()

label dewitts_office_night_lock:
    scene expression game.timer.image("school_hall_third_floor{}_b"):
    show player 55 at Position (xoffset=12) with dissolve
    pause
    show player 56 with dissolve
    player_name "Eu deveria ir para casa e descansar um pouco."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
