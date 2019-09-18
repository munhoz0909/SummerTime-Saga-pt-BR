label mia_bedroom:
    if M_jenny.is_state(S_jenny_spy_on_mia_telescope) and game.timer.is_morning():
        hide screen telescope
        hide screen telescope_fake
        call expression game.dialog_select("telescope_mia_sister_spying")
        $ persistent.cookie_jar["Mia"]["unlocked"] = True
        $ persistent.cookie_jar["Mia"]["gallery"]["02_unlocked"] = True
        $ M_jenny.trigger(T_jenny_spied_on_mia)
        jump expression game.dialog_select("bedroom_dialogue")
    else:
        call expression game.dialog_select(game.telescope.mia)

    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_mia_sister_spying:
    scene telescope_mia_masturbate with dissolve
    pause
    player_name "Ela provavelmente está apenas se preparando para"
    player_name "!!!"
    pause
    player_name "Uau!!"
    scene expression "backgrounds/location_home_bedroom_caught_01.jpg" with dissolve
    player_name "Ela está se masturbando!"
    scene expression "backgrounds/location_home_bedroom_caught_02.jpg" with dissolve
    pause
    scene expression "backgrounds/location_home_bedroom_caught_03.jpg" with dissolve
    player_name "Eu me pergunto o que ela está pensando?"
    scene expression "backgrounds/location_home_bedroom_caught_04.jpg" with dissolve
    pause
    scene expression "backgrounds/location_home_bedroom_telescope_window.jpg"
    show player b_telescope_peeking a_empty f_empty
    with dissolve
    pause
    show jenny b_telescope_standing a_empty f_telescope_standing_grin zorder 1 with dissolve
    pause
    jen "{b}*Ahem*{/b}"
    show player b_telescope_peeking_caught
    player_name "!!!" with hpunch
    show player b_telescope f_telescope_surprised
    with dissolve
    show jenny f_telescope_standing_grin_talk
    jen "O que você está fazendo?"
    show jenny f_telescope_standing_grin
    show player f_telescope_worried_talk
    player_name "Nada..."
    show player f_telescope_worried
    show jenny f_telescope_standing_grin_talk
    jen "Você está pervertendo nos vizinhos?"
    show jenny f_telescope_standing_grin
    show player f_telescope_surprised
    player_name "..."
    show jenny f_telescope_standing_grin_talk
    jen "Deixe-me ver!"
    show jenny f_telescope_standing_grin
    show player f_telescope_worried_talk
    player_name "Você não precisa"
    show player f_telescope_surprised
    show jenny f_telescope_standing_grin_talk
    jen "Vou da uma olhadinha!"
    show jenny b_telescope_look f_empty a_empty
    show player b_telescope_laying_back a_telescope_side f_telescope_lay_surprised zorder 0 at Position (yoffset=40)
    with dissolve
    pause
    show jenny f_telescope_laugh b_telescope a_telescope_down with dissolve
    jen "Hehe, essa é a garota super religiosa com quem você está sempre por perto?"
    show jenny f_telescope_normal
    show player f_telescope_lay_worried_talk at Position (yoffset=40)
    player_name "{b}Mia{/b} ela não é super religiosa..."
    show player f_telescope_lay_worried at Position (yoffset=40)
    show jenny f_empty b_telescope_look a_empty with dissolve
    pause
    show player f_telescope_lay_worried_talk at Position (yoffset=40)
    player_name "...mais Sua família é bastante."
    show player f_telescope_lay_worried at Position (yoffset=40)
    jen "Hã."
    pause
    jen "Ela está fazendo um belo  show lá."
    player_name "..."
    show jenny f_telescope_normal_talk b_telescope a_telescope_down with dissolve
    jen "Aposto que te excita, né?"
    show jenny f_telescope_normal
    show player f_telescope_lay_worried_talk at Position (yoffset=40)
    player_name "O que?!"
    show player f_telescope_lay_surprised_teeth at Position (yoffset=40)
    show jenny f_telescope_laugh
    jen "Você sabe, vendo o pequeno bumbum da bíblia esfregar sua framboesa!"
    show jenny f_telescope_normal
    pause
    show jenny f_telescope_normal_talk
    jen "Isso te deixa excitado?"
    show jenny f_telescope_normal
    if M_jenny.get("dominance") <= 0:
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Eu não"
        player_name "Do que você está falando?"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Mostre-me."
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Você não quer dizer..."
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Vamos lá, quero ver!"
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "... Mesmo?"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "você me viu nua uma dúzia de vezes..."
        jen "Deixar de ser um perdedor e me mostre!"
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Ok."
        show player a_telescope_pull1 f_telescope_lay_shy_down at Position (yoffset=40) with dissolve
        pause
        show player a_telescope_pull2 at Position (yoffset=40) with dissolve
        pause
        show player a_telescope_pull3 f_telescope_lay_worried at Position (yoffset=40) with dissolve
        show jenny f_telescope_surprised
        jen "PUTA MERDA..."
        jen "Como você anda com essa coisa o dia todo?"
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Umm, Não sei."
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_laugh a_telescope_up with dissolve
        jen "É como um taco de beisebol da liga!"
        show jenny a_telescope_touch with dissolve
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "O que você quis dizer?"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Cale a boca!"
        show jenny f_telescope_normal_down a_telescope_pushing
        show player a_telescope_pushed f_telescope_lay_shy_down at Position (yoffset=40)
        with dissolve
        show jenny a_telescope_pushing_after
        show player a_telescope_springing at Position (yoffset=40)
        with dissolve
        pause
        show player a_telescope_pull3 f_telescope_lay_worried at Position (yoffset=40) with dissolve
        show jenny f_telescope_laugh
        jen "Hahahaah!"
        show jenny f_telescope_normal_down a_telescope_down with dissolve
        pause
        show jenny f_telescope_normal_talk
        jen "Eu não posso acreditar que você está bem equipado..."
        show jenny f_telescope_normal_down
        pause
        show jenny f_telescope_normal_talk
        jen "Eu acho que não tenho que me preocupar, Com você ficar envergonhado na frente de uma câmera."
        show jenny f_telescope_normal_down
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "O que você quer dizer?"
        show player f_telescope_lay_worried at Position (yoffset=40)
        pause
        show jenny f_telescope_normal_talk
        jen "Você quer fazer coisas comigo, não é?"
        show jenny f_telescope_angry
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "O QUE?!" with hpunch
        show player f_telescope_lay_surprised_teeth at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Não negue isso."
        jen "Por que outro motivo você estaria me espiando no chuveiro, Ou pagando para me ver nua?"
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Isso não é verdade"
        player_name "Quer dizer, não podemos"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Ahh, Cale-se!"
        jen "Você tem sorte de eu estar considerando isso..."
        show jenny f_telescope_normal
        pause
        show jenny f_telescope_normal_down
        pause
        show jenny f_telescope_normal_talk
        jen "{b}*Suspiro*{/b} Tudo bem, venha para {b}meu quarto esta tarde{/b}."
        show jenny b_telescope_standing a_empty f_telescope_standing_grin with dissolve
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Hã?"
        player_name "O que nós vamos fazer?"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_standing_grin_talk
        jen "Você vai fazer o que eu mandar."
        jen "Nada mais nada menos."
        show jenny f_telescope_standing_grin
        pause
        show jenny f_telescope_standing_grin_talk
        jen "Coloque essa coisa para dentro das calças. Você parece ridículo."
        show player f_telescope_lay_surprised at Position (yoffset=40)
        hide jenny with dissolve
        player_name "..."
    else:
        show player f_telescope_lay_skeptical_talk at Position (yoffset=40)
        player_name "Você realmente acabou de me perguntar isso?"
        show player f_telescope_lay_skeptical at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Mostre-me."
        show jenny f_telescope_normal
        show player f_telescope_lay_surprised at Position (yoffset=40)
        player_name "..."
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Você quer que eu te mostre meu pau?"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Está certo."
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Por que você está  interessada?"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Quem disse que eu estava interessada?!"
        show jenny f_telescope_normal
        show player f_telescope_lay_squint at Position (yoffset=40)
        pause
        show player f_telescope_lay_skeptical_talk at Position (yoffset=40)
        player_name "Bem, se você não está interessada, então eu não vou mostrar"
        show player f_telescope_lay_skeptical at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Tudo bem, tudo bem ... Droga, estou interessada."
        jen "Apenas me mostre já, sheesh!"
        show jenny f_telescope_normal
        show player f_telescope_lay_skeptical_talk at Position (yoffset=40)
        player_name "està bem."
        show player a_telescope_pull1 f_telescope_lay_shy_down at Position (yoffset=40) with dissolve
        pause
        show player a_telescope_pull2 at Position (yoffset=40) with dissolve
        pause
        show player a_telescope_pull3 f_telescope_lay_worried at Position (yoffset=40) with dissolve
        show jenny f_telescope_surprised
        jen "PUTA MERDA..."
        jen "Como você anda com essa coisa o dia todo?"
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Umm, Não sei."
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_laugh a_telescope_up with dissolve
        jen "É como um taco de beisebol da liga!"
        show jenny a_telescope_touch with dissolve
        show player f_telescope_lay_skeptical_talk at Position (yoffset=40)
        player_name "Ei, quem disse que você poderia tocar?!"
        show player f_telescope_lay_skeptical at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Pfft, Eu deixo você me tocar..."
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Mais você não deixa tocar graça!"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Cale a boca!"
        show jenny f_telescope_normal_down a_telescope_pushing
        show player a_telescope_pushed f_telescope_lay_shy_down at Position (yoffset=40)
        with dissolve
        show jenny a_telescope_pushing_after
        show player a_telescope_springing at Position (yoffset=40)
        with dissolve
        pause
        show player a_telescope_pull3 f_telescope_lay_worried at Position (yoffset=40) with dissolve
        show jenny f_telescope_laugh
        jen "Hahahaah!"
        show jenny f_telescope_normal_down a_telescope_down with dissolve
        pause
        show jenny f_telescope_normal_talk
        jen "Eu não posso acreditar que você está bem equipado..."
        show jenny f_telescope_normal_down
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Bem, se você diz."
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Eu aposto que você não seria tímido sobre as pessoas verem isso, né?"
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Eu não sei, provavelmente não..."
        player_name "Por quê?"
        show player f_telescope_lay_worried at Position (yoffset=40)
        pause
        show jenny f_telescope_normal_talk
        jen "Você quer fazer coisas comigo, não é?"
        show jenny f_telescope_angry
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Que tipo de coisa?"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Não seja tolo, você sabe do que estou falando!"
        show jenny f_telescope_normal
        player_name "..."
        show jenny f_telescope_normal_talk
        jen "Por que outro motivo você estaria me espiando no chuveiro ou pagando para me ver nua?"
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Bem, você tem um corpo legal ... eu gosto disso."
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Bem deixe me pensar."
        jen "E eu suponho ... Você tem um bom pau."
        show jenny f_telescope_normal_down
        show player f_telescope_lay_skeptical_talk at Position (yoffset=40)
        player_name "Você gostou nè."
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_laugh
        jen "Pena que está preso a um perdedor como você."
        show jenny f_telescope_normal
        show player f_telescope_lay_skeptical_talk at Position (yoffset=40)
        player_name "... E aí você começa."
        player_name "Sempre com os comentários mal-intencionados..."
        show player f_telescope_lay_skeptical at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Tanto faz."
        jen "Apenas venha para {b}meu quarto esta tarde{/b}."
        jen "Eu tenho uma proposta para você."
        show jenny f_telescope_normal
        show player f_telescope_lay_skeptical_talk at Position (yoffset=40)
        player_name "Sim, está bem."
        show player f_telescope_lay_skeptical at Position (yoffset=40)
        show jenny f_telescope_normal_down
        pause
        show jenny f_telescope_normal_talk
        jen "Eu não posso acreditar que estou considerando isso..."
        show jenny f_telescope_normal
        pause
        show jenny b_telescope_standing a_empty f_telescope_standing_grin_talk with dissolve
        jen "Coloque essa coisa para dentro das calças. Você parece ridículo."
        show jenny f_telescope_standing_grin
        show player f_telescope_lay_skeptical_talk at Position (yoffset=40)
        player_name "Dane-se."
        show player f_telescope_lay_skeptical at Position (yoffset=40)
        hide jenny with dissolve
        jen "Haha!"
    scene expression game.timer.image("bedroom{}") with None
    show player 5 with dissolve
    player_name "( Isso foi estranho. )"
    player_name "( Eu não posso acreditar que ela pediu para ver meu pau. )"
    player_name "( É ela ainda tocou nele! )"
    pause
    show player 4 with dissolve
    player_name "( Hmm, Eu me pergunto o que ela está planejando {b}no quarto dela{/b}? )"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Mia"]["unlocked"] = True
    $ persistent.cookie_jar["Mia"]["gallery"]["02_unlocked"] = True
    return

