label jenny_pregnancy_baby_need_anything:
    show player f_normal_talk
    player_name "Vocês precisam de alguma coisa?"
    show player f_normal
    show jenny f_happy_talk_down
    jen "Não, estamos bem."
    jen "Sim somos nós?"
    jen "Sim, nós somos!"
    jen "Somos maravilhosos!"
    show jenny f_happy_down
    return

label jenny_pregnancy_baby_looking_forward_daycare:
    show player f_normal_talk
    player_name "Ansiosa para creche?"
    show player f_surprised
    show jenny f_angry_talk
    jen "Não porra!"
    show jenny f_upset_talk
    jen "Eu odeio pensar em deixá-la com um estranho."
    show jenny f_upset
    show player f_worried_talk
    player_name "Não será um estranho {b}[jen_name]{/b}..."
    show player f_normal_talk
    player_name "{b}[deb_name]{/b} e {b}Diane{/b} Conheçe a dona da casa, ouvi dizer que ela é muito legal."
    show player f_normal
    show jenny f_upset_talk
    jen "Eu não me importo se ela é a porra da Mary Poppins, Eu não acho uma boa ideia deixar meus filhos com ela!"
    show jenny f_upset
    show player f_normal_talk
    player_name "Eu nunca pensei que você fosse o tipo de mamãe urso..."
    show player f_normal
    show jenny f_happy_talk_down
    jen "Sim, bem ... eu sou."
    show jenny f_happy_down
    show player f_laugh
    player_name "Haha!"
    show player f_normal
    return

label jenny_pregnancy_baby_leave:
    show player f_normal_talk
    player_name "Vou deixar você."
    show player f_normal
    show jenny f_happy_talk_down
    jen "Diga tchau para o {b}papai{/b}..."
    jen "Tchau tchau, {b}papai{/b}!"
    show jenny f_happy_down
    show player f_laugh
    player_name "Tchau tchau!"
    hide player with dissolve
    return

label jenny_pregnancy_debbie_driving_crazy:
    show player f_magic_sit_stand_worried_talk
    player_name "{b}[deb_name]{/b} está te deixando louca?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_eyeroll
    jen "Oh meu deus, sim!!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Como assim?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Ela está sempre me seguindo por aí, tentando me fazer comer..."
    jen "É irritante!!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "São apenas seus instintos maternais se manifestando, {b}[jen_name]{/b}."
    player_name "Você é como uma filha para ela, afinal."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_eyeroll
    jen "Sim, sim, eu sei..."
    show jenny f_magic_sit_stand_upset_talk
    jen "Eu só queria que ela calasse a boca sobre o fato de ser uma madrinha..."
    jen "Eu juro, Ela é mais safada do que você sobre essas coisas."
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_normal_talk
    player_name "Eu acho que é doce."
    show player f_magic_sit_stand_normal
    show jenny f_magic_sit_stand_eyeroll
    jen "Ugh, tanto faz."
    show jenny f_magic_sit_stand_upset
    return

