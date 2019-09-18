label erik_bedroom:
    call expression game.dialog_select(game.telescope.erik)
    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_erik_morning_1:
    scene windowerikmorning01
    if game.timer.is_weekend():
        player_name "( Ele não está no quarto dele. )"
    else:
        player_name "( Ele provavelmente já saiu para a escola. )"
    return

label telescope_erik_morning_2:
    scene windowerikmorning02
    if game.timer.is_weekend():
        player_name "( Ele provavelmente ficou acordado a noite toda jogando esse jogo... )"
    else:
        player_name "( Ele está jogando a essa hora? Ele deveria estar se preparando para a escola... )"
    return

label telescope_erik_afternoon_1:
    scene windowerikday 1
    player_name "( Ele não está em casa. )"
    return

label telescope_erik_afternoon_2:
    scene windowerikday 2
    player_name "( As persianas estão fechadas. Ele deve estar usando sua loção novamente. )"
    return

label telescope_erik_afternoon_3:
    scene windowerikday04a_b
    player_name "( O que {b}Erik{/b} està olhando? )"
    player_name "( Isso parece estranhamente familiar... )"
    return

label telescope_erik_afternoon_4:
    scene windowerikday05a_b
    player_name "Ahh!!" with hpunch
    player_name "( Eu posso ver porque ele estava tão animado em conseguir... )"
    return

label telescope_erik_night_1:
    scene windoweriknight01
    player_name "( Ele está sempre jogando esse jogo... )"
    return

label telescope_erik_night_2:
    scene windoweriknight02
    player_name "( As persianas estão fechadas. Ele deve estar usando sua loção novamente. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
