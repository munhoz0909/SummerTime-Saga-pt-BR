label bissettes_office_first_visit:
    scene school_office1_b with fade
    show player 10 with dissolve
    player_name "O escritório da {b}Sra. Bisette{/b} parece tão ... francês!"
    show player 14
    player_name "Talvez um dia possamos fazer uma viagem de campo com ela..."
    hide player with dissolve
    return

label bissettes_office_afternoon_visit:
    scene expression game.timer.image("french_office_c{}")
    show player 13 at left
    show teacher 2 at right
    with dissolve
    bis "Bonjour, {b}[firstname]{/b}!"
    show teacher 1
    show player 14
    player_name "Olá, {b}Miss Bissette{/b}."
    show player 17
    player_name "Eu gosto do seu escritório! É muito ... Umm ... Francês."
    show player 13
    show teacher 3
    bis "Merci beaucoup !"
    show teacher 1
    show player 35
    player_name "Então, por que você quer me ver no seu escritório?"
    show player 13
    show teacher 5
    bis "Bem, {b}[firstname]{/b}, Estou preocupado com o próximo exame."
    show teacher 4
    show player 33
    player_name "Hã? Você não precisa se preocupar, {b}Miss Bissette{/b}."
    show player 14
    player_name "Eu nunca senti tão preparado para um teste antes. Eu vou conseguir com certeza!"
    show player 13
    show teacher 5
    bis "Oui, {b}[firstname]{/b}! Você é o meu melhor aluno e estou muito orgulhosa de você!"
    bis "A {b}Roxxy{/b} está me preocupando tanto..."
    show teacher 4
    show player 12
    player_name "{b}Roxxy{/b}?"
    show player 5
    show teacher 5
    bis "Oui! Supondo que ela apareça no exame, não há como ela tirar uma nota de aprovação."
    show teacher 4
    show player 10
    player_name "O que acontece se ela não fizer o teste?"
    show player 5
    show teacher 5
    bis "Ce serait ennuyeux..."
    bis "E se {b}Roxxy{/b} não aparecer no exame, diminuirá a média de todos os alunos."
    show teacher 15 with dissolve
    bis "Estou com medo da {b}Diretora Smith{/b} perder a cabeça!"
    show teacher 14
    show player 10
    player_name "Você quer dizer que ela vai te demitir?!"
    show player 5
    show teacher 5 with dissolve
    bis "Oui..."
    show teacher 4
    show player 24
    player_name "..."
    show player 12
    player_name "Bem, eu não vou deixar isso acontecer!"
    show player 14
    player_name "Vou encontrar uma maneira de convencer {b}Roxxy{/b} para aparecer para o teste, eu prometo!"
    show player 13
    show teacher 2
    bis "Oh, {b}[firstname]{/b}! Tu es mon heros!"
    show teacher 12
    bis "Se você fizer isso por mim, darei a melhor recompensa especial que você puder imaginar, sim?"
    show teacher 13
    show player 29 with dissolve
    player_name "Sim!"
    show player 13 with dissolve
    show teacher 2
    bis "Très Bien! Boa sorte, {b}[firstname]{/b}!"
    show teacher 1
    show player 14
    player_name "Obrigado, {b}Miss Bissette{/b}."
    show player 13
    hide teacher with dissolve
    show player 35
    player_name "Hmm, isso vai ser difícil..."
    player_name "Tet uma coisa convincente {b}Roxxy{/b} para aparecer no exame."
    player_name "Mas ela também terá que passar de alguma forma..."
    show player 4 with dissolve
    player_name "..."
    show player 12
    player_name "... Tenho que pensar em algo."
    hide player with dissolve
    return