label jenny_pregnancy_can_i_get_you_something_3:
    show player f_magic_sit_stand_worried_talk
    player_name "Posso te dar uma coisa?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Como o quê?!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_normal_talk
    player_name "Eu não sei, uma massagem nos pés ou algo assim?"
    show player f_magic_sit_stand_grin
    show jenny f_magic_sit_stand_gross_talk
    jen "Eca, não!"
    jen "Eu nem quero te mostrar meus pés agora, eles são gigantescos!"
    show jenny f_magic_sit_stand_gross
    show player f_magic_sit_stand_flirt_talk
    player_name "Realmente, não me importo"
    show player f_magic_sit_stand_flirt
    show jenny f_magic_sit_stand_gross_talk
    jen "Não, sério!"
    show jenny f_magic_sit_stand_gross
    show player f_magic_sit_stand_skeptical_talk
    player_name "Ok, não vou esfregar seus pés."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "Algo para comer talvez?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_normal_talk a_magic_sit_stand_belly_touch with dissolve
    jen "Ah, isso seria incrível!"
    jen "Eu tenho desejado algumas coisas muito estranhas..."
    show jenny f_magic_sit_stand_normal
    show player f_magic_sit_stand_worried_talk
    player_name "O que você quer dizer?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Você só vai rir de mim..."
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_normal_talk
    player_name "Não, não vou."
    show player f_magic_sit_stand_normal
    jen "..."
    show player f_magic_sit_stand_normal_talk
    player_name "Eu prometo!"
    show player f_magic_sit_stand_normal
    show jenny f_magic_sit_stand_sad_talk
    jen "Tudo bem."
    show jenny f_magic_sit_stand_eyeroll
    jen "{b}*Suspiro*{/b} quero um pedaço de Giz."
    show jenny f_magic_sit_stand_sad
    show player f_magic_sit_stand_shock
    player_name "O que?!"
    show player f_magic_sit_stand_surprised_teeth
    show jenny f_magic_sit_stand_normal_talk
    jen "Eu não posso explicar isso ... Eu realmente quero morder um grande pedaço de giz..."
    show jenny f_magic_sit_stand_gross
    pause
    show jenny f_magic_sit_stand_gross_talk
    jen "É estranho né?"
    show jenny f_magic_sit_stand_gross
    player_name "..."
    show jenny f_magic_sit_stand_gross_talk
    jen "Eles fazem giz comestível?"
    show jenny f_magic_sit_stand_gross
    show player f_magic_sit_stand_laugh
    player_name "Hahaha!"
    show jenny f_magic_sit_stand_angry a_magic_sit_stand_crossed with dissolve
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "Me desculpe, eu só não estava preparado, isso e estranho haha!"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_angry_talk
    jen "Você disse que não iria rir!"
    show jenny f_magic_sit_stand_angry
    show player f_magic_sit_stand_worried_talk
    player_name "Eu sei, eu sinto muito mesmo!"
    show player f_magic_sit_stand_normal_talk
    player_name "Não, {b}[jen_name]{/b}, Eles não fazem giz comestível..."
    show player f_magic_sit_stand_normal
    show jenny f_magic_sit_stand_sad_talk
    jen "Hmmph, bem eles deveriam!"
    show jenny f_magic_sit_stand_sad
    show player f_magic_sit_stand_worried_talk
    player_name "Você realmente quer comer giz?!"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_sad_talk
    jen "Sim eu quero..."
    show jenny f_magic_sit_stand_grin_talk a_magic_sit_stand_belly_touch with dissolve
    jen "... E marshmallows."
    show jenny f_magic_sit_stand_grin
    show player f_magic_sit_stand_laugh
    player_name "Ok, marshmellows podemos conseguir."
    player_name "Eu vou pegar um pouco!"
    show player f_magic_sit_stand_normal
    show jenny f_magic_sit_stand_normal_talk
    jen "Com picles!"
    show jenny f_magic_sit_stand_normal
    show player f_magic_sit_stand_surprised
    player_name "..."
    show jenny f_magic_sit_stand_normal_talk
    jen "E mostarda!"
    show jenny f_magic_sit_stand_normal
    show player f_magic_sit_stand_worried_talk
    player_name "Ei, tudo bem..."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_eyeroll
    jen "... Mas não mostarda regular."
    show jenny f_magic_sit_stand_grin_talk a_magic_sit_stand_crossed with dissolve
    jen "Eu quero coisa cara de dijon!"
    show jenny f_magic_sit_stand_grin
    show player f_magic_sit_stand_worried_talk
    player_name "Certo."
    player_name "Deixa comigo ok."
    show player f_magic_sit_stand_worried
    player_name "( Meu deus, isso é tão repugnante!!! )"
    return

label jenny_pregnancy_about_debbie:
    show player f_magic_sit_stand_worried_talk
    player_name "Sobre {b}[deb_name]{/b}..."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_grin_talk
    jen "Eu não posso acreditar ja vem você com essa besteira de historia..."
    show jenny f_magic_sit_stand_grin
    show player f_magic_sit_stand_worried_talk
    player_name "Eu não entendo porque não podemos simplesmente contar a ela a verdade?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_angry_talk
    jen "Você quer contar {b}[deb_name]{/b} que você é o pai?!"
    jen "Ela iria pirar, seu idiota!"
    show jenny f_magic_sit_stand_angry
    show player f_magic_sit_stand_worried_talk
    player_name "Eu não acho que ela"
    show player f_magic_sit_stand_surprised
    show jenny f_magic_sit_stand_angry_talk
    jen "De jeito nenhum, {b}[firstname]{/b}!"
    show jenny f_magic_sit_stand_angry
    show player f_magic_sit_stand_worried_talk
    player_name "{b}[jen_name]{/b}..."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_angry_talk
    jen "NÃO!"
    show jenny f_magic_sit_stand_angry
    show player f_magic_sit_stand_tired_talk
    player_name "{b}*Suspiro*{/b}"
    show player f_magic_sit_stand_worried
    return

