label jenny_pregnant_announcement_1:
    scene expression player.location.background_blur with None
    show player f_looking_down a_dressed_phone
    player_name "Hmm?"
    show player f_shock_down
    player_name "Eu tenho uma menssagem de texto de {b}[jen_name]{/b}!"
    hide player with dissolve
    return

label jenny_pregnant_announcement_2:
    if not player.location == L_map:
        scene expression player.location.background_blur
        show player f_worried_talk a_dressed_phone
        with fade
    player_name "Eu me pergunto o que está acontecendo?"
    player_name "{b}Eu deveria passar {b}[jen_name]na{/b} sala e ver qual é o problema?{/b}."
    hide player with dissolve
    return

label jenny_pregnant_labor_1:
    scene expression player.location.background_blur
    show player f_normal_talk with dissolve
    player_name "Parece que eu tenho um texto."
    hide player with dissolve
    return

label jenny_pregnant_labor_2:
    scene expression player.location.background_blur
    show player f_shock
    with fade
    player_name "{b}[jen_name]{/b} teve o bebê?!"
    player_name "puta merda!"
    pause
    show player f_worried_talk
    player_name "É melhor eu ir para {b}clínica{/b} certificar de que estão bem."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
