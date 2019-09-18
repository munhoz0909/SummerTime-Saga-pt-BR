label sis_computer_locked:
    scene expression "backgrounds/location_computer_jenny_01.jpg"
    player_name "( Hmm... Ela tem uma {b}senha{/b}... )"
    return

label sis_computer_locked_diary_locked:
    player_name "( Eu deveria tentar descobrir a senha. )"
    return

label sis_computer_locked_diary_unlocked:
    player_name "( Vamos ver se consigo entrar no computador dela... )"
    return

label sis_computer_unlocked_unread_email:
    player_name "( Eu deveria procurar outros segredos que ela possa ter aqui... )"
    return

label sispc_desktop_response:
    scene jenny_computer_bg with None
    player_name "Funcionou!"
    player_name "eu imagino o que {b}[jen_name]{/b} tem no seu computador..."
    return

label sispc_nude_response:
    if sispc_nude_seen == False:
        call expression game.dialog_select("sispc_nude_response_dialogue")
        $ sispc_nude_seen = True
    show screen sis_computer
    show screen sis_recycle
    call screen sis_picture(3)

label sispc_nude_response_dialogue:
    scene jenny_computer_bg
    show jenny_computer_nude
    with None
    player_name "!!!" with hpunch
    player_name "É... {b}Dela{/b}?!"
    return

label sispc_family_response:
    if sispc_family_seen == False:
        call expression game.dialog_select("sispc_family_response_dialogue")
        $ sispc_family_seen = True
    show screen sis_computer
    show screen sis_family
    call screen sis_picture(5)

label sispc_family_response_dialogue:
    scene jenny_computer_bg
    show jenny_computer_family
    with None
    player_name "( Eu nunca soube que ela tinha essa foto. )"
    player_name "( eu sinto sua falta  {b}pai{/b}... )"
    return

label sispc_swimsuit_response:
    if sispc_swimsuit_seen == False:
        call expression game.dialog_select("sispc_swimsuit_response_dialogue")
        $ sispc_swimsuit_seen = True
    show screen sis_computer
    show screen sis_newfolder
    call screen sis_picture(1)

label sispc_swimsuit_response_dialogue:
    scene jenny_computer_bg
    show jenny_computer_swimsuit
    with None
    player_name "( Ela adora tirar fotos de si mesma... )"
    return

label sispc_igor_response:
    if sispc_igor_seen == False:
        call expression game.dialog_select("sispc_igor_response_dialogue")
        $ sispc_igor_seen = True
    show screen sis_computer
    show screen sis_family
    call screen sis_picture(4)

label sispc_igor_response_dialogue:
    scene jenny_computer_bg
    show jenny_computer_igor
    with None
    player_name "..."
    player_name "( Eu acho que já vi esse cara antes. )"
    player_name "( Ele costumava trabalhar com meu {b}pai{/b}... )"
    return

label sispc_summertime_response:
    if sispc_summertime_seen == False:
        call expression game.dialog_select("sispc_summertime_response_dialogue")
        $ sispc_summertime_seen = True
    show screen sis_computer
    call screen summertime_error

label sispc_summertime_response_dialogue:
    scene jenny_computer_bg
    show jenny_computer_summertime
    with None
    player_name "( Cara ... este jogo {b}sempre{/b} tem erros. )"
    return

label sispc_toylist_response:
    if sispc_toylist_seen == False:
        call expression game.dialog_select("sispc_toylist_response_dialogue")
        $ sispc_toylist_seen = True
    show screen sis_computer
    call screen sis_list

label sispc_toylist_response_dialogue:
    scene jenny_computer_bg
    show jenny_computer_toylist
    with None
    player_name "( Parece uma lista de... {b}brinquedos{/b}? )"
    return

label sispc_livecrush_response:
    if sispc_livecrush_seen == False:
        call expression game.dialog_select("sispc_livecrush_response_dialogue")
        $ sispc_livecrush_seen = True
    show screen sis_computer
    call screen jenny_camslut

label sispc_livecrush_response_dialogue:
    scene jenny_computer_bg
    show jenny_computer_livecrush
    with None
    player_name "( {b}[jen_name]{/b} tem um perfil no LiveCrush?! )"
    player_name "Uau..."
    player_name "( Ela fez {b}shows ao vivo{/b} no quarto dela? )"
    player_name "( Ela deve ter muito cuidado em manter isso em segredo; Eu não fazia ideia... )"
    return

label sispc_email_response:
    if sispc_email_seen == False:
        call expression game.dialog_select("sispc_email_response_dialogue")
        $ sispc_email_seen = True
    show screen sis_computer
    call screen sis_email

label sispc_email_response_dialogue:
    scene jenny_computer_bg
    show jenny_computer_email
    with None
    player_name "( Eu não sei Se eu deveria passar por estes... )"
    return

label sispc_email04_response:
    if sis_email_04_read == False:
        call expression game.dialog_select("sispc_email04_response_dialogue")
        $ sis_email_04_read = True
    show screen sis_computer
    call screen sis_email

label sispc_email04_response_dialogue:
    player_name "( {b}[jen_name]{/b} tem uma conta rosa ?! Ela assistir canal adulto de TV a cabo quando todos estão dormindo. )"
    player_name "( Eu deveria checar se ela está lá embaixo à noite. )"
    return

label sispc_password_reminder:
    scene jennybedroom_night
    show player 35 at left
    player_name "( Se bem me lembro, a senha estava em seu diário... )"
    jump expression game.dialog_select("sis_bedroom_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
