label hallway_jenny_hallway_talk:
    scene expression player.location.background_blur with None
    show player
    show jenny f_normal_talk b_towelhead
    with dissolve
    jen "Ei, {b}[firstname]{/b}!"
    show jenny f_normal
    show player f_worried_talk
    with dissolve
    player_name "Oi {b}[jen_name]{/b}..."
    player_name "Você acabou de sair do banho?"
    show player f_worried
    show jenny f_gross_talk
    jen "Duh, o que deu isso?"
    show jenny f_normal
    show player f_skeptical
    player_name "..."
    show jenny f_laugh
    jen "Hahahaah!"
    show player f_skeptical_talk
    player_name "Muito engraçado."
    show player f_skeptical
    show jenny f_grin
    pause
    show player f_normal_talk
    player_name "Então, o que você está fazendo hoje?"
    show player f_normal
    show jenny f_eyeroll
    jen "Uhh, estamos fazendo um camshow, lembra?"
    show jenny f_normal
    show player f_normal_talk
    player_name "Sim eu sei disso..."
    player_name "Eu estava apenas pensando que talvez depois nós pudéssemos sair?"
    show player f_normal
    show jenny f_gross_talk
    jen "Sair para curtir?"
    show jenny f_gross
    show player f_normal_talk
    player_name "Sim ou talvez sair e fazer alguma coisa juntos?"
    show player f_normal
    show jenny f_gross_talk
    jen "Por que faríamos isso?"
    show jenny f_gross
    show player f_laugh
    player_name "Porque isso seria divertido!"
    show player f_normal
    jen "..."
    show player f_normal_talk
    player_name "Nós nos divertimos no cinema outro dia, não foi?"
    show player f_normal
    show jenny f_gross_talk
    jen "Uhh, eu acho..."
    show jenny f_gross
    pause
    show jenny f_upset_talk
    jen "{b}*Suspiro*{/b} Precisamos falar de namoro de novo?"
    show jenny f_upset
    show player f_tired
    player_name "..."
    show player f_tired_talk
    player_name "eu apenas pensei!"
    show player f_surprised
    show jenny f_upset_talk
    jen "Você pensou o que, que eu realmente não quis dizer isso nas duas primeiras vezes que eu te disse que não estou interessada?"
    show jenny f_upset
    show player f_worried_talk
    player_name "Mas"
    show player f_worried
    show jenny f_angry_talk
    jen "Eu não quero falar sobre isso {b}[firstname]{/b}!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Por que não?!"
    show player f_worried
    show jenny f_eyeroll
    jen "Porque nossa vida e namoro seria super estranho!!!"
    show jenny f_upset
    show player f_thinking a_dressed_rub with dissolve
    player_name "..."
    show jenny f_gross_talk
    jen "Seria como namorar meu irmão ou algo assim..."
    show jenny f_grin
    show player f_laugh a_dressed_pocket with dissolve
    pause 1
    show player f_worried_talk
    player_name "Isso não é "
    show player f_unimpressed_talk
    player_name "O que?!"
    show player f_unimpressed
    show jenny f_upset_talk
    jen "Estou falando sério, {b}[firstname]{/b}!"
    jen "Nós temos uma coisa boa aqui..."
    jen "Por que você está tentando estragar tudo?"
    show jenny f_upset
    show player f_unimpressed_talk
    player_name "Tudo bem, tanto faz."
    player_name "Esqueça isso então."
    show player f_unimpressed
    show jenny f_upset_talk
    jen "Com prazer!"
    show jenny f_grin_talk
    jen "Agora, não se esqueça do nosso show esta tarde!"
    show jenny f_grin
    show player f_unimpressed_talk
    player_name "Sim Sim..."
    hide player with dissolve
    show jenny f_grin_talk
    jen "... E certifique-se de comer alguma coisa!"
    jen "Meus fãs estão esperando um bom desempenho!"
    show jenny f_grin
    pause
    show jenny f_eyeroll
    jen " Você e uma Dor na minha bunda..."
    scene black with fade
    $ player.go_to(L_home_entrance)
    scene expression player.location.background_blur with None
    show player f_tired with dissolve
    player_name "( Bem, isso poderia ter sido melhor... )"
    player_name "( Ela está realmente sendo teimosa sobre isso! )"
    show player f_thinking a_dressed_thinking with dissolve
    player_name "( {b}Tem que haver um jeito de convencê-la!{/b} )"
    player_name "( Hmm, Talvez {b}Eu deveria checar o diário dela de novo?{/b} )"
    player_name "( Tem sido muito útil até agora... )"
    hide player with dissolve
    return

