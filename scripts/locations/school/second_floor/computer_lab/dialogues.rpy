label printer_dialogue_bissette_scan_missing_pages:
    show xtra 40
    show player 520 at Position (xpos=375) with dissolve
    player_name "Ok, agora eu apenas coloco o livro aqui..."
    player_name "E aperto...."
    player_name "O botão!"
    player_name "..."
    player_name "..."
    player_name "Carta de carregamento do PC? Que diabos isso significa?"
    player_name "Talvez eu deva {b}perguntar alguém aqui{/b} como fazer isso funcionar."
    hide player with dissolve
    return

label printer_dialogue_bissette_print_poem_assignment:
    show player 518 at left with dissolve
    player_name "Impressão!"
    show player 519 with vpunch
    show xtra_paper 39 at Position (xoffset=100) with dissolve
    pause .25
    hide xtra_paper 39 with dissolve
    show player 184 with dissolve
    pause    
    show player 386 with dissolve
    player_name "Tudo bem! Agora para entregar meu poema em francês."
    hide player with dissolve
    return

label printer_dialogue_nothing:
    show player 4 at left with dissolve
    player_name "Não tenho nada que eu precise imprimir no momento."
    hide player with dissolve
    return

label printer_dialogue:
    scene computer_room_printer_c
    if M_bissette.is_state([S_bissette_scan_missing_pages, S_bissette_fix_printer]):
        call expression game.dialog_select("printer_dialogue_bissette_scan_missing_pages")
        $ M_bissette.trigger(T_bissette_broken_printer)

    elif M_bissette.is_state(S_bissette_print_poem_assignment):
        call expression game.dialog_select("printer_dialogue_bissette_print_poem_assignment")
        $ M_bissette.trigger(T_bissette_print_assignment)
    else:

        call expression game.dialog_select("printer_dialogue_nothing")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
