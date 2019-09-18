label backyard:
    call expression game.dialog_select(game.telescope.backyard)

    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_backyard_morning_1:
    scene windowbackyardday01
    player_name "( {b}Sra. Johnson{/b} tapete de yoga está lá... )"
    player_name "( ...Não há ninguém no quintal. )"
    return

label telescope_backyard_afternoon_1:
    scene windowbackyardday01
    player_name "( {b}Sra. Johnson{/b} tapete de yoga está lá... )"
    player_name "( ...Não há ninguém no quintal. )"
    return

label telescope_backyard_afternoon_2:
    scene windowbackyardday02
    player_name "( Cara... )"
    player_name "( {b}Sra. Johnson{/b} é tão ... flexível... )"
    return

label telescope_backyard_afternoon_3:
    scene windowbackyardday03
    player_name "( {b}Sra. Johnson{/b} está sempre fazendo yoga... )"
    player_name "( Eu acho que ela gosta de ficar em forma. )"
    return

label telescope_backyard_afternoon_4:
    scene windowbackyardday04
    player_name "( Oh sim... )"
    player_name "( Essa é minha posição favorita. )"
    player_name "( Eu fico tão excitado quando ela faz isso ... Eu não sei porque. )"
    return

label telescope_backyard_night_1:
    scene windowbackyardnight01
    player_name "( {b}Sra. Johnson{/b} deixou seu tapete de yoga fora. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
