label office_dialogue:
    $ player.go_to(L_school_smithoffice)
    if M_diane.is_state(S_diane_delivery_3_fetch_invoice):
        call expression game.dialog_select("principals_office_delivery_invoice")
        $ M_diane.trigger(T_diane_delivery_3_got_invoice)

    elif M_dewitt.is_state([S_dewitt_paint_trail, S_dewitt_check_up]):
        call expression game.dialog_select("principals_office_dewitt_paint_trail")
        $ player.go_to(L_school_floor3)
        $ M_dewitt.trigger(T_dewitt_clue_dead_end)

    elif M_dewitt.is_state(S_dewitt_smith_office_trap):
        call expression game.dialog_select("principals_office_dewitt_smith_office_trap")
        $ player.remove_item("sticky_tape")
        $ player.go_to(L_map)

        $ game.timer.tick()
        $ M_dewitt.trigger(T_dewitt_trap_set)

    elif M_dewitt.is_state(S_dewitt_trap_check_up):
        call expression game.dialog_select("principals_office_dewitt_trap_check_up")
        $ player.go_to(L_school_floor3)
        $ M_dewitt.trigger(T_dewitt_trap_check_ok)

    elif M_dewitt.is_state(S_dewitt_office_night_visit_delay):
        call expression game.dialog_select("principals_office_dewitt_office_night_visit_delay")
        $ player.go_to(L_school_floor3)

    elif M_okita.is_state(S_okita_get_keycode) and game.timer.is_morning():
        call expression game.dialog_select("principals_office_okita_get_keycode_morning")
        $ player.go_to(L_school_floor3)
        $ game.main()

    elif M_okita.is_state(S_okita_get_keycode) and game.timer.is_afternoon():
        call expression game.dialog_select("principals_office_okita_get_keycode_afternoon")

    elif M_okita.is_state(S_okita_get_ingredients) and game.timer.is_morning():
        call expression game.dialog_select("principals_office_okita_get_ingredients_morning")
        $ player.go_to(L_school_floor3)
        $ game.main()

    elif M_latinas.is_state(S_latinas_caught):
        call expression game.dialog_select("principals_office_annie_trouble")
        $ persistent.cookie_jar["Annie"]["unlocked"] = True
        $ persistent.cookie_jar["Annie"]["gallery"]["01_unlocked"] = True
        $ M_latinas.trigger(T_latinas_annie_trouble)

    elif M_smith.is_state([S_smith_intro, S_smith_go_to_locker]):
        $ pass

    elif player.location.is_here(M_smith):
        if game.timer.is_dark():
            call expression game.dialog_select("principals_office_no_entry_night")
        else:
            call expression game.dialog_select("principals_office_no_entry")
        $ player.go_to(L_school_floor3)
        $ game.main()
    $ game.main()

label smith_office_smith_delivery_3_dialogue:
    scene expression "backgrounds/location_school_office_chair_closeup.jpg"
    show player 168b at left
    show titty 1f at right
    show principal 27 at Position (xpos=614)
    with dissolve
    smi "Pare de olhar para o rei e leve a entrega para a cafeteria!"
    show principal 26
    show player 168c
    player_name "Sim, senhora!"
    hide player
    hide titty
    hide principal
    with dissolve
    $ game.main()

