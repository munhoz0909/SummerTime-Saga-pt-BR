label coach_locker_dialogue:
    if player.has_picked_up_item("master_key"):
        if M_bissette.is_state(S_bissette_roxxy_pom_poms):
            if player.has_item("pompoms"):
                jump expression game.dialog_select("coachs_office_locker_peeking")
            else:

                call expression game.dialog_select("coachs_locker_bissette_roxxy_pom_poms")
        python:
            for image in renpy.get_showing_tags():
                renpy.hide(image)
        call screen coachs_locker
    else:

        if M_bissette.is_state(S_bissette_roxxy_pom_poms):
            call expression game.dialog_select("coachs_locker_locked_bissette_roxxy_pom_poms")
        else:

            call expression game.dialog_select("coachs_locker_locked")
    $ game.main()

label coachs_locker_bissette_roxxy_pom_poms:
    show coach_locker
    player_name "Lá estão elas!"
    return

label coachs_locker_locked_bissette_roxxy_pom_poms:
    show expression game.timer.image("coach_office{}_b")
    show player 12 with dissolve
    player_name "Eu aposto que elas estão naquele armário."
    player_name "Parece que vou precisar de uma chave para entrar."
    hide player with dissolve
    return

label coachs_locker_locked:
    show expression game.timer.image("coach_office{}_b")
    show player 1 with dissolve
    player_name "O armário da treinadora Bridget está trancado. Eu não posso abri-lo porque não tenho a chave."
    hide player with dissolve
    return

label coachs_office_roxxy_pom_poms_right_time:
    show player 30 with dissolve
    player_name "Tudo bem, ela não está aqui."
    show player 14
    player_name "Esta é minha chance de encontrar aqueles {b}Pom Poms{/b}!"
    show player 3f with dissolve
    player_name "..."
    show player 38 at Position (xoffset=41) with dissolve
    player_name "Agora onde eles poderiam estar?"
    hide bridget
    hide player
    with dissolve
    return

label coachs_office_roxxy_pom_poms_wrong_time:
    show bridget a_dressed_sides f_normal at right
    show player 23 at left
    with dissolve
    player_name "Oh porcaria! Ela está aqui!"
    show player 22
    show bridget a_dressed_sides f_suspicious
    bri "Posso ajudar?"
    show bridget a_dressed_sides f_normal
    show player 10
    player_name "Err, umm..."
    show player 11
    show bridget a_dressed_sides f_suspicious
    bri "sim?"
    show bridget a_dressed_sides f_normal
    show player 21
    player_name "Não, eu estava apenas..."
    show player 27
    show bridget a_dressed_sides f_suspicious_right
    bri "..."
    show bridget a_dressed_sides f_normal
    show player 29
    show xtra 21 at left
    with dissolve
    player_name "Com licença, preciso usar o banheiro!"
    hide player
    hide xtra
    with dissolve
    show bridget a_dressed_sides f_suspicious
    bri "Que esquisito..."
    hide bridget
    hide player
    with dissolve
    return

label coachs_office_roxxy_pom_poms:
    scene expression game.timer.image("coach_office{}_b")
    if game.timer.is_morning():
        call expression game.dialog_select("coachs_office_roxxy_pom_poms_right_time")
    else:

        call expression game.dialog_select("coachs_office_roxxy_pom_poms_wrong_time")
        $ player.go_to(L_school_righthallway)
    return

label coach_locker_pom_poms:
    show coach_locker
    player_name "Impressionante!"
    call expression game.dialog_select("coach_locker_pom_poms_dialogue")
    $ player.get_item("pompoms")

    $ player.location.call_screen(False)

label coach_locker_pom_poms_dialogue:
    show expression "boxes/popup_item_pompom1.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_item_pompom1.png" with dissolve

    scene expression game.timer.image("coach_office{}_b")
    show player 14 with dissolve
    player_name "Agora eu só preciso voltar para {b}Rox{/b}"
    show player 11
    bri "Sim Sim! Apenas vá para a pista e eu te encontro lá."
    bri "Preciso mudar primeiro."
    show player 22
    player_name "!!!" with hpunch
    show player 23
    player_name "Oh porcaria! Ela está vindo!"
    player_name "Eu estou tão morto! O que eu vou fazer!?"
    player_name "Eu tenho que me esconder em algum lugar!"
    hide player with dissolve
    return

