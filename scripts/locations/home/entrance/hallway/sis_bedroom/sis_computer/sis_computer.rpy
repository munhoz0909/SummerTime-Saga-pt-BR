label pass_check:
    if sis_pass.lower().strip() == "bad monster" or sis_pass.lower().strip() == "badmonster":
        scene jenny_comp
        $ M_jenny.set("comp locked", False)
        if not sispc_desktop_seen:
            show screen sis_computer
            player_name "( Consegui! )"
            player_name "( Tudo bem, agora vamos ver o que ela tem feito... )"
            call screen sis_computer
        $ sispc_desktop_seen = True
    else:

        scene jenny_comp
        show jenny_wrong_pass at Position(xpos=570, ypos= 448) with dissolve
        $ renpy.pause()
        hide jenny_wrong_pass with dissolve
    call screen sis_computer

label upstairs_bedroom_enter_laptop:
    if L_home_sisbedroom.is_here(M_jenny) and not game.timer.is_night():
        call expression game.dialog_select("jenny_bedroom_cannot_snoop")
        $ game.main()
    if not M_jenny.finished_state(S_jenny_snoop_around_for_laptop) or M_jenny.is_state(S_jenny_snoop_around_for_laptop):
        call expression game.dialog_select("jenny_bedroom_no_password")
        $ game.main()
    if M_jenny.is_state(S_jenny_check_laptop) and game.timer.is_dark():
        call expression game.dialog_select("jenny_bedroom_no_password")
        $ game.main()
    if M_jenny.is_state(S_jenny_check_laptop) and game.timer.is_day():
        scene expression "backgrounds/location_computer_jenny_01.jpg"
        player_name "( Ahh porcaria, está trancado. )"
        player_name "( Preciso da senha dela! )"
        scene expression player.location.background_closeup with None
        show player 4 with dissolve
        pause
        player_name "( \"Meu brinquedo favorito...\" )"
        player_name "( Ela não mencionou algo sobre um brinquedo em {b}seu diário{/b}? )"
        jen "{b}[deb_name]{/b}, Você viu o meu alisador de cabelo?!"
        show player 22 with dissolve
        player_name "( Oh droga, parece que {b}[jen_name]{/b} terminou o banho dela! )"
        deb "Não, querida."
        jen "Bem, eu não consigo encontrar!"
        player_name "( É melhor eu sair daqui! )"
        hide player with dissolve
        $ player.go_to(L_home_hallway)
        scene expression player.location.background_closeup with None
        show player 11 at left
        show jenny b_towel a_towel_hips f_upset_talk
        with dissolve
        jen "Você acabou de sair do meu quarto?!"
        show jenny f_upset
        show player 10
        player_name "Hã?"
        player_name "Não..."
        show player 5
        show jenny f_angry
        pause
        show player 6 with dissolve
        player_name "Por favor não me bata com o secador de cabelo novamente!"
        show jenny f_eyeroll
        jen "Ugh, apenas saia do meu caminho, perdedor!"
        hide jenny with dissolve
        pause
        show player 37 with dissolve
        player_name "( Ufa, isso foi perto! )"
        pause
        show player 5 with dissolve
        player_name "( Quanto tempo levarei para encontrar coisas ruins no {b}laptop dela{/b}... )"
        player_name "( Só deveria tentar quando, Souber que vou ter tempo de sobra para bisbilhotar. )"
        pause
        show player 4 with dissolve
        player_name "( Talvez {b}à noite{/b}, quando {b}ela estiver dormindo{/b}? )"
        pause
        show player 17 with dissolve
        player_name "( Vou ter que ter cuidado, mas acho que vale a pena tentar. )"
        hide player with dissolve
        $ game.timer.tick()
        $ player.go_to(L_home_hallway)
        $ M_jenny.trigger(T_jenny_return_from_shower)
        $ game.main()
    if M_jenny.is_state(S_jenny_figure_out_password) and game.timer.is_day():
        call siscomp_day
        $ player.go_to(L_home_hallway)
        $ game._in_shower = None
        $ game.main()
    else:
        $ M_player.set("on_jenny_pc", True)
        call screen sis_computer