label hallway_jenny_acknowleges_debbie_sex:
    scene expression player.location.background_closeup with None
    show player
    show debbie f_normal_talk
    deb "Bom dia {b}[firstname]{/b}."
    show debbie f_normal
    show player f_normal_talk
    player_name "Bom dia, {b}[deb_name]{/b}."
    show player f_normal
    show debbie f_sexy_talk
    deb "Eu estava me preparando para tomar banho..."
    show debbie f_sexy
    show player f_normal_talk
    player_name "Oh?"
    show player f_normal
    show debbie f_sexy_talk
    deb "É {b}[jen_name]{/b} ainda dormindo?"
    show debbie f_sexy
    show player f_normal_talk
    player_name "Sim, acho que sim."
    show player f_normal
    show debbie f_sexy_talk
    deb "Você quer se juntar a mim?"
    show debbie f_sexy
    show player f_shy_talk
    player_name "Mesmo?"
    show player f_shy
    show debbie f_laugh
    deb "Mmhmm!"
    show debbie f_normal_talk
    deb "Apenas espere alguns minutos antes de entrar, ok?"
    show debbie f_sexy
    show player f_shy_talk
    player_name "Sim, ok."
    show player f_shy
    show debbie f_laugh
    deb "Hehe, e não me deixe esperando por muito tempo!"
    show debbie f_sexy
    show player f_laugh
    player_name "Eu não vou."
    show player f_normal
    hide debbie with dissolve
    pause
    show player f_grin
    player_name "( Impressionante! )"
    jen "Então vocês dois {i}está{/i} porra, hein?!"
    show player f_surprised
    player_name "!!!" with hpunch
    show jenny f_grin with dissolve
    show player f_worried_talk
    player_name "O quê"
    player_name "Eu não sei do que você está falando..."
    show player f_worried
    show jenny f_eyeroll
    jen "Oh, por favor!"
    show jenny f_upset_talk
    jen "É tão óbvio!"
    show jenny f_upset
    player_name "..."
    show jenny f_upset_talk
    jen "Olha, eu realmente não dou a minìma."
    show jenny f_upset
    show player f_worried_talk
    player_name "Você não?"
    show player f_worried
    show jenny f_laugh
    jen "Psh, de jeito nenhum!"
    show jenny f_upset_talk a_dressed_crossed with dissolve
    jen "Foda quem você quiser, só não deixe interferir com o nosso camshows!"
    show jenny f_upset
    show player f_skeptical
    player_name "..."
    show jenny f_upset_talk
    jen "Estou falando sério!"
    show jenny f_angry_talk
    jen "Se você estragar eu vou te cortar!"
    show jenny f_angry
    show player f_shock
    player_name "!!!"
    show jenny f_upset
    pause
    show player f_worried_talk
    player_name "Você não acha estranho que eu e {b}[deb_name]{/b} são ... Você sabe?"
    show player f_worried
    show jenny f_laugh
    jen "Haha, claro que é estranho!"
    show jenny f_grin_talk a_dressed_hips with dissolve
    jen "Não é realmente minha preocupação, é?!"
    show jenny f_grin
    show player f_worried_talk
    player_name "eu acho que não..."
    show player f_worried
    show jenny f_upset_talk
    jen "Apenas tenha certeza que você está pronto para o show esta tarde, entendeu?"
    show jenny f_upset
    show player f_worried_talk
    player_name "É, eu entendi."
    show player f_worried
    show jenny f_upset_talk
    jen "Boom."
    show jenny f_grin_talk
    jen "Até mais tarde, perdedor!"
    hide jenny with dissolve
    player_name "..."
    show player f_thinking a_dressed_thinking with dissolve
    player_name "( Hmm, {b}[deb_name]{/b} está me esperando... )"
    show player f_worried a_dressed_pocket with dissolve
    player_name "( ... Talvez esta não seja uma boa ideia. )"
    hide player with dissolve
    return

