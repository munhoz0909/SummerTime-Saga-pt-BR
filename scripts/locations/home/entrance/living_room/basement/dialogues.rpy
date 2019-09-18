label basement_mom_wash_clothes:
    scene home_basement_sideview
    show player 324 at Position(xpos=860)
    show debbie 136 at Position(xpos=550,ypos=805)
    deb "... Oh bom, você trouxe essas roupas sujas para baixo."
    show debbie 137
    deb "{b}*Risadinha*{/b}"
    show player 325
    show debbie 135
    player_name "O que é tão engraçado?"
    show player 326
    show debbie 136
    deb "Sua roupas! Elas são uma bagunça!"
    show player 324
    show debbie 137
    deb "Você estava realmente trabalhando duro lá fora, né?"
    show player 325
    show debbie 135
    player_name "Sim, eu provavelmente deveria ter tirado antes de fazer qualquer outra coisa..."
    show player 324
    show debbie 136
    deb "Tudo bem, querido! Nós vamos limpar tudo."
    deb "Entregue suas roupas eu vou colocar na lavanderia."
    show player 325
    show debbie 135
    player_name "Está bem, {b}[deb_name]{/b}. eu posso fazer isso."
    show player 324
    show debbie 136
    deb "Não tem problema. Eu estava me preparando para começar a lavar."
    show debbie 135
    show player 327 at Position(xoffset=-27) with fastdissolve
    pause

    scene expression "backgrounds/location_home_basement_cutscene.jpg"
    show expression FilteredText("Foi um pouco embaraçoso despir na frente de {b}[deb_name]{/b}. \nEla não pareceu notar embora. Ela apenas apressadamente enfiou minhas roupas na máquina. \nEu não pude deixar de notar a visão enquanto ela fazia seu trabalho.\nDificil será dizer que esqueci meu constrangimento rapidamente...") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade

    scene home_basement_sideview
    show player 330 at Position(xpos=860)
    show debbie 142 at Position(xpos=550,ypos=805)
    with fade
    deb "( Ele provavelmente vai usar esses pugilistas fedidos o dia todo agora. )"
    deb "( Eu deveria adicioná-los também. Caso contrário, eles podem acabar colocando em seu andar para a próxima semana... )"
    show debbie 136
    deb "Boxers também, {b}[firstname]{/b}."
    show player 332
    deb "Pode muito bem fazer tudo agora."
    show debbie 135
    player_name "( !!! )"
    show player 331
    player_name "Mesmo? Não, está tudo bem. Eu só vou jogá-los na cesta de roupa suja no andar de cima..."
    show debbie 136
    show player 330
    deb "Não seja bobo, você está aqui agora. Vamos apenas jogá-los e você pode ir tomar um banho!"
    show debbie 135
    show player 333
    player_name "... Sim mas"
    show debbie 136
    show player 330
    deb "Não há necessidade de se sentir envergonhado. Não é nada que eu não tenha visto um milhão de vezes antes."
    deb "Vamos apenas apressar e acabar com isso."
    show debbie 138
    show player 334 with fastdissolve
    pause
    show player 335 with fastdissolve
    pause
    show player 336 with fastdissolve
    pause 0.1
    show debbie 139
    show player 337 at Position(xpos=855) with vpunch
    pause
    show debbie 140
    show player 338 at Position(xpos=853)
    deb "Oh Meu..."
    deb "..."
    deb "Uau! Isso é um ... Isso é..."
    deb "Deixe-me pegar algo para você se cobrir."
    show debbie 141 with fastdissolve
    pause
    show player 339 at Position(xpos=845)
    show debbie 142
    with fastdissolve
    pause
    show player 341
    player_name "Eu sinto Muito, {b}[deb_name]{/b}."
    show player 340
    show debbie 143
    deb "Sem problema, Docinho."
    deb "Essas coisas acontecem."
    show debbie 140
    deb "É perfeitamente natural."
    show debbie 142
    deb "Heh."
    show debbie 143
    deb "Essa toalha de mão não é realmente o tamnhao certo è?"
    deb "Desculpe eu não tenho nada maior aqui..."
    deb "É melhor você correr agora e tomar banho."
    show debbie 142
    show player 341
    player_name "Sim, senhora"
    hide player with dissolve

    show debbie 139
    deb "( Minha nossa... )"
    deb "( ... Eu não tinha ideia de que ele era tão ...bem dotado. )"
    scene black with fade
    return

