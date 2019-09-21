label dexter_court_dialogue:
    scene expression player.location.background_blur
    if M_roxxy.get("roxxy relationship") == 0:
        call expression game.dialog_select("button_dexter_intro_beginning")
        $ game.main()
    else:
        if M_roxxy.get("roxxy relationship") == 5:
            call expression game.dialog_select("button_dexter_intro_final")
        else:
            call expression game.dialog_select("button_dexter_intro")
        menu:
            "Show de talentos." if M_dewitt.is_set("talent ask dexter"):
                if M_dewitt.is_set("talent helping kevin"):
                    call expression game.dialog_select("dewitt_talent_show_helping_kevin")

                elif M_dewitt.is_set("talent helping eve"):
                    call expression game.dialog_select("dewitt_talent_show_helping_eve")
                else:

                    call expression game.dialog_select("button_dexter_talent_show")
                    $ M_dewitt.set("talent ask dexter", False)

            "Desafio." if player.location == L_basketball_court:
                call expression game.dialog_select("button_dexter_challenge")
                $ M_dexter.trigger(T_dex_challenge)

            "Flexões." if M_roxxy.is_state(S_roxxy_do_pushups_intro, S_roxxy_do_pushups):
                if M_roxxy.is_state(S_roxxy_do_pushups):
                    call expression game.dialog_select("dexter_button_pushups")
                    call screen pushups_minigame
                else:
                    call expression game.dialog_select("dexter_button_pushups_rematch")
                    call screen pushups_minigame

            "Livro da biblioteca." if M_bissette.between_states(S_bissette_jane_return_books, [S_bissette_got_eriks_martinez_books, S_bissette_got_martinez_eriks_books]) and not M_bissette.is_set("dexters book search"):
                call expression game.dialog_select("button_dexter_library_book")
            "Ainda jogando basquete":

                if M_roxxy.get("roxxy relationship") == 5:
                    call expression game.dialog_select("button_dexter_basketball_final")
                else:
                    call expression game.dialog_select("button_dexter_basketball")
            "comportando-se?" if M_roxxy.get("roxxy relationship")==5:
                call expression game.dialog_select("button_dexter_behaving_yourself")

            "Corra ao longo agora." if M_roxxy.get("roxxy relationship")==5:
                call expression game.dialog_select("button_dexter_run_along")

            "Tanto faz." if M_roxxy.get("roxxy relationship") < 5:
                call expression game.dialog_select("button_dexter_whatever")
    hide dexter
    hide player
    with dissolve
    $ game.main()
# TRADUZIDO