label jenny_pregnancy_can_i_get_you_something:
    show player f_magic_sit_stand_worried_talk
    player_name "Posso te dar uma coisa?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_eyeroll
    jen "Sim, uma máquina do tempo."
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_skeptical_talk
    player_name "Hã?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_angry_talk
    jen "Para que eu possa voltar no tempo, E fazer você desistir do que fez!"
    show jenny f_magic_sit_stand_gross
    player_name "..."
    return

label jenny_pregnancy_are_you_still_mad:
    show player f_magic_sit_stand_worried_talk
    player_name "Você ainda está brava?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_angry_talk a_magic_sit_stand_crossed with dissolve
    jen "Claro que estou, seu idiota!"
    show jenny f_magic_sit_stand_upset_talk
    jen "Você percebe o quanto isso vai me custar?"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_skeptical_talk
    player_name "Hã?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Quem vai assistir meus shows se eu engordar?!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Você não vai engordar, {b}[jen_name]{/b}..."
    player_name "... E mesmo se você fizer Shows, algumas pessoas gosta disso sabia."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_eyeroll
    jen "Ugh, algumas aberrações que você quer dizer."
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Tudo vai ficar bem, você vai ver."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_phone_upset_talk a_magic_sit_stand_phone with dissolve
    jen "Tanto faz."
    show jenny f_magic_sit_stand_phone_upset
    return

label jenny_pregnancy_leave:
    show player f_magic_sit_stand_worried_talk
    player_name "Eu vou deixar você sozinha."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_eyeroll
    jen "Se fodendo neh!"
    show jenny f_magic_sit_stand_phone_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Você vai me deixar saber se você precisar de alguma coisa?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Sim, sim, eu vou deixar você saber."
    jen "Vá embora."
    show jenny f_magic_sit_stand_phone_upset
    show player f_magic_sit_stand_tired_talk
    player_name "{b}*Suspiro*{/b}"
    hide player with dissolve
    return

label jenny_pregnancy_you_doing_ok_1:
    show player f_magic_sit_stand_worried_talk
    player_name "Você está bem?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_phone_upset_talk
    jen "Estou bem."
    show jenny f_magic_sit_stand_phone_upset
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "Tem certeza?"
    player_name "Nós podemos falar sobre isso, se você quiser?"
    show player f_magic_sit_stand_surprised
    if randomizer() > 50:
        show jenny f_magic_sit_stand_angry_talk
        jen "Oh meu deus, cala a boca!"
        jen "{b}[deb_name]{/b} pode ouvir você, idiota!"
        show jenny f_magic_sit_stand_angry
        show player f_magic_sit_stand_worried_talk
        player_name "Estou apenas dizendo"
        show player f_magic_sit_stand_worried
        show jenny f_magic_sit_stand_eyeroll
        jen "Eu sei o que você está dizendo, {b}[firstname]{/b}!"
        show jenny f_magic_sit_stand_upset_talk
        jen "Sério, estou bem!"
    else:
        show jenny f_magic_sit_stand_upset_talk
        jen "Eu disse que estou bem, {b}[firstname]{/b}!"
    jen "Me deixe."
    show jenny f_magic_sit_stand_phone_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Ok."
    show player f_magic_sit_stand_worried
    return

label jenny_pregnancy_you_doing_ok_2:
    show player f_magic_sit_stand_worried_talk
    player_name "Você está bem?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_gross_talk
    jen "Não, não estou bem!"
    jen "Essa coisa toda é uma merda!"
    show jenny f_magic_sit_stand_gross
    show player f_magic_sit_stand_worried_talk
    player_name "Qual é o problema?!"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_eyeroll
    jen "Hmm, bem vamos ver..."
    show jenny f_magic_sit_stand_gross_talk
    jen "Para começar, eu vomitei minhas tripas toda manhã."
    jen "Então estou alimentando como uma vaca, Porque sua amiga idiota está determinada a me engordar."
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "{b}[jen_name]{/b}..."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Estou desconfortável, praticamente o dia todo."
    show jenny f_magic_sit_stand_angry_talk
    jen "Ah, e eu acordo e faço xixi quatro vezes por noite agora!"
    show jenny f_magic_sit_stand_gross
    show player f_magic_sit_stand_worried_talk
    player_name "Eu sinto Muito?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_angry_talk
    jen "Você deveria se arrepender do que fez!"
    jen "Isso é tudo culpa sua, idiota!"
    show jenny f_magic_sit_stand_gross
    return