label basement_mom_close_valve:
    scene home_basement
    show player 34 with dissolve
    player_name "( A válvula de água deve estar ao lado do aquecedor de água. )"
    player_name "( É melhor desligá-lo antes das inundações no andar de cima. )"
    hide player with dissolve
    return

label basement_mom_give_laundry:
    scene home_basement_c
    show debbie 125 at right
    show player 277 at left
    with dissolve
    player_name "Ah, aí está você!"
    show player 276
    player_name "Eu trouxe sua roupa para baixo como você pediu."
    show player 13
    show debbie 121
    with dissolve
    pause
    show debbie 123
    deb "Obrigada querido."
    deb "Isso foi apenas uma desculpa para você vim até aqui..."
    show debbie 124
    show player 10
    player_name "O que está rolando?"
    show player 5
    show debbie 123
    deb "Hehe..."
    show debbie 63 with dissolve
    deb "Deixei essa anotação esta manhã porque queria ver você antes de sair."
    show debbie 61
    show player 11
    player_name "Hã?"
    show debbie 39
    deb "Eu quero você, {b}[firstname]{/b}!"
    show debbie 62
    show player 1
    deb "Eu quero montar no seu grande pau!"
    show debbie 61
    show player 2
    player_name "Claro!"
    show player 13
    show debbie 62
    deb "Tire essas roupas!"
    show player 11
    show debbie 125
    player_name "( !!! )"
    show player 297
    player_name "Sim, senhora!"
    show player 13
    show debbie 62
    deb "{b}[jen_name]{/b} Não nos encontrará aqui embaixo."
    show player 21
    show debbie 125
    player_name "Bem ... tudo bem."
    return

label basement_mom_sex:
    $ M_mom.set("sex speed", .175)
    $ player.go_to(L_home_basement)
    $ cum = False
    $ anim_toggle = True
    $ animated = False
    $ xray = False
    if not M_mom.is_state(S_mom_give_laundry) and randomizer() <= 50:
        $ mom_basement_rand = True
    else:
        $ mom_basement_rand = False
    call expression game.dialog_select("basement_mom_sex_pre")
    jump expression game.dialog_select("basement_mom_sex_loop")

label basement_mom_sex_pre:
    if mom_basement_rand:
        scene home_basement_c
        show debbie 62 at right
        show player 13 at left
        with dissolve
        deb "Sente-se na lavadora para mim."
    scene home_basement_sex_01
    show player 270 zorder 1 at Position(xpos=466,ypos=768)
    show debbie 107 zorder 0 at Position(xpos=200)
    with fade
    pause
    show player 271 at Position(xpos=655,ypos=768)
    pause
    if mom_basement_rand:
        player_name "Bom assim?"
        show debbie 108
        deb "Perfeito."
        deb "Esse seu pau é simplesmente perfeito."
    else:

        show debbie 108
        deb "My turn..."
    show debbie 109 at Position(xpos=205)
    pause
    show debbie 110
    pause
    show debbie 111 at Position(xpos=207)
    pause
    show debbie 112 at Position(xpos=196)
    pause
    show debbie 113 at Position(xpos=203)
    pause
    show debbie 114
    pause
    show debbie 115
    if mom_basement_rand:
        deb "Agora sente-se e deixe-me ajudá-lo com sua carga pegajosa suja."
    else:

        deb "Gostou do que está vendo?"
        show debbie 114
        player_name "Você é linda, {b}[deb_name]{/b}."
        show debbie 115
        deb "Apenas sente-se e relaxe, querido."
        deb "Vamos começar bem devagar..."
    hide player
    hide debbie
    show debbies 124 at Position(xpos=650)
    with dissolve
    pause
    show debbies 125 at Position(xpos=655) with dissolve
    pause
    show debbies 126f at Position(xpos=660) with dissolve
    deb "Oh!"
    show debbies 126e
    pause
    show debbies 126d
    pause
    show debbies 126c
    pause
    show debbies 126b
    pause
    show debbies 126
    if mom_basement_rand:
        deb "Mmmm..."
        deb "Eu mal consigo encaixar todo esse pau."
    else:

        deb "Ahh..."
        player_name "( !!! )"
        player_name "Você é tão sexy..."
    return

