label shower_jenny_pregnant:
    scene expression L_home_shower.background_blur
    show jenny b_towel a_magic_preggo_towel f_gross_down at flip
    show jenny at Position (xpos=500)
    show player f_flirt with dissolve
    pause 1
    show jenny f_gross_down_talk
    jen "{b}*Suspiro*{/b} eu nunca vou perdoá-lo por essa merda..."
    show player f_surprised_teeth a_dressed_surprised_up_both with dissolve
    jen "Aquele bastardo deveria estar esperando por mim!"
    show player at Position (xoffset=-100) with dissolve
    jen " Para todas as minhas necessidades!"
    hide player with dissolve
    jen "Esfregando meus pés..."
    scene expression L_home_hallway.background_blur
    show player f_worried with dissolve
    player_name "( Sim, eu provavelmente não deveria ir lá agora... )"
    hide player with dissolve
    return

label shower_jenny_peep:
    player_name "( Ela está ... se masturbando?! )"
    player_name "( Ah, isso é incrível! )"
    pause
    player_name "( Eu queria ficar, aqui e continuar assistindo... )"
    pause
    player_name "( É melhor eu ir antes que ela me veja. )"
    return

label shower_jenny_pissed_at_handjob:
    pause
    player_name "( Eu me pergunto se ela percebe que estou a observando? )"
    pause
    player_name "( Será que ela se importaria se eu me juntasse a ela? )"
    player_name "( Quero dizer, depois do que temos feito algumas coisas interessantes, tomar banho juntos não parece tão ruim... )"
    pause
    player_name "( Não, ela poderia surtar e me bater com seu secador Maldito. )"
    player_name "( Não vale a pena. )"
    return

