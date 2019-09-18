label jenny_couch_sex:
    if M_jenny.get("dominance") <= 0:
        hide jenny_couch_dick_rub
        show jenny a_couch_dick3 f_couch_sit_sexy_talk
        jen "Tudo bem, estou entediada com isso..."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right
        player_name "Hmm?"
        show player a_couch_boner zorder 1
        show jenny b_couch_remove f_empty a_empty zorder 0
        with dissolve
        pause
        show jenny b_couch_sit f_couch_sit_sexy_talk a_couch_rest o_couch_teasing with dissolve
        jen "Venha aqui e me foda."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "O que?!"
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk
        jen "Você me ouviu."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "Mas, {b}[deb_name]{/b} está bem aí!"
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk
        jen "Eu sei, é emocionante! Não é?"
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "Não?"
        show player f_couch_sit_right
        show jenny f_couch_sit_eyeroll
        jen "{b}*Suspiro*{/b} Sim!"
        show jenny f_couch_sit_sexy
        player_name "..."
        show jenny f_couch_sit_sexy_talk
        jen "Não seja uma bucetinha."
        show jenny f_couch_sit_sexy_talk_down
        jen "Eu quero esse pau grande!"
        show jenny f_couch_sit_sexy_down
    else:
        show jenny f_couch_sit_sexy_talk_down
        jen "Você está chegando perto?"
        show jenny f_couch_sit_sexy_down
        show player f_couch_sit_down_talk
        player_name "Sim."
        show player f_couch_sit_right
        hide jenny_couch_dick_rub
        show jenny a_couch_dick3 f_couch_sit_sexy_down
        pause
        show player f_couch_sit_right_talk
        player_name "O que você está fazendo?!"
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk
        jen "Estou entediada disso..."
        show jenny f_couch_sit_sexy
        pause
        show jenny f_couch_sit_sexy_talk
        jen "Vamos foder!"
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "Hã?!"
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk
        jen "Você me ouviu."
        show player a_couch_boner zorder 1
        show jenny b_couch_remove f_empty a_empty zorder 0
        with dissolve
        pause
        show jenny b_couch_sit f_couch_sit_sexy_talk a_couch_rest o_couch_teasing with dissolve
        jen "eu quero você dentro de mim."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "Mas, {b}[deb_name]{/b} está bem aí!"
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk
        jen "Assim?"
        jen "Eu posso ficar quieta."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "Ok, certo."
        show player f_couch_sit_right
        show jenny f_couch_sit_upset_talk
        jen "Venha, por favor?"
        show jenny f_couch_sit_upset
        show player f_couch_sit_down_surprised
        player_name "!!!"
        show player f_couch_sit_right_talk
        player_name "Você acabou de dizer, por favor?"
        show player f_couch_sit_right
        show jenny f_couch_sit_eyeroll
        jen "... Talvez."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "Uau, você realmente quer."
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_down
        jen "Mmhmm!"
    show player f_couch_sit_right_talk
    player_name "Està bem."
    show player b_couch_remove a_empty f_empty
    with dissolve
    pause
    show player b_couch_jump
    show jenny b_couch_jump o_empty f_empty a_empty
    with dissolve
    jen "Oh, fooode!"
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .09)
    hide jenny
    scene expression "backgrounds/location_home_livingroom_couch_sex.jpg"
    show expression AnimatedImage("jenny_couch_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_couch_sex at Position(xalign = 0.0, yoffset = 0)
    with fade
    player_name "Shhh!"
    player_name "{b}[deb_name]{/b} Vai surtar se ela nos encontrar!"
    jen "Eu sei!"
    jen "É tão profundo que não posso"
    jump jenny_couch_sex_loop

label jenny_couch_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_couch_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_couch_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_couch_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_couch_sex {}".format(pose_list[pose_counter]) as jenny_couch_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_couch_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_couch_sex_options

label jenny_couch_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jen "Ahh!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jen "Eu amo tanto seu pau!{p=2}{nw}"
        jen "Oh, Deus!!{p=1}{nw}"
        jen "I love it, I love it, I LOVE IT!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jen "Me Fooode, SIM!{p=1}{nw}"
        player_name "Shh!!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        jen "Vamos lá, {b}[firstname]{/b}!{p=1}{nw}"
        jen "Fuck me harder!{p=1}{nw}"
        player_name "Pare de puxar!{p=2}{nw}"
        if M_jenny.get("sex speed") > 0.061:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.03)
        jen "Ah, bem aí!{p=1}{nw}"
    return

label jenny_couch_sex_cum_outside:
    player_name "Vou gozar!"
    jen "Eu também!"
    jen "NGGHHH!!!"
    show jenny_couch_sex cumshot
    player_name "HNNGGG!!!" with flash
    pause
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show jenny b_couch_after3 f_empty a_empty
    show player b_couch_sit_naked f_couch_sit_right_talk a_couch_naked_after
    with fade
    player_name "Uau..."
    show player f_couch_sit_right
    show jenny b_couch_after4
    jen "Haah... Haah..."
    show jenny b_couch_after3
    show player f_couch_sit_right_talk
    player_name "Isso foi intenso!"
    show player f_couch_sit_right
    show jenny b_couch_after4
    jen "Você gozou em cima de mim!"
    show jenny b_couch_after3
    show player f_couch_sit_right_talk
    player_name "Você prefere que eu tenha gozado dentro de você?"
    show player f_couch_sit_right
    show jenny b_couch_after4
    jen "Não, mas você poderia ter"
    show jenny b_couch_after3
    pause
    show jenny b_couch_after4
    jen "{b}*Suspiro*{/b} deixa pra lá."
    show jenny b_couch_remove with dissolve
    jen "Vou tomar banho."
    show jenny b_couch_transition with dissolve
    pause 1
    hide jenny with dissolve
    jen "Ate mais tarde, perdedor."
    show player f_couch_sit_right_talk
    player_name "Sim, te vejo depois."
    show player f_couch_sit_right
    pause
    show player f_couch_sit_down_surprised
    player_name "( Ufa, eu acho que estamos fodendo demais... )"
    player_name "( Impressionante! )"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["08_unlocked"] = True
    call hide_home_tv
    $ M_jenny.set("couch_sex_first", False)
    $ M_jenny.set("had_couch_sex", True)
    $ game.timer.tick()
    $ game.main()

label jenny_couch_sex_cum_inside:
    player_name "Vou gozar!"
    jen "Eu também!"
    player_name "Me solte!"
    jen "NGGHHH!!!"
    player_name "{b}[jen_name]{/b} Eu não posso-"
    show jenny_couch_sex cum
    player_name "HNNGGG!!!" with flash
    jen "AHHHH!!!"
    show jenny_couch_sex cum 2
    show xray_jenny_couch at Position (align=(0,0))
    pause
    hide xray_jenny_couch
    show jenny_couch_sex pullout 1
    with dissolve
    player_name "puta merda..."
    show jenny_couch_sex pullout 2 with dissolve
    jen "Haah... Haah..."
    call call_pregnancy_minigame ("jenny_couch_sex_cum_inside_post_pregnancy", M_jenny)

label jenny_couch_sex_cum_inside_post_pregnancy:
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show jenny b_couch_after2 f_empty a_empty
    show player b_couch_sit_naked f_couch_sit_right_talk a_couch_naked_after
    with fade
    show player f_couch_sit_right
    show jenny b_couch_after1
    jen "Oh meu deus, você gozou dentro de mim?!"
    show jenny b_couch_after2
    show player f_couch_sit_right_talk
    player_name "Eu tentei tirar, mas você não me soltou!"
    show player f_couch_sit_right
    show jenny b_couch_after1
    jen "Bem, eu estava focada em gozar!"
    show jenny b_couch_after2
    pause
    show jenny b_couch_after1
    jen "PORRA!"
    jen "Você está tão morto se eu engravidar!"
    show jenny b_couch_after2
    show player f_couch_sit_right_talk
    player_name "Eu?!"
    player_name "Você é o única que me segurou lá!"
    show player f_couch_sit_right
    show jenny b_couch_after1
    jen "Cale-se!"
    show jenny b_couch_remove with dissolve
    jen "Grr, Vou correr pro chuveiro!"
    show jenny b_couch_transition_mad with dissolve
    pause 1
    hide jenny with dissolve
    jen "Idiota..."
    show player f_couch_sit_right_talk
    player_name "Ah, então é tudo culpa minha, né?!"
    show player f_couch_sit_right
    pause
    player_name "( Ela se foi... )"
    pause
    show player f_couch_sit_down_surprised
    player_name "( Ufa, eu acho que estamos apenas fodendo sempre... )"
    player_name "( Impressionante! )"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["09_unlocked"] = True
    call hide_home_tv
    $ M_jenny.set("had_couch_sex", True)
    $ M_jenny.set("couch_sex_first", False)
    $ game.timer.tick()
    $ game.main()

label jenny_shower_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_shower_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_shower_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_shower_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_shower_sex {}".format(pose_list[pose_counter]) as jenny_shower_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_shower_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_shower_sex_options

label jenny_shower_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jen "Ahh!!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jen "É tão profundo!{p=1}{nw}"
        jen "Foda-me!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jen "FOOOODE!!!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        player_name "Uhh!{p=1}{nw}"
    return

label jenny_shower_sex_cum_inside:
    jen "Estou gozando! Estou gozando!"
    jen "NGGHHH!!!"
    player_name "Sim, estou chegando perto também"
    pause
    player_name "{b}[jen_name]{/b}?"
    show jenny_shower_sex cum
    player_name "HNNGGG!!!" with flash
    jen "AAAHHHH!!!"
    show jenny_shower_sex cum 2
    show xray_jenny_shower at Position (align=(0,0))
    pause
    call call_pregnancy_minigame ("jenny_mc_shower_sex_cum_inside_post_pregnancy_minigame", M_jenny)

