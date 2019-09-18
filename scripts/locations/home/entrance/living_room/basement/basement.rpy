label home_basement_dialogue:
    $ player.go_to(L_home_basement)
    if M_mom.is_state(S_mom_wash_clothes):
        call expression game.dialog_select("basement_mom_wash_clothes")
        $ M_mom.trigger(T_mom_clean_clothes)
        $ player.go_to(L_home_bedroom)

        $ game.timer.tick()

    elif M_mom.is_state(S_mom_close_valve):
        call expression game.dialog_select("basement_mom_close_valve")

    elif M_mom.is_state(S_mom_lotion_adventure) and M_mom.is_set("retrieved lotion"):
        jump expression game.dialog_select("mom_lotion_fun")

    elif M_mom.is_state(S_mom_give_laundry):
        call expression game.dialog_select("basement_mom_give_laundry")
        jump expression game.dialog_select("basement_mom_sex")
    $ game.main()

label basement_basket_debbie_panties:
    scene expression player.location.background_closeup with None
    if M_somrak.finished_state(S_somrak_start):
        show player 724 with dissolve
        player_name "( Essa e a calcinha da {b}[deb_name]{/b} . )"
        player_name "( Cara, ela são tão macio... )"
        pause
        player_name "( Aposto que {b}Mestre Somrak{/b} gostaria disso. )"
        hide player with dissolve
        $ player.get_item("debbie_panties")
    else:
        show player 10 with dissolve
        player_name "(Por que eu tentaria roubar as calcinha da {b}[deb_name]{/b} . )"
        player_name " ( Eu não tenho uso para ela agora )"
        hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
