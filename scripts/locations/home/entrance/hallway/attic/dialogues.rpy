label attic_first_visit:
    scene expression "backgrounds/location_home_attic_cutscene.jpg"
    show expression FilteredText("Usando a chave e o banco, consegui entrar no sótão.\nEu nunca tinha estado lá antes.\nEu estava cheio de emoção me perguntando que tesouros {b}[deb_name]{/b} e papai tem escondido.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    return

label painting:
    scene expression game.timer.image("attic{}")
    show expression "objects/closeup_painting01.png" with dissolve
    player_name "{b}[deb_name]{/b} costumava amar pintar animais de fazenda..."
    hide expression "objects/closeup_painting01.png" with dissolve
    $ A_rooster.unlock()
    $ game.main()

label globe:
    scene location_home_attic_globe
    pause
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