label basement_mom_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("debbies", ["126","126b","126c","126d","126e","126f","126g","126h","126i","126j"], M_mom) as debbies at Position(xpos = 660)
                $ animated = True
            pause 4
            call expression game.dialog_select("debbie_basement_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = ["126","126b","126c","126d","126e","126f","126g","126h","126i","126j"]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies at Position(xpos = 660)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("debbie_basement_hscene_dialog")
        $ animcounter += 1
    call screen basement_mom_sex_options

label debbie_basement_hscene_dialog:
    if animcounter == 1:
        if mom_basement_rand:
            deb "Oh, bebê!{p=1}{nw}"
            deb "Sim!{p=1}{nw}"
        else:

            deb "Ahhhh!!!{p=1}{nw}"

    elif animcounter == 2:
        deb "Ahh!!!{p=1}{nw}"

    elif animcounter == 3:
        if mom_basement_rand:
            deb "Oh!{p=1}{nw}"
        else:

            deb "Oh, DOCINHO!!!{p=1}{nw}"
            player_name "Uhhh...{p=1}{nw}"
    return

label basement_mom_sex_cum:
    player_name "{b}[deb_name]{/b}!"
    show white
    show debbies 129 at Position(xpos=609) with vpunch
    hide white with dissolve
    if mom_basement_rand:
        deb "Oh, DOCINHO!"
        deb "Estou gozando também!"
        show debbies 129 with flash
        deb "AHH!!!"
    else:

        deb "Ahh!!!"
    jump expression game.dialog_select("basement_mom_sex_after")

label basement_mom_sex_after:
    if M_mom.is_state(S_mom_give_laundry):
        call expression game.dialog_select("basement_mom_sex_after_pre_give_laundry")

    elif mom_basement_rand:
        call expression game.dialog_select("basement_mom_sex_after_pre_random")
    else:

        call expression game.dialog_select("basement_mom_sex_after_pre")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["12_unlocked"] = True
    $ game.timer.tick()
    if M_mom.is_state(S_mom_give_laundry):
        jump expression game.dialog_select("basement_confession_kiss")
    $ game.main()

label basement_confession_kiss:
    call expression game.dialog_select("basement_confession_kiss_pre")
    if randomizer() <= M_mom.get("mom concerned"):
        if M_mom.get("mom concerned") > 0:
            $ M_mom.set("mom concerned", M_mom.get("mom concerned") - 20)

        if M_mom.get("mom concerned") < 0:
            $ M_mom.set("mom concerned", 0)

        call expression game.dialog_select("basement_confession_kiss_concerned_random")
    call expression game.dialog_select("basement_confession_kiss_after")
    $ M_mom.trigger(T_mom_basement_fun)

    $ game.main()

label basement_mom_sex_after_pre_give_laundry:
    show debbies 132 at Position(xpos=650) with fade
    deb "Obrigado por me trazer a roupa..."
    show debbies 131
    player_name "Foi um prazer, {b}[deb_name]{/b}."
    show debbies 132
    deb "Deixe-me saber se você quer fazer isso de novo aqui."
    show debbies 131
    player_name "Concerteza."
    return

label basement_mom_sex_after_pre_random:
    show debbies 130 at Position(xpos=650) with fade
    deb "Isso foi maravilhoso, querido!"
    show debbies 131
    player_name "sim, foi!"
    player_name "Eu gosto de fazer isso com você no porão!"
    player_name "Aqui nós podemos fazer bastante barulho, Que ninguêm pode nos ouvir."
    show debbies 132
    deb "Hehe, Sim. aqui e um lugar perfeito!"
    return

label basement_mom_sex_after_pre:
    show debbies 132 at Position(xpos=650) with fade
    deb "Isso foi bom querido."
    deb "Obrigada pelo convite!"
    show debbies 131
    player_name "Até qualquer momento!"
    return

label basement_confession_kiss_pre:
    scene home_basement_c
    show player 227 at Position(xpos=200)
    show debbie 73 at Position(xpos=650)
    with fade
    deb "querido..."
    return

label basement_confession_kiss_concerned_random:
    deb "Eu quero que você me diga se você não quer mais fazer isso, ok?"
    show player 228
    show debbie 76
    player_name "Não, está bem, {b}[deb_name]{/b}..."
    player_name "Eu sempre sinto vontade de fazer isso com você."
    show player 227
    show debbie 77
    deb "Mesmo?"
    show player 228
    player_name "Sim, isso é tudo que eu penso quando vejo você..."
    show player 227
    show debbie 75
    deb "Você é sempre tão doce..."
    return

label basement_confession_kiss_after:
    deb "Dê-me um beijo."
    hide player
    show debbie 80 at Position(xpos=500)
    with dissolve
    pause
    show debbie 79 with dissolve
    pause
    show debbie 80 with dissolve
    pause
    show player 228 at Position(xpos=200)
    show debbie 78 at Position(xpos=650)
    with dissolve
    player_name "eu te amo, {b}[deb_name]{/b}!"
    show player 227
    show debbie 75
    deb "Eu também te amo docinho..."
    scene home_basement
    hide debbie
    hide player
    with fade
    return

label broken_pipe:
    call expression game.dialog_select("broken_pipe_dialogue")
    $ M_mom.trigger(T_mom_closed_valve)
    $ game.main()

label broken_pipe_dialogue:
    scene home_basement
    show popup_pipe_fixed at truecenter with dissolve
    pause
    hide popup_pipe_fixed with dissolve
    scene home_basement_c
    show player 2
    with dissolve
    player_name "Ok, a válvula está fechada."
    player_name "Eu deveria voltar para o {b}banheiro{/b} para ver se consigo consertar a {b}Pia{/b}."
    hide player
    with dissolve
    return

label laundry_dialogue:
    call expression game.dialog_select("laundry_dialogue_pre")
    menu:
        "Deixa-me ajudar.":
            call expression game.dialog_select("laundry_dialogue_help")
            $ M_mom.trigger(T_mom_cleaned_laundry)
        "Você está ocupado.":


            call expression game.dialog_select("laundry_dialogue_busy")
    $ M_mom.set("chores", False)
    $ game.main()

label laundry_dialogue_pre:
    scene home_basement_c
    show debbie 123 at right
    show player 1 at left
    with dissolve
    deb "Oh! Oi docinho!"
    deb "Você precisa de algo?"
    show debbie 124
    return

label laundry_dialogue_help:
    show debbie 124
    show player 14
    player_name "Eu posso lavar a roupa {b}[deb_name]{/b}. Por que você não faz uma pausa."
    show debbie 123
    show player 5
    deb "Está bem. eu posso fazer isso."
    show debbie 122
    show player 10
    player_name "Você merece um descanso. Você faz muito trabalho pela casa."
    player_name "Além disso, eu gosto de ajudar você."
    show debbie 123
    show player 11
    deb "Ah {b}[firstname]{/b}. Você tem sido uma grande ajuda por aqui ultimamente!"
    show player 1
    deb "O que eu fiz para merecer um inquilino tão maravilhoso?"
    show player 275
    show debbie 62
    deb "Você sabe como tudo funciona?"
    show debbie 125
    show player 276
    player_name "Sim, não é minha primeira vez fazendo uma lavagem de roupa."
    show debbie 63
    show player 275
    deb "Muito obrigada por fazer isso, {b}[firstname]{/b}."
    deb "Eu realmente apreciei isso."
    deb "Seu {b}Pai{/b} ficaria tão orgulhoso de você!"
    show debbie 125
    show player 277
    player_name "Hehe, obrigado!"
    scene expression "backgrounds/location_home_cutscene03.jpg"
    show expression FilteredText("Tem sido muito divertido ajudar {b}[deb_name]{/b} em casa. \nEu acho que ela está gostando também. Sempre tão ansiosa para iniciar uma conversa e aprender mais sobre a minha vida. \nNós certamente estamos nos aproximando muito ultimamente e não posso deixar de admirar sua beleza e charme. \nEla parece estar ficando mais confortável comigo também. A maneira como ela olha para mim, seus toques inocentes...") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade

    scene home_basement_c
    show debbie 2 at right
    show player 13 at left
    with dissolve
    deb "E obrigada novamente por isso, {b}[firstname]{/b}."
    deb "Eu realmente estive aproveitando nossas pequenas conversas."
    show debbie 1
    show player 14
    player_name "Sim eu também!"
    show player 13
    show debbie 13
    deb "Você tem sido uma grande ajuda recentemente..."
    deb "Você se importaria de pegar minha {b}loção{/b} , {b}No andar de cima{/b}?"
    deb "Minhas pernas estão um pouco secas."
    show debbie 1
    show player 12
    player_name "Onde no andar de cima?"
    show player 5
    show debbie 13
    deb "Basta olhar na {b}gaveta no meu quarto{/b}."
    deb "Deve estar lá."
    show debbie 1
    show player 14
    player_name "Ok, volto já!"
    hide player
    hide debbie
    with dissolve
    show popup_debbiebedroom at truecenter with dissolve
    pause
    hide popup_debbiebedroom with dissolve
    return

label laundry_dialogue_busy:
    show player 14
    player_name "Parece que está ocupada."
    player_name "Vou voltar mais tarde."
    return

label mom_lotion_fun:
    if M_mom.is_set("lotion fun"):
        if player.location == L_home_basement:
            scene home_basement_c

        elif player.location == L_home_kitchen:
            scene homekitchen_closeup
            if M_mom.is_set("sex available"):
                call expression game.dialog_select("mom_lotion_fun_kitchen_sex_available")
                $ player.remove_item("lotion")
                $ M_mom.set("fetch lotion", False)
                $ M_mom.set("retrieved lotion", False)

                pause
                $ M_mom.set("sex speed", .225)
                $ M_mom.set("sex flip", False)
                $ M_mom.set("robe on", True)
                $ first_pass = True
                $ animated = False
                jump expression game.dialog_select("mom_finger_loop")

        call expression game.dialog_select("mom_lotion_fun_pre")
        call expression game.dialog_select("mom_lotion_fun_location_dialogue")
        call expression game.dialog_select("mom_lotion_fun_location_dialogue_after")

        if player.location == L_home_basement:
            $ player.go_to(L_home_livingroom)
            scene home_livingroom_b with fade

        elif player.location == L_home_kitchen:
            $ player.go_to(L_home_entrance)
            scene expression L_home_entrance.background with fade

        call expression game.dialog_select("mom_lotion_fun_after")
    else:

        call expression game.dialog_select("mom_lotion_fun_first_pre")
        menu:
            "Ajude ela.":
                call expression game.dialog_select("mom_lotion_fun_first_help_her")
                $ player.go_to(L_home_livingroom)
                $ M_mom.set("lotion fun", True)
            "Sair.":

                call expression game.dialog_select("mom_lotion_fun_first_leave")

        $ M_mom.trigger(T_mom_lotion_applied)
    hide player
    hide debbie
    with dissolve
    $ player.remove_item("lotion")
    $ M_mom.set("fetch lotion", False)
    $ M_mom.set("retrieved lotion", False)

    $ game.timer.tick()
    $ game.main()

label mom_lotion_fun_kitchen_sex_available:
    show debbie 1 at right
    show player 485 at left
    with dissolve
    player_name "Aqui está, {b}[deb_name]{/b}!"
    show player 484
    show debbie 2
    deb "Obrigada querido."
    deb "Deixe-me apenas sentar no balcão para que você não tenha que se curvar."
    show debbie 183 with dissolve
    pause
    show debbie 184 zorder 2
    show debbie_robe 184f zorder 2
    with dissolve
    pause
    show debbie 185
    show debbie_robe 185j
    with dissolve
    pause
    hide player
    show player 487c zorder 1
    show player_arms 488 zorder 3
    with dissolve
    pause
    show player_arms 488b
    with dissolve
    pause
    show player_arms 488c_488d with dissolve
    show player 487g
    show debbie 185b
    deb "O isso faz cócegas!"
    show debbie 185g
    deb "Você gosta de cuidar de mim, não é?"
    show debbie 185f
    show player 487f
    player_name "Sim eu gosto muito de cuidar de você!"
    show player 487g
    show player_arms 488c_488d_488e with dissolve
    pause
    show debbie 185b
    deb "Eu diria que você é um menino tão bom..."
    deb "...Mas eu sei porque você gosta de fazer isso."
    show debbie 185f
    show player 487
    player_name "..."
    show debbie 185g
    deb "Você apenas gosta do pequeno show que eu te dou..."
    show debbie 185f
    show player 487g
    player_name "!!!"
    show debbie 185g
    deb "Sua pequena massagem me deixa com muito tesão."
    show debbie 185b
    show player 487d
    deb "Continue massageando, E talvez você possa me ajudar, Um pouco mais  em alguma coisa..."
    show debbie 185f
    show player 487f
    player_name "Sim, senhora!"
    show player 487g
    show debbie_robe 185k
    show player_arms 488e_488f
    with dissolve
    pause
    show debbie 185b
    deb "Isso é muito bom. Eu sou como manteiga nas suas mãos."
    hide player_arms
    show player 13 at Position (xoffset=-118)
    hide debbie_robe
    show debbie 189
    with dissolve
    deb "Até minhas roupas querem escorregar parece."
    show debbie 188
    show player 26 at Position (xoffset=-118)
    player_name "E quando sua calcinha saiu?"
    show player 13 at Position (xoffset=-118)
    show debbie 189
    deb "{b}*Risadinha*{/b}"
    show debbie 187
    deb "Eu me perguntei se você notaria."
    show debbie 189
    deb "Bem, então, você está disposto a tentar outra coisa?"
    show debbie 188
    show player 14 at Position (xoffset=-118)
    player_name "Claro!"
    show player 110f at Position (xoffset=-118)
    show debbie 191
    show debbie_robe 191b zorder 2
    with dissolve
    deb "Então seja um bom menino e use seus dedos para me fazer gozar..."
    show debbie 190
    show player 26 at Position (xoffset=-119)
    player_name "Sim, {b}[deb_name]{/b}."
    show player finger 193b zorder 3
    show debbie 192
    show debbie_robe 194b at right
    with dissolve
    return

label mom_lotion_fun_pre:
    show debbie 1 at right
    show player 485 at left
    with dissolve
    player_name "Consegui!"
    show player 484
    show debbie 2
    deb "Ótimo! Um segundo."
    show player 486
    show debbie 183 with dissolve
    pause
    show debbie 184b zorder 2
    show debbie_robe 184e zorder 2
    with dissolve
    deb "Pronto!"
    show player 484
    show debbie 185
    show debbie_robe 185h
    with dissolve
    pause
    hide player
    show player 487c zorder 1
    show player_arms 488 zorder 3
    with dissolve
    pause
    show player_arms 488b
    with dissolve
    show debbie 185d
    deb "Oh! Está frio."
    show player 487d
    deb "Esfregue a loção em suas mãos um pouco antes de aplicá-la."
    show player 487c
    show debbie 185
    show player_arms 488c_488d with dissolve
    show debbie 185b
    deb "Isso é bom."
    show debbie 185
    show player 487f
    show player_arms 488b with dissolve
    player_name "Bom!"
    show player 487g
    show player_arms 488c_488d with dissolve
    pause
    show player 487f
    show player_arms 488 with dissolve
    player_name "Em algum outro lugar?"
    show player 487g
    show debbie 185c
    deb "Hmm?"
    show player 487e
    player_name "Você quer que eu passe a loção em outro lugar?"
    show player 487d
    show debbie 185d
    deb "Oh..."
    show debbie 185g
    deb "Umm... Se você não se importa, você pode esfregar um pouco mais na minha perna..."
    show debbie 185f
    show player 487e
    player_name "O... Ok..."
    show player_arms 488b with dissolve
    show player 487c
    pause
    show player_arms 488c_488d_488e with dissolve
    show debbie 185d
    deb "Mmm... Cave suas mãos um pouco mais lá."
    show player_arms 488e with dissolve
    deb "Sinta esse nó?"
    deb "Tente e esfregue isso..."
    show debbie 185c
    show player 487b
    player_name "O... Ok..."
    show player 487c
    show player_arms 488e_488f with dissolve
    pause
    show debbie 185b
    deb "Mmm... Isso é bom."
    show debbie 185
    show player 487f
    player_name "!!!"
    show player 487g
    player_name "( Ela está realmente relaxando agora! )"
    player_name "( Eu me pergunto se ela percebe que eu posso ver através de sua calcinha! )"
    show debbie 185d
    deb "Ah, seus dedos são otimos."
    deb "Você tem praticado?"
    show debbie 185g
    deb "Alguma pequena senhora vai amar o quão prestativo e atencioso você é."
    show debbie 185d
    deb "Oh! Ali..."
    show debbie 185f
    pause
    show debbie_robe 185i with dissolve
    pause
    show debbie 185e
    deb "!!!"
    hide player_arms
    show player 3 at Position (xpos=420)
    show xtra 21 zorder 2 at Position (xpos=289)
    hide debbie_robe
    show debbie 187
    with dissolve
    deb "...Um... Obrigada docinho..."
    show debbie 186
    show player 29
    player_name "...De nada..."
    show player 3
    show debbie 187
    deb "Ouça, eu deveria ... hum..."
    return

label mom_lotion_fun_location_dialogue:
    if player.location == L_home_basement:
        deb "Eu provavelmente deveria terminar essa carga ... de roupas..."
        deb "Vá lá em cima... hum..."

    elif player.location == L_home_kitchen:
        deb "Eu provavelmente deveria terminar os pratos..."
    return

label mom_lotion_fun_location_dialogue_after:
    show debbie 186
    show player 29
    player_name "Sim ... eu estava quase pronto."
    show player 3
    show debbie 187
    deb "Obrigada ... mais uma vez, querido."
    show debbie 186
    show player 29
    player_name "De nada!."
    return

label mom_lotion_fun_after:
    show player 24 with dissolve
    player_name "Droga..."
    player_name "Eu acho que ela notou que eu estava olhando..."
    show player 34
    pause
    show player 35
    player_name "Ela estava ficando molhada!"
    show player 43
    pause
    show player 81 with dissolve
    pause
    show player 83
    player_name "É melhor eu encontrar outra coisa para fazer."
    return

label mom_lotion_fun_first_pre:
    scene home_basement_c
    show debbie 1 at right
    show player 485 at left
    with dissolve
    player_name "Eu tenho a sua {b}loção{/b}, {b}[deb_name]{/b}."
    show player 484
    show debbie 2
    deb "Oh, muito obrigada!"
    show debbie 8b
    deb "Ai!"
    show player 486
    pause
    show debbie 11b
    deb "Isso não vai funcionar!"
    deb "Realmente não é divertido envelhecer, {b}[firstname]{/b}. Eu não recomendo!"
    show debbie 10b
    return

label mom_lotion_fun_first_help_her:
    show player 485
    player_name "Você quer que eu te ajude?"
    show player 484
    show debbie 13
    deb "Hmm?"
    deb "Você quer dizer ... com minha loção?"
    show debbie 10b
    show player 485
    player_name "Bem, sim ... Se você quiser?"
    show player 484
    show debbie 11b
    deb "Você não se importaria?"
    show debbie 10b
    show player 485
    player_name "Claro que não! Eu ficaria muito feliz em ajudar!."
    player_name "Eu posso aplicar a loção e dar-lhe uma massagem de uma só vez!"
    player_name "Como isso soa?!"
    show player 484
    show debbie 14
    deb "..."
    show debbie 2
    deb "Isso parece maravilhoso, querido!"
    deb "Como uma garota poderia dizer não a uma massagem gratuita?"
    deb "Um segundo..."
    deb "... Deixe-me ficar confortável."
    show player 486
    show debbie 183 with dissolve
    pause
    show debbie 184 zorder 2
    show debbie_robe 184e zorder 2
    with dissolve
    show player 485
    player_name "Você disse que suas pernas estão secas?"
    show player 484
    show debbie 184b
    deb "Sim, elas sempre ficam secas nesta época do ano!"
    show debbie 184
    show player 485
    player_name "Ok."
    show player 484
    show debbie 185
    show debbie_robe 185h
    with dissolve
    pause
    hide player
    show player 487c zorder 1
    show player_arms 488 zorder 3
    with dissolve
    pause
    show player_arms 488b
    with dissolve
    player_name "( !!! )"
    show debbie 185c
    show player 487b
    player_name "Oops, Eu não esperava que saísse tão rápido!"
    show player 487d
    show debbie 185b
    deb "Heh."
    show debbie 185d
    deb "Está tudo bem querido. Há muito chão para cobrir!"
    show debbie 185
    show player 487b
    player_name "Ok."
    show player 487c
    show player_arms 488c_488d with dissolve
    show player 487
    show debbie 185d
    deb "Mmm, isso é legal..."
    show debbie 185
    show player 487c
    show player_arms 488b with dissolve
    player_name "..."
    show player_arms 488c_488d with dissolve
    pause
    show player_arms 488 with dissolve
    show player 487e
    player_name "Isso cuida da metade inferior."
    player_name "Você quer que eu faça, Na suas coxas também?"
    show player 487d
    show debbie 185b
    deb "... Sim, suponho. Contanto que você tenha certeza que não se importa?"
    show debbie 185
    show player 487b
    player_name "Not at all."
    show player 487c
    show player_arms 488b with dissolve
    pause
    show player_arms 488c_488d_488e with dissolve
    pause
    show debbie 185d
    deb "Mmm, você é muito bom nisso, {b}[firstname]{/b}..."
    show player_arms 488e with dissolve
    deb "Você pode esfregar um pouco mais se quiser."
    deb "Eu definitivamente tenho alguma tenssão armazenada nos meus músculos da coxa..."
    show debbie 185c
    show player 487b
    player_name "Sim, eu posso sentir isso."
    show player 487c
    show player_arms 488e_488f with dissolve
    pause
    show debbie 185b
    deb "Oh, Isso é o céu..."
    show debbie 185
    show player 487f
    player_name "( !!! )"
    show player 487g
    player_name "( Ela está muito relaxada agora! )"
    player_name "( Eu me pergunto se ela percebe que eu posso ver através de sua calcinha? )"
    show debbie 185d
    deb "Você tem mãos maravilhosas {b}[firstname]{/b}!"
    deb "Você deveria considerar se tornar um massagista..."
    show debbie 185g
    deb "Eu aposto que você faria uma fortuna!"
    show debbie 185d
    deb "Oh! Ali..."
    show debbie 185f
    pause
    show debbie_robe 185i with dissolve
    pause
    show debbie 185e
    deb "( !!! )"
    hide player_arms
    show player 3 at Position (xpos=420)
    show xtra 21 zorder 2 at Position (xpos=289)
    hide debbie_robe
    show debbie 187
    with dissolve
    deb "... Provavelmente é o suficiente. Posso terminar daqui."
    show debbie 186
    show player 29
    player_name "Você tem certeza?"
    show player 3
    show debbie 187
    deb "Por que você não vai para o andar de cima?"
    deb "Eu tenho que ficar de olho nessa lavanderia..."
    deb "... e pegar o secador."
    show debbie 186
    show player 29
    player_name "Sim, ok."
    show player 3
    show debbie 187
    deb "Obrigado novamente, querido."
    show debbie 186
    show player 29
    player_name "De nada"
    scene home_livingroom_b with fade
    show player 24 with dissolve
    player_name "Maldição..."
    player_name "Ela deve ter notado que eu estava espiando."
    show player 34
    pause
    show player 35
    player_name "Ela estava ficando excitada ou eu imaginei isso?"
    show player 43
    pause
    show player 81 with dissolve
    pause
    show player 83
    player_name "... Eu deveria tirar minha mente disso!"
    return

label mom_lotion_fun_first_leave:
    show player 485
    player_name "Algo mais, {b}[deb_name]{/b}?"
    show player 484
    show debbie 11b
    deb "Não, isso foi tudo."
    deb "Obrigado novamente por toda a ajuda, querido."
    show debbie 10b
    show player 485
    player_name "De nada, {b}[deb_name]{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
