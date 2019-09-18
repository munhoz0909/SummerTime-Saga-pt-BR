label hide_home_tv:
    hide home_tv_channel_01
    hide home_tv_channel_02
    hide home_tv_channel_03
    hide home_tv_channel_04
    hide home_tv_channel_05
    hide home_tv_channel_06
    hide home_tv_channel_07
    hide home_tv_channel_08
    hide home_tv_channel_09
    hide home_tv_channel_10
    return

label cant_watch_porn_during_day:
    player_name "( Eu não posso assistir pornografia durante o dia! )"
    player_name "( {b}[deb_name]{/b} poderia me pegar. )"
    player_name "( Eu {b}NÃO{/b} estou tendo essa conversa {i}novamente{/i}... )"
    return

label home_livingroom_tv:
    if M_player.get("masturbated tv"):
        if M_jenny.get("had_couch_sex"):
            call expression game.dialog_select("home_livingroom_tv_masturbated_tv_sis")
        else:
            call expression game.dialog_select("home_livingroom_tv_masturbated_tv")
        jump expression game.dialog_select("home_livingroom_dialogue")
    $ tv_channel = 0
    jump expression game.dialog_select("tv_channel_responses")

label home_livingroom_tv_locked:
    scene expression game.timer.image("home_livingroom{}_b") with None
    show popup_tv_locked at truecenter with dissolve
    pause
    hide popup_tv_locked with dissolve
    $ game.main()

label home_livingroom_tv_masturbated_tv_sis:
    scene home_livingroom_night_b with None
    show player 11
    with dissolve
    player_name "( Eu não estou arriscando isso de novo, esta noite... )"
    player_name "( eu deveria ir para a cama. )"
    hide player with dissolve
    hide home_livingroom_night_b
    return

label home_livingroom_tv_masturbated_tv:
    scene home_livingroom_night_b with None
    show player 11
    with dissolve
    player_name "( Eu acho que é o suficiente por uma noite. )"
    player_name "( eu deveria ir para a cama. )"
    hide player with dissolve
    hide home_livingroom_night_b
    return

label tv_channel_responses:
    scene home_livingroom_tv
    $ pink_user = ""
    $ pink_pass = ""
    if tv_channel == -1:
        $ tv_channel = 7
    elif tv_channel == 8:
        $ tv_channel = 0
    if tv_channel in range(7) and tv_channel not in game.seen_tv_channels:
        $ renpy.call(game.dialog_select("tv_channel_channel_0{}_first_view".format(tv_channel+1)))
        $ game.seen_tv_channels.append(tv_channel)

    elif tv_channel == 7:
        if game.timer.is_day():
            call cant_watch_porn_during_day
            call hide_home_tv
            $ game.main()
        elif not M_jenny.finished_state(S_jenny_figure_out_password):
            call sis_pink_pass
            call hide_home_tv
            $ game.main()
        elif game.timer.is_evening():
            $ tv_pink_channel = 8
        elif M_jenny.finished_state(S_jenny_catch_her_jilling):
            $ tv_pink_channel = renpy.random.randint(7,8)
        else:
            $ tv_pink_channel = 7

        if tv_pink_channel in (7, 8) and not tv_channel_pink:
            call expression game.dialog_select("tv_channel_pink_intro")
            if tv_pink_channel == 7:
                show home_tv_channel_09 at Position(xpos=522, ypos=521)
            elif tv_pink_channel == 8:
                show home_tv_channel_10 at Position(xpos=522, ypos=521)
            if game.timer.is_evening():
                if M_jenny.get("force_couch_sex"):
                    $ rn = 50
                else:
                    $ rn = random.randint(1, 100)
                if rn <= 40:
                    call expression game.dialog_select("tv_channel_channel_08_finishes_himself")
                elif rn <= 80 and M_jenny.finished_state(S_jenny_catch_her_jilling):
                    call expression game.dialog_select("tv_channel_channel_08_jenny_interrupts")
                else:
                    call expression game.dialog_select("tv_channel_channel_08_mom_interrupts")
                $ M_player.set("masturbated tv", True)
                $ game.timer.tick()
                jump expression game.dialog_select("home_livingroom_dialogue")

        elif 8 not in game.seen_tv_channels:
            show home_tv_channel_08 at Position(xpos=522, ypos=522)
            call expression game.dialog_select("sis_pink_pass")
            $ tv_channel = 7
            $ game.seen_tv_channels.append(8)

    call hide_home_tv
    call screen home_livingroom_tv