label bissettes_office_night_visit:
    scene expression game.timer.image("french_office_sex_c{}")
    show teacher 29 at right
    show player 13 at left
    with dissolve
    bis "Ahh, {b}[firstname]{/b}! Eu estava começando a pensar que você não viria!"
    show teacher 28
    show player 10
    player_name "Você começou sem mim?"
    show player 5
    show teacher 29
    bis "*Soluço* Oui, mon bel homme!"
    bis "Acabei de pegar a segunda garrafa."
    show teacher 30 with dissolve
    bis "Deixe-me derramar yo- *soluço*"
    show teacher 31 with dissolve
    bis "ça me saoûle."
    show teacher 33 with dissolve
    show player 13
    bis "Ah entende *soluço* os franceses fazem o melhor vinho!"
    show teacher 32
    show player 17
    player_name "Hehe, se você diz."
    show player 13
    show teacher 33
    bis "Tsk! É verdade!"
    bis "O melhor vinho..."
    bis "E os melhores amantes..."
    show teacher 32
    show player 11
    player_name "*Gole*"
    show teacher 33
    bis "Eu ainda te devo uma recompensa especial, sim?"
    show teacher 32
    show player 26
    player_name "Concerteza..."
    show player 13
    show teacher 33
    bis "Bem, está esperando por você, aqui..."
    bis "Por que você não vem e desembrulha?"
    show player 523 at Position (xoffset=378)
    show teacher 34
    with dissolve
    pause
    show player 525 at Position (xoffset=360)
    show teacher 35
    with dissolve
    pause
    show player 524 at Position (xoffset=378)
    show teacher 37
    with dissolve
    pause
    show player 525 at Position (xoffset=360)
    show teacher 38
    with dissolve
    pause
    show teacher 39
    bis "Você gosta?"
    show teacher 38
    show player 526 at Position (xoffset=360)
    player_name "eu gosto muito."
    show player 527 at Position (xoffset=360)
    player_name "Você é linda."
    show player 525 at Position (xoffset=360)
    show teacher 39
    bis "Não seja tímido, beije-os."
    hide player
    show teacher 39b
    with dissolve
    bis "Mmm..."
    bis "Lembre-se de usar sua língua, {b}[firstname]{/b}."
    show teacher 39b_39c_39d
    bis "Oh, mon bel homme..."
    bis "Você está fazendo- *Soluço*"
    bis "Você está me fazendo derreter com esses beijos!"
    pause
    pause
    show player 83c at left
    show teacher 39
    with dissolve
    bis "Eu sei que você está escondendo algo grande nessas suas calças..."
    bis "Eu te mostro a minha. Você me mostra o seu, sim?"
    show teacher 38
    show player 83b
    player_name "Certo!"
    show player 261bf with dissolve
    pause
    show player 263cf with dissolve
    show teacher 39
    bis "Oh mon Dieu! Elle est magnifique!"
    bis "Me dê isto, {b}[firstname]{/b}!"
    show teacher 38
    show player 262bf
    player_name "Você quer dizer ... Você quer que eu..."
    show player 263cf
    show teacher 39
    bis "S'il te plaît!"
    bis "Sua recompensa está apenas começando."
    show teacher 40 with dissolve
    pause
    show teacher 41 with dissolve
    pause
    show teacher 42 with dissolve
    pause
    show teacher 43 with dissolve
    show player 263bf
    bis "Não posso começar a descrever o quanto estou ansiosa por isso."
    pause
    show teacher 44 with dissolve
    pause
    show teacher 45 with dissolve
    pause
    show player 263cf
    show teacher 46
    bis "Você gosta do meu corpo francês, sim?"
    show teacher 45
    show player 262bf
    player_name "Sim!"
    show player 263cf
    show teacher 46
    bis "Excellente!"
    show teacher 47 at Position (yoffset=-61) with dissolve
    show player 263bf
    pause
    show teacher 48 at Position (yoffset=-61)
    bis "Venha! Deixe-me ensinar sobre o amor francês!"
    show teacher 50 with dissolve
    bis "Estou pronta para você."
    hide player
    hide teacher
    show teachers 51 at right
    with dissolve
    bis "Entrar em mim, {b}[firstname]{/b}."
    show teachers 52 with dissolve
    bis "Ohh, Elle est si grosse!"
    bis "Aaaah!"

    $ M_bissette.set("change angle", False)
    $ M_bissette.set("sex speed", .175)
    show expression AnimatedImage("teachers", [1,2,3,4,5,6,7], M_bissette) as teachers at right with dissolve
    pause
    return

