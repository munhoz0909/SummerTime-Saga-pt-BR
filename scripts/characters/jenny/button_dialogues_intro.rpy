label jenny_button_intro_bedroom_evening_j8:
    scene expression player.location.background_closeup with None
    show player f_worried
    show jenny f_upset_talk a_dressed_crossed
    with dissolve
    jen "Que porra você está fazendo?!"
    show jenny f_upset
    player_name "Hmm?"
    show player f_worried_talk
    player_name "Nada ... eu só"
    show player f_worried
    show jenny f_upset_talk
    jen "Saia do meu quarto, seu pervertido!"
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Por que você está sempre de mau humor?"
    show player f_skeptical
    show jenny f_angry_talk
    jen "SAIA DO MEU QUARTO, {b}[firstname]{/b}!!!" with hpunch
    show jenny f_angry
    show player f_surprised_talk a_dressed_rub with dissolve
    player_name "Ok, tudo bem ... eu estou indo."
    hide player with dissolve
    return

label jenny_button_intro_bedroom_evening_j16:
    scene expression player.location.background_closeup with None
    show player f_worried
    show jenny f_upset_talk
    with dissolve
    jen "Oh meu deus, o que você quer agora?!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Nada ... eu só"
    show player f_worried
    show jenny f_upset_talk
    jen "É melhor você ter um bom motivo para me incomodar!"
    show jenny f_upset
    show player f_surprised_teeth a_dressed_behind_head with dissolve
    player_name "..."
    show player a_dressed_pocket with dissolve
    return

label jenny_button_intro_bedroom_evening_j20:
    scene expression player.location.background_closeup with None
    show player f_normal_talk a_dressed_wave
    show jenny f_upset
    with dissolve
    player_name "Ei."
    show player f_normal a_dressed_pocket with dissolve
    show jenny f_upset_talk
    jen "Ei"
    show jenny f_upset
    show player f_worried
    pause
    show player f_worried_talk
    player_name "Então..."
    player_name "Estás bem?"
    show player f_worried
    show jenny f_eyeroll
    jen "Oh meu Deus..."
    show jenny f_upset_talk
    jen "Pare de agir de maneira estranha e vá direto ao ponto."
    show jenny f_upset
    show player f_tired
    player_name "..."
    return

label jenny_button_intro_bedroom_evening_j21:
    scene expression player.location.background_closeup with None
    show player f_normal_talk
    show jenny
    with dissolve
    player_name "Ei."
    show player f_normal
    show jenny f_normal_talk
    jen "Ei."
    show jenny f_normal
    pause
    show player f_normal_talk
    player_name "Você està ocupada?"
    show player f_normal
    show jenny f_normal_talk
    jen "Na verdade não, Estou apenas esperando {b}Jane{/b} chamar."
    show jenny f_normal
    show player f_normal_talk
    player_name "A...legal."
    show player f_normal
    show jenny f_eyeroll
    jen "..."
    show jenny f_normal_talk
    jen "O que você quer, {b}[firstname]{/b}?"
    show jenny f_normal
    return

label jenny_button_intro_backyard_j21:
    scene expression player.location.background_closeup with None
    show player f_worried_talk
    show jenny f_upset b_swimsuit a_swimsuit_hips
    player_name "Ei, {b}[jen_name]{/b}."
    show player f_worried
    show jenny f_upset_talk
    jen "Ei."
    show jenny f_upset
    pause
    show player f_skeptical_talk
    player_name "Você você ... Quer que eu esfregue um pouco de protetor solar em você ou algo assim?"
    show player f_worried
    show jenny f_laugh
    jen "Pfft, você deseja!"
    show jenny f_grin
    pause
    show jenny f_grin_talk
    jen "Fique nu e eu vou pensar nisso."
    show jenny f_grin
    show player f_worried_talk
    player_name "O que?!"
    show player f_worried
    show jenny f_grin_talk
    jen "Vamos, tire a roupa."
    show jenny f_grin
    show player f_skeptical_talk
    player_name "De jeito nenhum!"
    player_name "{b}[deb_name]{/b} está bem ali, na cozinha!"
    show player f_skeptical
    show jenny f_laugh
    jen "Hahahaah!"
    show jenny f_grin_talk
    jen "Seria tão engraçado se ela saísse e você estivesse nu!"
    show jenny f_grin
    show player f_worried_talk
    player_name "Não, não..."
    player_name "Ela iria surtar!"
    show player f_worried
    show jenny f_grin_talk
    jen "Eu sei!"
    show jenny f_laugh
    jen "Hahahaah!"
    show jenny f_grin
    return

