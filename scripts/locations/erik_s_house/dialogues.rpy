label erikshouse_erik_intro_known:
    scene erikhouse
    show player 2 at left with dissolve
    show erik 1 at right with dissolve
    player_name "Olá, {b}Erik{/b}!"
    show erik 5 at right
    show player 1 at left
    eri "Olá, {b}[firstname]{/b} ..."
    show player 10 at left
    show erik 1 at right
    player_name "Você parece muito cansado ... Você está bem?"
    show erik 3 at right
    show player 5 at left
    eri "Bem, eu fiquei no computador a noite toda jogando esse novo jogo que saiu ..."
    show erik 2 at right
    show player 5 at left
    eri "... e eu odeio ir à escola."
    show erik 3 at right
    eri "Eu gostaria de poder ficar em casa o tempo todo."
    show player 10 at left
    show erik 1 at right
    player_name "Sim, eu ouvi você ..."
    show erik 3 at right
    show player 24 at left
    eri "Lamento o que aconteceu com o seu {b}Pai{/b}, a propósito. Como você está indo?"
    show player 25 at left
    show erik 1 at right
    player_name "Eu vou ficar bem, cara. Obrigado por perguntar!"
    player_name "Deveríamos realmente ir antes que nos atrasemos para a aula."
    hide player 25 at left with dissolve
    hide erik 1 at right with dissolve
    return

label erikshouse_erik_intro_started:
    scene erikhouse
    show player 11 at left
    show erik 5 at right
    eri "Não deveríamos ir à {b} escola {/b}?"
    show erik 1 at right
    show player 14 at left
    player_name "Oh sim. Você está certo..."
    hide player 14 at left
    hide erik 1 at right
    hide erikhouse
    return

label erikshouse_erik_intro_over:
    scene erikhouse
    show player 12 with dissolve
    player_name "( Não tem ninguém aqui ... )"
    show player 35
    player_name "( {b}Erik{/b} provavelmente já foi para a {b} escola {/b}. )"
    hide player 35 with dissolve
    hide erikhouse
    return

label erikshouse_erik_intro_over_weekend:
    scene erikhouse
    show player 12 with dissolve
    player_name "( Não tem ninguém aqui ... )"
    show player 35
    player_name "( {b}Erik{/b} provavelmente está jogando videogame ou comprando alguns no {b} shopping {/b}. )"
    hide player 35 with dissolve
    hide erikhouse
    return

label mrs_j_intro:
    scene erikhouse
    show player 1 at left with dissolve
    show mrsj 2 at right with dissolve
    mrsjo "Olá, {b}[firstname]{/b}!"
    show mrsj 1 at right
    show player 14 at left
    player_name "{b}Sr. Johnson{/b}! Apenas passando para ver o {b}Erik{/b}!"
    show mrsj 4 at right
    show player 1 at left
    eri "Olá, {b}[firstname]{/b}!"
    show mrsj 5 at right
    show player 11 at left
    mrsjo "Aqui está minha pequena abóbora!"
    show mrsj 6 at right
    eri "Vamos lá, {b}Sr. Johnson{/b}. Eu disse para você não me chamar assim ..."
    show mrsj 7 at right
    show player 5 at left
    mrsjo "A propósito, {b}Erik{/b} me contou sobre seu pai ..."
    mrsjo "Sinto muito ouvir isso. Deixe-nos saber se você precisar de alguma coisa, ok?"
    show mrsj 8 at right
    show player 10 at left
    player_name "Obrigado, {b}Sr. Johnson{/b}."
    show mrsj 7 at right
    show player 13 at left
    mrsjo "Ok, é melhor eu ir para a minha aula de Yoga. Vocês dois se comportem!"
    show mrsj 8 at right
    show player 1 at left
    mrsjo "Tente tirar {b} Erik {/b} de casa para variar!"
    mrsjo "Seria bom para ele pegar um sol!"
    mrsjo "Boa sorte!"
    show mrsj 6 at right
    eri "Ok, certo."
    hide mrsj 6 at right with dissolve
    show erik 1 at right with dissolve
    show player 14 at left
    player_name "Cara, ela está tão em forma! Você tem tanta sorte que ela está deixando você alugar um quarto!"
    show erik 3 at right
    show player 1 at left
    eri "Hum ... Sim ... eu acho ..."
    show erik 1 at right
    show player 26 at left
    player_name "Vamos lá, cara. Admita. Para a idade dela, ela está {i} REALMENTE {/i} em boa forma!" with hpunch
    show erik 5 at right
    show player 1 at left
    eri "Bem, ela fica muito tempo no {b} ginásio{/b}."
    eri "Eles a fizeram dar uma aula de ioga agora."
    show erik 1 at right
    show player 14 at left
    player_name "Então, você quer participar de um hangout ... ou?"
    show erik 3 at right
    show player 11 at left
    eri "Eu não posso agora. Eu ... baixei este novo jogo e-"
    show erik 1 at right
    show player 12 at left
    player_name "Está tudo bem, {b} Erik {/b}. Vejo você amanhã ou algo assim."
    show player 36 at left
    show erik 7 at right
    eri "Legal. Te vejo mais tarde..."
    hide player 36 at left with dissolve
    hide erik 7 at right with dissolve
    hide erikhouse
    return

label door18_locked_dialogue:
    if player.location == L_erikhouse:
        scene erikhouse
    elif player.location == L_erikhouse_backyard:
        scene eriks_backyard_b
    show player 11 at left
    show erik 5 at right
    eri "Umm ... Por que estamos indo na minha casa?"
    eri "Não deveríamos ir à {b} escola {/b}?"
    show erik 1 at right
    show player 14 at left
    player_name "Oh sim! Você está certo..."
    hide player 14 at left
    hide erik 1 at right
    $ game.main()

label erik_gf_stolen:
    if player.location == L_erikhouse:
        scene expression game.timer.image("erikhouse{}")
    elif player.location == L_erikhouse_backyard:
        scene expression game.timer.image("eriks_backyard{}_b")
    show player 10
    with dissolve
    player_name "Eu não deveria tornar isso mais estranho ..."
    player_name "Vou esperar até amanhã para falar com eles."
    hide player
    with dissolve
    $ game.main()

label erik_thief_block:
    scene erikhouse_night
    show player 2 with dissolve
    player_name "Eu deveria pegar aquele {b} ladrão {/b} primeiro."
    hide player 2 with dissolve
    $ game.main()

label closed_erik:
    if not game.timer.is_dark():
        if player.location == L_erikhouse:
            scene erikhouse
        elif player.location == L_erikhouse_backyard:
            scene eriks_backyard_b
        show player 12 with dissolve
        player_name "( Não há ninguém aqui ... )"
        show player 35
        player_name "O {b}Erik{/b} provavelmente está na {b}escola{/b} agora."
    else:

        if player.location == L_erikhouse:
            scene erikhouse_night
        elif player.location == L_erikhouse_backyard:
            scene eriks_backyard_night_b
        show player 2 with dissolve
        player_name "( {b}Erik{/b} provavelmente está dormindo. Eu deveria voltar amanhã. )"
        hide player 2 with dissolve
    $ game.main()

label closed_erik_weekend:
    if player.location == L_erikhouse:
        scene erikhouse
    elif player.location == L_erikhouse_backyard:
        scene eriks_backyard_b
    show player 12 with dissolve
    player_name "( Não há ninguém aqui. )"
    show player 35
    player_name "( O {b}Erik{/b} provavelmente saiu com {b} Sra. Johnson {/b} para algum lugar. )"
    hide player 35 with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
