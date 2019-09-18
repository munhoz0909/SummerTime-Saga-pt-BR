label home_garage_pick_up_shovel:
    scene expression game.timer.image("backgrounds/location_home_garage{}_blur.jpg")
    show player 244 with dissolve
    player_name "Sim, isso deve funcionar!"
    player_name "Vai ser bom ter algum dinheiro para uma mudança..."
    show player 243
    jen "{b}*Ahem*{/b}"
    player_name "!!!" with hpunch
    show player 243 at left
    show jenny f_upset_talk a_dressed_crossed
    with dissolve
    jen "O que você está fazendo com essa pá?"
    show jenny f_upset
    show player 244
    player_name "... Hã?"
    player_name "Oh! Eu estou levando isso para casa da {b}Diane{/b} ."
    player_name "Eu vou estar trabalhando para ela neste verão."
    show player 243
    show jenny f_upset_talk
    jen "{b}Diane{/b} te deu um emprego?"
    jen "... Ela nunca me ofereceu nenhum trabalho!"
    show jenny f_upset
    show player 14 with dissolve
    player_name "Bem, é trabalho físico em seu jardim."
    player_name "Ela provavelmente apenas assumiu que você não estaria interessado..."
    show player 13
    show jenny f_eyeroll
    jen "Ugh, nesse calor?"
    show jenny f_upset_talk
    jen "Sim, de jeito nenhum. Dane-se isso!"
    show jenny f_upset
    show player 10
    player_name "O que você está fazendo na garagem?"
    player_name "Você nunca vem aqui..."
    show player 5
    show jenny f_normal_talk a_dressed_hips with dissolve
    jen "Eu preciso de algumas baterias. Ainda temos algumas aqui ?"
    show jenny f_normal
    show player 4 with dissolve
    pause
    show player 14 with dissolve
    player_name "Sim, acho que sim."
    player_name "Tente essa caixa na prateleira de baixo."
    show player 13
    pause
    show jenny b_bend f_empty a_empty at flip
    show jenny at Position (xpos=800)
    with dissolve
    show player 428
    player_name "!!!"
    pause
    show jenny b_bend_down with dissolve
    pause
    show player 12
    hide jenny
    show jenny a_dressed_hips_battery f_upset_talk b_dressed at unflip
    with dissolve
    player_name "Caramba, por que você precisa de tantas baterias?"
    show player 5
    jen "Não é da sua conta, perdedor!"
    jen "Apenas pegue sua pá e vá embora."
    show jenny f_upset
    show player 12
    player_name "Tanto faz."
    show player 90
    show jenny f_grin_talk
    jen "Divirta-se rebentando sua bunda para {b}Diane{/b}..."
    show jenny f_laugh
    jen "Hahaha!"
    hide jenny with dissolve
    show player 12
    player_name "... Ela é uma vadia."
    show player 90
    show screen popup("boxes/popup_item_shovel1.png")
    $ player.get_item("shovel")
    hide player with dissolve
    $ game.main()

label car_dialogue:
    if M_mom.is_state(S_mom_mall_outing):
        call expression game.dialog_select("garage_car_mom_mall_outing")
        jump expression game.dialog_select("mall_dialogue")

    scene expression game.timer.image("home_garage{}")
    if M_mom.is_state(S_mom_check_car):
        $ player.go_to(L_home_car)
        call expression game.dialog_select("garage_car_mom_check_car")
        $ player.location.call_screen(False)
    else:

        if seen_garage_locked:
            call expression game.dialog_select("garage_car_seen")
        else:
            call expression game.dialog_select("garage_car_not_seen")
            $ seen_garage_locked = True
    $ game.main()