label jenny_mc_shower_sex_cum_inside_post_pregnancy_minigame:
    call scene_shower_with_vfx
    show player b_naked a_naked_sides f_tired_talk od_naked_dick1
    show jenny b_shower_back a_shower_back_push f_shower_overshoulder_back_look_normal at Position (align=(0,0))
    with fade
    player_name "Haah... Haah..."
    show jenny a_shower_back_butt f_shower_overshoulder_back_look_surprised with dissolve
    show player f_normal_talk
    player_name "Puta merda!"
    show player f_normal
    show jenny b_shower_back_creampie a_empty with dissolve
    jen "Você gozou comigo?!"
    show player f_worried_talk
    player_name "Sim, um pouco..."
    show player f_surprised
    show jenny b_naked a_naked_crossed f_angry_talk with dissolve
    jen "UM POUCO?!"
    jen "Isso é muito amor!"
    show jenny f_angry
    show player f_worried_talk
    player_name "Eu sinto Muito."
    player_name "Eu acho que fiquei um pouco empolgado lá no final..."
    show player f_worried
    show jenny f_angry_talk
    jen "E se eu engravidar?!"
    show jenny f_angry
    show player f_worried_talk
    player_name "Eu não fiz por mau"
    show player f_worried
    show jenny f_angry_talk
    jen "Droga, {b}[firstname]{/b}!"
    jen "Dê o fora daqui!"
    show jenny f_angry
    show player f_worried_talk
    player_name "Tudo bem, tudo bem..."
    player_name "Eu disse que sinto muito, sheesh."
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["14_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_hallway)
    $ game.main()

label jenny_shower_sex_cum_outside:
    jen "Estou gozando! Estou gozando!"
    jen "NGGHHH!!!"
    player_name "Sim, estou chegando perto também"
    pause
    player_name "{b}[jen_name]{/b}?"
    hide jenny_shower_sex
    show jenny b_shower_cumshot a_empty f_shower_cumshot
    show player b_side_naked_forward od_side_naked_forward_cum1 f_side_react a_side_naked_up_clench
    player_name "HNNGGG!!!" with flash
    show player od_side_naked_forward_cum2 o_side_naked_forward_cum3 with dissolve
    pause
    show player b_naked a_naked_sides f_tired_talk od_naked_dick1 o_empty
    show jenny b_naked a_naked_side f_sexy_down at Position (align=(0,0))
    with dissolve
    player_name "Haah... Haah..."
    show player f_normal
    show jenny f_sexy_talk
    jen "Haah... Puta merda!"
    show jenny f_sexy_talk_down
    jen "eu acho que"
    jen "Eu preciso ir deitar um pouco."
    show jenny f_sexy
    show player f_worried_talk
    player_name "Você está certa?"
    show player f_worried
    show jenny f_sexy_talk
    jen "Sim, é só o vapor e o sexo e..."
    show player f_normal
    show jenny f_laugh
    jen "Porra, eu mal posso andar!"
    show jenny f_sexy
    show player f_grin
    player_name "Heh."
    show player f_normal_talk
    player_name "Aqui eu te ajudo."
    show player f_worried
    show jenny f_upset_talk a_naked_hips with dissolve
    jen "Não, foda-se!"
    jen "Estou bem!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Tudo bem, sheesh."
    player_name "Eu só estou tentando ser atencioso..."
    show player f_worried
    show jenny f_upset_talk
    jen "Bem, pare com isso!"
    hide jenny with dissolve
    pause
    player_name "( Ela é tão estranha às vezes... )"
    show player f_grin
    player_name "( Oh bem, isso foi incrível! )"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["14_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_hallway)
    $ game.main()

label bj_shower_repeat_sub:
    show player f_worried_talk_low
    player_name "Arf!"
    show player f_worried_low
    show jenny f_grin_talk
    jen "Heh, Mais!"
    show jenny f_grin
    show player f_worried_talk_low
    player_name "{b}*Suspiro*{/b}"
    show player f_shock
    player_name "Arf! Arf! Arf!"
    show player f_worried_low
    show jenny f_laugh
    jen "Hahahaah!!"
    show player b_side_naked a_side_naked_react f_side_shy_down od_side_naked_dick3
    show jenny b_shower_kneeling f_shower_kneeling_talk a_empty
    with dissolve
    if randomizer() > 50:
        jen "Bom cãozinho!"
    else:
        jen "Tem um bom menino!"
    call scene_shower_with_vfx_zoom
    show jenny_shower_bj_mc
    show jenny_shower_bj pre_talk
    with fade
    jen "Agora você recebe uma recompensa!"

label bj_shower_repeat_dom:
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .14)
    show expression AnimatedImage("jenny_shower_bj", [1,2,3,4,5,6,7], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
    player_name "!!!" with hpunch

    if M_jenny.get('first_time_deep_bj'):
        $ M_jenny.set('first_time_deep_bj', False)
        player_name "{b}*Gasp*{/b}"
        pause
        player_name "Uau, tudo bem..."
        player_name "Ahh!"
        pause
        player_name "Mm, isso é tão bom!"
        jen "Mmhrmm."
        pause
        show jenny_shower_bj_mc
        show jenny_shower_bj pre_talk
        with dissolve
        jen "Tudo bem, vou tentar alguma coisa agora..."
        show jenny_shower_bj pre_look
        player_name "Hmm?"
        show jenny_shower_bj pre_talk
        jen "Meus fãs me pedem algo e eu vou testar em você."
        show jenny_shower_bj pre_look
        player_name "O que é isso?"
        show jenny_shower_bj pre_talk
        jen "Você verá."
        jen "Apenas tenta ficar parado!"
        show expression AnimatedImage("jenny_shower_bj", [1,2,3,4,5,6,7], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
        player_name "Você não vai fazer nada estranho, vai?"
        pause
        player_name "{b}[jen_name]{/b}?"
    else:
        player_name "Mmm."
        pause
        player_name "Muito agradável!"
        jen "Shrmmup!!"
        player_name "Ohh!"
        pause
        player_name "Mm, isso é tão bom!"
        jen "Mmhrmm."
        pause

    $ M_jenny.set('sex speed', .4)
    show expression AnimatedImage("jenny_shower_bj_deep", [1,2], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
    $ M_jenny.set("jenny_bj_deep", True)
    player_name "!!!" with hpunch
    player_name "Oh my god!!"
    pause
    player_name "Isso é incrível!!!"
    jen "{b}*Gllrrkkk*{/b}"
    pause
    jen "{b}*Bllgghhh*{/b}"
    player_name "{b}[jen_name]{/b}, Eu não posso"

    label jenny_shower_bj_loop:
        show screen sex_anim_buttons
        pause
        hide screen sex_anim_buttons
        $ animcounter = 0
        while animcounter < 4:
            if anim_toggle:
                if not animated:
                    if M_jenny.get("jenny_bj_deep"):
                        $ M_jenny.set('sex speed', .4)
                        show expression AnimatedImage("jenny_shower_bj_deep", [1,2], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0) with dissolve
                    else:
                        $ M_jenny.set('sex speed', .14)
                        show expression AnimatedImage("jenny_shower_bj", [1,2,3,4,5,6,7], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0) with dissolve
                    $ animated = True
                pause 5
                call expression game.dialog_select("jenny_shower_bj_hscene_dialog")
                pause 3
            else:

                $ pose_counter = 0
                if M_jenny.get("jenny_bj_deep"):
                    $ pose_list = [1,2]
                else:
                    $ pose_list = [1,2,3,4,5,6,7]
                $ poses_done = []
                while poses_done != pose_list:
                    if M_jenny.get("jenny_bj_deep"):
                        show expression "jenny_shower_bj_deep {}".format(pose_list[pose_counter]) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
                    else:
                        show expression "jenny_shower_bj {}".format(pose_list[pose_counter]) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
                    pause
                    $ poses_done.append(pose_list[pose_counter])
                    $ pose_counter += 1
                call expression game.dialog_select("jenny_shower_bj_hscene_dialog")
            $ animcounter += 1
        call screen jenny_shower_bj_options

label jenny_shower_bj_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        player_name "Mmm.{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        player_name "muito agradável!{p=1}{nw}"
        jen "Shrmmup!!{p=1}{nw}"
        player_name "Ohh!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        player_name "{b}*Gasp*{/b}"
    if animcounter == 3 and randomizer() < 10:
        player_name "Uau, tudo bem..."
        player_name "Ahh!"
    if animcounter == 3 and randomizer() < 10:
        player_name "Mm, isso é tão bom!"
        jen "Mmhrmm."
    return

label jenny_shower_bj_cum:
    player_name "Estou chegando perto!"
    jen "{b}*Sluuuuurp*{/b}"
    pause
    player_name "{b}[jen_name]{/b}!"
    pause
    show jenny_shower_bj cum
    player_name "HNNGGG!!!" with flash
    jen "!!!"
    show jenny_shower_bj after with dissolve
    pause
    call scene_shower_with_vfx
    show jenny b_naked a_naked_hips f_cheeks_surprised
    show player b_naked a_naked_sides f_normal_talk od_naked_dick1
    with fade
    if M_jenny.get("first_shower_time"):
        $ M_jenny.set("first_shower_time", False)
        player_name "Ufa, isso foi"
        player_name "Quer dizer, eu não estava esperando que você"
        show player f_surprised
        show jenny f_cheeks_swallow a_naked_shocked with dissolve
        player_name "!!!"
        show jenny f_normal_talk
        jen "Porra, isso foi muito esperma"
        show jenny f_normal a_naked_hips with dissolve
        show player f_worried_talk
        player_name "Você engoliu?"
        show player f_surprised
        show jenny f_normal_talk
        jen "Sim, então?"
        show jenny f_normal
        show player f_normal_talk
        player_name "Eu pensei que você não gostasse de fazer isso!"
        show player f_normal
        show jenny f_upset_talk
        jen "Quando eu disse isso?"
        show jenny f_upset
        show player f_skeptical_talk
        player_name "Quando você me deixou no ar!"
        player_name "Você disse que só engoliu porque seus fãs pagam mais por isso!"
        show player f_skeptical
        show jenny f_normal_talk
        jen "Oh, certo..."
        show jenny f_normal
        show player f_skeptical_talk
        player_name "Eles não podem nos ver aqui, {b}[jen_name]{/b}!"
        show player f_skeptical
        show jenny f_upset_talk
        jen "Talvez eu não quisesse fazer uma bagunça, você já pensou nisso?!"
        show jenny f_upset
        show player f_worried_talk
        player_name "Você não queria fazer uma bagunça ... No chuveiro?"
        show player f_worried
        jen "..."
        show jenny f_upset_talk
        jen "Oh meu deus, apenas"
        jen "Tanto faz."
        show jenny f_eyeroll
        jen "{b}*Suspiro*{/b} Eu gosto disso?"
        show jenny f_upset
        show player f_surprised
        player_name "..."
        show jenny f_upset_talk
        jen "Eu gosto de engolir seu esperma..."
        jen "Você está feliz agora?!"
        show jenny f_upset
        show player f_normal_talk
        player_name "Heh, eu não posso acreditar que você acabou de dizer isso..."
        show player f_normal
        show jenny f_eyeroll a_naked_crossed with dissolve
        jen "Ugh..."
        show jenny f_upset_talk
        jen "Não tenha idéias, perdedor!"
        jen "Só porque eu gosto do seu esperma e do seu pau grande, isso não significa que eu goste de você!"
        show jenny f_upset
        show player f_worried
        player_name "..."
        show jenny f_upset_talk
        jen "Agora vá embora e me deixe terminar meu banho!"
        show jenny f_upset
        show player f_worried_talk
        player_name "Tudo bem."
        show player f_normal_talk
        player_name "Obrigado pelo-"
        show player f_surprised
        show jenny f_angry_talk
        jen "Saia!!"
        hide player with dissolve
        jen "Por amor de merda!"
        show jenny f_angry_pouting

        $ player.go_to(L_home_hallway)
        scene expression player.location.background_closeup
        show player f_grin with dissolve
        player_name "( Isso foi tão incrível! )"
        player_name "( Isso significa {b}Eu posso me juntar a ela no chuveiro sempre que eu quiser{/b}? )"
        show player f_thinking a_dressed_thinking with dissolve
        pause
        show player f_grin
        player_name "( Eu acho que sim! )"
    else:
        player_name "Ufa..."
        player_name "Você está ficando muito bom nisso!"
        show player f_normal
        show jenny f_cheeks_swallow a_naked_shocked with dissolve
        pause
        show jenny f_grin_talk
        jen "Pfft, Eu nunca fui bom nisso?"
        show jenny f_grin
        show player f_normal_talk
        player_name "Heh, bom ponto."
        show player f_normal
        pause
        show jenny f_normal_talk
        jen "Tudo bem, fecha a porta para que eu possa terminar o meu banho."
        show jenny f_normal
        show player f_normal_talk
        player_name "Sim, ok."
        player_name "Obrigado pelo boquete!"
        show player f_grin
        show jenny f_eyeroll a_naked_crossed with dissolve
        jen "Oh meu Deus."
        show jenny f_upset_talk
        jen "Saia!"
        show jenny f_upset
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["13_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_hallway)
    $ game.main()

label jenny_mc_room_sex_on_sleep:
    if store._in_replay is not None:
        $ player.location = L_home_bedroom
        $ game.timer.tick(3)
    scene expression "backgrounds/location_home_bedroom_cutscene18.jpg"
    jen "Psst!"
    jen "{b}[firstname]{/b}acorda?"
    scene expression "backgrounds/location_home_bedroom_cutscene17.jpg"
    player_name "Mmm."
    pause
    scene expression "backgrounds/location_home_bedroom_sex01c.jpg"
    show player b_visit a_empty f_visit_sleep
    show jenny b_visit_sit a_visit_sit_down f_visit_sexy_talk with dissolve
    if M_jenny.is_state(S_jenny_night_time_sex):
        jen "{b}[firstname]{/b}?"
        show jenny f_visit_sexy
        player_name "Nnnhhh."
        pause
        show jenny f_visit_sexy_talk
        jen "Vamos, acorde."
        show jenny f_visit_sexy
        player_name "Não."
        show jenny f_visit_sexy_down a_visit_sit_reach with dissolve
        show player f_visit_normal_talk
        player_name "Droga, {b}[jen_name]{/b}..."
        player_name "É o meio da noite!"
        show player b_visit_up2 f_visit_up_tired
        show jenny f_visit_sexy_talk_down a_visit_sit_pull
        with dissolve
        jen "Cale a boca."
        show jenny f_visit_sexy_down a_visit_sit_up with dissolve
        show jenny a_visit_sit_up2 with dissolve
        pause
        show jenny a_visit_sit_stroke with dissolve
        show player f_visit_up_tired_talk
        player_name "O que você está fazendo, {b}[jen_name]{/b}?"
        player_name "Estou tentando dormir"
        show player f_visit_up_tired
        show jenny f_visit_sexy_talk_down
        jen "O que parece que estou fazendo?!"
        show jenny b_visit_remove1 a_visit_dick f_empty with dissolve
        show player f_visit_up_surprised
        pause
        show player f_visit_up_tired_talk
        show jenny b_visit_remove2 with dissolve
        player_name "Nós realmente temos que fazer isso agora?!"
        show jenny b_visit_climb a_empty with dissolve
        jen "Sim, estou com tesão e quero agora mesmo!"

        scene expression "backgrounds/location_home_bedroom_sex05.jpg"
        show jenny_mc_room_sex insert
        with fade
        player_name "!!!"
        player_name "Droga {b}[jen_name]{/b}, estou cansado..."
        jen "Oh, pelo amor de Deus ... Tudo que você tem a fazer é ficar quieto!"
        jen "Eu sou a única a fazer todo o trabalho!"
        show jenny_mc_room_sex 1 with dissolve
        jen "{b}*Gasp*{/b}"
        jen "Deus, eu amo seu pau!"
        jump jenny_mc_room_sex_start
    else:
        jen "Acorde, {b}[firstname]{/b}."
        show jenny f_visit_sexy
        show player f_visit_normal_talk
        player_name "{b}[jen_name]{/b}?"
        show player f_visit_normal
        show jenny f_visit_sexy_talk a_visit_sit_reach with dissolve
        jen "Vamos, eu preciso disso."
        show player b_visit_up2 f_visit_up_tired
        show jenny f_visit_sexy_talk_down a_visit_sit_pull
        with dissolve
        pause
        show jenny f_visit_sexy_down a_visit_sit_up with dissolve
        show jenny a_visit_sit_up2 with dissolve
        pause
        show jenny a_visit_sit_stroke with dissolve
        menu:
            "Agora mesmo?":
                show player f_visit_up_tired_talk
                player_name "Agora mesmo?"
                show jenny b_visit_remove1 a_visit_dick f_empty with dissolve
                show player f_visit_up_surprised
                pause
                show jenny b_visit_remove2 with dissolve
                pause
                show jenny b_visit_climb a_empty with dissolve
                jen "Sim, eu quero agora mesmo."

                scene expression "backgrounds/location_home_bedroom_sex05.jpg"
                show jenny_mc_room_sex insert
                with fade
                player_name "!!!"
                player_name "Ok."
                jen "Deus, eu não consigo tirar esse pau da minha cabeça!"
                player_name "Uau, você está realmente molhada..."
                show jenny_mc_room_sex 1 with dissolve
                jen "{b}*Gasp*{/b}"
                jen "Porra."
                jump jenny_mc_room_sex_start
            "Não essa noite" if store._in_replay is None:
                if M_jenny.get("dominance") <= 0:
                    show player f_visit_up_tired_talk
                    player_name "Não agora, {b}[jen_name]{/b}."
                    show player f_visit_up_tired
                    show jenny f_visit_sexy_talk_down
                    jen "Vamos lá, você sabe que você quer..."
                    show jenny f_visit_sexy_down
                    show player f_visit_up_tired_talk
                    player_name "Vamos apenas fazer isso amanhã, ok?"
                    show player f_visit_up_tired
                    show jenny f_visit_sexy_talk
                    jen "Eu não quero amanhã, eu quero agora!"
                    show jenny f_visit_sexy_down
                    show player f_visit_up_tired_talk
                    player_name "Ahhh, eu estou caaaaaansado..."
                    show player f_visit_up_tired
                    show jenny f_visit_angry_talk a_visit_sit_up2 with dissolve
                    jen "A sério?!"
                    jen "Você tem uma garota mega gostosa acariciando seu pau agora e você está dizendo não?!"
                    show jenny f_visit_angry
                    show player f_visit_up_tired_talk
                    player_name "{b}*Suspiro*{/b} Me desculpe ... eu não fiz-"
                    show player f_visit_up_tired
                    show jenny f_visit_angry_talk
                    jen "Esqueça!"
                    show jenny f_visit_angry
                    show player f_visit_up_tired_talk
                    player_name "Não, nós podemos se você realmente quiser-"
                    show player f_visit_up_tired
                    show jenny f_visit_angry_talk
                    jen "Eu não estou mais no clima!"
                    show jenny a_visit_dick b_empty f_empty with dissolve
                    jen "Você é uma putinha às vezes!"
                    show player f_visit_up_tired_talk
                    player_name "{b}[jen_name]{/b}, Me desculpe eu-"
                    show player f_visit_up_tired
                    player_name "..."
                else:
                    show player f_visit_up_tired_talk
                    player_name "Não agora, {b}[jen_name]{/b}."
                    show player f_visit_up_tired
                    show jenny f_visit_sexy_talk_down
                    jen "Vamos lá, você sabe que você quer..."
                    show jenny f_visit_sexy_down
                    show player f_visit_up_tired_talk
                    player_name "Não, eu só quero dormir ... Ok?"
                    show player f_visit_up_tired
                    show jenny f_visit_sexy_talk
                    jen "Por favor, {b}[firstname]{/b}?"
                    show jenny f_visit_sexy
                    show player f_visit_up_tired_talk
                    player_name "eu disse não!"
                    show player f_visit_up_tired
                    show jenny f_visit_angry_talk a_visit_sit_up2 with dissolve
                    jen "A sério?!"
                    jen "Estou tentando ser legal aqui, do jeito que você gosta ... Eu até disse por favor!"
                    show jenny f_visit_angry
                    show player f_visit_up_tired_talk
                    player_name "Eu não estou de bom humor, ok?"
                    show player f_visit_up_tired
                    jen "..."
                    show jenny f_visit_angry_talk
                    jen "Està bem!"
                    show jenny a_visit_dick b_empty f_empty with dissolve
                    jen "Eu não sei porque eu desperdiço meu tempo com você..."
                    show player f_visit_up_tired_talk
                    player_name "Whatever."
                    show player f_visit_up_tired
                scene black with fade
                pause
                $ game.timer.sleep()
                $ game.main()

label jenny_mc_room_sex_start:
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    show expression AnimatedImage("jenny_mc_room_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
    jen "Ahh!"
    pause
    player_name "Ok, isso é muito bom..."
    if M_jenny.is_state(S_jenny_night_time_sex):
        jen "Veja, e você estava choramingando sobre isso!"
        player_name "Bem, nós poderíamos ter feito isso amanhã!"
        jen "Sim e nós provavelmente vamos..."
        player_name "Mesmo?"
        jen "Uhh, sim ... Camshows, modelo."
        player_name "Oh, certo."
        jen "Apenas cale a boca e deixe-me aproveitar o momento!"
    else:
        jen "Ahh!"
        pause
        player_name "Ok, isso é muito bom..."
        jen "Sim ele faz!"
    pause
    jen "Ahh, fooode!"
    pause
    jen "Mmm, Eu vou gozar nesse pau grande , {b}[firstname]{/b}!"
    if M_jenny.get("dominance") <= 0:
        jen "Você gostaria disso, não é?!"
        player_name "Sim."
        if M_jenny.get("sex speed") > 0.061:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.03)
        jen "Ahh!"
        jen "Vamos, diga!"
        jen "Diga que você quer que eu goze no seu pau grande!"
        player_name "Eu quero que você goze no meu pau grande!"
        if not M_jenny.is_state(S_jenny_night_time_sex):
            jen "Eu acho que você pode fazer melhor..."
            pause
            jen "Me diga que eu sou uma deusa do sexo!"
            player_name "Você é uma deusa do sexo!"
            jen "Venha, cadela!"
            jen "Eu não posso te ouvir!"
            player_name "Você é uma deusa do sexo!!!"
            jen "Você adora essa buceta, não é mesmo?!"
            player_name "Sim!"
        jen "Hahahaah!!"
    else:
        player_name "Então faça!"
        if M_jenny.get("sex speed") > 0.061:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.03)
        jen "Ah, merda!"
        player_name "Me diga que você quer!"
        jen "Mmm, Quero isso!"
        pause
        player_name "Vamos lá {b}[jen_name]{/b}, Mais rápido!"
        jen "Oh meu Deus!"
        pause
        if M_jenny.is_state(S_jenny_night_time_sex):
            jen "Ah, foda-me!!"
        else:
            player_name "Me implore para dar a você!"
            jen "Ahh!"
            jen "Por favor!!"
            pause
            player_name "Vamos lá, você pode fazer melhor!"
            jen "HUMMMMM!"
            jen "Por favor, {b}[firstname]{/b}!!"
            jen "Me dê isto!!!"

    player_name "Shh!"
    player_name "Você vai acordar {b}[deb_name]{/b}..."
    jen "Eu não me importo!"
    pause
    jen "Estou tão perto!"

label jenny_mc_room_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_mc_room_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_mc_room_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_mc_room_sex {}".format(pose_list[pose_counter]) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_mc_room_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_mc_room_sex_options

label jenny_mc_room_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jen "Ahh, foooode!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jen "Fooode!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jen "Hahahaah!!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        player_name "Oh meu deus!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jen "Ahh, me fode!!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        player_name "Estou chegando perto de gozar...{p=1}{nw}"
    return

label jenny_mc_room_sex_cum_inside:
    jen "Oh meu deus, oh meu deus, OH MEU DEUS!"
    pause
    jen "Estou gozando! Estou gozando!"
    player_name "Eu também!"
    jen "AAAHHH, PORRA!!!"
    player_name "{b}[jen_name]{/b}, sai fora!"
    jen "NGGHHH!!!"
    player_name "Ah, merda!"
    $ M_jenny.set('sex speed', .4)
    show expression AnimatedImage("jenny_mc_room_sex cum", [1,2], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
    player_name "HNNGGG!!!" with flash
    show jenny_mc_room_sex cum 2
    show xray_jenny_mcbedroom at Position (align=(0,0))
    pause
    call call_pregnancy_minigame ("jenny_mc_room_sex_cum_inside_post_pregnancy_minigame", M_jenny)

label jenny_mc_room_sex_cum_inside_post_pregnancy_minigame:
    scene expression "backgrounds/location_home_bedroom_sex05.jpg"
    show jenny_mc_room_sex pullout
    with fade
    player_name "Haah... Haah..."
    hide jenny_mc_room_sex
    show jenny b_visit_after f_visit_after_angry_talk_down o_visit_after_creampie a_empty
    with dissolve
    jen "Oh meu Deus..."
    show jenny f_visit_after_angry_down
    pause
    show jenny f_visit_after_angry_talk
    jen "Você gozou comigo?!"
    show jenny f_visit_after_angry
    player_name "Eu te disse para sair de mim!"
    show jenny f_visit_after_angry_talk
    jen "Deus droga, {b}[firstname]{/b}!"
    show jenny f_visit_after_angry
    player_name "O que?!"
    show jenny f_visit_after_angry_talk
    jen "Eu se eu engravidar seu idiota!"
    show jenny f_visit_after_angry
    player_name "Bem, eu sinto muito, mas eu avisei..."
    show jenny f_visit_after_angry_talk
    jen "Ugh, seja o que for."
    show jenny f_visit_after_angry_down
    pause
    show jenny f_visit_after_normal_talk
    jen "{b}*Suspiro*{/b} Foda-se..."
    jen "Heh, minhas pernas estão tremendo como uma louca!"
    if M_jenny.get('girlfriend_in_progress'):
        jump jenny_mc_room_sex_end_girlfriend_experience
    else:
        jump jenny_mc_room_sex_end

label jenny_mc_room_sex_cum_outside:
    jen "Oh meu deus, oh meu deus, OH MEU DEUS!"
    pause
    jen "Estou gozando! Estou gozando!"
    jen "NGGHHH!!!"
    pause
    player_name "Eu também!"
    show jenny_mc_room_sex cumshot
    player_name "HNNGGG!!!{p=1}{nw}" with flash
    show jenny o_visit_cumshot f_empty a_empty b_empty
    pause
    hide jenny_mc_room_sex
    show jenny b_visit_after f_visit_after_normal a_empty o_visit_cumshot2
    with dissolve
    player_name "Haah... Haah..."
    show jenny f_visit_after_normal_talk
    jen "Ufa, isso foi demais..."
    show jenny f_visit_after_normal
    pause
    show jenny f_visit_after_normal_talk
    jen "Hahaha, você fez uma bagunça!"
    show jenny f_visit_after_normal
    player_name "Heh, eu nem me importo ... estou tão exausto."
    show jenny f_visit_after_normal_talk
    jen "{b}*Snort*{/b} Hehehe!"
    jen "Você deveria se limpar, você parece ridículo..."
    if M_jenny.get('girlfriend_in_progress'):
        jump jenny_mc_room_sex_end_girlfriend_experience
    else:
        jump jenny_mc_room_sex_end

label jenny_mc_room_sex_end_girlfriend_experience:
    scene expression "backgrounds/location_home_bedroom_bed.jpg"
    show jenny b_sleep_side_naked a_sleep_side_naked f_sleep_side_tired at flip
    show jenny at Position (xpos=500)
    show player b_sleep_side f_sleep_side_normal_talk a_sleep_side_poke o_sleep_side_dick2
    show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent2.png"
    with fade
    if M_jenny.get("jenny_girlfriend_first_time"):
        player_name "Esta noite foi muito divertida!"
        show player f_sleep_side_normal
        show jenny f_sleep_side_tired_talk
        jen "Estou feliz que você tenha se divertido."
        show jenny f_sleep_side_tired
        show player f_sleep_side_normal_talk
        player_name "... E eu estou muito feliz que você não esteja fugindo dessa vez."
        show player f_sleep_side_normal
        show jenny f_sleep_side_tired_talk
        jen "Bem, você não me pagou, lembra?"
        show jenny f_sleep_side_tired
        show player f_sleep_side_normal_talk
        player_name "Sim."
        show player f_sleep_side_normal
        show jenny f_sleep_side_tired_talk
        jen "Hahahaah!"
        show jenny f_sleep_side_tired
        show player f_sleep_side_normal_talk
        player_name "Você também se divertiu, não foi?"
        show player f_sleep_side_normal
        show jenny f_sleep_side_rolleye
        jen "Sim, {b}[firstname]{/b}..."
        show jenny f_sleep_side_tired_talk
        jen "Agora você pode calar a boca e me deixar dormir?"
        show jenny f_sleep_side_sleeping
        show player f_sleep_side_normal_talk
        player_name "Desculpa..."
        show player f_sleep_side_kiss
    else:
        player_name "Hehe, Estou gostando muito das noites que fazemos isso..."
        show player f_sleep_side_normal
        show jenny f_sleep_side_tired_talk
        jen "Sim eu também."
        jen "Estou feliz por ter tido a ideia."
        show jenny f_sleep_side_tired
        show player f_sleep_side_normal_talk
        player_name "Uhh, você sabe, isso foi tecnicamente minha ideia..."
        show player f_sleep_side_normal
        show jenny f_sleep_side_tired_talk
        jen "Cale a boca!"
        show jenny f_sleep_side_tired
        show player f_sleep_side_normal_talk
        player_name "Estou apenas dizendo..."
        show player f_sleep_side_normal
        show jenny f_sleep_side_tired_talk
        jen "Sim, eu sei o que você está dizendo ... Agora feche a boca!"
        jen "Você está arruinando minha felicidade."
        show jenny f_sleep_side_tired
        show player f_sleep_side_normal_talk
        player_name "Desculpa."
        show player f_sleep_side_normal
        show jenny f_sleep_side_rolleye
        jen "Vá dormir."
        show jenny f_sleep_side_sleeping
        show player f_sleep_side_kiss
    $ Sleep()
    if M_player.is_set("just wokeup"):
        $ renpy.call(game.dialog_select("player_just_wokeup"), woke_with = M_jenny)
    $ game.main()

label jenny_mc_room_sex_end:
    show jenny f_visit_after_normal
    if M_jenny.is_state(S_jenny_night_time_sex):
        player_name "Você ficar?"
    else:
        player_name "Você está saindo de novo?"
    jen "Hmm?"
    if M_jenny.is_state(S_jenny_night_time_sex):
        player_name "Você quer dormir aqui comigo esta noite?"
        show jenny f_visit_after_normal_talk
        jen "Eca, não!"
        jen "Eu não sou sua namorada, doofus..."
    else:
        player_name "Você pode dormir aqui, se você quiser?"
        show jenny f_visit_after_normal_talk
        jen "Por amor de foda..."
        jen "Nós já não superamos isso?"
    show jenny f_visit_after_normal

    if store._in_replay is not None:
        $ player.location = L_home_bedroom
    scene expression player.location.background_closeup with None
    show jenny b_naked a_naked_side f_normal o_empty at Position (xpos=100)
    show player b_underwear a_naked_sides f_skeptical_talk at flip
    with dissolve
    if M_jenny.is_state(S_jenny_night_time_sex):
        player_name "Espere!"
    else:
        player_name "Tudo bem, tudo bem.."
    show player f_worried
    hide jenny
    if M_jenny.is_state(S_jenny_night_time_sex):
        $ M_jenny.trigger(T_jenny_didnt_sleep_much)
        show jenny b_naked a_naked_crossed f_upset_talk at flip
        with dissolve
        jen "o que, {b}[firstname]{/b}?!"
        show jenny f_upset
        show player f_worried_talk
        player_name "Eu não estava tentando"
        player_name "{b}*Suspiro*{/b} Apenas explique isso para mim..."
        show player f_skeptical_talk
        player_name "Então, podemos fazer sexo sempre que quisermos, mas você não vai dormir na minha cama?"
        show player f_worried
        show jenny f_eyeroll
        jen "Umm, não ... Nós podemos fazer sexo sempre {b}{i}I{/i}{/b} quer..."
        show jenny f_upset_talk
        jen "... Contanto que não interfira com as minhas camshows."
        show jenny f_upset
        pause
        show jenny f_upset_talk
        jen "... E não, eu não vou dormir na sua cama!"
        jen "{b}Eu não sou sua namorada e você com certeza não é meu namorado{/b}!"
        jen "Tire isso do seu crânio grosso, manequim!"
        show jenny f_upset
        show player f_skeptical_talk
        player_name "Eu não entendo você de jeito nenhum..."
        show player f_skeptical
        show jenny f_upset_talk
        jen "Sim, bem ... Você não precisa {i}de{/i} mim."
        jen "É assim que as coisas são."
        jen "Lide com isso."
        show jenny f_upset
        player_name "..."
    else:
        show jenny b_naked a_naked_crossed f_upset at flip
        with dissolve
        show player f_skeptical_talk
        player_name "Apenas esqueça que eu disse qualquer coisa."
        show player f_skeptical
        show jenny f_upset_talk
        jen "Com prazer."
        show jenny f_upset
        pause
    show jenny f_upset_talk
    jen "Agora vá dormir!"
    show jenny f_grin_talk
    jen "Meus fãs estão esperando um bom show amanhã."
    hide jenny with dissolve
    pause
    show player f_worried
    player_name "..."
    scene black with fade
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["12_unlocked"] = True
    jump resume_sleeping_bedroom

label jenny_sex_intro_repeat:
    show player f_worried_talk
    player_name "Sexo. Por favor."
    show player f_worried
    show jenny f_upset_talk
    jen "Se apresse."
    show jenny f_grin_down b_pull1 a_empty with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show player f_surprised
    pause
    show jenny b_panties a_naked_hips f_upset with dissolve
    show jenny f_upset_talk
    jen "Bem?"
    player_name "Hmm?"
    jen "Get those clothes off!"
    show jenny b_naked f_grin_down a_naked_panties_remove with dissolve
    show player f_worried_talk
    player_name "Certo..."
    show player b_dressed_changing a_empty f_empty
    show jenny b_cheer_dress1 f_empty a_empty
    with dissolve
    pause
    show jenny b_cheer_dress3 f_grin_down with dissolve
    pause
    show jenny b_cheer_dress2 f_empty with dissolve
    show player f_worried_talk b_shorts a_naked_sides with dissolve
    player_name "Você vai usar isso de novo?"
    show player f_worried
    show jenny b_cheer a_cheer_hips f_sexy_talk with dissolve
    jen "Claro!"
    jen "Meus fãs gostam disso."
    show jenny f_sexy
    show player b_dressed_changing2 a_empty f_empty with dissolve
    player_name "..."
    show player b_underwear a_naked_sides f_worried with dissolve
    show jenny f_sexy_talk
    jen "Fique na cama."
    show jenny f_sexy
    hide player with dissolve
    pause
    show jenny f_sexy_talk
    jen "... E coloque sua máscara!"
    show jenny f_sexy
    label finger_blasting_sex:
    scene black with fade
    pause
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show player b_bed_jenny_sit a_empty f_jenny_bed_sit_shy_down of_jenny_bed_sit_mask at Position (align=(0,0))
    show jenny o_under_body_laptop o_naked_bed_belly_cheer b_naked_bed_bellytype a_empty f_bed_facing_comp_sexy_talk_down at Position (align=(0,0))
    with dissolve
    pause
    jen "Vocês meninos prontos para outro show?"
    show jenny f_bed_facing_comp_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_facing_comp_laugh
    jen "Hehehe!"
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Tudo bem, deixe-me preparar as coisas..."
    show jenny b_bed_climbing a_empty f_empty o_cheer_bed_climbing
    show player b_bed_jenny_laying_undies_arms f_empty a_empty of_bed_jenny_laying_undies_arms_mask
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick7.png" zorder 2
    show expression "characters/jenny/layeredimage/jenny_overlay_o_laptop.png"
    with dissolve
    jump jenny_cheer_sex_intro_prepare

label jenny_cheer_sex_intro_prepare:
    player_name "Nós realmente vamos"
    jen "Shh!"
    pause
    show jenny b_bed_back_sit o_cheer_bed_back
    show expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_handcuffs.png" zorder 1
    with dissolve
    player_name "Aww, vamos {b}[jen_name]{/b}!"
    player_name "Você sabe que eu odeio essas coisas..."
    show jenny a_bed_back_sit_tie
    hide expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_handcuffs.png"
    show expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_tie.png" zorder 1
    show player oh_bed_jenny_laying_undies_handcuffs
    with dissolve
    jen "Cale a boca!"
    if M_jenny.get("dominance") <= 0:
        player_name "..."
        pause
        show jenny a_bed_back_sit_hips
        hide expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_tie.png"
        show expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_hips.png" zorder 1
        with dissolve
        if M_jenny.finished_inclusive(S_jenny_end) or store._in_replay:
            jen "E se você os odeia tanto, pare de gemer sobre eles e fazer algo."
            jen "Eles são apenas de plástico, tenho certeza que os meninos adorariam ver você tentar e se libertar!"
        else:
            jen "Bom."
        jen "Agora, implore por isso."
        player_name "O que?!"
        jen "Você quer que eu pegue seu grande pau para um passeio, não é?"
        player_name "Sim..."
        jen "Então você vai me implorar por isso, na frente dos meus fãs!"
        player_name "..."
        jen "Continue!"
        player_name "Por favor..."
        jen "Princesa!"
        player_name "..."
        player_name "Por favor, {b}Princesa [jen_name]{/b}..."
        "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
        jen "HAHAHAAH!"
        show jenny b_bed_front_sit a_bed_front_sit_pull1 f_bed_front_sit_sexy_down o_cheer_bed_front_sit2
        hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick7.png"
        hide expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_hips.png"
        show jenny a_bed_front_sit_pull1
        with dissolve
        pause
        show jenny a_bed_front_sit_pull2 f_bed_front_sit_sexy_talk_down o_cheer_bed_front_sit3 with dissolve
        jen "Vocês meninos prontos?"
    else:
        player_name "Eu não gosto deles!"
        jen "SEGURE FIRME!"
        player_name "Grr!"
        jen "Eu estou no comando aqui, não você!"
        "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
        show jenny a_bed_back_sit_hips
        hide expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_tie.png"
        show expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_hips.png" zorder 1
        with dissolve
        jen "Lá!"
        jen "Eu não sei do que você está reclamando..."
        show jenny b_bed_front_sit a_bed_front_sit_pull1 f_bed_front_sit_sexy_talk_down o_cheer_bed_front_sit2
        hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick7.png"
        hide expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_hips.png"
        show jenny a_bed_front_sit_pull1
        with dissolve
        jen "Aqui estou eu, me oferecendo para foder seus miolos e você está choramingando sobre algemas estúpidas!"
        show jenny a_bed_front_sit_pull2 o_cheer_bed_front_sit3 with dissolve
        jen "Vocês garotos não brigariam, você faria?!"
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    show jenny a_bed_front_sit_sides f_bed_front_sit_sexy_down o_cheer_bed_front_sit
    with dissolve
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_front_sit_sexy_talk_down
    jen "Heh, eles estão animados..."
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg"
    show jenny_cheer_sex tied insert
    with fade
    jen "( Aqui vamos nós, {b}[firstname]{/b}...Esse e o momento que você sonhou! )"
    jen "Ohh!"
    jen "Puta merda!"
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .09)
    show expression AnimatedImage("jenny_cheer_sex_tied_mask", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
    jen "Oh meu deus..."
    jen "Este é um pau muito grande!"
    jump jenny_cheer_sex_loop_tied

label jenny_cheer_sex_loop_tied:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_jenny.get("cam show mask"):
                    show expression AnimatedImage("jenny_cheer_sex_tied_mask", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression AnimatedImage("jenny_cheer_sex_tied", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_cheer_sex_hscene_dialog_tied")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
            $ poses_done = []
            while poses_done != pose_list:
                if M_jenny.get("cam show mask"):
                    show expression "jenny_cheer_sex_tied_mask {}".format(pose_list[pose_counter]) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression "jenny_cheer_sex_tied {}".format(pose_list[pose_counter]) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_cheer_sex_hscene_dialog_tied")
        $ animcounter += 1
    call screen jenny_cheer_sex_options_tied

label jenny_cheer_sex_hscene_dialog_tied:
    if animcounter == 0 and randomizer() < 10:
        jen "Ahh!{p=1}{nw}"
    if animcounter == 0 and randomizer() < 10:
        jen "Isso é tão bom pra caralho!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jen "A, fode!{p=1}{nw}"
        jen "Eu vou esguichar esse pau grande!{p=2}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jen "Mmm, FODE!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jen "É tão bom!!{p=1}{nw}"
        player_name "I'm getting close!{p=1}{nw}"
        jen "TÃO FODA DE BOM!!{p=1}{nw}"
        player_name "{b}[jen_name]{/b}!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        player_name "Você é muito boa nisso!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 5:
        jen "Você gosta disso, não é?!{p=1}{nw}"
        player_name "Sim.{p=1}{nw}"
        jen "Me diga que você gostou!{p=1}{nw}"
        player_name "I like it!{p=1}{nw}"
        jen "Me diga que você ama minha buceta!{p=1}{nw}"
        player_name "Ah, eu amo isso!{p=1}{nw}"
        jen "Hahahaah!{p=1}{nw}"
        if M_jenny.get("sex speed") > 0.031:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.03)
        jen "Mmm, Sim!{p=1}{nw}"
    return

label jenny_cheer_sex_cum_inside_tied:
    if M_jenny.is_state(S_jenny_cheerleader_sex):
        player_name "I can't hold it!"
    else:
        player_name "Sai fora!"
    pause
    player_name "{b}[jen_name]{/b}!!!"
    jen "NGGHHH!!!"
    player_name "Eu não posso"
    pause
    show jenny_cheer_sex tied cum
    player_name "HNNGGG!!!" with flash
    show jenny_cheer_sex tied cum 2
    show xray_jenny_cheer_bedroom at Position (align=(0,0))
    pause
    call call_pregnancy_minigame ("jenny_cheer_sex_cum_inside_tied_post_pregnancy", M_jenny)

label jenny_cheer_sex_cum_inside_tied_post_pregnancy:
    hide screen pregnancy_minigame
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg"
    show jenny_cheer_sex tied pullout 1
    with fade
    jen "Haah... Haaah..."
    show jenny_cheer_sex tied pullout 2 with dissolve
    jen "Pooorra, isso foi incrivel-"
    show jenny_cheer_sex tied pullout 3 with dissolve
    jen "!!!"
    show jenny_cheer_sex tied pullout 4 with dissolve
    if M_jenny.is_state(S_jenny_cheerleader_sex):
        jen "Você gozou dentro de mim?!"
        player_name "Você me disse para não parar..."
        jen "Sim, mas eu não disse para terminar dentro de mim seu idiota!"
        player_name "Me desculpe, eu não queria"
        jen "E se eu engravidar?!"
        player_name "..."
    else:
        jen "Você gozou dentro de mim?!"
        player_name "Eu te avisei!"
        jen "Eu não ouvi nada!"
        player_name "Bem, o que você quer que eu faça?!"
        player_name "Estou algemado na sua cama!"
        jen "E se eu engravidar seu idiota!"
        player_name "Então você deveria ter descido quando eu te avisei!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "Oh porra tudo bem..."
    jump jenny_cheer_sex_aftermath

label jenny_cheer_sex_cum_outside_tied:
    player_name "Vou gozar!"
    jen "Segure isso!"
    player_name "O que?! Não funciona assim!"
    jen "Estou tão perto!"
    player_name "{b}[jen_name]{/b}!!!"
    jen "PORRA!!"
    show jenny_cheer_sex tied cumshot
    show jenny_cheer_sex_mc tied cumshot initial
    player_name "HNNGGG!!!" with flash
    show jenny_cheer_sex_mc tied cumshot
    pause
    player_name "Haah... Haah..."
    jen "Você não poderia ter durado mais dez segundos?!"
    if randomizer() > 50:
        player_name "Sinto muito."
    else:
        player_name "É difícil quando estou algemado na cama!"
    jen "Tanto faz..."
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "Porra tudo bem..."
    jump jenny_cheer_sex_aftermath

label jenny_cheer_sex_break_free:
    if player.has_required_str(7) or store._in_replay is not None:
        show jenny_cheer_sex free break
        jen "!!!" with hpunch
        $ animated = True
        $ anim_toggle = True
        $ M_jenny.set('sex speed', .08)
        if M_jenny.get("cam show mask"):
            show expression AnimatedImage("jenny_cheer_sex_free_mask", [1,2,3,4,5], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
        else:
            show expression AnimatedImage("jenny_cheer_sex_free", [1,2,3,4,5], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
        jen "OH FODA!!{p=1}{nw}"
        pause 1
        jen "Ó MEUDEUS, Ó MEUDEUS, Ó MEUDEUS!!!{p=1}{nw}"
        pause 1
        jen "AHHH!!!{p=1}{nw}"
        "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}{p=1}{nw}"
        pause 1
        jen "FOOODE MEEEE!!!{p=1}{nw}"

        label jenny_cheer_sex_loop_free:
            show screen sex_anim_buttons
            pause
            hide screen sex_anim_buttons
            $ animcounter = 0
            while animcounter < 4:
                if anim_toggle:
                    if not animated:
                        if M_jenny.get("cam show mask"):
                            show expression AnimatedImage("jenny_cheer_sex_free_mask", [1,2,3,4,5], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                        else:
                            show expression AnimatedImage("jenny_cheer_sex_free", [1,2,3,4,5], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                        $ animated = True
                    pause 5
                    call expression game.dialog_select("jenny_cheer_sex_hscene_dialog_free")
                    pause 3
                else:

                    $ pose_counter = 0
                    $ pose_list = [1,2,3,4,5]
                    $ poses_done = []
                    while poses_done != pose_list:
                        if M_jenny.get("cam show mask"):
                            show expression "jenny_cheer_sex_free_mask {}".format(pose_list[pose_counter]) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                        else:
                            show expression "jenny_cheer_sex_free {}".format(pose_list[pose_counter]) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                        pause
                        $ poses_done.append(pose_list[pose_counter])
                        $ pose_counter += 1
                    call expression game.dialog_select("jenny_cheer_sex_hscene_dialog_free")
                $ animcounter += 1
            call screen jenny_cheer_sex_options_free

        label jenny_cheer_sex_hscene_dialog_free:
            if animcounter == 0 and randomizer() < 30:
                jen "OH FODE!!{p=1}{nw}"
            if animcounter == 1 and randomizer() < 10:
                jen "FODA-ME!{p=.5}{nw}"
                jen "FODA-ME!{p=.5}{nw}"
                jen "FOOODE MEEEE!!!{p=1}{nw}"
            if animcounter == 2 and randomizer() < 30:
                jen "AHHH!!!{p=1}{nw}"
            return
    else:

        jen "[str_warn]Oh meu Deus!{p=1}{nw}"
        pause 1
        jen "[str_warn]Foda-me!{p=1}{nw}"
        pause 1
        jen "[str_warn]Foda-me!!{p=1}{nw}"
        jump jenny_cheer_sex_loop_tied

label jenny_cheer_sex_cum_inside_free:
    player_name "Estou chegando perto de gozar!"
    pause
    jen "Não pare!"
    player_name "{b}[jen_name]{/b}, Eu não posso"
    jen "NÃO PARE!"
    pause
    jen "NGGHHH!!!"
    show jenny_cheer_sex free cum
    player_name "HNNGGG!!!" with flash
    show jenny_cheer_sex free cum 2
    show xray_jenny_cheer_bedroom at Position (align=(0,0))
    pause
    call call_pregnancy_minigame ("jenny_cheer_sex_cum_inside_free_post_pregnancy", M_jenny)

label jenny_cheer_sex_cum_inside_free_post_pregnancy:
    hide screen pregnancy_minigame
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg"
    pause
    show jenny_cheer_sex free pullout 1 with dissolve
    jen "Haah... Haaah..."
    show jenny_cheer_sex free pullout 2 with dissolve
    jen "Puta merda, isso foi incrivel"
    show jenny_cheer_sex free pullout 3 with dissolve
    jen "!!!"
    show jenny_cheer_sex free pullout 4 with dissolve
    jen "Você gozou dentro de mim?!"
    player_name "Você me disse para não parar..."
    jen "Eu não quis dizer para você gozar dentro de mim, idiota!"
    player_name "Não comece com o nome chamando..."
    jen "E se eu engravidar?!!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "A Merda tudo bem..."
    jump jenny_cheer_sex_aftermath

label jenny_cheer_sex_cum_outside_free:
    player_name "Estou chegando perto de gozar!"
    pause
    jen "Não pare!"
    player_name "{b}[jen_name]{/b}, Eu não posso"
    jen "NÃO PARE!"
    pause
    jen "NGGHHH!!!"
    show jenny_cheer_sex free cumshot
    show jenny_cheer_sex_mc tied cumshot initial
    player_name "HNNGGG!!!" with flash
    show jenny_cheer_sex_mc tied cumshot
    pause
    player_name "Haah... Haah..."
    jen "Que porra, eu te disse para não parar!!"
    player_name "O que você quer que eu goze dentro de você?!"
    jen "Não, apenas ... Me senti muito bem se "
    jen "{b}*Suspiro*{/b} deixa pra lá..."
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "Boa foda..."
    jen "O show acabou, pervertidos!"
    jen "Espero vocês na próxima vez!"
    jump jenny_cheer_sex_aftermath

label jenny_cheer_sex_aftermath:
    scene expression player.location.background_closeup with None
    show jenny f_upset b_cheer a_cheer_hips
    show player f_normal_talk b_underwear a_naked_sides
    with dissolve
    player_name "Isso foi demais!"
    show player f_normal
    show jenny f_eyeroll
    jen "Sim, tanto faz."
    show jenny f_upset_talk
    jen "Você se saiu bem."
    show player f_worried
    jen "Agora saia!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Não podemos apenas-"
    show player f_worried
    show jenny f_upset_talk a_cheer_hips_money
    jen "Não, pegue seu dinheiro estúpido e saia!"
    hide jenny with dissolve
    show player f_worried_talk
    player_name "Tudo bem, sheesh..."
    hide player with dissolve
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player f_grin with dissolve
    player_name "( Eu acabei de fazer sexo com {b}[jen_name]{/b}... )"
    player_name "( Na frente da câmera com centenas de pessoas assistindo! )"
    pause
    player_name "( Quão louco é isso?! )"
    player_name "( Espero que façamos de novo. )"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["11_unlocked"] = True
    call screen money_popup(amount=200)
    $ M_jenny.trigger(T_jenny_had_cheerleader_sex)
    $ player.get_money(200)
    $ game.timer.tick()
    $ player.go_to(L_home_hallway)
    $ game.main()

label jenny_cunni_intro_repeat:
    show player f_worried_talk
    player_name "Então vai ter camshow hoje?"
    show player f_worried
    show jenny f_upset_talk
    jen "Não, não estou de bom humor..."
    show jenny f_upset
    show player f_worried_talk
    player_name "O que?!"
    player_name "Você está sempre de mal humor."
    show player f_worried
    show jenny f_upset_talk
    jen "Para ser estupido, idiota!"
    jen "Eu não estou com vontade de ficar estupefato!"
    show jenny f_upset
    show player f_laugh
    player_name "Oh heh Peguei você."
    show player f_normal
    show jenny f_upset_talk
    jen "Preciso de um dia de folga..."
    show jenny f_upset
    show player f_grumpy_talk at flip
    show player at Position (xpos=-100)
    with dissolve
    player_name "Eu vou deixar você sozinha então."
    show player f_grumpy
    show jenny f_upset_talk
    jen "Espere."
    show jenny f_upset
    hide player
    show player f_normal
    with dissolve
    player_name "..."
    show jenny f_grin_talk
    jen "Já que você já está aqui..."
    show jenny f_grin
    show player f_worried
    player_name "Hmm?"
    show jenny f_grin_talk
    jen "Vamos lá."
    hide jenny
    hide player
    with dissolve
    label finger_blasting_cunni:
    scene expression "backgrounds/location_home_hallway_cutscene.jpg" with dissolve
    player_name "Onde estamos indo?!"
    jen "Eu acho que você precisa de mais prática..."
    player_name "Por que estamos indo para o meu quarto?!"
    jen "Cale a boca!"
    $ player.go_to(L_home_bedroom)
    scene expression player.location.background_closeup with None
    show player f_worried
    show jenny b_dressed_panties_remove_down a_empty f_empty
    with dissolve
    pause
    show player f_worried_talk
    show jenny b_pantieless a_dressed_hips f_grin with dissolve
    player_name "O que você está fazendo?"
    show player f_worried
    show jenny f_grin_talk
    jen "Você vai lamber minha buceta."
    show jenny f_grin
    if M_jenny.get("dominance") <= 0:
        show player f_worried_talk
        player_name "Eu vou?"
        show player f_worried
        show jenny f_grin_talk
        jen "Sim."
        jen "Vamos, perdedor!"
        jen "Eu vou gozar nessa sua boca!"
    else:
        show player f_worried_talk
        player_name "Mesmo"
        show player f_worried
        show jenny f_grin_talk
        jen "Sim."
        show jenny f_grin
        show player f_worried_talk
        player_name "Talvez se você me perguntar com jeitinho."
        show player f_worried
        show jenny f_upset_talk
        jen "Ugh, você ainda está preso nessa merda?!"
        show jenny f_upset
        show player f_skeptical_talk
        if randomizer() > 50:
            player_name "Se você quer voltar a se masturbar, se prepare..."
        else:
            player_name "Eu não sou seu pequeno chicoteador, {b}[jen_name]{/b}..."
        show player f_skeptical
        show jenny f_upset_talk
        jen "Grr, Você é uma dor na bunda!"
        jen "Bem."
        show jenny f_angry_pouting a_dressed_crossed with dissolve
        pause
        show jenny f_upset_talk
        jen "{b}[firstname]{/b}, você poderia por favor lamber minha buceta?"
        show jenny f_upset
        show player f_laugh
        player_name "Haha, sure!"
        show player f_skeptical
        show jenny f_eyeroll
        jen "Apenas vamos!"
    jump jenny_cunni_repeat


label jenny_cunni_repeat:
    scene bedroom_sex2
    if M_jenny.is_state(S_jenny_give_cunni):
        show jennysex 135 at right
    else:
        show jennysex 137 at right
    show jennysex_cunnilingus_player at right
    with fade
    if M_jenny.is_state(S_jenny_give_cunni):
        jen "Hehe, lembra que gozou você atirou em todo o meu consolador?!"
        jen "É tempo de retorno, cadela!"
        show jennysex 134
        player_name "Ei, eu lavei para você!"
        show jennysex 135
        jen "Hahaha!"
        show jennysex 137 with dissolve
    pause
    show jennysex 137b
    jen "Bem, o que você está esperando, um convite?!"
    jen "Lamber minha buceta"
    $ M_jenny.set('sex speed', .3)
    show expression AnimatedImage("jenny_lick_shirt", [1,2,3,4], M_jenny) as jennysex at Position(xalign = 0.0, yoffset = 0)
    hide jennysex_cunnilingus_player
    with fastdissolve
    jen "EEyyyy!!!"
    pause
    jen "Fooooda!"
    pause
    jen "Mmm, sua língua parece incrível!"
    jen "Ahh!"
    pause
    show jennysex 135
    show jennysex_cunnilingus_player at right
    with dissolve
    jen "Concentre-se no meu clitóris mais, manequim!"
    jen "... E brinque com minhas mamas também!"
    show jennysex 134
    if M_jenny.get("dominance") <= 0:
        player_name "Tudo bem."
        show jennysex 135
        jen "{b}*Ahem*{/b} Tudo bem, o que?"
        show jennysex 134
        player_name "{b}*Suspiro*{/b} Tudo bem, {b}Princesa Jenny{/b}..."
        show jennysex 135
        jen "Hahaha!"
        jen "Isso mesmo, perdedor!"
    else:
        player_name "Peça com jeitinho estou parando..."
        show jennysex 135
        jen "O que?!"
        jen "Oh meu deus, você não pode parar agora!"
        show jennysex 134
        player_name "Veja."
        show jennysex 135
        jen "Não não não!"
        show jennysex 134
        jen "Grr!"
        show jennysex 135
        jen "Por favor, brinque com meus peitos, {b}[firstname]{/b}..."
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .2)
    show expression AnimatedImage("jenny_lick", [1,2,3,4], M_jenny) as jennysex at Position(xalign = 0.0, yoffset = 0)
    hide jennysex_cunnilingus_player
    with dissolve
    jump jenny_lick_loop

label jenny_lick_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_lick", [1,2,3,4], M_jenny) as jennysex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_lick_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_lick {}".format(pose_list[pose_counter]) as jennysex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_lick_hscene_dialog")
        $ animcounter += 1
    call screen jenny_lick_options

label jenny_lick_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jen "!!!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jen "isso!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jen "Bem desse jeito.{p=1}{nw}"
        jen "Simmm!!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        jen "Mmm, Estou chegando perto de gozar!{p=2}{nw}"
    return

label jenny_lick_cum:
    jen "Eu vou"
    jen "Oh foda!"
    pause
    show jennysex 143
    jen "NGGHHH!!!" with flash
    show jennysex 135c
    show jennysex_cunnilingus_player at right
    with dissolve
    jen "Haah... Haah..."
    show jennysex 134c
    player_name "Sheesh, você me encharcou."
    pause
    show jennysex 135c
    jen "Psh Você gosta disso!"
    show jennysex 134c
    player_name "Ok, certo..."
    show jennysex 135c
    jen "Hehehe!"
    hide jennysex
    hide jennysex_cunnilingus_player
    with dissolve
    scene expression player.location.background_closeup with None
    show jenny f_normal_talk b_pantieless
    show player f_worried
    with dissolve
    jen "Ufa, tudo bem ... Isso foi muito bom."
    show jenny f_normal
    show player f_worried_talk
    player_name "Sim, para você."
    show player f_worried
    show jenny f_laugh
    jen "Hahaha!"
    show jenny f_normal_talk
    jen "Não se preocupe, eu cuidarei de você mais tarde."
    show jenny f_grin_talk
    jen "Talvez..."
    show jenny f_grin
    pause
    show jenny f_grin_talk
    jen "... Se você é um bom menino."
    show jenny f_grin
    show player f_worried_talk
    player_name "Vamos lá, {b}[jen_name]{/b}..."
    show player f_worried
    show jenny f_upset_talk
    jen "Não."
    show jenny f_grin_talk
    jen "Além disso, você não tem roupa para lavar?!"
    show jenny f_grin
    show player f_grumpy
    player_name "..."
    show jenny f_grin_talk a_pantieless_panties with dissolve
    jen "Mais tarde, perdedor!"
    hide jenny with dissolve
    jen "Hahahaah!"
    show player f_unimpressed_talk
    player_name "{b}*Suspiro*{/b}"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["10_unlocked"] = True
    $ player.go_to(L_home_bedroom)
    $ game.timer.tick()
    $ M_jenny.trigger(T_jenny_gave_cunni)
    $ game.main()


label jenny_bj_intro_repeat:
    show player f_worried_talk
    player_name "Oral."
    show player f_worried
    show jenny f_upset_talk
    jen "Se apresse."
    show jenny f_grin_down b_pull1 a_empty with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show player f_surprised
    pause
    show jenny b_panties a_naked_hips f_upset with dissolve
    show jenny f_upset_talk
    jen "Bem?"
    player_name "Hmm?"
    jen "Tire essas roupas!"
    show jenny f_grin_down b_naked a_naked_panties_remove with dissolve
    show player f_worried_talk
    player_name "Certo..."
    show player f_worried
    show jenny b_naked_panties_remove_down a_empty f_empty with dissolve
    pause
    label finger_blasting_bj:
    scene black with fade
    pause
    scene expression "backgrounds/location_home_jennybedroom_cutscene05.jpg" with dissolve
    jen "Você sabe o que fazer."
    jen "Lembra Mascara e mantenha sua boca fechada."
    player_name "Sim, eu me lembro."
    jen "Eu vou lidar com o resto."
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show player b_bed_jenny_sit a_empty f_jenny_bed_sit_shy_down of_jenny_bed_sit_mask at Position (align=(0,0))
    show jenny o_under_body_laptop b_naked_bed_bellytype a_empty f_bed_facing_comp_sexy_talk_down at Position (align=(0,0))
    with dissolve
    jen "Oi de novo, pessoal!"
    jen "Eu trouxe meu brinquedinho de volta para dar a vocês um outro show."
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_laugh
    jen "Hehe, claro!"
    show jenny b_bed_climbing a_empty f_empty
    show player b_bed_jenny_laying_undies_arms f_empty a_empty of_bed_jenny_laying_undies_arms_mask od_bed_jenny_laying_dick1
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick1.png"
    with dissolve
    pause
    show jenny b_bed_back_sit a_bed_back_sit_handcuffs with dissolve
    player_name "Algemas de novo?!"
    show jenny a_bed_back_sit_tie
    show player oh_bed_jenny_laying_undies_handcuffs
    with dissolve
    jen "Shh!"
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick1.png"
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick7.png"
    with dissolve
    player_name "{b}[jen_name]{/b}, Eu não quero"
    jen "Cale-se!"
    show jenny b_bed_back_look a_bed_back_look_up f_bed_back_look_normal_talk with dissolve
    jen "Lá."
    jen "Vamos ver se o seu amigo está acordado, hmm?"
    show jenny b_bed_front_sit a_bed_front_sit_sides f_bed_front_sit_sexy_down with dissolve
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick7.png"
    show jenny a_bed_front_sit_pull1
    with dissolve
    pause
    show jenny a_bed_front_sit_pull2 with dissolve
    jen "!!!"
    show jenny f_bed_front_sit_sexy_talk_down
    jen "Olá grande amigo."
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    show player od_bed_jenny_laying_dick6
    show jenny b_bed_front_laying a_empty f_bed_front_laying_sexy_talk_down
    with dissolve
    jen "Vocês rapazes prontos para se divertir?"
    show jenny f_bed_front_laying_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    player_name "O que nós vamos"
    show jenny b_bed_pussy1 f_bed_pussy1_sexy_down
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    player_name "!!!" with hpunch
    player_name "Mrphmmmll-"
    show jenny f_bed_pussy1_sexy_talk_down
    jen "O que foi isso, garoto brinquedo?"
    jen "Nós não podemos te ouvir... Hahahaah!"
    show player od_empty
    show jenny b_bed_pussy f_bed_pussy_sexy_down
    with dissolve
    pause
    show jenny f_bed_pussy_sexy_talk_down
    jen "Mmm, porra sim!"
    show jenny f_bed_pussy_sexy_down
    pause
    show jenny f_bed_pussy_nipple2
    jen "Ahh!"
    show jenny f_bed_pussy_nipple3
    pause
    show jenny f_bed_pussy_nipple2
    jen "Você é tão bom nisso!"
    show jenny f_bed_pussy_nipple3
    player_name "Errmmhnnn!"
    show jenny f_bed_pussy_nipple2
    jen "Hahaha!"
    show jenny f_bed_pussy_nipple3
    pause
    show jenny f_bed_pussy_nipple2
    jen "Estou chegando perto de gozar!"
    show jenny f_bed_pussy_nipple3
    pause
    show jenny f_bed_pussy_nipple2
    jen "Oh, Deus!"
    jen "Assim!!"
    show jenny f_bed_pussy_nipple3
    pause
    show jenny b_bed_pussy1 f_bed_pussy1_nipple2
    jen "NGGHHH!!!" with flash
    pause
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    show jenny b_bed_front_laying a_empty f_bed_front_laying_nipple2
    show player od_bed_jenny_laying_dick6
    with dissolve
    jen "Haah... Haaah..."
    player_name "{b}*Gasp*{/b}"
    player_name "{b}*Cough* *Sputter* *Cough*{/b}"
    player_name "Droga, {b}[jen_name]{/b}!"
    player_name "Você sabe que eu não posso respirar quando você faz isso!"
    show jenny f_bed_front_laying_laugh
    jen "Hehehe!"
    show jenny f_bed_front_laying_sexy_down
    player_name "Não é engraçado!"
    show jenny f_bed_front_laying_sexy_talk_down
    jen "Oh, Cale-se..."
    jen "Meus fãs não querem ouvir sua putaria."
    show jenny f_bed_front_laying_sexy_down
    pause
    show jenny f_bed_front_laying_sexy_talk_down
    jen "Sério?"
    show jenny f_bed_front_laying_sexy_down
    pause
    show jenny f_bed_front_laying_eyeroll
    jen "{b}*Suspiro*{/b} Novamente?!"
    show jenny f_bed_front_laying_sexy_down
    pause
    show jenny f_bed_front_laying_sexy_talk_down
    jen "Bem, eu não vou fazer isso a menos que vocês-"
    show jenny f_bed_front_laying_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_front_laying_surprised_down_talk
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "Por amor de foda..."
    show jenny f_bed_front_laying_sexy_down
    player_name "Agora o que está acontecendo?"
    show jenny f_bed_front_laying_sexy_talk_down
    jen "Você está prestes a ter seu pau sugado novamente."
    show jenny f_bed_front_laying_sexy_down
    player_name "Mesmo?"
    player_name "Isso é incrivel-"
    show jenny b_bed_pussy1 f_bed_pussy1_sexy_down
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    with dissolve
    player_name "Srrrmmmph!"
    show jenny f_bed_pussy1_sexy_talk_down
    jen "Cale-se!"
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg" with None
    show expression AnimatedImage("jenny_bj", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_bj at Position(xalign = 0.0, yoffset = 0)
    player_name "Nnnrrrmmph-" with hpunch
    jen "{b}*Gluullggh*{/b}"
    jump jenny_bj_loop

label jenny_bj_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_bj", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_bj at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_bj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_bj {}".format(pose_list[pose_counter]) as jenny_bj at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_bj_hscene_dialog")
        $ animcounter += 1
    call screen jenny_bj_options

label jenny_bj_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        jen "Mmm.{p=1}{nw}"
    if animcounter == 1 and randomizer() > 50:
        jen "{b}*Slurp*{/b}{p=1}{nw}"
    if animcounter == 2 and randomizer() < 50:
        player_name "...{p=1}{nw}"
    if animcounter == 3 and randomizer() > 50:
        jen "{b}*Slurrrrrp*{/b}{p=1}{nw}"
    return

label jenny_bj_cum:
    player_name "Jrrnnnneeeee!"
    player_name "mmy grrn krrrwwws!!"
    pause
    player_name "Jrrnnnneeeee!!!"
    pause
    show jenny_bj cum
    player_name "HrrrNNGGG!!!" with flash
    jen "!!!"
    pause
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    show player b_bed_jenny_laying_undies_arms f_empty a_empty of_bed_jenny_laying_undies_arms_mask oh_bed_jenny_laying_undies_handcuffs od_bed_jenny_laying_dick3 at Position (align=(0,0))
    show jenny b_bed_front_sit a_bed_front_sit_shocked f_bed_front_sit_cheeks_surprised o_laptop at Position (align=(0,0))
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick3.png"
    with dissolve
    jen "{b}*Gulp*{/b}"
    show jenny f_bed_front_sit_cheeks_angry
    jen "{b}*Cough* *Sputter* *Cough*{/b}"
    if M_jenny.is_state(S_jenny_start_camshow_blowjob):
        show jenny b_bed_back_sit f_empty a_bed_back_sit_hips with dissolve
        jen "Deus Droga!!"
        jen "Você gozou bem na minha maldita garganta!"
        show jenny b_bed_climbing a_empty with dissolve
        jen "Eu engoli um monte disso!"
        show jenny b_bed_side f_bedside_angry a_bed_side_laptop with dissolve
        player_name "Eu tentei te avisar..."
        show jenny f_bedside_angry_talk
        jen "Mentira, eu não ouvi nada!"
        show jenny f_bedside_angry
        player_name "Sim, provavelmente porque você estava se esfregando no meu rosto!"
        show jenny f_bedside_angry_talk
        jen "Tanto faz..."
        show jenny b_bed_side_laptop f_bedside_laptop_gross_down with dissolve
        pause
        show jenny f_bedside_laptop_gross_down_talk
        jen "Grr, não é engraçado!"
        jen "É nojento!"
        show jenny f_bedside_laptop_gross_down
        pause
        show jenny f_bedside_laptop_gross_down_talk
        jen "Ugh, vocês são todos idiotas!"
        jen "Show ACABOU!"
        show jenny f_bedside_laptop_gross_down
        scene black with fade
        pause
        scene expression player.location.background_closeup with None
        show jenny b_naked a_naked_hips f_angry_talk
        show player 101e at left
        with dissolve
        jen "Inacreditável!"
        show jenny f_angry
        show player 101
        player_name "Eu realmente tentei avisar-"
        show player 101e
        show jenny f_angry_talk
        jen "Eu não quero ouvir nada!"
        jen "Apenas cale a boca!"
        show jenny f_gross_down_talk
        jen "Eu tenho que ir escovar os dentes!"
        hide jenny with dissolve
        pause
        show player 101g
        player_name "Ei, e meu dinheiro?!"
        show player 100
        pause
        player_name "( Hmm, Eu acho que vou perguntar a ela sobre isso amanhã. )"
        $ M_jenny.trigger(T_jenny_done_camshow_blowjob)
    else:
        show jenny b_bed_back_sit f_empty a_bed_back_sit_hips with dissolve
        jen "Ufa, feliz agora?"
        player_name "Eu te avisei de novo!"
        jen "Eu sei."
        pause
        jen "Eu só não estava esperando muito..."
        show jenny b_bed_climbing a_empty with dissolve
        player_name "Espere, então você"
        show jenny b_bed_side_laptop f_bedside_laptop_sexy_talk_down a_bed_side_laptop with dissolve
        jen "Atè mais meninos!"
        jen "Obrigado por sintonizar!"
        show jenny f_bedside_laptop_sexy_down
        pause
        show jenny f_bedside_laptop_sexy_talk_down
        jen "Hehe, nos vemos na próxima!"
        show jenny f_bedside_laptop_sexy_talk_down
        scene black with fade
        pause
        scene expression player.location.background_closeup with None
        show jenny b_naked a_naked_hips f_normal
        show player 101c at left
        with dissolve
        player_name "Você engoliu de propósito?"
        show player 100c
        show jenny f_upset_talk
        jen "Sim?"
        show jenny f_upset
        show player 101e
        player_name "!!!"
        show jenny f_upset_talk
        jen "Não tenha idéias, é apenas o que os fãs querem ver..."
        show jenny f_upset
        show player 101c
        player_name "Hã."
        show player 100c
        show jenny f_upset_talk a_naked_money with dissolve
        jen "Aqui está o sua parte."
        call screen money_popup(amount=100)
        $ player.get_money(100)
        show jenny f_upset a_naked_side with dissolve
        show player 101c
        player_name "Obrigado."
        show player 100c
        show jenny f_angry_talk
        jen "Agora saia daqui!"
        hide jenny with dissolve
        jen "Eu preciso de um bochecho!"
        player_name "..."
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["09_unlocked"] = True
    $ player.go_to(L_home_hallway)
    $ game.timer.tick()
    $ game.main()

label jenny_couch_fj_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_couch_dick_rub", [1,2,3], M_jenny) as jenny_couch_dick_rub at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_couch_fj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_couch_dick_rub {}".format(pose_list[pose_counter]) as jenny_couch_dick_rub at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_couch_fj_hscene_dialog")
        $ animcounter += 1
    call screen jenny_couch_fj_options

label jenny_couch_fj_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        show jenny f_couch_sit_sexy_talk_down
        jen "É bom?{p=1}{nw}"
        show jenny f_couch_sit_sexy_down
        show player f_couch_sit_down_talk
        player_name "Sim.{p=1}{nw}"
        show player f_couch_sit_down
    if animcounter == 1 and randomizer() < 10:
        show jenny f_couch_sit_sexy_talk_down
        jen "Você está chegando perto?{p=1}{nw}"
        show jenny f_couch_sit_sexy_down
        show player f_couch_sit_down_talk
        player_name "Sim.{p=1}{nw}"
        show player f_couch_sit_down
    if animcounter == 2 and randomizer() < 10:
        show player f_couch_sit_right_talk
        if randomizer() > 50:
            player_name "Você é muito boa nisso!{p=2}{nw}"
        else:
            player_name "puta merda!{p=1}{nw}"
        show player f_couch_sit_down
        show jenny f_couch_sit_laugh
        jen "Hehehe!{p=1}{nw}"
        show jenny f_couch_sit_sexy_down
    return

label jenny_couch_fj_cum:
    if M_jenny.finished_state(S_jenny_catch_her_jilling):
        show player f_couch_sit_down_surprised
        player_name "Aqui vai!"
        pause
        show player f_couch_sit_down_surprised
    show player f_couch_sit_down_surprised
    hide jenny_couch_dick_rub
    show jenny a_couch_dick3
    player_name "HNNGGG!!!" with flash
    show jenny_player_couch_cum zorder 3 with dissolve
    show player f_couch_sit_down
    pause
    show player f_couch_sit_right
    show jenny f_couch_sit_laugh
    jen "Pfft, hahaha!"
    hide jenny_player_couch_cum
    show player a_couch_boner
    show jenny a_couch_after2 f_couch_sit_sexy_talk_down
    with dissolve
    if M_jenny.is_state(S_jenny_catch_her_jilling):
        $ M_jenny.trigger(T_jenny_gave_footjob)
        jen "Eu só fiz você gozar com meus pés!"
        jen "Eu sou como uma deusa do sexo total!!"
        show jenny a_couch_after1 f_couch_sit_sexy_down with dissolve
        show player f_couch_sit_right_talk
        player_name "Isso foi incrível!"
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk_down
        jen "Eu sei!"
        jen "De nada, perdedor."
        show jenny b_couch_transition f_empty a_empty zorder 0 with dissolve
        show player f_couch_sit_right_talk
        player_name "Onde você vai?"
        show player f_couch_sit_right
        show jenny b_couch_sit a_couch_rest f_couch_sit_sexy_talk with dissolve
        jen "Umm, lavar meus pés?"
        show jenny a_couch_after2 with dissolve
        jen "A menos que você queira limpá-los com sua língua?"
    else:
        jen "Sheesh, olhe para a bagunça que você fez nos meus lindos pezinhos!"
        jen "Tem certeza de que não quer limpá-los com sua língua?!"
    show jenny f_couch_sit_sexy a_couch_after1 with dissolve
    if M_jenny.get("dominance") <= 0:
        show player f_couch_sit_right_talk
        player_name "Por favor, não me faça fazer isso..."
        show player f_couch_sit_right
        show jenny f_couch_sit_laugh
        jen "Hahaha!"
        show jenny f_couch_sit_sexy_talk
        jen "Não faça perguntas estúpidas então."
    else:
        show player f_couch_sit_right_talk
        player_name "Eca, de jeito nenhum!"
        show player f_couch_sit_right
        show jenny f_couch_sit_laugh
        jen "Hahaha!"
        show jenny f_couch_sit_sexy_talk
        jen "Aww, vamos..."
        show jenny f_couch_sit_sexy a_couch_after2 with dissolve
        jen "Lambe meus dedos, {b}[firstname]{/b}!"
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "Esqueça!"
        show player f_couch_sit_right
        show jenny f_couch_sit_laugh
        jen "Hahaha!"
        show jenny f_couch_sit_sexy_talk
        jen "Està bem."
    jen "Vou tomar banho."
    jen "Te vejo, depois pervetido."
    hide jenny with dissolve
    show player f_couch_sit_down
    player_name "( Ufa, isso foi demais! )"
    show player b_couch_sit_watching f_couch_sit_watching_straight with dissolve
    player_name "( Eu deveria desligar isso e ir para a cama antes {b}[deb_name]{/b} ouve. )"
    hide player with dissolve
    $ renpy.end_replay()
    $ game.timer.tick()
    $ game.main()

label jenny_computer_video_1:
    scene expression "backgrounds/location_home_jennybedroom_cam1.jpg"
    show jenny b_cam_intro a_cam_intro_cover f_cam_intro_normal_talk
    show expression "characters/jenny/layeredimage/jenny_webcam_border.png"
    with dissolve
    jen "Desculpe meninos ... Esta próxima parte é apenas para assinantes."
    jen "É melhor você pagar rapidamente se não quiser perder!!"
    show jenny f_cam_intro_normal
    pause
    show jenny f_cam_intro_normal_talk a_cam_intro_reveal with dissolve
    jen "Hehe, tudo bem. Quem está pronto para ficar malcriado?"
    show jenny a_cam_intro_electro f_cam_intro_normal_talk_left with dissolve
    jen "Eu tenho um bom brinquedo novo aqui ... Só para vocês!"
    jen "Mmm, Eu não posso esperar para provocar meu clitóris com isso..."
    show jenny f_cam_intro_normal_left
    pause
    show jenny f_cam_intro_normal_talk
    jen "Por que vocês não me dão um pequeno incentivo?"
    show jenny f_cam_intro_normal_down
    "{b}*PING*{/b}"
    "{b}*PING*{/b}"
    show jenny f_cam_intro_normal_talk_down
    jen "Oh, Vamos agora ... Você pode fazer melhor que isso, não pode?"
    jen "Minha buceta está absolutamente doendo por alguma atenção..."
    show jenny f_cam_intro_normal_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    "{b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_cam_intro_normal_talk_down
    jen "Hehe, isso é melhor!"
    show jenny f_cam_intro_normal_down
    pause
    show jenny b_cam_electro_talk a_empty f_empty with dissolve
    jen "Ah, estou tão molhada..."
    show expression AnimatedImage("jenny_electro", [1,2,3,4], M_jenny) as jenny with dissolve
    jen "Ai sim!"
    pause
    jen "É tão bom!"
    pause
    jen "Mmm, Vamos rapazes, preciso de mais amor!"
    "{b}*PING*{/b} {b}*PING*{/b}"
    jen "É isso aí! Estou chegando mais perto de gozar!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny b_cam_electro_insert a_empty f_empty
    jen "Ahh!!" with hpunch
    pause
    show jenny b_cam_electro_talk with dissolve
    jen "Hehe! Como foi isso?!"
    scene expression game.timer.image("backgrounds/location_home_bedroom_desk_cam{}.jpg") as cutscene
    show player 311 at Position(xpos = 672)
    with dissolve
    jen "Hmm, você quer que eu pegue algo maior da próxima vez?"
    pause
    jen "Anal?!"
    jen "Você realmente quer que eu coloque algo na minha bunda, {b}sam9{/b}?"
    jen "Tch, vocês são tão exigentes!"
    pause
    jen "Hmm, se eu conseguir mais trinta inscritos, vou pegar algo maior, ok?"
    pause
    jen "Sim eu prometo."
    pause
    jen "Eu não sei sobre o anal, {b}sam9{/b}... Veremos..."
    pause
    player_name "( Uau, isso foi muito quente! )"
    player_name "( Eu deveria ver o que mais ela tem... )"
    hide cutscene
    hide player
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["03_unlocked"] = True
    return

label jenny_computer_video_2:
    scene expression "backgrounds/location_home_jennybedroom_cam1.jpg"
    show jenny b_cam_intro a_cam_intro_cover f_cam_intro_normal_talk
    show expression "characters/jenny/layeredimage/jenny_webcam_border.png"
    with dissolve
    jen "Desculpe meninos ... Esta próxima parte é apenas para assinantes."
    jen "Você ainda pode entrar e assistir se você se apressar!!"
    show jenny f_cam_intro_normal
    pause
    show jenny f_cam_intro_normal_talk a_cam_intro_reveal with dissolve
    jen "Hehe, tudo bem. Eu fiz uma promessa para vocês, não é?"
    show jenny a_cam_intro_vibrate f_cam_intro_normal_talk_left with dissolve
    jen "O que você acha desse cara grande?"
    jen "Eu te disse que iria conseguir algo maior"
    show jenny f_cam_intro_normal_down
    pause
    show jenny f_cam_intro_normal_talk_down a_cam_intro_back with dissolve
    jen "Não, {b}sam9{/b}... Não vai na minha bunda."
    jen "Sim, sim ... Talvez no futuro, veremos."
    show jenny f_cam_intro_normal_down
    pause
    show jenny f_cam_intro_normal_talk_down
    jen "Agora, que tal algum incentivo para a sua deusa do sexo?"
    show jenny f_cam_intro_normal_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    "{b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_cam_intro_normal_talk_down
    jen "Hehe, é o que eu gosto de ver!"
    jen "Só mais um pouquinho!"
    show jenny f_cam_intro_normal_down
    pause
    show jenny f_cam_intro_normal_talk_down a_cam_intro_vibrate with dissolve
    jen "Você não quer me ver goza nesse brinquedo?"
    show jenny f_cam_intro_normal_down
    "{b}*PING*{/b} {b}*PING*{/b}"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_cam_intro_normal_talk_down
    jen "Aqui vamos nós!"
    show jenny f_cam_intro_normal_down
    pause
    show jenny b_cam_vibrate_talk a_empty f_empty with dissolve
    jen "Hehe, Eu não sei se vai caber dentro da minha bocetinha apertada..."
    show expression AnimatedImage("jenny_vibrate", [1,2,3,4], M_jenny) as jenny with dissolve
    pause
    jen "Oh, porra..."
    pause
    jen "Haah!"
    pause
    jen "Mmm, Vamos meninos, mostre-me o dinheiro!"
    "{b}*PING*{/b} {b}*PING*{/b}"
    jen "É isso aí! Isso é tão bom!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "I'm getting close!!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "Oh foda sim!!"
    show jenny b_cam_vibrate_cum1 a_empty f_empty
    jen "Ahh!!" with hpunch
    pause
    pause
    show jenny b_cam_vibrate_cum2 with dissolve
    jen "Hehe, Acho que fiz uma bagunça..."
    scene expression game.timer.image("backgrounds/location_home_bedroom_desk_cam{}.jpg") as cutscene
    show player 311 at Position(xpos = 672)
    with dissolve
    player_name "( Uau, ela acabou de esguichar?! )"
    jen "Eu acho que vou lavar meus lençóis..."
    pause
    jen "O que?!"
    jen "Eu não estou lhe enviando meus lençóis!"
    pause
    jen "Você vai me pagar quanto?"
    pause
    jen "vou pensar sobre isso..."
    jen "Por enquanto, eu só quero-"
    jen "Hmm?"
    pause
    jen "Vocês querem me ver com um pênis real?"
    pause
    jen "Taaalvezzz..."
    pause
    jen "Hã, {b}sam9{/b} quer me ver com um pênis de verdade, na minha bunda ... Grande surpresa."
    pause
    jen "Vocês são dorks."
    player_name "( Uau, eu posso ver porque ela está ganhando dinheiro fazendo isso... )"
    jen "Eu vou te ver meninos em breve, ok?"
    player_name "( Hmm, Eu acho que é isso para esse vídeo. )"
    hide cutscene
    hide player
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["04_unlocked"] = True
    return

label jenny_computer_video_3:
    scene expression "backgrounds/location_home_jennybedroom_cam1.jpg"
    show jenny b_cam_intro a_cam_intro_cover f_cam_intro_normal_talk
    show expression "characters/jenny/layeredimage/jenny_webcam_border.png"
    with dissolve
    jen "Desculpe meninos ... Esta próxima parte é apenas para assinantes."
    jen "Vocês devem pagar e se juntar a nós hoje!"
    jen "Alerta de spoiler!"
    show jenny a_cam_intro_monster f_cam_intro_normal_talk_left with dissolve
    jen "Essa coisa está dentro de mim hoje!"
    jen "Espero ver você lá!"
    show jenny f_cam_intro_normal_down
    pause
    show jenny f_cam_intro_normal_talk_down a_cam_intro_back with dissolve
    jen "Hehe, tudo bem. Vamos esperar apenas um segundo e ver se alguém mais se junta..."
    show jenny f_cam_intro_normal_down
    pause
    show jenny f_cam_intro_normal_talk_down
    jen "Sim, estou a falar a sério!"
    jen "Eu vou me foder nesse monstro!"
    show jenny f_cam_intro_normal
    pause
    show jenny f_cam_intro_normal_talk
    jen "Ugh, sim, está bem, {b}sam9{/b}. Eu vou colocar isso."
    jen "Você vê esse cara?"
    jen "eu dou {b}sam9{/b} o que ele quer porque ele é sempre tão generoso com suas dicas!"
    show jenny f_cam_intro_normal
    pause
    show jenny f_cam_intro_normal_talk
    jen "É isso mesmo, dica mais e você vai conseguir o que quer também."
    show jenny f_cam_intro_normal_down
    pause
    show jenny f_cam_intro_normal_talk_down
    jen "Puta merda, nós temos quase duzentos novos subs aqui para este show!"
    jen "Eu acho que vocês estão com sede de sua deusa do sexo, huh?"
    show jenny f_cam_intro_normal_down
    pause
    show jenny f_cam_intro_normal_talk
    jen "Ok, as primeiras coisas primeiro..."
    show jenny b_cam_monster_talk a_empty f_empty with dissolve
    jen "Isso é para {b}sam9{/b}!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny b_cam_monster_talk2 with dissolve
    jen "NGGGHHH!!"
    jen "foda me sam!"
    pause
    jen "Sim, eu sei ... Está crescendo em mim."
    pause
    jen "Eu apenas disse que gostava, não é?!"
    jen "Preste atenção, manequim!"
    pause
    jen "Não, isso não significa que estou conseguindo algo maior."
    pause
    jen "Tudo bem, o suficiente com o material anal..."
    show jenny b_cam_monster_talk3 with dissolve
    jen "It's time for the main event!"
    pause
    jen "Vocês estão prontos?"
    "{b}*PING*{/b} {b}*PING*{/b}"
    jen "Eu não posso te ouvir!!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "Hehe, aqui vamos nós!"
    pause
    show jenny b_cam_monster_anim1 with dissolve
    jen "Haah..."
    show jenny b_cam_monster_anim2 with dissolve
    jen "Oh meu Deus..."
    jen "É enorme!"
    pause
    show jenny b_cam_monster_anim3 with dissolve
    jen "Puta merda!!!"
    pause
    jen "Ok..."
    $ M_jenny.set("sex speed", 0.175)
    show expression AnimatedImage("jenny_monster", [4,1,2,3], M_jenny) as jenny with dissolve
    pause
    jen "Ahh!!"
    pause
    jen "Oh, sim, sim, SIM!!!"
    pause
    jen "Oh meu deus vocês, isso é incrível!"
    "{b}*PING*{/b} {b}*PING*{/b}"
    pause
    jen "AH FODA!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "Vou gozar!!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "SIM!!"
    $ M_jenny.set("sex speed", 0.6)
    show expression AnimatedImage("jenny_monster", [2,3], M_jenny) as jenny
    jen "Ngghhh!!!" with hpunch
    pause
    show jenny b_cam_monster_after f_empty a_empty with dissolve
    pause
    jen "Haah... haah..."
    jen "Uau, isso foi"
    pause
    scene expression game.timer.image("backgrounds/location_home_bedroom_desk_cam{}.jpg") as cutscene
    show player 311 at Position(xpos = 672)
    with dissolve
    player_name "( Holy crap! )"
    jen "Oh meu deus, olha o quanto eu estou tremendo..."
    pause
    jen "Ufa, apenas me dê um segundo."
    pause
    jen "Hahaha! Eu disse a vocês que valeria a pena."
    pause
    jen "Eu sei?"
    pause
    jen "Sim, eu sei que você quer me ver fazendo no de verdade..."
    jen "Está chegando, ok?"
    jen "Basta ter suas carteiras prontas, porque eu estou esperando muitas dicas para esse show."
    pause
    jen "Hehe, Sim."
    pause
    jen "Seja bem-vindo, {b}sam9{/b}."
    pause
    jen "Sim, vejo todos vocês na próxima vez."
    pause
    jen "Tchau, garotos."
    player_name "( Totalmente vale a pena. )"
    player_name "( Isso foi demais! )"
    hide cutscene
    hide player
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["05_unlocked"] = True
    return

label jenny_hj_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_hj", [1,2,3,4,5,4,3,2], M_jenny) as jenny_hj at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_hj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,4,3,2]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_hj {}".format(pose_list[pose_counter]) as jenny_hj at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_hj_hscene_dialog")
        $ animcounter += 1
    call screen jenny_hj_options

label jenny_hj_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        player_name "puta merda!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        player_name "Oh meu Deus!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jen "Mmm, Eu posso sentir isso latejando...{p=2}{nw}"
        "{b}*PING*{/b} {b}*PING*{/b}{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        player_name "Estou chegando perto de gozar...{p=2}{nw}"
        if M_jenny.get("sex speed") > 0.051:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.025)
        player_name "Oh meu Deus!{p=1}{nw}"
    return

label jenny_hj_cum:
    if M_jenny.is_state(S_jenny_start_camshow_handjob):
        jen "Eu me pergunto o que mais eu"
        hide jenny_hj
        show jenny_hj_mc cum
        player_name "HNNGGG!!!{p=1}{nw}" with flash
        show jenny_hj_cum
        jen "{b}*Gasp*{/b}"
        pause
        jen "Que porra!"
        "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
        player_name "Ufa..."
        scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
        show player b_bed_jenny_laying a_empty f_empty od_bed_jenny_laying_dick3 of_bed_jenny_laying_mask
        show jenny b_bed_side f_bedside_angry_talk o_laptop a_bed_side_cum at Position (align=(0,0))
        with dissolve
        jen "Por que você não me avisou!"
        show jenny f_bedside_angry
        player_name "Você não me disse para avisar..."
        "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
        show jenny f_bedside_angry_talk
        jen "Bem, eu pensei que isso era óbvio, seu idiota!"
        jen "Oh meu deus, está em todo lugar!"
        show jenny f_bedside_angry
        "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
        show jenny f_bedside_angry_talk
        jen "Ugh, ok... Stream's acabou!"
        show jenny f_bedside_angry
        player_name "Mas eles ainda estão Chegando"
        show jenny f_bedside_angry_talk
        jen "FORA DO MEU QUARTO!"
        show jenny f_bedside_angry
        player_name "Está bem, está bem..."
        hide player with dissolve
        show jenny f_bedside_gross_down_talk
        jen "Eca."
        show jenny f_bedside_gross_down
        pause
        show jenny b_bed_side_laptop f_bedside_laptop_gross_down_talk with dissolve
        jen "Não é engraçado!"
        show jenny f_bedside_laptop_gross_down
        scene black with fade
        pause
        $ game.timer.tick()
        $ M_jenny.trigger(T_jenny_gave_handjob)
        $ player.go_to(L_home_bedroom)
        scene expression player.location.background_closeup with None
        show player 101h with dissolve
        player_name "( Uau! )"
        player_name "( Eu não posso acreditar {b}[jen_name]{/b} apenas me empurrou... )"
        player_name "( Estava tão quente!! )"
        pause
        show player 100c
        player_name "( Cara, espero poder fazer isso de novo! )"
        hide player with dissolve
    else:
        player_name "Aqui vai"
        jen "Hmm?"
        hide jenny_hj
        show jenny_hj_mc cum
        player_name "HNNGGG!!!{p=1}{nw}" with flash
        show jenny_hj_cum
        jen "!!!"
        "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
        scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
        show player b_bed_jenny_laying a_empty f_empty od_bed_jenny_laying_dick3 of_bed_jenny_laying_mask
        show jenny b_bed_side f_bedside_angry_talk o_laptop a_bed_side_cum at Position (align=(0,0))
        with hpunch
        jen "Novamente?!"
        jen "Deus caramba, seu idiota!"
        show jenny f_bedside_angry
        player_name "eu te avisei!"
        show jenny f_bedside_angry_talk
        jen "Bem, eu não estava prestando atenção!"
        show jenny f_bedside_angry
        "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
        show jenny f_bedside_gross_down_talk
        jen "Eugh."
        show jenny b_bed_side_laptop f_bedside_laptop_gross_down_talk with dissolve
        jen "Sim, sim ... Muito engraçado."
        jen "Mostrar mais pervertidos!"
        hide jenny
        hide player
        with dissolve
        scene expression player.location.background_closeup with None
        show player 100c at left
        show jenny b_naked f_upset_talk a_naked_hips
        with dissolve
        jen "Você está lavando meus lençóis dessa vez!"
        show jenny f_upset
        show player 101c
        player_name "Tudo bem."
        show player 100c
        show jenny f_upset_talk
        jen "Estou indo para o chuveiro."
        show jenny a_naked_money with dissolve
        jen "Tome isso e dê o fora!"
        hide jenny with dissolve
        pause
        show player 101c
        player_name "Doce!"
        call screen money_popup(50)
        $ player.get_money(50)
        $ game.timer.tick()
        $ player.go_to(L_home_basement)
        scene expression player.location.background_closeup
        show player f_normal_talk
        with fade
        player_name "Ufa!"
        player_name "Tudo bem, pronto."
        show player f_normal
        pause
        show player f_laugh
        player_name "Totalmente vale a pena!"
        hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
    $ game.main()

label jenny_hj_intro_repeat:
    show jenny f_upset_talk
    jen "Se apresse."
    show jenny f_grin_down b_pull1 a_empty with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show player f_surprised
    pause
    show jenny b_panties a_naked_hips f_upset with dissolve
    show jenny f_upset_talk
    jen "Bem?"
    show jenny f_grin_down b_naked a_naked_panties_remove with dissolve
    show player f_worried
    player_name "Hmm?"
    show jenny b_naked_panties_remove_down a_empty f_empty with dissolve
    pause
    show jenny b_naked a_naked_hips f_upset_talk with dissolve
    jen "Tire essas roupas!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Certo..."
    show player f_worried
    label finger_blasting_hj:
    scene black with fade
    pause
    scene expression "backgrounds/location_home_jennybedroom_cutscene05.jpg" with dissolve
    jen "Você sabe o que fazer."
    jen "Mascara e mantenha sua boca fechada."
    player_name "Sim, eu me lembro."
    jen "Eu vou lidar com o resto."
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show player b_bed_jenny_sit a_empty f_jenny_bed_sit_shy_down of_jenny_bed_sit_mask at Position (align=(0,0))
    show jenny o_under_body_laptop b_naked_bed_bellytype a_empty f_bed_facing_comp_sexy_talk_down at Position (align=(0,0))
    with dissolve
    jen "Oi de novo, todo mundo!"
    show jenny b_naked_bed_belly with dissolve
    jen "Eu trouxe meu brinquedinho de volta para dar a vocês um outro show."
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_laugh
    jen "Hehe, claro!"
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Bem, vamos descobrir, vamos?"
    show jenny o_laptop b_bed_side a_bed_side_laptop f_bedside_sexy_talk_down
    show player b_bed_jenny_laying f_empty od_bed_jenny_laying_dick1 of_bed_jenny_laying_mask
    with dissolve
    jen "Aposto que ele está bem e pronto desta vez."
    show jenny a_bed_side_pull1 f_bedside_sexy_down with dissolve
    pause
    show player od_empty
    show jenny a_bed_side_pull2
    with dissolve
    pause
    show jenny a_bed_side_point
    show player od_bed_jenny_laying_dick4
    with fastdissolve
    show player od_bed_jenny_laying_dick5 with fastdissolve
    show player od_bed_jenny_laying_dick6 with fastdissolve
    jen "!!!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    pause
    show jenny b_bed_side_laptop f_bedside_laptop_sexy_talk_down with dissolve
    jen "Hehe, I know it's big!"
    jen "Eu não me contentaria com nada menos, iria?"
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Sim, acho que deveria também."
    $ M_jenny.set("sex speed",0.4)
    show jenny b_bed_side f_bedside_sexy_down a_bed_side_jerk with dissolve
    player_name "!!!"
    pause
    player_name "Oh Deus!"
    show jenny f_bedside_sexy_talk_down
    jen "Sim, você gosta disso, não é?"
    show jenny f_bedside_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    pause
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg" with None
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .1)
    show jenny_hj_mc
    show expression AnimatedImage("jenny_hj", [1,2,3,4,5,4,3,2], M_jenny) as jenny_hj at Position(xalign = 0.0, yoffset = 0)
    with dissolve
    jen "Vamos, brinquedo de menino!!"
    jen "Diga a todos o quanto você me ama acariciando seu pau grande e duro..."
    player_name "eu amo isso!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "Hahaha!"
    pause
    player_name "{b}[jen_name]{/b}, Eu vou-"
    jen "Vocês meninos vendo isso?!"
    jen "Hehe, você gosta dos meus seios grandes, hein?"
    "{b}*PING*{/b} {b}*PING*{/b}"
    jump jenny_hj_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
