label entrance_jenny_pregnancy_first_baby_coming_home:
    scene expression player.location.background_closeup
    $ player.last_baby_gender = M_jenny.pregnancy.baby_gender
    show jenny b_casual a_dressed_baby f_happy at flip
    show jenny at Position (xpos=150)
    show debbie
    show player f_normal_talk at Position (xpos=450) with dissolve
    player_name "Ei, você está em casa!"
    show player f_normal
    show jenny f_eyeroll
    jen "Sim, finalmente..."
    show jenny f_upset_talk
    jen "Eu odeio tanto hospitais!"
    show jenny f_upset
    show debbie f_normal_talk
    deb "Estou fazendo um grande bife de boas vindas para o jantar, querida."
    show debbie f_normal
    show jenny f_happy_talk
    jen "Isso parece incrível!"
    pause
    if M_jenny.pregnancy.baby_gender == "twins":
        jen "Você se importaria de cuidar dos meus filhos um pouquinho?"
    elif M_jenny.pregnancy.baby_gender == "boy":
        jen "Você se importaria de cuidar do meu filho um pouquinho?"
    else:
        jen "Você se importaria de cuidar da minha filha um pouquinho?"
    jen "Eu me mataria para um banho agora."
    show jenny f_happy
    show debbie f_normal_talk
    if M_jenny.pregnancy.baby_gender == "twins":
        deb "Claro, eu vou cuidar deles!"
        deb "Venha ver sua madrinha, pequeninos!"
        show debbie f_normal_talk_down a_robe_baby
        show jenny a_dressed_side
        with dissolve
        deb "Ah, eles são tão fofos!"
    elif M_jenny.pregnancy.baby_gender == "boy":
        deb "Claro, eu vou cuidar deles!"
        deb "Venha ver sua madrinha, carinha!"
        show debbie f_normal_talk_down a_robe_baby
        show jenny a_dressed_side
        with dissolve
        deb "Ah, uma torta tão fofa!"
    else:
        deb "Claro, eu vou cuidar dela!"
        deb "Venha ver sua madrinha, garotinha!"
        show debbie f_normal_talk_down a_robe_baby
        show jenny a_dressed_side
        with dissolve
        deb "Ah, uma torta tão fofa!"
    show debbie f_normal_down
    show jenny f_happy_talk
    jen "Obrigada, {b}[deb_name]{/b}."
    show jenny f_happy
    show player f_normal_talk
    player_name "Bem-vindo a casa, {b}[jen_name]{/b}!"
    show player f_normal
    show jenny f_happy_talk
    jen "Sim, obrigada {b}[firstname]{/b}."
    show jenny f_upset_talk
    jen "Fora do meu caminho, eu tenho um encontro com a banheira!"
    jen "E não me incomoda!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Eu não ia..."
    show player f_worried
    show jenny f_upset_talk
    jen "Hã."
    hide jenny with dissolve
    pause
    show player f_normal_talk
    player_name "A tirana retorna, né?"
    show player f_grin
    show debbie f_normal
    deb "Hmm?"
    show player f_tired_talk
    player_name "... deixa pra lá."
    hide player with dissolve
    return

label entrance_jenny_first_baby_stage_2_end:
    pause
    show jenny f_upset_talk
    jen "Então, agora o que?!"
    show jenny f_upset
    show debbie f_curious
    pause
    show player f_worried_talk
    player_name "{b}[deb_name]{/b}?"
    player_name "Você está bem?!"
    show player f_worried
    show debbie f_laugh
    deb "Estou feliz..."
    show debbie f_curious
    show jenny f_upset_talk
    jen "Feliz?!"
    show jenny f_upset
    show debbie f_normal_talk
    deb "Eu não posso acreditar que vou ser madrinha!"
    show debbie f_curious
    show jenny f_angry_pouting_top
    jen "..."
    show debbie f_normal_talk
    deb "Não é maravilhoso, {b}[firstname]{/b}?!"
    show debbie f_normal
    show player f_worried_talk
    player_name "Eh sim?"
    show player f_worried
    show debbie f_laugh
    deb "Hehe!"
    show jenny b_empty a_empty f_surprised zorder 2 at Position (xpos=376)
    show debbie b_robe_hug_jenny_bump a_empty f_normal_talk
    with dissolve
    deb "{b}*Sniff*{/b} Seu filho vai ser o garoto mais sortudo do mundo!"
    show debbie f_normal
    show jenny f_sad_talk
    jen "{b}[deb_name]{/b}..."
    show jenny at flip
    show jenny b_dressed_pregnant_bump f_sad a_dressed_side zorder 1 at Position (xpos=100)
    show debbie b_robe a_robe_mug f_normal_talk
    with dissolve
    deb "Você também tem que ajudar {b}[firstname]{/b}!"
    show debbie f_sad_talk
    deb "Ser mãe solteira é difícil, acredite em mim."
    deb "{b}[jen_name]'s{/b} Vai precisar de todo o apoio que puder."
    show debbie f_normal
    show player f_normal_talk
    player_name "Sim claro!"
    show player f_normal
    show debbie f_normal_talk
    deb "Por que vocês dois não entram na sala de jantar e se sentam?"
    show debbie f_laugh
    deb "Vou fazer um ótimo café da manhã para comemorar!"
    show debbie f_normal
    show player f_laugh
    player_name "Sim, ok."
    show player f_normal_talk
    player_name "Vamos lá, {b}[jen_name]{/b}!"
    hide player with dissolve
    show jenny f_sad_talk
    jen "Obrigada, {b}[deb_name]{/b}..."
    show jenny f_sad
    show debbie f_normal_talk
    deb "De nada querida."
    show debbie f_normal
    scene black with fade
    return

label entrance_jenny_first_baby_stage_2_no_diane:
    pause
    show debbie f_sad_talk
    deb "Apenas me diga, {b}[jen_name]{/b}."
    show debbie f_sad
    pause
    show jenny f_upset_talk
    jen "Eu acho que engravidei de um assento de toalete no shopping..."
    show jenny f_upset
    show debbie f_surprised_worried
    deb "{b}*Gasp*{/b}"
    show debbie f_sad
    show player f_surprised
    player_name "!!!"
    show player f_worried
    show debbie f_sad_talk
    deb "Isso não é"
    show debbie f_sad
    pause
    show debbie f_surprised_worried
    deb "Isso pode acontecer?"
    show debbie f_sad
    pause
    show jenny f_eyeroll
    jen "Eu não sei, provavelmente..."
    show jenny f_upset
    pause
    show debbie f_sad_talk
    deb "Olha, você não precisa me dizer se não quer..."
    deb "A decisão é tua."
    deb "O importante é que o bebê seja saudável e você receba o cuidado de que precisa."
    show debbie f_sad
    show jenny f_upset_talk
    jen "Mesmo?"
    show jenny f_upset
    show debbie f_sad_talk
    deb "É claro querida."
    deb "Eu só queria que você tivesse me dito mais cedo, eu poderia ter sido mais ajuda!"
    show debbie f_sad
    return

label entrance_jenny_first_baby_stage_2_diane:
    show diane f_laugh
    dia "Provavelmente porque ela está dormindo com metade da cidade..."
    show diane f_smirk
    show jenny f_angry_talk
    jen "Foda-se!"
    show jenny f_angry
    show diane f_annoyed
    show debbie f_angry_talk
    deb "Ei, pare com isso! Vocês dois!"
    show debbie f_angry
    show jenny f_angry_pouting_top
    jen "Hmmph!"
    pause
    show debbie f_sad_talk
    deb "Apenas me diga {b}[jen_name]{/b}."
    show debbie f_sad
    pause
    show jenny f_upset_talk
    jen "Eu acho que engravidei de um assento de toalete no shopping..."
    show jenny f_upset
    show diane f_laugh
    show debbie f_surprised_worried
    deb "{b}*Gasp*{/b}"
    show debbie f_sad
    show player f_surprised
    player_name "!!!"
    show player f_worried
    dia "Hahahaah, essa é a coisa mais ridícula que eu já ouvi!"
    show diane f_smirk
    show jenny f_angry_talk
    jen "Cale-se, {b}Diane{/b}!!!"
    show jenny f_upset
    show debbie f_sad_talk
    deb "Isso não é"
    show debbie f_sad
    pause
    show debbie f_surprised_worried
    deb "Isso pode acontecer?"
    show debbie f_sad
    show diane f_smirk_talk
    dia "Não."
    show diane f_smirk
    show jenny f_upset_talk
    jen "Sim pode!!"
    show jenny f_angry_pouting_top
    show diane f_lookup
    dia "Realmente não pode."
    show diane f_smirk
    show debbie f_sad_talk
    deb "{b}*Suspiro*{/b} pare."
    deb "Olha, ela não tem que me dizer se ela não quer..."
    show debbie f_sad
    show diane f_lookup
    dia "O inferno ela não!"
    show diane f_shamed_talk_smile_back
    dia "Você merece melhor do que"
    show diane f_shamed
    show debbie f_sad_talk
    deb "Está tudo bem, {b}Diane{/b}..."
    deb "É a decisão dela."
    deb "O importante é que o bebê seja saudável e {b}[jen_name]{/b} Obtém o cuidado que ela precisa."
    show debbie f_sad
    show diane f_shamed_talk_smile_back
    dia "Meu Deus, {b}[deb_name]{/b}..."
    dia "Você gosta muito com ela!"
    show diane f_shamed
    show debbie f_sad_talk
    deb "Apenas deixe ir, por favor."
    show debbie f_sad
    dia "..."
    show diane f_normal_talk
    dia "Està bem."
    dia "Eu tenho que ir de qualquer maneira..."
    show debbie b_empty a_empty f_normal
    show diane b_hug_deb_robe a_empty f_normal_talk at flip
    show diane at Position (xpos=914)
    with dissolve
    dia "Eu vou te ver hoje a noite, amor."
    show diane f_normal
    deb "..."
    hide diane
    show debbie b_robe a_robe_mug at Position (xpos=600)
    with dissolve
    return

