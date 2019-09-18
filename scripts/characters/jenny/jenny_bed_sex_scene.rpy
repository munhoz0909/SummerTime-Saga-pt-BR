label jenny_bed_night_button:
    $ player.go_to(L_home_sisbedroom)
    if not M_jenny.finished_state(S_jenny_give_cunni):
        call expression game.dialog_select("jenny_bed_night_pre_j17")
        $ player.go_to(L_home_hallway)
        $ game.main()
    elif M_jenny.between_states(S_jenny_give_cunni, S_jenny_night_time_sex):
        call expression game.dialog_select("jenny_bed_night_j17_j20")
        $ player.go_to(L_home_hallway)
        $ game.main()
    else:
        call expression game.dialog_select("jenny_bed_night_sex_intro")
    $ game.main()

label jenny_bed_night_pre_j17:
    scene expression player.location.background_closeup with None
    show player f_surprised_teeth with dissolve
    player_name "( Não tem como eu estar incomodando ela! )"
    player_name "( Ela vai me matar! )"
    hide player with dissolve
    return

label jenny_bed_night_j17_j20:
    scene expression player.location.background_closeup with None
    show player f_thinking a_dressed_thinking with dissolve
    player_name "( Você sabe, nós temos nos dado bem melhor recentemente... )"
    player_name "( Talvez ela não se importe? )"
    show player f_grin
    menu:
        "Faça.":
            call expression game.dialog_select("jenny_bed_night_do_it_j17")
        "É melhor eu não fazer isso":
            call expression game.dialog_select("jenny_bed_night_better_not")
    return

label jenny_bed_night_do_it_j17:
    scene expression "backgrounds/location_home_jennybedroom_bed.jpg"
    show jenny b_sleep_side o_sleep_blanket a_sleep_side f_sleep_side_rolleye
    show player b_sleep_climb a_empty f_empty at Position (align=(0,0)) with dissolve
    pause
    show player b_sleep_side f_sleep_side_shy o_sleep_side_boxers
    show expression "characters/player/layeredimage/player_arms_a_sleep_side_normal.png"
    show jenny o_empty
    show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png"
    with dissolve
    pause
    show player b_sleep_cuddle f_sleep_cuddle_side_shy o_empty
    hide expression "characters/player/layeredimage/player_arms_a_sleep_side_normal.png"
    with dissolve
    pause
    show jenny f_sleep_side_wake
    jen "Hmm?"
    show jenny b_sleep_turn a_sleep_turn f_sleep_turn_angry_talk o_sleep_panties with dissolve
    jen "O que"
    show jenny f_sleep_turn_angry
    show player f_sleep_cuddle_side_shy_talk
    player_name "Oi."
    show player f_sleep_cuddle_side_shy
    pause
    show jenny f_sleep_turn_angry_talk a_sleep_turn_push
    show player b_sleep_side o_sleep_side_boxers a_sleep_side_react f_sleep_side_shock
    jen "O QUE PORRA E ESSA!" with hpunch
    scene expression player.location.background_blur
    show player f_surprised_teeth b_underwear a_naked_sides
    show jenny f_angry_talk a_dressed_crossed
    with fade
    jen "Sério, o que diabos está errado com você?!"
    show jenny f_angry
    show player f_sad_talk
    player_name "Me desculpe eu"
    show player f_sad
    show jenny f_angry_talk
    jen "Você não pode esgueira-se na cama de uma mulher enquanto dorme, {b}[firstname]{/b}!"
    jen "Isso é tão assustador!"
    show jenny f_angry
    show player f_sad_talk
    player_name "Eu apenas pensei que talvez"
    show player f_sad_talk_down
    show jenny f_angry_talk
    jen "Não, você obviamente não achou!"
    jen "Ei, apenas saia daqui!"
    show jenny f_angry
    show player f_sad
    player_name "..."
    hide player with dissolve
    show jenny f_eyeroll
    jen "Maldito perdedor..."
    scene black with fade
    pause
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with None
    show player f_sad_talk_down with dissolve
    player_name "( Bem, isso foi horrível... )"
    player_name "( Eu pensei que fosse uma boa ideia? )"
    player_name "( {b}*Suspiro*{/b} Espero que ela não conte {b}[deb_name]{/b} sobre isso... )"
    hide player with dissolve
    return

