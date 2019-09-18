label helen_room:
    call expression game.dialog_select(game.telescope.helen)

    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_helen_morning_1:
    scene windowhelenmorning01
    player_name "( {b}Mãe da Mia{/b} está sempre rezando de manhã... )"
    return

label telescope_helen_afternoon_1:
    scene windowhelenday01
    player_name "( Elas não estão em casa... )"
    return

label telescope_helen_night_1:
    scene windowhelennight01
    player_name "( É estranho como ambos têm sua própria cama... )"
    player_name "( ...Eu nunca os vi dormir juntos. )"
    return

label telescope_helen_night_2:
    scene location_telescope_helen_night02
    player_name "( Cara. )"
    player_name "( Parece que a {b}Helen{/b} está com raiva dele... )"
    player_name "..."
    player_name "( {b}Harold{/b} sempre parece tão triste... )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