label entrance_jenny_first_baby_stage_2_intro:
    scene expression L_home_entrance.background_closeup
    deb "Por que você não me diz quem é o pai?!"
    show player f_shock
    player_name "!!!" with hpunch
    jen "Você poderia, por favor, relaxar?, {b}[deb_name]{/b}?!"
    show player f_surprised_teeth
    player_name "( Uh oh, parece {b}[jen_name]'s{/b} segredo está fora de quetão... )"
    player_name "( É melhor eu ir até lá! )"
    $ player.go_to(L_home_kitchen)
    scene expression player.location.background_closeup
    show jenny at flip
    show jenny b_dressed_pregnant_bump f_upset a_dressed_crossed zorder 1 at Position (xpos=100)
    show debbie f_sad_talk zorder 1 at Position (xpos=600)
    if M_diane.finished_state(S_diane_check_barn_out):
        show diane b_casual a_casual_sides f_smirk zorder 0 at Position (xpos=400)
    show player f_worried zorder 2 at Position (xpos=400) with dissolve
    deb "Por que você não me diz quem é o pai?"
    show debbie f_sad
    show jenny f_upset_talk
    jen "Eu não sei quem é o pai, ok {b}[deb_name]{/b}?!"
    jen "Pare de perguntar!"
    show jenny f_upset
    show debbie f_sad_talk
    deb "Como você pode não saber?!"
    show debbie f_sad
    return

label entrance_jenny_want_some_breakfast:
    scene expression player.location.background_closeup with None
    show player
    show debbie f_normal_talk
    with dissolve
    deb "Querido, você poderia vir aqui por um segundo?"
    show debbie f_normal
    show player f_normal_talk
    player_name "Certo."
    $ player.go_to(L_home_kitchen)
    scene expression player.location.background_closeup with None
    show player f_normal_talk
    show debbie
    with dissolve
    player_name "Estás bem, {b}[deb_name]{/b}?"
    show player f_normal
    show debbie f_normal_talk
    deb "Você se importaria de perguntar {b}[jen_name]{/b} se ela quer um pouco desse café da manhã?"
    show debbie f_normal
    show player f_worried_talk
    player_name "Ehh, não me importo."
    player_name "Ela só vai dizer não..."
    show player f_worried
    show debbie f_laugh
    deb "Hehe, provavelmente."
    hide player
    show debbie b_robe_hug1 a_empty f_empty
    with dissolve
    deb "Obrigado querido."
    show debbie b_robe_hug2
    player_name "Sem problemas."
    hide debbie
    show player f_thinking a_dressed_thinking with dissolve
    player_name "( Hmm, eu acho que{b}[jen_name]{/b} està {b}descansando à beira da piscina...{/b} )"
    hide player with dissolve
    return

label entrance_jenny_catch_her_jilling:
    $ player.location = L_home_entrance
    if store._in_replay is not None:
        $ game.timer._tod = 3
    scene expression player.location.background_closeup with None
    show player f_thinking a_dressed_thinking at flip
    with dissolve
    player_name "( Hmm? )"
    player_name "( Por que a TV está ligada? )"
    pause
    player_name "( Alguém esqueceu de desligar? )"
    player_name "( Eu deveria verificar isso. )"
    hide player with dissolve
    scene expression "backgrounds/location_home_livingroom_couch_night_closeup.jpg"
    player_name "( É {b}[jen_name]{/b}?! )"
    player_name "( O que ela- )"
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show player 300 at Position(xpos=566,ypos=331)
    show jenny b_couch_clit a_empty f_empty zorder 2
    player_name "( !!! )"
    hide player
    show player 299d zorder 1 at Position (yoffset=-291,xoffset=16)
    with dissolve
    pause
    show player 301 at Position(xpos=602,ypos=386) with fastdissolve
    player_name "( Ela está se masturbando na sala de estar! )"
    player_name "( Isso é incrível! )"
    pause
    player_name "( O que ela está assistindo?! )"
    scene home_livingroom_tv
    show home_tv_channel_10 at Position(xpos=522, ypos=521)
    with dissolve
    player_name "( É uma mulher esfregando um cara com os pés! )"
    pause
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show player 301 at Position(xpos=602,ypos=386)
    show jenny b_couch_clit a_empty f_empty
    player_name "Pés!"
    show jenny b_couch_cought
    jen "!!!" with hpunch
    jen "Que porra, {b}[firstname]{/b}?!"
    hide player
    show player b_couch_sit a_couch_boner_covered f_couch_sit_right_talk zorder 1
    show jenny b_couch_sit f_couch_sit_angry a_couch_rest zorder 2
    with dissolve
    player_name "Me desculpe eu-"
    show player f_couch_sit_right
    show jenny f_couch_sit_angry_talk
    jen "Você está me perseguindo por toda a casa agora?!"
    show jenny f_couch_sit_angry
    show player f_couch_sit_right_talk
    player_name "Shh, você vai acordar {b}[deb_name]{/b}!"
    show player f_couch_sit_right
    show jenny f_couch_sit_upset_talk
    jen "Sério, o que eu tenho que fazer para conseguir algum tempo sozinha?!"
    jen "Está realmente começando-"
    show jenny f_couch_sit_surprised
    jen "Você está com uma ereção agora?"
    show player f_couch_sit_down_talk
    player_name "Uhh sim..."
    show player f_couch_sit_right_talk
    player_name "Você estava se masturbando e estava muito excitante..."
    show player f_couch_sit_right
    jen "Jesus."
    show jenny f_couch_sit_sexy_down
    pause
    show jenny f_couch_sit_sexy_talk_down
    jen "Deixa eu ver."
    show jenny f_couch_sit_sexy_down
    show player f_couch_sit_right_talk
    player_name "Hã?"
    show player f_couch_sit_right
    show jenny f_couch_sit_sexy_talk_down
    jen "Mostre-me!"
    show jenny f_couch_sit_sexy_down
    show player f_couch_sit_right_talk
    player_name "Ok..."
    show player f_couch_sit_down a_couch_boner_pull1 with dissolve
    pause
    show player f_couch_sit_down a_couch_boner_pull2 with dissolve
    show player f_couch_sit_down a_couch_boner with dissolve
    show jenny f_couch_sit_sexy_talk_down
    jen "Eu sempre quis experimentar isso..."
    show jenny f_couch_sit_sexy_down a_couch_up with dissolve
    show player f_couch_sit_down_surprised
    player_name "!!!"
    show player f_couch_sit_down_talk a_couch_sides
    $ M_jenny.set('sex speed', .3)
    show jenny a_empty
    show expression AnimatedImage("jenny_couch_dick_rub", [1,2,3], M_jenny) as jenny_couch_dick_rub zorder 3 at Position(xalign = 0.0, yoffset = 0)
    with dissolve
    player_name "O que você é"
    show player f_couch_sit_down
    show jenny f_couch_sit_sexy_talk_down
    jen "Shhh!"
    jen "Agora você é quem vai acordar {b}[deb_name]{/b}!"
    show jenny f_couch_sit_sexy_down
    player_name "..."
    pause
    if store._in_replay is not None:
        jump jenny_couch_fj_loop
    return

label entrance_jenny_catch_her_leaving_has_money_dom:
    show player 10
    player_name "Aqui."
    show player 41 with dissolve
    pause
    show player 5
    show jenny f_upset_talk a_money
    with dissolve
    jen "É sobre o maldito tempo..."
    show jenny f_grin_down a_dressed_money_counting
    pause
    show player 10
    player_name "Posso ir com você?"
    show player 5
    show jenny f_upset_talk a_dressed_hips with dissolve
    jen "O que?! NÃO!"
    show jenny f_upset
    show player 12
    player_name "C'mon!"
    show player 90
    show jenny f_upset_talk
    jen "Absolutamente não!"
    jen "Eu não vou sair em público com um perdedor como você..."
    show jenny f_gross
    show player 10
    player_name "... Mas eu te dei tanto dinheiro"
    show player 5
    pause
    show jenny f_upset_talk
    jen "Você é uma dor na minha bunda..."
    show jenny f_upset
    show player 40 with dissolve
    player_name "Por favor?!"
    pause
    show jenny f_eyeroll
    jen "{b}*Suspiro*{/b} Tudo bem, apenas pare de choramingar."
    show jenny f_upset
    show player 17 with dissolve
    player_name "Doce!"
    show player 13
    show jenny f_upset_talk
    jen "... E não ande muito perto! Eu não quero que as pessoas pensem que estamos juntos."
    show jenny f_upset
    show player 10
    player_name "Ok."
    hide player
    hide jenny
    with dissolve
    return

label entrance_jenny_catch_her_leaving_no_money_dom:
label entrance_jenny_catch_her_leaving_no_money_sub:
label entrance_jenny_catch_her_leaving_no_money_dom_first:
    show player 29 with dissolve
    player_name "Na verdade, eu não tenho duzentos agora..."
    show player 5 with dissolve
    show jenny f_upset_talk
    jen "Ugh, você está brincando comigo?"
    show jenny f_upset
    pause
    show jenny f_upset_talk
    jen "Bem, vá e pegue!"
    show jenny f_upset
    show player 12
    player_name "Sim Sim..."
    show player 90
    show jenny f_angry_talk
    jen "Estou falando sério!"
    show jenny f_angry
    show player 12
    player_name "Eu vou pegar, só relaxar."
    show jenny f_angry_talk
    jen "Se apresse!"
    hide player
    hide jenny
    with dissolve
    return

label entrance_jenny_catch_her_leaving_repeat:
    scene expression player.location.background_blur with None
    show player 5 at left
    show jenny b_casual f_upset_talk
    with dissolve
    jen "Você consegue o dinheiro?"
    show jenny f_upset
    return

label entrance_jenny_catch_her_leaving_has_money_sub:
    show player 10
    player_name "Aqui."
    show player 41 with dissolve
    pause
    show player 5
    show jenny f_upset_talk a_money
    with dissolve
    jen "É sobre o maldito tempo..."
    show jenny f_grin_down a_dressed_money_counting
    pause
    show player 10
    player_name "Posso ir com você?"
    show player 5
    show jenny f_upset_talk a_dressed_hips with dissolve
    jen "O que?! NÃO!"
    show jenny f_upset
    show player 12
    player_name "C'mon!"
    show player 90
    show jenny f_upset_talk
    jen "Absolutamente não!"
    jen "Eu não vou sair em público com um perdedor como você..."
    show jenny f_gross
    show player 10
    player_name "... Mas eu te dei tanto dinheiro"
    show player 5
    pause
    show jenny f_upset_talk
    jen "Você é uma dor na minha bunda..."
    show jenny f_upset
    show player 40 with dissolve
    player_name "Por favor?!"
    pause
    show jenny f_eyeroll
    jen "{b}*Suspiro*{/b} Tudo bem, apenas pare de choramingar."
    show jenny f_upset
    show player 17 with dissolve
    player_name "Doce!"
    show player 13
    show jenny f_upset_talk
    jen "... E não ande muito perto! Eu não quero que as pessoas pensem que estamos juntos."
    show jenny f_upset
    show player 10
    player_name "Ok."
    hide player
    hide jenny
    with dissolve
    return

