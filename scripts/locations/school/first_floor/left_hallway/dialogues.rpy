label left_hallway_judith_changing:
    scene lefthall_c
    show player 2 at left with dissolve
    show judith 6 at right with dissolve
    player_name "Ei, {b}Judith{/b}..."
    show player 11 at left
    player_name "..."
    show player 10 at left
    player_name "Está tudo bem?"
    show player 5 at left
    show judith 3 at right
    jud "Oh, Ei, {b}[firstname]{/b}..."
    jud "Eu não estou me sentindo muito bem; Eu poderia ir para casa."
    show player 10 at left
    show judith 1 at right
    player_name "Você não está indo para a aula de atletismo?"
    show player 5 at left
    show judith 2 at right
    jud "Bem..."
    jud "...eu só..."
    show judith 3 at right
    jud "... Eu não posso entrar no {b}vestiário dos meninos{/b}."
    show player 10 at left
    show judith 1 at right
    player_name "... O {b}vestiáriodos meninos{/b}?"
    player_name "Por que você precisa ir no {b}vestiário dos meninos{/b}?"
    show player 5 at left
    show judith 3 at right
    jud "Quer dizer que ninguém te contou?"
    show judith 1 at right
    show player 10 at left
    player_name "... Não?"
    show player 5 at left
    show judith 3 at right
    jud "Um cano estourou no {b}vestiário das meninas{/b} e está fechado para reparos..."
    show judith 2 at right
    jud "Estamos compartilhando o {b}vestiário dos meninos{/b} agora."
    show judith 1 at right
    show player 10 at left
    player_name "Sério?!"
    show player 5 at left
    show judith 3 at right
    jud "Eu realmente não me sinto confortável com isso, como as outras garotas."
    show judith 6 at right
    show player 35 at left
    player_name "Bem..."
    show player 10 at left
    show judith 1 at right
    player_name "A aula está começando em breve, então provavelmente não há muitas pessoas lá de qualquer maneira?"
    show player 1 at left
    show judith 5 at right
    jud "Sim, eu acho que você está certo..."
    show player 2 at left
    show judith 4 at right
    player_name "Eu posso ir com você, para ter certeza de que você está bem..."
    show player 33 at left
    player_name "...E eu não vou olhar!"
    show player 13 at left
    show judith 5 at right
    jud "Ok ... eu vou te seguir, então."
    hide player 13 at left with dissolve
    hide judith 5 at left with dissolve
    return

label left_hallway_latinos_bashing:
    scene lefthall_c
    show judith 10 at left
    show martinez at Position (xpos=350)
    show lopez f_normal_talk
    with dissolve
    lopez "Basta olhar para esses seios flácidos desagradáveis!"
    show lopez f_normal_talk
    show judith 7 at left
    jud "..."
    show judith 8 at left
    show martinez f_normal_talk
    martinez "Ela provavelmente é muito pobre para comprar um sutiã..."
    show martinez f_normal
    show judith 7 at left
    jud "Não é verdade!!"
    show judith 10 at left
    show lopez f_normal_talk
    lopez "Você acha que vai chamar a atenção dos garotos mostrando seus peitos assim?"
    show lopez f_normal
    show judith 7 at left
    jud "Meus seios são sensíveis !! Dói quando eu uso sutiã..."
    jud "Estou mais confortável assim!!"
    show judith 10 at left
    show lopez f_laugh
    lopez "Haha!"
    show lopez f_normal
    show judith 9 at left
    show martinez f_angry_talk
    martinez "É melhor você não ficar por aqui mais..."
    show martinez a_dressed_sign with dissolve
    martinez "PUTA! Você acabou de ouvir? Este é o nosso território, então saia!"
    show martinez f_angry a_dressed_crossed with dissolve
    show player 12 at Position( xpos = 290, ypos = 768)
    hide judith 9
    show judith 9 at left
    with dissolve
    player_name "Oque esta acontecendo aqui?!"
    show player 114
    jud "{b}*Soluçando*{/b}"
    show player 90 at Position( xpos = 290, ypos = 768)
    show judith 9 at left
    show lopez f_angry
    show martinez f_angry_talk
    martinez "Você está defendendo essa cadela feia agora??"
    show martinez f_angry
    show lopez f_angry_talk
    lopez "Continue andando menino branco!"
    show lopez f_angry
    show player 113
    player_name "Você está bem {b}Judith{/b}?"
    hide judith
    show player 90 at left
    with dissolve
    show martinez f_angry_talk
    martinez "Qual é o problema, garoto branco, você não vai correr atrás da sua cadela?"
    show martinez f_angry
    show player 12 at left
    player_name "Você não precisa fazer isso..."
    show martinez f_angry_talk a_dressed_sign with dissolve
    martinez "Nós vamos fazer o que quisermos!"
    show martinez f_angry a_dressed_crossed with dissolve
    show lopez f_laugh
    lopez "Haha! Até mais!"
    hide player
    hide lopez
    hide martinez
    with dissolve
    return

