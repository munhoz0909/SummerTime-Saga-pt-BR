label erikmom_bedroom:
    if M_jenny.is_state(S_jenny_perv_on_tammy) and game.timer.is_morning():
        call expression game.dialog_select("telescope_jenny_perv_on_tammy")
        $ persistent.cookie_jar["Mrs Johnson"]["unlocked"] = True
        $ persistent.cookie_jar["Mrs Johnson"]["gallery"]["02_unlocked"] = True
        $ M_jenny.trigger(T_jenny_spied_on_tammy)
        hide screen telescope
        jump bedroom_jenny_give_cunni
    else:
        call expression game.dialog_select(game.telescope.mrsj)

    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_jenny_perv_on_tammy:
    if mrsj.over(mrsj_private_yoga):
        label mrsj_private_yoga_perv_jenny_replay:
        scene windowmrsjday 3a with dissolve
        player_name "( Lá está ela... )"
        player_name "( Puta merda Ela está completamente nua! )"
        pause
        scene windowmrsjday 3b with dissolve
        player_name "( O que é ela )"
        scene windowmrsjday 3c-d
        player_name "( !!! )" with hpunch
        player_name "( puta merda! )"
        pause
        player_name "( Ela sabe que eu estou assistindo?! )"
        scene expression "backgrounds/location_home_bedroom_caught_01.jpg" with dissolve
        player_name "Uauuuu!"
        scene expression "backgrounds/location_home_bedroom_caught_02.jpg" with dissolve
        pause
        scene expression "backgrounds/location_home_bedroom_caught_03.jpg" with dissolve
        pause
        scene expression "backgrounds/location_home_bedroom_caught_04.jpg" with dissolve
        pause
        scene expression "backgrounds/location_home_bedroom_telescope_window.jpg" with None
        show player b_telescope_peeking a_empty f_empty
        show jenny b_telescope_standing a_empty f_telescope_standing_grin_talk zorder 1 at Position (align=(0,0)) with dissolve
        jen "Espionando a garota vizinha de novo?"
        show jenny f_telescope_standing_grin
        show player b_telescope_laying_back a_telescope_side f_telescope_lay_surprised zorder 0 at Position (align=(0,0)) with hpunch
        player_name "Não, e da sua conta desculpe inventei isso na tradução "
        show player f_telescope_lay_worried
        show jenny f_telescope_standing_grin_talk
        jen "Ok, certo."
        jen "Não minta."
        show jenny b_telescope_look f_empty a_empty with dissolve
        jen "O que ela está fazendo agora?"
        player_name "..."
        jen "Puta merda!"
        scene windowmrsjday 3c-d with dissolve
        jen "Não é seu amigo, qual é o nome dele e a {b}landlady{/b}?"
        player_name "{b}Erik{/b}."
        jen "Sim, {b}Erik{/b}."
        pause
        jen "Hã, o que ela está fazendo?!"
        scene expression "backgrounds/location_home_bedroom_telescope_window.jpg" with None
        show player b_telescope_laying_back a_telescope_side f_telescope_lay_worried_talk at Position (align=(0,0))
        show jenny b_telescope_look f_empty a_empty
        with fade
        player_name "Eu não sei"
        show player f_telescope_lay_worried
        show jenny f_telescope_surprised b_telescope a_telescope_down with dissolve
        jen "Espere um minuto..."
        show jenny f_telescope_normal_talk
        jen "Ela sabe que você está a observando?!"
        show jenny f_telescope_normal
        player_name "..."
        show jenny f_telescope_laugh
        jen "De jeito nenhum!"
        show jenny f_telescope_normal
        player_name "..."
        show jenny f_telescope_normal_talk
        jen "Você pensa na {b}Sra. Johnson{/b}, {b}[firstname]{/b}?!"
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk
        player_name "Talvez um pouquinho..."
        show player f_telescope_lay_worried
        show jenny b_telescope_look f_empty a_empty with dissolve
        jen "Hahahahaah!"
        pause
        jen "Eu tenho que rir de você, {b}[firstname]{/b}."
        jen "Ela é muito boa para sua idade."
        show player f_telescope_lay_worried_talk
        player_name "Talvez."
        show player f_telescope_lay_worried
        jen "Quero dizer, ela não é tão perto quanto eu, mas ainda assim"
        player_name "..."
        show jenny b_telescope_rub a_telescope_rub with dissolve
        show player f_telescope_lay_surprised
        player_name "( !!! )"
        jen "Porra, olhe para ela ..."
        jen "Você acha que ela está imaginando seu pau dentro dela, agora?"
        pause
        $ persistent.cookie_jar["Mrs Johnson"]["unlocked"] = True
        $ persistent.cookie_jar["Mrs Johnson"]["gallery"]["02_unlocked"] = True
        $ renpy.end_replay()
    else:
        label mrsj_erik_cunni_perv_jenny_replay:
        scene windowmrsjday 4a with dissolve
        pause
        player_name "( Hmm, ela só está falando com {b}Erik{/b}. )"
        player_name "( Eu acho que não vai ser um show hoje... )"
        pause
        scene windowmrsjday 4b with dissolve
        player_name "( Puta Merda Espere um minuto!)"
        scene windowmrsjday 4c
        player_name "( !!! )" with hpunch
        player_name "( Ele vai chupar a buceta dela! )"
        pause
        player_name "( Isso {b}Erik{/b} parece que você não e tão bobo como pensei hehe! )"
        scene expression "backgrounds/location_home_bedroom_caught_01.jpg" with dissolve
        player_name "Uauuuu!"
        scene expression "backgrounds/location_home_bedroom_caught_02.jpg" with dissolve
        pause
        scene expression "backgrounds/location_home_bedroom_caught_03.jpg" with dissolve
        pause
        scene expression "backgrounds/location_home_bedroom_caught_04.jpg" with dissolve
        pause
        scene expression "backgrounds/location_home_bedroom_telescope_window.jpg" with None
        show player b_telescope_peeking a_empty f_empty
        show jenny b_telescope_standing a_empty f_telescope_standing_grin_talk zorder 1 at Position (align=(0,0)) with dissolve
        jen "Espionando a garota vizinha de novo?"
        show jenny f_telescope_standing_grin
        show player b_telescope_laying_back a_telescope_side f_telescope_lay_surprised zorder 0 at Position (align=(0,0)) with hpunch
        player_name "!!!"
        show player f_telescope_lay_worried_talk
        player_name "Não, eu não"
        show player f_telescope_lay_worried
        show jenny f_telescope_standing_grin_talk
        jen "Mentiroso."
        jen "Não minta."
        show jenny b_telescope_look f_empty a_empty with dissolve
        jen "O que ela está fazendo agora?"
        player_name "..."
        jen "Puta merda!"
        scene windowmrsjday 4c with dissolve
        jen "Não é esse seu amigo, qual é o nome dele?"
        player_name "{b}Erik{/b}."
        jen "Sim, {b}Erik{/b}."
        pause
        jen "Hã, Ela parece desesperada com aquele garoto bunda gorda!"
        scene expression "backgrounds/location_home_bedroom_telescope_window.jpg" with None
        show player b_telescope_laying_back a_telescope_side f_telescope_lay_worried_talk at Position (align=(0,0))
        show jenny b_telescope_look f_empty a_empty
        with fade
        player_name "Ei, seja legal!"
        player_name "{b}Erik{/b} é um cara legal."
        show player f_telescope_lay_worried
        show jenny f_telescope_laugh b_telescope a_telescope_down with dissolve
        jen "Pfft, sim tudo bem."
        show jenny f_telescope_normal_talk
        jen "Quem se importa!"
        show jenny b_telescope_look f_empty a_empty with dissolve
        jen "Bem, ela parece estar se divertindo..."
        show jenny b_telescope_rub a_telescope_rub with dissolve
        player_name "( !!! )"
        jen "Eu acho que ele realmente sabe o que está fazendo."
        pause
        $ persistent.cookie_jar["Mrs Johnson"]["unlocked"] = True
        $ persistent.cookie_jar["Mrs Johnson"]["gallery"]["03_unlocked"] = True
        $ renpy.end_replay()
    return