label telescope_mia_morning_1:
    scene windowmiamorning01
    if game.timer.dayOfWeek() == "Sun":
        player_name "( Ela está se preparando para a igreja. )"
    elif game.timer.is_weekend():
        player_name "( Eu me pergunto o que ela está fazendo hoje? )"
    else:
        player_name "( Ela está se preparando para a escola. )"
    return

label telescope_mia_morning_2:
    scene windowmiamorning02
    player_name "( Tarde demais ... Eu sempre perco a melhor parte! )"
    return

label telescope_mia_afternoon_1:
    scene windowmiaday 1
    player_name "( Suas cortinas estão fechadas. Ela provavelmente não está em casa. )"
    return

label telescope_mia_afternoon_2:
    scene windowmiaday 2
    player_name "( Ela não está em casa. )"
    return

label telescope_mia_night_1:
    scene windowmianight01
    player_name "( Ela está sempre lendo ou estudando... )"
    return

label telescope_mia_night_2:
    if not M_mia.get("telescope teddy seen"):
        $ persistent.cookie_jar["Mia"]["unlocked"] = True
        $ persistent.cookie_jar["Mia"]["gallery"]["01_unlocked"] = True
        $ M_mia.set("telescope teddy seen", True)
        scene windowmianight03a_b
        player_name "( O que ela está fazendo? )"
        player_name "..."
        player_name "( Ela é... )"
        player_name "( ...humping ela {b}Urso Teddy{/b}? )"
        player_name "( Uau Puta Merda.. )"
        player_name "( Isso é muito excitante )"
        scene windowmianight03c with hpunch
        player_name "!!!"
        scene windowmianight03d
        player_name "( Ai droga! )"
        player_name "( Eu acho que ela acabou de ser pega... )"
        player_name "( A {b}Mãe{/b} dela deve estar furiosa ... Ela é sempre tão rigorosa com ela... )"
        $ renpy.end_replay()
    else:
        call telescope_mia_night_3
    return

label telescope_mia_night_3:
    scene windowmianight02
    player_name "( Ela deve estar dormindo. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