label hallway_jenny_caught_talking_to_camslut:
    if store._in_replay is not None:
        $ player.location = L_home_hallway
        $ game.timer.tick(3)
    scene expression player.location.background_closeup with None
    show player 5 at left
    jen "Tà maluco?!"
    pause
    show player 4 with dissolve
    player_name "( Hmm? )"
    show player 5 with dissolve
    jen "De jeito nenhum, haha!"
    show player 90
    player_name "( Ela está sendo muito barulhenta... )"
    pause
    show player 5
    player_name "( Eu me pergunto com quem ela está falando? )"
    jen "O plug anal é suficiente para você, confie em mim!"
    show player 11
    pause
    jen "Hahaha, porra sam9!"
    player_name "( É ela estar na... Streaming Agora? )"
    player_name "( Eu deveria dar uma olhada rápida... )"
    scene expression "backgrounds/location_home_jennybedroom_cutscene03.jpg" with dissolve
    jen "Então, qual brinquedo vocês querem ver hoje à noite?"
    jen "{b}Monstro Ruim{/b}?"
    pause
    jen "Sim, eu sei que vocês querem me ver montando um pau de verdade ... Estou trabalhando nisso, ok?!"
    pause
    jen "Hmm?"
    pause
    jen "O que você quer dizer?"
    pause
    jen "Tem alguém no fundo?"
    scene expression "backgrounds/location_home_jennybedroom_cutscene04.jpg"
    jen "!!!" with hpunch
    jen "{b}[firstname]{/b}?!"
    pause
    $ player.go_to(L_home_sisbedroom)
    scene expression player.location.background_closeup with None
    show player 22f at right
    show jenny f_angry_talk b_naked a_naked_hips at flip
    with dissolve
    jen "VOCÊ PORRA PERVERTIDO!!"
    show jenny f_angry
    show player 10f
    player_name "Você tem algo em sua bunda agora?!"
    show player 91f
    show jenny f_angry_talk
    jen "SAIA DAQUI!!!"
    show jenny f_angry
    show player 17f
    player_name "Você é uma camgirl?!"
    show jenny f_angry_talk
    jen "RRRAAAAAHHH!!!"
    show jenny a_naked_monster_hit at Position (xpos=200)
    show player 6f
    with dissolve
    player_name "Aiiii!"
    jen "Saia!!!"
    player_name "Ok, ok!"
    jen "FORA!!!"
    player_name "Eu sinto Muito!"
    player_name "Apenas pare de me bater!"
    hide player with dissolve
    show jenny a_naked_hips with dissolve
    jen "Inacreditável!"
    show jenny f_angry
    scene black with dissolve
    pause
    scene expression "backgrounds/location_home_jennybedroom_desk_evening.jpg"
    show jenny b_naked_back_plug f_empty a_naked_back_sides with dissolve
    jen "{b}*Suspiro*{/b} Desculpem rapazes..."
    pause
    jen "Não, esse é"
    jen "... Ele é apenas um cara com quem eu moro."
    pause
    show jenny a_naked_back_hips with dissolve
    jen "Não, eu não vou transar com ele."
    pause
    jen "Ugh, Não!"
    pause
    jen "... Sério?"
    pause
    jen "Eu não acredito em você!"
    "PING"
    show jenny a_naked_back_sides with dissolve
    pause
    show jenny a_empty b_naked_back_bending_plug with dissolve
    jen "Puta merda..."
    pause
    jen "Três vezes isso?!"
    pause
    jen "Olha, pessoal ... eu realmente não posso."
    jen "Apenas esqueça, ok?"
    jen "Eu vou encontrar alguém ... eu prometo."
    jen "Ele não."
    pause
    jen "Eu sei."
    jen "Vamos apenas fazer com os brinquedos esta noite."
    pause
    jen "Não, não vá embora!"
    pause
    jen "..."
    show jenny b_naked_back_plug a_naked_back_hips with dissolve
    jen "Porra!"
    scene black with dissolve
    pause
    $ player.go_to(L_home_bedroom)
    scene expression player.location.background_closeup with None
    show player 37 with dissolve
    player_name "( Merda, ela realmente acabou de me bater com um vibrador gigante? )"
    player_name "( Pelo menos não foi o secador de cabelo ... Aquele secador de cabelo e um pesadelo! )"
    pause
    show player 25 with dissolve
    player_name "( Cara, estou exausto. )"
    player_name "( Espero que ela ainda não esteja brava com isso amanhã. )"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["06_unlocked"] = True
    return

