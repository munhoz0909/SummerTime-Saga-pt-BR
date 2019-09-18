label right_tombstone:
    scene location_church_graveyard_tombstone01
    if M_aqua.is_state(S_aqua_graveyard_search):
        call expression game.dialog_select("right_tombstone_aqua_graveyard_search")
        $ M_aqua.trigger(T_aqua_tomb_engraving)
    else:

        pause
    $ game.main()

label right_tombstone_aqua_graveyard_search:
    player_name "( O nome desta pedra tumular é Ben Dover! )"
    player_name "( Isso tem que ser o único. )"
    player_name "( Mas agora que eu encontrei, eu não tenho certeza do que eu deveria estar procurando... )"
    player_name "Hmm..."
    player_name "( Talvez haja uma {b}pista{/b} em algum lugar? )"
    player_name "( Esta gravura se destaca... )"
    player_name "( Talvez eu deva procurar um grande {b}Sino{/b} em algum lugar da cidade? )"
    return

label stray_cat:
    scene location_church_graveyard_closeup
    if not M_player.is_set("found cat"):
        $ M_player.set("found cat", True)
        call expression game.dialog_select("stray_cat_first_pre")
        if player.has_item("cat_food"):
            call expression game.dialog_select("feed_cat")
            $ player.remove_item("cat_food")
            jump expression game.dialog_select("stray_cat_take_home")
        call expression game.dialog_select("stray_cat_first_after")

    elif not player.has_item("cat_food"):
        call expression game.dialog_select("stray_cat_no_food")

    elif player.has_item("cat_food"):
        call expression game.dialog_select("stray_cat_have_food_pre")
        $ player.remove_item("cat_food")
        menu stray_cat_take_home:
            "Levá-la para casa.":
                call expression game.dialog_select("stray_cat_have_food_take_her_pre")
                call screen cat_name_input
                if cat_name.strip() == "":
                    $ cat_name = "Pussywillow"
                $ cat = Character("[cat_name]", color = "#c87efe")
                call expression game.dialog_select("stray_cat_have_food_take_her_after")
                $ M_player.set("pet cat", True)
            "Deixe ela aqui.":

                call expression game.dialog_select("stray_cat_have_food_leave_her")

    hide cat
    hide player
    with dissolve
    $ game.main()

label stray_cat_first_pre:
    show player 11 at left with dissolve
    cat "Miau"
    show player 10
    player_name "Uhh, Olá"
    show player 11
    cat "Miau"
    show player 10
    player_name "De onde vem esse som?"
    cat "Groooour!"
    show player 11
    show cat 3 at Position(xpos=0.57, ypos=0.77) with dissolve
    pause
    show player 1
    pause
    show player 2
    player_name "Aww."
    player_name "Bem, e aé carinha."
    show player 1
    show cat 4
    cat "Brrrep"
    show player 2
    show cat 3
    player_name "O que você está fazendo aqui sozinho?"
    player_name "Você está perdido?"
    show player 1
    show cat 4
    cat "Brrrep"
    show player 2
    show cat 3
    player_name "Coitadinho."
    player_name "Eu não vejo um colarinho."
    show cat 3
    player_name "Deve ser um perdido..."
    player_name "Onde está seu dono em casa?"
    show player 1
    show cat 4
    cat "Groooour!"
    show player 11
    show cat 3
    pause
    show player 10
    player_name "Bem, qual é o problema?"
    show player 11
    show cat 4
    cat "Groooour!"
    show player 30
    show cat 3
    player_name "Hmm..."
    show player 2
    player_name "Oh, entendi!"
    player_name "Você é uma pequena dama, não é?!"
    show player 1
    show cat 4
    cat "Brrrep"
    show cat 5 with dissolve
    cat "Prrrr"
    show player 2
    player_name "Você parece está com fome."
    player_name "Você está com fome garota?"
    show player 1
    show cat 4
    cat "Miau"
    show player 2
    show cat 3
    return

label stray_cat_first_after:
    player_name "Hehe, tudo bem. Bem, talvez eu possa encontrar algo para você."
    show player 4
    show cat 3
    player_name "(Hmm.)"
    player_name "(Eu deveria ver como conseguir algo para ela comer.)"
    player_name "(Eu aposto que o Consum-r tem algo.)"
    return

