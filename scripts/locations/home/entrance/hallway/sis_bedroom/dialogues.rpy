label jenny_bedroom_cannot_snoop:
    if game.timer.is_evening():
        scene expression "backgrounds/location_home_jennybedroom_jenny_evening_blur.jpg"
    elif game.timer.is_dark():
        scene expression "backgrounds/location_home_jennybedroom_night_blur.jpg"
    else:
        scene expression "backgrounds/location_home_jennybedroom_jenny_day_blur.jpg"
    show player 5 with dissolve
    player_name "( Eu não posso bisbilhotar com {b}[jen_name]{/b} Aqui! )"
    show player 4
    player_name "( Eu deveria voltar quando ela não estiver mais por perto. )"
    hide player
    return

label sis_bedroom_jenny_pregnancy_announcement_repeat:
    scene expression player.location.background_closeup
    show jenny f_upset a_dressed_crossed
    show player f_worried_talk with dissolve
    player_name "Você queria me ver?"
    show player f_worried
    show jenny f_upset_talk
    jen "Sim."
    jen "Parabéns, Boneco ... Estou grávida de novo."
    show jenny f_angry_pouting
    show player f_shock
    player_name "O que, de novo?!"
    show player f_worried
    show jenny f_angry_talk
    jen "Eu te disse para não gozar dentro de mim!"
    show jenny f_angry
    show player f_tired_talk
    player_name "{b}*Suspiro*{/b}"
    show player f_worried_talk
    player_name "Isso significa que você vai ficar toda maluca de novo?"
    show player f_worried
    show jenny f_angry_talk
    jen "COM LICENÇA?!"
    show jenny f_angry
    show player f_shock
    player_name "WHA"
    show player f_worried_talk
    player_name "Eu não quis dizer"
    show player f_surprised_teeth
    pause
    show player f_shock
    player_name "Por favor, não pegue o secador de cabelo..."
    show player f_surprised_teeth
    show jenny f_angry_talk
    jen "Apenas saia!"
    show jenny f_angry
    show player f_worried_talk
    player_name "Bem, aguente firme."
    player_name "Eu sei que isso não é uma situação ideal, mas estou aqui para você, sabe?"
    show player f_worried
    show jenny f_eyeroll
    jen "Ugh, Saia !"
    show jenny f_angry
    show player f_worried_talk
    player_name "Ok..."
    show player f_worried
    hide jenny with dissolve
    pause
    player_name "( Bem, eu tentei... )"
    hide player with dissolve
    return

label sis_bedroom_jenny_pregnancy_announcement_first:
    scene expression player.location.background_closeup
    show player f_worried_talk with dissolve
    player_name "Ei, eu vim assim que eu"
    show jenny f_angry_talk a_dressed_hit2 with dissolve
    show player 6 at left
    jen "Seu idiota!"
    show jenny a_dressed_hit with dissolve
    player_name "O que"
    show jenny a_dressed_hit2 with dissolve
    jen "Eu sabia que isso ia acontecer!"
    show jenny a_dressed_hit with dissolve
    player_name "Por que você está tão brava"
    show jenny a_dressed_hit2 with dissolve
    jen "VOCÊ ESTÚPIDO, IDIOTA, FILHA DA MÃE"
    show jenny a_dressed_hit with dissolve
    player_name "Pare de me bater!"
    show jenny f_angry a_dressed_upset with dissolve
    jen "Grrr!!!"
    show player f_skeptical_talk with dissolve
    player_name "AHH, O que deu em você?!"
    show player f_skeptical
    show jenny f_angry_talk
    jen "Sua batata desova A prole, é isso que!"
    show jenny f_angry
    show player f_skeptical_talk
    player_name "Hã?"
    show player f_skeptical
    show jenny f_angry_talk a_dressed_crossed with dissolve
    jen "Estou grávida, seu idiota!"
    show jenny f_angry
    show player f_shock
    player_name "!!!"
    player_name "Você está grávida?!"
    show player f_surprised_teeth
    show jenny f_angry_talk
    jen "Sim, Boneco!"
    jen "Você continuou gozando dentro de mim, o que você achou que ia acontecer?!"
    show jenny f_angry
    show player f_skeptical_talk
    player_name "Ei, isso não é justo!"
    player_name "Isso é tão culpa sua quanto minha..."
    show player f_skeptical
    show jenny f_eyeroll
    jen "Pfft, tanto faz."
    show jenny f_angry_pouting_top
    pause
    show player f_worried_talk
    player_name "Então, o que você vai dizer a {b}[deb_name]{/b}?"
    show player f_worried
    show jenny f_eyeroll
    jen "Ugh, Eu não sei..."
    show jenny f_angry_pouting_top
    show player f_worried_talk
    player_name "Ela vai descobrir isso eventualmente."
    show player f_worried
    show jenny f_upset_talk
    jen "Sim, mas não por um tempo, vou pensar em algo..."
    show jenny f_upset
    pause
    show player f_laugh
    player_name "eu vou ser pai de novo..."
    show player f_grin
    show jenny f_eyeroll
    jen "Sim, sinto muito pelo garoto coitadinho."
    show jenny f_angry_pouting_top
    show player f_normal_talk
    player_name "... E {b}[jen_name]{/b}, você vai ser mãe!"
    show player f_normal
    pause
    show player f_worried_talk
    player_name "Você não está nem um pouco animada?"
    show player f_worried
    show jenny f_sad
    pause
    show jenny f_sad_talk
    jen "Não"
    show jenny f_angry
    pause
    show jenny f_angry_talk a_dressed_upset with dissolve
    jen "Grr, Eu não posso acreditar que você está animado com isso!"
    show jenny f_angry
    player_name "..."
    show jenny f_angry_talk
    jen "Você é sempre uma dor na minha bunda, você sabe disso?!"
    show jenny f_angry a_dressed_crossed with dissolve
    show player f_worried_talk
    player_name "Eu sinto Muito?"
    show player f_worried
    show jenny f_eyeroll
    jen "Apenas, ugh ... Esqueça."
    show jenny f_upset_talk
    jen "Saia."
    show jenny f_upset
    show player f_worried_talk
    player_name "O que?!"
    show player f_worried
    show jenny f_angry_talk
    jen "Saia do meu quarto, {b}[firstname]{/b}!"
    hide jenny with dissolve
    show player f_worried_talk
    player_name "Ok..."
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup
    show player f_worried
    with fade
    player_name "( Eu não tenho certeza se ela sabe como se sentir agora... )"
    player_name "( ... E o que vai acontecer com a {b}[deb_name]{/b} quando ela descobrir?! )"
    show player f_surprised_teeth
    pause
    player_name "( Caralho, as coisas estão prestes a ficar muito mais complicadas por aqui... )"
    hide player with dissolve
    return

label sis_bedroom_jenny_cheerleader_sex:
    if store._in_replay is not None:
        $ player.location = L_home_sisbedroom
    scene expression player.location.background_closeup with None
    show player f_worried_talk
    show jenny f_upset
    with dissolve
    player_name "Tudo bem, peguei seu uniforme no sótão."
    show player f_worried
    show jenny f_gross_down_talk
    jen "Está tudo empoeirado?"
    show jenny f_gross
    show player f_worried_talk
    player_name "Não, parece bom"
    show player f_worried_talk
    show jenny f_upset_talk
    jen "Dê aqui!"
    show jenny f_upset_down a_dressed_hips_cheer with dissolve
    pause
    show jenny f_upset_down_talk
    jen "Hmm, terá que servir."
    show jenny f_upset_down
    player_name "..."
    show jenny f_upset_talk
    jen "Por que você ainda está com roupas?!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Uhh..."
    show player f_worried
    show jenny f_grin_down b_pull1 a_empty with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show player f_surprised
    pause
    show jenny b_panties a_naked_hips f_upset with dissolve
    show jenny f_upset_talk
    jen "Apresse-se, meus fãs estão esperando..."
    show jenny b_naked f_grin_down a_naked_panties_remove with dissolve
    show player f_worried_talk
    player_name "Certo..."
    show player f_worried
    show jenny b_cheer_dress1 f_empty a_empty
    show player b_dressed_changing a_empty f_empty
    with dissolve
    pause
    show player b_dressed_changing2 a_empty f_empty with dissolve
    pause
    show player b_underwear a_naked_sides f_worried_talk with dissolve
    player_name "O que vamos fazer hoje?"
    show player f_worried
    show jenny b_cheer_dress3 f_grin_talk with dissolve
    jen "Algo especial."
    show jenny b_cheer_dress2 f_empty with dissolve
    pause
    show jenny b_cheer a_cheer_hips f_sexy_talk with dissolve
    jen "Bem, o que você acha?"
    show jenny f_sexy
    show player f_worried_talk
    player_name "É um pouco pequeno..."
    show player f_worried
    show jenny f_laugh
    jen "Haha, mais que um pouco!"
    show jenny b_cheer_showoff a_empty f_sexy_talk with dissolve
    jen "É sexy, certo?"
    show jenny b_cheer_side f_overshoulder_back_look_normal at Position (align=(0,0)) with dissolve
    show player f_laugh
    player_name "Concerteza!"
    show player f_normal
    show jenny b_cheer a_cheer_hips f_sexy_talk with dissolve
    jen "Haha, bom!"
    jen "Suba na cama."
    show jenny f_sexy
    hide player with dissolve
    pause
    show jenny f_sexy_talk
    jen "... E coloque sua máscara!"
    show jenny f_sexy
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show player b_bed_jenny_sit a_empty f_jenny_bed_sit_shy_down of_jenny_bed_sit_mask at Position (align=(0,0))
    show jenny o_under_body_laptop o_naked_bed_belly_cheer b_naked_bed_bellytype a_empty f_bed_facing_comp_sexy_down at Position (align=(0,0))
    with dissolve
    pause
    show jenny f_bed_facing_comp_laugh
    jen "Hehe, Veja!"
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Eu disse a vocês que eu costumava ser líder de torcida."
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Sério?"
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Então você sempre quis foder uma líder de torcida, hein?"
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "E os outros garotos?!"
    jen "Você quer me ver fodida?"
    show jenny f_bed_facing_comp_sexy_down
    show player f_jenny_bed_sit_surprised
    player_name "( !!! )"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Você pode fazer melhor do que isso..."
    show jenny f_bed_facing_comp_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_facing_comp_laugh
    jen "Hehehe!"
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Tudo bem, deixe-me preparar as coisas..."
    show jenny b_bed_climbing a_empty f_empty o_cheer_bed_climbing
    show player b_bed_jenny_laying_undies_arms f_empty a_empty of_bed_jenny_laying_undies_arms_mask
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick7.png" zorder 2
    show expression "characters/jenny/layeredimage/jenny_overlay_o_laptop.png"
    with dissolve
    jump jenny_cheer_sex_intro_prepare