label entrance_jenny_catch_her_leaving:
    show expression player.location.background_blur with None
    show player 5 at left
    show jenny b_casual a_phone f_grin_down at flip
    show jenny at Position (xpos=500)
    with dissolve
    pause
    show player 10
    player_name "Onde você vai?"
    show player 5
    show jenny f_gross_down_talk
    jen "Out."
    show jenny f_grin_down
    show player 10
    player_name "Uhh, ok?"
    show player 5
    pause
    show player 12
    player_name "Cuidado ao elaborar?"
    show player 5
    show jenny f_gross_down_talk
    jen "Eu preciso pegar algumas coisas do shopping..."
    show jenny f_grin_down
    pause
    show player 10
    player_name "Que tipo de coisas?"
    show player 5
    show jenny f_eyeroll
    jen "Não é da sua conta, perdedor!"
    jen "Eu não sei porque você sempre tem que ter o seu nariz no meu negócio?!"
    show jenny f_gross_down
    pause
    show player 24
    show jenny f_angry_pouting_top
    pause
    hide jenny
    show jenny b_casual f_upset_talk
    with dissolve
    jen "Quanto dinheiro você tem?."
    show jenny f_upset
    show player 10
    player_name "Hã?"
    show player 5
    show jenny f_upset_talk
    jen "Dá-me duzentos dólares."
    show jenny f_upset
    show player 12
    player_name "De jeito nenhum, eu já te dei muito dinheiro!"
    show player 5
    show jenny f_eyeroll
    jen "Sim e você tem coisas em troca!"
    show jenny f_upset_talk
    jen "Não aja como se eu não fosse mais do que justo com você..."
    show jenny f_upset
    return

label entrance_jenny_catch_her_leaving_dom_first:
    show player 10
    player_name "Tudo bem, então o que eu ganho desta vez?"
    show player 5
    show jenny f_upset_talk
    jen "Você não está ganhando merda."
    show jenny f_upset
    show player 12
    player_name "està bem."
    show player 12f with dissolve
    player_name "Divirta-se fazendo compras."
    show player 90f
    show jenny f_upset_talk
    jen "Esperar!"
    show jenny f_upset
    show player 17 with dissolve
    pause
    show jenny f_angry_talk
    jen "Grr, DROGA!"
    show jenny f_angry_pouting
    pause
    show jenny f_angry_talk
    jen "Por que você não faz o que eu pergunto?!"
    show jenny f_angry
    show player 12
    player_name "Por que você nunca me pergunta bem?"
    show player 5
    show jenny f_upset_talk
    jen "C'mon, {b}[firstname]{/b}! Você me deve por isso por estragar meu brinquedo no outro dia."
    show jenny f_upset
    show player 4 with dissolve
    player_name "( Cara, transa com ela. Ela tem sorte que eu comprei aquele brinquedo para ela... )"
    player_name "( ... Então, novamente, esta pode ser uma boa oportunidade para aprender mais sobre o que ela está fazendo com esse dinheiro. )"
    show jenny f_upset_talk
    jen "Então você vai me dar o dinheiro ou não?"
    show jenny f_upset
    show player 12 with dissolve
    player_name "Sim, eu acho ... Se você disser por favor."
    show player 5
    show jenny f_eyeroll
    jen "Ugh..."
    jen "Por favor?"
    show jenny f_angry_pouting_top
    return

label entrance_jenny_catch_her_leaving_sub_first:
    show player 26
    player_name "Sim, tudo bem"
    show player 11
    show jenny f_upset_talk
    jen "Pare de ser uma putinha, {b}[firstname]{/b}!"
    jen "Você ganha muito dinheiro."
    jen "Além disso, você me deve por essa pequena bagunça com o brinquedo no outro dia."
    show jenny f_upset
    show player 4 with dissolve
    player_name "( Ugh, eu acho que ela está certa sobre isso... )"
    player_name "( ... E esta pode ser uma boa oportunidade para aprender mais sobre o que ela está fazendo por esse dinheiro. )"
    show jenny f_upset_talk
    jen "Umm, Olá?!"
    jen "Terra para perdedor!"
    show jenny f_upset
    show player 10 with dissolve
    player_name "{b}*Suspiro*{/b} Està bem."
    player_name "Você disse duzentos?"
    show player 5
    show jenny f_grin_talk
    jen "Sim."
    show jenny f_grin
    return

label entrance_jenny_debbie_altercation:
    scene expression player.location.background_closeup with None
    show jenny f_upset_talk a_dressed_crossed
    show debbie 10bf zorder 1 at left
    jen "Por que não?!"
    show jenny f_upset
    show debbie 11bf
    deb "Porque eu não posso pagar!"
    deb "Você não é mais uma criança {b}[jen_name]{/b}..."
    deb "Se você quiser roupas novas, então você precisa arranjar um emprego e comprá-los com seu próprio dinheiro."
    show debbie 10bf
    show player 5 zorder 0 at Position (xpos=400)
    show jenny f_upset_talk
    jen "Como posso conseguir um emprego quando não tenho nada legal para usar na entrevista?!"
    show jenny f_upset
    show debbie 9bf with dissolve
    pause
    show debbie 11bf with dissolve
    deb "{b}[jen_name]{/b}, você tem muitas roupas bonitas..."
    show debbie 10bf
    show jenny f_upset_talk
    jen "Não é bom o suficiente, não para o trabalho que eu quero..."
    show jenny f_upset
    show player 12
    player_name "Que tipo de trabalho você está tentando conseguir?"
    show player 5
    show jenny f_eyeroll
    jen "Eu não sei, algo com um escritório, talvez?"
    show jenny f_upset
    show player 12
    player_name "Hah, sim certo."
    player_name "Eu não acho que muitas empresas estão procurando por uma faculdade desistir sem qualificações e experiência zero..."
    show player 90
    show jenny f_upset_talk
    jen "Cale a boca, bosta!"
    jen "Quem pediu sua opinião?!"
    show jenny f_upset
    show player 11
    show debbie 11bf
    deb "Vocês dois pode parar com isso?!"
    show jenny f_angry_pouting
    deb "Estou tão cansada de vocês brigar o tempo todo."
    show debbie 10bf
    show player 24
    player_name "Desculpa, {b}[deb_name]{/b}."
    show player 5
    show debbie 11bf
    deb "{b}*Suspiro*{/b} Apenas pegue algo do meu armário, {b}[jen_name]{/b}."
    show debbie 10bf
    show jenny f_upset_talk
    jen "Està bem."
    show jenny f_upset
    pause
    show debbie 11bf
    deb "Você nunca deveria ter desistido do seu trabalho {b}Consum-R{/b}..."
    show debbie 10bf
    show jenny f_upset_talk
    jen "Esse trabalho era RUIM!"
    show jenny f_upset
    show player 9 at Position (xoffset=41) with dissolve
    show debbie 11bf
    deb "Oh, cresça, {b}[jen_name]{/b}."
    deb "Você acha que todos gostam do que fazem para viver?!"
    show debbie 10bf
    show jenny f_upset_talk
    jen "... Não."
    show jenny f_upset
    show debbie 11bf
    deb "As pessoas fazem o que têm para colocar comida na mesa!"
    deb "Eu não posso te apoiar para sempre, sabe?!"
    show debbie 10bf
    show player 5 with dissolve
    show jenny f_upset_talk
    jen "Oh, isso é muito legal {b}[deb_name]{/b}..."
    show jenny f_eyeroll
    jen "Desculpe, eu sou um fardo tão grande para vocês!"
    show jenny f_upset
    show debbie 11bf
    deb "eu nunca disse isso."
    show debbie 10bf
    show jenny f_upset_talk
    jen "Você pode muito bem ter dito!"
    jen "Não se preocupe, você não terá que me aturar por muito tempo."
    jen "No segundo em que recebo um pouco de dinheiro, vou embora."
    show jenny f_angry_pouting_top
    show debbie 11bf
    deb "... Nossa que drama."
    deb "Por que você sempre tem que transformar tudo em um grande drama?!"
    show debbie 10bf
    show jenny f_angry_pouting
    jen "..."
    show debbie 11bf
    deb "{b}*Suspiro*{/b} Você sabe que te amo {b}[jen_name]{/b} e você não é um fardo..."
    deb "Só estou dizendo que você precisa fazer algo na sua vida."
    deb "Você não pode ficar sentado em sua bunda para sempre, esperando a oportunidade perfeita para se apresentar."
    deb "Você tem que sair e fazer acontecer."
    show debbie 10bf
    show jenny f_upset_talk
    jen "Sim Sim..."
    hide jenny with dissolve
    jen "Deus, eu não posso esperar para deixar esta cidade estúpida!"
    pause
    show debbie at center
    show player at left
    with dissolve
    deb "..."
    show debbie 11bf
    deb "Talvez eu esteja sendo muito duro com ela?"
    show debbie 10bf
    show player 10
    player_name "Eh, na verdade não."
    player_name "Quer dizer, estou ajudando por aqui e ela é mais velha do que eu..."
    show player 5
    show debbie 11bf
    deb "eu sei."
    hide player
    show debbie 4b at left
    with dissolve
    deb "Eu realmente aprecio isso, querido."
    deb "Você é um bom menino."
    show debbie 4
    pause
    show player 13 at left
    show debbie 2 at right
    with dissolve
    deb "Quer que eu faça algo para você comer?"
    show debbie 1
    show player 14
    player_name "Não, tudo bem {b}[deb_name]{/b}..."
    player_name "Eu não estou com muita fome."
    show player 13
    show debbie 2
    deb "Tudo bem."
    deb "Talvez eu faça uma torta..."
    deb "... Algo para tirar minha mente de todo esse drama."
    show debbie 1
    show player 17
    player_name "Tudo bem."
    show player 13
    hide debbie with dissolve
    pause
    show player 5
    player_name "( Pobre {b}[deb_name]{/b}. )"
    player_name "( {b}[jen_name]{/b} não percebe o quão sortuda ela é... )"
    hide player with dissolve
    return