label shower_jenny_blowjob_intro_repeat:
    player_name "( E há minha sugestão... )"
    menu:
        "Entrar.":
            call scene_shower_with_vfx
            show jenny f_sexy_talk b_shower a_naked_hips
            show player b_naked a_naked_sides f_normal od_naked_dick3
            with fade
            jen "É sobre a maldita hora!"
            jen "Eu não achei que você fosse se juntar a mim!"
            show jenny f_sexy
            show player f_normal_talk
            player_name "Bem, aqui estou eu..."
            show jenny f_grin_down a_shower_soap1 with dissolve
            player_name "Então, você."
            show player f_surprised
            show jenny a_shower_soap2 with dissolve
            pause
            show jenny a_shower_soap3 with dissolve
            pause
            show jenny f_grin b_shower_soaping a_empty with dissolve
            player_name "..."
            show jenny f_grin_talk
            jen "O que você estava dizendo?"
            show jenny f_grin
            show player f_worried_talk
            player_name "Eu estava dizendo alguma coisa?"
            show player f_worried
            show jenny f_laugh
            jen "Hahaha!"
            show jenny f_grin
            menu:
                "Boquete":

                    show jenny f_grin_talk
                    jen "Você quer se divertir um pouco?"
                    show jenny f_grin b_shower a_naked_hips with dissolve
                    show player f_normal_talk
                    player_name "Sim!"
                    show player f_normal
                    if M_jenny.get("dominance") <= 0:
                        show jenny f_grin_talk
                        jen "Bem, então você sabe o que vem a seguir..."
                        show jenny f_grin
                        show player f_worried_talk
                        player_name "Eu tenho que?"
                        show player f_worried
                        show jenny f_grin_talk
                        jen "Vamos, cãozinho..."
                        jen "Você tem que implorar pelo seu deleite!"
                        show jenny f_grin
                        show player f_worried_talk
                        player_name "{b}*Suspiro*{/b}"
                        jump bj_shower_repeat_sub
                    else:
                        show player f_skeptical_talk
                        player_name "E antes que você pergunte, eu não estou implorando!"
                        show player f_skeptical
                        show jenny f_upset_talk
                        jen "Sim Sim."
                        jen "Estou bem ciente disso."
                        show jenny f_upset
                        call scene_shower_with_vfx_zoom
                        show jenny_shower_bj_mc
                        show jenny_shower_bj pre_talk
                        with fade
                        jen "Apenas cale a boca e aproveite, idiota."
                        jump bj_shower_repeat_dom

                "Sexo" if M_jenny.finished_inclusive(S_jenny_end):

                    label jenny_shower_sex_intro_replay:
                    if store._in_replay is not None:
                        $ player.location = L_home_shower
                        call scene_shower_with_vfx
                        show jenny f_grin b_shower_soaping a_empty
                        show player b_naked a_naked_sides f_worried od_naked_dick3
                        with fade
                        pause
                    show jenny f_grin_talk b_shower a_naked_hips with dissolve
                    jen "Hmm, Eu acho que mereço um tratamento diferente hoje."
                    show jenny f_grin
                    show player f_worried_talk
                    player_name "O que você quer dizer?"
                    show player f_worried
                    show jenny f_grin_talk
                    jen "Quero dizer, você vai me foder."
                    show jenny f_grin
                    show player f_surprised
                    player_name "!!!"
                    show player f_normal_talk
                    player_name "OK, isso e ótimo!"
                    show player f_normal
                    show jenny b_shower_back a_shower_back_down f_shower_overshoulder_back_look_normal_talk o_shower_back_soap at Position (align=(0,0)) with dissolve
                    jen "Ah ah ah, não tão rápido!"
                    show player b_side_naked_forward a_side_naked_react f_side_shock_down od_empty zorder 0
                    show jenny b_shower_butt1 f_shower_butt1_talk a_empty o_empty zorder 1
                    with dissolve
                    jen "Você quer fazer isso?"
                    jen "Você tem que implorar por isso!"
                    show jenny b_shower_butt f_empty with dissolve
                    show player f_side_shy_down_talk
                    player_name "La vem ela, com essa conversa?!"
                    show player f_side_shy_down
                    show jenny b_shower_butt1 f_shower_butt1_talk with dissolve
                    jen "Vamos, perdedor."
                    jen "Implore sua princesa!"
                    show jenny b_shower_butt f_empty with dissolve
                    if M_jenny.get("dominance") <= 0:
                        show player f_side_shy_down_talk
                        player_name "{b}*Suspiro*{/b}"
                        player_name "Por favor, {b}Princesa [jen_name]{/b}..."
                        show player f_side_shy_down
                        show jenny b_shower_butt1 f_shower_butt1_talk with dissolve
                        jen "Por favor, o que?"
                        show jenny f_shower_butt1
                        show player f_side_shy_down_talk
                        player_name "Por favor, posso colocar meu pau dentro de você?"
                        show player f_side_shy_down
                        show jenny f_shower_butt1_talk
                        jen "Hmm, Eu acho que você pode fazer melhor..."
                        show jenny f_shower_butt1
                        show player f_side_shy_down_talk
                        player_name "POR FAVOR?!"
                        show player f_side_shy_down
                        show jenny f_shower_butt1_talk
                        jen "Hahahaah!!"
                        jen "Tudo bem, faça isso!"
                        show jenny_shower_sex 1
                        hide player
                        hide jenny
                        jen "!!!" with hpunch
                        $ animated = True
                        $ anim_toggle = True
                        $ M_jenny.set('sex speed', .12)
                        show expression AnimatedImage("jenny_shower_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_shower_sex at Position(xalign = 0.0, yoffset = 0) with dissolve
                        jen "Uau, você está realmente está bem animado!"
                        player_name "Concerteza!"
                    else:
                        pause
                        show jenny_shower_sex 1
                        hide player
                        hide jenny
                        jen "O que" with hpunch
                        $ animated = True
                        $ anim_toggle = True
                        $ M_jenny.set('sex speed', .12)
                        show expression AnimatedImage("jenny_shower_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_shower_sex at Position(xalign = 0.0, yoffset = 0) with dissolve
                        jen "... Oh, Foooode!"
                        pause
                        jen "Eu não disse que você poderia"
                        player_name "Você quer que eu pare?"
                        jen "NÃO!"
                        jen "Não pare!"
                    jump jenny_shower_sex_loop
        "Agora não.":
            player_name "( Hmm, Não... )"
            player_name "( Eu não estou realmente com vontade de mexer com ela hoje. )"
            pause
            $ renpy.end_replay()
            return

label shower_jenny_blowjob_intro_first:
    if store._in_replay is not None:
        $ player.location = L_home_shower
        call scene_shower_with_vfx
        with None
        $ M_jenny.set('rng', randomizer())
        if M_jenny.get('rng') > 50:
            show jenny b_shower_scene_d1 a_empty f_empty
            pause
            show jenny b_shower_scene_d_rub with dissolve
        else:
            show jenny b_shower_scene_e_rub a_empty f_empty
    player_name "( Eu me pergunto se ela percebe que estou a observando? )"
    pause
    player_name "( Será que ela se importaria se eu me juntasse a ela? )"
    player_name "( Quero dizer, depois do que temos feito coisas interessantes, tomar banho juntos não parece ser tão ruim... )"
    pause
    player_name "( Não, ela poderia surtar e me bater com seu secado maldito )"
    jen "Você só vai ficar aí e assistir?"
    player_name "!!!" with hpunch

    if M_jenny.get('rng') > 50:
        show jenny b_shower a_naked_hips f_sexy_camera at Position (xoffset=-200) with dissolve
    else:
        show jenny b_shower_back f_shower_overshoulder_back_look_normal a_shower_back_down at Position (align=(0,0)) with dissolve
    player_name "Hã?!"
    player_name "Eu não estava"
    if M_jenny.get('rng') > 50:
        show jenny f_sexy_camera_talk at Position (xoffset=-200)
    else:
        show jenny f_shower_overshoulder_back_look_normal_talk
    jen "Hehe, você tirar suas roupas e entrar aqui já!"
    if M_jenny.get('rng') > 50:
        show jenny f_sexy_camera at Position (xoffset=-200)
    else:
        show jenny f_shower_overshoulder_back_look_normal
    player_name "Sèrio?"
    if M_jenny.get('rng') > 50:
        show jenny f_sexy_camera_talk at Position (xoffset=-200)
    else:
        show jenny f_shower_overshoulder_back_look_normal_talk
    jen "Sim!"
    if M_jenny.get('rng') > 50:
        show jenny f_sexy_camera at Position (xoffset=-200)
    else:
        show jenny f_shower_overshoulder_back_look_normal
    player_name "Ok."
    call scene_shower_with_vfx
    show jenny f_sexy b_shower a_naked_hips
    show player b_naked a_naked_sides f_worried_talk od_naked_dick3
    with fade
    player_name "Então, ehh..."
    player_name "Você precisa de uma mão ou algo assim?"
    show player f_worried
    show jenny f_grin_talk
    jen "Você realmente perguntou se eu precisava de uma mão?"
    show jenny f_grin
    player_name "..."
    show jenny f_laugh
    jen "Pfft, hahahaha!"
    jen "Isso é tão patético!"
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Cale-se!"
    show player f_skeptical
    show jenny f_laugh
    jen "Haha!"
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Você acabou de me convidar para entrar, so para tirar sarro de mim?"
    show player f_skeptical
    show jenny f_grin_talk a_shower_soap1 with dissolve
    jen "Não."
    jen "Eu na verdade estava pensando que poderiamos nos divertir um pouco."
    show jenny f_grin_down a_shower_soap2 with dissolve
    pause
    show jenny a_shower_soap3 with dissolve
    show player f_worried_talk
    player_name "{b}*Gole*{/b} Mesmo?"
    show player f_worried
    show jenny f_grin_talk a_shower_soap2 o_shower_soap1 with dissolve
    jen "Sim."
    show jenny f_grin
    pause
    show jenny f_upset_talk a_shower_soap1 with dissolve
    jen "Claro, isso foi antes de você me alimentar com essa conversa estúpida."
    show jenny f_grin_down a_shower_soap4 with dissolve
    player_name "..."
    show jenny f_grin_talk b_shower_soaping a_empty o_empty with dissolve
    jen "Então agora, eu estou pensando ... Você terá que implorar."
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Hã?"
    show player f_skeptical
    pause
    show jenny f_eyeroll b_shower a_naked_hips with dissolve
    jen "Você quer me ajudar no banho, não é?"
    show jenny f_upset
    show player f_worried_talk
    player_name "Concerteza."
    show player f_worried
    show jenny f_grin_talk
    jen "Então seja um bom cãozinho e implore!"
    show jenny f_grin
    show player f_worried_talk
    player_name "Você quer que eu implore?"
    show player f_worried
    show jenny f_grin_talk
    jen "Continue."
    show jenny f_grin
    player_name "..."
    if M_jenny.get("dominance") <= 0:
        show player f_worried_talk
        player_name "Por favor?"
        show player f_worried
        show jenny f_grin_talk
        jen "Por favor, o que?"
        show jenny f_grin
        show player f_worried_talk
        player_name "Por favor, deixa eu te ajudar com banho..."
        show player f_worried
        show jenny f_grin_talk
        jen "Agora late como um cachorro."
        show jenny f_grin
        show player f_worried_talk
        player_name "A FALA SERIO?!"
        show player f_worried
        show jenny f_laugh
        jen "Ah ah ah, eu disse faça!"
        show jenny f_grin
        player_name "..."
        jump bj_shower_repeat_sub
    else:
        show player f_skeptical_talk
        player_name "De jeito nenhum!"
        show player f_skeptical
        show jenny f_grin_talk
        jen "Sim Vamos!"
        show jenny f_grin
        player_name "..."
        show jenny f_upset_talk
        jen "Vamos lá {b}[firstname]{/b}, faça!"
        show jenny f_upset
        show player f_skeptical_talk
        player_name "Não!"
        show player f_skeptical
        show jenny f_angry_talk
        jen "Implore ou saia!"
        show jenny f_angry
        show player f_skeptical_talk
        player_name " Ta louca, Eu vo sair daqui."
        show player f_skeptical
        show jenny f_angry_talk
        jen "O que?!"
        jen "Você está seriamente indo embora mesmo?!"
        show jenny f_angry
        show player f_skeptical_talk
        player_name "Você sabe que eu odeio humilhação, {b}[jen_name]{/b}!"
        player_name "Se isso é que você que fazer, então esqueça!"
        show player f_skeptical
        show jenny f_angry_pouting
        jen "..."
        show jenny f_angry_talk
        jen "Grr, Bem!"
        show jenny f_angry
        call scene_shower_with_vfx_zoom
        show jenny_shower_bj_mc
        show jenny_shower_bj pre_look
        with fade
        player_name "!!!"
        show jenny_shower_bj pre_talk
        jen "Você realmente tira sarro de tudo isso!"
        show jenny_shower_bj pre_look
        player_name "O que você está fazendo?!"
        show jenny_shower_bj pre_talk
        jen "Que porra parece que estou fazendo?!"
        jump bj_shower_repeat_dom

label shower_jenny_snoop_around_for_laptop:
    scene expression player.location.background_closeup with None
    show player 17 with dissolve
    player_name "( Hmm, isto é {b}minha chance de entrar em seu quarto e olhar através de seu diário{/b}. )"
    player_name "( Eu deveria me apressar! )"
    hide player with dissolve
    return

label shower_jenny_snoop_around:
    scene expression player.location.background_closeup with None
    show player 13 with dissolve
    player_name "( Hmm, isto é {b}minha chance de entrar em seu quarto e procurar por aquela câmera{/b}. )"
    player_name "( Eu deveria me apressar! )"
    hide player with dissolve
    return

label shower_mom_sis_check:
    scene shower_cutscene1
    show text "Eu corri para cima em direção a {b}[jen_name]{/b} maldição.\nA cena ao entrar era quase cômica. {b}[jen_name]{/b} estava agitada e parecia um rato afogado.\nO tubo exposto estava jorrando água para todo lado e fazendo uma bagunça." at Position(xpos=500, ypos=700)
    with dissolve
    $ renpy.pause()
    hide shower_cutscene1
    hide text
    scene shower2
    show player 11 at left
    show jenny f_upset_talk b_wet a_dressed_hips
    with dissolve
    jen "Finalmente você apareceu!"
    show player 10
    show jenny f_upset
    player_name "Como isso aconteceu?!"
    show player 11
    show jenny f_upset_talk
    jen "Como eu deveria saber! Eu pareço um encanador para você ?! Tudo que fiz foi ligar a pia!"
    show player 12
    show jenny f_upset
    player_name "O que eu deveria fazer?"
    show player 11
    show jenny f_upset_talk
    jen "Conserta essa porcaria! Você é o único homem por aqui!"
    show jenny f_gross
    show player 12
    player_name "Bem! Eu acho que vou no {b}andar de baixo{/b} e desligar a {b}válvula de água{/b}..."
    hide player
    hide jenny
    with dissolve
    return

label shower_mom_close_valve:
    scene shower2
    show jenny f_upset_talk b_wet a_dressed_hips
    show player 11 at left
    with dissolve
    jen "A água ainda está vazando por toda parte!"
    jen "Vai atè o {b}porão{/b} e desligue a água na {b}válvula{/b}!"
    hide player
    hide jenny
    with dissolve
    return

label shower_mom_pipe_check:
    scene shower2
    show jenny b_wet a_dressed_hips f_upset_talk
    show player 11 at left
    with dissolve
    jen "Parece que você conseguiu. A água parou."
    show player 12
    show jenny f_upset
    player_name "Sim, desliguei a válvula de água. O que fasso agora?"
    show player 5
    show jenny f_upset_talk
    jen "O que você está me perguntando? Eu não sei, substitua ou algo assim?"
    show player 10
    show jenny f_upset
    player_name "Eu nunca trabalhei em nada assim antes!"
    show player 5
    show jenny f_upset_talk
    jen "Bem, você está morando em uma casa com garotas agora, o que significa que você precisa aprender a consertar essas coisas!"
    show player 10
    show jenny f_gross
    player_name "OK! OK! Eu acho que vou para {b}CONSUMIR{/b} e ver se consigo uma {b}chave inglesa{/b}."
    show player 212
    player_name "..."
    show player
    show jenny f_normal_low
    pause
    show jenny f_angry
    jen "..."
    show jenny f_angry_talk
    jen "Você deu uma boa olhada seu pequeno pervertido?!"
    show player 23
    show jenny f_angry
    player_name "Eu não estava olhando"
    show player 22
    show jenny f_angry_talk
    jen "Por favor, você acha que eu não posso dizer quando alguém está olhando para os meus seios?"
    show jenny f_angry
    player_name "..."
    show jenny f_angry_talk
    jen "Qual o problema com você?"
    show jenny f_angry
    show player 24
    player_name "Eu sinto Muito, {b}[jen_name]{/b}. eu só estava"
    show jenny f_angry_talk
    jen "Cale a boca!"
    show player 25
    jen "Se você vai olhar, pelo menos seja um homem sobre isso!"
    jen "Negar ou dar desculpas só faz você parecer um covarde."
    jen "Ninguém quer ser espiado por um pequeno covarde!"
    show jenny f_angry
    show player 5
    player_name "..."
    show jenny f_upset_talk at right
    jen "Se você tivesse chegado aqui para resolver, Essa situação mais cedo, talvez eu estivesse de bom humor."
    jen "... Mas desde que você decidiu tomar seu tempo doce..."
    show jenny f_grin_talk
    jen "Eu acho que você deveria levar isso..."
    show player 22
    show jenny f_grin_down a_empty b_pull1_wet with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show player 23
    show jenny b_panties f_upset_talk a_panties_shirt with dissolve
    jen "... Lá embaixo para a lavagem para mim."
    show jenny f_upset
    player_name "( !!! )" with hpunch
    show player 21
    player_name "Certo..."
    show jenny a_naked_hips f_angry
    show player 211
    with dissolve
    jen "..."
    show jenny f_angry_talk
    jen "Pare de olhar e vá! Eu não quero esperar o dia todo para você {b}consertar esse cano{/b}!"
    show jenny f_angry
    show player 22 with dissolve
    player_name "( !!! )"
    hide player with dissolve
    pause
    show jenny f_grin_talk
    jen "Ahh, eu sabia disso!"
    jen "Esse pequeno perdedor tem uma queda por mim!"
    hide jenny with dissolve
    hide shower2
    return

label shower_mom_fix_pipe_no_wrench:
    scene shower2
    show player 11 at left
    if not game.timer.is_dark():
        show jenny f_upset_talk b_panties a_naked_hips
        with dissolve
        jen "Você finalmente vai consertar a pia?"
        jen "Apresse-se já!"
        hide jenny with dissolve
        show player 4
    with dissolve
    player_name "( Eu preciso de uma chave inglesa para consertar o cano quebrado. )"
    hide player
    with dissolve
    return

label shower_mom_fix_pipe_wrench:
    scene expression "backgrounds/location_home_bathroom_cutscene02.jpg"
    show expression FilteredText("Assim que cheguei em casa, subi as escadas para arrumar a pia do banheiro.\nEu substituí a junta por um novo tubo e a apertei o máximo que pude.\nÉ meio estranho ter {b}[deb_name]{/b} e {b}[jen_name]{/b} me olhando o tempo todo.\nSorte para mim, os reparos correu tudo bem...") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade

    scene shower2
    show player 203f at right
    show jenny f_upset a_dressed_crossed at flip
    show jenny at Position (xpos=200)
    show debbie 62f at left
    with dissolve
    deb "Uau!!"
    deb "Ótimo trabalho, {b}[firstname]{/b}!"
    show jenny f_upset_talk
    show debbie 61f
    jen "Finalmente..."
    show jenny f_upset
    show debbie 62f
    deb "Não seja rude, {b}[jen_name]{/b}. Foi legal da parte dele consertar isso para nós..."
    show player 2f
    show debbie 61f
    player_name "Sem problema."
    player_name "Eu fico feliz em fazer isso."
    player_name "... Além disso, {b}[jen_name]{/b} está certa. Conserto de coisas assim é minha responsabilidade agora."
    show player 29f
    show jenny f_gross
    show debbie 62f
    deb "Você vai fazer da garota sortuda um ótimo marido um dia!"
    show player 203f
    show debbie 61f
    jen "Pfft haha fala serio..."
    show jenny f_upset_talk
    jen "Não diga coisas assim, Ele só traz dó de cabeça das grande!"
    show player 16f
    show jenny f_grin_talk
    jen "Ele ainda é um covarde, afinal."
    show player 15f
    show jenny f_grin
    show debbie 61f
    player_name "Eu não sou um covarde!"
    show player 16f
    show jenny f_grin_talk
    jen "E um Banana então!"
    show player 1f
    show jenny f_grin
    show debbie 62f
    deb "... Não dê ouvidos a ela {b}[firstname]{/b}. Ela só está brincando com você porque acha que você é um fofo."
    show jenny f_angry_talk
    show debbie 59f
    jen "... Até parece!"
    show player 11f
    show jenny f_eyeroll
    jen "... Agora vocês dois podem sair? Eu estive esperando para tomar banho o dia todo!"
    show jenny f_upset
    show debbie 60f
    show player 1f
    deb "Vamos {b}[firstname]{/b}. Vamos sair do caminho da princesa antes que seu mau humor nos infecte."
    show jenny f_grin_talk
    show debbie 59f
    jen "O que você diz \"Princesa\" é um elogio..."
    hide debbie
    hide jenny
    hide player
    with dissolve
    return

label shower_mom_shower_peek_after:
    scene location_home_hallway_day
    show player 3
    player_name "( {b}[deb_name]{/b} tem um corpo muito bom, mas eu não quero espiá-la por muito tempo... )"
    player_name "( Seria muito estranho se ela me pegasse. )"
    hide player with dissolve
    return

label shower_mom_shower_peek:
    player_name "( !!! )"
    show debbie_shower 6a_6b_6c
    player_name "( {b}[deb_name]{/b} no banho! )"
    player_name "( Uau... )"
    player_name "( Ela tem um corpo tão bom! )"
    player_name "( Eu não posso acreditar que ela deixou a porta aberta! "
    player_name "( Eu posso ver tudo! )"
    hide debbie_shower 6a_6b_6c
    scene shower06a
    player_name "..."
    scene shower06d
    player_name "( É melhor eu ir antes que ela me veja. )"
    scene hallway
    show player 79 with dissolve
    player_name "Uau..."
    player_name "Eu não posso acreditar que estou vivendo com essa linda mulher agora!"
    player_name "... É uma pena, Que ela só me veja como um filho do meu {b}Pai{/b}."
    show player 78 with dissolve
    player_name "( !!! )"
    show player 81
    player_name "É melhor eu voltar para o meu quarto antes que alguém veja esta barraca armada hehe..."
    hide player with dissolve
    return

label shower_mom_walk_in:
    player_name "( Impressionante! )"
    show debbie_shower 6a_6b_6c
    pause
    player_name "( Eu me pergunto se os seios dela são tão macios quanto as pernas dela. )"
    player_name "( Eles parecem ... perfeitos! )"
    hide debbie_shower 6a_6b_6c
    scene shower06a
    pause
    scene shower06d
    player_name "( Eu me pergunto o que aconteceria se eu entrar lá? )"
    player_name "( Ela provavelmente ficaria brava, mas e se ela gostar disso? )"
    show debbie_shower 6a_6b_6c
    player_name "( Eu posso fingir que não sabia que ela estar no chuveiro... )"
    return

label shower_mom_walk_in_yes:
    player_name "( Eu não posso resistir ... eu vou entrar! )"
    hide debbie_shower 6a_6b_6c
    call scene_shower_with_vfx
    show player 5 at left
    show debbie 35b at right
    with dissolve
    deb "( !!! )"
    show player 29 with dissolve
    player_name "Oops!"
    show player 3
    show debbie 35c
    deb "Querido, o que você está fazendo aqui?!!"
    show debbie 35
    deb "Estou nua!"
    show debbie 34
    show player 42 at Position (xoffset=38) with dissolve
    player_name "Desculpa, {b}[deb_name]{/b}! Eu não sabia que tinha alguêm aqui!"
    deb "..."
    show debbie 35
    deb "Está tudo bem.."
    deb "Se você precisar de algo no banheiro, apenas bata."
    deb "Eu terminarei em alguns minutos, ok?"
    show debbie 34
    show player 37 with dissolve
    player_name "Ok..."
    show player 3 with dissolve
    show debbie 35
    deb "Agora deixe-me terminar meu banho, docinho."
    show debbie 33
    deb "E feche a porta atrás de você!"
    show debbie 32
    show player 29
    player_name "esta bem!"
    hide player with dissolve
    show debbie 35
    deb "Isso é por causa do"
    deb "..."
    deb "Beijo..."
    deb "Eu deveria ter mais cuidado com ele."
    hide debbie with dissolve
    scene hallway
    show player 24 with dissolve
    player_name "( Ahh... Isso foi estranho... )"
    player_name "( Afinal Isso parecia uma boa ideia? )"
    pause
    show player 37 at Position (xoffset=41) with dissolve
    player_name "( Espero que ela não esteja muito brava comigo. )"
    hide player with dissolve
    return

label shower_mom_walk_in_no:
    player_name "Eu provavelmente não deveria."
    player_name "Eu não quero que ela fique chateada."
    hide debbie_shower 6a_6b_6c
    return

label shower_mom_sex:
    show debbie_shower 6a_6b_6c
    return

label shower_mom_sex_walk_in_pre:
    call scene_shower_with_vfx
    with dissolve
    show debbie 35 at right
    show player 1 at left
    deb "Oh, {b}[firstname]{/b}... Eu não esperava que você entrasse aqui agora!"
    show debbie 33
    deb "Porém, agora que você está aqui..."
    show debbie 36
    deb "Quer se juntar a mim, Docinho?"
    hide debbie
    hide player
    show debbies 37 with dissolve
    return

label shower_mom_sex_walk_in_after:
    call scene_shower_with_vfx
    show debbies 37_36 at Position (xpos=474)
    pause 4.8
    show debbies 35
    player_name "Eu amo tomar banho com você {b}[deb_name]{/b}"
    show debbies 76 with dissolve
    pause .1
    show debbies 41_76
    pause 4
    show debbies 42 at Position (xoffset=38)
    deb "Posso te ajudar aqui também?"
    show debbies 43 at Position (xoffset=38)
    deb "Humm..."
    show debbies 44 at Position (xoffset=38)
    deb "O que você tem em mente hoje?"
    show debbies 43 at Position (xoffset=38)
    deb "Algo divertido?"
    show debbies 72_71 at Position (xoffset=38)
    pause 4
    show debbies 45 at Position (xoffset=38) with dissolve
    deb "Você estar de pau duro. Faça o que você quiser comigo, querido..."
    show debbies 73 at Position (xoffset=38) with dissolve
    return

label shower_mom_sex_wash:
    player_name "Eu quero te lavar desta vez."
    show debbies 50 with dissolve
    deb "Vá em frente, querido."
    show debbies 51
    pause 1
    show debbies 52_53_52_51
    pause
    show debbies 54
    player_name "Tão macio..."
    return

label shower_mom_sex_wash_handjob:
    show debbies 45 with dissolve
    pause .4
    show debbies 73_74
    pause
    show debbies 73
    player_name "{b}[deb_name]{/b}, Eu vou..."
    show debbies 47 at Position(xpos=526,ypos=768)
    player_name "HNNGGG!!!"
    show white zorder 4 with dissolve
    show debbies 47 at Position(xpos=526,ypos=768)
    show playersex 33 zorder 3 at Position(xpos=610,ypos=880)
    hide white with dissolve
    pause
    show debbies 48
    hide playersex
    with dissolve
    deb "Mmm, bom menino."
    return

label shower_mom_sex_finger:
    player_name "Eu não tenho lavado {b}em toda parte{/b} ainda..."
    show debbies 55 at Position(xpos=688,ypos=768) with dissolve
    pause .35
    show debbies 56_55
    pause 4
    deb "... Estou quase lá, querido..."
    show debbies 56
    deb "EU Aaaaah!!!"
    show debbies 50 at Position(xpos=498,ypos=768) with dissolve
    deb "Como você sempre sabe exatamente onde esfregar?"
    show debbies 49
    player_name "Eu não sei, isso vem naturalmente, eu acho?"
    show debbies 50
    return

label shower_mom_sex_blowjob:
    show debbies 111 with dissolve
    deb "Que tal um tratamento especial?"
    show debbies 110
    player_name "Sim por favor..."
    show debbies 112 at Position(xpos=512) with dissolve
    pause .3
    show expression AnimatedImage("debbies", [113,114], M_mom) as debbies at Position(xpos=513) with dissolve
    $ animated = True
    call screen debbie_shower_blowjob_options

label debbie_shower_blowjob_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("debbies", [113,114], M_mom) as debbies at Position(xpos=513) with dissolve
                $ animated = True
            pause 5
            call expression game.dialog_select("debbie_shower_blowjob_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [113,114]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies at Position(xpos=513) with dissolve
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("debbie_shower_blowjob_hscene_dialog")
        $ animcounter += 1
    call screen debbie_shower_blowjob_options

label debbie_shower_blowjob_hscene_dialog:
    if animcounter == 1 and randomizer() < 25:
        player_name "Oh, Deus!{p=1}{nw}"
    if animcounter == 4 and randomizer() < 25:
        player_name "Eu não posso segurar mais{p=1}{nw}"
    return

label debbie_shower_blowjob_cum_in:
    show debbies 113 at Position(xpos=513)
    pause .3
    show debbies 116 at Position(xpos=517)
    player_name "HNNGGG!!!"
    deb "( !!! )"
    show white with dissolve
    hide white with dissolve
    pause
    show debbies 117 at Position(xpos=523) with dissolve
    deb "HMMPH!!!"
    show debbies 118 at Position(xpos=516)
    deb "{b}*Gole*{/b}"
    show debbies 115 at Position(xpos=531)
    deb "... Oh, isso foi muito!"
    show debbies 110 at Position(xpos=512)
    player_name "Desculpa, {b}[deb_name]{/b}."
    show debbies 111
    deb "Não, não se desculpe, querido."
    deb "Eu amo o gosto do seu esperma!"
    return

label debbie_shower_blowjob_cum_out:
    show debbies 113 at Position(xpos=513)
    pause .3
    show debbies 116 at Position(xpos=517)
    player_name "HNNGGG!!!"
    deb "( !!! )"
    show white with dissolve
    show debbies 115 at Position(xpos=531)
    show playersex 74 at Position(xpos=530,ypos=519)
    hide white with dissolve
    pause
    show playersex 75 at Position(xpos=574,ypos=655)
    deb "Hehe, olha a bagunça que você fez no meu rosto!"
    deb "... Estou coberto..."
    player_name "Desculpa, {b}[deb_name]{/b}."
    deb "Está bem!"
    deb "Estamos no chuveiro, por isso é fácil de limpar!"
    deb "... Apenas me ajude a tirar isso do meu cabelo."
    return

label shower_mom_sex_already_fingered:
    show debbies 49
    player_name "Posso colocar isso?"
    show debbies 50
    deb "Querido, eu acabei de chegar ... É um pouco sensível demais agora..."
    deb "Eu vou acabar com a minha mão."
    return

label shower_mom_sex_fuck_pre:
    show debbies 49 with dissolve
    if randomizer() <= 33:
        player_name "{b}[deb_name]{/b}..."
        player_name "Posso colocar dentro de você?"
        show debbies 50
        deb "Claro, Docinho..."
        show debbies 57 at Position(xpos=688,ypos=768) with dissolve
        deb "Oh, eu estive esperando o dia todo por isso..."
    elif randomizer() <= 66:
        player_name "{b}[deb_name]{/b}, Eu quero fazer isso com você."
        show debbies 50
        deb "Querido..."
        deb "Você é insaciável."
        deb "Segure minha perna e me dê esse pau grande!"
        show debbies 57 at Position(xpos=688,ypos=768) with dissolve
        pause
    else:
        player_name "{b}[deb_name]{/b}, eu quero você."
        show debbies 50
        deb "Eu estava esperando por isto."
        deb "Me dê esse lindo pau gostoso."
        show debbies 57 at Position(xpos=688,ypos=768) with dissolve
        pause
    show debbies 58 with dissolve
    deb "Haah!"
    show debbies 59 with dissolve
    pause
    return

label mom_shower_sex_loop:
    show screen xray_scr
    pause
    hide screen xray_scr
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("debbies", [59,60,61], M_mom) as debbies at Position(xpos = 688,ypos = 768)
                $ animated = True
            pause 5
            if animcounter in [1,2,3]:
                call expression game.dialog_select("debbie_shower_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [59,60,61]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies at Position(xpos = 688,ypos = 768)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,2,3]:
                call expression game.dialog_select("debbie_shower_hscene_dialog")
        $ animcounter += 1
    call screen shower_mom_sex_options

label debbie_shower_hscene_dialog:
    if randomizer() <= 33:
        if animcounter == 1:
            deb "Ahhhh!!!{p=1}{nw}"
            deb "Goza para mim, Docinho!{p=2}{nw}"
        elif animcounter == 3:
            deb "Goza para mim!{p=2}{nw}"
    elif randomizer() <= 66:
        if animcounter == 1:
            deb "Ohh!!{p=1}{nw}"
        elif animcounter == 2:
            deb "Querido! mais fundo!{p=2}{nw}"
        elif animcounter == 3:
            player_name "{b}[deb_name]{/b}, eu te amo!{p=2}{nw}"
            deb "Eu também te amo!{p=2}{nw}"
    else:
        if animcounter == 2:
            player_name "Eu amo o jeito que seus peitos saltam.{p=2}{nw}"
            deb "Sim, bem, eu amo seu pau enorme!{p=2}{nw}"
        elif animcounter == 3:
            deb "Ahh!!{p=1}{nw}"
            deb "Sim, esse é o local!{p=2}{nw}"
    return

label mom_shower_sex_cum:
    call expression game.dialog_select("mom_shower_sex_cum_pre")
    $ cum = True
    call expression game.dialog_select("mom_shower_sex_cum_after")
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["07_unlocked"] = True
    jump expression game.dialog_select("mom_shower_end")

label mom_shower_sex_cum_pre:
    if randomizer() <= 33:
        player_name "UHHH!"
    elif randomizer() <= 66:
        deb "Goza para mim querido!"
        deb "Goza dentro de mim!"
    else:
        deb "HAAAAAHH!"
    return

label mom_shower_sex_cum_after:
    show debbies 60
    show white zorder 4 with dissolve
    hide white with dissolve
    pause
    if randomizer() <= 50:
        player_name "Isso foi bom..."

    show playersex 53 zorder 3 at Position(xpos=663,ypos=632)
    show debbies 57
    with dissolve
    if randomizer() <= 50:
        deb "Você gozou tanto..."
        deb "Uma bagunça."
        deb "Ainda bem que estamos no chuveiro..."
    else:
        deb "Ohh!"
        deb "Deus, eu amo esse seu pau!"
        player_name "Hehe, Tenho certeza que ele sente da mesma maneira sobre você..."
        deb "Ha Ha Ha!"
        deb "Me segure. eu não sinto minhas pernas depois de tudo isso!"
    return

label mom_shower_end_dialogue:
    hide playersex
    hide debbies
    show debbies 34 at Position(xpos=474,ypos=768)
    with dissolve
    if randomizer() <= 50:
        deb "Isso foi divertido, mas eu realmente deveria descer e começar o jantar."
        deb "Nós vamos fazer isso de novo, ok?"
        deb "Certificar-se de que{b}[jen_name]{/b} não vê você sair do banheiro, ok?"
    else:
        deb "eu espero {b}[jen_name]{/b} não nos ouviu..."
        show debbies 35
        player_name "Eu duvido. Não com o chuveiro ligado..."
        show debbies 34
        deb "... Sim, suponho que estou me preocupando demais."
        deb "Eu deveria descer e começar a preparar o jantar..."
        deb "Me traga uma toalha?"
        show debbies 35
        player_name "Coisa certa, {b}[deb_name]{/b}!"
    hide debbie_shower
    hide debbie
    hide debbies
    hide player
    with dissolve
    return

label mom_shower_end:
    call expression game.dialog_select("mom_shower_end_dialogue")
    $ renpy.end_replay()
    $ game.timer.tick()
    $ playSound()
    jump expression game.dialog_select("hallway_dialogue")

label shower_mom_sex_leave:
    player_name "Eu provavelmente não deveria."
    player_name "Eu não quero que ela fique chateada."
    return

label shower_jenny_shower_spy_repeat:
    call scene_shower_with_vfx_peep
    $ M_jenny.set('rng', randomizer())
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a1_blurred f_empty a_empty
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b1_blurred f_empty a_empty
    else:
        show jenny b_shower_scene_c1_blurred f_empty a_empty
    with dissolve
    pause
    player_name "( Hmm, tá embassado... )"
    player_name "( Eu não consigo ver droga! )"
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a1
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b1
    else:
        show jenny b_shower_scene_c1
    show bathroom_door_left at Position (xoffset=-50)
    show bathroom_door_right at Position (xoffset=50)
    with dissolve
    if M_jenny.finished_state(S_jenny_perv_on_tammy) and not M_jenny.get("first_shower_time"):
        player_name "( Olá, {b}[jen_name]{/b}... )"
    elif M_jenny.finished_state(S_jenny_pissed_at_handjob) or store._in_replay is not None:
        player_name "( Oh, aqui vamos nós. )"
        player_name "( Espero não ter perdido o show! )"
    elif M_jenny.finished_state(S_jenny_talked_to_cedric):
        player_name "( Hehe, è {b}[jen_name]{/b} novamente! )"
    else:
        player_name "( Uau!! )"
        player_name "( è a {b}[jen_name]{/b}! )"
    pause

    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a2
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b2
    else:
        show jenny b_shower_scene_c2
    with dissolve

    if M_jenny.finished_state(S_jenny_perv_on_tammy) and not M_jenny.get("first_shower_time"):
        player_name "( Eu não posso acreditar o quanto aconteceu entre nós! )"
        player_name "( Algumas semanas atrás, ela teria se apavorado com isso, mas agora... )"
    elif M_jenny.finished_state(S_jenny_pissed_at_handjob) or store._in_replay is not None:
        pause
    elif M_jenny.finished_state(S_jenny_talked_to_cedric):
        player_name "( Ela deveria levar sua webcam lá com ela, ela provavelmente faria uma fortuna... )"
        pause
    else:
        player_name "( Caralho, ela ficaria tão chateada se soubesse que eu estava espiando ela! )"
        pause

    if M_jenny.get('rng') > 75:
        show jenny b_shower_scene_a3
    elif 75 > M_jenny.get('rng') > 50:
        show jenny b_shower_scene_b3
    elif 50 > M_jenny.get('rng') > 25:
        show jenny b_shower_scene_c3
    else:
        show jenny b_shower_scene_e3
    with dissolve

    if M_jenny.finished_state(S_jenny_perv_on_tammy) and not M_jenny.get("first_shower_time"):
        player_name "( Eu posso apenas entrar e me juntar a ela, sempre que eu quiser! )"
    elif M_jenny.finished_state(S_jenny_pissed_at_handjob) or store._in_replay is not None:
        player_name "( Vamos lá {b}[jen_name]{/b}, Você sabe que você quer... )"
    elif M_jenny.finished_state(S_jenny_talked_to_cedric):
        player_name "( Mmm, Eu poderia vê-la esfregar esse corpo o dia todo... )"
    else:
        player_name "( É uma pena que ela seja uma vadia o tempo todo... )"
        player_name "( Com um corpo assim, ela poderia ter qualquer cara que ela quisesse. )"
        pause
        player_name "( Eu deveria sair daqui antes que ela me pegue. )"
        pause
        scene black with fade
        jump jenny_shower_peep_end

    if M_jenny.get('rng') > 50:
        show jenny b_shower_scene_d1
    else:
        show jenny b_shower_scene_e_rub

    if M_jenny.finished_state(S_jenny_perv_on_tammy) and not M_jenny.get("first_shower_time"):
        pause
    elif M_jenny.finished_state(S_jenny_pissed_at_handjob) or store._in_replay is not None:
        player_name "( Bingo! )"
    else:
        player_name "( !!! )" with hpunch

    if M_jenny.get('rng') > 50:
        show jenny b_shower_scene_d_rub with dissolve
    return

label shower_jenny_shower_spy:
    call scene_shower_with_vfx_peep
    $ M_jenny.set('rng', randomizer())
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a1_blurred f_empty a_empty
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b1_blurred f_empty a_empty
    else:
        show jenny b_shower_scene_c1_blurred f_empty a_empty
    with dissolve
    pause
    player_name "( Hmm, Droga tá embassado... )"
    player_name "( Eu não consigo ver nada! )"
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a1
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b1
    else:
        show jenny b_shower_scene_c1
    show bathroom_door_left at Position (xoffset=-50)
    show bathroom_door_right at Position (xoffset=50)
    with dissolve
    player_name "( Uau!! )"
    player_name "( È a {b}[jen_name]{/b}! )"
    pause
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a2
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b2
    else:
        show jenny b_shower_scene_c2
    with dissolve
    player_name "( Caralho, ela ficaria tão chateada se soubesse que eu estava espiando ela! )"
    pause
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a3
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b3
    else:
        show jenny b_shower_scene_c3
    with dissolve
    player_name "( Basta olhar para esse corpo! )"
    player_name "( Ela é perfeita )"
    show jenny b_shower_caught_front_surprised
    player_name "( !!! )" with hpunch
    jen "Que porra {b}[firstname]{/b}!!!"
    player_name "( Ai merda ela me viu... )"

    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 6 at left
    show jenny b_towel a_towel_hit f_angry_talk at Position (xpos=350)
    with dissolve
    jen "Você!"
    show jenny f_angry a_towel_hit2 with dissolve
    player_name "Aii!"
    show jenny f_angry_talk a_towel_hit with dissolve
    jen "Que Pouca vergonha!"
    show jenny f_angry a_towel_hit2 with dissolve
    player_name "Ow!!"
    show jenny f_angry_talk a_towel_hit with dissolve
    jen "PERVERTIDO!!!"
    show jenny f_angry a_towel_hit2 with dissolve
    player_name "Aii ta doendo!!"
    show player 12
    show jenny a_towel_hit
    with dissolve
    player_name "Pare de me bater!!!"
    show player 90
    hide jenny
    show jenny b_towel f_angry_talk a_towel_hips with dissolve
    jen "O que diabos qual é o problema com você?!"
    show jenny f_angry
    show player 12
    player_name "Nada, eu só vi a porta aberta e eu"
    show player 24
    show jenny f_angry_talk
    jen "... E você o que?!"
    jen "Achava que estava tudo bem, Me espiar no chuveiro?!"
    show jenny f_angry
    show player 25
    player_name "Não me desculpe..."
    show jenny f_gross
    pause
    show player 24
    pause
    player_name "Tudo bem. eu não conseguir resistir..."
    show jenny f_angry_talk
    jen "É seu pequeno patético"
    show jenny f_angry
    show player 10
    player_name "Me desculpe, tudo bem?!"
    show player 5
    pause
    show jenny f_angry_talk
    jen "{b}*Suspiro*{/b} SAIA DAQUI, Se não vou contar para {b}[deb_name]{/b}!"
    show jenny f_angry
    show player 23
    player_name "Não, não, por favor não diga {b}[deb_name]{/b}!"
    player_name "Estou indo agora mesmo!"
    hide player with fastdissolve
    pause
    show jenny f_gross
    jen "( Grr, ele é um fracassado perdedor! )"
    jen "( Eu só quero torcer o pescoço idiota dele! )"
    hide jenny with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