label jenny_pregnancy_you_doing_ok_3:
    show player f_magic_sit_stand_worried_talk
    player_name "Você está bem?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_gross_talk
    jen "Não, não estou bem!"
    show jenny f_magic_sit_stand_angry_talk a_magic_sit_stand_belly_touch with dissolve
    jen "Apenas olhe o que você fez comigo, {b}[firstname]{/b}!"
    jen "Eu sou uma baleia!"
    show jenny f_magic_sit_stand_angry
    show player f_magic_sit_stand_worried_talk
    player_name "Você não é uma baleia, {b}[jen_name]{/b}..."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_sad_talk
    jen "Sim eu sou!"
    show jenny f_magic_sit_stand_sad
    show player f_magic_sit_stand_normal_talk
    player_name "Não, você é linda..."
    show player f_magic_sit_stand_normal
    show jenny f_magic_sit_stand_sad_talk
    jen "Linda?!"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_angry_talk
    jen "O que você é retardado?!"
    show jenny f_magic_sit_stand_angry
    show player f_magic_sit_stand_worried_talk
    player_name "Você está carregando nosso filho ... Eu acho lindo."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_eyeroll a_magic_sit_stand_crossed with dissolve
    jen "Oh meu deus, você é o pior..."
    show jenny f_magic_sit_stand_sad
    pause
    show jenny f_magic_sit_stand_sad_talk
    jen "Eu só quero essa coisa fora de mim logo!"
    show jenny f_magic_sit_stand_sad
    return

label jenny_button_pregnancy_stage_1:
    if player.location == L_home_diningroom:
        scene expression game.timer.image("dining_room{}")
        show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    else:
        scene expression player.location.background_closeup
    show player b_magic_sit_stand_dressed f_magic_sit_stand_normal_talk a_magic_sit_stand_resting zorder 1 at Position (align=(0,0))
    show jenny f_magic_sit_stand_phone_upset a_magic_sit_stand_phone b_magic_sit_stand_dressed zorder 1 at Position (align=(0,0))
    player_name "Bom dia."
    show player f_magic_sit_stand_worried
    jen "..."
    return

label jenny_button_pregnancy_stage_2:
    if player.location == L_home_diningroom:
        scene expression game.timer.image("dining_room{}")
        show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    else:
        scene expression player.location.background_closeup
    show player b_magic_sit_stand_dressed f_magic_sit_stand_normal_talk a_magic_sit_stand_resting zorder 1 at Position (align=(0,0))
    show jenny f_magic_sit_stand_phone_upset a_magic_sit_stand_phone b_magic_sit_stand_dressed zorder 1 at Position (align=(0,0))
    with dissolve
    player_name "Ei, {b}[jen_name]{/b}."
    show player f_magic_sit_stand_normal
    show jenny f_magic_sit_stand_eyeroll
    jen "Ugh, o que você quer, {b}[firstname]{/b}?"
    show jenny f_magic_sit_stand_gross a_magic_sit_stand_crossed with dissolve
    return

label jenny_button_pregnancy_stage_3:
    if player.location == L_home_diningroom:
        scene expression game.timer.image("dining_room{}")
        show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    else:
        scene expression player.location.background_closeup
    show player b_magic_sit_stand_dressed f_magic_sit_stand_worried_talk a_magic_sit_stand_resting zorder 1 at Position (align=(0,0))
    show jenny f_magic_sit_stand_phone_upset a_magic_sit_stand_phone b_magic_sit_stand_dressed zorder 1 at Position (align=(0,0))
    player_name "Ei, {b}[jen_name]{/b}."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_surprised a_magic_sit_stand_crossed with dissolve
    jen "Merda, você me assustou!"
    show jenny f_magic_sit_stand_upset_talk
    jen "Eu pensei que você fosse {b}[deb_name]{/b}..."
    jen "Ela está me deixando louca."
    show jenny f_magic_sit_stand_gross
    return

label jenny_button_pregnancy_holding_baby:
    scene expression player.location.background_closeup
    $ player.last_baby_gender = M_jenny.pregnancy.baby_gender
    show jenny a_dressed_baby b_casual f_happy_talk_down
    show player f_normal with dissolve
    jen "Você é tão linda, e tão pequena?!"
    jen "Você parece muito com sua {b}Mamãe{/b}."
    jen "Que é muita sorte porque o seu {b}pai{/b} é basicamente um troll de ponte..."
    show jenny f_happy_down
    show player f_worried_talk
    player_name "Ei!"
    show player f_worried
    show jenny f_laugh
    jen "Hahahaah!"
    show jenny f_happy_down
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