label smith_office_ronda_delivery_3_dialogue:
    scene expression "backgrounds/location_school_office_chair_closeup.jpg"
    show annie 6 zorder 3 at right
    show ronda b_chair1 a_empty f_chair_upset zorder 1 at Position (ypos=830)
    show player 427f zorder 2 at Position (xpos=700)
    with dissolve
    player_name "Oi {b}Ronda{/b}..."
    show player 433f
    show ronda f_chair_upset_talk
    with dissolve
    ron "Tire-me daqui!"
    show ronda f_chair_upset
    show player 427f with dissolve
    player_name "Não se preocupe, eu vou tirar você daqui."
    show ronda f_chair_surprised_down
    show player 670bf at Position (xoffset=-140)
    with dissolve
    player_name "Deixe-me apenas..."
    show ronda b_chair2 f_chair_hurt_down
    show player 670d at Position (xoffset=-218)
    with dissolve
    pause
    show ronda f_chair_surprised_down
    show player 670b zorder 0 at Position (xoffset=-740) with dissolve
    with dissolve
    ron "... Obrigada."
    show ronda f_chair_hurt_talk_down
    ron "Ugh, isso é tão embaraçoso..."
    show ronda f_chair_hurt_down
    show annie 5
    ann "Oh, não seja tão dramática!"
    show ronda f_chair_upset
    ann "Não é tão ruim."
    show annie 6
    show ronda f_chair_upset_angry
    ron "Vocês todas são algumas pessoas confusas!"
    show ronda f_chair_upset
    show annie 3
    ann "Ela pode fazer muito pior, você sabe..."
    show annie 5
    ann "... Eu recomendaria que ela te amordaçasse."
    show annie 6
    show ronda f_chair_upset_talk
    ron "Putinha assustadora..."
    show ronda f_chair_upset
    show annie 4
    ann "Eu ouvi isso!"
    show annie 6
    show ronda f_chair_upset_angry
    ron "Oh, sim?! Você tem sorte que eu estou amarrada agora!"
    ron "Caso contrário, eu iria tirar esse olhar presunçoso da sua cara estúpida!"
    show ronda f_chair_upset
    player_name "Vocês duas, por favor, cale a boca!"
    player_name "Já é difícil tentar desatar isso sem vocês duas me distraírem!"
    ron "..."
    player_name "Consegui!"
    show ronda b_chair3 with dissolve
    show player 433f at Position (xpos=700) with dissolve
    pause
    hide ronda
    show ronda shirt_on
    with dissolve
    pause
    show ronda a_casual_box f_upset_talk at flip with dissolve
    show player 11f
    ron "estou fora daqui."
    ron "É melhor você rezar para que meu pai não descubra isso!"
    show ronda f_upset
    smi "{b}*Snobar*{/b} Como aquele simplório gordo pode fazer alguma coisa!"
    show annie 7
    ann "Hahaha!"
    show ronda f_upset_talk
    ron "Grrr!!!!"
    hide ronda with dissolve
    pause
    show player 10f
    show annie 6
    player_name "{b}Ronda{/b}, espere!"
    hide player with dissolve
    pause
    show annie 3f at center with dissolve
    ann "{b}Diretora Smith{/b}, Vou garantir que eles entreguem-"
    show annie 1f
    smi "Ah, ah, ah!"
    smi "Você não vai a lugar nenhum até ter sido devidamente punido por invadir aqui."
    show annie 10f
    ann "O claro, senhora."
    hide annie with dissolve
    scene expression "backgrounds/location_school_cafeteria_day_blur.jpg"
    show ronda a_casual_box f_normal_talk at flip
    show ronda at Position (xpos=-100)
    show player 13f zorder 1 at right
    with dissolve
    ron "Mais uma vez obrigada por me tirar de lá, {b}[firstname]{/b}."
    show ronda f_normal a_casual_sides with dissolve
    show player 14f
    player_name "Sem problema."
    show player 10f
    player_name "O que você fez?"
    show player 5f
    show ronda f_normal_talk
    ron "Ugh, Eu estava no escritório da {b}treinadora Bridget{/b} , e {b}Sra. Smith{/b} entra gritando se eu tinha permissão para estar lá ou não."
    ron "eu disse a ela, A {b}Treinadora{/b} deixa eu usar o equipamento dela o tempo todo, mas ela não acreditou em mim."
    ron "A próxima coisa que lembro, É que estou amarrada no escritório dela, E que a psicopata estava puxando meu sutiã para baixo!"
    show ronda f_normal
    show player 10f
    player_name "Sim, ela é bem estranha..."
    show player 12f
    player_name "Me fala seu pai é o chefe de polícia?!"
    show player 5f
    show ronda f_normal_talk
    ron "Sim por que?"
    show ronda f_normal
    show player 12f
    player_name "Então, por que você não conta a ele sobre todas as coisas inapropriadas {b}Mrs. Smith{/b} faz por aqui?!"
    player_name "Certamente ele poderia ajudar-"
    show player 11f
    show ronda f_normal_talk
    ron "Não, eu não quero incomodá-lo com isso."
    ron "Ele já tem o suficiente no prato, confie em mim."
    show ronda f_normal
    show player 4f with dissolve
    pause
    show player 10f with dissolve
    player_name "Oh."
    show player 401f
    player_name "Ok..."
    show player 13f
    show kevin 9b zorder 0 at Position (xpos=600) with dissolve
    kev "Mano!"
    show kevin 19 at Position (xoffset=-95) with dissolve
    kev "É esse o novo leite para a cafeteria?"
    show kevin 23f at Position (xoffset=-50) with dissolve
    show player 14f
    player_name "Ei, {b}Kevin{/b}."
    player_name "Sim, é isso."
    show player 13f
    show kevin 40 at Position (xoffset=-58) with dissolve
    kev "Direito em!"
    show kevin 42 at Position (xoffset=-47) with dissolve
    pause
    show kevin 41 at Position (xoffset=-113) with dissolve
    kev "Uau, isso é delicioso!"
    show kevin 39 at Position (xoffset=-58) with dissolve
    show player 14f
    player_name "Eu sei direito?"
    show player 13f
    show kevin 38 at Position (xoffset=-58)
    kev "Você tentou essas coisas?"
    show kevin 23
    show ronda a_casual_milk
    with dissolve
    pause
    show ronda f_drink a_casual_milk_drink with dissolve
    pause
    show ronda f_surprised a_casual_milk with dissolve
    ron "!!!"
    show ronda f_surprised_down
    ron "Mmm!"
    ron "Oh meu Deus, isso seria incrível em um shake de proteína!"
    show ronda f_drink a_casual_milk_drink with dissolve
    show kevin 9b
    kev "Totalmente!"
    show kevin 23
    show ronda f_normal a_casual_milk with dissolve
    show player 14f
    player_name "Então, quem deveria me pagar por isso?"
    show player 13f
    show kevin 9bf at Position (xoffset=-127) with dissolve
    kev "eu entendi você."
    show kevin 43f zorder 2 at Position (xoffset=-50) with dissolve
    pause
    show kevin 23f zorder 0 at Position (xoffset=-127)
    show player 640ef at Position (xoffset=-9)
    with dissolve
    player_name "Obrigado!"
    show player 13f
    show ronda f_normal_talk
    show kevin 23
    with dissolve
    ron "Você pode me trazer mais disso?"
    show ronda f_normal
    show player 14f
    player_name "Hehe, você terá que pedir minha amiga."
    player_name "Ela é quem faz isso."
    show player 13f
    show kevin 9b
    kev "Eu tenho o número dela na cozinha."
    kev "Vamos eu tenho que entregar o próximo pedido de qualquer maneira."
    show kevin 23
    show ronda f_normal_talk
    ron "Logo atrás de você."
    show ronda f_normal
    show player 14f
    player_name "Vou deixar vocês..."
    show player 13f
    show kevin 9bf at Position (xoffset=-127) with dissolve
    kev "Tchau!"
    show kevin 23f at Position (xoffset=-127)
    show ronda f_normal_talk a_casual_milk_wave with dissolve
    ron "Até mais, {b}[firstname]{/b}."
    show ronda f_normal
    show player 14f
    player_name "Até mais."
    hide ronda
    hide player
    hide kevin
    with dissolve
    $ player.remove_item("milk_carton")
    $ M_diane.trigger(T_diane_delivery_3_finished)
    $ player.go_to(L_school_cafeteria)
    $ game.unlock_ui()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