label left_hallway_judith_missing:
    scene expression game.timer.image("lefthall{}")
    show player 11 with dissolve
    player_name "..."
    show player 10
    player_name "...Onde está a {b}Judith{/b}?"
    player_name "( Ela geralmente fica neste corredor. )"
    show player 34
    player_name "Hmm..."
    show player 35
    player_name "( eu posso {b}ouvir{/b} alguma coisa... )"
    show player 10
    player_name "( Isso é alguém...? )"
    show player 12
    player_name "( É como uma voz de choro vindo do {b}vestiário das meninas{/b}... )"
    hide player 12 with dissolve
    return

label left_hallway_martinez_book_search:
    scene lefthall_c
    show martinez a_dressed_backpack at Position (xpos=350)
    show lopez f_angry
    show player 10 at left
    with dissolve
    player_name "Oi, {b}Martinez{/b}?"
    show player 5
    show martinez f_normal_talk
    martinez "...O que você quer, Culo?"
    show martinez f_normal
    show lopez f_angry_talk
    lopez "sim! O que você quer?"
    show lopez f_angry
    show player 10
    player_name "Uhh, Eu ouvi dizer que você tinha um livro atrasado da biblioteca."
    show player 5
    show martinez f_angry_talk
    martinez "O que, você está me perseguindo ou algo assim, garoto branco?"
    show martinez f_angry
    show player 10
    player_name "Hã? Não, o bibliotecário me enviou!"
    show player 5
    show lopez f_angry_talk
    lopez "Então, você é apenas a pequena vadia dos bibliotecários?"
    show lopez f_angry
    show martinez f_laugh
    martinez "Haha!"
    show martinez f_normal
    show player 12
    player_name "O que? Não, ela pediu um livro para mim e perguntou se eu poderia falar com vocês em troca."
    show player 5
    show martinez f_angry_talk
    martinez "Seja como for, Nós não temos tempo para isso..."
    show martinez f_normal_talk
    martinez "Vamos {b}Lopez{/b}. Temos que nos preparar para a aula de ginástica."
    show martinez f_normal
    show lopez f_angry_talk
    lopez "Coisa certa, {b}Martinez{/b}. até Mais tarde, Culo!"
    show lopez f_laugh
    lopez "Hahaha!"
    hide lopez
    show martinez b_back f_empty a_empty
    with dissolve
    show player 428
    pause
    show martinez at Position (xpos=500) with dissolve
    show player 11
    player_name "!!!"
    hide martinez with dissolve
    show player 12
    player_name "Eu aposto que é isso na mochila dela!"
    show player 30
    player_name "Eu deveria tentar {b}pegá-lo enquanto elas estão tomando banho{/b}. Elas provavelmente nem vão perceber."
    show player 33
    player_name "Eu só tenho que ser sorrateiro..."
    hide player with dissolve
    return