label garage_car_mom_mall_outing:
    scene expression "backgrounds/location_car_cutscene01.jpg"
    show expression FilteredText("Então nós pulamos no carro e fizemos nosso caminho para o shopping.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    show expression FilteredText("Eu achei que o tempo passou rapidamente quando eu estava com {b}[deb_name]{/b}...") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide cutscene
    show expression FilteredText("... Sua companhia agradável e sorriso contagiante nunca deixou de iluminar meu humor.") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide cutscene
    scene black
    with fade
    return

label garage_car_mom_check_car:
    show player 4 with dissolve
    player_name "( Ela está certa. O carro não quer funcionar. )"
    show player 5
    player_name "( É melhor eu verificar o motor. )"
    if game.timer.is_dark():
        player_name "( Com certeza está escuro aqui. )"
    return

label garage_car_seen:
    show player 34 at left with dissolve
    player_name "Hmm..."
    show player 35
    player_name "Eu não preciso usar o carro {b}[deb_name]{/b} ."
    hide player 35 with dissolve
    return

label garage_car_not_seen:
    show player 2 at left with dissolve
    player_name "{b}[deb_name]{/b}... gostaria de ter um motivo para dirigir o carro..."
    hide player 2 at left with dissolve
    return

label engine_broken:
    call expression game.dialog_select("engine_broken_dialogue")
    $ M_mom.trigger(T_mom_check_engine)
    jump expression game.dialog_select("home_garage")

label engine_broken_dialogue:
    scene expression game.timer.image("home_garage{}")
    show player 23 with dissolve
    player_name "( !!! )"
    show player 22
    player_name "( Que diabos?! Parece que alguém trabalhou com um martelo! )"
    pause
    show player 16
    player_name "( Eu me pergunto se isso tem algo a ver com aqueles caras sombrios nos trajes? )"
    player_name "( Aqueles Scumbags! )"
    show player 11
    player_name "( Não há como consertar isso. Nós temos que pegar um motor novo ou algo assim. )"
    player_name "( Eu deveria dizer a {b}[deb_name]{/b} sobre isso. Ela não será feliz! )"
    return

label lawnmower_dialogue:
    $ player.go_to(L_home_garage)
    if M_mom.is_state(S_mom_fill_mower) and not player.has_item("gas_can"):
        if not game.timer.is_dark():
            call expression game.dialog_select("garage_mom_fill_mower_no_gas")
        else:
            call expression game.dialog_select("garage_mom_fill_mower_night")

    elif M_mom.is_state(S_mom_fill_mower) and player.has_item("gas_can"):
        if not game.timer.is_dark():
            call expression game.dialog_select("garage_mom_fill_mower_success")

            $ player.remove_item("gas_can")
            $ M_mom.trigger(T_mom_filled_mower)
            jump expression game.dialog_select("home_front")
        else:

            call expression game.dialog_select("garage_mom_fill_mower_night")
    else:
        call expression game.dialog_select("garage_lawnmower_not_needed")
    $ game.main()

label garage_mom_fill_mower_night:
    scene expression game.timer.image("home_garage{}")
    show player 35f with dissolve
    player_name "( Por que eu usaria o cortador de grama à noite? Eu deveria voltar durante o dia... )"
    hide player 35 with dissolve
    return

label garage_mom_fill_mower_no_gas:
    scene home_garage_closeup
    show player 428f at right
    player_name "( Eu não uso um cortador de grama há anos ... eu ainda lembro como usar um? )"
    player_name "( Meu {b}pai{/b} puxava esse cabo, E ele começava a funcionar. Deixe-me tentar isso. )"
    scene home_garage_closeup
    show player 197
    with dissolve
    pause
    show player 200 at Position (xpos=566)
    pause
    show player 197 at center
    scene home_garage
    show player 35f
    with dissolve
    player_name "( Deve estar sem gasolina. Mal começou, então pelo menos eu sei o que está errado. )"
    show player 2f
    player_name "( Bem, não vai começar sem gasolina. Eu provavelmente deveria comprar no {b}CONSUM-R{/b}. )"
    return

label garage_mom_fill_mower_success:
    scene home_garage_closeup
    show player 202 at Position (xpos=521) with dissolve
    player_name "( Eu finalmente tenho um pouco de gasolina para o cortador. )"
    show player 201 at Position (xpos=509)
    player_name "( Isso deve ser o suficiente. )"
    show player 196 at Position (xpos=521)
    player_name "Espero que isso funcione. Eu não sei mais o que fazer depois dissos..."
    show player 197 at center
    pause
    show player 200 at Position (xpos=566)
    pause
    show player 197 at center
    pause
    show player 200 at Position (xpos=566)
    pause
    show player 199 at center
    player_name "Hmm... não está funcionando. Vou tentar puxar um pouco mais..."
    show player 200 at Position (xpos=566)
    pause
    show player 198 at center
    player_name "Funcionou!"
    return

label garage_lawnmower_not_needed:
    scene expression game.timer.image("home_garage{}")
    show player 35 with dissolve
    player_name "( Por que eu usaria o cortador de grama? A grama parece bem... )"
    hide player 35 with dissolve
    return

label garage_use_workbench_night:
    scene expression player.location.background_blur
    show player 3 with dissolve
    player_name "( Droga! Eu não consigo ver nada! )"
    show player 4 with dissolve
    player_name "( E a luminária está quebrada! )"
    player_name "( Eu deveria voltar e trabalhar nisso durante o {b}dia{/b}... )"
    hide player with dissolve
    return

label garage_dewitt_drill:
    call expression game.dialog_select("garage_dewitt_drill_dialogue")
    $ player.get_item("drill")
    $ game.main()

label garage_dewitt_drill_dialogue:
    scene expression game.timer.image("home_garage{}")
    show player 14 with dissolve
    player_name "Aqui está uma broca antiga!"
    player_name "As baterias ainda estão carregadas também."
    show player 12
    player_name "Agora eu só preciso procurar {b}um galho de árvore caída{/b}."
    hide player with dissolve
    return

label garage_dewitt_make_new_flute:
    scene home_garage_cs1
    with fade
    show text "Você sabe, foi estranhamente satisfatório, construir essa flauta manualmente.\nEstou realmente muito animado com isso agora!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene expression game.timer.image("home_garage{}")
    show player 566 with dissolve
    player_name "Lá!"
    player_name "Não parece tão ruim assim!"
    show player 567
    pause
    show player 566
    player_name "Vamos ver o que isso faz quando eu coloco meus lábios e sopro..."
    show player 567d with dissolve
    pause
    show player 566 with dissolve
    player_name "Ei, isso parece muito bom!"
    player_name "Eu aposto que {b}Sra. Dewitt{/b} Vai surtar quando ela vê que eu construí uma flauta do zero!"
    hide player with dissolve
    return

label garage_dewitt_find_paint:
    scene expression game.timer.image("home_garage{}")
    show player 32 at Position (xoffset=68) with dissolve
    player_name "Eu não vejo tinta aqui..."
    pause
    show player 10 with dissolve
    player_name "Talvez {b}[deb_name]{/b} sabe."
    hide player with dissolve
    return

label garage_dewitt_make_replacement_guitar:
    scene home_garage_cs2
    with fade
    show text "Você sabe, eu estou realmente começando a cavar todo esse trabalho em madeira.\nTalvez eu deva pensar em me tornar um carpinteiro algum dia." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene expression game.timer.image("home_garage{}")
    show player 575 with dissolve
    player_name "Caramba! Então, novamente, talvez eu não seja tão talentoso quanto eu pensava."
    player_name "Espero que isso seja bom o suficiente para enganar a {b}Sra. Johnson{/b}."
    hide player with dissolve
    return

label garage_build_easels:
    scene location_home_garage_cutscene03
    with fade
    show text "Sim, acho que parece certo." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "eu espero {b}Miss Ross{/b} Gosta disso!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Eu realmente não quero decepcioná-la..." at Position (xpos=512, ypos=700) with dissolve
    pause
    hide text
    with dissolve
    return

label garage_workbench_not_needed:
    scene expression game.timer.image("home_garage{}")
    show player 12 with dissolve
    player_name "( Eu não tenho razão para usar isso agora. )"
    hide player with dissolve
    return

label debbie_car_sex_pre:
    scene car_interior
    show player car 2d
    show player_arms car 1
    show debbie car 4 at right
    show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_mom) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
    show xtra 30 at right
    with dissolve
    return

