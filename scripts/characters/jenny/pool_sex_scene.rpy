label jenny_pool_sex_intro:
    scene expression "backgrounds/location_home_backyard_pool_sex.jpg"
    show jenny_pool_sex pre
    show jenny_pool_sex_face normal_talk_down
    show overlay_o_water zorder 100
    with fade
    jen "Apenas certifique-se de manter a cabeça baixa, eu não quero {b}[deb_name]{/b} nos ver!"
    show jenny_pool_sex_face normal_down
    player_name "Eu vou!"
    show jenny_pool_sex insert with dissolve
    player_name "Eu vou!..."
    show jenny_pool_sex_face normal_talk_down
    jen "Cale a boca e desça mais baixo, manequim!"
    show jenny_pool_sex_face normal_down
    player_name "Eu não posso ir mais baixo, a água é"
    hide jenny_pool_sex_face normal_down
    show jenny_pool_sex 1
    player_name "!!!" with hpunch
    $ M_jenny.set('pool_clothes', True)
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    show expression AnimatedImage("jenny_pool_sex", [1,2,3,4,5,6,7,8,9,10], M_jenny) as jenny_pool_sex at Position(xalign = 0.0, yoffset = 0) with dissolve
    pause
    jen "Mmm, porra!"
    player_name "Pare, você está me empurrando!"
    jen "Shh!!"
    player_name "bllgggh!"
    pause
    player_name "{b}[jen_name]{/b} você está indo-"
    player_name "bllgghhrrghhh!!"
    jen "Pare de fazer tanto barulho!"
    player_name "Você está me afogando!"
    jen "Oh, eu não sou você grande bebê!"
    pause
    player_name "bllggh!!!"
    player_name "{b}*Cough* *Cough*{/b}"
    jen "Mm, Eu amo esse pau grande ... Tanto!!"
    pause
    jen "Vamos, me foda mais rápido, {b}[firstname]{/b}!"
    player_name "estou tentando!"
    pause
    jen "Porra sagrada!!"
    jen "Vou gozar!"
    player_name "Eu também"

label jenny_pool_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_jenny.get('pool_clothes'):
                    show expression AnimatedImage("jenny_pool_sex", [1,2,3,4,5,6,7,8,9,10], M_jenny) as jenny_pool_sex at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression AnimatedImage("jenny_pool_sex_naked", [1,2,3,4,5,6,7,8,9,10], M_jenny) as jenny_pool_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_pool_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                if M_jenny.get('pool_clothes'):
                    show expression "jenny_pool_sex {}".format(pose_list[pose_counter]) as jenny_pool_sex at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression "jenny_pool_sex_naked {}".format(pose_list[pose_counter]) as jenny_pool_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_pool_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_pool_sex_options

label jenny_pool_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jen "Ahh!!{p=1}{nw}"
        player_name "blghrghhh!!!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        player_name "bllgggh!{p=1}{nw}"
        jen "É tão profundo!{p=1}{nw}"
        jen "Foda-me!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jen "Fooode!!!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        player_name "bllgghhrrghhh!!!{p=1}{nw}"
    return

label jenny_pool_sex_cum_inside:
    jen "O meus deus, o meu deus, O MEU DEUS!!"
    jen "Não pare!!"
    jen "NGGHHH!!!"
    show jenny_pool_sex cum
    player_name "HNNGGG!!!" with flash
    show jenny_pool_sex cum2
    show xray_jenny_pool at Position (align=(0,0))
    pause
    hide xray_jenny_pool
    show jenny_pool_sex pullout1
    show jenny_pool_sex_face normal_down
    with dissolve
    pause
    show jenny_pool_sex after
    show jenny_pool_sex_face normal_talk_down
    show player_jenny_pool pullout2
    with dissolve
    jen "Haah... Haah..."
    jen "Isso foi demais!"
    call call_pregnancy_minigame ("jenny_pool_sex_cum_inside_post_pregnancy", M_jenny)

label jenny_pool_sex_cum_inside_post_pregnancy:
    scene expression "backgrounds/location_home_backyard_pool_closeup_day.jpg"
    show player f_homepool_jenny_tired_talk b_pool a_empty at Position (align=(0,0))
    show jenny b_pool a_empty f_homepool_player_upset_down at Position (align=(0,0))
    with fade
    player_name "Eu acho que vou desmaiar..."
    show player f_homepool_jenny_tired
    show jenny f_homepool_player_angry_talk
    jen "Você gozou comigo?!"
    show jenny f_homepool_player_angry
    show player f_homepool_jenny_tired_talk
    player_name "Eu nem sei, {b}[jen_name]{/b}... Minha vida estava piscando diante dos meus olhos!"
    show player f_homepool_jenny_tired
    show jenny f_homepool_player_eyeroll
    jen "Oh, pare de ser tão dramático..."
    show jenny f_homepool_player_angry_talk
    jen "Eu juro, se eu engravidar, vou te matar!"
    show jenny f_homepool_player_angry
    show player f_homepool_jenny_tired_talk
    player_name "{b}[jen_name]{/b}, Eu não posso nem"
    player_name "Eu preciso ir deitar ou algo..."
    hide player with dissolve
    pause
    show jenny f_homepool_player_angry_talk
    jen "Coloque suas calças antes de entrar, idiota!"
    show jenny f_homepool_player_angry
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["16_unlocked"] = True
    $ player.go_to(L_home_bedroom)
    $ game.timer.tick()
    $ game.main()

label jenny_pool_sex_cum_outside:
    jen "O meu deus, o meu deus, O MEU DEUS!!"
    jen "Não pare!!"
    jen "NGGHHH!!!"
    show jenny_pool_sex pullout1
    show jenny_pool_sex_face normal_down
    with dissolve
    pause
    show jenny_pool_sex after
    show jenny_pool_sex_face normal_down
    show player_jenny_pool flying_cum
    player_name "HNNGGG!!!" with flash
    show player_jenny_pool pullout3 with dissolve
    pause
    show jenny_pool_sex_face normal_talk_down
    jen "Haah... Haah..."
    jen "Isso foi demais!"
    scene expression "backgrounds/location_home_backyard_pool_closeup_day.jpg"
    show player f_homepool_jenny_tired_talk b_pool a_empty at Position (align=(0,0))
    show jenny b_pool a_empty f_homepool_player_upset_down at Position (align=(0,0))
    with fade
    player_name "Eu acho que vou desmaiar..."
    show player f_homepool_jenny_tired
    show jenny f_homepool_player_gross_talk
    jen "Eca, seu esperma está flutuando ao meu redor!"
    show jenny f_homepool_player_gross
    show player f_homepool_jenny_tired_talk
    player_name "Sim, desculpe ... Minha vida estava piscando diante dos meus olhos!"
    show player f_homepool_jenny_tired
    show jenny f_homepool_player_gross_talk
    jen "Oh, pare de ser tão dramático..."
    jen "Eu sou o marinheiro no seu suco de bola por aqui!"
    show jenny f_homepool_player_gross
    show player f_homepool_jenny_tired_talk
    player_name "{b}[jen_name]{/b}, Eu não posso nem"
    player_name "Eu preciso ir deitar ou algo..."
    hide player with dissolve
    pause
    show jenny f_homepool_player_gross_talk
    jen "Coloque suas calças antes de entrar, idiota!"
    show jenny f_homepool_player_gross
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["16_unlocked"] = True
    $ player.go_to(L_home_bedroom)
    $ game.timer.tick()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