label jenny_bed_night_better_not:
    show player f_worried a_dressed_pocket with dissolve
    player_name "( É, não... )"
    player_name "( Não vale a pena irritá-la. )"
    hide player with dissolve
    return

label jenny_bed_night_sex_intro:
    if store._in_replay is not None:
        $ player.location = L_home_sisbedroom
        $ game.timer.tick(3)
    scene expression player.location.background_closeup with None
    show player f_thinking a_dressed_thinking with dissolve
    player_name "( Certamente ela não vai ficar com raiva de mim agora, certo? )"
    player_name "( Quero dizer, ela está subindo na minha cama no meio da noite ... Por que eu não posso fazer o mesmo? )"
    show player f_grin
    menu:
        "Faça.":
            call expression game.dialog_select("jenny_bed_night_sex_do_it")
        "É melhor eu não fazer isso" if store._in_replay is None:
            call expression game.dialog_select("jenny_bed_night_better_not")
    return

label jenny_bed_night_sex_do_it:
    if store._in_replay is not None or M_jenny.get("bed_sex_first_time"):
        $ M_jenny.set("bed_sex_first_time", False)
        scene expression "backgrounds/location_home_jennybedroom_bed.jpg"
        show jenny b_sleep_side o_sleep_blanket a_sleep_side f_sleep_side_sleeping
        show player b_sleep_climb a_empty f_empty at Position (align=(0,0)) with dissolve
        pause
        show player b_sleep_side f_sleep_side_shy o_sleep_side_boxers
        show expression "characters/player/layeredimage/player_arms_a_sleep_side_normal.png"
        show jenny o_empty
        show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png" zorder 3
        with dissolve
        pause
        show player b_sleep_cuddle f_sleep_cuddle_side_shy o_empty a_empty
        hide expression "characters/player/layeredimage/player_arms_a_sleep_side_normal.png"
        with dissolve
        pause
        show jenny f_sleep_side_wake
        jen "Hmm?"
        show jenny b_sleep_turn a_sleep_turn f_sleep_turn_angry_talk o_sleep_panties with dissolve
        jen "{b}[firstname]{/b}?"
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "Oi."
        show player f_sleep_cuddle_side_shy
        pause
        show jenny f_sleep_turn_angry_talk
        jen "Que porra você está fazendo?"
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "Uhh indo para a cama?"
        show player f_sleep_cuddle_side_shy
        show jenny f_sleep_turn_angry_talk
        jen "Vá sua cama, perdedor!"
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "Aww, vamos {b}[jen_name]{/b}... Você sobe na minha cama o tempo todo!"
        show player f_sleep_cuddle_side_shy
        show jenny f_sleep_turn_angry_talk
        jen "Sim, porque eu quero foder ... Não se aconchegar e babar em cima de você enquanto você está tentando dormir."
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "Eu não babo..."
        show player f_sleep_cuddle_side_shy
        show jenny b_sleep_side a_sleep_side f_sleep_side_tired_talk with dissolve
        jen "Sim, certo."
        show jenny f_sleep_side_sleeping
        pause
        show jenny b_sleep_turn a_sleep_turn f_sleep_turn_normal with dissolve
        jen "..."
        show jenny f_sleep_turn_normal_talk
        jen "Tudo bem, apenas se apresse!"
        show jenny f_sleep_turn_normal
        player_name "Hmm?"
        show player f_sleep_cuddle_side_shy
        show jenny f_sleep_turn_normal_talk
        jen "estou cansada, {b}[firstname]{/b}!"
        jen "Então, se você vai me foder então se apresse e faça isso já ... Caso contrário, dê o fora!"
        show jenny b_sleep_side a_sleep_side f_sleep_side_sleeping with dissolve
        show player f_sleep_cuddle_side_shock
        menu:
            "Esqueça." if store._in_replay is None:
                show player b_sleep_leave a_empty f_empty
                show jenny b_sleep_turn a_sleep_turn f_sleep_turn_normal o_sleep_blanket
                hide expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png"
                with dissolve
                player_name "Tudo bem, apenas esqueça..."
                hide player with dissolve
                show jenny f_sleep_turn_normal_talk
                jen "Com prazer."
                $ player.go_to(L_home_hallway)
                $ game.main()
            "Ok.":

                show player f_sleep_cuddle_side_shy_talk
                player_name "Ok."
                show player f_sleep_cuddle_side_shy
                pause
                show player f_sleep_cuddle_side_shy_talk
                player_name "Umm..."

                label jenny_bed_night_grope_in_bed:
                    show player f_sleep_cuddle_side_kiss b_empty
                    show jenny b_sleep_side_grope
                    with dissolve
                    pause
                    jen "Mmm."
                    show player b_sleep_side f_sleep_side_shy o_sleep_side_boxers_boner
                    show expression "characters/player/layeredimage/player_arms_a_sleep_side_normal.png"
                    show jenny b_sleep_turn a_sleep_turn_remove_top1 f_sleep_turn_normal
                    with dissolve
                    pause
                    show jenny b_sleep_turn_shirtup a_sleep_turn_remove_top2
                    with dissolve
                    player_name "..."
                    show jenny b_sleep_side_shirtup a_sleep_side f_sleep_side_normal with dissolve
                    pause
                    show player f_sleep_cuddle_side_kiss b_empty o_empty a_empty
                    hide expression "characters/player/layeredimage/player_arms_a_sleep_side_normal.png"
                    show jenny b_sleep_side_grope_shirtup f_sleep_side_enjoy
                    with dissolve
                    pause
                    jen "Ok, isso é muito bom..."
                    show jenny b_sleep_side_grope_hump_shirtup
                    show jenny f_sleep_side_rolleye
                    jen "Ngghhh!"
                    pause
                    show player f_sleep_cuddle_side_shy_talk
                    player_name "Você está feliz que eu te acordei?"
                    show player f_sleep_cuddle_side_shy
                    show jenny f_sleep_side_tired_talk
                    jen "Cale-se..."
                    show player f_sleep_cuddle_side_kiss
                    show jenny f_sleep_side_enjoy
                    pause
                    menu jenny_bed_night_whatcha_do:
                        "Ir Fundo.":
                            jump jenny_bed_night_go_further
                        "Continue.":
                            pause
                            jump jenny_bed_night_whatcha_do
    else:

        scene expression "backgrounds/location_home_jennybedroom_bed.jpg"
        show jenny b_sleep_side o_sleep_blanket a_sleep_side f_sleep_side_sleeping
        show player b_sleep_climb a_empty f_empty at Position (align=(0,0)) with dissolve
        pause
        show player b_sleep_cuddle f_sleep_cuddle_side_shy
        show jenny o_empty
        show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png" zorder 3
        with dissolve
        show jenny f_sleep_side_wake
        jen "Hmm?"
        show jenny b_sleep_turn a_sleep_turn f_sleep_turn_angry_talk o_sleep_panties with dissolve
        jen "{b}[firstname]{/b}?"
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "Oi."
        show player f_sleep_cuddle_side_shy
        pause
        show jenny f_sleep_turn_angry_talk
        jen "Essa merda de novo?"
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "Eu pensei que você gostou?"
        show player f_sleep_cuddle_side_shy
        show jenny f_sleep_turn_angry_talk
        jen "Que porra te deu essa ideia?"
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "Então você não gostou?"
        show player f_sleep_cuddle_side_shy
        show jenny f_sleep_turn_angry_talk
        jen "Isso não é"
        show jenny f_sleep_turn_angry
        pause
        show jenny f_sleep_turn_angry_talk
        jen "deixa pra lá, apenas se apresse, você faria?!"
        show jenny b_sleep_side a_sleep_side f_sleep_side_sleeping with dissolve
        jump jenny_bed_night_grope_in_bed