label entrance_diane_gave_birth_dialogue_seen:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 10 at left
    show debbie 1f at Position (xpos=600)
    show diane a_casual_baby b_casual at Position (xpos=625)
    show jenny f_grin at flip
    show jenny at Position (xpos=150)
    with dissolve
    player_name "{b}Diane{/b}?"
    show player 14
    player_name "Vocês estão finalmente em casa?"
    show player 13
    show diane f_normal_talk
    dia "Sim, estamos em casa."
    show diane f_normal
    show debbie 2f
    show diane f_down_front
    if M_diane.pregnancy.baby_gender == "boy":
        deb "Ele é a coisa mais preciosa que nunca existiu?!"
        show debbie 1f
        show jenny f_normal_talk
        jen "Eu não sei, ele parece um tipo de batata..."
        show jenny f_normal
        show debbie 2f
        deb "Não ele não!"
        deb "Ele é tão lindo!"
        show debbie 1f
        pause
        show debbie 2f
        deb "Quem é um menino bonito, huh?"
    elif M_diane.pregnancy.baby_gender == "twins":
        deb "Eles é a coisa mais preciosa que nunca existiu??!"
        show debbie 1f
        show jenny f_normal_talk
        jen "Eu não sei, eles parecem com batatas..."
        show jenny f_normal
        show debbie 2f
        deb "Não eles não!"
        show debbie 1f
        pause
        show debbie 2f
        deb "Quem é lindo, né?"
    else:
        deb "Ela é a coisa mais preciosa que nunca existi?!"
        show debbie 1f
        show jenny f_normal_talk
        jen "Eu não sei, ela parece uma batata..."
        show jenny f_normal
        show debbie 2f
        deb "Não ela não!"
        deb "Ela é linda!"
        show debbie 1f
        pause
        show debbie 2f
        deb "Quem é uma garota bonita, hein?"
    show debbie 1f
    show diane f_laugh
    dia "Hehe!"
    show diane f_normal
    show debbie 2f
    if M_diane.pregnancy.baby_gender == "twins":
        deb "Eu não posso acreditar que você finalmente tem filhos, {b}Diane{/b}."
    else:
        deb "Eu não posso acreditar que você finalmente tem um filho {b}Diane{/b}."
    deb "Eu estou tão feliz por você!"
    show debbie 1f
    show diane f_normal_talk
    dia "Eu sei, eu não acho que alguma vez chegaria a ser uma mamãe."
    show diane f_normal
    show debbie 2f
    show diane f_down_front
    if M_diane.pregnancy.baby_gender == "boy":
        deb "Ele é tão adorável..."
        show jenny f_eyeroll
        show debbie 3f
        deb "Eu poderia apenas engolir ele!"
        show debbie 1f
        show jenny f_normal
        pause
        show diane f_normal_talk
        dia "Eu realmente deveria derrubá-lo noite."
        dia "Ele teve um dia agitado."
    elif M_diane.pregnancy.baby_gender == "twins":
        deb "Eles são tão adoráveis..."
        show jenny f_eyeroll
        show debbie 3f
        deb "Eu poderia apenas engolir eles!"
        show debbie 1f
        show jenny f_normal
        pause
        show diane f_normal_talk
        dia "Eu realmente deveria derrubá-los a noite."
        dia "Eles tiveram um dia agitado."
    else:
        deb "Ela é tão adorável..."
        show jenny f_eyeroll
        show debbie 3f
        deb "Eu poderia apenas devorar ela!"
        show debbie 1f
        show jenny f_normal
        pause
        show diane f_normal_talk
        dia "Eu realmente deveria derrubá-la a noite."
        dia "Ela teve um dia agitado."
    show diane f_down_front
    show debbie 2f
    deb "Aww, tudo bem..."
    if M_diane.pregnancy.baby_gender == "twins":
        deb "Tchau tchau, pequeninos."
    else:
        deb "Tchau tchau, pequenino."
    show debbie 1f
    pause
    show debbie 1 at right
    show jenny at Position (xpos=200)
    hide diane
    with dissolve
    pause
    show debbie 3
    deb "Eu adoro bebês!"
    show debbie 1
    show jenny f_eyeroll
    jen "Ugh, tanto faz."
    show jenny f_upset_talk
    if M_diane.pregnancy.baby_gender == "twins":
        jen "Se essas coisas ficar a noite toda gritando, eu absolutamente vou perder minha paciência!"
    else:
        jen "Se essa coisa ficar a noite toda gritando, eu vou absolutamente perder minha paciência!"
    show jenny f_upset
    show debbie 13
    deb "{b}*Suspiro*{/b}, {b}[jen_name]{/b}..."
    deb "Não seja assim, querida."
    show debbie 14b
    show jenny f_normal_talk
    jen "Eu só estou dizendo, eu preciso das minhas oito horas ou eu fico irritada."
    show jenny f_normal
    show player 12
    player_name "Você é sempre estar irritada..."
    show player 13 with None
    show jenny f_upset_talk at unflip
    show jenny at Position (xpos=-200)
    with dissolve
    jen "O que você disse?!"
    show jenny f_gross
    show player 10
    player_name "Nada."
    show player 5
    pause
    show jenny f_upset_talk
    jen "Uh hã."
    show jenny f_upset
    pause
    show jenny f_upset_talk
    jen "É melhor você calar sua boca."
    jen "Eu sei onde você dorme."
    hide jenny with dissolve
    pause
    show player 12
    player_name "Ela é um raio de sol..."
    show player 13
    show debbie 3
    deb "Hehehe!"
    show debbie 2
    deb "Oh, não ligue para ela."
    deb "Ela gosta de bebês também, ela só não quer admitir."
    show debbie 1
    show player 12
    player_name "Se você diz."
    hide player
    hide debbie
    hide diane
    with dissolve
    return

label entrance_diane_peeking:
    scene expression "backgrounds/location_home_entrance_night_blur.jpg"
    show player 34 with dissolve
    pause
    show player 35
    player_name "Hmm, com certeza está quieto aqui esta noite..."
    show player 10
    player_name "eu imagino o que {b}[deb_name]{/b} e {b}Diane{/b} estão fazendo."
    show player 14
    player_name "{b}Elas geralmente estão na sala de estar assistindo tv e conversando com garotas."
    player_name "{b}Eu deveria verificar isso.{/b}"
    hide player with dissolve
    return

label entrance_diane_couch_crashing:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 13 at left
    show diane b_casual a_casual_bag f_laugh zorder 1 at Position (xpos=625)
    with dissolve
    dia "Querida, estamos em casa!"
    dia "Haha!"
    show player 17
    player_name "Haha!"
    show diane f_normal
    show debbie 2f zorder 0 with dissolve
    deb "O que diabos vai-"
    show debbie 3f
    show player 13
    deb "{b}*Gasp*{/b} Você está aqui!"
    show debbie 2f
    show diane f_normal_talk
    dia "Estou aqui!"
    show diane f_normal_talk a_casual_bag_point with dissolve
    dia "Estamos começando com uma festa do pijama?"
    show diane f_normal a_casual_bag
    show debbie 222f
    with dissolve
    deb "Hã?"
    pause
    show debbie 3f with dissolve
    deb "Oh, shuddup."
    show debbie 1f
    show diane f_normal_talk
    dia "Estou falando sério, trouxe minha camisola e tudo mais!"
    show diane f_normal
    show debbie 2f
    deb "Está com fome?"
    show debbie 1f
    show diane f_normal_talk
    dia "Oh, serviço de quarto e tudo mais."
    show diane f_smirk_talk
    dia "Você não me disse que seria tão chique..."
    show diane f_smirk
    show debbie 2f
    deb "Basta entrar aqui e eu vou ajudá-lo a desfazer as malas."
    show debbie 1f
    show diane f_laugh
    dia "Sim, senhora."
    show diane f_normal_talk
    dia "Você quer se juntar a nós, {b}[firstname]{/b}?"
    show debbie 1 with dissolve
    show diane f_normal
    show player 55 with dissolve
    player_name "{b}*Bocejar*{/b}"
    show player 26 with dissolve
    player_name "... Certo!"
    show player 25
    show debbie 2
    deb "Oh querido, você parece exausto!"
    deb "Por que você simplesmente não vai para a cama e deixa {b}Diane{/b} e eu passo algum tempo juntos.."
    show diane f_wink
    show debbie 1f with dissolve
    pause
    show diane f_smirk_talk
    dia "Mmm, tempo juntos, hã?"
    show diane f_smirk
    show debbie 3f
    deb "Oh, hush!"
    show diane f_laugh
    dia "Haha."
    show diane f_normal
    show debbie 1 with dissolve
    show player 26
    player_name "Sim, ok."
    player_name "Eu estou bem cansado."
    show player 25
    show diane f_smirk_talk
    dia "Eu acho que é só você e eu, linda."
    show diane f_smirk
    show debbie 3f with dissolve
    deb "Hehe, pare com isso!"
    show debbie 1f
    show diane f_smirk_talk
    dia "Boa noite, {b}[firstname]{/b}."
    show player 55
    hide debbie
    hide diane
    with dissolve
    pause
    hide player with dissolve
    return

label entrance_diane_debbie_drop_off_request:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 13 at left
    show debbie 221 at right
    with dissolve
    deb "Aguente, {b}[firstname]{/b}."
    show debbie 220
    show player 14
    player_name "Ei, {b}[deb_name]{/b}."
    player_name "Estás bem?"
    show player 13
    show debbie 221
    deb "Você fez algum trabalho para {b}Diane{/b} hoje?"
    show debbie 220
    show player 14
    player_name "Sim, eu estava lá mais cedo."
    show player 13
    show debbie 221
    deb "Ela está bem?"
    show debbie 220
    show player 5
    player_name "Hmm?"
    show player 10
    player_name "Sim, eu acho..."
    show player 5
    show debbie 221
    deb "... Porque eu acabei de desligar o telefone com ela e ela parece exausta."
    show debbie 220
    show player 10
    player_name "Bem, ela está trabalhando muito duro com esse novo negócio dela."
    player_name "Eu disse a ela para ir mais devagar, mas você sabe o quão apaixonada ela é sobre isso."
    show player 5
    show debbie 221
    deb "Sim, ela tem uma tendência a se dedicar ao seu trabalho e desconsiderar suas necessidades."
    deb "Isso me preocupa."
    deb "Você se importaria de voltar para lá?"
    show debbie 220
    show player 10
    player_name "Esta noite?"
    show player 5
    show debbie 221
    deb "Sim, quero que você leve para ela esta torta que fiz hoje e garanta que ela coma!"
    deb "Ela provavelmente não comeu nada o dia todo."
    show debbie 220
    show player 14
    player_name "Sim, eu posso fazer isso"
    show player 13
    show debbie 221
    deb "Eu realmente apreciaria isto."
    show debbie 2
    show player 673
    with dissolve
    deb "Diga a ela que é melhor que durma bem por oito horas, que vou visita-la em breve!"
    show debbie 1
    show player 674
    player_name "Tudo bem."
    hide debbie
    hide player
    with dissolve
    return