label tv_channel_pink_intro:
    scene home_livingroom_tv
    show home_tv_channel_09 at Position(xpos=522, ypos=521) with dissolve
    player_name "( Oh, lésbicas! )"
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show player b_couch_sit_watching f_couch_sit_watching_straight a_couch_boner_covered
    player_name "( Todo mundo está dormindo ... Esta é a oportunidade perfeita para esfregar meu pau! )"
    show player a_couch_boner_pull1 with dissolve
    pause
    show player a_couch_boner_pull2 with dissolve
    show player a_couch_boner with dissolve
    pause
    show player a_couch_boner_jerk with dissolve
    player_name "( Porra essas gorotas são sexy! )"
    pause
    pause
    show player f_couch_sit_watching_jerking
    player_name "( Eu não vou durar muito tempo! )"
    pause
    return

label tv_channel_sis_couch03_started:
    scene home_livingroom_couch01 with None
    show playersex 82 at Position(xpos=497)
    with dissolve
    player_name "Vamos ver o que está passando na TV..."

    scene home_livingroom_tv
    show home_tv_channel_08 at Position(xpos = 522, ypos = 521)
    player_name "( Alguém deixou no Canal Rosa? )"
    player_name "A senha foi aceita..."
    pause .4
    show text "{color=#ff4bdf}L6bv12R{/color}" as username at Position(xpos = 433, ypos = 341)
    pause .4
    show text "{color=#ff4bdf}12345{/color}" as password at Position(xpos = 423, ypos = 411)
    pause 1
    hide username
    hide password
    show home_tv_channel_10 at Position(xpos = 522, ypos = 521)
    player_name "Uau!"
    player_name "( Eu nunca vi alguém usar seus pés como {b}that{/b}. )"
    player_name "( Na verdade, isso é meio quente. )"
    return

label tv_channel_channel_01_first_view:
    show home_tv_channel_01 at Position(xpos=522, ypos=521)
    player_name "Hmm... Vamos ver o que está passando na TV."
    return

label tv_channel_channel_02_first_view:
    show home_tv_channel_02 at Position(xpos=522, ypos=521)
    player_name "( Notícias locais. Chato! )"
    return

label tv_channel_channel_03_first_view:
    show home_tv_channel_03 at Position(xpos=522, ypos=521)
    player_name "( Esse é o tipo de esporte que eu poderia entrar. )"
    return

label tv_channel_channel_04_first_view:
    show home_tv_channel_04 at Position(xpos=522, ypos=521)
    player_name "( Ei, é o prefeito Rump! )"
    return

label tv_channel_channel_05_first_view:
    show home_tv_channel_05 at Position(xpos=522, ypos=521)
    player_name "..."
    player_name "( Esses canais da natureza são tão estranhos... )"
    return

label tv_channel_channel_06_first_view:
    show home_tv_channel_06 at Position(xpos=522, ypos=521)
    player_name "( Quem assiste essas coisas? )"
    return

label tv_channel_channel_07_first_view:
    show home_tv_channel_07 at Position(xpos=522, ypos=521)
    player_name "( Este canal é um fracasso. )"
    return

label tv_channel_channel_08_mom_interrupts:
    scene home_livingroom_couch02
    show player b_couch_sit_watching f_couch_sit_watching_jerking a_couch_boner_jerk
    with fade
    deb "{b}[firstname]{/b}?"
    show player b_couch_sit f_couch_sit_down_surprised a_couch_boner_jerk1 with dissolve
    player_name "( Oh, porcaria! )"
    show player f_couch_sit_right_talk
    player_name "( {b}[deb_name]{/b} está vindo! )"
    show debbie 126 at Position (xpos=917,ypos=694)
    show player 303 at left
    with dissolve
    deb "Tem alguém aqui fora?!"
    show debbie 127 at Position (xpos=872,ypos=540) with dissolve
    deb "Olá?!"
    deb "Deixaram a tv ligada"
    show debbie 128 at Position (xpos=862,ypos=511) with dissolve
    deb "!!!"
    show debbie 132 at Position (xpos=680,ypos=768) with dissolve
    deb "Oh, meu deus."
    pause
    deb "Que mundo é esse!"
    pause
    deb "Uau, eles estão realmente fazendo essas coisas!..."
    pause
    deb "Eu não deveria estar assistindo isso!"
    deb "{b}[firstname]{/b} e {b}[jen_name]{/b} poderia entrar aqui a qualquer segundo!"
    show debbie 133 at Position (xpos=812,ypos=767) with dissolve
    pause
    hide debbie with dissolve
    pause
    scene expression player.location.background_closeup with None
    show player f_worried_talk
    player_name "Essa foi por pouco!"
    player_name "É melhor eu ir para a cama..."
    hide player with dissolve
    hide home_livingroom_couch01
    return