label hallway_jenny_confront_her_hallway:
    scene expression player.location.background_closeup with None
    show jenny a_dressed_side at flip
    show player 12f at right
    player_name "Sua mentirosa!"
    show player 90f
    show jenny f_upset_talk a_dressed_hips with dissolve
    jen "Desculpe?!"
    show jenny f_upset
    show player 12f
    player_name "Eu sei que você não está online."
    show player 90f
    show jenny f_upset_talk
    jen "Ok, certo. Você não sabe de nada..."
    show jenny f_upset
    show player 12f
    player_name "Bem, eu sei que você está mentindo para {b}[deb_name]{/b}!"
    show player 90f
    show jenny f_upset_talk
    jen "Por que você não se importa com seu próprio negócio, perdedor?!"
    show jenny f_upset
    player_name "..."
    show player 12f
    player_name "Eu só espero que você não esteja fazendo algo que você vai se arrepender por esse dinheiro."
    show player 90f
    show jenny f_eyeroll
    jen "Ugh, tanto faz."
    show player 22b at left
    show jenny f_upset_talk a_dressed_wave_off at Position (xpos=500)
    with dissolve
    jen "Saia do meu caminho, estou indo tomar banho!"
    show player 90
    hide jenny with dissolve
    pause
    player_name "( Hmm, ela está escondendo algo com certeza e eu vou descobrir o que! )"
    hide player with dissolve
    return

