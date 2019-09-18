label jenny_button_dialogue:
    if player.location == L_home_diningroom:
        $ M_jenny.set('sit', 1)
    else:
        $ M_jenny.set('sit', 0)
    scene expression player.location.background_closeup
    if M_jenny.is_state(S_jenny_talked_to_cedric) and game.timer.is_day():
        call expression game.dialog_select("jenny_button_talked_to_cedric")
        $ M_jenny.trigger(T_jenny_cedric_didnt_call)
        $ game.timer.tick()
        $ game.main()
    elif M_jenny.is_state(S_jenny_go_to_her_room) and L_home_sisbedroom.is_here(M_jenny):
        if M_jenny.get("dominance") > 0:
            call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_dominant")
            if player.has_money(200):
                call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_dominant_has_money")
                $ player.spend_money(200)
                $ game.timer.tick()
                $ M_jenny.trigger(T_jenny_pay_for_favors)
            else:
                call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_dominant_no_money")
        else:
            call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_submissive")
            if player.has_money(200):
                call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_submissive_has_money")
                $ player.spend_money(200)
                $ game.timer.tick()
                $ M_jenny.trigger(T_jenny_pay_for_favors)
            else:
                call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_submissive_no_money")
        $ game.main()
    elif M_jenny.is_state(S_jenny_have_breakfast_2) and L_home_diningroom.is_here(M_jenny):
        call expression game.dialog_select("dining_room_jenny_have_breakfast_2")
        menu:
            "Você é sexy. {color=7ff7}[[Submissive]{/color}":
                call expression game.dialog_select("dining_room_jenny_have_breakfast_2_youre_hot")
                $ M_jenny.decrement("dominance")
            "NÃO. {color=f77b}[[Dominant]{/color}":
                call expression game.dialog_select("dining_room_jenny_have_breakfast_2_no")
                $ M_jenny.increment("dominance")
        $ M_jenny.trigger(T_jenny_had_breakfast_2)
        $ game.main()
    elif M_jenny.is_state(S_jenny_get_a_mask, S_jenny_buy_mask) and L_home_sisbedroom.is_here(M_jenny):
        call expression game.dialog_select("jenny_button_get_mask")
        $ game.main()
    elif M_jenny.is_state(S_jenny_bought_mask) and L_home_sisbedroom.is_here(M_jenny):
        call expression game.dialog_select("jenny_button_bought_mask")
        $ M_jenny.trigger(T_jenny_delivered_mask)
        $ game.main()
    elif M_jenny.is_state(S_jenny_start_camshow_handjob) and L_home_sisbedroom.is_here(M_jenny):
        call expression game.dialog_select("button_jenny_start_camshow_handjob")
    elif M_jenny.is_state(S_jenny_pool_talk) and game.timer.is_weekend() and game.timer.is_morning():
        call expression game.dialog_select("button_jenny_pool_talk")
        $ M_jenny.trigger(T_jenny_stalked)
        $ player.go_to(L_home)
        $ game.main()
    elif M_jenny.is_state(S_jenny_ask_movie_date) and L_home_sisbedroom.is_here(M_jenny):
        call expression game.dialog_select("jenny_button_ask_movie_date")
        $ M_jenny.trigger(T_jenny_movie_date)
        $ game.main()
    elif M_jenny.is_state(S_jenny_movie_date) and L_home_sisbedroom.is_here(M_jenny):
        call expression game.dialog_select("jenny_button_movie_date")
        $ game.main()
    elif M_jenny.pregnancy.stage >= 1:
        if M_jenny.pregnancy.stage <= 1:
            call expression game.dialog_select("jenny_button_pregnancy_stage_1")
            jump jenny_pregnancy_menu
        elif M_jenny.pregnancy.stage == 2:
            call expression game.dialog_select("jenny_button_pregnancy_stage_2")
            jump jenny_pregnancy_menu
        elif M_jenny.pregnancy.stage in (3, 4):
            call expression game.dialog_select("jenny_button_pregnancy_stage_3")
            jump jenny_pregnancy_menu
        else:
            call expression game.dialog_select("jenny_button_pregnancy_holding_baby")
            jump jenny_pregnancy_baby_menu
    else:
        if L_home_diningroom.is_here(M_jenny):
            if M_jenny.between_states(S_jenny_start, S_jenny_caught_snooping):
                call expression game.dialog_select("jenny_button_intro_diningroom_j8")
                $ game.main()
            elif M_jenny.between_states(S_jenny_caught_snooping, S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_intro_diningroom_j16")
            elif M_jenny.between_states(S_jenny_caught_talking_to_camslut, S_jenny_end):
                call expression game.dialog_select("jenny_button_intro_diningroom_j20")
            else:
                call expression game.dialog_select("jenny_button_intro_diningroom_j21")
        elif L_home_backyard.is_here(M_jenny):
            if M_jenny.between_states(S_jenny_start, S_jenny_caught_snooping):
                call expression game.dialog_select("jenny_button_intro_backyard_j8")
                $ game.main()
            elif M_jenny.between_states(S_jenny_caught_snooping, S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_intro_backyard_j16")
            elif M_jenny.between_states(S_jenny_caught_talking_to_camslut, S_jenny_end):
                call expression game.dialog_select("jenny_button_intro_backyard_j20")
            else:
                call expression game.dialog_select("jenny_button_intro_backyard_j21")
        elif L_home_sisbedroom.is_here(M_jenny):
            if game.timer.is_afternoon():
                if M_jenny.between_states(S_jenny_start, S_jenny_caught_snooping):
                    call expression game.dialog_select("jenny_button_intro_bedroom_j8")
                    $ player.go_to(L_home_hallway)
                    $ game.main()
                elif M_jenny.between_states(S_jenny_caught_snooping, S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_intro_bedroom_j16")
                elif M_jenny.between_states(S_jenny_caught_talking_to_camslut, S_jenny_end):
                    call expression game.dialog_select("jenny_button_intro_bedroom_j20")
                else:
                    call expression game.dialog_select("jenny_button_intro_bedroom_j21")
            elif game.timer.is_evening():
                if M_jenny.between_states(S_jenny_start, S_jenny_caught_snooping):
                    call expression game.dialog_select("jenny_button_intro_bedroom_evening_j8")
                    $ player.go_to(L_home_hallway)
                    $ game.main()
                elif M_jenny.between_states(S_jenny_caught_snooping, S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_intro_bedroom_evening_j16")
                elif M_jenny.between_states(S_jenny_caught_talking_to_camslut, S_jenny_end):
                    call expression game.dialog_select("jenny_button_intro_bedroom_evening_j20")
                else:
                    call expression game.dialog_select("jenny_button_intro_bedroom_evening_j21")
    menu sis_bedroom_menu:
        "{b}Roxxy{/b}." if M_bissette.is_state(S_bissette_jenny_mentoring_payment) and L_home_sisbedroom.is_here(M_jenny):
            call expression game.dialog_select("jenny_dialogue_roxxy_pre")
            menu:
                "Pagar" if player.has_money(500):
                    $ player.spend_money(500)
                    call expression game.dialog_select("jenny_dialogue_roxxy_pay")
                    $ M_bissette.trigger(T_bissette_jenny_paid)
                "Não pague":

                    call expression game.dialog_select("jenny_dialogue_roxxy_do_not_pay")

        "Eu tenho uma surpresa para você!" if M_jenny.is_state(S_jenny_diary_clue) and player.has_item("\w+_necklace", regex=True) and game.timer.is_tick(1, 2):
            call expression game.dialog_select("button_jenny_have_a_surprise_necklace")
            menu:
                "Sim.":
                    call expression game.dialog_select("button_jenny_have_a_surprise_yes")
                "Não, Eu quero a coisa real!":
                    call expression game.dialog_select("button_jenny_have_a_surprise_no")
            $ M_jenny.trigger(T_jenny_give_necklace)
            jump sis_bedroom_menu

        "Fazer um acordo." if M_jenny.finished_state(S_jenny_go_to_her_room):
            if L_home_diningroom.is_here(M_jenny) or L_home_backyard.is_here(M_jenny):
                call expression game.dialog_select("jenny_dialogue_make_a_deal_breakfast")
            else:
                call expression game.dialog_select("jenny_dialogue_make_a_deal")
            $ game.main()

        "Brinquedo." if M_jenny.is_state(S_jenny_get_a_toy, S_jenny_go_to_pink, S_jenny_bring_toy_back) and L_home_sisbedroom.is_here(M_jenny):
            if M_jenny.is_state(S_jenny_bring_toy_back):
                call expression game.dialog_select("button_jenny_has_toy_electroclit")
                if M_jenny.get("dominance") <= 0:
                    call expression game.dialog_select("button_jenny_has_toy_electroclit_submissive")
                else:
                    call expression game.dialog_select("button_jenny_has_toy_electroclit_dominant")
                $ M_jenny.trigger(T_jenny_brought_back_toy)
                $ game.timer.tick()
                $ game.main()
            else:
                call expression game.dialog_select("button_jenny_get_toy_electroclit")
                jump sis_bedroom_menu

        "{b}Cedric{/b}." if M_jenny.is_state(S_jenny_talk_to_cedric) and L_home_sisbedroom.is_here(M_jenny):
            call expression game.dialog_select("button_jenny_talk_to_cedric")

        "Camshow." if M_jenny.is_state(S_jenny_come_back_camshow) and not M_jenny.pregnancy and game.timer.is_day():
            call expression game.dialog_select("button_jenny_come_back_camshow")

        "Camshow." if M_jenny.finished_state(S_jenny_start_camshow_handjob) and L_home_sisbedroom.is_here(M_jenny) and not M_jenny.pregnancy and game.timer.is_day():
            $ M_jenny.set('teasin_before_sex', False)
            call expression game.dialog_select("button_jenny_camshow")
            menu jenny_camshow_options:
                "Masturbação.":
                    if M_jenny.get('teasin_before_sex'):
                        call expression game.dialog_select("finger_blasting_hj")
                    else:
                        call expression game.dialog_select("jenny_hj_intro_repeat")

                "Oral." if M_jenny.finished_state(S_jenny_start_camshow_blowjob):
                    if M_jenny.get('teasin_before_sex'):
                        call expression game.dialog_select("finger_blasting_bj")
                    else:
                        call expression game.dialog_select("jenny_bj_intro_repeat")

                "Cunnilingua." if M_jenny.finished_state(S_jenny_give_cunni):
                    if M_jenny.get('teasin_before_sex'):
                        call expression game.dialog_select("finger_blasting_cunni")
                    else:
                        call expression game.dialog_select("jenny_cunni_intro_repeat")

                "Sexo." if M_jenny.finished_state(S_jenny_cheerleader_sex):
                    if M_jenny.get('teasin_before_sex'):
                        call expression game.dialog_select("finger_blasting_sex")
                    else:
                        call expression game.dialog_select("jenny_sex_intro_repeat")

        "Apenas curioso." if L_home_diningroom.is_here(M_jenny) and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("jenny_button_just_curious")
            jump sis_bedroom_menu

        "Você e esse telefone." if L_home_diningroom.is_here(M_jenny) and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("jenny_button_you_and_phone")
            jump sis_bedroom_menu

        "Só dizendo Oi." if L_home_sisbedroom.is_here(M_jenny) and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("jenny_button_just_saying_hi")
            jump sis_bedroom_menu

        "Não está nadando?" if L_home_backyard.is_here(M_jenny) and M_jenny.between_states(S_jenny_start, S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("button_jenny_not_swimming")
            jump sis_bedroom_menu

        "Finalmente você está gostando de mim?" if game.timer.is_morning() and M_jenny.finished_state(S_jenny_catch_her_jilling):
            call expression game.dialog_select("jenny_button_warming_up")
            jump sis_bedroom_menu

        "O que você está escrevendo?" if game.timer.is_evening() and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            if not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_what_are_you_writing")
            elif M_jenny.between_states(S_jenny_start, S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_what_are_you_writing_2")
                jump sis_bedroom_menu

        "Você está realmente ficando?" if M_jenny.finished_inclusive(S_jenny_end) and not M_jenny.pregnancy.had_baby:
            call expression game.dialog_select("jenny_button_really_staying")
            jump sis_bedroom_menu

        "Você quer assistir porno comigo?" if M_jenny.finished_state(S_jenny_catch_her_jilling) and game.timer.is_afternoon():
            call expression game.dialog_select("button_jenny_wanna_watch_porn")
            $ M_jenny.set("force_couch_sex", True)

        "Quer brincar?" if game.timer.is_day() and L_home_diningroom.is_here(M_jenny) and M_jenny.finished_inclusive(S_jenny_end) and not M_jenny.pregnancy:
            $ player.go_to(L_home_diningroom)
            if M_jenny.get("first_sex_dining"):
                call expression game.dialog_select("button_jenny_fool_around_diningroom_first")
            else:
                call expression game.dialog_select("button_jenny_fool_around_diningroom_repeat")
            jump jenny_dining_room_sex_intro

        "Quer brincar?" if game.timer.is_day() and L_home_backyard.is_here(M_jenny) and M_jenny.finished_inclusive(S_jenny_end) and not M_jenny.pregnancy:
            if M_jenny.get("first_sex_pool"):
                $ M_jenny.set("first_sex_pool", False)
                call expression game.dialog_select("button_jenny_fool_around_pool_first")
            else:
                call expression game.dialog_select("button_jenny_fool_around_pool_repeat")

        "Quer brincar?" if L_home_sisbedroom.is_here(M_jenny) and M_jenny.finished_inclusive(S_jenny_end) and not M_jenny.pregnancy and game.timer.is_afternoon():
            call expression game.dialog_select("jenny_button_fool_around")
            menu:
                "Ok.":
                    $ M_jenny.set('teasin_before_sex', True)
                    jump jenny_camshow_options
                "Hoje nao.":
                    call expression game.dialog_select("jenny_button_fool_around_not_today")
                    $ player.go_to(L_home_hallway)
                    $ game.main()

        "Quer brincar?" if game.timer.is_evening() and M_jenny.finished_inclusive(S_jenny_end):
            call expression game.dialog_select("jenny_button_fool_around_evening")
            jump sis_bedroom_menu

        "Venha para o meu quarto esta noite." if M_jenny.finished_state(S_jenny_night_time_sex) and L_home_sisbedroom.is_here(M_jenny):
            call expression game.dialog_select("jenny_button_come_to_my_room")
            $ M_jenny.set("forced_sneak_in_chance", 60)
            jump sis_bedroom_menu

        "Experiencia de namorada." if M_jenny.finished_inclusive(S_jenny_necklace_rebutal):
            if game.timer.is_day():
                call expression game.dialog_select("jenny_button_gf_experience_day")
                jump sis_bedroom_menu
            elif game.timer.is_evening():
                call expression game.dialog_select("jenny_button_gf_experience_evening")
                menu:
                    "Sim.":
                        jump expression game.dialog_select("jenny_button_gf_experience_yes")
                    "deixa pra lá.":
                        call expression game.dialog_select("jenny_button_gf_experience_nevermind")
                        jump sis_bedroom_menu

        "Nada." if L_home_diningroom.is_here(M_jenny) and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            if not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_nothing")
            elif M_jenny.between_states(S_jenny_start, S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_nothing_2")

        "Deixa pra lá." if (L_home_sisbedroom.is_here(M_jenny) or L_home_backyard.is_here(M_jenny)) and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            if game.timer.is_day():
                if not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_nevermind")
                elif M_jenny.between_states(S_jenny_start, S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_nervermind_2")
            else:
                if not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_nevermind_evening_2")
                elif M_jenny.between_states(S_jenny_start, S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_nervermind_evening")

        "Eu devo ir." if (L_home_diningroom.is_here(M_jenny) or L_home_backyard.is_here(M_jenny)) and M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("jenny_button_leave_final_morning")

        "Estou ocupado." if L_home_sisbedroom.is_here(M_jenny) and M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("jenny_button_leave_final_bedroom")

    hide player
    hide jenny
    $ game.main()

label jenny_hospital_bed_dialogue:
    $ player.last_baby_gender = M_jenny.pregnancy.baby_gender
    scene expression game.timer.image("hospital_bed{}") with None
    show jenny a_gown_bed_baby b_gown_bed f_gurney_happy_down at Position (align=(0,0))
    show player f_normal_talk with dissolve
    player_name "Ei, como você está se sentindo?"
    show player f_normal
    show jenny f_gurney_happy_talk_down
    jen "Ahh, {b}[firstname]{/b}..."
    if M_jenny.pregnancy.baby_gender == "gêmeos":
        jen "Eles são lindos?"
        jen "Eu não consigo parar de olhar para eles..."
    elif M_jenny.pregnancy.baby_gender == "Garoto":
        jen "Ele é tão bonito?"
        jen "Eu não consigo parar de olhar..."
    else:
        jen "Ela é tão linda?"
        jen "Eu não consigo parar de olhar para ela..."
    show jenny f_gurney_happy_down
    show player f_normal_talk
    player_name "Hehe, É tão estranho ouvir você falar assim..."
    show player f_normal
    show jenny f_gurney_upset_talk
    jen "Cale a boca!"
    show jenny f_gurney_upset
    show player f_laugh
    player_name "O {b}[jen_name]{/b} Eu sei eu te amo."
    show player f_normal
    show jenny f_gurney_eyeroll
    jen "...Caralho"
    show jenny f_gurney_happy_down
    menu:
        "Eu só queria ver você.":
            show player f_normal_talk
            player_name "Eu só queria ver você."
            show player f_normal
            show jenny f_gurney_happy_talk_down
            jen "Bem, estamos bem."
            show jenny f_gurney_eyeroll
            jen "Quer dizer, eu estou exausto e a comida aqui é uma merda, mas..."
            show jenny f_gurney_happy_talk_down
            jen "... Caso contrário, estamos bem."
            show jenny f_gurney_happy_down
            show player f_normal_talk
            player_name "Você voltará para casa em breve."
            if M_jenny.pregnancy.baby_gender == "gêmeos":
                player_name "Você quer que eu Segure por algum tempo para que você possa dormir?"
            elif M_jenny.pregnancy.baby_gender == "Garoto":
                player_name "Você quer que eu Segure ele por algum tempo para que você possa dormir?"
            else:
                player_name "Você quer que eu Segure ela por algum tempo para que você possa dormir?"
            show player f_normal
            show jenny f_gurney_happy
            jen "Hmm?"
            show jenny f_gurney_happy_talk_down
            if M_jenny.pregnancy.baby_gender == "gêmeos":
                jen "Não, eu estou carregando eles!"
            elif M_jenny.pregnancy.baby_gender == "Garoto":
                jen "Não, eu estou carregando ele!"
            else:
                jen "Não, eu estou carregando ela!"
            show jenny f_gurney_happy_down
            show player f_normal_talk
            player_name "Tem certeza?"
            show player f_normal
            show jenny f_gurney_upset_talk
            if M_jenny.pregnancy.baby_gender == "gêmeos":
                jen "Eu disse, que estou carregando eles {b}[firstname]{/b}!"
            elif M_jenny.pregnancy.baby_gender == "boy":
                jen "Eu disse, que estou carregando eles {b}[firstname]{/b}!"
            else:
                jen "Eu disse, que estou carregando elas, {b}[firstname]{/b}!"
            show jenny f_gurney_happy_down
            show player f_worried_talk
            player_name "Ok."
            hide player with dissolve
    $ game.main()

label jenny_pregnancy_menu:
    menu:
        "{b}Roxxy{/b}." if M_bissette.is_state(S_bissette_jenny_mentoring_payment) and L_home_sisbedroom.is_here(M_jenny):
            call expression game.dialog_select("jenny_dialogue_roxxy_pre")
            menu:
                "Pagar" if player.has_money(500):
                    $ player.spend_money(500)
                    call expression game.dialog_select("jenny_dialogue_roxxy_pay")
                    $ M_bissette.trigger(T_bissette_jenny_paid)
                "Não pague":

                    call expression game.dialog_select("jenny_dialogue_roxxy_do_not_pay")
        "Você está bem?" if game.timer.is_morning() and M_jenny.pregnancy.stage == 1:
            call expression game.dialog_select("jenny_pregnancy_you_doing_ok_1")
            jump jenny_pregnancy_menu
        "Você ainda está brava?" if M_jenny.pregnancy.stage == 1:
            call expression game.dialog_select("jenny_pregnancy_are_you_still_mad")
            jump jenny_pregnancy_menu
        "Você está bem?" if M_jenny.pregnancy.stage == 2:
            call expression game.dialog_select("jenny_pregnancy_you_doing_ok_2")
            jump jenny_pregnancy_menu
        "Posso te dar uma coisa?" if M_jenny.pregnancy.stage == 2:
            call expression game.dialog_select("jenny_pregnancy_can_i_get_you_something")
            jump jenny_pregnancy_menu
        "Sobre {b}[deb_name]{/b}..." if M_jenny.pregnancy.stage == 2:
            call expression game.dialog_select("jenny_pregnancy_about_debbie")
            jump jenny_pregnancy_menu
        "Posso te dar uma coisa?" if game.timer.is_afternoon() and M_jenny.pregnancy.stage == 4:
            call expression game.dialog_select("jenny_pregnancy_can_i_get_you_something_3")
            jump jenny_pregnancy_menu
        "{b}[deb_name]{/b} está te deixando louco?" if M_jenny.pregnancy.stage in (3,4):
            call expression game.dialog_select("jenny_pregnancy_debbie_driving_crazy")
            jump jenny_pregnancy_menu
        "Vou deixar você sozinha.":
            call expression game.dialog_select("jenny_pregnancy_leave")
            $ game.main()

label jenny_pregnancy_baby_menu:
    menu:
        "Vocês precisam de alguma coisa?":
            call expression game.dialog_select("jenny_pregnancy_baby_need_anything")
            jump jenny_pregnancy_baby_menu
        "Ansiosa para Creche.":
            call expression game.dialog_select("jenny_pregnancy_baby_looking_forward_daycare")
            jump jenny_pregnancy_baby_menu
        "Eu vou deixar você Sozinha.":
            call expression game.dialog_select("jenny_pregnancy_baby_leave")
            $ game.main()

label jenny_button_gf_experience_yes:
    if not player.has_money(500) and M_jenny.get("jenny_girlfriend_first_time"):
        call expression game.dialog_select("jenny_button_gf_experience_no_money_first")
        jump sis_bedroom_menu
    elif not player.has_money(200) and not M_jenny.get("jenny_girlfriend_first_time"):
        call expression game.dialog_select("jenny_button_gf_experience_no_money_repeat")
        jump sis_bedroom_menu
    else:
        if M_jenny.get("jenny_girlfriend_first_time"):
            $ player.spend_money(500)
        else:
            $ player.spend_money(200)
        $ M_jenny.set("girlfriend_in_progress", True)
        call expression game.dialog_select("jenny_button_gf_experience_start")
        menu:
            "Fique.":
                call expression game.dialog_select("jenny_button_gf_experience_stay_in")
                $ game.timer.tick()
                $ player.go_to(L_home_livingroom)
                $ game.main()

label jenny_button_girlfriend_experience_bedroom:
    scene expression "backgrounds/location_home_bedroom_sex01d.jpg"
    show player b_sit a_sit_lap f_sit_flirt_talk o_sit_boner at Position (align=(0,0))
    show jenny b_visit_sit_naked a_visit_sit_naked_down f_visit_sexy_up
    with fade
    if M_jenny.get("jenny_girlfriend_first_time"):
        player_name "Uau."
        show player f_sit_flirt
        show jenny f_visit_sexy_talk_up
        jen "Demorou o suficiente..."
        show jenny f_visit_sexy_up
        player_name "..."
        show jenny f_visit_sexy_talk_up
        jen "Você gosta?"
        show jenny f_visit_sexy_up
        show player f_sit_flirt_talk
        player_name "Eu gosto!"
        show player f_sit_flirt
        show jenny f_visit_sexy_talk_up
        jen "Hehe, bom!"
        show jenny a_visit_sit_naked_push f_visit_sexy_up
        show player b_sit_falling a_empty f_empty
        with dissolve
        pause
        show jenny f_visit_sexy_talk a_visit_sit_naked_down
        show player b_sit_laying o_visit_laying_boner
        with dissolve
        jen "Agora deite-se e deixe-me cuidar de você."

        scene expression "backgrounds/location_home_bedroom_sex05.jpg"
        show jenny_mc_room_sex insert
        with fade
        jen "Mmm, Estou muito feliz que meu novo namorado tenha um pau tão legal!"
        player_name "Você gosta disso?"
        show jenny_mc_room_sex 1 with dissolve
        jen "Fuuuuck!"
        pause
        $ animated = True
        $ anim_toggle = True
        $ M_jenny.set('sex speed', .12)
        show expression AnimatedImage("jenny_mc_room_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
        jen "Hehe, eu não estaria namorando com você se não o fizesse..."
        player_name "Uau, você está realmente molhada esta noite!"
        jen "eu sei..."
        pause
        jen "Mmm, Eu estive pensando em seu pau a noite toda!"
        player_name "Mesmo enquanto estávamos assistindo seu show?"
        jen "Sim, eu já vi tudo isso antes..."
        player_name "Oh, certo."
        pause
        jen "Eu vou dormir muito bem depois disso!"
        player_name "Sim eu também!"
    else:
        player_name "Você sabe, eu realmente poderia me acostumar a ver você nua na minha cama à noite..."
        show player f_sit_flirt
        show jenny f_visit_sexy_talk_up
        jen "Sim, aposto que você poderia."
        show jenny a_visit_sit_naked_push f_visit_sexy_up
        show player b_sit_falling a_empty f_empty
        with dissolve
        pause
        show jenny f_visit_sexy_talk a_visit_sit_naked_down
        show player b_sit_laying o_visit_laying_boner
        with dissolve
        jen "Agora deite-se e deixe-me cuidar de você."
        scene expression "backgrounds/location_home_bedroom_sex05.jpg"
        show jenny_mc_room_sex insert
        with fade
        jen "Mmm, Eu amo esse pau!"
        player_name "Eu acho que te ama também."
        jen "Hah!"
        show jenny_mc_room_sex 1 with dissolve
        jen "porraaaa!"
        pause
        $ animated = True
        $ anim_toggle = True
        $ M_jenny.set('sex speed', .12)
        show expression AnimatedImage("jenny_mc_room_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
        jen "É tão profundo {b}[firstname]{/b}!"
        player_name "Sim.."
        pause
        player_name "Eu adoro ver seus peitos saltando dessa posição!"
        jen "Ahh!"
    jump jenny_mc_room_sex_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