label coachs_office_locker_hide_fail:
    call expression game.dialog_select("coachs_office_locker_hide_fail_dialogue")

    $ M_bissette.trigger(T_bissette_bridget_pompoms_steal)
    $ player.go_to(L_school_righthallway)
    $ game.main()

label coachs_office_locker_hide_fail_dialogue:
    scene expression game.timer.image("coach_office{}_b")
    show bridget a_dressed_crossed f_angry_talk
    show player 22 at left
    with dissolve
    bri "O que você esta fazendo aqui?"
    show bridget a_dressed_crossed f_angry
    show player 23
    player_name "Eu ... Uh..."
    show player 29 with dissolve
    player_name "Isto ... não é o banheiro?"
    show player 22 with dissolve
    show bridget a_dressed_crossed f_angry_yell
    bri "Tire sua bunda magricela daqui!"
    show bridget a_dressed_crossed f_angry
    show player 23
    player_name "Saindo!"
    hide player with dissolve
    show bridget a_dressed_sides f_suspicious with dissolve
    bri "Esquisito."
    hide bridget with dissolve
    return

label coachs_office_locker_peeking:
    call expression game.dialog_select("coachs_office_locker_peeking_dialogue")

    $ M_bissette.trigger(T_bissette_bridget_pompoms_steal)
    $ game.main()

label coachs_office_locker_peeking_dialogue:
    scene expression game.timer.image("coach_office{}_b")
    show player 10 with dissolve
    player_name "Este é o único lugar para se esconder!"
    player_name "Eu só tenho que esperar que ela não olhe aqui."
    hide player with dissolve

    scene coach_locker_cs1
    with fade
    show text "Foi um ajuste apertado, mas eu consegui entrar no armário e fechar a porta.\nBem a tempo também, {b}Treinadora Bridget{/b} quase me pegou!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve

    scene coach_locker_cs2
    with fade
    show text "Tudo o que eu podia fazer agora era ficar quieto e torcer para que ela não me encontrasse." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve

    scene coach_locker_peek
    show bridget a_dressed_crossed f_normal
    show coach_locker_peek_overlay
    with dissolve
    player_name "( Lá está ela! )"
    player_name "( Por favor, não olhe aqui... )"
    pause
    show bridget a_dressed_crossed f_normal_talk
    bri "Cara, com certeza está cozinhando lá fora."
    bri "Estou suando como uma prostituta na igreja!"
    show bridget b_undress f_empty a_empty with dissolve
    player_name "( Ela está se despindo! )"
    player_name "( Eu estou tão morto se ela me encontrar! )"
    show bridget b_lingerie a_lingerie_undress_top with dissolve
    pause
    show bridget a_lingerie_hips f_pleased_down with dissolve
    bri "Mmm, Espero que você esteja prestando atenção!"
    player_name "( Ela sabe?! )"
    pause
    show bridget a_lingerie_flex f_pleased_down_left with dissolve
    bri "Eu odiaria que você perdesse o show de armas!"
    player_name "( ... )"
    pause
    bri "Menina maldita!"
    bri "Melhor colocá-los fora antes que machuquem alguém."
    show bridget a_lingerie_undress_top with dissolve
    player_name "( Que esquisito... )"
    show bridget b_undress f_empty a_empty with dissolve
    pause
    show bridget b_dressed a_dressed_sides f_suspicious_right with dissolve
    pause
    show bridget a_dressed_sides f_suspicious
    bri "Hã. Pensei ter ouvido algo."
    bri "Deve ter sido minha imaginação..."
    hide bridget with dissolve
    pause
    pause
    player_name "( Eu acho que ela se foi. )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