label bissettes_office_night_visit_repeat:
    $ persistent.cookie_jar["Bissette"]["gallery"]["02_unlocked"] = True
    scene expression game.timer.image("french_office_sex_c{}")
    show teacher 29 at right
    show player 13 at left
    with dissolve
    bis "Então, você gostaria de um pouco de vinho ou ir direto para o amor?"
    show teacher 28
    show player 26
    player_name "Vamos para o Amor, por favor."
    show player 13
    show teacher 31 with dissolve
    bis "Dieu merci!"
    show teacher 33 with dissolve
    bis "Hehe!"
    bis "Estou ansiosa por isso o dia todo!"
    bis "Venha, mon bel homme! Devaste-me!"
    show teacher 32
    show player 14
    player_name "Avec plaisir!"
    show player 523 at Position (xoffset=378)
    show teacher 34
    with dissolve
    pause
    show player 525 at Position (xoffset=360)
    show teacher 35
    with dissolve
    pause
    show player 524 at Position (xoffset=378)
    show teacher 37
    with dissolve
    pause
    show player 525 at Position (xoffset=360)
    show teacher 38
    with dissolve
    pause
    show player 527 at Position (xoffset=360)
    player_name "Você é linda."
    show player 525 at Position (xoffset=360)
    show teacher 39
    bis "Não seja tímido, beije-os."
    hide player
    show teacher 39b
    with dissolve
    bis "Mmm..."
    bis "Lembre-se de usar sua língua, {b}[firstname]{/b}."
    show teacher 39b_39c_39d
    bis "Oh, mon bel homme..."
    bis "Você está fazendo- *Soluço*"
    bis "Você está me fazendo derreter com esses beijos!"
    pause
    show player 83c at left
    show teacher 39
    with dissolve
    bis "Eu sei que você está escondendo algo grande nessas suas calças..."
    bis "Eu te mostro a minha. Você me mostra o seu, sim?"
    show teacher 38
    show player 83b
    player_name "Certo!"
    show player 261bf with dissolve
    pause
    show player 263cf with dissolve
    show teacher 39
    bis "Oh mon Dieu! C'est beau..."
    bis "Me dê isto, {b}[firstname]{/b}!"
    show teacher 40 with dissolve
    pause
    show teacher 41 with dissolve
    pause
    show teacher 42 with dissolve
    pause
    show teacher 43 with dissolve
    show player 263bf
    pause
    show teacher 44 with dissolve
    pause
    show teacher 45 with dissolve
    pause
    show player 263cf
    show teacher 46
    bis "Você gosta do meu corpo francês, sim?"
    show teacher 45
    show player 262bf
    player_name "Sim!"
    show player 263cf
    show teacher 46
    bis "Excellente!"
    show teacher 47 at Position (yoffset=-61) with dissolve
    show player 263bf
    pause
    show teacher 48 at Position (yoffset=-61)
    bis "Ah, ma chatte toute serrée a envie de ta grosse bite bien juteuse."
    show teacher 47 at Position (yoffset=-61)
    show player 262bf
    player_name "O que?"
    show player 263cf
    show teacher 50 with dissolve
    bis "Eu estive esperando por você."
    hide player
    hide teacher
    show teachers 51 at right
    with dissolve
    bis "Entrar em mim, {b}[firstname]{/b}."
    show teachers 52 with dissolve
    bis "Ohh, elle est si grosse!"
    bis "Aaaah!"
    $ M_bissette.set("change angle", False)
    $ M_bissette.set("sex speed", .175)
    show expression AnimatedImage("teachers", [1,2,3,4,5,6,7], M_bissette) as teachers at right with dissolve
    pause
    return