label entrance_erik_bullying:
    scene expression L_home_entrance.background
    show mrsj 19c at right with dissolve
    show player 10 at left with dissolve
    player_name "Está tudo bem, {b}Mrs. Johnson{/b}?"
    show player 5
    show mrsj 19
    mrsjo "Desculpe incomodá-lo esta manhã."
    show mrsj 52
    mrsjo "É só ... é sobre {b}Erik{/b}."
    mrsjo "O {b}Erik{/b} tem tido problemas ultimamente na escola?"
    show mrsj 19c
    show player 12
    player_name "Hã?"
    show player 35
    player_name "Não que eu saiba?"
    show player 10
    player_name "Ele geralmente tira notas boa na escola..."
    show player 5
    show mrsj 20
    mrsjo "Não. Eu não estou falando de notas."
    show mrsj 52
    mrsjo "As outras crianças da escola estão dando {b}Erik{/b} um momento difícil?"
    mrsjo "Ele está pedindo para ficar em casa em vez de ir para a aula."
    show mrsj 20
    mrsjo "Eu até o vi chegar em casa na semana passada com hematomas."
    show mrsj 19c
    show player 23
    player_name "!!!" with hpunch
    show player 12
    player_name "{b}Erik{/b} é bem tranquilo na escola."
    player_name "Eu nunca o vi se envolver em qualquer tipo de coisa ruim."
    show player 5
    show mrsj 19
    mrsjo "Talvez, se um amigo próximo parasse para vê-lo, ele estaria mais disposto a falar..."
    show mrsj 19c
    show player 10
    player_name "Você quer que eu pergunte a ele?"
    show player 5
    show mrsj 19
    mrsjo "Eu só quero o melhor para ele, e você é o único amigo que ele tem."
    show mrsj 19c
    show player 12
    player_name "OK. Eu vou ver ele."
    hide mrsj
    hide player
    with dissolve
    return

label entrance_erik_bullying_3:
    scene expression L_home_entrance.background
    show mrsj 19c at Position (xpos=700)
    show debbie 13 at right
    with dissolve
    show player 5 at left with dissolve
    deb "Querido!! Você está bem?!"
    show debbie 14b
    show player 10
    player_name "Estou bem, {b}[deb_name]{/b}. A enfermeira disse que eu tive uma pequena contusão."
    show player 11
    show debbie 13
    deb "Você teve uma contusão!"
    show debbie 14b
    show player 10
    player_name "Tudo está bem. Eu ficarei bem, {b}[deb_name]{/b}."
    show player 5
    show debbie 13
    deb "Sua escola estúpida nem ligou para me avisar que você estava no hospital!"
    deb "Eu tive que ouvir sobre isso {b}Tammy{/b}!"
    show debbie 14b
    show player 10
    player_name "{b}[deb_name]{/b}, está tudo bem. Eu estou muito bem! Acalme-se."
    show player 11
    show debbie 13
    deb "Me desculpe ... eu estava tão preocupada com você!"
    deb "Seu {b}pai{/b} está contando comigo para cuidar de você!"
    show debbie 14b
    show mrsj 19
    mrsjo "Estou tão feliz em ver que você está bem {b}[firstname]{/b}."
    mrsjo "Eu vim aqui para ajudar {b}[deb_name]{/b} assim que {b}Erik{/b} me ligou."
    mrsjo "Você fez uma coisa boa em pé por {b}Erik{/b}."
    show mrsj 38
    show debbie 13
    deb "Sim, foi muito corajoso da sua parte defender o seu amigo na escola."
    deb "Mas, por favor, seja cuidadoso!"
    show debbie 14b
    show player 24
    player_name "eu sei {b}[deb_name]{/b}..."
    show player 25
    player_name "Eu prometo que vou tentar evitar problemas."
    show player 24
    show debbie 13
    deb "Venha aqui."
    hide player
    hide debbie
    hide mrsj
    with dissolve
    show mrsj 14 at right
    show debbie 4
    with dissolve
    deb "Estou tão feliz por você estar seguro."
    deb "{b}Seu pai{/b} entraria em choque se soubesse que deixei isso acontecer."
    player_name "Está tudo bem, {b}[deb_name]{/b}."
    hide debbie
    hide mrsj
    with dissolve
    show mrsj 14 at Position (xpos=700)
    show debbie 1 at right
    show player 13 at left
    with dissolve
    show mrsj 17
    mrsjo "obrigada novamente, {b}[firstname]{/b}."
    mrsjo "Você é sempre bem-vindo para parar me visitar."
    show mrsj 14
    show player 14
    player_name "Está bem. Apenas estava ajudando um amigo."
    show player 13
    show mrsj 17
    mrsjo "Obrigada."
    show mrsj 14
    show player 36 with dissolve
    player_name "Boa noite {b}Mrs. Johnson{/b}."
    show player 13 with dissolve
    show mrsj 17
    mrsjo "Boa noite."
    hide mrsj with dissolve
    show debbie 2
    deb "Agora corra para a cama e descanse um pouco."
    hide player
    hide debbie
    with dissolve
    return

label entrance_mia_angelicas_impatience:
    scene expression L_home_entrance.background
    show debbie 1f at Position (xpos=500)
    show ang 1 at right
    with dissolve
    pause.5
    show player 5 at left
    show debbie 3
    with dissolve
    deb "Ali está ele!"
    show debbie 1
    show player 22
    player_name "!!!" with hpunch
    show debbie 2
    deb "Estou tão feliz em ouvir {b}[firstname]{/b} visitou nossa igreja local ultimamente..."
    deb "... E ofereceu trabalho voluntário com o clero!"
    show debbie 1
    show player 24
    player_name "HÃ..."
    show debbie 2
    deb "Bem! Vou deixar vocês dois para isso, eu tenho coisas cozinhando na cozinha!"
    show debbie 2f with dissolve
    deb "Foi ótimo conhecê-la {b}Irmã Angelica{/b}!"
    hide debbie with dissolve
    show player 12
    player_name "Trabalho voluntário?"
    player_name "E por que você está aqui?!"
    show player 11
    show ang 2
    ang "Eu pensei que nós tínhamos um acordo?"
    show ang 1
    show player 24
    player_name "..."
    show ang 2
    ang "Você achou que eu apenas deixaria você escapar de mim?!"
    show ang 1
    show player 10
    player_name "Não, eu só ... O que você quer de mim?"
    show player 11
    show ang 2
    ang "A porta da igreja ficará destrancada à noite."
    ang "Venha me visitar no meu quarto e eu vou explicar o que eu preciso de você..."
    ang "...E não tente se esconder de mim novamente, ou então"
    show ang 1
    show player 12
    player_name "Está bem, está bem!"
    player_name "Apenas não diga nada ao Minha {b}landlady{/b}..."
    show player 11
    show ang 2
    ang "Isso vai depender de você..."
    hide ang with dissolve
    show player 12
    player_name "Agora eu tenho que ir vê-la na igreja? No meio da noite?!"
    show player 10
    player_name "Isto é estranho..."
    hide player with dissolve
    return

label entrance_mia_angelicas_home_visit:
    scene expression L_home_entrance.background with fade
    show debbie 2f at Position (xpos=500)
    show ang 1 at right
    with dissolve
    pause.5
    show player 5 at left
    show debbie 3f
    with dissolve
    deb "É sempre um prazer ouvir isso {b}[firstname]{/b} que você está envolvido com a igreja."
    deb "Vocês dois devem estar se conhecendo muito bem."
    show debbie 1f
    show ang 2
    ang "Sim, {b}[firstname]{/b} tem sido muito útil trazer pecadores miseráveis."
    ang "{b}Deus{/b} certamente se lembrará de seus frutos de amor para seus vizinhos."
    show ang 1
    show debbie 3f
    deb "Isso é ótimo!"
    deb "Eu sei que todos nós podemos ser impertinentes às vezes..."
    show debbie 2f
    deb "Bem, então é melhor eu ir. A roupa não vai se dobrar."
    hide debbie with dissolve
    show ang 3
    player_name "..."
    show player 30
    player_name "E agora?"
    player_name "Eu trouxe você{b}Helen{/b}. Não é suficiente?"
    show player 5
    show ang 4
    ang "Oh não meu querido filho. {b}Deus{/b} Tem muitas coisas para você."
    ang "{b}Helen{/b} está longe de ser purificado. Sua teimosia é muito irritante."
    show ang 3
    show player 26
    player_name "Me fale sobre isso."
    show player 5
    show ang 2
    ang "Os cristãos mais penitentes exigem cuidados extras."
    ang "Eles precisam ser quebrados de seu pedestal para que possamos reconstruí-los."
    ang "Eu acredito que vai demorar mais dois rituais para ela..."
    ang "É por isso que vim te ver."
    ang "Eu estou precisando de uma ferramenta essencial usada nos tempos bíblicos."
    show ang 1
    show player 11
    player_name "..."
    show player 12
    player_name "O que você precisa?"
    show player 5
    show ang 2
    ang "Pretendo subverter {b}Helen{/b} tatravés dos meios de flagelação."
    show ang 1
    show player 12
    player_name "Como?"
    show player 5
    show ang 4
    ang "Me pega {b}um chicote{/b}."
    show ang 3
    show player 23
    player_name "{b}Um chicote{/b}!?"
    show player 11
    show ang 4
    ang "Eu preferiria um gato com nove caudas, das quais {b}Salvador{/b} foi submetido a."
    ang "Mas temo que isso seja mais difícil de acontecer."
    ang "{b}Um chicote de couro padrão{/b} vai fazer."
    show ang 2
    ang "Traga para mim em meus aposentos."
    show ang 1
    show player 10
    player_name "Isso não parece certo-"
    show player 11
    show ang 2
    ang "Você esqueceu o seu lugar? Não me faça lembrar a você e a todos os outros de seus pecados depravados!"
    show ang 1
    show player 15
    player_name "Mas você quer chicotear {b}Helen{/b}!"
    show player 16
    show ang 2
    ang "Você fez um acordo comigo. Não questione meus ... métodos da igreja."
    show ang 1
    show player 12
    player_name "Não está certo."
    show player 5
    show ang 4
    ang "E quem é você para julgar o certo do errado?"
    show ang 3
    show player 24
    player_name "..."
    show player 12
    player_name "Bem. Onde eu devo encontrar? {b}um chicote{/b} Apesar?"
    show player 17
    player_name "Existe uma lista de distribuidores na parte de trás da bíblia?"
    show player 5
    show ang 1
    ang "..."
    show ang 2
    ang "Tenho certeza que alguém da sua idade sabe de lugares sujos cheios de luxuria que vendem essas coisas."
    ang "Não me deixe esperando."
    hide ang with dissolve
    show player 37 with dissolve
    player_name "Eu nunca deveria ter ido à igreja."
    pause
    show player 38 with dissolve
    player_name "Onde eu vou conseguir {b}um chicote{/b}?"
    player_name "Talvez a {b}Loja rosa no shopping{/b} tem algo assim."
    show player 37 with dissolve
    player_name "..."
    hide player with dissolve
    return

