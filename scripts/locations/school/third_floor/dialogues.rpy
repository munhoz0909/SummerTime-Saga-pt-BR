label okita_office_door:
    $ player.go_to(L_school_floor3)
    if M_okita.is_set("office locked"):
        if player.has_item("keycode_note"):
            call screen okita_keypad
        else:

            call expression game.dialog_select("okita_office_door_need_keycode")
    else:

        if M_okita.is_state(S_okita_tired_from_belt):
            call expression game.dialog_select("okita_office_door_okita_tired")
        else:

            jump expression game.dialog_select("mrs_okitas_office_dialogue")
    $ game.main()

label okita_office_door_need_keycode:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10
    with dissolve
    player_name "Hmm, eu acho que {b}Miss Okita{/b} mantém seu escritório trancado quando ela não está lá dentro?"
    player_name "Também possui um desses bloqueios automatizados de teclado."
    show player 11
    pause
    show player 10
    player_name "Definitivamente, não vou chegar lá sem um {b}Código chave{/b}."
    return

label okita_office_door_okita_tired:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10
    with dissolve
    player_name "Eu deveria deixá-la descansar por enquanto."
    return

label okita_office_unlock:
    $ M_okita.set("office locked", False)
    jump expression game.dialog_select("mrs_okitas_office_dialogue")

label okita_office_locked:
    $ player.go_to(L_school_floor3)
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10
    with dissolve
    player_name "Oops! Esse não era o código certo..."
    show player 34
    player_name "Hmm, É melhor eu checar esse {b}Código chave{/b} na mesa da {b}Diretora Smith{/b} antes de tentar novamente."
    $ game.main()

label third_floor_okita_get_ingredients:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10 with dissolve
    player_name "Hmm, Eu preciso entrar no escritorio da {b}Diretora Smith{/b} novamente para procurar algum tipo de amostra de DNA..."
    player_name "Eu deveria entrar quando ela não estiver lá."
    return

label annie_enter_office_dialogue:
    $ player.go_to(L_school_floor3)
    if not M_okita.is_set("talked to annie"):
        call expression game.dialog_select("smith_office_annie_guarding")
        $ M_okita.set("talked to annie", True)
    else:

        call expression game.dialog_select("smith_office_annie_guarding_repeat")
        if player.has_required_chr(7):
            call expression game.dialog_select("smith_office_annie_guarding_distract_pass")
            $ player.go_to(L_school_smithoffice)
            $ game.main()
        else:

            call expression game.dialog_select("smith_office_annie_guarding_distract_fail")
    $ game.main()

label smith_office_annie_guarding_distract_pass:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 2 at left
    show annie 1 at right
    player_name "Acabei de ouvir seu ladrão se gabando lá embaixo perto do vestiário dos meninos..."
    show player 1
    show annie 3
    ann "O que? Mesmo!?"
    show player 2
    show annie 1
    player_name "Sim, e se você se apressar, você ainda pode pegá-lo..."
    show player 1
    show annie 3
    ann "O diretor Smith definitivamente me recompensará por isso!"
    ann "Você se importaria de vigiar esta porta para mim?"
    show player 2
    show annie 1
    player_name "De modo nenhum. Vá buscá-lo!"
    hide annie
    hide player
    show player 1f
    show annie 16 at left
    with dissolve
    ann "Ahahahahaah!"
    hide annie with dissolve

    show player 2f
    player_name "Bem, isso deve mantê-la ocupada por algum tempo..."
    player_name "Agora procuro no escritório alguma coisa que possa ter {b}DNA{/b} da {b}Diretora Smith{/b} ."
    return

label smith_office_annie_guarding_distract_fail:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10 at left
    show annie 1 at right
    player_name "[chr_warn]Ok..."
    player_name "[chr_warn]... Eu só estava procurando a {b}Diretora Smith{/b}."
    show player 11
    show annie 3
    ann "[chr_warn]Sim, bem, ela não está aqui."
    show annie 4
    ann "[chr_warn]Então saia!"
    show player 12
    show annie 1
    player_name "[chr_warn]Tudo bem, sheesh! Você não precisa colocar sua calcinha em um monte!"
    return

label smith_office_annie_guarding_repeat:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 11 at left
    show annie 3 at right
    with dissolve
    ann "Ninguém está passando por mim, {b}[firstname]{/b}!"
    return

label smith_office_annie_guarding:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10 at left
    show annie 1 at right
    with dissolve
    player_name "Annie, o que você está fazendo aqui?"
    show player 11
    show annie 3
    ann "Eu estou de vigiando o escritorio da {b}Diretora Smith{/b} enquanto ela estiver fora."
    show player 10
    show annie 1
    player_name "... Por quê?"
    show player 11
    show annie 3
    ann "Umm, porque ela me pediu Duh."
    show annie 1
    player_name "..."
    show annie 3
    ann "Ela disse que alguém continua se escondendo e vasculhando suas coisas."
    show annie 5
    ann "Você não sabia nada sobre isso, sabia?!"
    show player 10
    show annie 6
    player_name "Eu? Não, eu não sei nada sobre isso!"
    show player 11
    show annie 5
    ann "Uh huh..."
    show annie 3
    ann "Bem, quem quer que seja, {b}Não vai passar por mim!{/b}"
    show player 10
    player_name "Ok, boa sorte com isso..."
    hide annie with dissolve
    hide player
    show player 5 with dissolve
    player_name "( Eu tenho que entrar nesse escritório... )"
    show player 34
    player_name "( Talvez eu possa {b}enganá-la{/b} de alguma forma? )"
    return

label third_floor_roxxy_intro:
    scene expression game.timer.image("school_hall_third_floor{}_b")
    show player 30 with dissolve
    player_name "( ... )"
    player_name "( Parece {b}Roxxy{/b} está discutindo com alguns dos professores... )"
    show player 33
    player_name "( Eu deveria dar uma olhada! )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