label jenny_bed_night_go_further:
    show player b_sleep_side f_sleep_side_shy o_sleep_side_boxers_boner
    show expression "characters/player/layeredimage/player_arms_a_sleep_side_normal.png"
    show jenny b_sleep_turn_shirtup o_sleep_panties f_sleep_turn_normal_talk
    with dissolve
    jen "Tudo bem, isso é bastante preliminares."
    show jenny a_sleep_turn_remove1 o_empty f_sleep_turn_normal with dissolve
    pause
    show player a_sleep_side_remove1_boner f_sleep_side_normal o_empty zorder 1
    show jenny a_sleep_turn_remove2 zorder 2
    with dissolve
    pause
    show player b_sleep_side a_sleep_side_remove2
    show jenny a_sleep_turn o_sleep_panties_down
    with dissolve
    pause
    show player a_sleep_side_insert o_sleep_side_boxers_down with dissolve
    pause
    scene expression "backgrounds/location_home_jennybedroom_sex_sleep.jpg"
    show jenny_sleeping_sex default
    show jenny_sleeping_sex_face normal_talk
    show player_jenny_sleeping_sex pre
    show jenny_sex_sleep_blanket
    with fade
    jen "Coloque dentro de mim."
    hide jenny_sleeping_sex_face
    show jenny_sleeping_sex insert
    hide player_jenny_sleeping_sex
    with dissolve
    player_name "Tudo bem."
    show jenny_sleeping_sex 1 with dissolve
    jen "Fooode..."
    $ anim_toggle = True
    $ animated = True
    $ M_jenny.set('sex speed', .12)
    show expression AnimatedImage("jenny_sleeping_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_sleeping_sex at Position(xalign = 0.0, yoffset = 0)
    jump jenny_jenny_bed_sex_loop

label jenny_jenny_bed_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_sleeping_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_sleeping_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_jenny_bed_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_sleeping_sex {}".format(pose_list[pose_counter]) as jenny_sleeping_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_jenny_bed_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_jenny_bed_sex_options

label jenny_jenny_bed_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 25:
        jen "Mmm, isso é bom...{p=1}{nw}"
    if animcounter == 1 and randomizer() < 25:
        player_name "Mmhmm.{p=1}{nw}"
    if animcounter == 2 and randomizer() < 25:
        jen "Ahhh!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 25:
        jen "Ah, bem isso!{p=1}{nw}"
        jen "Sim!{p=1}{nw}"
    return

label jenny_jenny_bed_sex_cum_outside:
    $ M_jenny.set("jenny_bed_cum_inside", False)
    jen "Não pare!"
    player_name "Vou gozar!"
    jen "NÃO PARE!!"
    show jenny_sleeping_sex insert with dissolve
    jen "NÃO"
    show jenny_sleeping_sex default
    show jenny_sleeping_sex_face cum
    show player_jenny_sleeping_sex cum
    player_name "HNNGGG!!!" with flash
    show jenny_sleeping_sex_face angry_talk
    jen "Oh, que porra, {b}[firstname]{/b}!"
    scene expression "backgrounds/location_home_jennybedroom_bed.jpg"
    show jenny b_sleep_after a_empty f_sleep_turn_angry
    show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png" zorder 1
    show player f_sleep_cuddle_side_shy b_empty a_empty at Position (align=(0,0))
    with fade
    player_name "Hmm?"
    show jenny f_sleep_turn_angry_talk
    jen "Eca, é porra em toda parte!"
    jen "Como vou dormir agora?"
    show jenny f_sleep_turn_angry
    show player f_sleep_cuddle_side_shy_talk
    player_name "Desculpa..."
    show player f_sleep_cuddle_side_shy
    show jenny f_sleep_turn_angry_talk
    jen "Por favor..."
    show jenny f_sleep_turn_angry
    pause
    show jenny f_sleep_turn_angry_talk
    jen "Saia!"
    show jenny f_sleep_turn_angry
    show player f_sleep_cuddle_side_shy_talk
    player_name "O que?!"
    player_name "Você está falando sério?"
    show player f_sleep_cuddle_side_shy
    show jenny f_sleep_turn_angry_talk
    jen "Sim, você é nojento!"
    show jenny f_sleep_turn_angry
    jump jenny_bed_sex_night_end

label jenny_jenny_bed_sex_cum_inside:
    $ M_jenny.set("jenny_bed_cum_inside", True)
    jen "Não pare!"
    player_name "Vou gozar!"
    jen "NÃO PARE!!"
    jen "NGGHHH!!!"
    show jenny_sleeping_sex cum
    player_name "HNNGGG!!!" with flash
    show xray_jenny_jenny_bed at Position (align=(0,0))
    show jenny_sleeping_sex cum2
    with dissolve
    pause
    hide xray_jenny_jenny_bed
    show jenny_sleeping_sex pullout
    with dissolve
    jen "Oh, uau!"
    show jenny_sleeping_sex default
    show jenny_sleeping_sex_face normal
    show player_jenny_sleeping_sex after
    with dissolve
    player_name "Haah... Haah..."
    call call_pregnancy_minigame ("jenny_bed_sex_cum_inside_post_pregnancy", M_jenny)

label jenny_bed_sex_cum_inside_post_pregnancy:
    scene expression "backgrounds/location_home_jennybedroom_bed.jpg"
    show jenny b_sleep_after a_empty f_sleep_turn_angry_talk
    show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png" zorder 1
    show player f_sleep_cuddle_side_shy b_empty a_empty at Position (align=(0,0))
    with fade
    jen "Você porra você gozou dentro de mim?"
    show jenny f_sleep_turn_angry
    show player f_sleep_cuddle_side_shy_talk
    player_name "Sim."
    show player f_sleep_cuddle_side_shy
    show jenny f_sleep_turn_angry_talk
    jen "Deus droga, {b}[firstname]{/b}!"
    show jenny f_sleep_turn_angry
    show player f_sleep_cuddle_side_shy_talk
    player_name "Você disse para não parar..."
    show player f_sleep_cuddle_side_shy
    show jenny f_sleep_turn_angry_talk
    jen "Você sabe que não é isso que eu quis dizer!"
    show jenny f_sleep_turn_angry
    show player f_sleep_cuddle_side_shy_talk
    player_name "Me desculpe..."
    player_name "Nós estávamos realmente interessados e tudo parecia tão bom, eu-"
    show player f_sleep_cuddle_side_shy
    show jenny f_sleep_turn_angry_talk
    jen "{b}*Suspiro*{/b} Por favor..."
    jen "Apenas saia!"
    show jenny f_sleep_turn_angry
    show player f_sleep_cuddle_side_shy_talk
    player_name "O que?!"
    player_name "Você está falando sério?"
    show player f_sleep_cuddle_side_shy
    show jenny f_sleep_turn_angry_talk
    jen "Sim, você é nojento!"
    show jenny f_sleep_turn_angry
    jump jenny_bed_sex_night_end

label jenny_bed_sex_night_end:
    if M_jenny.get("dominance") > 0:
        show player f_sleep_cuddle_side_normal_talk
        player_name "Você apenas relaxaria?"
        if M_jenny.get("jenny_bed_cum_inside"):
            player_name "Tudo vai ficar bem."
        else:
            player_name "Não é como se você nunca tivesse tido o meu sêmen em você antes..."
        show player f_sleep_cuddle_side_normal
        jen "..."
        show player f_sleep_cuddle_side_normal_talk
        player_name "Apenas cale a boca e vá dormir, podemos lidar com isso de manhã."
        show player f_sleep_cuddle_side_normal
        show jenny f_sleep_turn_angry_talk
        jen "està bem."
        jen "... Idiota."
        show jenny f_sleep_turn_angry
        scene black with fade
        pause
    else:
        show player f_sleep_cuddle_side_shy_talk
        player_name "Vamos lá, {b}[jen_name]{/b}..."
        player_name "Não podemos apenas dormir?"
        show player f_sleep_cuddle_side_shy
        show jenny f_sleep_turn_angry_talk
        jen "Eu não quero você roncando no meu ouvido a noite toda!"
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "Você é quem ronca!!!"
        show player f_sleep_cuddle_side_shy
        show jenny f_sleep_turn_angry_talk
        jen "Foda-se você!"
        show jenny f_sleep_turn_angry
        pause
        show jenny f_sleep_turn_angry_talk
        jen "Bem."
        jen "Seu grande bebê!"
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "Obrigado!"
        show player f_sleep_cuddle_side_shy
        show jenny f_sleep_turn_angry_talk
        jen "Eugh..."
        show jenny f_sleep_turn_angry
        scene black with fade
        pause
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["17_unlocked"] = True
    jump jenny_bed_sex_sleeping

label jenny_bed_sex_sleeping:
    $ Sleep()
    if M_player.is_set("just wokeup"):
        $ renpy.call(game.dialog_select("player_just_wokeup"), woke_with = M_jenny)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
