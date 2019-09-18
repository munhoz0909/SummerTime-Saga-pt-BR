label peep_hole_dialogue:
    if M_player.get("peep_hole_first"):
        scene expression player.location.background_blur
        player_name "( Esse é um tapete esquisito... )"
        player_name "( Eu me pergunto por que está aqui em cima? )"
        scene expression game.timer.image("backgrounds/location_home_attic_cutscene01{}.jpg")
        player_name "( Hmm? )"
        player_name "( Há um pequeno buraco no piso aqui... )"
        pause
        player_name "( Que é isso )"
        $ M_player.set("peep_hole_first", False)
        call expression game.dialog_select("peep_hole_{}_first".format(game.timer._tod))
    else:
        scene expression game.timer.image("backgrounds/location_home_attic_cutscene01{}.jpg")
        pause
        player_name "( Vamos ver o que {b}[jen_name]{/b} está fazendo? )"
        call expression game.dialog_select("peep_hole_{}".format(game.timer._tod))
    $ game.main()

label peep_hole_0_first:
label peep_hole_1_first:
    scene expression "backgrounds/location_home_attic_peep_morning.jpg"
    pause
    player_name "( !!! )" with hpunch
    player_name "( É um olho mágico, bem em cima da cama de {b}[jen_name]{/b} ! )"
    pause
    player_name "( Bem, isso é interessante... )"
    player_name "( Eu me pergunto porque tem um buraco, Bem em cima da cama da {b}[jen_name]{/b} estranho? )"
    return

label peep_hole_2_first:
label peep_hole_3_first:
    scene expression "backgrounds/location_home_attic_peep_night.jpg"
    pause
    player_name "( !!! )" with hpunch
    player_name "( É um olho mágico, bem em cima da cama de {b}[jen_name]{/b} ! )"
    pause
    player_name "( Bem, isso é interessante... )"
    player_name "( Eu me pergunto porque tem um buraco aqui estranho? )"
    return

label peep_hole_0:
    scene expression "backgrounds/location_home_attic_peep_morning.jpg"
    pause
    player_name "( Hmm, apenas uma cama vazia... )"
    player_name "( Eu me pergunto onde ela está? )"
    return

label peep_hole_1:
    scene expression "backgrounds/location_home_attic_peep_day_01.jpg"
    pause
    player_name "( Hmm, ela está apenas, Escrevendo em seu diário... )"
    scene expression "backgrounds/location_home_attic_peep_day_02.jpg"
    pause
    player_name "( Que Chato!! )"
    return

label peep_hole_2:
    scene expression "backgrounds/location_home_attic_peep_evening_01.jpg"
    pause
    player_name "( Olha ela )"
    player_name "( Uau )" with hpunch
    player_name "( Ela está se masturbando! )"
    scene expression "backgrounds/location_home_attic_peep_evening_02.jpg"
    pause
    player_name "( Ah, isso é demais!! )"
    pause
    return

label peep_hole_3:
    scene expression "backgrounds/location_home_attic_peep_night.jpg"
    pause
    player_name "( Ahh, ela já foi para a cama a noite. )"
    pause
    player_name "( Ela e tão fofa, e inocente quando está dormindo... )"
    player_name "( ... Não como uma ignorante como costuma ser! )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
