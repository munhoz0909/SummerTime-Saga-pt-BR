label ross_office_first_visit:
    scene school_office3_b with fade
    show player 11 with dissolve
    player_name "*Cheirar*"
    show player 12
    player_name "Que cheiro é esse?"
    player_name "É como ... incenso ... e ervas..."
    player_name "{b}Miss Ross{/b} deve estar ficando muito tempo aqui."
    hide player with dissolve
    return

label ross_hscene_start:
    $ M_ross.set ("sex speed", 0.15)
    if M_ross.is_state(S_ross_paint_with_body):
        call expression game.dialog_select("ross_office_hscene")
        call expression game.dialog_select("ross_hscene_first_time")
    else:
        $ persistent.cookie_jar["Ross"]["gallery"]["02_unlocked"] = True
        scene location_school_office3_closeup_sex
        show rosss 1 at right
        with dissolve
    $ animated = False
    jump ross_hscene_loop

label ross_office_hscene:
    scene expression player.location.background_closeup
    show ross 13 at Position(xpos=0.35, ypos=1.0)
    show player 1f at Position(xpos=0.85, ypos=1.0)
    with dissolve
    ross "Aqui está meu pequeno herói!"
    show ross 12
    show player 2f
    player_name "Uau, cheira muito bem aqui!"
    show ross 13
    show player 1f
    ross "Você gosta disso? É o meu incenso favorito."
    ross "Realmente melhora o humor, você não acha?"
    show ross 12
    show player 10f
    player_name "Uhh, Certo. eu acho..."
    player_name "O que há com a tela gigante?"
    show player 11f
    show ross 13
    ross "Hehe, paciência, {b}[firstname]{/b}. Você não pode se apressar ou a arte sofrerá."
    show player 10f
    show ross 12
    player_name "... Oh, ok."
    show player 11f
    show ross 13
    ross "Por que você não trava a porta? Não queremos que ninguém nos perturbe..."
    show player 2f
    show ross 12
    player_name "Tudo bem."
    hide player with dissolve
    pause
    show ross 14 at Position(xpos=0.37, ypos=1.0) with dissolve
    pause
    show player 2f at Position(xpos=0.85, ypos=1.0)
    show ross 15 at Position(xpos=0.37, ypos=1.0)
    with dissolve
    player_name "... Okay agora "
    show ross 16 at Position(xpos=0.35, ypos=1.0)
    show player 11f
    with dissolve
    pause
    show player 10f
    show ross 17 at Position(xpos=0.34, ypos=1.0) with dissolve
    player_name "... Eh?"
    show ross 37 at Position(xpos=0.36, ypos=1.0) with dissolve
    player_name "O que você está fazendo, {b}Miss Ross{/b}?"
    show player 11f
    show ross 36
    ross "Oh, você vai precisar se despir também..."
    ross "... Nós vamos usar nossos corpos para pintar, {b}[firstname]{/b}."
    show ross 37
    show player 10f
    player_name "... Nossos corpos?"
    hide ross
    show rossp 9 at Position(xpos=0.34, ypos=1.0)
    with dissolve
    show player 11f
    player_name "( !!! )" with hpunch
    show rossp 10
    ross "Está certo!"
    ross "Não seja tímido agora..."
    ross "Perca essas roupas!"
    show rossp 9
    show player 10f
    player_name "... ok."
    show player 8f with dissolve
    pause
    show player 261 with dissolve
    pause
    show player 430f with dissolve
    show rossp 10
    ross "Maravilhoso!"
    ross "Você é um jovem tão talentoso, {b}[firstname]{/b}..."
    show player 430bf
    show rossp 9
    player_name "Hehe, Obrigado."
    show player 430f
    ross "Mmmhmm."
    show rossp 10
    ross "Ok, para o próximo passo..."
    ross "Nós vamos precisar adicionar um pouco de tinta para a equação..."
    show rossp 9
    show player 430bf
    player_name "Não tenho certeza..."
    hide ross
    show rossp 6 at Position(xpos=0.46, ypos=1.0)
    with dissolve
    show player 430f
    ross "Aqui pegue isso."
    show rossp 9 at Position(xpos=0.34, ypos=1.0)
    show player 613 at Position(xpos=0.83, ypos=1.0)
    with dissolve
    pause
    show player 614
    player_name "...O que eu estou pintando exatamente?"
    hide ross
    show rossp 1 at Position(xpos=0.41, ypos=1.0)
    with dissolve
    show player 613
    ross "Hehe, seu bobo!"
    ross "Não se preocupe, eu vou te mostrar."
    show rossp 2
    pause
    hide rossp
    hide player
    with dissolve
    scene black with fade
    ross "É isso aí, {b}[firstname]{/b}..."
    ross "Apenas enlouqueça com isso!"
    player_name "..."
    ross "Hehe, isso faz cócegas!"
    scene expression player.location.background_closeup with fade
    show ross 48 zorder 0 at Position(xpos=0.43, ypos=1.0)
    show rosso 1 zorder 1 at Position(xpos=0.43, ypos=0.99)
    show player 616 zorder 2 at Position(xpos=0.73, ypos=1.0)
    with dissolve


    pause
    show player 615 at Position(xpos=0.745, ypos=1.0) with dissolve
    show ross 47
    ross "Bem feito, {b}[firstname]{/b}!"
    ross "Oh, Eu realmente amo essa técnica!"
    hide rosso
    hide ross
    show rossp 3_4_5_4 at Position(xpos=0.43, ypos=1.0)
    with dissolve
    pause
    hide rossp
    show ross 47 zorder 0 at Position(xpos=0.43, ypos=1.0)
    show rosso 1 zorder 1 at Position(xpos=0.43, ypos=0.99)
    with dissolve
    ross "... Isso é tão incrível!"
    hide ross
    hide rosso
    show rossp 3_4_5_4 at Position(xpos=0.43, ypos=1.0)
    show player 432f at Position(xpos=0.855, ypos=1.0)
    with dissolve
    player_name "Onde você aprendeu isso de qualquer maneira?"
    show rossp 10 zorder 0 at Position(xpos=0.4, ypos=1.0)
    show rosso 1 zorder 1 at Position(xpos=0.42, ypos=0.99)
    with dissolve
    show player 431f
    ross "Oh, é apenas algo que eu inventei há muito tempo."
    ross "Meu primeiro ano de ensino, na verdade."
    show rossp 9
    show player 432f
    player_name "Mesmo?"
    show player 431f
    ross "Mmmhmm..."
    show rossp 10
    ross "... Mas ainda não chegamos à melhor parte."
    show rossp 9
    show player 432f
    player_name "... Qual é a melhor parte?"
    show rossp 10
    show player 431f
    ross "Eu quero que você faça amor comigo, {b}[firstname]{/b}!"
    show player 430f
    player_name "( !!! )" with hpunch
    show player 430bf
    show rossp 9
    player_name "O que?!"
    show player 430f
    show rossp 10
    ross "Faça amor comigo! Bem aqui nesta tela!"
    ross "Use meu corpo para pintar sua obra-prima!"
    show player 430bf
    show rossp 9
    player_name "Você realmente quer ... comigo?"
    hide player
    hide rosso
    show rossp 11_12 at Position(xpos=0.785, ypos=1.0)
    with dissolve
    ross "Claro que eu quero!"
    ross "Eu quero esse seu pau grande dentro de mim, desde o momento em que vi aquela girafa bonitinha que você fez de barro."
    player_name "... Você gostou?"
    ross "Oh, Sim!"
    ross "Nada me excita mais do que um jovem artista talentoso!"
    player_name "... Isso é muito bom."
    ross "Está prestes a se sentir muito melhor!"
    ross "Venha deitar."
    return

