label home_lock_check(destination_screen, destination_label):
    $ temp_bg = player.location.background_blur

    if M_mom.is_set("bedroom locked") and destination_screen == "Master Bedroom":
        scene expression temp_bg
        if not game.timer.is_dark():
            if not erik.over(erik_intro):
                show player 22 at left
                show debbie 2 at right
                with dissolve
                deb "{b}[firstname]{/b}? Você está procurando algo no meu quarto?"
                show player 21 at left
                show debbie 1 at right
                player_name "Eu estava ... Umm ... Procurando pelo meu celular!"
                show player 18 at left
                player_name "Mas está bem aqui no meu bolso, na verdade!"
                show debbie 3 at right
                show player 11 at left
                deb "Não é {b}Erik{/b} Esperando Por Você?"
                show debbie 1 at right
                show player 17 at left
                player_name "Sim, estou a caminho!"
            else:

                show player 10 with dissolve
                player_name "( Eu não deveria bisbilhotar {b}[deb_name]{/b} no quarto. )"
            $ game.main()
        else:


            if M_mom.is_state(S_mom_debt_call):
                show player 10 with dissolve
                player_name "( Eu deveria ver se {b}[deb_name]{/b} está bem. )"
            else:

                show player 10 with dissolve
                player_name "( Eu realmente não deveria incomodar {b}[deb_name]{/b} quando ela está dormindo. )"
            $ game.main()
        hide player
        hide debbie
        with dissolve

    elif M_jenny.get("girlfriend_in_progress") and destination_screen in ("Upstairs Bedroom", "Master Bedroom"):
        scene expression temp_bg
        show player with dissolve
        player_name "( Não, {b}[jen_name]{/b} foi {b}no meu quarto{/b}, eu acho que... )"
        player_name "( Eu deveria segui-la. )"
        hide player with dissolve

    elif (M_mom.is_state([S_mom_romance_movie, S_mom_romance_movie_two]) or (M_mom.is_set("movie night") and game.timer.is_dark())) and destination_screen == "Living Room TV":
        jump mom_movie_night

    elif M_mia.is_state(S_mia_midnight_call, S_mia_urgent_message) and game.new_message and player.location == L_home_bedroom:
        scene expression temp_bg
        if not game.timer.is_dark():
            show player 12 with dissolve
        else:
            show player 101 with dissolve
        player_name "Eu deveria checar minhas mensagens de texto."

    elif M_bissette.is_state(S_bissette_roxxy_jenny_spying) and destination_screen not in ["Hallway", "Upstairs Bedroom"]:
        scene expression temp_bg
        show player 10 with dissolve
        player_name "Eu deveria verificar {b}Roxxy{/b} e {b}[jen_name]{/b}..."
        hide player with dissolve

    elif M_mom.is_state(S_mom_note) and player.location == L_home_bedroom and destination_screen not in ["MC Computer"]:
        scene expression temp_bg
        show player 10 with dissolve
        player_name "( Eu deveria ver o que está nesse {b}bilhete{/b}. )"
        hide player with dissolve

    elif not ( L_home_sisbedroom.is_here(M_jenny) or not L_home_sisbedroom.locked ) and destination_screen == "Upstairs Bedroom":
        scene expression temp_bg
        show player 12 with dissolve
        play audio sfxDoor(True)
        player_name "( A porta dela está trancada... )"
        hide player with dissolve

    elif M_jenny.is_state(S_jenny_pissed_at_handjob, S_jenny_pissed_at_blowjob) and destination_screen == "Upstairs Bedroom":
        $ player.go_to(L_home_hallway)
        show expression player.location.background_closeup with None
        show player f_worried with dissolve
        player_name "( Está trancado. )"
        show player f_worried_talk
        player_name "{b}[jen_name]{/b}?"
        show player f_worried
        jen "Vá embora, idiota!"
        player_name "( Hmm, Eu acho que ela ainda está chateada comigo. )"
        pause
        player_name "( eu deveria tentar {b}falar com ela de manhã enquanto ela está tomando café da manhã{/b}. )"
        hide player with dissolve

    elif M_diane.is_state(S_diane_peeking_masturbate):
        scene expression temp_bg
        show player 427b at Position (xoffset=50) with dissolve
        player_name "Eu não posso sair com essa coisa."
        player_name "{b}Eu deveria me masturbar e limpar minha cabeça.{/b}"
        hide player with dissolve

    elif M_diane.is_state(S_diane_get_dirty_with_debbie) and destination_screen not in ["Bedroom", "Hallway", "Entrance", "Living Room", "Master Bedroom"]:
        scene expression temp_bg
        show player 10 with dissolve
        player_name "Eu deveria seguir {b}[deb_name]{/b}."
        player_name "Eu acho que ela entrou em seu quarto."
        hide player with dissolve

    elif M_diane.is_state(S_diane_3way_aftermath) and destination_screen not in ["Master Bedroom", "Living Room", "Entrance", "Kitchen"]:
        scene expression temp_bg
        show player 14 with dissolve
        player_name "Eu deveria ver o que {b}[deb_name]{/b}está cozinhando{b}na cozinha{/b}."
        hide player with dissolve
    else:

        if player.location == L_home and destination_screen in ["Home Entrance", "Garage"]:
            $ playSound()
            play audio sfxDoor()
        if player.location in [L_home_entrance, L_home_hallway]:
            $ playSound()
        if destination_screen in ["Master Bedroom", "Upstairs Bedroom", "Shower", "Bedroom"]:
            play audio sfxDoor()
        if player.location in [L_home_bedroom, L_home_sisbedroom, L_home_shower, L_home_mombedroom] and destination_screen in ["Hallway", "Living Room"]:
            play audio sfxDoor()
        jump expression destination_label

    hide jersey
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