label jenny_computer_camslut:
    $ game.in_dialogue = True
    if not sispc_livecrush_seen:
        player_name "( Aqui está. )"
        pause
        player_name "( Humm, O perfil dela é horrível... )"
        player_name "( Deusa do sexo de vinte e quatro anos? Haha! )"
        pause
        player_name "( Há uma aba de vídeos! )"
        $ sispc_livecrush_seen = True
    $ game.in_dialogue = False
    call screen jenny_camslut

label jenny_camslut_videos_tab:
    $ game.in_dialogue = True
    show screen jenny_camslut_videos
    if not jenny_camslut_videos_tab_seen:
        player_name "( Ela tem dois vídeos salvos aqui! )"
        pause
        player_name "( Eu não posso assistir isso no quarto dela ... Ela pode acordar! )"
        pause
        player_name "( Talvez haja alguma maneira de {b}conectar seu computador ao meu{/b}? )"
        $ jenny_camslut_videos_tab_seen = True
    elif M_player.get("on_jenny_pc") and game.timer.is_dark():
        player_name "( Eu não posso assistir esses vídeos em seu quarto ... Ela pode acordar! )"
        pause
    elif M_jenny.is_state(S_jenny_check_for_new_video):
        player_name "( Droga! )"
        pause
        player_name "( Sem vídeo novo... )"
        pause
        player_name "( Aqui diz que ela estava online ontem ... Eu me pergunto por que ela não está salvando seus novos shows? )"
        $ M_jenny.trigger(T_jenny_checked_pc_for_new_vids)
    elif M_jenny.is_state(S_jenny_video_3_uploaded):
        player_name "( Funcionou, ela salvou um novo vídeo! )"
    $ renpy.hide_screen("jenny_camslut")
    $ game.in_dialogue = False
    call screen jenny_camslut_videos

label jenny_camslut_video_choice(video=1):
    if not M_player.get("on_jenny_pc"):
        if not (M_jenny.get("watched_video_1") or M_jenny.get("watched_video_2")):
            player_name "( Legal! )"
            player_name "( Agora vamos conferir esses vídeos! )"
        hide screen MC_computer
        hide screen sis_computer
        hide screen jenny_camslut_videos
        call expression game.dialog_select("jenny_computer_video_{}".format(video))
        $ M_jenny.set("watched_video_{}".format(video), True)
        if M_jenny.get("watched_video_1") and M_jenny.get("watched_video_2") and M_jenny.is_state(S_jenny_figure_out_password):
            scene expression player.location.background_closeup with None
            show player 5
            player_name "( Um pênis de verdade? )"
            player_name "( Ela está falando sobre foder alguém na câmera??! )"
            player_name "( Certamente, ela não iria tão longe? )"
            pause
            show player 403
            player_name "( Cara, espero que ela faça mais vídeos! )"
            hide player with dissolve
            hide screen comp_screen
            hide screen sis_computer
            $ M_jenny.trigger(T_jenny_a_real_penis)
            $ game.main()
        if M_jenny.is_state(S_jenny_video_3_uploaded):
            $ M_jenny.trigger(T_jenny_checked_new_vid)
    else:
        $ game.in_dialogue = True
        show screen jenny_camslut_videos
        show screen sis_computer
        player_name "Eu não posso assistir aqui! Ela pode acordar!"
        $ game.in_dialogue = False
    show screen sis_computer
    call screen jenny_camslut_videos
    return

label jenny_bedroom_no_password:
    scene expression "backgrounds/location_computer_jenny_01.jpg"
    player_name "( Sua senha está bloqueada... )"
    player_name "( Eu deveria tentar descobrir a senha primeiro. )"
    player_name " ( Talvez ela tenha deixado algum tipo de pista. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