label debbie_car_sex_pre_first_time:
    pause
    show debbie car 4b
    deb "Você sabe, eu realmente não estava esperando que você me trouxesse para o carro."
    show debbie car 5g
    deb "Eu estava cético no começo, mas agora que estamos sentados aqui..."
    show player car 3
    deb "... É meio que me excitando."
    deb "Imagine se estivéssemos estacionados em público em algum lugar?!"
    deb "Mmm..."
    deb "Estou me molhando só de pensar nisso!"
    show debbie car 5f
    show player car 4g
    player_name "Eu iria para baixo para tentar algo parecido..."
    show player car 5
    player_name "... Você não ficaria envergonhado?"
    show player car 5b
    show debbie car 5c
    show debbie_arms_car 5 at Position(xalign = 0.357, yalign = 0.558)

    deb "..."
    show debbie car 5g
    deb "Hehe, Eu não sei ... Eu provavelmente ficaria mortificado se fôssemos pegos!."
    deb "... Mas..."
    deb "... Isso é o que faz com que seja tão emocionante, sabe?!"
    deb "Bem, pelo menos me excita..."
    deb "Estou me molhando só de pensar nisso!"
    show debbie car 5f
    show player car 4h
    player_name "..."
    show player car 5
    player_name "você está?"
    show player car 5b
    show debbie car 3b
    deb "Hehe, Sim..."
    deb "Então, o que vamos fazer com esse pau grande e duro aqui?"
    show debbie car 3
    show player car 2d
    return

