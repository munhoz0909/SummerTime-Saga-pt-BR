label locker_check(direction, locker):
    if direction == "left":
        show expression game.timer.image("backgrounds/location_school_lefthall{}.jpg")
    else:
        show expression game.timer.image("backgrounds/location_school_right_hall{}.jpg")
    show player 1 at center
    if game.timer.is_day():
        if player.has_picked_up_item("master_key"):
            if not locker.is_visited:
                $ charname = locker.name.split("'")[0]
                player_name "Usando a chave mestra, eu consegui abrir o armario {b}[charname]{/b} ."
            $ player.location = locker
        else:
            call expression game.dialog_select("locker_locked_{}".format(random.randint(1,2)))
            $ game.main()
    else:
        if not player.has_picked_up_item("master_key"):
            call expression game.dialog_select("locker_locked_night")
            $ game.main()
        else:
            if not locker.is_visited:
                $ charname = locker.name.split("'")[0]
                player_name "Usando a chave mestra, eu consegui abrir o armario {b}[charname]{/b} ."
            $ player.location = locker
    scene expression locker.background
    return

label locker_locked_1:
    show player 10 with dissolve
    player_name "Esse não é meu armário ... eu precisaria de uma chave para abri-lo."
    return

label locker_locked_2:
    player_name "Está trancado e não tenho a chave."
    player_name "{b}Diretora Smith{/b} provavelmente tem uma chave para tudo."
    hide player with dissolve
    return

label locker_locked_night:
    scene expression player.location.background_blur
    show player 5 with dissolve
    player_name "Esta não é a melhor hora para ficar vagando pelos corredores. Eu deveria tentar novamente durante o dia."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