label stray_cat_no_food:
    show player 1 at left
    show cat 3 at Position(xpos=0.57, ypos=0.77) with dissolve
    pause
    show cat 4
    cat "Miau"
    show player 2
    show cat 3
    player_name "Ah... Ainda com fome, né?"
    show player 1
    show cat 4
    cat "Brrrep"
    show player 2
    show cat 5
    player_name "Você é tão fofa!"
    player_name "Vou tentar encontrar algo para você comer, ok?"
    show player 1
    show cat 4
    cat "Prrrr"
    show player 2
    show cat 5
    player_name "Você espere aqui!"
    return

label stray_cat_have_food_pre:
    show player 1 at left with dissolve
    show cat 3 at Position(xpos=0.57, ypos=0.77) with dissolve
    pause
    show cat 4
    cat "Miau"
    show player 2
    show cat 3
    player_name "Olá novamente pequenina."
    show player 1
    show cat 4
    cat "Miau"
    show player 2
    show cat 3
    label feed_cat:
        player_name "Adivinha o que eu tenho para você?"
        show player 239_240
        pause
        hide player with dissolve
        show cplayer 1 at left with dissolve
        show cat 4
        cat "Brrrep"
        show cplayer 2
        show cat 3
        player_name "Está certo! Eu te trouxe algo gostoso!"
        show cat 4
        cat "Miau"
        hide cat with dissolve
        show cat 6 at Position(xpos=0.578, ypos=0.77) with dissolve
        pause



        hide cat with dissolve
        show cat 7 at Position(xpos=0.45, ypos=0.70) with dissolve
        player_name "!!!" with hpunch
        hide cplayer with dissolve
        hide cat with dissolve
        show cat 8 at left with dissolve
        pause
        show cat 9
        cat "Prrrr"
        show cat 10
        player_name "Hehe, isso mesmo."
        player_name "Aqui está e sua comida!"
        show cat 9
        cat "Brrrep"
        show cat 8

        scene black with fade
        scene location_church_graveyard_closeup with fade

        show cat 17 at left
        player_name "Uau, você realmente estava com muita fome, não estava?"
        show cat 18
        cat "Buuuuuurp!"
        show cat 17
        player_name "..."
        player_name "Haha, bem, estou feliz que tenha gostado disso..."
        hide cplayer with dissolve
        show player 2 at left
        show cat 3 at Position(xpos=0.57, ypos=0.77)
        with dissolve
        player_name "Agora está melhor não é menina?"
        show player 1
        show cat 4
        cat "Brrrep"
        show player 2
        show cat 5
        player_name "Você é tão doce."
        show player 4
        player_name "( Hmm... )"
        player_name "( Talvez eu deva te levar para casa comigo. )"
        player_name "( Eu não acho que {b}[deb_name]{/b} importaria... )"
    return

label stray_cat_have_food_take_her_pre:
    show player 2
    player_name "O que você diz garota?"
    player_name "Você quer voltar para casa comigo?"
    show player 1
    show cat 4
    cat "Brrrep!"
    hide cat with dissolve
    show cat 6 at Position(xpos=0.578, ypos=0.77) with dissolve
    pause
    hide cat with dissolve
    show cat 7 at Position(xpos=0.45, ypos=0.70) with dissolve
    player_name "!!!" with hpunch
    hide player
    hide cat
    with dissolve
    show cat 13 at left with dissolve
    pause
    show cat 16
    pause
    show cat 14
    player_name "Hehe, Ah..."
    show cat 15
    pause
    show cat 14
    player_name "Vou tomar isso como um sim!"
    show cat 12
    cat "Prrrr"
    show cat 14
    player_name "Bem, você vai precisar de um nome se vier para casa comigo..."
    return

label stray_cat_have_food_take_her_after:
    player_name "Então... [cat]?"
    player_name "Você gosta disso?"
    show cat 12
    cat "Miau"
    show cat 14
    player_name "hehe, tudo bem. [cat] é então!"
    show cat 15
    cat "Prrrr"
    show cat 16
    pause
    show cat 14
    player_name "Vamos lá [cat], Vamos para casa!"
    show popup_cat at truecenter with dissolve
    pause
    hide popup_cat with dissolve
    return

label stray_cat_have_food_leave_her:
    show player 10 at left
    show cat 5
    player_name "Hmm, Desculpe garota."
    player_name "Eu não acho que {b}[deb_name]{/b} ficaria muito feliz se eu te levasse para casa."
    show player 11
    show cat 4
    cat "Miau"
    show player 10
    show cat 5
    player_name "Pelo menos eu te dei um pouco de comida..."
    show player 11
    show cat 4
    cat "Brrrep"
    show player 10
    show cat 5
    player_name "Você é uma boa menina."
    player_name "Fique seguro, ok?"
    show player 11
    show cat 4
    cat "Miau"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