label hallway_jenny_hallway_eavesdropping:
    if store._in_replay is not None:
        $ player.location = L_home_hallway
        $ game.timer.tick(3)
    scene expression player.location.background_closeup with None
    show player 5
    player_name "..."
    show player 10
    player_name "O que é essa luz saindo do quarto da {b}[jen_name]{/b}?"
    show player 5
    pause
    show player 12
    player_name "Ela deve estar em seu computador ou algo assim..."
    show player 5
    mans_voice "Você gosta disso, não sua pequena puta?!"
    show player 11
    jen "Mmm, sim!"
    mans_voice "Eu não te disse para me excitar {b}Papai{/b}?!"
    jen "Eu sinto Muito, {b}Papai{/b}!"
    show player 10
    player_name "O que"
    show player 11
    mans_voice "Você acha que esse grande pau vai se encaixar no seu rabo apertado?!"
    jen "Ahh, Não sei {b}Papai{/b}..."
    show player 10
    player_name "com quem ela està falando?!"
    show player 11
    mans_voice "Bem, você está prestes a descobrir ... Fique de joelhos, vadia."
    jen "Ngghhh, Sim {b}Papai{/b}!"
    show player 12
    player_name "Ok, eu tenho que espiar agora!"
    scene expression "backgrounds/location_home_jennybedroom_cutscene01.jpg" with dissolve
    pause
    player_name "Ufa, não tem Nimguêm aqui..."
    player_name "Ela só está vendo pornografia."
    pause
    player_name "!!!" with hpunch
    player_name "Eu não sabia que {b}[jen_name]{/b} assisti pornô!"
    jen "Ngghh!! Me dê isto {b}Papai{/b}!"
    jen "Por favor!!!"
    player_name "{b}*Espantado*{/b} Nossa, ela está esquisita"
    scene expression "backgrounds/location_home_jennybedroom_cutscene02.jpg" with dissolve
    player_name "!!!" with hpunch
    jen "OH MEU DEUS!"
    jen "VOCÊ ESTÁ ME ESPIONANDO NOVAMENTE?!"
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["01_unlocked"] = True
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 22 at left
    show jenny f_angry_talk a_dressed_upset at Position (xpos=350)
    with dissolve
    jen "O que eu disse para você!"
    show jenny f_angry
    show player 23
    player_name "Eu sinto Muito!"
    show player 22
    show jenny f_angry_talk
    jen "Sobre ficar me espionando!"
    show jenny f_angry a_dressed_hit with dissolve
    show jenny a_dressed_hit2
    show player 6
    with dissolve
    player_name "Ai!!"
    show jenny f_angry_talk a_dressed_hit with dissolve
    jen "Seu fracassado perdedor!"
    show jenny f_angry a_dressed_hit2 with dissolve
    pause
    show jenny a_dressed_hit with dissolve
    show player 38 with dissolve
    player_name "Para com isso doí!"
    hide jenny
    show jenny a_dressed_upset f_angry
    with dissolve
    show player 34 with dissolve
    jen "..."
    show player 12
    player_name "Ahhh, De onde sai esses secadores de cabelo que diabos?!"
    show player 5
    show jenny f_angry_talk
    jen "vou falar para {b}[deb_name]{/b}!"
    show jenny f_angry at flip
    show jenny at Position (xpos=1050)
    with dissolve
    show player 10
    player_name "O que?!"
    player_name "Não, não, por favor!!"
    show jenny a_dressed_crossed at unflip
    show jenny at Position (xpos=550)
    with dissolve
    player_name "Não diga {b}[deb_name]{/b}!"
    show player 11
    show jenny f_grin a_dressed_hips with dissolve
    pause
    show jenny f_grin_talk
    jen "Cem dólares."
    show jenny f_grin
    show player 23
    player_name "O que!"
    show player 22
    show jenny f_grin_talk
    jen "Dá-me cem dólares ou eu vou falar para {b}[deb_name]{/b}, agora!"
    show jenny f_grin
    show player 10
    player_name "Sèrio?!"
    show player 11
    pause
    show player 12
    player_name "Você so pode estar maluca, Se acha que eu vou da cem dólares!"
    show player 11
    show jenny f_grin_talk at flip
    show jenny at Position (xpos=1050)
    with dissolve
    jen "{b}[deb_name]{/b}!"
    show jenny f_grin
    show player 37 with dissolve
    player_name "Ok, ok, pare!"
    show player 24 with dissolve
    show jenny at unflip
    show jenny at Position (xpos=550)
    with dissolve
    if player.has_money(100):
        show player 638 with dissolve
        player_name "Jesus Cristo..."
        player_name "{b}*Suspirou*{/b} Aqui."
        show player 5
        show jenny f_grin_down a_dressed_money_counting
        with dissolve
    else:
        if not player.has_money(1):
            show player 10
        else:
            show player 638 with dissolve
        player_name "Eu não tenho cem Dólares."
        if not player.has_money(1):
            show player 5
        else:
            show player 638b
        show jenny f_grin_talk
        jen "Então me dê o que você tem!"
        show jenny f_grin
        if not player.has_money(1):
            show player 529 with dissolve
            player_name "{b}*Suspiro*{/b} Isto funciona?"
            show player 528
            show jenny f_upset_talk
            jen "Que nojo!"
            jen "Você é patético..."
            show jenny f_upset
        else:
            show player 638
            player_name "{b}*Suspiro*{/b} Aqui."
            show player 5
            show jenny f_grin_down a_dressed_money_counting
            with dissolve
    pause
    show player 10 with dissolve
    player_name "Então você não vai contar para {b}[deb_name]{/b} ?"
    show player 5
    if not player.has_money(1):
        show jenny f_eyeroll
    else:
        show jenny f_grin_talk
    jen "Não dessa vez."
    if not player.has_money(1):
        show jenny f_angry_talk
        jen "O dinheiro, perv."
    else:
        jen "Prazer fazer negócios com você, pervertido."
    hide jenny with dissolve
    pause
    show player 37 with dissolve
    player_name "( Ufa, isso foi perto! )"
    pause
    show player 38 with dissolve
    if player.has_money(1):
        player_name "( ...caralho! )"
    player_name "( Eu tenho que ser mais cuidadoso. )"
    hide player with dissolve
    return

