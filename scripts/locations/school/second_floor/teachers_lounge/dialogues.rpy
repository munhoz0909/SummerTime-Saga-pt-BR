label teachers_lounge_first_visit:
    scene expression game.timer.image("backgrounds/location_school_lounge{}_blur.jpg") with fade
    show player 14 with dissolve
    player_name "Este deve ser o salão dos professores."
    player_name "Seu pequeno refúgio privado de meus colegas."
    hide player with dissolve
    return

label teachers_lounge_okita_dose_smith:
    scene location_school_lounge_day_blur
    show player 11
    player_name "( Lá está ela! tomando café como eu pensava. )"
    player_name "( Eu só preciso dar uma dose na cafeteira! )"
    return

label coffee_pot_dialogue_wrong_time:
    scene location_school_lounge_day_blur
    show player 11
    player_name "( Eu não posso fazer isso enquanto ela está sentada lá... )"
    return

label coffee_pot_dialogue_right_time:
    scene expression "backgrounds/location_school_lounge_cutscene01.jpg"
    with fade
    show text "Este parecia ser o melhor curso de ação." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Eu sabia que a {b}Diretora Smith{/b} bebia café desse pote todas as tardes." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "E desde que foi sintetizado usando o DNA dela, não deveria afetar ninguém." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Pelo menos, é o que eu esperava." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    return

label coffee_pot_dialogue:
    if M_okita.is_state(S_okita_dose_smith):
        if game.timer.is_afternoon():
            call expression game.dialog_select("coffee_pot_dialogue_wrong_time")

        elif game.timer.is_morning():
            call expression game.dialog_select("coffee_pot_dialogue_right_time")
            $ M_okita.trigger(T_okita_dosed_smith)
    $ player.go_to(L_school_teacherslounge)
    $ game.main()

label smith_lounge_dialogue:
    scene expression game.timer.image("backgrounds/location_school_lounge_day{}_blur.jpg")
    show player 22 at left
    show principal 33 at right
    with dissolve
    player_name "( Oh porcaria! a diretora Smith está aqui! )"
    show player 11
    show principal 31 with dissolve
    player_name "( ... )"
    show principal 32
    smi "{b}[firstname]{/b}?"
    smi "O que você está fazendo na sala dos professores?!"
    show player 10
    show principal 31
    player_name "eu só estava!"
    show player 11
    show principal 32
    smi "Os estudantes não estão autorizados a estar aqui!"
    smi "Volte imediatamente para a sua aula ou expulsarei você!"
    show player 10
    show principal 31
    player_name "Sim, senhora!"
    $ player.go_to(L_school_floor2)
    $ game.main()

label microwave_dialogue:
    scene expression game.timer.image("backgrounds/location_school_lounge_microwave{}.jpg")
    player_name "Uma maçã?!" with hpunch
    player_name "Por que alguém cozinharia maçãs em microondas..."
    $ A_apple.unlock()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