label ross_hscene_first_time:
    scene location_school_office3_closeup_sex
    show rosss 1 at right
    with dissolve
    ross "Oh, Não acredito que finalmente está acontecendo!"
    ross "..."
    show rosss 2 with dissolve
    ross "Oooh, Uau!"
    $ M_ross.set ("sex speed", 0.2)
    show expression AnimatedImage("rosss", [2,3,4,5,6,7,8,9,10,11], M_ross) as rosss at right
    pause 3
    ross "Oh Minha deusa! É ainda melhor do que eu imaginava!"
    pause 2
    player_name "Oh, {b}Miss Ross{/b}!"
    $ M_ross.set ("sex speed", 0.1)
    pause 5
    ross "Nunca me senti tão bem!"
    pause 5
    ross "Isto é incrível!"
    pause 2
    player_name "Ahhh!"
    pause 2
    ross "Por que isso é tão bom?!"
    $ M_ross.set ("sex speed", 0.06)
    pause 5
    ross "Oh, me foda!"
    player_name "Eu não posso-"
    player_name "Você está indo rápido demais!"
    pause 5
    ross "Eu amo seu pau {b}[firstname]{/b}!"
    pause 2
    ross "Oh, eu amo tanto isso!"
    return

label ross_hscene_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("rosss", [2,3,4,5,6,7,8,9,10,11], M_ross) as rosss at right
                $ animated = True
            pause 1
            if animcounter in [1,3]:
                call expression game.dialog_select("ross_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [2,3,4,5,6,7,8,9,10,11]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "rosss {}".format(pose_list[pose_counter]) as rosss at right
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("ross_hscene_dialog")
        $ animcounter += 1
    call screen ross_sex_options

label ross_hscene_dialog:
    if M_ross.is_state(S_ross_paint_with_body):
        $ temp = choice_randomizer([(1, 1), (2, 2), (3, 1)])
    else:
        $ temp = choice_randomizer([(1, 1), (2, 2), (3, 2), (4, 1)])

    if temp == 1:
        if M_ross.is_state(S_ross_paint_with_body):
            ross "Oh Minha deusa! É ainda melhor do que eu imaginava!"
            player_name "Oh, {b}Miss Ross{/b}!"
        else:

            ross "Oh, Estou tão feliz que você veio hoje!"
            ross "Eu realmente precisava disso!"
            player_name "Oh,isso é tão bom!"
            ross "Mmm, Eu amo tanto esse pau!"
            ross "Me dê isto, {b}[firstname]{/b}!"
            ross "É isso aí!"
            ross "AAAHHH!"

    elif temp == 2:
        if M_ross.is_state(S_ross_paint_with_body):
            ross "Nunca me senti tão bem!"
            ross "Isto é incrível!"
            player_name "Ahhh!"
            ross "Por que isso é tão bom?!"
        else:

            ross "É isso aí, {b}[firstname]{/b}!"
            ross "Oh, isto é tao bonito!"
            ross "Eu quero que você venha para mim desta vez!"
            player_name "Oh, Uau!"
            player_name "Ahhh!!"
            ross "É isso aí!"
            ross "Pintar uma obra-prima branca na minha tela ovariana!"

    elif temp == 3:
        if M_ross.is_state(S_ross_paint_with_body):
            ross "Oh, Foda-me!"
            player_name "Eu não posso-"
            player_name "Você está indo rápido demais!"
            ross "Eu amo seu pau, {b}[firstname]{/b}!"
            ross "Oh, Eu amo tanto isso!"
        else:

            ross "Oh, Eu ainda estou um pouco dolorida da nossa última sessão..."
            player_name "Devemos parar?"
            ross "Não ouse parar!"
            ross "Oh, sim!"
            ross "Sim! Sim! Me foda!"
            ross "É tão bom, {b}[firstname]{/b}!"
            player_name "Oh, {b}Miss Ross{/b}!!!"

    elif temp == 4:
        ross "Eu estive pensando sobre isso o dia todo!"
        player_name "Você tem pensado?"
        ross "Sim..."
        ross "... O dia todo..."
        ross "... só pensando no seu pinto feliz..."
        ross "... E o quanto eu preciso dentro da minha vagina feliz!"
        player_name "..."
        ross "Oh, Eu vou gozar!"
        ross "OH PORRA!"
        ross "AAAHHHHH!!!"
    return

label ross_office_ross_sex_cum_dialogue:
    player_name "Não aguento mais não vou durar mais!"
    ross "Oh, Eu amo isso! Eu amo isso! eu amo isso!"
    pause
    ross "AAAhhhh!!!"
    pause
    show rosss 12_13 at right with flash
    player_name "HNNGGG!!!"
    ross "{b}*GASP*{/b}!"
    ross "Mmmph!"
    pause
    show rosss 14 with dissolve
    ross "Haaah... Haaah..."
    ross "Uau!"
    ross "... {b}[firstname]{/b}."
    ross "Isso foi..."
    show rosss 15 with dissolve
    pause
    show rosss 16 with dissolve

    ross "... Quero dizer, tive muito sexo na minha vida..."
    ross "... Muito sexo bom!"
    ross "... Mas isso foi outra coisa, foi incrivel!"
    player_name "... Sim."
    scene expression player.location.background_closeup
    show rossp 10 zorder 0 at Position(xpos=0.2, ypos=1.0)
    show rosso 1 zorder 1 at Position(xpos=0.22, ypos=1.0)
    show player 8f at right
    with dissolve
    ross "Precisamos fazer isso de novo!"
    show player 1f with dissolve
    ross "Eu nunca vi um pau tão duro como esse antes!"
    show rossp 9
    player_name "..."
    show rossp 10
    ross "Você não se importaria de fazer novamente algum dia, você faria {b}[firstname]{/b}?"
    show rossp 9
    show player 2f
    player_name "Claro que não!"
    player_name "Eu vou fazer isso quando quiser!"
    show rossp 10
    show player 1f
    ross "Hehe, bem, acho que é o suficiente por hoje..."
    ross "estou exausta..."
    show player 2f
    show rossp 9
    player_name "Sim eu também."
    show player 1f
    show rossp 10
    ross "Você vem, E me encontra no {b}meu escritório{/b} sempre que você precisar de outra \"lição privada.\" Ok?"
    show player 2f
    show rossp 9
    player_name "Hehe, sim, senhora!"
    return

label ross_office_ross_sex_cum:
    call expression game.dialog_select("ross_office_ross_sex_cum_dialogue")
    $ renpy.end_replay()
    $ game.timer.tick()
    $ M_ross.trigger(T_ross_sexual_body_painting)
    $ M_ross.set_default_locations([[L_school_artclassroom, L_school_rossoffice, L_school_rossoffice, L_NULL],
                                    [L_NULL, L_NULL, L_NULL, L_NULL]])
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