label entrance_mia_angelicas_final_home_visit:
    scene expression L_home_entrance.background with fade
    show player 11 at left
    show ang 2 at right
    with dissolve
    ang "Já é hora de você descer."
    ang "Eu preciso de você de novo."
    show ang 1
    show player 5
    player_name "..."
    show player 12
    player_name "Não tenho certeza se quero continuar ajudando depois do que você fez com {b}Helen{/b}."
    show player 5
    show ang 4
    ang "Oh, não seja tão ingênuo!"
    ang "Apesar de sua relutância, nós dois sabemos que ela gostou."
    show ang 3
    show player 11
    player_name "..."
    show ang 2
    ang "Eu não vim aqui para discutir com um pecador."
    show ang 39 with dissolve
    ang "Se você realmente pretende ajudar {b}Helen{/b} você vai me ajudar a obter isso..."
    show ang 38
    pause
    show ang 3
    show player 459 at Position (xoffset=1)
    with dissolve
    player_name "..."
    hide player
    hide ang
    show note_01_c
    with dissolve
    pause
    hide note_01_c
    show player 1 at left
    show ang 3 at right
    show player 460 at Position (xoffset=1)
    with dissolve
    player_name "O que é isso?"
    show player 461 at Position (xoffset=1)
    show ang 4
    ang "É um elemento crucial para o ritual final de {b}Helen's{/b} purificação..."
    ang "...E sua última tarefa."
    show ang 3
    show player 460 at Position (xoffset=1)
    player_name "Mas como isso vai ser usado para purificar {b}Helen{/b}?"
    show player 11 with dissolve
    show ang 2
    ang "Não me questione!"
    ang "Os pecadores devem apenas aceitar as palavras ditas {b}de Deus{/b} escolhido."
    ang "Agora me pegue o item na foto e me encontre em meus aposentos."
    show ang 1
    show player 5
    player_name "..."
    show player 12
    player_name "Tudo bem..."
    show player 5
    show ang 2
    ang "Bom. E seja rápido sobre isso."
    hide ang with dissolve
    show player 5
    player_name "..."
    show player 10
    player_name "{b}Helen{/b} nem parece perceber {b}Irmã Angelica{/b} está a transformando em..."
    player_name "...Uma aberração sexual!"
    show player 12
    player_name "Eu deveria falar com {b}Harold{/b} antes de ajudar {b}Irmã Angelica{/b}."
    player_name "Talvez ele possa me ajudar a descobrir o que fazer."
    show unlock55 at truecenter with dissolve
    $ player.get_item("strapon_drawing")
    pause
    hide unlock55 with dissolve
    hide player with dissolve
    return

label entrance_mom_overheard:
    scene expression game.timer.image("home_entrance{}")
    show player 34 with dissolve
    player_name "...{b}*voz distante*{/b}..."
    show player 35
    player_name "( É {b}[deb_name]{/b} no telefone? )"
    show player 12
    player_name "( ...Ela parece estar com raiva. Ela está gritando? )"
    show player 10
    player_name "( Eu deveria ir ver se ela está bem. )"
    hide player with dissolve
    return

label entrance_mom_lawn_help:
    scene expression L_home_entrance.background
    show player 1 at left
    show debbie 2 at right
    with dissolve
    if game.timer.is_morning():
        deb "Bom dia, querido."
    else:
        deb "Olá docinho."
    show debbie 1
    show player 2
    if game.timer.is_morning():
        player_name "Bom dia, {b}[deb_name]{/b}."
    else:
        player_name "Olá, {b}[deb_name]{/b}."
    show player 1
    show debbie 2
    if game.timer.is_morning():
        deb "Pronto para a escola?"
    else:
        deb "Feliz por estar de volta à escola?"
    show debbie 1
    show player 10
    player_name "Sim, eu acho. Eu tenho muito trabalho de casa para pôr em dia."
    show player 1
    show debbie 3
    deb "Ah, tenho certeza que você vai se sair bem."
    show debbie 2
    deb "É bom voltar a uma rotina normal."
    show debbie 1
    show player 14
    player_name "Eu acho."
    player_name "O que você está fazendo hoje?"
    show player 13
    show debbie 13
    deb "Oh eu?"
    deb "Trabalho doméstico principalmente. Isso me mantém bem ocupado."
    deb "Não é fácil cuidar desse grande lugar sozinha."
    show debbie 14b
    show player 5
    pause
    show player 2
    player_name "Eu poderia ajudar."
    show player 1
    show debbie 13
    deb "Você quer ajudar com o trabalho da casa?"
    show debbie 1
    show player 29 with dissolve
    player_name "Certo! Quero dizer, eu sinto que devo puxar meu próprio peso por aqui..."
    show player 1 with dissolve
    show debbie 2
    deb "Essa é uma ótima atitude para ter, {b}[firstname]{/b}!"
    show debbie 1
    deb "Hmm..."
    show debbie 2
    deb "Bem, o gramado não foi cortado em semanas."
    deb "Você pode começar por aí, se quiser!"
    deb "O {b}cortador de grama{/b} deve estar na {b}garagem{/b}."
    show debbie 1
    show player 14
    player_name "Tudo certo. Eu vou dar uma olhada."
    show player 13
    show debbie 2
    deb "Obrigada, {b}[firstname]{/b}."
    deb "Seja cuidadoso!"
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_clothes_dirty:
    scene expression L_home_entrance.background
    show player 11 zorder 1 at left
    show xtra 15 zorder 2 at Position(xpos=170,ypos=754)
    show jenny f_gross_talk
    with dissolve
    jen "Ei, o que é esse cheiro?!"
    show player 14
    show jenny f_gross
    player_name "... Eu acho. Eu estava la fora cortando a grama."
    show player 11
    show jenny f_gross_talk
    jen "Isso é nojento! Você está coberto de grama em todos os lugares, seu idiota!"
    show player 12
    show jenny f_gross
    player_name "Eu sinto Muito. Eu estava apenas tentando ajudar {b}[deb_name]{/b}."
    show player 11
    show jenny f_upset_talk
    jen "Então, o que, você vai começar a fazer tarefas por aqui agora?"
    show jenny f_grin_talk a_dressed_crossed with dissolve
    jen "Você tem uma queda por {b}[deb_name]{/b} ou alguma coisa?"
    show player 10
    show jenny f_grin
    player_name "Não! Eu sou apenas-"
    show player 11
    show jenny f_eyeroll
    jen "Pfft, não se faça de idiota! Eu vejo o que você está fazendo!"
    hide jenny with dissolve
    pause
    show player 12
    player_name "Qual é o problema dela?"
    show player 10
    player_name "Oh bem, eu deveria pegar essas roupas {b}no térreo para a lavagem{/b}."
    hide player with dissolve
    return

label entrance_mom_debt_collectors:
    scene henchman_cs1 2 with fade
    show text "Eu estava esperando para ver {b}Erik{/b}, em vez disso eu vi um homem estranho...\nEle estava vestindo um terno todo preto, com um olhar severo que colocaria o treinador Bridget com vergonha." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    scene henchman_cs1 1
    show player 2 at left
    show henchman2 1 at right
    with dissolve
    player_name "Oi?"
    show henchman2 2
    show player 1
    henchman2 "Onde está o dono desta residência?"
    show henchman2 1
    show player 11
    player_name "..."
    show player 12
    player_name "Quem está perguntando?"
    show player 11
    show henchman2 3
    henchman2 "É assunto pessoal, garoto."
    show henchman2 1
    show player 12
    player_name "Bem, ela está meio ocupada no momento, então por que você não vem outra hora?"
    show henchman2 2
    show player 11
    henchman2 "Não há necessidade. Apenas dê a ela esta mensagem."
    show henchman2 3
    henchman2 "Ela está ficando sem tempo. É melhor ela pagar ou então!"
    henchman2 "Meu chefe não é do tipo paciente."
    show henchman2 1
    show player 11
    player_name "..."
    show player 12
    player_name "Ou então, o que?"
    show player 11
    show henchman2 3
    henchman2 "Apenas dê a ela a mensagem, garoto."
    henchman2 "Voltaremos em breve..."
    show henchman2 1
    player_name "..."
    $ playMusic()
    hide henchman2
    with dissolve
    scene expression L_home_entrance.background
    show player 10 at left
    with fade
    player_name "( O que foi isso {b}tudo{/b}sobre... )"
    show player 5
    show debbie 62 at right with dissolve
    deb "Alguém estava na porta, querido?"
    show player 10
    show debbie 61
    player_name "Sim, um cara estranho de terno preto veio..."
    show player 5
    show debbie 59
    deb "!!!"
    show player 11
    show debbie 60
    deb "...O que ele queria?"
    show debbie 59
    show player 10
    player_name "Ele disse que você precisa pagar e que ele estará de volta em breve, mas se recusou a dizer por que."
    show player 11
    show debbie 60
    deb "Deve ser sobre..."
    deb "Mas eu já paguei tudo"
    show debbie 59
    deb "..."
    show player 10
    player_name "O que é isso?"
    show player 11
    show debbie 60
    deb "Não é nada, querido."
    show player 1
    show debbie 62
    deb "Eles devem ter obtido o endereço errado, é tudo."
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_pipe_help:
    scene expression L_home_entrance.background
    show player 11 at left
    show debbie 13 at right
    with dissolve
    deb "Querida! Graças a Deus você está aqui!"
    show debbie 14b
    show player 10
    player_name "{b}[deb_name]{/b}?"
    show player 5
    show debbie 13
    deb "{b}[jen_name]{/b} e eu preciso da sua ajuda."
    show debbie 14b
    show player 12
    player_name "Hã?"
    show player 5
    show debbie 13
    deb "Há um cano quebrado no andar de cima e água em todos os lugares!"
    deb "Ela está lá em cima mexendo com isso agora."
    deb "Você poderia ir e ajudá-la?"
    show debbie 14b
    show player 10
    player_name "Eu? Eu err..."
    show player 5
    show debbie 13
    deb "Eu não posso me dar ao luxo de ligar para um reparador agora. Não com tudo o que aconteceu recentemente..."
    show debbie 14b
    show player 10
    player_name "Oh, certo..."
    show player 14
    player_name "Vou dar uma olhada."
    show player 13
    show debbie 2
    deb "Obrigado querido! Deixe-me saber se há algo que eu possa fazer para ajudar."
    show debbie 1
    show player 14
    player_name "Tudo bem."
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_movie_night:
    scene location_home_entrance_night_blur
    show player 1 at left
    show debbie 62 at right
    deb "Oh, ei, querido!"
    deb "Indo para a cama?"
    show player 2
    show debbie 61
    player_name "Não, só procurando por algo para fazer..."
    show player 14
    player_name "Por que, o que você está fazendo?"
    show player 1
    show debbie 62
    deb "Eu estava pensando em começar um filme."
    show player 2
    show debbie 61
    player_name "Legal."
    show player 1
    deb "..."
    show debbie 63
    deb "Por que você não vem se juntar a mim?"
    show player 10
    show debbie 61
    player_name "Really?"
    show player 11
    show debbie 62
    deb "Claro, por que não? Ainda é cedo e eu adoraria a companhia!"
    show player 2
    show debbie 61
    player_name "Sim, ok. Isso parece legal, {b}[deb_name]{/b}."
    show player 1
    show debbie 62
    deb "Ótimo!"
    deb "Vou me sentar e você vem se juntar a mim quando estiver pronta, certo?"
    show player 2
    show debbie 61
    player_name "Parece bom!"
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_hang_out:
    scene location_home_entrance_day_blur
    show player 1 at left with dissolve
    show debbie 165 at right with dissolve
    deb "Ei, querido!"
    show player 2
    show debbie 164
    player_name "Ei {b}[deb_name]{/b}!"
    player_name "Você está bonita! Indo para algum lugar?"
    show player 1
    show debbie 165
    deb "Eu só preciso correr para o {b}shop{/b} e pegar algumas coisas."
    show debbie 164
    deb "..."
    show debbie 165
    deb "Você gostaria de se juntar a mim?"
    show player 11
    show debbie 164
    player_name "Hmm?"
    show player 10
    player_name "Oh eu não sei, eu ia"
    show player 11
    show debbie 165
    deb "A, vamos! Vai te fazer bem tomar um pouco de ar fresco."
    show debbie 164
    player_name "..."
    show debbie 165
    deb "... E além disso, eu não quero ir sozinha..."
    deb "Você vem e me faz companhia??"
    show debbie 164
    return