label left_hallway_cult_discovery:
    scene cult_event 5
    with dissolve
    window hide
    $ renpy.pause()
    scene cult_event 6
    with Dissolve(0.3)
    $ renpy.pause()
    scene expression "backgrounds/location_school_lefthall_night.jpg"
    with Dissolve(0.3)
    scene expression game.timer.image("lefthall{}")
    show player 11 at left with dissolve
    show erik 1 at right with dissolve
    player_name "..."
    show player 12
    player_name "Elas foram no armário de utilidades?"
    show player 90
    show erik 5
    eri "Por que elas iriam lá?"
    show player 35
    show erik 1
    player_name "A melhor pergunta é: como elas poderiam se encaixar lá??"
    player_name "Deve levar para outro lugar..."
    show player 34
    show erik 5
    eri "Podemos sair agora?"
    show player 12
    show erik 1
    player_name "Vamos nos ater ao nosso plano original e olhar em volta."
    show player 1
    show erik 3
    eri "Ok..."
    hide player 1 with dissolve
    hide erik 3 with dissolve
    return

label left_hallway_school_sneak_mission:
    scene cult_event 5
    with dissolve
    window hide
    pause
    scene cult_event 6
    with Dissolve(0.3)
    pause
    scene expression game.timer.image("lefthall{}")
    show player 11 at left with dissolve
    show erik 51 at right with dissolve
    player_name "..."
    show player 12
    player_name "Elas entraram no armário de utilidades?"
    show player 90
    show erik 53
    eri "Por que elas iriam lá?"
    show erik 52
    show player 35
    player_name "Não faz sentido."
    player_name "Elas não podiam se encaixar lá!"
    show player 34
    show erik 53
    eri "Você acha que talvez haja um túnel secreto ou algo assim?"
    show erik 52
    show player 10
    player_name "Hmm, Não sei. Talvez?"
    show player 5
    show erik 53
    eri "Isso está realmente me assustando."
    eri "Podemos sair agora?"
    show erik 52
    show player 12
    player_name "Aguente. Nós ainda temos uma missão para completar."
    show player 5
    show erik 50
    eri "..."
    show player 12
    player_name "Vamos lá, vamos para o escritorio da {b}Diretora Smith{/b} no {b}terceiro andar{/b}."
    hide player
    hide erik
    with dissolve
    return

label door14_locked_dialogue:
    scene expression game.timer.image("lefthall{}")
    show player 35 at left
    player_name "( O armário da utilidade está trancado. )"
    $ game.main()

label left_hallway_roxxy_lockerroom_event:
    scene expression game.timer.image("lefthall{}")
    show player 34 with dissolve
    player_name "Hmm?"
    player_name "( Há vozes vindo do {b}vestiário das garotas{/b}! )"
    player_name "( É suposto estar fora dos limites... )"
    show player 4 at Position (xoffset=6) with dissolve
    player_name "( ... Eu me pergunto o que está acontecendo? )"
    hide player with dissolve
    return

label left_hallway_roxxy_shower_event:
    scene expression game.timer.image("lefthall{}")
    show erik 62 at right
    show jersey 10 at left
    with dissolve
    player_name "{b}Erik{/b}?"
    show erik 61
    player_name "Onde estão todas as suas roupas?"
    show jersey 5
    show erik 63
    eri "oi, {b}[firstname]{/b}..."
    eri "Eu estava apenas no {b}vestiário dos meninos{/b} se trocando, quando {b}Roxxy{/b} e suas amigas vieram..."
    show erik 62
    eri "... Elas me expulsaram."
    show erik 61
    show jersey 10
    player_name "Então suas roupas ainda estão lá?"
    show jersey 5
    show erik 62
    eri "... Sim."
    show erik 61
    show jersey 12
    player_name "Vamos cara, eu vou com você."
    player_name "Nós vamos pegar suas roupas e então eu preciso ir no chuveiro."
    show jersey 5
    show erik 62
    eri "Ok..."
    hide player
    hide erik
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