label bissettes_office_chair_sex_intro:
    scene expression game.timer.image("bissette_office_sex_chair_c{}")
    show teachers_chair 1 at Position(xalign = 0.564)
    with dissolve
    bis "Vamos tentar na cadeira, devemos estar mais confortáveis."
    show teachers_chair 2 with dissolve
    player_name "Você sabe melhor. Você é a professora!"
    show teachers_chair 3 with dissolve
    bis "Oh, mon bel homme..."
    show teachers_chair 16 with dissolve
    pause
    show teachers_chair 4 with vpunch
    bis "Aaaah!"
    jump expression game.dialog_select("bissettes_office_sex_loop")

label bissettes_office_sex_intro:
    scene expression game.timer.image("french_office_sex_c{}")
    show player 263cf at left
    show teacher 50 at right
    with dissolve
    if randomizer() <= 50:
        bis "Você gosta de fazer na mesa, sim?"
    else:
        bis "Voltar para a mesa?"
    hide player
    hide teacher
    show teachers 51 at right
    with dissolve
    pause
    show expression AnimatedImage("teachers", [1,2,3,4,5,6,7], M_bissette) as teachers at right with dissolve
    bis "Ohh, elle est si grosse!"
    bis "Aaaah!"
    jump expression game.dialog_select("bissettes_office_sex_loop")

