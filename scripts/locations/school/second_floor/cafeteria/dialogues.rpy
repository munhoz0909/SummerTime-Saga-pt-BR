label cafeteria_diane_delivery_3_drop_off_goods:
    scene cafeteria_b
    show player 164 at left with dissolve
    show annie 1 at right with dissolve
    player_name "Tudo feito!"
    show annie 9
    show player 163
    ann "..."
    show annie 3
    ann "{b}Diretora Smith{/b} tomou a {b}fatura{/b}?"
    show annie 1
    show player 164
    player_name "Sim, ela estava ... meio que ... ocupada. Mas ela disse que eu deveria dar a você."
    show annie 5
    show player 163
    ann "Entendo..."
    show annie 15
    show player 1
    ann "Eu vou tirar isso de você, então."
    show annie 14
    show player 17
    player_name "Obrigado, {b}Annie{/b}!"
    hide player
    hide annie
    with dissolve
    return

label cafeteria_erik_favor_not_known:
    scene cafeteria_b
    show player 2 at left with dissolve
    show kevin 1 at right with dissolve
    player_name "Ei, {b}Kevin{/b}!"
    show player 1 at left
    show kevin 2 at right
    kev "Ei cara..."
    show kevin 1 at right
    show player 10 at left
    player_name "Você está trabalando na cafetaria huh..."
    show kevin 2 at right
    show player 13 at left
    kev "Sim! Eu tenho mais dois meses dessa porcaria."
    show kevin 1 at right
    show player 17 at left
    player_name "Isso é péssimo."
    show kevin 2 at right
    show player 1 at left
    kev "Sim mas o que eu posso fazer?"
    kev "O {b}Dexter{/b} dando a vocês um tempo difícil no corredor?"
    show kevin 1 at right
    show player 24 at left
    player_name "Sim, ele e a {b}Roxxy{/b} estão sempre no nosso pé..."
    show player 26 at left
    player_name "Mas não é nada. Eu realmente não me importo com o que eles dizem."
    show kevin 3 at right
    show player 11 at left
    kev "Cara. Você tem que se defender."
    show kevin 1 at right
    show player 10 at left
    player_name "Prefiro evitá-lo, sabia?"
    player_name "Não faz sentido brigar com um cara com o dobro do meu tamanho."
    show kevin 3 at right
    show player 11 at left
    kev "Você não pode deixá-lo andar por cima de você. Como você vai sobreviver a faculdade assim??"
    show kevin 1 at right
    show player 24 at left
    player_name "Bem, eu sou muito fraco para fazer algo sobre isso."
    show kevin 4 at right
    show player 11 at left
    kev "Hmm... Talvez pudéssemos trabalhar em algo."
    show kevin 1 at right
    show player 10 at left
    player_name "O que você quer dizer?"
    show kevin 4 at right
    show player 1 at left
    kev "Bem, eu poderia ajudá-lo a malhar na {b}Academia{/b}..."
    kev "E mostrar alguns truques."
    show kevin 2 at right
    show player 34 at left
    kev "Mas você terá que {b}encontrar alguém para tomar o meu lugar{/b} na cafeteria."
    kev "Eu não aguento mais isso."
    show player 34 at left
    show kevin 1 at right
    player_name "Tudo bem! Eu posso tentar encontrar alguém que possa trocar com você."
    show kevin 2 at right
    show player 1 at left
    kev "Tudo bem cara. Eu tenho que voltar ao trabalho. Te vejo depois!"
    show kevin 1 at right
    show player 36 at left
    player_name "Até logo, {b}Kevin{/b}!"
    hide player
    hide kevin
    with dissolve
    return

label cafeteria_erik_favor_known_intro:
    scene cafeteria_b
    show player 2 at left with dissolve
    show kevin 1 at right with dissolve
    player_name "Ei, {b}Kevin{/b}!"
    show kevin 2 at right
    show player 1 at left
    kev "Ei cara..."
    kev "Você conseguiu encontrar alguém para assumir minhas tarefas na cafeteria?"
    return

label cafeteria_erik_favor_known_found_replacement:
    show player 14 at left
    show kevin 1 at right
    player_name "Acho que encontrei um substituto!"
    show kevin 2 at right
    show player 1 at left
    kev "Serio, cara! Fantástico!"
    kev "Quem está tomando o meu lugar?"
    show kevin 1 at right
    show player 17 at left
    player_name "O {b}Erik{/b}... E eu tive que suborná-lo..."
    show kevin 2 at right
    show player 1 at left
    kev "Haha! Bem, obrigado, cara!"
    kev "Agora eu posso passar mais tempo no {b}Ginasio{/b}!"
    show kevin 6 at right
    show player 11 at left
    kev "...E eu não vou precisar mais disso!"
    show kevin 5 at right
    show player 12 at left
    player_name "Essa coisa é desagradável..."
    show kevin 12 at right
    show player 1 at left
    kev "Ei! Se você estiver procurando por uma academia mano, saberá onde me encontrar!"
    show kevin 5 at right
    show player 14 at left
    player_name "Tudo bem! Eu vou passar lá em breve!"
    return

label cafeteria_erik_favor_known_not_yet:
    show kevin 1 at right
    show player 26 at left
    player_name "Ainda não, mas continuarei procurando!"
    show kevin 3 at right
    show player 1 at left
    kev "Tudo certo..."
    return

label cafeteria_erik_favor_known:
    call expression game.dialog_select("cafeteria_erik_favor_known_intro")
    menu:
        "Acho que sim!" if erik.known(erik_favor_2):
            call expression game.dialog_select("cafeteria_erik_favor_known_found_replacement")
            $ erik_favor_2.finish()
            $ M_kevin.set_default_locations([[L_gym, L_school_cafeteria, L_gym, L_NULL],
                                            [L_gym, L_gym, L_gym, L_NULL]])
            $ M_kevin.outfit.set_default_outfit_schedule([["gym", "apron", "apron", "apron"]])
        "Ainda não.":

            call expression game.dialog_select("cafeteria_erik_favor_known_not_yet")
    hide player
    hide kevin
    with dissolve
    return

label cafeteria_erik_favor_2_completed:
    scene cafeteria_b
    show player 36 at left with dissolve
    show erik 11 at right with dissolve
    player_name "Ei, {b}Erik{/b}!"
    show erik 12 at right
    show player 1 at left
    eri "Ei, {b}[firstname]{/b}!"
    show erik 11 at right
    show player 21 at left
    player_name "Então ... Como estão as tarefas da cafeteria?"
    show erik 12 at right
    show player 13 at left
    eri "Poderia ser pior, eu acho."
    eri "Eu costumo não fazer nada durante o almoço na escola, de qualquer maneira..."
    show erik 11 at right
    show player 17 at left
    player_name "Estou feliz que você esteja bem com isso."
    show erik 12 at right
    show player 1 at left
    eri "Eu vou pra casa brincar com {b}Sea Dogs SAGA{/b}!"
    show erik 11 at right
    show player 14 at left
    player_name "Legal! Bem, eu vou deixar você voltar aos seus deveres..."
    show erik 11 at right
    show player 1 at left
    eri "Te vejo mais tarde!"
    hide erik
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