label hallway_jenny_in_shower:
    scene expression player.location.background_closeup with None
    show player 11 with dissolve
    player_name "( Hmm? )"
    show player 5
    player_name "( Parece que alguém deixou a porta do banheiro aberta... )"
    player_name "( Eu me pergunto quem está lá? )"
    show player 403
    pause
    player_name "( Uma pequena espiada não faria mal, certo? )"
    hide player with dissolve
    return

label hallway_jenny_start:
    scene expression player.location.background_closeup with None
    show player 10 at left
    show jenny
    with dissolve
    player_name "Oh, uhh..."
    show player 36 with dissolve
    show jenny f_gross
    player_name "Oi"
    show player 11 with fastdissolve
    show jenny f_upset_talk
    jen "Salve, perdedor!"
    show jenny f_upset
    player_name "..."
    show player 12
    player_name "Nossa, qual é o seu problema?!"
    show player 5
    show jenny f_upset_talk
    jen " O que você acha,  Do meu problema?!"
    jen "... Preso aqui, morando com você."
    show jenny f_upset
    show player 24
    player_name "{b}*Suspiro*{/b} Sim, seja qual for..."
    show player 5
    show jenny f_normal_talk
    jen "Você não deveria estar na escola ou algo assim?"
    show jenny f_normal
    show player 12
    player_name "Você não deveria estar à procura de um novo emprego?!"
    show player 90
    show jenny f_surprised a_dressed_upset with dissolve
    jen "!!!"
    show jenny f_upset_talk a_dressed_crossed with dissolve
    jen "Ah, você não quer jogar esse jogo comigo, espertinho."
    show jenny f_upset
    show player 12
    player_name "Ei, você é quem começou!"
    show player 90
    player_name "..."
    show player 4 with dissolve
    player_name "{b}*Cheirar*{/b}"
    show jenny f_upset_talk
    jen "Por que você está fazendo essa cara?"
    show jenny f_upset
    player_name "{b}*Cheirar*{/b}"
    show player 26 with dissolve
    player_name "Algo cheira muito bem..."
    show player 403
    show jenny f_upset_talk
    jen "Ahh, É o café da manhã que está esperando por você {b}andar de baixo{/b}, Manequim."
    show jenny f_eyeroll
    jen "Eu não posso acreditar que ela ainda está fazendo o café da manhã todos os dias."
    show jenny f_upset_talk
    jen "Já faz mais de um mês desde {b}seu pai{/b} morreu."
    show jenny f_upset
    show player 24
    player_name "Sim, bem ... Talvez ela goste de fazer isso?"
    player_name "Ela é uma boa senhora."
    show jenny f_upset_talk
    jen "O Sim, Ela é muito legal se você me perguntar."
    show player 90
    hide jenny with dissolve
    pause
    player_name "( Eu me pergunto o que ela está fazendo? )"
    show player 13
    player_name "( Eu deveria descer e ver o que cheira tão delicioso! )"
    hide player with dissolve
    return

label hallway_mom_sis_boobs_afterthoughts:
    scene hallway
    show player 26 with dissolve
    player_name "Uau..."
    player_name "Eu não posso acreditar {b}[jen_name]{/b} realmente tirou a blusa na minha frente..."
    player_name "Seus seios são tão legais..."
    hide player with dissolve
    return