label debbie_car_sex_pre_repeat:
    show debbie car 4b
    show debbie_arms_car 5c at Position(xalign = 0.357, yalign = 0.558)
    deb "Eu gosto de sentir esse cara grande endurecer na minha mão."
    show debbie car 4
    pause
    show player car 4b
    show debbie car 3b
    show debbie_arms_car 5 with dissolve
    deb "Garotos jovens com certeza ficam duros bem facil."
    show debbie car 4
    pause
    show player car 2d
    show debbie car 5b with dissolve
    deb "Parece tão ... Delicioso!"
    show debbie car 3b
    deb "Quer que eu  pegue e coloque na minha boca?"
    show debbie car 3
    return

label debbie_car_sex_jerk_off:
    show player car 2c
    player_name "Apenas continue fazendo o que você está fazendo!"
    show player car 2d
    show debbie car 3b
    deb "Tudo bem querido."
    show debbie car 4
    return

label debbie_car_sex_bj:
    show player car 2c
    player_name "Você usaria sua boca?"
    show player car 2d
    show debbie car 3b
    deb "absolutamente!"
    scene car_interior bj
    show player car 4c
    show player_arms car 1
    show debbie_car_bj 11 at right
    show xtra 30 zorder 2 at right
    with dissolve
    pause
    show debbie_car_bj 12 with dissolve
    pause
    show debbie_car_bj 7
    show player_boner car 3
    with dissolve
    pause
    hide player_boner
    show debbie_car_bj 8 zorder 1 at Position(xalign = 0.93, yalign = 1.0)
    with dissolve
    pause
    show player car 4c
    return

label debbie_car_sex_leave:
    show player car 5
    player_name "Eu acho que estou bem por agora."
    player_name "Isso foi bom."
    show player car 5b
    show debbie car 5g
    deb "Mesmo?"
    deb "Mas você ainda nem gozou?"
    show debbie car 5f
    show player car 2
    player_name "Isso é bom."
    show player car 5b
    show debbie car 5g
    deb "Fiz algo de errado?"
    show debbie car 5f
    show player car 2c
    player_name "Foi bom {b}[deb_name]{/b}! Não se preocupe."
    player_name "Eu tenho que ir, é tudo."
    show player car 5b
    deb "..."
    show debbie car 5g
    deb "Tudo bem..."
    return

label debbie_car_sex:
    $ M_mom.set("sex speed", .175)
    $ animated = False
    call expression game.dialog_select("debbie_car_sex_pre")
    if not M_mom.is_set("car sex"):
        call expression game.dialog_select("debbie_car_sex_pre_first_time")
        $ M_mom.set("car sex", True)
    else:

        call expression game.dialog_select("debbie_car_sex_pre_repeat")
    menu:
        "Me masturbar.":
            $ M_mom.set("car jerk", True)
            call expression game.dialog_select("debbie_car_sex_jerk_off")
            jump expression game.dialog_select("car_mom_sex_loop")
        "Boquete.":

            $ M_mom.set("car jerk", False)
            call expression game.dialog_select("debbie_car_sex_bj")
            jump expression game.dialog_select("car_mom_sex_loop")

        "Sair." if store._in_replay == None:
            call expression game.dialog_select("debbie_car_sex_leave")
    scene black with fade
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["05_unlocked"] = True
    $ player.go_to(L_home_garage)
    $ game.timer.tick()
    $ game.main()