label sis_bedroom_jenny_get_cheerleader_outfit:
    show player f_worried
    show jenny f_upset_talk a_dressed_crossed
    with dissolve
    jen "O que você está fazendo?!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Você me disse para te encontrar aqui esta tarde."
    show player f_worried
    show jenny f_upset_talk
    jen "Sim, {b}com meu uniforme de cheerleading{/b}!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Oh, Certo"
    show player f_worried
    show jenny f_upset_talk
    jen "Apresse-se e vá {b}pegar no sótão{/b}!"
    hide jenny with dissolve
    jen "Idiota..."
    hide player with dissolve
    return

label sis_bedroom_jenny_start_camshow_blowjob:
    if store._in_replay is not None:
        $ player.location = L_home_sisbedroom
        scene expression player.location.background_blur with None
    show player f_worried
    with dissolve
    jen "A finalmente!"
    show jenny b_naked a_naked_hips f_upset_talk with dissolve
    jen "Vamos lá!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Voce esta nua..."
    show player f_worried
    show jenny f_upset_talk
    jen "Não merda, Estou vertida que pergunta idiota"
    jen "Todo mundo está esperando por você, Boneco!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Eu não estava"
    show player f_worried
    show jenny f_upset_talk
    jen "Vamos, tire suas roupas!"
    show jenny f_upset
    scene black with fade
    pause
    scene expression "backgrounds/location_home_jennybedroom_cutscene05.jpg" with dissolve
    jen "Coloque sua máscara!"
    player_name "eu sei."
    jen "Bem se apresse!"
    player_name "Pare de me puxar!"
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show player b_bed_jenny_sit a_empty f_jenny_bed_sit_shy_down of_jenny_bed_sit_mask at Position (align=(0,0))
    show jenny o_under_body_laptop b_naked_bed_bellytype a_empty f_bed_facing_comp_sexy_talk_down at Position (align=(0,0))
    with dissolve
    jen "É isso mesmo, estamos fazendo um show especial hoje..."
    show jenny b_naked_bed_belly f_bed_facing_comp_sexy_down with dissolve
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Você só vai ter que esperar e descobrir, não vai?"
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Ah, você quer ver um pau grande, hein?"
    jen "Bem, eu quero ver mais dicas!"
    show jenny f_bed_facing_comp_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Hehe, aqui vamos nós!"
    jen "Me dê um segundo para ter tudo configurado..."
    show jenny o_laptop b_bed_climbing a_empty f_empty
    show player b_bed_jenny_laying_undies_arms f_empty a_empty of_bed_jenny_laying_undies_arms_mask od_bed_jenny_laying_dick1
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick1.png"
    with dissolve
    player_name "O que você é"
    show jenny b_bed_back_sit a_bed_back_sit_handcuffs with dissolve
    jen "..."
    player_name "Ei, eu não concordei com algemas!"
    show jenny a_bed_back_sit_tie
    show player oh_bed_jenny_laying_undies_handcuffs
    with dissolve
    jen "Cale-se!"
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick1.png"
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick7.png"
    with dissolve
    if M_jenny.get("dominance") <= 0:
        jen "Você só está aqui para fazer o que eu digo, lembra?!"
        player_name "Sim..."
        jen "Eu acho que você quer dizer, \"Sim, {b}Princesa [jen_name]{/b}.\""
        player_name "Sim, {b}Princesa [jen_name]{/b}..."
        show jenny a_bed_back_sit_hips with dissolve
        jen "Hahahaah!"
    else:
        player_name "Isso não é engraçado {b}[jen_name]{/b}!"
        player_name "Tire isso de mim!"
        jen "Oh, apenas relaxe por um segundo."
        show jenny a_bed_back_sit_hips with dissolve
        jen "Você vai gostar disso, eu prometo."
        player_name "..."
    show jenny b_bed_back_look a_bed_back_look_up f_bed_back_look_normal with dissolve
    pause
    show jenny a_bed_back_look_butt f_bed_back_look_normal_talk with dissolve
    jen "Agora, vamos dar um ar grande para o cara, vamos?"
    show jenny b_bed_front_sit a_bed_front_sit_sides f_bed_front_sit_sexy_down with dissolve
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick7.png"
    show jenny a_bed_front_sit_pull1
    with dissolve
    pause
    show jenny a_bed_front_sit_pull2 f_bed_front_sit_sexy_talk_down with dissolve
    jen "Hehe, Parece que ele está pronto para dar a vocês um bom show."
    show player od_bed_jenny_laying_dick6
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    show jenny a_bed_front_sit_sides f_bed_front_sit_sexy_down
    with dissolve
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_front_sit_sexy_talk_down
    jen "Hoje não vai ser sobre ele embora..."
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    show jenny b_bed_front_laying a_empty f_bed_front_laying_sexy_down
    with dissolve
    pause
    show jenny f_bed_front_laying_sexy_talk_down
    jen "Hehe, está certo."
    jen "Hoje, meu brinquedinho vai aprender a comer buceta."
    show jenny f_bed_front_laying_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    player_name "O que?!"
    player_name "Que você està"
    show jenny b_bed_pussy1 f_bed_pussy1_sexy_down
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    with dissolve
    player_name "!!!"
    player_name "Mrphmmmll-"
    show jenny f_bed_pussy1_sexy_talk_down
    jen "O que Disse, garoto brinquedo?"
    jen "Nós não podemos te ouvir..."
    show jenny f_bed_pussy1_laugh
    jen "Hahahaah!"
    show player od_empty
    show jenny b_bed_pussy f_bed_pussy_sexy_talk_down
    with dissolve
    jen "Vamos para de lutar e enfiar a língua dentro da minha buceta!"
    show jenny f_bed_pussy_sexy_down
    pause
    show jenny f_bed_pussy_sexy_talk_down
    jen "{b}*Gasp*{/b} Oh, Sim!"
    jen "Aqui vamos nós!"
    show jenny f_bed_pussy_sexy_down
    pause
    show jenny f_bed_pussy_nipple2
    jen "Mmm, Huuuumm..."
    show jenny f_bed_pussy_sexy_down
    pause
    show jenny f_bed_pussy_sexy_talk_down
    jen "Ele é muito bom nisso, pessoal!"
    show jenny f_bed_pussy_nipple2
    jen "Ahh!"
    show jenny f_bed_pussy_nipple3
    pause
    show jenny f_bed_pussy_nipple2
    jen "Ngghhh, Issooo!"
    show jenny f_bed_pussy_nipple3
    jen "{b}*Whimper*{/b}"
    pause
    show jenny f_bed_pussy_nipple2
    jen "Ah Merda!"
    jen "OHHH, MERDA!"
    jen "Eu vou"
    show jenny f_bed_pussy_nipple3
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    pause
    show jenny b_bed_pussy1 f_bed_pussy1_nipple2
    jen "NGGHHH!!!" with flash
    pause
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    show jenny b_bed_front_laying a_empty f_bed_front_laying_nipple2
    show player od_bed_jenny_laying_dick6
    with dissolve
    jen "Haah... Haaah..."
    player_name "{b}*respiração penosa*{/b}"
    player_name "{b}*Sufocando* *Falar cuspindo* *Sufocando*{/b}"
    player_name "Eu pensei que você fosse me afogar!"
    show jenny f_bed_front_laying_laugh
    jen "Hehehe!"
    show jenny f_bed_front_laying_sexy_talk_down
    jen "Então meninos, como foi o show?"
    jen "Muito bom, né?"
    show jenny f_bed_front_laying_sexy_down
    pause
    jen "Hmm?"
    pause
    show jenny f_bed_front_laying_gross_down_talk
    jen "Eca, boquete não!"
    show jenny f_bed_front_laying_gross_down
    pause
    show jenny f_bed_front_laying_gross_down_talk
    jen "De jeito nenhum! Eu não faço isso!"
    show jenny f_bed_front_laying_gross_down
    pause
    show jenny f_bed_front_laying_gross_down_talk
    jen "Porque é nojento?"
    show jenny f_bed_front_laying_gross_down
    pause
    show jenny f_bed_front_laying_laugh
    jen "Heh,sim, certo..."
    show jenny f_bed_front_laying_sexy_talk_down
    jen "Vocês teriam que me dar uma gorjeta de dinheiro antes que eu considerasse"
    show jenny f_bed_front_laying_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_front_laying_surprised_down_talk
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "Ahh, vamos lá galera..."
    show jenny f_bed_front_laying_gross_down
    player_name "O que está acontecendo?"
    show jenny f_bed_front_laying_gross_down_talk
    jen "{b}*Suspiro*{/b} Eles querem que eu chupe seu pau..."
    show jenny f_bed_front_laying_gross_down
    player_name "!!!"
    show jenny f_bed_front_laying_gross_down_talk
    jen "Não há mais alguma coisa que eu possa fazer?"
    show jenny f_bed_front_laying_gross_down
    pause
    show jenny f_bed_front_laying_gross_down_talk
    jen "Ugh, Bem..."
    jen "... Mas não espere que isso se torne uma coisa normal!"
    show jenny f_bed_front_laying_gross_down
    player_name "{b}*Gole*{/b} Você realmente vai chupar meu pau?"
    show jenny b_bed_pussy1 f_bed_pussy1_upset
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    with dissolve
    player_name "!!!"
    show jenny f_bed_pussy1_upset_talk
    jen "Cale-se!"
    show jenny f_bed_pussy1_upset
    player_name "Mrphmmmll-"
    show jenny f_bed_pussy1_eyeroll
    jen "{b}*Suspiro*{/b} Eu não posso acreditar que estou fazendo isso..."
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg" with None
    show expression AnimatedImage("jenny_bj", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_bj at Position(xalign = 0.0, yoffset = 0)
    player_name "Nnnrrrmmph-" with hpunch
    jen "{b}*Gluullggh*{/b}"
    jump jenny_bj_loop

label sis_bedroom_jenny_get_a_mask_quest:
    scene expression player.location.background_closeup with None
    show jenny f_angry_talk
    show player 5 at left
    with dissolve
    jen "Já estava na hora!"
    show jenny f_angry
    show player 10
    player_name "Hã?"
    show player 5
    show jenny f_angry_talk
    jen "Eu não posso esperar para sempre!"
    show jenny f_angry
    show player 10
    player_name "Eu estou bem aqui!"
    show player 11
    show jenny f_angry_talk
    jen "Cale-se!"
    show jenny f_angry
    show player 5
    player_name "..."
    show jenny f_upset_talk
    jen "Ugh, essa é uma ideia tão ruim..."
    show jenny f_upset
    if M_jenny.get("dominance") <= 0:
        show player 12
        player_name "Você vai me dizer"
        show player 5
        show jenny f_upset_talk
        jen "Eu não te disse para calar a boca?!"
        show jenny f_upset
        show player 10
        player_name "Sim"
        show player 5
        show jenny f_upset_talk
        jen "Então, por que você ainda está falando?!!"
        show jenny f_upset
        show player 10
        player_name "Me desculpe eu-"
        show player 11
        show jenny f_upset_talk
        jen "Não se desculpe, fique quieto!"
        show jenny f_upset
        show player 5
        player_name "..."
        jen "..."
        show jenny f_eyeroll
        jen "Finalmente!"
        show jenny f_upset_talk
        jen "{b}*Suspiro*{/b} Tudo bem, aqui está o acordo."
        jen "Como eu tenho certeza que você já percebeu isso, eu tenho feito shows por dinheiro recentemente..."
        jen "Eu sei que não é a profissão mais glamourosa, mas está trazendo muito dinheiro."
        show jenny f_upset
        show player 10
        player_name "Você sabe se a {b}[deb_name]{/b} descobrir vai matar você, certo?"
        show player 5
        show jenny f_upset_talk
        jen "{b}[deb_name]{/b} não vai descobrir!"
        show jenny f_upset
        player_name "..."
        show jenny f_angry_talk
        jen "Eu juro por Deus, eu vou te matar se você disser uma palavra para ela!"
        show jenny f_angry
        show player 10
        player_name "{b}*Gole*{/b} Eu não faria isso."
        player_name "Quer dizer, eu não vou contar nada a ela!"
        show player 5
        show jenny f_angry_talk
        jen "Droga certo você!"
        show jenny f_upset
        pause
        show jenny f_upset_talk
        jen "Na verdade, você vai me ajudar."
        show jenny f_upset
        show player 11
        player_name "Hmm?"
        show jenny f_upset_talk
        jen "Você vê, meus fãs estão cansados de me ver apenas com brinquedos."
        jen "Eles querem me ver com um cara de verdade e eu não posso arrumar qualquer pessoa..."
        show jenny f_eyeroll a_dressed_crossed with dissolve
        jen "Você terá que fazer."
        show jenny f_upset
        show player 12c with dissolve
        player_name "Eu?!"
        show player 5 with dissolve
        show jenny f_upset_talk
        jen "Sim você."
        show jenny f_upset
        show player 10
        player_name "Você está falando, tipo ... sexo?"
        show player 5
        show jenny f_gross
        jen "Sexo?! Eca, não!"
        show jenny f_angry_talk
        jen "Que diabo qual é o seu problema?!"
        show jenny f_gross
        show player 10
        player_name "Mas"
        show player 5
        show jenny f_angry_talk
        jen "Como se eu fosse fazer sexo com você, nojento!"
        show jenny f_gross
        show player 12
        player_name "Ok, estou confuso."
        show player 5
        show jenny f_eyeroll
        jen "Você é um idiota."
        show jenny f_gross
        show player 10
        player_name "O que você quer que eu faça?"
        show player 5
        show jenny f_upset_talk
        jen "Eu quero que você se sente na cama e mantenha a boca fechada."
        jen "Você acha que consegue fazer isso?!"
        show jenny f_upset
        show player 10
        player_name "Concerteza."
        show player 5 at Position (xoffset=50) with dissolve
        show jenny f_upset_talk
        jen "Não agora, idiota!"
        show jenny f_upset
        show player 10 with dissolve
        player_name "Mas você acabou de dizer"
        show player 5
        show jenny f_upset_talk
        jen "Nós não vamos transmitir neste segundo!"
        jen "Além disso, precisamos de algumas coisas primeiro."
        show jenny f_upset
        show player 10
        player_name "Como o quê?"
        show player 5
        show jenny f_upset_talk
        jen "Você precisa de uma máscara ou algo assim."
        show jenny f_upset
        show player 10
        player_name "Mascara?"
        show player 5
        show jenny f_upset_talk
        jen "Sim, para cobrir seu rosto."
        show jenny f_upset
        show player 10
        player_name "Porque?"
        show player 5
        show jenny f_angry_talk
        jen "Umm, porque eu não quero que ninguém saiba quem é você, Boneco!"
        show jenny f_upset_talk
        jen "Você tem alguma ideia do que as pessoas diriam se me vissem fazendo coisas com você?!"
        show jenny f_eyeroll
        jen "Ugh, Eu nem quero pensar nisso."
        show jenny f_gross
        show player 10
        player_name "AH."
        show player 5
        show jenny f_upset_talk a_dressed_hips with dissolve
        jen "Então corra para {b}O Shopping{/b} e pegar uma máscara de esqui ou algo assim..."
        show jenny f_upset
        show player 10
        player_name "E se eles não tiverem máscaras de esqui?"
        show player 5
        show jenny f_upset_talk
        jen "Então descubra alguma coisa, perdedor!"
        show jenny f_upset
        show player 24
        player_name "{b}*Suspiro*{/b} Està bem."
        show player 10
        player_name "Algo mais?"
        show player 5
        show jenny f_upset_talk
        jen "Não, vou pegar as outras coisas."
        jen "Somente {b}não volte aqui sem uma máscara{/b}, entendeu?!"
        show jenny f_upset
        show player 10
        player_name "É, eu entendi."
        show player 5
        show jenny f_upset_talk
        jen "Bom."
        jen "Agora Some!"
        hide jenny with dissolve
        pause
        show player 24
        player_name "{b}*Suspiro*{/b}"
        show player 37 with dissolve
        player_name "( Tudo bem, eu deveria ir para {b}O Shopping{/b} e procurar por {b}uma máscara{/b}. )"
        hide player with dissolve
    else:
        show player 12
        player_name "Você poderia me dizer o que está acontecendo?!"
        show player 5
        show jenny f_upset_talk
        jen "Não levante sua voz comigo!"
        jen "Você tem sorte de eu mesmo considerar"
        show jenny f_upset
        show player 12
        player_name "Ok, eu vou sair daqui."
        show player 5f with dissolve
        show jenny f_upset_talk
        jen "Não, espere!!"
        show player 5 with dissolve
        jen "Deus droga..."
        show jenny f_eyeroll
        jen "{b}*Suspiro*{/b} Eu preciso da sua ajuda, ok?"
        show jenny f_gross
        show player 12
        player_name "Se você vai agir como uma cadela, então você pode esquecer minha ajuda."
        show player 5
        show jenny f_upset_talk
        jen "Grr, Bem"
        show jenny f_eyeroll
        jen "Eu vou ... Ugh....ser legal."
        show jenny f_gross
        show player 10
        player_name "Okay, certo."
        show player 5
        show jenny f_upset_talk
        jen "Você!"
        show jenny f_angry_pouting_top
        pause
        show jenny f_upset_talk
        jen "Posso pelo menos explicar a situação?"
        show jenny f_upset
        show player 10
        player_name "Ok, explicar."
        show player 5
        show jenny f_eyeroll
        jen "{b}*Suspiro*{/b} Como eu tenho certeza que você já percebeu isso, eu tenho feito camshows por dinheiro recentemente."
        show jenny f_upset
        show player 14
        player_name "Ahh, Sim ... Não foi exatamente difícil de juntar as peças, {b}[jen_name]{/b}."
        show player 13
        show jenny f_angry_talk
        jen "Não ria, é um bom dinheiro!"
        show jenny f_angry
        show player 17
        player_name "Ahh, tudo bem, mas você sabe se a {b}[deb_name]{/b} descobrir vai matar você, certo?"
        show player 13
        show jenny f_angry_talk
        jen "Você disse alguma coisa a ela?"
        show jenny f_angry
        show player 14
        player_name "Não, eu não falei nada."
        show player 13
        pause
        show jenny f_eyeroll
        jen "Ufa, isso é bom!"
        show jenny f_upset_talk
        jen "Se a {b}[deb_name]{/b} descobrir eu te mato."
        show jenny f_upset
        show player 14
        player_name "Então, com o que você quer minha ajuda?"
        show player 13
        show jenny f_sad_talk
        jen "Bem é isso..."
        jen "Entende..."
        show jenny f_sad
        show player 11
        player_name "..."
        show player 14
        player_name "Fala logo."
        show player 13
        show jenny f_sad_talk
        jen "Meus fãs... Bem, eles estão cansados de me ver com brinquedos..."
        show jenny f_sad
        pause
        show player 14
        player_name "E?"
        show player 13
        show jenny f_sad_talk
        jen "... E eles estão oferecendo para me pagar um monte de dinheiro, se eu puder encontrar um homem para transmitir."
        show jenny f_sad
        show player 22
        player_name "!!!"
        show player 10
        player_name "Você não pode estar falando sério..."
        show player 5
        show jenny f_upset_talk a_dressed_crossed with dissolve
        jen "Por que não?"
        jen "Estúpido {b}Cedric{/b} não vai fazer isso, mais você ... poderia fazer."
        show jenny f_upset
        show player 10
        player_name "Não na câmera?"
        show player 5
        show jenny f_upset_talk
        jen "Não seja um frango."
        show jenny f_upset
        show player 10
        player_name "E se eles descobrirem quem somos?!"
        show player 5
        show jenny f_upset_talk
        jen "Eles não vão."
        show jenny f_grin_talk
        jen "Você vai usar uma máscara."
        show jenny f_grin
        show player 12
        player_name "Hã?"
        show player 5
        show jenny f_upset_talk
        jen "Sim, nós só precisamos te dar uma máscara de esqui ou algo assim."
        show jenny f_upset
        show player 10
        player_name "Estamos no meio do verão..."
        player_name "Onde vamos encontrar uma máscara de esqui?!"
        show player 5
        show jenny f_upset_talk
        jen "Não tem que ser uma máscara de esqui, pode ser outra qualquer."
        show jenny a_dressed_facepalm with dissolve
        jen "{b}*Suspiro*{/b} Somente {b}vá ao shoping{/b} e encontra {b}a mascara{/b}!"
        jen "Qualquer {b}máscara{/b} Certo."
        show jenny f_upset a_dressed_hips with dissolve
        show player 12
        player_name "Eu vou ser pago por isso?"
        show player 5
        jen "..."
        show jenny f_upset_talk
        jen "Você pode me tocar, isso é pagamento suficiente."
        show jenny f_upset
        show player 12
        player_name "Não, eu quero minha fatia do bolo."
        show player 5
        show jenny f_angry
        jen "..."
        show player 12
        player_name "Você não vai conseguir esse dinheiro sem mim..."
        show player 5
        show jenny f_angry_talk
        jen "Oh meu Deus, tudo bem!"
        jen "Porra você e uma dor na minha bunda..."
        show jenny f_angry
        show player 14
        player_name "Bom."
        show player 13
        show jenny f_angry_talk
        jen "Apenas saia!"
        hide jenny with dissolve
        jen "E não volte sem {b}a mascara{/b}!"
        show player 4 with dissolve
        player_name "( Hmm, Eu me pergunto o que ela está planejando fazer para o streams? )"
        pause
        player_name "( Eu vou ter que {b}comprar uma máscara{/b} se eu quiser descobrir... )"
        player_name "( Eu deveria {b}ir para o shopping e comprar uma mascara{/b}. )"
        hide player with dissolve
    return

label jenny_bedroom_jenny_deliver_bad_monster:
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg"
    show jenny b_bed_reading a_bed_phone1 f_bed_lay_way_back_laugh at Position (yoffset=62) with dissolve
    jen "Você pode acreditar nisso?!"
    pause
    show jenny f_bed_lay_way_back_happy_talk at Position (yoffset=62)
    jen "Sim, eu disse a ele quanto dinheiro estava trazendo, mas ele está sendo um pouco puto sobre isso!"
    show jenny f_bed_lay_way_back_happy at Position (yoffset=62)
    pause
    show jenny f_bed_lay_way_back_happy_talk at Position (yoffset=62)
    jen "Não, ele não fará isso."
    show jenny f_bed_lay_way_back_laugh at Position (yoffset=62)
    jen "Haha! Sim, eu sei!"
    show jenny f_bed_lay_way_back_happy at Position (yoffset=62)
    pause
    show jenny f_bed_lay_way_back_happy_talk at Position (yoffset=62)
    jen "Eu não sei, eu vou encontrar alguém eventualmente..."
    show player 13 at left with dissolve
    show jenny f_bed_lay_way_back_upset at Position (yoffset=62)
    jen "!!!"
    show jenny f_bed_lay_way_back_upset_talk a_bed_phone2 at Position (yoffset=62) with dissolve
    jen "Estou no telefone!"
    show jenny f_bed_lay_way_back_upset at Position (yoffset=62)
    show player 14
    player_name "Eu tenho uma coisa pra você."
    show player 13
    show jenny f_bed_lay_way_back_surprised at Position (yoffset=62)
    jen "Hã?"
    show jenny f_bed_lay_way_back_angry at Position (yoffset=62)
    show player 14
    player_name "Um presente."
    show player 13
    show jenny f_bed_lay_way_back_upset_talk at Position (yoffset=62)
    jen "Você me comprou alguma coisa?"
    show jenny f_bed_lay_way_back_upset at Position (yoffset=62)
    show player 14
    player_name "Sim."
    show player 13
    show jenny f_bed_lay_way_back_upset_talk at Position (yoffset=62)
    jen "Isso foi caro?"
    show jenny f_bed_lay_way_back_upset at Position (yoffset=62)
    player_name "..."
    show player 14
    player_name "Sim."
    show player 13
    show jenny f_bed_lay_way_back_happy_talk a_bed_phone1 at Position (yoffset=62) with dissolve
    jen "{b}Jane{/b}, Eu vou ter ligar de volta."
    show jenny f_bed_lay_way_back_happy at Position (yoffset=62)
    pause
    show jenny f_bed_lay_way_back_happy_talk at Position (yoffset=62)
    jen "Haha, Sim ... tenho certeza que eles adorariam isso."
    show jenny f_bed_lay_way_back_happy at Position (yoffset=62)
    pause
    show jenny f_bed_lay_way_back_happy_talk at Position (yoffset=62)
    jen "Eu vou manter isso em mente..."
    jen "Você é uma puta!"
    show jenny f_bed_lay_way_back_happy at Position (yoffset=62)
    pause
    show jenny f_bed_lay_way_back_laugh at Position (yoffset=62)
    jen "Haha, tchau!"
    show jenny f_bed_upset b_bed_dressed a_bed_dressed_down with dissolve
    pause
    show jenny f_bed_upset_talk
    jen "Ok, é melhor que seja bom."
    show jenny f_bed_upset
    show player 239_240 with dissolve
    pause
    show player 286g
    show jenny f_bed_surprised
    jen "!!!" with hpunch
    jen "O que {b}Monstro Ruim{/b}?!"
    show player 286
    player_name "Sim."
    show player 286g
    jen "Como você"
    show jenny f_bed_upset_talk
    jen "Por que você comprou isso para mim?!"
    show jenny f_bed_upset
    show player 286
    player_name "Bem você"
    show player 286e
    show jenny f_bed_angry_talk
    jen "Você leu meu diário?"
    show jenny f_bed_angry
    show player 286d
    player_name "O que?"
    player_name "Não!"
    player_name "Você comprar brinquedos sexuais para você, Eu ouvi dizer que esse e o melhor ..."
    show player 286e
    pause
    show player 286d
    player_name "Eu não li o seu diário! Merda!"
    show player 286e
    show jenny f_bed_angry_talk
    jen "É melhor você não te lido mesmo!"
    jen "Me dê isso!"
    show jenny f_bed_grin_down a_bed_dressed_hips_toy4b
    show player 5
    with dissolve
    pause
    show jenny f_bed_grin_down_talk
    jen "É incrivel..."
    show player 13
    jen "Eles vão enlouquecer por isso!"
    show jenny f_bed_grin_down
    show player 14
    player_name "Quem vai?"
    show player 13
    show jenny f_bed_upset
    jen "Hmm?"
    show jenny f_bed_upset_talk
    jen "Oh, uhh ... Ninguém!"
    jen "Apenas cale a boca e saia!"
    show jenny f_bed_upset
    show player 10
    player_name "Você nem vai dizer obrigado?"
    show player 90
    if M_jenny.get("dominance") <= 0:
        show jenny f_bed_eyeroll
        jen "Uhh, não?"
        show jenny f_bed_upset_talk
        jen "Eu sei que provavelmente há algum motivo assustador por trás disso..."
        show jenny f_bed_upset
        show player 29 with dissolve
        player_name "Não, não há!"
        player_name "Não posso fazer algo de bom para você?"
        show player 3
        show jenny f_bed_upset_talk
        jen "Sim certo, tanto faz."
    else:
        show jenny f_bed_eyeroll
        jen "Ugh, Obrigada."
        show jenny f_bed_upset
        show player 29
        player_name "Seja bem-vindo."
        show player 3
    show jenny f_bed_angry_talk
    jen "Agora saia!"
    show jenny f_bed_angry
    show player 24 with dissolve
    player_name "{b}*Suspiro*{/b} Està bem."
    hide player with dissolve
    pause
    show jenny f_bed_grin_down_talk
    jen "Hehehehehe!"
    scene black with fade
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 90 with dissolve
    player_name "( Resultado mal intencionado típico... )"
    pause
    show player 403
    player_name "( Oh bem, talvez ela faça outro vídeo no {b}Perfil de CAMslut{/b}! )"
    player_name "( Eu só vou ter que esperar e {b}verificar de manhã, haha como sou esperto.{/b} )"
    hide player with dissolve
    return

label upstairs_bedroom_jenny_figure_out_password:
    scene expression player.location.background_closeup with None
    show player 11 with dissolve
    player_name "( Tudo bem, eu tenho que ficar quieto aqui... )"
    player_name "( Eu só preciso {b}logar em seu laptop{/b} e encontrá-la na {b}CAMslut{/b} . )"
    show player 403
    player_name "( Mole mole... )"
    hide player with dissolve
    return

label sis_bedroom_jenny_get_a_toy:
    scene expression player.location.background_blur with None
    show player 10 at left
    show jenny
    with dissolve
    player_name "Tudo bem, estou aqui."
    player_name "O que você quer?"
    show player 5
    show jenny a_dressed_hips f_normal_talk with dissolve
    jen "Eu encontrei outra maneira de ganhar dinheiro."
    jen "Melhor do que esse estúpido {b}Sluttygram{/b} site."
    show jenny f_normal
    show player 10
    player_name "Okay."
    player_name "O que é isso?"
    show player 5
    show jenny f_normal_talk
    jen "Não é da sua conta, perdedor."
    show jenny f_normal
    player_name "..."
    return

label sis_bedroom_jenny_get_a_toy_submissive:
    show player 10
    player_name "{b}*Suspiro*{/b} Vamos lá, {b}[jen_name]{/b}..."
    show player 5
    show jenny f_upset_talk
    jen "Você calaria a boca e escutaria!"
    show jenny f_upset
    player_name "..."
    show jenny f_normal_talk
    jen "Eu preciso que você vá ao shopping e compre algo para mim."
    show jenny f_normal
    show player 12
    player_name "Por que sempre se resume a dinheiro com você?"
    show player 5
    show jenny f_normal_talk
    jen "Umm, porque você não tem mais nada para me oferecer?"
    jen "Não é tão caro assim, são apenas cem dólares..."
    show jenny f_normal
    show player 11
    pause
    show player 10
    player_name "Mais cem?!"
    player_name "Eu não sei, isso me parece muito dinheiro!"
    show player 11
    show jenny f_upset_talk
    jen "Se você me comprar isso, vou tirar toda a roupa para você."
    show jenny f_upset
    show player 12
    player_name "Você vai ficar completamente nua?"
    show player 11
    show jenny f_upset_talk
    jen "Por dois minutos..."
    show jenny f_angry_talk
    jen "Mas sem me tocar!"
    show jenny f_upset
    show player 4 with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "Tudo bem."
    player_name "Eu acho que vale cem dólares"
    show player 5
    show jenny f_eyeroll
    jen "Vale muito mais do que cem dólares"
    show jenny f_upset_talk
    jen "Estou sendo generosa com você..."
    show jenny f_upset
    return

label sis_bedroom_jenny_get_a_toy_end:
    show player 10
    player_name "Então, O que irei comprar?"
    show player 5
    show jenny f_normal_talk
    jen "Eu preciso que você vá para {b}O shoping{/b} e olhe {b}o segundo andar{/b} para uma loja chamada {b}Pink{/b}."
    show jenny f_normal
    show player 10
    player_name "{b}Pink{/b}, Am?"
    player_name "Okay..."
    show player 5
    show jenny f_normal_talk
    jen "O brinquedo que eu quero é chamado, {b}De Electro Clit.{/b}"
    show jenny f_normal
    show player 10
    player_name "Brinquedo?"
    player_name "Você não acha que tá bem crescidinha, para brinquedos?"
    show player 5
    show jenny f_upset_talk
    jen "É uma sex shop, Boneco..."
    show jenny f_upset
    show player 23
    player_name "!!!" with hpunch
    show player 12c with dissolve
    player_name "Você está pedindo, para que eu vá a uma sex shop?!"
    show player 12 with dissolve
    player_name "De jeito nenhum!"
    show player 5
    show jenny f_grin_talk
    jen "É um pequeno virgem com medo de uma grande loja de sexo assustador?"
    show jenny f_grin
    show player 10
    player_name "O que não..."
    player_name "Eu... Por que você não pode ir?!"
    player_name "Eu vou te dar o dinheiro e você pode muito bem fazer isso"
    show player 5
    show jenny f_eyeroll
    jen "Eu tenho outras coisas que preciso fazer!"
    show jenny f_upset_talk
    jen "Seja homem e vai, doofus."
    show jenny f_upset
    show player 10
    player_name "Está bem."
    show player 5
    show jenny f_eyeroll
    pause
    hide jenny with dissolve
    pause
    player_name "( Eu não posso acreditar que ela está me fazendo passar por isso... )"
    show player 37 with dissolve
    player_name "( Ugh, Vamos acabar logo com isso. )"
    hide player with dissolve
    return

label sis_bedroom_jenny_get_a_toy_dominant:
    show player 10
    player_name "Ok, até mais."
    show player 5f with dissolve
    pause
    show jenny f_sad_talk a_dressed_upset with dissolve
    jen "Não, espere!"
    show jenny f_sad
    show player 5 with dissolve
    show jenny f_angry_pouting a_dressed_crossed
    pause
    show jenny f_upset_talk
    jen "Eu não quero dizer, é embaraçoso..."
    show jenny f_upset
    show player 12
    player_name "Mesmo?"
    player_name "Eu não acho que já vi você envergonhada sobre qualquer coisa antes."
    show player 5
    show jenny f_upset_talk
    jen "Você pode me ajudar, por favor?"
    show jenny f_upset
    show player 10
    player_name "{b}*Suspiro*{/b} bem."
    player_name "... Mas só porque você me pediu com jeitinho."
    show player 5
    show jenny f_eyeroll
    jen "Sim, sim, tanto faz."
    show jenny f_upset_talk
    jen "Eu preciso que você vá ao shopping e compre algo para mim."
    show jenny f_upset
    show player 12
    player_name "Por que sempre se resume a dinheiro com você?"
    show player 5
    show jenny f_upset_talk
    jen "Não seja um idiota, você sabe que eu preciso do dinheiro."
    jen "Não é tão caro assim, são apenas cem dólares..."
    show jenny f_upset
    show player 23
    player_name "Isto é muito dinheiro, {b}[jen_name]{/b}!"
    show player 11
    show jenny f_eyeroll
    jen "Não seja idiota, cem dólares não são nada."
    show jenny f_upset
    show player 12
    player_name "{b}*Suspiro*{/b} O quê eu ganho?"
    show player 5
    show jenny f_upset_talk
    jen "Eu não sei, eu acho ... que vou tirar toda minha roupa pra você?"
    show jenny f_upset
    show player 17
    player_name "Você vai ficar completamente nua na minha frente, mas você não vai me dizer qual o seu plano para esse dinheiro?"
    show player 13
    show jenny f_angry_talk
    jen "Você quer me ver nua ou não?"
    show jenny f_angry
    show player 4 with dissolve
    player_name "..."
    show player 14 with dissolve
    player_name "Tudo bem, claro."
    show player 26
    player_name "... Mas eu posso olhar o quanto quiser?"
    show player 13
    show jenny f_eyeroll
    jen "Ugh, bem ... Dentro da razão."
    show jenny f_upset_talk
    jen "... E nem ouse me tocar  porque isso não vai acontecer, pervertido!"
    show jenny f_upset
    show player 14
    player_name "Sim Sim..."
    return

label jenny_bedroom_jenny_go_to_her_room_dominant:
    scene expression player.location.background_closeup with None
    show jenny f_upset at flip
    show jenny at Position (xpos=500)
    show player 10 at left
    with dissolve
    player_name "Ouça, {b}[jen_name]{/b} Eu não estava tentando"
    hide jenny
    show jenny f_grin_down b_pull1 a_empty
    with dissolve
    pause
    show jenny b_pull2 f_empty
    show player 22
    player_name "!!!" with hpunch
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show jenny b_groping a_groping_hips f_upset with dissolve
    show player 23
    player_name "O que você está fazendo?"
    show player 428
    show jenny f_upset_talk
    jen "Diga-me, estes não são os pares de seios mais gostosos que você já viu?!"
    show jenny f_upset
    show player 427
    player_name "Concerteza..."
    player_name "{b}*Gole*{/b} Isso é muito legal!"
    show player 427g
    show jenny f_upset_talk
    jen "Isso foi o que eu pensei."
    show jenny f_eyeroll
    jen "Merda!"
    jen "... Eu deveria ter feito você pagar por isso."
    show jenny f_upset
    show player 429
    player_name "Sim posso pagar."
    show player 426
    show jenny f_surprised
    jen "Hmm?"
    show player 429
    player_name "Se você me deixar tocá-los."
    show player 426
    show jenny f_eyeroll
    jen "Okay, certo!"
    show jenny f_upset_talk
    jen "Nos seus sonhos, perdedor!"
    show jenny f_upset
    player_name "..."
    show player 429
    player_name "Bem vou indo."
    show player 5f with dissolve
    pause
    show jenny f_sad
    hide player with dissolve
    pause
    show jenny f_sad_talk
    jen "Espere!"
    show jenny f_sad
    show player 426 at left with dissolve
    pause
    show jenny f_upset_talk
    jen "Duzentos Dólares."
    show jenny f_upset
    show player 429
    player_name "O que?"
    show player 426
    show jenny f_upset_talk
    jen "Duzentos e você pode tocá-los."
    show jenny f_upset
    show player 429
    player_name "Tudo bem."
    show player 426
    show jenny f_eyeroll
    jen "... Eu não posso acreditar que estou fazendo isso."
    show jenny f_upset_talk
    jen "Você tem sorte de eu precisar do dinheiro."
    show jenny f_upset
    return

label jenny_bedroom_jenny_go_to_her_room_dominant_has_money:
    show player 638 with dissolve
    player_name "Aqui."
    show player 640b

    show jenny f_eyeroll
    jen "Eu deveria ter pedido trezentos..."
    show jenny f_upset
    show player 640e
    player_name "Tarde demais agora."
    show player 426 with dissolve
    if M_jenny.finished_state(S_jenny_go_to_her_room):
        show jenny f_grin_down b_pull1 a_empty
        with dissolve
        pause
        show jenny b_pull2 f_empty
        pause
        show jenny b_pull3 with dissolve
        show jenny b_pull4 with dissolve
        pause
        show jenny b_groping a_groping_hips f_upset_talk with dissolve
    else:
        show jenny f_upset_talk
    jen "Apenas se apresse."
    hide player
    show jenny b_groping_touch_look f_upset
    with dissolve
    pause
    show jenny b_groping_touch_talk
    player_name "Uau!"
    player_name "Eles são tão macios!"
    show jenny f_eyeroll b_groping_touch
    jen "Bem, sim, manequim."
    show jenny f_upset
    pause
    show jenny a_groping_up f_sad_talk with dissolve
    jen "Mmm, seja cuidadoso!"
    jen "Meus mamilos são sensíveis!"
    show jenny f_sad
    pause
    show jenny b_groping_suck a_groping_up_clench f_nipple2
    jen "!!!" with hpunch
    show jenny f_nipple1
    jen "Eu nunca disse que você poderia"
    show jenny f_nipple2
    jen "Ahh!"
    pause
    jen "Meeerrrddaa"
    pause
    show jenny f_angry_talk b_cover a_empty
    show player 24 at left
    with dissolve
    jen "Pare!"
    jen "É demais, não posso deixar..."
    show jenny f_angry
    pause
    show jenny f_angry_talk
    jen "Ugh, você é tão pervertido!"
    show jenny f_angry
    show player 14
    player_name "Você gostou."
    show player 13
    show jenny f_angry_talk
    jen "Nem um pouco!"
    show jenny f_angry
    show player 17
    player_name "Mentirosa."
    show player 13
    show jenny f_angry_talk
    jen "Apenas saia."
    show jenny f_angry
    show player 14
    player_name "Está bem."
    player_name "Prazer fazer negócios com você, {b}[jen_name]{/b}."
    hide player with dissolve
    show jenny f_angry_talk
    jen "Cale-se!"
    show jenny f_angry

    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 17 with dissolve
    player_name "( Uau, ela tem os melhores peitos do mundo. )"
    player_name "( Eu não posso acreditar que ela está me deixando tocá-los! )"
    player_name "( Isso é incrível! )"
    hide player with dissolve
    return

label jenny_bedroom_jenny_go_to_her_room_dominant_no_money:
    show player 10
    player_name "Eu não tenho duzentos."
    show player 5
    show jenny f_upset_talk
    jen "Ugh, a sério?!"
    jen "Bem, você não vai tocar neles de graça!"
    show jenny f_upset
    show player 10
    player_name "Eu vou te dar tudo o que tenho."
    show player 5
    show jenny f_upset_talk
    jen "De jeito nenhum!"
    jen "Se você acha que eu estou deixando você tocá-los por nada menos que duzentos, você está louco!"
    show jenny f_upset
    player_name "..."
    show player 10
    player_name "{b}*Suspiro*{/b} bem."
    player_name "{b}Volto com o dinheiro então{/b}."
    show player 5
    show jenny f_upset_talk
    jen "Apresse-se, perdedor."
    jen "Eu preciso desse dinheiro!"
    show jenny f_upset
    show player 10
    player_name "Sim Sim."
    hide player
    hide jenny
    with dissolve
    return

label jenny_bedroom_jenny_go_to_her_room_submissive:
    scene expression player.location.background_closeup with None
    show jenny a_phone f_grin_down at flip
    show jenny at Position (xpos=500)
    show player 10 at left
    with dissolve
    player_name "Ouça {b}[jen_name]{/b} Eu não estava tentando"
    show player 5 with None
    hide jenny
    show jenny b_dressed a_dressed_hips f_upset_talk
    with dissolve
    jen "Apenas cale a boca..."
    jen "Eu tenho uma proposta para você."
    show jenny f_upset
    show player 10
    player_name "Certo o que?"
    show player 5
    show jenny f_grin_talk
    jen "Você é um pequeno perdedor excitado, certo?"
    show jenny f_grin
    show player 29 with dissolve
    player_name "O que?! Não..."
    show player 3
    show jenny f_upset_talk a_dressed_crossed with dissolve
    jen "E eu preciso de dinheiro, então..."
    show jenny f_upset
    pause
    show jenny f_eyeroll
    jen "... Que tal você me pagar duzentos dólares e eu deixo você olhar para as minhas tetas?"
    show jenny f_upset
    show player 12 with dissolve
    player_name "Duzentos dólares?!"
    show player 10
    player_name "Eu não sei, isso é muito dinheiro..."
    show player 5
    show jenny f_upset_talk
    jen "Sim, mas estamos falando como verdadeiros peitos reais aqui."
    jen "Não te Anima ver seios, perdedor."
    show jenny f_upset
    show player 4 with dissolve
    player_name "..."
    show player 92
    player_name "Bem."
    return

label jenny_bedroom_jenny_go_to_her_room_submissive_has_money:
    show player 640e with dissolve
    player_name "Aqui."
    show player 13

    show jenny f_grin_down a_dressed_money_counting
    with dissolve
    pause
    show jenny f_eyeroll a_dressed_hips with dissolve
    jen "Eu deveria ter pedido trezentos..."
    show jenny f_gross
    pause
    show jenny f_upset_talk
    jen "{b}*SUSPIRO*{/b}"
    label repeat_boobies:
    jen "Espero que você possa apreciar a sorte que tem."
    show jenny f_grin_down b_pull1 a_empty with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4
    show player 428
    player_name "!!!" with hpunch
    show jenny b_groping a_groping_hips f_grin with dissolve
    show player 429
    player_name "Uau..."
    show jenny f_grin_talk
    jen "Coloque sua língua de volta em sua boca, nerd!"
    show jenny f_grin
    pause
    player_name "Eles são tão"
    show jenny f_grin_talk
    jen "Belos."
    show player 731 with dissolve
    jen "Eu sei."
    show jenny f_grin
    pause
    hide player
    show jenny f_surprised b_groping_touch1 a_groping_up
    jen "!!!" with hpunch
    show player 732
    show jenny f_angry_talk b_cover a_empty
    with dissolve
    jen "Ei, sem tocar!"
    show jenny f_angry b_groping a_groping_up_clench
    show player 24 at left
    with dissolve
    player_name "Desculpe, eu não queria"
    show jenny f_upset_talk a_groping_hips with dissolve
    jen "Pequenos perdedores patéticos não conseguem tocar!"
    show player 11
    show jenny b_pull1 a_empty with dissolve
    jen "Acho que é o bastante..."
    show jenny b_dressed a_dressed_hips f_upset with dissolve
    show player 12
    player_name "Ah, vamos!"
    show player 90
    show jenny f_upset_talk with dissolve
    jen "Não, você já teve o suficiente por hoje."
    show jenny f_grin_talk
    jen "Você quer olhar de novo, você sabe o preço."
    show jenny f_grin
    show player 10
    player_name "Duzentos Dólares?"
    show player 5
    show jenny f_grin_talk
    jen "Está certo."
    show jenny f_upset_talk
    jen "Agora saia."
    hide jenny with dissolve
    pause
    show player 29 with dissolve
    player_name "Ah, puta merda, Isso foi bom pra caralho..."
    hide player with dissolve
    pause

    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with None
    show player 17 with dissolve
    player_name "( Uau, ela tem os melhores peitos do mundo. )"
    show player 26
    player_name "( Eu queria, poder tocá-los... )"
    player_name "( Talvez na próxima vez? )"
    hide player with dissolve
    return

label jenny_bedroom_jenny_go_to_her_room_submissive_no_money:
    show player 10
    player_name "Eu nem tenho duzentos!"
    show player 5
    show jenny f_upset_talk
    jen "Bem, eu não estou mostrando meus peitos para nada menos que duzentos."
    jen "Então é melhor você ir buscá-lo se quiser dar uma olhada nessas coisas..."
    show jenny f_upset
    show player 24
    player_name "{b}*Suspiro*{/b} bem."
    player_name "{b}Volto com o dinheiro{/b}."
    show jenny f_upset_talk
    jen "Apresse-se, perdedor."
    jen "Eu preciso desse dinheiro!"
    show jenny f_upset
    show player 10
    player_name "Sim Sim."
    hide player
    hide jenny
    with dissolve
    return

label jennys_bedroom_jenny_caught_snooping:
    scene expression player.location.background_blur with None
    show player 11 at left
    show jenny f_angry_talk a_dressed_hips
    with dissolve
    jen "Que porra, {b}[firstname]{/b}?!"
    show jenny f_angry
    show player 22
    player_name "!!!" with hpunch
    if M_jenny.finished_state(S_jenny_snoop_nightstand) and player.has_item('jenny_panties'):
        show jenny f_upset_talk
        jen "Oh.{w=1} Meu.{w=1} Deus."
        show jenny f_angry_talk
        jen "SÃO ESSAS MINHAS CALCINHAS?!"
        show jenny f_angry
        show player 23
        player_name "Não?"
        player_name "Eu não fiz nada"
        show player 22
        show jenny f_angry_talk
        jen "MERDA, perdedor. me devolve!"
        $ player.remove_item("jenny_panties")
        $ player.inventory.remove_picked_up("jenny_panties")
        show jenny f_upset_talk
        jen "Eu suponho que você acabou de tropeçar aqui por acidente, hein?"
    else:
        show jenny f_angry_talk
        jen "O que você está fazendo no meu quarto,pervertido perdedor?!"
        show jenny f_angry
        show player 23
        player_name "Nada!"
        show player 22
        show jenny f_upset_talk
        jen "Ahh, Ok, certo. Você acabou de tropeçar aqui por acidente, né?"
    show jenny f_upset
    show player 29 with dissolve
    player_name "Não exatamente..."
    show player 24 with dissolve
    player_name "{b}*Suspiro*{/b} Eu estava procurando sua {b}camêra digital{/b}, ok?"
    show jenny f_upset_talk
    jen "Hã por que?!"
    show jenny f_upset
    show player 3 with dissolve
    pause
    show jenny f_grin_talk
    jen "Ahh, entendi."
    jen "Você é tão patético, sabe disso?"
    jen "Você preferiria se sentar em seu quarto fingindo ter fotos roubadas minhas, Do que sair e encontrar uma namorada de verdade."
    show jenny f_grin
    show player 10 with dissolve
    player_name "Não."
    show player 5
    show jenny f_grin_talk
    jen "Haha, Ok, certo!"
    show jenny f_grin
    show player 24
    player_name "..."
    show jenny f_grin_talk a_dressed_camera_give with dissolve
    jen "Vou te dizer uma coisa, vou deixar você olhar as fotos, ok?"
    show jenny f_grin
    show player 10
    player_name "Hã você vai?"
    show player 5
    show jenny f_grin_talk
    jen "Certo."
    show player 20
    show jenny f_grin_talk a_dressed_camera_back with dissolve
    with dissolve
    jen "{b}Sessenta dólares{/b}."
    show jenny f_grin
    show player 10 with dissolve
    player_name "O que?!"
    show player 5
    show jenny f_grin_talk
    jen "{b}Sessenta dólares{/b} e você pode olhar para elas por dois minutos."
    show jenny f_grin
    show player 10
    player_name "Dois minutos?!"
    show player 12
    player_name "Você está Maluca.."
    show player 5
    show jenny f_upset_talk
    jen "Ei, você é o patético é difícil de lidar..."
    jen "Você quer ver as fotos sensuais ou não?"
    show jenny f_upset
    menu:
        "Está bem. {color=7ff7}[[Submissive]{/color}":
            $ M_jenny.decrement("dominance")
            if player.has_money(60):
                show player 174b with dissolve
                player_name "Here."
                show player 727
                show jenny f_grin_talk a_money
                with dissolve
                jen "Hahaha! Oh meu deus, você é tão patético!"
                jen "Você tem dois minutos..."
            else:
                show player 24
                player_name "Eu nem tenho sessenta dólares..."
                show jenny f_eyeroll
                jen "{b}*Suspiro*{/b} Deus, você é patético."
                show jenny f_upset
                pause
                show jenny f_upset_talk
                jen "Tudo bem, apenas me dê o que você tem."
                show jenny f_upset
                if not player.has_money(1):
                    show player 40 with dissolve
                    player_name "Eu não tenho nada ... Por favor, posso apenas olhar?"
                    show jenny f_upset_talk
                    jen "Patético..."
                    jen "Você tem 30 segundos..."
                else:
                    show player 174b with dissolve
                    show jenny f_upset_talk
                    jen "Você tem dois minutos..."
            $ player.spend_money(60)
        "Dane-se. {color=f77b}[[Dominant]{/color}":
            $ M_jenny.increment("dominance")
            show player 12
            player_name "Eu não vou pagar {b}sessenta dólares{/b} para um par de fotos estúpidas..."
            show player 90
            show jenny f_angry_talk
            jen "Peça Desculpa?!"
            show jenny f_angry
            show player 12
            player_name "Você me ouviu!"
            show player 90
            show jenny f_angry_pouting a_dressed_crossed with dissolve
            jen "Hmph!"
            pause
            show jenny f_upset_talk
            jen "{b}Trinta dólares{/b}?!"
            show jenny f_upset
            show player 12
            player_name "NÃO!"
            show player 90
            show jenny f_gross_talk
            jen "A sério?!"
            show jenny f_angry_talk
            jen "Grr, Apenas saia!"
            show jenny f_angry
            show player 10
            player_name "O que?"
            show player 90
            show jenny f_angry_talk a_dressed_upset with dissolve
            jen "Saia da porra do meu quarto antes que eu diga a {b}[deb_name]{/b} que você está pervertendo no meu quarto!"
            show jenny f_angry
            show player 12
            player_name "Com todo prazer."
            hide player with dissolve
            show jenny f_angry_pouting a_dressed_crossed with dissolve
            jen "( Ele é uma dor na minha bunda! )"

            $ player.go_to(L_home_hallway)
            scene expression player.location.background_closeup with None
            show player 90 with dissolve
            player_name "( Porra, eu realmente queria ver essas fotos, mas não tanto para ser humilhado dessa forma. )"
            show player 13
            player_name "( Pelo menos eu descobri que ela tem um diário e ela é sexualmente frustrada. )"
            show player 17
            player_name "( Haha! )"
            hide player with dissolve
            return
    show expression "backgrounds/location_home_jennybedroom_photo01.jpg" at Position (yoffset=110) with dissolve
    pause
    show expression "backgrounds/location_home_jennybedroom_photo02.jpg" at Position (yoffset=110) with dissolve
    pause
    show expression "backgrounds/location_home_jennybedroom_photo03.jpg" at Position (yoffset=110) with dissolve
    pause
    scene expression player.location.background_closeup with None
    show player 11 at left
    show jenny f_upset_talk a_dressed_camera_look
    with dissolve
    jen "Chegou a hora, perdedor!"
    show jenny f_upset a_dressed_hips with dissolve
    show player 12
    if not player.has_money(1):
        player_name "Isso não foi nem 30 segundos!"
    else:
        player_name "Isso não foi nem dois minutos!"
    show player 90
    show jenny f_grin_talk
    jen "Ah,tadinho do pobrezinho virgem..."
    show jenny f_upset_talk
    jen "Vá reclamar com alguém que se importa."
    hide jenny with dissolve
    jen "... E saia do meu quarto, PERDEDOR!"
    show player 15
    player_name "Está bem!"
    hide player with dissolve
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 90 with dissolve
    player_name "( Ela é uma puta! )"
    show player 17
    player_name "( Essas fotos valeram a pena... )"
    hide player with dissolve
    return

label jennys_bedroom_jenny_snoop_around:
    scene expression player.location.background_closeup with None
    show player 5 with dissolve
    player_name "( Ok, eu só preciso {b}encontrar essa câmera e sair daqui o mais rápido possível{/b}. )"
    player_name "( Ela provavelmente mantém )"
    show player 11
    player_name "( !!! )"
    player_name "( Isso é um diário?! )"
    show player 17
    player_name "( Tenho que verificar isso! )"
    hide player with dissolve
    return

label sis_bedroom_sis_not_in_room:
    scene jennybedroom
    show player 34 at left with dissolve
    player_name "( Hmmm... )"
    show player 35 at left
    player_name "( Ela não está no quarto dela... )"
    show player 18 at left
    player_name "( Talvez eu possa olhar em volta um pouco! )"
    hide player 18 at left with dissolve
    return

label sis_bedroom_sis_sleeping:
    scene jennybedroom_clear
    player_name "( {b}[jen_name]{/b} Está dormindo. )"
    player_name "( Eu tenho que ficar bem quieto ou ela pode me ouvir... )"
    player_name "( ...Não quero acordá-la ou estarei morto! )"
    return

label bedtable_night:
    call expression game.dialog_select("jenny_bedroom_cannot_snoop")
    $ in_sis_room = True
    jump expression game.dialog_select("sis_bedroom_dialogue")

label desk02_locked_dialogue:
    scene expression game.timer.image("sisbedroom{}")
    show player 35 at left
    player_name "( Eu não tenho a {b}senha{/b} do computador dela... )"
    $ game.main()

label sister_bedtable_panties:
    scene expression player.location.background_blur with None
    show player 5 with dissolve
    player_name "( Hmm, não está aqui... )"
    pause
    show player 30
    player_name "( São aquelas calcinhas? )"
    hide player with dissolve
    return

label siscomp_day:
    scene expression player.location.background_closeup
    show player 98 at Transform(align=(-.53, 1.)) with dissolve
    player_name "( Hmm... Vamos ver se ela deixou o computador ligado. )"
    player_name "( Eu me pergunto o que eu poderia encontrar aqui... )"
    show jenny f_angry at right
    if L_home_shower.is_here(M_jenny):
        show jenny b_towelhead
    with dissolve
    jen "..."
    show jenny f_angry_talk with hpunch
    jen "Posso ajudá-lo com {b}ALGUMA COISA{/b}??!"
    show jenny f_angry
    hide player
    show player f_shock at left
    with Dissolve(.2)
    player_name "!!!"
    show player f_shy_talk a_dressed_behind_head at left
    show jenny a_dressed_crossed f_gross
    with dissolve
    player_name "Desculpa!! Eu estava apenas ... tentando ver se a sua internet está funcionando!!"
    player_name "Eu não consigo me conectar no meu computador..."
    show player f_shy
    show jenny f_gross_talk
    jen "Não {b}toca{/b} no meu computador!!"
    show player f_looking_down a_dressed_pocket with dissolve
    jen "Apenas me pergunte da próxima vez."
    show player f_sad_talk_down
    show jenny f_gross
    player_name "Claro!"
    show player f_surprised_teeth
    show jenny f_angry_talk
    jen "Agora saia do {b}MEU QUARTO{/b}!!!"
    hide player
    hide jenny
    with dissolve
    return

label jennys_bedroom_bissette_roxxy_cheerleader_deal:
    scene jennybedroom
    show jenny f_upset
    show player f_worried_talk
    with dissolve
    player_name "Ei, {b}[jen_name]{/b}."
    show player f_worried
    show jenny f_upset_talk
    jen "O que você quer?"
    show jenny f_upset a_dressed_crossed with dissolve
    show player f_worried_talk
    player_name "Eu preciso da sua ajuda com algo..."
    show player f_worried
    show jenny f_grin_talk
    jen "Quanto você vai me pagar?"
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Eu nem te contei o que é ainda!"
    show player f_worried
    show jenny f_grin_talk
    jen "Hmm, bom ponto ... eu deveria ouvir todos os detalhes antes de definir o preço!"
    show jenny f_grin
    show player f_tired_talk
    player_name "*Suspiro*"
    show player f_worried_talk
    player_name "Tem uma garota na escola que precisa de ajuda com sua rotina de liderança."
    show player f_worried
    show jenny f_grin_talk
    jen "Isso é alguma garota que você está tentando foder?"
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Hã? NÃO!"
    show player f_worried
    show jenny f_grin_talk a_dressed_hips with dissolve
    jen "Por que não? Ela é feia?"
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Não, ela é linda, mas uma puta total!"
    show player f_worried
    show jenny f_grin_talk
    jen "Hmm, Eu já estou começando a gostar dessa garota."
    show jenny f_grin
    player_name "..."
    show player f_skeptical_talk
    player_name "Então você vai ajudá-la com a rotina?"
    show player f_worried
    show jenny f_grin_talk
    jen "$500."
    show jenny f_grin
    show player f_surprised
    player_name "O que?! Você é louca?"
    show player f_worried
    show jenny f_upset_talk
    jen "Esse é o preço."
    jen "Pague ou saia."
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Você não poderia simplesmente me ajudar?"
    show player f_worried
    show jenny f_laugh
    jen "Hahahaha, você e uma piada {b}[firstname]{/b}!"
    show jenny f_upset_talk a_dressed_hips_asking with dissolve
    jen "$500."
    show jenny f_upset
    show player f_skeptical_talk
    player_name "*Suspiro* bem!"
    show jenny a_dressed_crossed with dissolve
    player_name "Eu voltarei quando tiver dinheiro..."
    hide player
    hide jenny
    with dissolve
    return

label jennys_bedroom_bissette_roxxy_jenny_spying:
    $ persistent.cookie_jar["Roxxy"]["gallery"]["02_unlocked"] = True
    $ suffix = ""
    if M_roxxy.get("roxxy trailer sex"):
        $ suffix = "_sex"
    call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_pre")
    if M_jenny.is_set("seen MCs penis"):
        call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_seen_penis{}".format(suffix))
    else:
        call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_havent_seen_penis{}".format(suffix))
    call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_after")
    $ del suffix
    $ renpy.end_replay()
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_pre:
    scene jennybedroom_peek_c
    show jenny b_bed_cheer a_bed_cheer_down f_bed_roxxy_normal at Position (align=(0,0))
    show roxxy 36 at Position (xpos=415,ypos=692)
    show roxxy_outfit cheer 41b
    show poms 41 zorder 665
    show xtra 41 zorder 666
    with dissolve
    rox "Obrigado novamente por me emprestar seu antigo uniforme."
    show roxxy 35
    show jenny f_bed_roxxy_normal_talk
    jen "Sem problema!"
    jen "Não me serve de qualquer maneira."
    jen "Merda, esse uniforme de faculdade mal se encaixa..."
    show jenny f_bed_roxxy_normal
    show roxxy 37
    rox "Haha, Sim."
    show roxxy 36
    rox "Parece que seus peitos vão se espalhar, qualquer segundo..."
    show roxxy 35
    show jenny f_bed_roxxy_laugh
    jen "Hehe!"
    show jenny f_bed_roxxy_normal_talk
    jen "... É o que estou dizendo! Os juízes dão pontos extras para sex appeal."
    jen "É por isso que nunca uso sutiã durante as competições."
    show jenny f_bed_roxxy_normal
    show roxxy 36
    rox "Sim, eu nunca pensei sobre isso."
    rox "Você é um gênio total!"
    show roxxy 35
    show jenny f_bed_roxxy_normal_talk
    jen "Me diga algo que eu não sei..."
    jen "Essas Belezinhas me conquistaram três campeonatos estaduais consecutivos!"
    show jenny f_bed_roxxy_normal
    show roxxy 36
    rox "... Eles são muito legais..."
    show roxxy 38
    show jenny f_bed_roxxy_normal_talk
    jen "Obrigada!"
    show jenny f_bed_roxxy_sexy_talk_down
    jen "Os seus também são lindos."
    show jenny f_bed_roxxy_sexy_down
    show roxxy 36
    rox "Sim, mas o meu não é tão grande quanto o seu..."
    show roxxy 38
    show jenny f_bed_roxxy_sexy_talk_down
    jen "Mmm, talvez não, mas aposto que são mais firmes do que o meu."
    show jenny f_bed_roxxy_sexy_down
    show roxxy 37
    rox "Hehe, Talvez..."
    show roxxy 35
    show jenny f_bed_roxxy_sexy_talk_down
    jen "Deixe-me dar uma olhada nesses filhotes."
    hide roxxy
    hide roxxy_outfit
    show jenny b_bed_cheer_roxxy_lift1 a_empty f_bed_roxxy_sexy_down
    with dissolve
    rox "Uau!! O que você{p=1}{nw}"
    show jenny b_bed_cheer_roxxy_lift2 with dissolve
    pause .1
    show jenny b_bed_cheer_roxxy_lift3 with dissolve
    pause .1
    show roxxy 34b at Position (xpos=380,ypos=692)
    show jenny b_bed_cheer a_bed_cheer_down f_bed_roxxy_normal_talk
    with dissolve
    jen "Acalme-se!"
    jen "Somos apenas nois de garotas aqui."
    show jenny f_bed_roxxy_sexy_down
    rox "..."
    show roxxy 34
    rox "Eu não sei..."
    show roxxy 34b
    show jenny f_bed_roxxy_sexy_talk_down
    jen "Aqui."
    show jenny b_bed_cheerlift f_bed_roxxy_normal_low a_empty with dissolve
    pause
    show jenny b_bed_cheerup a_bed_cheerup_surprised f_bed_roxxy_happy_talk_down with dissolve
    jen "Veja, nada para se envergonhar!"
    show jenny f_bed_roxxy_sexy_down
    show roxxy 40 at Position (xpos=415,ypos=692)
    show roxxy_outfit cheer 41d
    with dissolve
    rox "... Sim, eu acho..."
    hide roxxy
    hide roxxy_outfit
    show jenny b_bed_cheer_roxxy_touch1 a_empty f_bed_roxxy_sexy_down
    rox "!!!" with hpunch
    show jenny f_bed_roxxy_sexy_talk_down
    jen "Eu estava certo, eles são mais firmes que os meus..."
    jen "Eu sou meio ciumenta!"
    show jenny b_bed_cheer_roxxy_touch2 f_bed_roxxy_sexy_down
    rox "... Obrigada."
    show jenny b_bed_cheer_roxxy_touch1 f_bed_roxxy_sexy_talk_down
    jen "Você também tem mamilos fofos!"
    show jenny f_bed_roxxy_sexy_down
    rox "..."
    show jenny f_bed_roxxy_normal_talk
    jen "Uau, você é tímida!"
    show jenny b_bed_cheer_roxxy_touch2 f_bed_roxxy_normal
    rox "Eu não sou"
    show jenny b_bed_cheer_roxxy_touch1 f_bed_roxxy_normal_talk
    jen "Tão adorável!"
    jen "Você não quer sentir o meu?"
    show jenny b_bed_cheer_roxxy_touch2 f_bed_roxxy_normal
    rox "Você quer que eu?"
    show jenny b_bed_cheer_roxxy_grab1 f_bed_roxxy_sexy_down
    rox "!!!" with hpunch
    jen "Veja, não tão ruim..."
    show jenny b_bed_cheer_roxxy_grab2
    rox "Sua pele é tão macia..."
    show jenny b_bed_cheer_roxxy_grab1 f_bed_roxxy_sexy_talk_down
    jen "Eu sei bem?"
    jen "É essa loção especial que uso. Eu vou te passar!"
    show jenny b_bed_cheer_roxxy_grab2 f_bed_roxxy_sexy_down
    rox "Obrigada, {b}[jen_name]{/b}!"
    show roxxy 39 at Position (xpos=415,ypos=692)
    show jenny b_bed_cheerup a_bed_cheerup_down f_bed_roxxy_laugh
    show roxxy_outfit cheer 41d
    with dissolve
    jen "Maldita garota! Você tem um corpo estrondoso!"
    show jenny f_bed_roxxy_sexy_down
    show roxxy 40
    rox "Você acha que os juízes vão notar?"
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Concerteza!"
    if M_roxxy.get("roxxy trailer sex"):
        jen "Eu não posso acreditar {b}[firstname]{/b} está acertando isso!"
        show jenny f_bed_roxxy_normal
        show roxxy 40
        rox "Hehe, bem eu realmente o fiz trabalhar para isso."
        rox "Ele é um cara muito tenaz..."
    else:
        jen "Eu posso ver por que aquele idiota lá embaixo quer pegar neles."
        show jenny f_bed_roxxy_normal
        show roxxy 40
        rox "Não acredito que vocês dois morem juntos!"
        rox "Você é tão incrível e ele é tão idiota!"
    show roxxy 39
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_seen_penis:
    show jenny f_bed_roxxy_normal_talk
    jen "Ele não é tão ruim..."
    jen "Ele pode ser bastante útil por perto."
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "... Sim, acho que ele foi muito útil recentemente."
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Além disso, só entre você e eu..."
    jen "Ele tem pau do tamanho de um cavalo!"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Mesmo?! Quer dizer que você viu o pau dele?"
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Eu já vi muitas vezes."
    jen "Nós vivemos juntos seria dificil não notar."
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Eu acho que isso é verdade..."
    rox "Então é grande, mesmo?"
    show roxxy 39
    show jenny f_bed_roxxy_laugh
    jen "Imenso!"
    show jenny f_bed_roxxy_normal
    show roxxy 42
    rox "Interessante."
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Seu namorado e bem dotado?"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "{b}Dexter{/b}?"
    show roxxy 42
    rox "Pfft."
    show roxxy 43 with dissolve
    show jenny f_bed_roxxy_laugh
    jen "Hahaha!"
    show jenny f_bed_roxxy_normal_talk
    show roxxy 39 with dissolve
    jen "Muito pequeno, Eh? Isso é ruim."
    show jenny f_bed_roxxy_normal
    rox "..."
    show jenny f_bed_roxxy_normal_talk
    jen "Bem, de qualquer maneira ... Você está pronta para aprender alguns movimentos?"
    show jenny f_bed_roxxy_normal
    show roxxy 37
    rox "Isso aí!"
    show roxxy 39
    show jenny f_bed_roxxy_laugh
    jen "Legal, vamos fazer isso!"
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_havent_seen_penis:
    show jenny f_bed_roxxy_normal_talk
    jen "Eu sei direito!"
    jen "Eu digo a todos que ele é o garoto de manutenção..."
    show jenny f_bed_roxxy_normal
    show roxxy 37
    rox "Hahaha!"
    show roxxy 40
    rox "Sim, meu namorado ameaça chutar a bunda o tempo todo."
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Você tem um namorado?"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Bem, mais ou menos..."
    rox "Vamos apenas dizer, ele acha que é meu namorado."
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "eu gosto do seu estilo, {b}Roxxy{/b}!"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Hehe, Obrigada!"
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Ele está fazendo as malas?"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "O que você quer dizer?"
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Você sabe, no sul..."
    jen "Ele é grande?"
    show jenny f_bed_roxxy_normal
    show roxxy 42
    rox "Pfft..."
    show roxxy 43 with dissolve
    show jenny f_bed_roxxy_laugh
    jen "Ele é pequeno!?"
    show jenny f_bed_roxxy_normal
    show roxxy 40 with dissolve
    rox "Muito pequeno."
    show roxxy 39
    show jenny f_bed_roxxy_laugh
    jen "Hahaha!"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Sim, eu não o mantenho por perto para o sexo."
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Eu não pensaria assim..."
    show jenny f_bed_roxxy_normal
    rox "..."
    show jenny f_bed_roxxy_normal_talk
    jen "Bem, de qualquer maneira ... Você está pronta para aprender alguns movimentos?"
    show jenny f_bed_roxxy_normal
    show roxxy 37
    rox "Isso aí!"
    show roxxy 39
    show jenny f_bed_roxxy_laugh
    jen "Legal, vamos fazer isso!"
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_seen_penis_sex:
    show jenny f_bed_roxxy_normal_talk
    jen "Sim, ele pode ser realmente teimoso..."
    jen "Ele é engenhoso, vou dar isso a ele."
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Além disso, ele tem aquele pau enorme!"
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Eu sei direito?!"
    jen "Ele tem pau do tamanho de um cavalo pirado!"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Uau, espere ... Você quer dizer que você viu?"
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Oh, eu já vi muitas vezes."
    jen "Tipo de inevitável, na verdade. Vivendo proxima a ele."
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Sim, acho que isso faz sentido."
    rox "Deve ser chato viver com algum cara aleatório..."
    show roxxy 39
    show jenny f_bed_roxxy_laugh
    jen "Hehe, Não sei. Tem suas vantagens."
    show jenny f_bed_roxxy_normal
    rox "..."
    show jenny f_bed_roxxy_normal_talk
    jen "Seu último namorado e bem dotado?"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "{b}Dexter{/b}?"
    show roxxy 42
    rox "Pfft."
    show roxxy 43 with dissolve
    show jenny f_bed_roxxy_laugh
    jen "Hahaha!"
    show jenny f_bed_roxxy_normal_talk
    show roxxy 39 with dissolve
    jen "Pequeno, Eh? Isso é ruim."
    show roxxy 35e at Position (xoffset=-120, yoffset=100)
    show jenny f_bed_roxxy_normal
    rox "Sim, ele acabou sendo um grande babaca também."
    show jenny f_bed_roxxy_normal_talk
    show roxxy 39
    jen "Bem, de qualquer maneira ... Você está pronta para aprender alguns movimentos?"
    show jenny f_bed_roxxy_normal
    show roxxy 37
    rox "Isso aí!"
    show roxxy 39
    show jenny f_bed_roxxy_laugh
    jen "Legal, vamos fazer isso!"
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_havent_seen_penis_sex:
    show jenny f_bed_roxxy_normal_talk
    jen "Não é forte o suficiente {b}Roxxy{/b}!"
    jen "Ele teria que beijar meus pés e rastejar como um cachorro antes de eu deixá-lo na minha calcinha..."
    show jenny f_bed_roxxy_normal
    show roxxy 37
    rox "Hahaha! Você é uma cadela hardcore, {b}[jen_name]{/b}!"
    show roxxy 40
    rox "Sorte dele, você não está interessado, né?"
    rox "Caso contrário, eu poderia totalmente vê-lo tentando..."
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "... Sim. Sorte para ele..."
    jen "... Então ele é bom?"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "O que você quer dizer? Como na cama?"
    jen "Sim."
    rox "Ele é incrível!"
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Surpreendente? Você está brincando."
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Não, estou falando sério sério!"
    rox "Ele é como um sábio idiota ou algo assim..."
    rox "... E ele tem um pau enorme!"
    show roxxy 39
    show jenny f_bed_roxxy_sad_talk
    jen "Hã? O que você quer dizer com massivo?"
    show jenny f_bed_roxxy_sad with None
    show roxxy 43b
    hide roxxy_outfit
    with dissolve
    rox "..."
    show roxxy 39
    show roxxy_outfit cheer 41d
    with dissolve
    show jenny f_bed_roxxy_normal_talk
    jen "Você está brincando!"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Nem um pouco."
    show roxxy 39
    show jenny f_bed_roxxy_sad_talk
    jen "Puta merda..."
    show jenny f_bed_roxxy_sad
    show roxxy 40
    rox "É super maluco!"
    show roxxy 39
    show jenny f_bed_roxxy_laugh
    jen "Hahaha!"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Eu juro, ele é como uma máquina de orgasmo!"
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Interessante..."
    show jenny f_bed_roxxy_normal
    rox "..."
    show jenny f_bed_roxxy_normal_talk
    jen "Bem, de qualquer maneira ... Você está pronta para aprender alguns movimentos?"
    show jenny f_bed_roxxy_normal
    show roxxy 37
    rox "Isso aí!"
    show roxxy 39
    show jenny f_bed_roxxy_laugh
    jen "Legal, vamos fazer isso!"
    return


label jennys_bedroom_bissette_roxxy_jenny_spying_after:
    scene black with fade
    scene hallway
    show player 33 with dissolve
    player_name "( Uau!!! )"
    show player 17
    player_name "( Talvez isso não tenha sido uma má idéia depois de tudo! )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