label tv_channel_channel_08_finishes_himself:
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show player b_couch_sit_watching f_couch_sit_watching_jerking a_couch_boner_jerk1
    player_name "HNNGGG!!!" with flash
    show player o_couch_boner_cum
    pause
    player_name "( Ufa, isso foi ótimo! )"
    show player f_couch_sit_watching_straight
    pause
    player_name "( Eu acho que é melhor eu ir e me limpar. )"
    hide player with dissolve
    return

label tv_channel_channel_08_jenny_interrupts:
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show player b_couch_sit_watching f_couch_sit_watching_jerking a_couch_boner_jerk
    show jenny b_couch_behind a_empty f_empty
    with fade
    jen "AHHHH, pervertido!"
    show player f_couch_sit_down_surprised b_couch_sit a_couch_boner
    player_name "!!!" with hpunch
    show player f_couch_sit_right_talk a_couch_boner_covered_shirt with dissolve
    player_name "Você me assustou!"
    show player f_couch_sit_right
    if M_diane.finished_state(S_diane_couch_crashing):
        jen "Onde está a {b}Diane{/b}?"
        show player f_couch_sit_right_talk
        player_name "Eu não sei, ela deve estar trabalhando até tarde ou algo assim..."
        show player f_couch_sit_right
    show jenny b_couch_sit f_couch_sit_upset_talk a_couch_rest with dissolve
    jen "Quem disse que você poderia usar meu {b}Canal rosa{/b} ,Essa e minha conta?"
    show jenny f_couch_sit_upset
    show player f_couch_sit_right_talk
    player_name "Eu não achei que você se importaria"
    show player f_couch_sit_right
    show jenny f_couch_sit_upset_talk
    jen "Ugh, lésbicas..."
    show jenny f_couch_sit_grin_talk
    jen "Você não acha isso meio chato?"
    show jenny f_couch_sit_grin
    show player f_couch_sit_right_talk
    player_name "Na verdade não."
    show player f_couch_sit_right
    show jenny f_couch_sit_grin_talk
    jen "Parece meio sem sentido quando não há pau envolvido..."
    show jenny f_couch_sit_grin
    player_name "..."
    show jenny f_couch_sit_surprised
    jen "Oh meu deus, você está gostando?!"
    show jenny f_couch_sit_sexy
    show player f_couch_sit_right_talk
    player_name "Não..."
    show player f_couch_sit_right
    show jenny f_couch_sit_sexy_talk
    jen "Sim você tá."
    show jenny f_couch_sit_laugh
    jen "Olhe para o seu pau, está ereto!"
    show jenny f_couch_sit_sexy
    pause
    show jenny f_couch_sit_sexy_talk
    jen "Você sabe, se você me pedir ... eu poderia te ajudar com isso."
    show jenny f_couch_sit_sexy
    show player f_couch_sit_right_talk
    player_name "Mesmo?"
    show player f_couch_sit_right
    show jenny f_couch_sit_sexy_talk
    jen "Sim, mas só se você me implorar por isso."
    show jenny f_couch_sit_sexy
    if M_jenny.get("dominance") <= 0:
        player_name "..."
        show player f_couch_sit_right_talk
        player_name "Por favor?"
        show player f_couch_sit_right
        show jenny f_couch_sit_eyeroll
        jen "Oh vamos lá, isso foi patético!"
        show jenny f_couch_sit_sexy
        player_name "..."
        show jenny f_couch_sit_sexy_talk
        jen "Diga isso:"
        jen "Por favor, {b}Princesa [jen_name]{/b}."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "Por favor, {b}Princesa [jen_name]{/b}."
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk
        jen "Eu sou, apenas um perdedor patético..."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "{b}*Suspiro*{/b} Eu sou, apenas um perdedor patético..."
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk
        jen "... Não sou digno dos seus pés."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "... Não sou digno dos seus pés."
        show player f_couch_sit_right
        show jenny f_couch_sit_laugh
        jen "Hahahaah!"
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "Shh, você vai acordar {b}[deb_name]{/b}!"
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk
        jen "Sim, sim ... Tudo bem, tire isso, perdedor."
        show jenny f_couch_sit_sexy_down
        show player a_couch_boner with dissolve
        pause
        show player f_couch_sit_down a_couch_sides
        $ M_jenny.set('sex speed', .3)
        show jenny a_empty
        show expression AnimatedImage("jenny_couch_dick_rub", [1,2,3], M_jenny) as jenny_couch_dick_rub zorder 3 at Position(xalign = 0.0, yoffset = 0)
        with dissolve
    else:
        show player f_couch_sit_right_talk
        player_name "Dane-se!"
        show player f_couch_sit_right
        show jenny f_couch_sit_upset_talk
        jen "O que?!"
        show jenny f_couch_sit_upset
        show player f_couch_sit_right_talk
        player_name "Eu não vou te implorar por nada, Na verdade você quer isso tanto quanto eu!"
        show player f_couch_sit_right
        show jenny f_couch_sit_angry_talk
        jen "Não fale comigo assim!"
        show jenny f_couch_sit_angry
        show player f_couch_sit_right_talk
        player_name "Shh, você vai acordar {b}[deb_name]{/b}!"
        show player f_couch_sit_right
        jen "Grr!"
        show player a_couch_boner with dissolve
        show player f_couch_sit_right_talk
        player_name "Apenas vá embora e me deixe terminar."
        show player f_couch_sit_right
        show jenny f_couch_sit_angry_pouting
        jen "..."
        show jenny f_couch_sit_upset_talk
        jen "Você é tão idiota!"
        show jenny f_couch_sit_upset
        player_name "Você é quem está tentando me fazer implorar por isso!"
        show jenny f_couch_sit_upset_talk
        jen "Tanto faz."
        show jenny f_couch_sit_gross_down
        pause
        show jenny f_couch_sit_upset_talk
        jen "{b}*Suspiro*{/b} Aqui..."
        show jenny f_couch_sit_sexy_down
        show player f_couch_sit_down_talk a_couch_sides
        $ M_jenny.set('sex speed', .3)
        show jenny a_empty
        show expression AnimatedImage("jenny_couch_dick_rub", [1,2,3], M_jenny) as jenny_couch_dick_rub zorder 3 at Position(xalign = 0.0, yoffset = 0)
        player_name "!!!" with hpunch
        player_name "Eu pensei que você não queria!"
        show player f_couch_sit_down
        show jenny f_couch_sit_sexy_talk_down
        jen "Just shut up!"
        jen "Eu fiquei o tempo todo aqui, eu poderia muito bem ter um pouco de diversão."
        show jenny f_couch_sit_sexy_down
        pause
    show jenny f_couch_sit_sexy_talk_down
    jen "Como se sente?"
    show jenny f_couch_sit_sexy_down
    show player f_couch_sit_down_talk
    player_name "Tão bom!"
    show player f_couch_sit_down
    pause
    show jenny f_couch_sit_sexy_talk_down
    jen "Você é tão pervertido, sabe disso?"
    jen "No meus pés?"
    show jenny f_couch_sit_sexy_down
    show player f_couch_sit_down_talk
    player_name "Esta foi a sua ideia..."
    show player f_couch_sit_down
    show jenny f_couch_sit_laugh
    jen "Hahahaah!"
    show jenny f_couch_sit_sexy_down
    $ M_player.set("masturbated tv", True)
    jump jenny_couch_fj_loop
    return

label sis_pink_pass:
    scene home_livingroom_tv
    show home_tv_channel_08 at Position(xpos=522, ypos=521) with dissolve
    player_name "( Cara, eu gostaria de poder acessar este canal. )"
    pause
    player_name "( {b}[jen_name]{/b} assiste muito pornô... )"
    player_name "( Gostaria de saber se {b}ela tem uma assinatura{/b}? )"
    return

label tv_pink_channel_pass_check:
    if M_jenny.finished_state(S_jenny_figure_out_password):
        if pink_user.lower().strip() == "l6bv12r" and pink_pass.strip() == "12345":
            $ tv_channel_pink = False
            player_name "( !!! )"
            player_name "( It worked! )"
            pause
        else:
            show home_tv_channel_08 at Position(xpos=522, ypos=522)
            show jenny_wrong_pass at Position(xpos=520, ypos= 510) with dissolve
            pause 1
            hide jenny_wrong_pass with dissolve
            $ game.main()
        jump expression game.dialog_select("tv_channel_responses")
    else:
        call sis_pink_pass
        $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
