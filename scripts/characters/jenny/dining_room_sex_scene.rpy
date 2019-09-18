label jenny_dining_room_sex_intro:
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_grin_talk
    jen "Shh!!"
    show jenny f_breakfast_grin
    show player f_diningroom_table_surprised_teeth_down
    show debbie b_breakfast_mug a_empty f_breakfast_standing_mug_normal_talk at Position (align=(0,0)) with dissolve
    deb "Você disse alguma coisa, querida?"
    show debbie f_breakfast_standing_mug_normal
    show jenny f_breakfast_grin_talk
    jen "Você me faria um café da manhã?"
    show player f_diningroom_table_shy_down
    show jenny f_breakfast_grin
    show debbie f_breakfast_standing_mug_normal_talk
    deb "Você quer que eu cozinhe para você?"
    show debbie f_breakfast_standing_mug_normal
    show jenny f_breakfast_grin_talk
    jen "Sim."
    show jenny f_breakfast_grin
    show debbie f_breakfast_standing_mug_normal_talk
    deb "Bem, claro que eu vou querida!"
    deb "Eu sempre me preocupo com você não ter o suficiente para comer"
    show debbie f_breakfast_standing_mug_sad
    show jenny f_breakfast_eyeroll
    jen "Sim, eu sei{b}[deb_name]{/b}... Você me diz o tempo todo!"
    show jenny f_breakfast_upset
    show debbie f_breakfast_standing_mug_sad_talk
    deb "Certo... Umm..."
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    show debbie f_breakfast_standing_mug_normal_talk
    deb "Vou preparar alguns ovos e bacon agora mesmo!"
    show player f_diningroom_table_looking_down_food a_dinner_sitting_resting with dissolve
    show debbie f_breakfast_standing_mug_normal
    show jenny f_breakfast_grin_talk
    jen "Obrigada."
    show jenny f_breakfast_grin
    show debbie f_breakfast_standing_mug_normal_talk
    deb "Será apenas alguns minutos, querida."
    show player f_diningroom_table_surprised_high_food with None
    show expression "characters/xtra/overlay_o_dinner_mug.png"
    hide debbie
    with dissolve
    show jenny f_breakfast_laugh a_breakfast_dressed_laugh with dissolve
    jen "Hehe..."
    show jenny b_breakfast_gettingup a_empty f_breakfast_getup_grin_down with dissolve
    pause
    show jenny b_breakfast_remove f_empty with dissolve
    if M_jenny.get("first_sex_dining"):
        $ M_jenny.set("first_sex_dining", False)
        show player f_diningroom_table_worried_talk_high
        player_name "Ok, então agora o que"
        show jenny b_breakfast_leaning f_breakfast_lean_grin with dissolve
        show player f_diningroom_table_surprised_teeth_left
        player_name "!!!"
        if M_jenny.get("dominance") <= 0:
            show player f_magic_sit_stand_worried_talk
            player_name "Nós não podemos"
            show player f_magic_sit_stand_worried
            show jenny f_breakfast_lean_upset_talk
            jen "{b}*Suspiro*{/b} Bem, não se você vai ser um pouco puta sobre isso..."
            show jenny b_breakfast_remove f_empty with dissolve
            pause 1
            show jenny b_breakfast_gettingup a_empty f_breakfast_getup_upset_talk with dissolve
            jen "... E aqui eu pensei que você estava finalmente começando a crescer uma espinha dorsal."
            show jenny f_breakfast_getup_upset
            show player f_magic_sit_stand_worried_talk
            player_name "Bem!"
            show jenny b_breakfast_remove f_empty with dissolve
            player_name "Vamos apenas nos apressar, ok?"
            show player f_magic_sit_stand_worried
            show jenny b_breakfast_leaning f_breakfast_lean_grin_talk with dissolve
            jen "Sim, sim ... Tire seu pau já!"
        else:
            show player f_magic_sit_stand_worried_talk
            player_name "Você está louca?!"
            show player f_magic_sit_stand_worried
            show jenny b_breakfast_standing_panties_down a_breakfast_standing_hips f_breakfast_standing_sexy_talk_down with dissolve
            jen "Vamos lá, {b}[firstname]{/b}... Você sabe que você quer."
            show jenny f_breakfast_standing_sexy_down
            show player f_magic_sit_stand_worried_talk
            player_name "{b}*Suspiro*{/b} bem."
            show player f_magic_sit_stand_worried
            show jenny f_breakfast_standing_sexy_talk_down
            jen "É melhor você se apressar, só temos alguns minutos..."
            show jenny f_breakfast_standing_sexy_down
            show player f_magic_sit_stand_worried_talk
            player_name "Apenas cale a boca e volte para lá!"
            show player f_magic_sit_stand_worried
            show jenny b_breakfast_leaning f_breakfast_lean_laugh a_empty with dissolve
            jen "Hehehe!"
            show jenny f_breakfast_lean_grin
    else:
        show player f_magic_sit_stand_worried_talk
        player_name "Por que não podemos simplesmente subir?!"
        show player f_magic_sit_stand_worried
        show jenny f_breakfast_lean_grin_talk b_breakfast_leaning with dissolve
        jen "Apenas cale a boca e me foda, {b}[firstname]{/b}!"
        show jenny f_breakfast_lean_grin
        show player f_diningroom_table_tired_talk
        player_name "{b}*Suspiro*{/b}"
        scene black with fade
        pause