label entrance_mom_hang_out_yes:
    show player 2
    player_name "Heh, sheesh {b}[deb_name]{/b}! Tudo bem, eu vou."
    show player 1
    show debbie 166
    deb "Legal!"
    show debbie 165
    deb "Eu vou te encontrar no carro então, querido!"
    return

label entrance_mom_hang_out_no:
    show player 10
    player_name "Desculpa {b}[deb_name]{/b}, Eu tenho outra coisa planejada para hoje..."
    show player 11
    show debbie 168
    deb "Oh."
    show debbie 169
    deb "..."
    show debbie 168
    deb "Ok, querido, bem ... Apenas fique em segurança e vá para casa para o jantar."
    show player 2
    show debbie 169
    player_name "Coisa certa."
    return

label entrance_mom_spy:
    scene expression L_home_entrance.background
    show player 10 with dissolve
    player_name "Hã?"
    player_name "O que foi aquele barulho?"
    show player 11
    pause
    show player 10
    player_name "Talvez a TV esteja ligada na sala de estar."
    hide player with dissolve
    return

label entrance_mom_kissing_practice:
    scene expression L_home_entrance.background
    show player 4 with dissolve
    player_name "Eu me pergunto se {b}[deb_name]{/b} deixaria eu beijá-la novamente se eu perguntasse?"
    player_name "eu deveria {b}falar com ela{/b} sobre isso..."
    hide player with dissolve
    return

label entrance_mom_car_broken:
    scene expression L_home_entrance.background
    show debbie 3 at right
    show player 1 at left
    with dissolve
    deb "Bom dia, querido."
    show debbie 1
    show player 14
    player_name "Bom dia, {b}[deb_name]{/b}."
    show player 13
    show debbie 2
    deb "Você dormiu bem noite passada?"
    show debbie 1
    show player 10
    player_name "...Sim ... meio."
    player_name "Eu tenho tido muitos sonhos estranhos ultimamente."
    show player 11
    show debbie 2
    deb "É assim mesmo? Que tipo de sonhos estranhos?"
    show debbie 1
    show player 10
    player_name "Oh, umm..."
    player_name "Bem, é meio embaraçoso."
    show player 11
    show debbie 2
    deb "... Sonhos impertinentes?"
    show debbie 1
    show player 10
    player_name "Err... Sim."
    show player 11
    show debbie 2
    deb "Bem, isso não é nada para se envergonhar, querido!"
    show debbie 3
    deb "Você está nessa idade depois de tudo."
    show debbie 1
    pause
    show debbie 2
    deb "Então, quem é a garota de sorte?"
    show player 10
    show debbie 1
    player_name "A garota?"
    player_name "Umm, Eu realmente não quero falar sobre isso..."
    show player 11
    show debbie 3
    deb "Hehe, Oh Eu me pergunto se é alguém que eu conheço?"
    show player 11
    player_name "..."
    show debbie 3
    deb "Tudo bem. Guarde seus segredos!"
    show debbie 2
    deb "Enquanto estiver aqui, preciso da sua ajuda com alguma coisa. Tem um minuto?"
    show debbie 14
    show player 10
    player_name "Sim ... O que é isso?"
    show player 1
    show debbie 13
    deb "Você pode olhar o carro e ver por que ele não está pegando?"
    show debbie 1
    show player 10
    player_name "Nós não acabamos de consertar no outro dia?"
    show player 1
    show debbie 13
    deb "Sim, mas por alguma razão ele não que da partida!"
    show debbie 1
    show player 2
    player_name "Você não deixou as luzes acesas e matou a bateria novamente, não é?"
    show debbie 2
    show player 1
    deb "Hah, não ... quero dizer, bem ... eu acho que não. Você se importaria de verificar?"
    show debbie 1
    show player 14
    player_name "De modo nenhum!"
    hide player
    hide debbie
    with dissolve
    return

label entrance_mom_panties_masturbation_again:
    scene expression L_home_entrance.background
    show player 1
    player_name "( Eu não posso acreditar {b}[deb_name]{/b} realmente esfregou meu pau! )"
    player_name "( ... mais alguns segundos e eu teria aparecido. )"
    player_name "( Arrgh, eu a quero tanto! Isso é tortura! )"
    show player 11
    player_name "( .... )"
    player_name "( Hmm, Eu sei que prometi não me masturbar no quarto dela, mas... )"
    show player 13
    player_name "( Apenas me senti tão bem na última vez! )"
    player_name "( ... )"
    player_name "( Talvez se eu fizer isso rápido e silenciosamente, eu posso pegar um par de calcinha e quebrar uma porca sem que ela perceba. )"
    player_name "( Ela parece estar {b}ocupada [temp]{/b} o que deveria me permitir entrar em seu quarto e esfregar em sua cama. )"
    player_name "( Eu acho que vale a pena um tiro ... Eu preciso do lançamento ... Para limpar a minha cabeça! )"
    hide player with dissolve
    return

label entrance_mom_diane_visit:
    scene expression L_home_entrance.background
    show player 34 with dissolve
    player_name "...{b}*voz distante*{/b}..."
    show player 35
    player_name "( Hmm, parece {b}[deb_name]{/b} está falando com alguém na cozinha... )"
    show player 12
    player_name "( Eu me pergunto quem está aqui? )"
    show player 10
    player_name "( Eu deveria ir dar uma olhada... )"
    hide player with dissolve
    return

label entrance_mom_vacuum:
    scene location_home_entrance_fight
    show debbie 94 at right with dissolve
    pause
    show debbie 95
    pause
    show debbie 94
    pause
    show debbie 95
    pause
    show debbie 94
    show player 1 at left with dissolve
    pause
    show debbie 95
    pause
    show debbie 97 with dissolve
    deb "Oh!!"
    deb "Você me assustou..."
    show debbie 98
    show player 17
    player_name "Desculpa, {b}[deb_name]{/b}."
    show player 14
    player_name "Eu não queria!"
    show debbie 97
    show player 1
    deb "Desculpe pelo barulho."
    deb "Eu deveria acabar logo com o aspirador."
    deb "... Ugh, isso está matando minhas costas!"
    show debbie 98
    return