label hallway_sis_final_started:
    scene hallway
    show player 11 with dissolve
    player_name "..."
    player_name "( Há vozes vindo de {b}[jen_name]'s{/b} quarto... )"
    show player 4
    player_name "( Parece que ela está falando com alguém? Mas quem... )"
    show player 1
    player_name "( Talvez eu possa me esgueirar até a porta dela e descobrir... )"
    hide player with dissolve
    return

label hallway_mom_sleepover_offer:
    scene hallway_night
    show debbie 3 at right
    show player 1 at left
    with dissolve
    deb "Oi, querido."
    show player 17
    show debbie 1
    player_name "Oi, {b}[deb_name]{/b}."
    show debbie 2
    show player 1
    deb "Como você tem dormido?"
    show player 10
    show debbie 14
    player_name "Eu não durmo tão fácil quanto antes, você sabe, antes do meu {b}pai{/b} morrer."
    show player 5
    show debbie 13
    deb "Você está pensando em todas as coisas que estão acontecendo ultimamente?"
    show debbie 14b
    show player 10
    player_name "Sim, eu acho ... Um pouco."
    show player 5
    show debbie 13
    deb "Eu não quero que você se preocupe com isso, querido."
    deb "Tudo vai ficar bem, eu prometo."
    show debbie 14
    show player 10
    player_name "E quanto a você? Você está dormindo bem?"
    show player 5
    show debbie 13
    deb "Na verdade não."
    show debbie 14
    pause
    show debbie 13
    deb "... Mas eu estou acostumado com isso. Eu tive problemas para dormir desde que meu marido partiu muitos anos atrás."
    show player 11
    deb "Eu entendo o que você está passando."
    show debbie 14b
    show player 12
    player_name "Sèrio?"
    show player 5
    show debbie 13
    deb "Sim. Sinto falta do seu {b}pai{/b} também."
    show debbie 14
    pause
    show debbie 2
    deb "Nós éramos amigos há muito tempo, sabe?"
    show debbie 1
    show player 13
    pause
    hide player
    show debbie 4 at center
    with dissolve
    pause
    show player 13 at left
    show debbie 2 at right
    with dissolve
    deb "Pelo menos eu tenho você agora..."
    show debbie 1
    pause
    show debbie 2
    deb "Se você tiver algum problema para dormir novamente, apenas venha me visitar, certo?"
    show debbie 1
    show player 10
    player_name "No seu quarto?"
    show player 5
    show debbie 3
    deb "Certo!"
    show debbie 2
    deb "Talvez nos ajude a adormecer?"
    show debbie 1
    show player 10
    player_name "Você não se importa de eu dormir na sua cama?"
    show player 11
    pause
    show debbie 13
    deb "Eu acho que poderia nos fazer bem..."
    show player 13
    deb "... Depois de tudo que aconteceu."
    show debbie 14
    show player 14
    player_name "...Ok. Certo, {b}[deb_name]{/b}."
    hide player
    hide debbie
    with dissolve
    show unlock34 at truecenter with dissolve
    pause
    hide unlock34 with dissolve
    return

label hallway_mom_movie_night_two:
    scene hallway_night
    show player 1 at left
    show debbie 62 at right
    deb "Ei, querido!"
    show player 2
    show debbie 61
    player_name "Ei {b}[deb_name]{/b}, estás bem?"
    show player 1
    show debbie 62
    deb "Eu estava pensando em assistir outro filme."
    deb "Quer se juntar a mim?"
    show player 2
    show debbie 61
    player_name "Claro, eu adoraria!"
    show player 1
    show debbie 62
    deb "Maravilhoso, vou me sentar então! Venha e junte-se a mim na {b}sala de estar{/b} quando você estiver pronto."
    show player 2
    show debbie 61
    player_name "Parece bom! Eu estarei là."
    hide debbie
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