label bissettes_office_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_bissette.is_set("change angle"):
                    show expression AnimatedImage("teachers_chair", [4,5,6,7,8,9,10,11,12,13], M_bissette) as teachers_chair at Position(xalign = 0.564)
                else:
                    show expression AnimatedImage("teachers", [1,2,3,4,5,6,7], M_bissette) as teachers at right
                $ animated = True
            pause 5
            if animcounter in [1,3]:
                call expression game.dialog_select("bissette_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            if M_bissette.is_set("change angle"):
                $ pose_list = [4,5,6,7,8,9,10,11,12,13]
            else:
                $ pose_list = [1,2,3,4,5,6,7]
            $ poses_done = []
            while poses_done != pose_list:
                if M_bissette.is_set("change angle"):
                    show expression "teachers_chair {}".format(pose_list[pose_counter]) as teachers_chair at Position(xalign = 0.564)
                else:
                    show expression "teachers {}".format(pose_list[pose_counter]) as teachers at right
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("bissette_hscene_dialog")
        $ animcounter += 1
    call screen bissettes_office_sex_options

label bissette_hscene_dialog:
    if animcounter == 1:
        bis "Ohhhh!!!{p=1}{nw}"

    elif animcounter == 3:
        if not M_bissette.is_state(S_bissette_wine_sampling):
            bis "Mais rapido! Foda-me mais!{p=2}{nw}"
            bis "Oh, Oui!{p=2}{nw}"
            bis "Eu vou gozar, {b}[firstname]{/b}!{p=2}{nw}"
            player_name "Eu tambem, Não vou durar muito tempo!{p=2}{nw}"
            bis "Não pare!{p=2}{nw}"
            bis "Não-{p=1}{nw}"

        elif M_bissette.is_state(S_bissette_wine_sampling):
            $ initial_sex_diag = False
            bis "C'est incroyable!{p=2}{nw}"
            bis "Eu estava errada!{p=2}{nw}"
            bis "Nenhum francês me fodeu assim antes!{p=2}{nw}"
            bis "Aaaaaahh!! Não pare!{p=2}{nw}"
    return

label bissettes_office_sex_cum_chair_angle:
    bis "AAAAAAAHHHHH!!!!"
    player_name "Hnnngg!!!"
    show teachers_chair 14_15 at Position(xalign = 0.564) with flash
    pause
    show teachers_chair 16 with dissolve
    pause
    show teachers_chair 17 with dissolve
    pause
    show teachers_chair 18 with dissolve
    bis "Haah... Haah..."
    show teachers_chair 1 with dissolve
    bis "{b}[firstname]{/b}..."
    bis "Isso foi magnífico!"
    show teachers_chair 2
    player_name "Haaha... Sim."
    show teachers_chair 1
    bis "Nós devemos fazer isso de novo, sim?"
    show teachers_chair 2
    player_name "Concerteza!"
    show teachers_chair 1
    bis "Tres Bien, mon bel homme!"
    bis "Agora então, sente-se."
    bis "Vou preparar um pouco de fromage para acompanhar o seu vinho..."
    show teachers_chair 2
    return

label bissettes_office_sex_cum_desk_angle:
    bis "AAAAAAAHHHHH!!!!"
    player_name "Hnnngg!!!"
    show teachers 52_53 at right with flash
    pause
    show teachers 54 with dissolve
    bis "Haah... Haah..."
    show teachers 55 with dissolve
    bis "{b}[firstname]{/b}..."
    bis "Isso foi magnífico!"
    show teachers 56
    player_name "Haaha... Sim."
    show teachers 55
    bis "Temos que fazer isso de novo, sim?"
    show teachers 56
    player_name "Concerteza!"
    show teachers 55
    bis "Tres Bien, mon bel homme!"
    bis "Agora então, sente-se."
    bis "Vou preparar um pouco de fromage para acompanhar o seu vinho..."
    show teachers 56
    player_name "Ok..."
    return

label bissettes_office_sex_cum_first:
    bis "Então você voltará outra noite?"
    show teacher 45
    show player 26
    player_name "Você pode apostar que eu vou!"
    show player
    show teacher 46
    bis "Eu não posso esperar!"
    show teacher 45
    show player 36 with dissolve
    player_name "Te vejo em breve, {b}Miss Bissette{/b}!"
    show player 426 with dissolve
    show teacher 46
    bis "Au revoir, {b}[firstname]{/b}!"
    hide player
    hide teacher
    with dissolve
    $ renpy.end_replay()
    return

label bissettes_office_sex_cum_repeat:
    show player 13 at left
    show teacher 46 at right
    with dissolve
    bis "Isso foi maravilhoso."
    show teacher 45
    show player 26
    player_name "Sim, foi."
    show player 13
    show teacher 46
    bis "Gostaria de outra sessão amanhã?"
    show teacher 45
    show player 14
    player_name "Talvez eu venha."
    show player 13
    show teacher 46
    bis "Muito bem. Au revoir, {b}[firstname]{/b}!"
    show teacher 45
    show player 36 with dissolve
    player_name "Au revoir, {b}Miss Bissette{/b}!"
    hide player
    hide teacher
    with dissolve
    $ renpy.end_replay()
    return

label bissettes_office_sex_cum_scene_change:
    scene black
    hide teachers
    hide teachers_chair
    with fade

    pause

    scene expression game.timer.image("french_office_sex_c{}") with fade
    show player 13 at left
    show teacher 46 at right
    with dissolve
    return

label bissettes_office_sex_cum:
    if M_bissette.get("change angle"):
        call expression game.dialog_select("bissettes_office_sex_cum_chair_angle")
    else:
        call expression game.dialog_select("bissettes_office_sex_cum_desk_angle")

    call expression game.dialog_select("bissettes_office_sex_cum_scene_change")

    if M_bissette.is_state(S_bissette_wine_sampling):
        call expression game.dialog_select("bissettes_office_sex_cum_first")
    else:
        call expression game.dialog_select("bissettes_office_sex_cum_repeat")
    $ M_bissette.trigger(T_bissette_sexy_time)
    $ M_bissette.set("night visit", False)
    $ game.timer.tick()
    $ player.go_to(L_school_floor3)
    $ game.main()

label bissette_office_night_lock:
    scene expression game.timer.image("school_hall_third_floor{}_b")
    show player 55 at Position (xoffset=12) with dissolve
    pause
    show player 56 with dissolve
    player_name "Puta merda isso foi demais, Eu deveria ir para casa e descansar um pouco."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