label jenny_button_intro_bedroom_j21:
    scene expression player.location.background_closeup with None
    show player f_worried_talk
    show jenny f_upset
    player_name "Ei."
    show player f_worried
    show jenny f_upset_talk
    jen "Ei."
    show jenny f_upset
    pause
    show jenny f_upset_talk
    jen "Você está pronto para fazer um show?"
    jen "Tire essas roupas!"
    show jenny f_upset
    show player f_skeptical
    player_name "Ehh..."
    show jenny f_upset_talk
    jen "Vamos lá {b}[firstname]{/b}, meus fãs estão esperando!"
    show jenny f_upset
    return

label jenny_button_intro_diningroom_j21:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_magic_sit_stand_dressed f_magic_sit_stand_normal_talk a_magic_sit_stand_resting zorder 1 at Position (align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    player_name "Manhã."
    show player f_magic_sit_stand_normal
    show jenny a_breakfast_dressed_spoon f_breakfast_normal_talk with dissolve
    jen "Manhã."
    show jenny f_breakfast_normal
    pause
    show player f_magic_sit_stand_normal_talk
    player_name "Você parece bem hoje."
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_eyeroll
    jen "Heh, duh."
    show jenny f_breakfast_normal
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    pause
    show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting with dissolve
    show jenny f_breakfast_normal_talk
    jen "Você vem ao meu quarto mais tarde?"
    show jenny f_breakfast_normal
    show player f_diningroom_table_surprised_talk_food
    player_name "Eu não sei, talvez?"
    show player f_diningroom_table_surprised_left_food
    show jenny f_breakfast_normal_talk
    jen "Seria melhor."
    jen "Muito dinheiro para ser feito."
    show jenny f_breakfast_normal
    show player f_magic_sit_stand_normal_talk with dissolve
    player_name "Sim, eu sei."
    show player f_magic_sit_stand_normal
    return

label jenny_button_intro_bedroom_j20:
    scene expression player.location.background_closeup with None
    show player f_worried_talk
    show jenny f_upset
    player_name "Ei."
    show player f_worried
    show jenny f_upset_talk
    jen "Ei."
    show jenny f_gross
    pause
    show player f_worried_talk
    player_name "Então..."
    player_name "estás bem?"
    show player f_worried
    show jenny f_eyeroll
    jen "Oh meu Deus..."
    show jenny f_upset_talk
    jen "Pare de agir de maneira estranha e vá direto ao ponto."
    show jenny f_upset
    show player f_skeptical
    player_name "..."
    return

label jenny_button_intro_backyard_j20:
    scene expression player.location.background_closeup with None
    show player f_worried_talk
    show jenny f_upset b_swimsuit a_swimsuit_hips
    player_name "Manhã."
    show player f_worried
    show jenny f_normal_talk
    jen "Manhã."
    show jenny f_normal
    pause
    show player f_normal_talk
    player_name "Com certeza é legal aqui hoje..."
    show player f_normal
    show jenny f_eyeroll
    jen "Sim."
    show jenny f_gross
    pause
    player_name "..."
    show jenny f_upset_talk
    jen "Saia já!"
    jen "Estou tentando relaxar aqui."
    show jenny f_upset
    show player f_worried
    player_name "..."
    return

label jenny_button_intro_diningroom_j20:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_magic_sit_stand_dressed f_magic_sit_stand_worried_talk a_magic_sit_stand_resting zorder 1 at Position (align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    player_name "Manhã."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Manhã."
    show jenny f_breakfast_upset_down
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "Você está olhando para a sua seção de comentários novamente?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Sim, essas pessoas são doidas!"
    jen "Você deveria ler algumas das coisas que eles me pedem para fazer..."
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_worried_talk
    player_name "O dinheiro,e bom certo?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Isso aí!"
    show jenny f_breakfast_upset_talk
    jen "Você quer alguma coisa?"
    show jenny f_breakfast_upset
    return

label jenny_button_intro_bedroom_j16:
    scene expression player.location.background_closeup with None
    show jenny f_eyeroll
    show player f_worried
    jen "Oh meu deus, o que você quer agora?"
    show jenny f_upset
    show player f_worried_talk
    player_name "Nada ... eu só"
    show player f_worried
    show jenny f_upset_talk
    jen "É melhor você ter um bom motivo para me incomodar!"
    show jenny f_upset
    player_name "..."
    return

label jenny_button_intro_backyard_j16:
    scene expression player.location.background_closeup with None
    show jenny f_upset b_swimsuit a_swimsuit_hips
    show player f_worried_talk
    player_name "Ei."
    show player f_worried
    jen "..."
    pause
    show player f_worried_talk
    player_name "Eu gosto do seu maiô"
    show player f_surprised
    show jenny f_upset_talk
    jen "O que você quer?"
    show jenny f_upset
    show player f_worried_talk
    player_name "Eu não"
    show player f_skeptical
    show jenny f_upset_talk
    jen "Fala ou vá embora!"
    jen "Estou tentando relaxar aqui."
    show jenny f_upset
    player_name "..."
    return

label jenny_button_intro_diningroom_j16:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_magic_sit_stand_dressed f_magic_sit_stand_worried_talk a_magic_sit_stand_resting zorder 1 at Position (align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    player_name "Bom dia."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Sim Sim..."
    show jenny f_breakfast_upset_down
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "O que você está fazendo?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Ugh, esses babacas..."
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_worried_talk
    player_name "Hã?!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Nada, esquece!"
    show jenny f_breakfast_upset_talk
    jen "O que você quer, {b}[firstname]{/b}?!"
    show jenny f_breakfast_upset
    return

label jenny_button_intro_bedroom_j8:
    scene expression player.location.background_closeup with None
    show jenny f_upset_talk a_dressed_crossed
    show player f_worried
    jen "Que porra você está fazendo?!"
    show jenny f_upset
    player_name "Hmm?"
    show player f_worried_talk
    player_name "Nada ... eu só"
    show player f_worried
    show jenny f_angry_talk
    jen "Saia do meu quarto, seu pervertido!"
    show jenny f_angry
    show player f_skeptical_talk
    player_name "Por que você está sempre de mau humor?"
    show player f_surprised
    show jenny f_angry_talk
    jen "SAIA DO MEU QUARTO, {b}[firstname]{/b}!!!" with hpunch
    show jenny f_angry
    show player f_worried_talk
    player_name "Ok, tudo bem ... eu estou indo."
    hide player with dissolve
    return

label jenny_button_intro_backyard_j8:
    scene expression player.location.background_closeup with None
    show jenny f_upset b_swimsuit a_swimsuit_hips
    show player f_worried_talk
    player_name "Ei."
    show player f_worried
    jen "..."
    pause
    show player f_worried_talk
    player_name "Eu gosto do seu maiô"
    show player f_surprised
    show jenny f_upset_talk
    jen "Vá embora."
    show jenny f_upset
    player_name "..."
    show player f_skeptical_talk
    player_name "Eu estava apenas elogiando."
    show player f_skeptical
    show jenny f_upset_talk
    jen "Eu disse, vá embora, perdedor!"
    jen "Estou tentando relaxar aqui."
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Tchau, tudo bem."
    hide player with dissolve
    return

label jenny_button_intro_diningroom_j8:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_magic_sit_stand_dressed f_magic_sit_stand_worried_talk a_magic_sit_stand_resting zorder 0 at Position (align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    player_name "Bom dia."
    show player f_magic_sit_stand_worried
    jen "..."
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "Eu disse, bom dia?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "eu te ouvi."
    jen "Apenas cale a boca e me deixe em paz, perdedor..."
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_tired_talk
    player_name "Està bem."
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    pause
    show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting with dissolve
    pause
    scene black with fade
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