label entrance_mom_vacuum_yes:
    show debbie 98 at right
    show player 14 at left
    player_name "Aqui, {b}[deb_name]{/b}, passa-me o aspirador."
    show player 1
    show debbie 96
    deb "..."
    show debbie 97
    deb "Você quer o aspirador?"
    show debbie 96
    show player 14
    player_name "Sim, vou assumir daqui."
    player_name "Você deve descansar as costas um pouco..."
    show player 10
    player_name "Não faz sentido trabalhar tanto quando estou aqui para ajudar."
    show debbie 97
    show player 11
    deb "Não, tudo bem querido. Você não tem que ajudar"
    show debbie 98
    show player 10
    player_name "Eu sei que não tenho que ajudar, {b}[deb_name]{/b}."
    player_name "Eu quero fazer isso."
    show debbie 97
    show player 1
    deb "Bem, se você insiste..."
    show player 257
    show debbie 100
    with dissolve
    deb "Isso é muito gentil de sua parte."
    show player 259
    show debbie 99
    player_name "Não é um problema!"
    hide player
    hide debbie
    with dissolve
    scene expression "backgrounds/location_home_cutscene02.jpg"
    show expression FilteredText("eu me senti mal {b}[deb_name]{/b} estava tendo um tempo difícil com a dor nas costas. \nO mínimo que eu poderia fazer era ajudá-la, mesmo que me levasse uma eternidade para terminar. \nAs escadas eram a pior parte! Não é de admirar que suas costas estejam machucando... \nFinalmente {b}[deb_name]{/b} manteve-me companhia enquanto eu trabalhava.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    return

label entrance_mom_vacuum_no:
    show debbie 96 at right
    show player 10 at left
    player_name "Você pode por favor terminar de limpar outra hora?"
    player_name "Eu estou tentando estudar lá em cima e todo esse barulho está me distraindo."
    show debbie 97
    show player 11
    deb "Me desculpe, querido!"
    deb "Eu não tinha ideia de que você estava no andar de cima estudando."
    show debbie 96
    show player 14
    player_name "Está bem, {b}[deb_name]{/b}."
    show debbie 97
    show player 1
    deb "Vai ser bom descansar um pouco minhas costas..."
    show debbie 96
    show player 17
    player_name "Obrigado!"
    hide player
    hide debbie
    with dissolve
    return

label entrance_sis_couch_1:
    scene expression L_home_entrance.background
    show player 11 with dissolve
    player_name "( Que som é esse? )"
    player_name "( Parece que a TV está ligada. )"
    show player 4 at Position(xpos=518)
    player_name "( Quem poderia estar assistindo TV tão tarde? )"
    hide player with dissolve
    return

label entrance_sis_couch_2:
    scene expression L_home_entrance.background
    show player 26 with dissolve
    player_name "( Que porno {b}[jen_name]{/b} estava assistindo estava excitante! Eu meio que sinto vontade de assistir também... )"
    show player 33
    player_name "Hmm... Talvez {b}outra noite{/b}."
    hide player with dissolve
    return

label entrance_sis_couch_3:
    scene expression L_home_entrance.background
    show player 11 with dissolve
    player_name "( O que foi esse som? )"
    hide player with dissolve
    return

label entrance_bissette_roxxy_jenny_mentoring:
    scene expression L_home_entrance.background
    show player 13 at Position (xpos=300)
    show debbie 2 at right
    with dissolve
    deb "Querido, alguém está na porta! Você pode pegar isso?"
    show debbie 1
    show player 14
    player_name "Coisa certa, {b}[deb_name]{/b}!"
    show player 10
    show roxxy 1 at Position (xpos=600) with dissolve
    player_name "Ei {b}Roxxy{/b}! Você está aqui para a sua sessão com {b}[jen_name]{/b}?"
    show player 5
    show roxxy 2
    rox "O que você acha que eu estou aqui para ver você ou algo assim?!"
    show roxxy 1
    show player 21
    player_name "... Não."
    show player 5
    show roxxy 2
    rox "Bom, porque não tem jeito"
    show roxxy 1 with None
    show jenny f_grin a_dressed_crossed at flip
    show jenny at Position (xpos=-120)
    with dissolve
    jen "*Ahem*"
    show jenny f_grin_talk
    jen "É essa garota que você queria que eu ajudasse?"
    jen "Você sabe, aquela que você está tentando transar?"
    show jenny f_grin
    hide xtra
    show player 11
    with dissolve
    show debbie 14
    player_name "!!!" with hpunch
    show roxxy 3
    rox "COM LICENÇA!?"
    show roxxy 14
    show player 113
    player_name "Não!!"
    show player 10
    player_name "{b}Roxxy{/b}, Eu juro que nunca disse"
    show player 11
    show roxxy 2
    rox "Como se você tivesse um tiro ... Nem mesmo em seus sonhos, imbecil!"
    show roxxy 1
    show player 37 at Position (xoffset=41) with dissolve
    show jenny f_grin_talk
    jen "Aww, pervertido muito ruim."
    jen "Eu acho que você está preso com a mão e uma garrafa de loção."
    show jenny f_grin
    show roxxy 4
    rox "Hah! Sim, e sinto muito pela loção..."
    show roxxy 1
    show jenny f_laugh a_dressed_hips with dissolve
    jen "Hahaha! Eu gosto de você! {b}Roxxy{/b} foi isso?"
    show jenny f_grin
    show roxxy 1b
    rox "E você é {b}[jen_name]{/b}?"
    show roxxy 1
    show jenny f_grin_talk
    jen "Está certo."
    jen "Vamos lá, {b}Roxxy{/b}. Nós podemos deixar o dweeb e começar no meu quarto."
    show jenny f_grin
    show roxxy 1b
    rox "Alegremente."
    show roxxy 2
    rox "Até mais, dweeb!"
    hide roxxy
    hide jenny
    show player 25
    with dissolve
    player_name "..."
    show player 24
    player_name "Tenho um mau pressentimento sobre isso."
    hide player
    hide debbie
    with dissolve

    scene location_home_entrance_cutscene04
    with fade
    show text "Aquelas duas tinham formado uma conexão quase que instantaneamente...\neu acho {b}[jen_name]{/b} e {b}Roxxy{/b} tem muito em comum." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    show text "Ambos eram capitães do esquadrão de torcida, populares, lindos,\ne ambos tinham dominado a arte de ser uma cadela..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    show text "Eu realmente espero que eu não acabe me arrependendo..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    with dissolve

    scene expression L_home_entrance.background
    show player 24 at Position (xpos=300)
    show debbie 13 at right
    with dissolve
    deb "Who was that?"
    show debbie 14
    show player 10
    player_name "Just a girl from my school. {b}[jen_name]{/b} agreed to help her with some cheer-leading stuff."
    show player 5
    show debbie 13
    deb "{b}[jen_name]{/b} está ajudando alguém?"
    show debbie 3
    deb "Isso é novo."
    show debbie 1
    show player 12
    player_name "Porque paguei ela..."
    show player 90
    show debbie 13
    deb "Ah."
    deb "Querido, você realmente não deveria deixar {b}[jen_name]{/b} tirar proveito de você assim..."
    show debbie 14
    show player 12
    player_name "Sim, eu sei."
    show player 90
    player_name "..."
    show debbie 13
    deb "Algo mais em sua mente?"
    show debbie 14
    show player 12
    player_name "Eu nunca vi {b}[jen_name]{/b} ficar tão proxima de alguém assim..."
    show player 10
    player_name "Meio que me assusta, para ser honesto."
    show player 5
    show debbie 2
    deb "Bem, acho que é bom que ela seja uma nova amiga."
    deb "Eu me preocupo com ela sentada no andar de cima sozinha o dia todo..."
    show debbie 13
    deb "Tenho certeza que ela fica sozinha."
    show debbie 14
    show player 10
    player_name "eu duvido."
    show player 5
    player_name "..."
    show player 11
    jen "Hahahaha!!"
    show player 10
    player_name "...{b}Talvez eu devesse ir verificá-los{/b}?"
    show player 5
    show debbie 2
    deb "Talvez."
    show debbie 13
    deb "...Apenas tenha cuidado, docinho."
    hide player
    hide debbie
    with dissolve
    return

label entrance_bissette_roxxy_jenny_mentoring_sex:
    scene expression L_home_entrance.background
    show player 13 at Position (xpos=300)
    show debbie 2 at right
    with dissolve
    deb "Querido, alguém está na porta! Você pode pegar isso?"
    show debbie 1
    show player 14
    player_name "Coisa certa, {b}[deb_name]{/b}!"
    show player 10
    show roxxy 1 at Position (xpos=600) with dissolve
    player_name "Ei {b}Roxxy{/b}! Você está aqui para a sua sessão com {b}[jen_name]{/b}?"
    show player 5
    show roxxy 2
    rox "Sim. ela està em casa, certo?"
    show roxxy 1
    show player 21
    player_name "absolutamente."
    show player 5
    show roxxy 2
    rox "Impressionante! Estou tão animada"
    show roxxy 1 with None
    show jenny f_grin a_dressed_crossed at flip
    show jenny at Position (xpos=-120)
    with dissolve
    jen "*Ahem*"
    show jenny f_grin_talk
    jen "É essa garota que você queria que eu ajudasse?"
    jen "Você sabe, aquele que você está tentando transar?"
    show jenny f_grin
    hide xtra
    show player 11
    with dissolve
    show debbie 14
    player_name "!!!" with hpunch
    show roxxy 4
    rox "... Hahaha!"
    show roxxy 14
    show player 113
    player_name "Eu não"
    show player 10
    player_name "{b}Roxxy{/b}, Eu juro que nunca disse"
    show player 11
    show roxxy 1h
    rox "O que exatamente você tem dito a elas?, {b}[firstname]{/b}?"
    show roxxy 1
    show player 37 at Position (xoffset=41) with dissolve
    show jenny f_surprised
    jen "Espere um segundo..."
    jen "Você quer dizer, você ... e ele?!"
    show jenny f_sad
    show roxxy 4
    rox "Uhh Sim?!"
    rox "Contanto que ele continue cuidando bem de mim..."
    show jenny f_grin
    rox "... E não engorda nem perde o cabelo!"
    show roxxy 1
    show jenny f_laugh
    jen "Hahaha! Eu gosto de você! {b}Roxxy{/b} foi isso?"
    show jenny f_grin
    show roxxy 1b
    rox "E você é {b}[jen_name]{/b}?"
    show roxxy 1
    show jenny f_grin_talk
    jen "Está certo."
    jen "Vamos lá, {b}Roxxy{/b}. Nós vamos fazer isso no meu quarto."
    show jenny f_grin
    show roxxy 1b
    rox "Tudo bem."
    show roxxy 2
    rox "obrigado novamente, {b}[firstname]{/b}."
    hide roxxy
    hide jenny
    show player 25
    with dissolve
    player_name "..."
    show player 24
    player_name "Tenho um mau pressentimento sobre isso."
    hide player
    hide debbie
    with dissolve
    scene expression L_home_entrance.background
    show player 24 at Position (xpos=300)
    show debbie 13 at right
    with dissolve
    deb "Então vocês dois estão namorando agora?"
    show debbie 14
    show player 10
    player_name "Sim. {b}[jen_name]{/b} concordou em ajudá-la com alguma coisa de líder de torcida."
    show player 5
    show debbie 13
    deb "{b}[jen_name]{/b} está ajudando alguém?"
    show debbie 3
    deb "Isso é novo."
    show debbie 1
    show player 12
    player_name "Porque paguei a ela..."
    show player 90
    show debbie 13
    deb "Ah."
    deb "QueridO, você realmente não deveria deixar {b}[jen_name]{/b} tirar proveito de você assim..."
    show debbie 14
    show player 12
    player_name "Sim, eu sei."
    show player 90
    player_name "..."
    show debbie 13
    deb "Algo mais em sua mente?"
    show debbie 14
    show player 12
    player_name "Eu nunca vi{b}[jen_name]{/b} se aproximar de alguém assim..."
    show player 10
    player_name "Meio que me assusta, para ser honesto."
    show player 5
    show debbie 2
    deb "Bem, acho que é bom que ela seja uma nova amiga."
    deb "Eu me preocupo com ela sentada no andar de cima sozinha o dia todo..."
    show debbie 13
    deb "Tenho certeza que ela fica sozinha."
    show debbie 14
    show player 10
    player_name "eu duvido."
    show player 5
    player_name "..."
    show player 11
    jen "Hahahaha!!"
    show player 10
    player_name "...{b}Talvez eu devesse ir verificá-los{/b}?"
    show player 5
    show debbie 2
    deb "Talvez."
    show debbie 13
    deb "...Apenas tenha cuidado, querido."
    hide player
    hide debbie
    with dissolve
    return

label entrance_bissette_roxxy_jenny_spying:
    scene expression L_home_entrance.background
    show player 10 with dissolve
    player_name "Eu deveria ir verificar {b}Roxxy{/b} e {b}[jen_name]{/b}..."
    hide player with dissolve
    return

label entrance_diane_debbie_evening_visit_overhear:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 34 with dissolve
    player_name "( Hmm? )"
    player_name "( É {b}Diane{/b}? )"
    player_name "( {b}[deb_name]{/b} deve tê-la convidado. )"
    player_name "( {b}Eu me pergunto o que elas estão falando?{/b} )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