label jenny_dining_room_sex_pre_insert:
    scene expression "backgrounds/location_home_diningroom_sex.jpg"
    show jenny_sex_table b_default f_back
    show player_jenny_diningroom_sex pre
    with fade
    player_name "Apenas não faça muito barulho..."
    show jenny_sex_table f_back_talk
    jen "Oh, por favor ... eu tenho certeza que posso me controlar "
    hide jenny_sex_table
    hide player_jenny_diningroom_sex
    show jenny_diningroom_sex insert
    with dissolve
    pause 1
    show jenny_diningroom_sex 1
    jen "AUTO!!!" with hpunch
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    show expression AnimatedImage("jenny_diningroom_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_diningroom_sex at Position(xalign = 0.0, yoffset = 0) with dissolve
    jen "Oh, porraaaa!"
    player_name "Shhh!!!"
    jen "Ngghhh!"
    pause
    jen "puta merda"
    jen "!!!"
    player_name "Você tem que ficar quieta ou eu vou parar!"
    jen "Não se atreva a parar!"
    pause
    player_name "Você está me apertando muito forte!"
    jen "Eu não posso evitar, isso está realmente me excitando!"
    pause
    deb "{b}[jen_name]{/b}?!"
    hide jenny_diningroom_sex
    show jenny_sex_table b_default f_surprised
    show player_jenny_diningroom_sex pre
    with dissolve
    player_name "!!!" with hpunch
    jen "!!!"
    show jenny_sex_table f_angry_talk
    jen "Sim?"
    show jenny_sex_table f_angry
    deb "Você gostaria de seus ovos sejam preparado inteiros ou mexidos?"
    show jenny_sex_table f_angry_talk
    jen "Oh, umm...mexidos está bem!"
    hide jenny_sex_table
    hide player_jenny_diningroom_sex
    show expression AnimatedImage("jenny_diningroom_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_diningroom_sex at Position(xalign = 0.0, yoffset = 0) with hpunch
    deb "Ok querida."
    jen "Se apresse, {b}[firstname]{/b}!"
    pause
    player_name "Estou chegando perto."
    jen "Eu também!"

label jenny_diningroom_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_diningroom_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_diningroom_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_diningroom_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_diningroom_sex {}".format(pose_list[pose_counter]) as jenny_diningroom_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_diningroom_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_diningroom_sex_options

label jenny_diningroom_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jen "Ahh!!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jen "É tão bom!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jen "Fodeeeee!!!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        player_name "Uhh!{p=1}{nw}"
    return

label jenny_diningroom_sex_cum_inside:
    player_name "Vou gozar!"
    jen "Não pare!!"
    show jenny_diningroom_sex cum
    player_name "HNNGGG!!!" with flash
    show jenny_diningroom_sex cum2
    show xray_jenny_diningroom_table at Position (align=(0,0))
    jen "NGGHHH!!!"
    hide xray_jenny_diningroom_table
    pause
    show jenny_diningroom_sex 1 with dissolve
    player_name "Haah... Haah..."
    jen "Puta merda..."
    player_name "Sim..."
    jen "Sai de cima de mim."
    hide jenny_diningroom_sex
    show jenny_sex_table b_default f_angry
    show player_jenny_diningroom_sex after
    with dissolve
    pause
    call call_pregnancy_minigame ("jenny_diningroom_sex_cum_inside_post_pregnancy", M_jenny)

label jenny_diningroom_sex_cum_inside_post_pregnancy:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_standing_panties_down a_breakfast_standing_cum2 f_breakfast_standing_upset_down_talk zorder 1 at Position (align=(0,0))
    show player b_dinner_sitting a_dinner_sitting_resting f_diningroom_table_shy_down zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    show expression "characters/xtra/overlay_o_dinner_mug.png" zorder 2
    with fade
    jen "droga, {b}[firstname]{/b}!"
    jen "Se eu engravidar vou matar você!"
    show jenny f_breakfast_standing_upset_down a_breakfast_standing_cum1 with dissolve
    show player f_diningroom_table_flirt_talk_left
    player_name "Você me disse para não parar..."
    show player f_diningroom_table_flirt_left
    show jenny f_breakfast_standing_gross_down_talk
    jen "Sim, mas eu não te disse para gozar dentro de mim, não é?"
    show jenny f_breakfast_standing_gross_down
    player_name "..."
    show jenny f_breakfast_standing_gross_down_talk
    jen "Porra idiota..."
    show jenny f_breakfast_standing_gross_down
    show player f_magic_sit_stand_worried_talk
    player_name "Cale-se!"
    show player f_magic_sit_stand_worried
    deb "Ok, quem está com fome?!"
    show player f_magic_sit_stand_surprised
    show jenny f_breakfast_standing_surprised
    jen "!!!" with hpunch
    show jenny b_breakfast_remove a_empty f_empty with dissolve
    pause
    show jenny b_breakfast_dressed a_breakfast_dressed_spoon f_breakfast_upset_down with dissolve
    show player f_diningroom_table_normal_high
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_normal_talk zorder 1 at Position (align=(0,0)) with dissolve
    deb "Dois ovos mexidos e três tiras de bacon, como você queria."
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_normal_talk
    jen "Obrigada, {b}[deb_name]{/b}."
    show jenny f_breakfast_normal
    show player f_diningroom_table_shy_down
    show debbie f_breakfast_standing_normal_talk
    deb "De nada querida!"
    hide expression "characters/xtra/overlay_o_dinner_mug.png"
    show debbie b_breakfast_sitting a_breakfast_mug f_breakfast_sitting_normal
    with dissolve
    pause
    show debbie f_breakfast_sitting_normal_talk
    deb "{b}[firstname]{/b}, você parece cansado..."
    deb "Você está se sentindo bem, querido?"
    show debbie f_breakfast_sitting_normal
    show player f_magic_sit_stand_surprised
    player_name "Hmm?"
    show jenny f_breakfast_normal_talk
    jen "Ele está bem."
    show jenny f_breakfast_normal
    show player f_diningroom_table_normal_talk
    player_name "Sim, estou bem."
    show player f_diningroom_table_normal
    show debbie f_breakfast_sitting_normal_talk
    deb "Tudo bem, apenas certifique-se de que você está descansando o suficiente, ok?"
    show debbie f_breakfast_sitting_normal
    show player f_diningroom_table_normal_talk
    player_name "Ok."
    show player f_diningroom_table_shy_down
    show debbie a_breakfast_mug_drink f_breakfast_sitting_kiss with dissolve
    pause
    show debbie f_breakfast_sitting_sad_talk a_breakfast_mug with dissolve
    deb "Mmm, tem cheiro estranho aqui?"
    show debbie f_breakfast_sitting_sad
    show player f_diningroom_table_worried_talk
    player_name "Não?"
    show player f_diningroom_table_worried
    show debbie f_breakfast_sitting_normal
    show jenny f_breakfast_normal_talk
    jen "Eu não sinto cheiro de nada."
    show jenny f_breakfast_normal
    show debbie f_breakfast_sitting_normal_talk
    deb "Hmm, algo cheira engraçado..."
    show debbie f_breakfast_sitting_normal
    show jenny f_breakfast_laugh a_breakfast_dressed_phone with dissolve
    show player f_diningroom_table_worried_talk
    player_name "Sim, eu não sei {b}[deb_name]{/b}..."
    show player f_diningroom_table_worried
    jen "Hehehe!"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["15_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_diningroom)
    $ game.main()

label jenny_diningroom_sex_cum_outside:
    player_name "Vou gozar!"
    jen "Não pare!!"
    hide jenny_diningroom_sex
    show jenny_sex_table b_default f_angry
    show player_jenny_diningroom_sex after
    with dissolve
    pause
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_standing_panties_down a_breakfast_standing_hips f_breakfast_standing_gross_down_talk zorder 1 at Position (align=(0,0))
    show player b_dinner_standing_cumming a_empty f_diningroom_table_cum_surprised_teeth_down zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with fade
    jen "Que porra, {b}[firstname]{/b}?!"
    show jenny f_breakfast_standing_gross_down
    show player f_diningroom_table_cum_brag
    player_name "HNNGGG!!!" with flash
    show jenny f_breakfast_standing_gross_down_talk
    jen "Eu te disse para não parar!"
    show player f_diningroom_table_cum_surprised_teeth_down
    show jenny f_breakfast_standing_gross_down
    pause
    show player b_dinner_sitting a_dinner_sitting_resting f_diningroom_table_tired_talk zorder 0 at Position(align=(0,0))
    show expression "characters/xtra/overlay_o_dinner_mug.png" zorder 2
    with dissolve
    player_name "Haah... Haah..."
    show player f_magic_sit_stand_worried_talk
    player_name "O que você quer que eu faça, {b}[jen_name]{/b}?!"
    player_name "Eu deveria gozar dentro de você?!"
    show player f_magic_sit_stand_worried
    show jenny b_breakfast_remove a_empty f_empty with dissolve
    pause
    show jenny b_breakfast_dressed a_breakfast_dressed_spoon f_breakfast_upset_talk with dissolve
    jen "Não..."
    jen "{b}*Suspiro*{/b} Só teria sido bom terminar, idiota!"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Cale-se!"
    show player f_magic_sit_stand_worried
    deb "Ok, quem está com fome?!"
    show player f_magic_sit_stand_surprised
    show jenny f_breakfast_surprised
    jen "!!!" with hpunch
    show player f_diningroom_table_normal_high
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_normal_talk zorder 1 at Position (align=(0,0)) with dissolve
    deb "Dois ovos mexidos e três tiras de bacon, como você queria."
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_normal_talk
    jen "Obrigada, {b}[deb_name]{/b}."
    show jenny f_breakfast_normal
    show debbie f_breakfast_standing_normal_talk
    show player f_diningroom_table_shy_down
    deb "De nada querida!"
    hide expression "characters/xtra/overlay_o_dinner_mug.png"
    show debbie b_breakfast_sitting a_breakfast_mug f_breakfast_sitting_normal
    with dissolve
    pause
    show debbie f_breakfast_sitting_normal_talk
    deb "{b}[firstname]{/b}, você parece cansado..."
    deb "Você está se sentindo bem, querido?"
    show debbie f_breakfast_sitting_normal
    show player f_magic_sit_stand_surprised
    player_name "Hmm?"
    show jenny f_breakfast_normal_talk
    jen "Ele está bem."
    show jenny f_breakfast_normal
    show player f_diningroom_table_normal_talk
    player_name "Sim, estou bem."
    show player f_diningroom_table_normal
    show debbie f_breakfast_sitting_normal_talk
    deb "Tudo bem, apenas certifique-se de que você está descansando o suficiente, ok?"
    show debbie f_breakfast_sitting_normal
    show player f_diningroom_table_normal_talk
    player_name "Ok."
    show player f_diningroom_table_surprised_talk
    show jenny f_breakfast_surprised
    show debbie a_breakfast_mug_drink f_breakfast_sitting_kiss with dissolve
    player_name "Espere"
    show player f_magic_sit_stand_surprised
    pause
    show jenny f_breakfast_laugh
    show debbie f_breakfast_sitting_gross_talk a_breakfast_mug with dissolve
    deb "Eca, esse café tem um gosto horrível!"
    show debbie f_breakfast_sitting_gross
    show player f_diningroom_table_worried_talk
    player_name "Mesmo?"
    show player f_diningroom_table_worried
    show debbie f_breakfast_sitting_gross_talk
    deb "Sim!"
    show debbie f_breakfast_sitting_gross
    jen "{b}*Credo*{/b}"
    show jenny f_breakfast_grin
    show debbie f_breakfast_sitting_gross_talk
    deb "Eu não entendo, estava bom alguns minutos atrás..."
    show debbie f_breakfast_sitting_gross
    show player f_diningroom_table_worried_talk
    player_name "Esquisito..."
    player_name "Você provavelmente deve despejá-lo e pegar um novo copo."
    show player f_diningroom_table_worried
    show debbie f_breakfast_sitting_gross_talk
    deb "Sim, eu também penso assim."
    deb "que nojo!"
    show debbie f_breakfast_sitting_gross
    show jenny f_breakfast_laugh
    jen "Hehehe!"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["15_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_diningroom)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