label telescope_mrsj_morning_1:
    scene windowmrsjmorning01
    player_name "( ...È a {b}landlady de Erik{/b}?! )"
    scene windowmrsjmorning01b
    player_name "( Uau! Ela está se vestindo... )"
    scene windowmrsjmorning01c
    player_name "( Não! Só um pouquinho mais! )"
    scene windowmrsjmorning01d
    player_name "( Droga! Show acabou... )"
    return

label telescope_mrsj_morning_2:
    scene windowmrsjday02
    player_name "( Suas cortinas estão fechadas. Ela provavelmente não está em casa. )"
    return

label telescope_mrsj_afternoon_1:
    scene windowmrsjday01
    player_name "( Ela não está em casa. )"
    return

label telescope_mrsj_afternoon_2:
    show windowmrsjday 3a
    player_name "( Uau ... Ela está completamente nua!! )"
    show windowmrsjday 3b with fastdissolve
    player_name "( Isso é uma bola quicando ... com um vibrador nela?! )"
    show windowmrsjday 3c with fastdissolve
    player_name "( Por que ela não fechou as cortinas? )"
    show windowmrsjday 3c-d
    player_name "( É como se ela quisesse ser vista... )"
    player_name "( Eu acho que ela sabe... )"
    player_name "( Ela está olhando diretamente para mim. )"
    return

label telescope_mrsj_afternoon_3:
    scene windowmrsjday02
    player_name "( Suas cortinas estão fechadas. Ela provavelmente não está em casa. )"
    return

label telescope_mrsj_night_1:
    scene windowmrsjnight03
    player_name "( ...Ela está praticando yoga? )"
    player_name "( ...Na cama dela? )"
    scene windowmrsjnight04
    player_name "..."
    player_name "( {b}landlady do Erik{/b} está tão em forma... )"
    player_name "( ...ela realmente tem um ótimo corpo... )"
    return

label telescope_mrsj_night_2:
    scene windowmrsjnight01
    player_name "( Ela não está no quarto dela... )"
    return

label telescope_mrsj_night_3:
    scene windowmrsjnight02
    player_name "( Ela deve estar dormindo. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
