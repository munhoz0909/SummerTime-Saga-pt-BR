label courtyard_roxxy_intense_gymercise:
    scene expression game.timer.image("backgrounds/location_school_gym{}_blur.jpg") with dissolve
    show bridget a_dressed_crossed f_angry_talk at right
    show jersey 11 at left
    with dissolve
    bri "Bem, veja o que o gato arrastou."
    bri "Como está o seu treinamento?"
    show jersey 10
    show bridget a_dressed_crossed f_normal
    player_name "Uhm... Eu tenho tentado ir à academia!"
    show jersey 11
    show bridget a_dressed_crossed f_angry_talk
    bri "Tentando, hein?"
    bri "Vamos ver quantas flexões você pode fazer, agora."
    show bridget a_dressed_crossed f_normal_talk
    bri "Talvez você supere o seu melhor de ... O que foi isso de novo, dois!?"
    show bridget a_dressed_crossed f_angry_yell
    show jersey 22
    bri "Agora vai e dê vinte!" with hpunch
    show bridget b_bend a_empty f_bend_angry_talk_down at Position (yoffset=254)
    show jersey 29
    with fastdissolve
    pause 0.5
    show jersey 30
    pause 0.5
    show jersey 29
    bri "um!"
    show jersey 30
    pause 0.5
    show jersey 29
    bri "dois!"
    show jersey 30
    pause 0.7
    show jersey 29
    bri "Três!"
    show jersey 30
    pause 0.9
    show jersey 29
    bri "quatro!"
    show jersey 27
    show bridget a_dressed_crossed f_normal_talk b_dressed
    with fastdissolve
    bri "Parabéns, {b}[firstname]{/b}! Você melhorou de inútil para patético!"
    show bridget a_dressed_crossed f_angry_talk
    bri "Continue treinando, larva!"
    show bridget a_dressed_crossed f_normal
    show jersey 28
    player_name "Sim... {b}Treinadora Bridget{/b}..."
    show bridget a_dressed_crossed f_angry_talk
    show jersey 27
    bri "Agora saia da minha vista!"
    bri "E é melhor você mostrar mais progresso na próxima vez!"
    show bridget a_dressed_crossed f_normal
    player_name "Desculpe, {b}Treinadora Bridget{/b}!"
    hide bridget
    hide jersey
    with dissolve
    return

label courtyard_bridget_intro:
    scene expression game.timer.image("backgrounds/location_school_gym{}_blur.jpg")
    show jersey 13 at left with dissolve
    show bridget a_dressed_crossed f_normal_talk at right with dissolve
    bri "Olha quem decidiu aparecer!"
    show bridget a_dressed_crossed f_normal at right
    show jersey 17 at left
    player_name "Oi, {b}treinadora Bridget{/b}!"
    show jersey 18 at left
    player_name "Sei que perdi algumas sessões de treinamento, mas garanto que estarei pronto para o Campeonato Regional de Atletismo.-"
    show bridget a_dressed_crossed f_angry_talk at right
    show jersey 22 at left
    bri "Cale a boca, seu verme!" with hpunch
    bri "Você está um mês atrás de todos os outros, {b}[firstname]{/b}, e não vou deixar você arrastar a equipe com sua falta de compromisso!"
    bri "Se você não conseguir obter as pontuações de qualificação, poderá {b}esqueça seus créditos e se formar este ano.{/b}"
    show bridget a_dressed_crossed f_angry at right
    show jersey 10 at left
    player_name "Não se preocupe, senhora! Tenho certeza de que as eliminatórias não serão um problema!"
    show bridget a_dressed_crossed f_angry_talk at right
    show jersey 11 at left
    bri "...Oh Sim?"
    bri "Por que você não nos mostra sua \"habilidades atléticas de elite\" fazendo {b}20 flexões{/b} agora, seu patético pateta?!"
    show bridget a_dressed_whistle f_angry_yell at right
    show jersey 10 at left
    player_name "Mas"
    show jersey 23 at left
    bri "{b}*APITO*{/b}"
    show bridget b_bend a_empty f_bend_angry_talk_down at Position (yoffset=254) with dissolve
    show jersey 29 at left
    player_name "Ghh..."
    show jersey 30 at left
    bri "Um..."
    show jersey 29 at left
    player_name "Ghhhh..."
    show jersey 30 at left
    bri "Dois..."
    show jersey 29 at left
    player_name "...Eu ... eu não posso..."
    show jersey 30 at left
    bri "Três"
    bri "... ... ..."
    show bridget a_dressed_crossed f_angry_talk b_dressed with dissolve
    bri "O que?!! Isso é tudo que você tem??"
    show jersey 27 at left
    bri "Você não pode nem fazer três flexões miseráveis?!"
    show bridget a_dressed_crossed f_angry at right
    player_name "Eu..."
    player_name "Eu ... Desculpe ... Senhora..."
    show bridget a_dressed_crossed f_angry_talk at right
    bri "É melhor você levar sua bunda para a {b}academia local{/b} agora, e comece a levantar, se você quiser passar nesta aula..."
    show bridget a_dressed_crossed f_angry_yell at right
    bri "... Agora vai para classe da {b}Miss Bissette{/b}, onde trabalho duro e boas notas não importam para mim!"
    bri "Agora, {b}SAIA DA MINHA FRENTE!!!{/b}"
    hide bridget 7 with dissolve
    show ronda b_jersey a_jersey_sides f_normal_talk at right with dissolve
    ron "Você nunca vai superar as eliminatórias..."
    ron "Por que você se incomoda em vir para esta aula??"
    show ronda f_normal at right
    show jersey 28 at left
    player_name "Eu ainda posso fazer isso..."
    player_name "...E você sabe o que ... eu estava pensando, talvez você possa me ajudar"
    show ronda f_upset_angry at right
    show jersey 27 at left
    ron "Bem!"
    show ronda f_upset_talk
    ron "Se, por algum milagre, você conseguir {b}faça os ensaios{/b}... então venha falar comigo. Caso contrário, você pode parar de desperdiçar o fôlego."
    show ronda f_normal at right
    show jersey 28 at left
    player_name "Ok!"
    player_name "Mas quando eu fizer, você terá que me mostrar alguns dos seus truques!"
    show ronda f_normal_talk at right
    ron "Eu estarei na {b}piscina{/b} pelas próximas duas semanas, treinando para os 200m de testes..."
    ron "Se você faz parte da equipe, então venha me ver."
    show ronda f_normal at right
    show jersey 20 at left
    player_name "Combinado!!"
    show ronda f_rolleyes at right
    show jersey 19 at left
    ron "Ugh... Patético..."
    hide gym
    hide ronda
    hide jersey
    with dissolve
    return

label courtyard_bridget_training:
    scene gym
    show player 11 at left with dissolve
    show bridget a_dressed_crossed f_angry_talk at right with dissolve
    bri "{b}[firstname]{/b}!"
    bri "É melhor você treinar sua bunda na {b}Academia{/b}, ou eu vou enfiar meu pé na sua bunda!!"
    show player 32
    show bridget a_dressed_crossed f_angry
    player_name "Sim, senhora!!!"
    hide bridget
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