label car_mom_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_mom.is_set("car jerk"):
                    show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_mom) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
                else:
                    show expression AnimatedImage("debbie_car_bj", [8,"8b","8c","8d","8e","8f","8g"], M_mom) as debbie_car_bj zorder 1 at Position(xalign = 0.93, yalign = 1.0)
                $ animated = True
            pause 4
            if animcounter in [1,3]:
                call expression game.dialog_select("car_mom_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            if M_mom.is_set("car jerk"):
                $ pose_list = [5,"5b","5c","5b"]
            else:
                $ pose_list = [8,"8b","8c","8d","8e","8f","8g"]
            $ poses_done = []
            while poses_done != pose_list:
                if M_mom.is_set("car jerk"):
                    show expression "debbie_arms_car {}".format(pose_list[pose_counter]) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
                else:
                    show expression "debbie_car_bj {}".format(pose_list[pose_counter]) as debbie_car_bj zorder 1 at Position(xalign = 0.93, yalign = 1.0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("car_mom_hscene_dialog")
        $ animcounter += 1
    call screen car_mom_sex_options

label car_mom_hscene_dialog:
    if M_mom.is_set("car jerk"):
        if animcounter == 3:
            if randomizer() <= 50:
                show debbie car 4b
                show player car 5b
                deb "Eu não posso acreditar que seu pau é tão grande!{p=2}{nw}"
                deb "Eu amo como é macio.{p=2}{nw}"
                show debbie car 4
            else:

                show debbie car 5b
                show player car 5b
                deb "Eu adoro seu pau grande!?{p=2}{nw}"
                deb "Goza para mim, {b}[firstname]{/b}!{p=2}{nw}"
                show player car 4b
                pause 1
                show debbie car 4
                show player car 4c
                player_name "Ok...{p=2}{nw}"
                show player car 4h
    else:
        if animcounter == 1:
            deb "Mmmm...{p=1}{nw}"

        elif animcounter == 3:
            player_name "Oh...{p=1}{nw}"
            show player car 4d
            player_name "Assim, {b}[deb_name]{/b}.{p=2}{nw}"
            show player car 4c
    return

label car_mom_faster_dialogue:
    show player car 4c
    player_name "Mais rápido, {b}[deb_name]{/b}."
    show player car 4h
    jump expression game.dialog_select("car_mom_sex_loop")

label car_mom_slower_dialogue:
    show player car 4c
    player_name "Vá devagar..."
    show player car 4h
    jump expression game.dialog_select("car_mom_sex_loop")

label car_mom_sex_cum:
    if M_mom.is_set("car jerk"):
        call expression game.dialog_select("car_mom_jerk_cum")
    else:
        call expression game.dialog_select("car_mom_bj_cum")
    scene black with fade
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["05_unlocked"] = True
    $ player.go_to(L_home_garage)
    $ game.timer.tick()
    $ game.main()

label car_mom_jerk_cum:
    show player car 4c
    pause
    show player car 4d
    show player_arms car 2
    show debbie_arms_car 5d at Position(xalign = 0.357, yalign = 0.558)
    with dissolve
    player_name "( !!! )"
    show debbie car 4b
    deb "Uau!!!"
    show debbie car 5b
    deb "Docinho!"
    show player car 2b
    show player_arms car 1 with dissolve
    deb "Eu sempre esqueço a quantidade do seu esperma!"
    show debbie car 4b
    deb "Pelo menos não sujamos o carro..."
    show debbie car 3
    show player car 2c
    player_name "Isso foi ótimo..."
    scene car_interior kiss
    show debbie car 6 at right
    show player_boner car 1b
    show xtra 30 at right
    with dissolve
    pause
    scene car_interior
    show player car 2c
    show player_arms car 1
    show player_boner car 1b
    show debbie car 3 at right
    show debbie_arms_car 1
    show xtra 30 at right
    with dissolve
    player_name "Obrigado, {b}[deb_name]{/b}."
    show player car 2d
    show debbie car 3b
    deb "Você é bem-vindo, querido."
    show debbie car 4b
    deb "Vamos voltar para dentro antes que {b}[jen_name]{/b} começa a se perguntar para onde nós fugimos."
    show debbie car 3b
    deb "Eu não quero que ela descubra o que estamos fazendo aqui!"
    return

label car_mom_bj_cum:
    show player_arms car 2
    show player car 4d
    player_name "{b}[deb_name]{/b}, eu não vou durar muito tempo..."
    player_name "( !!! )"
    show debbie_car_bj 9
    show player_arms car 2
    with flash
    deb "Mmmmph!!"
    scene car_interior
    show player car 4d
    show player_arms car 1
    show player_boner car 2
    show debbie_car_bj 10 at right
    show xtra 30 at right
    with dissolve
    pause
    show player car 2d
    deb "{b}*Engolir*{/b}"
    deb "... {b}*Engolir*{/b}"
    show debbie car 2 at right
    hide debbie_arms_car
    hide debbie_car_bj
    show debbie_arms_car 1
    hide xtra
    show xtra 30 at right
    with dissolve
    pause
    show debbie car 3b
    deb "Uau! Isso foi muito!"
    deb "Ufa ... acho que não vou ter muito apetite no jantar hoje a noite."
    show debbie car 3
    show player car 2c
    player_name "Você engoliu tudo, Isso foi demais! Você é tão boa nisso!"
    show player car 2d
    show debbie car 3b
    deb "Hehe, bem, estou feliz que você goste {b}[firstname]{/b}. Porque eu amo chupar seu pau!"
    show debbie car 3b
    deb "Vamos voltar para dentro antes que {b}[jen_name]{/b} começa a se perguntar para onde nós fugimos."
    show debbie car 3
    show player car 5
    player_name "Tudo bem."
    player_name "Apenas deixe-me me limpar primeiro..."
    show player car 3
    show debbie car 3b
    deb "Eu vou te ver lá, querido!"
    show player car 5b
    show debbie car 4b
    deb "Não demore muito..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
