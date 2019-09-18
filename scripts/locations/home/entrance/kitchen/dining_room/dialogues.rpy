label dining_room_jenny_have_breakfast_4:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_dinner_sitting a_dinner_sitting_resting f_magic_sit_stand_worried zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    show jenny f_breakfast_upset_talk
    jen "Estava na hora..."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Qual é o seu problema?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "Nós temos um grande show hoje."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Grande show?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "Isso mesmo, então coma."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "O que você vai"
    show player f_diningroom_table_surprised_left
    deb "Bom Dia querido!"
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_normal
    show player f_diningroom_table_normal_talk
    player_name "Bom dia, {b}[deb_name]{/b}."
    show player f_diningroom_table_normal
    show debbie f_breakfast_standing_normal_talk
    deb "Espero que esteja com fome."
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_eyeroll
    show player f_diningroom_table_normal_talk
    player_name "Morrendo de fome."
    show player f_diningroom_table_normal
    show jenny f_breakfast_normal_talk
    jen "{b}[deb_name]{/b}, você sabe onde meu uniforme está?"
    show jenny f_breakfast_normal
    show debbie f_breakfast_standing_normal_talk
    deb "Que uniforme, querida?"
    show debbie f_breakfast_standing_normal
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    show jenny f_breakfast_normal_talk
    jen "Você sabe, da faculdade..."
    show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting with dissolve
    show jenny f_breakfast_normal
    show debbie f_breakfast_standing_normal_talk
    deb "Quer dizer, sua fantasia de animadora de torcida?"
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_upset_talk
    jen "{b}[deb_name]{/b}, é um uniforme!"
    show jenny f_breakfast_upset
    show debbie f_breakfast_standing_normal_talk
    deb "Ok, tudo bem, uniforme."
    show debbie f_breakfast_standing_sorry
    deb "Umm..."
    show debbie f_breakfast_standing_normal_talk
    deb "É provavelmente ta guardado no sótão com o resto das nossas roupas velhas..."
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_surprised
    jen "No sótão?!"
    show jenny f_breakfast_angry_talk
    show player f_diningroom_table_surprised_left_food
    jen "Droga, {b}[deb_name]{/b}!"
    show debbie f_breakfast_standing_surprised
    jen "Deve tá coberto de poeira e teias de aranha!"
    show jenny f_breakfast_angry_pouting
    show debbie f_breakfast_standing_sad_talk
    deb "Bem, desculpe querida..."
    show player f_diningroom_table_surprised_high_food
    deb "Não sabia"
    show debbie f_breakfast_standing_sad
    pause
    show debbie f_breakfast_standing_sorry_talk
    deb "Que você ia precisar dessa roupa?"
    deb "Provavelmente nem vai caber em você agora."
    show debbie f_breakfast_standing_sorry
    show player f_diningroom_table_surprised_left_food
    show jenny f_breakfast_upset_talk
    jen "Sim, eu sei mas meus fãs"
    show jenny f_breakfast_surprised
    jen "Err... Digo, eu"
    show jenny f_breakfast_surprised_back
    pause
    show jenny f_breakfast_upset_talk
    jen "{b}*Suspiro*{/b} Não é importante, apenas deixa pra lá."
    show jenny f_breakfast_upset
    show debbie f_breakfast_standing_normal_talk
    show player f_diningroom_table_surprised_high_food
    deb "Você quer que eu pegue, e lave pra você?"
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_upset_talk
    show player f_diningroom_table_surprised_left_food
    jen "Ugh, Eu disse esqueça, {b}[deb_name]{/b}!!"
    show debbie f_breakfast_standing_sad
    show jenny f_breakfast_upset
    menu:
        "Permaneça em silencio {color=7ff7}[[Submissive]{/color}":
            show player f_diningroom_table_surprised_teeth_down
            player_name "..."
            show debbie f_breakfast_standing_sad_talk
            deb "Ok, querido."
            hide debbie with dissolve
            pause
            show jenny f_breakfast_upset_talk
            jen "Por que nada nunca vai bem nesta casa?!"
            show jenny f_breakfast_upset
            show player f_magic_sit_stand_worried_talk
            player_name "Eu não sei."
            show player f_magic_sit_stand_worried
            $ M_jenny.decrement("dominance")
        "Diga algo {color=f77b}[[Dominant]{/color}":
            show player f_diningroom_table_grumpy_food_left_talk
            player_name "Hey, don't talk to {b}[deb_name]{/b} like that!"
            show player f_diningroom_table_grumpy_food_left
            show debbie f_breakfast_standing_surprised
            deb "!!!"
            $ M_jenny.increment("dominance")
            if M_jenny.get("dominance") <= 0:
                show jenny f_breakfast_angry_talk
                jen "O que você disse?!"
                show jenny f_breakfast_angry
                show debbie f_breakfast_standing_sad
                show player f_diningroom_table_grumpy_food_left_talk
                player_name "Ela está apenas tentando ajudar!"
                show player f_diningroom_table_grumpy_food_left
                pause
                show jenny f_breakfast_angry_talk
                jen "Bem, eu não pedi a ajuda dela, não é?!"
                show jenny f_breakfast_angry
                show player f_diningroom_table_grumpy_food_left_talk
                player_name "Eu não estava"
                show player f_diningroom_table_surprised_talk_food
                player_name "Eu não queria"
                show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting
                show jenny f_breakfast_angry_talk
                jen "Cuide do seu próprio negócio, perdedor!"
                show jenny f_breakfast_angry
                show player f_diningroom_table_shy_down with dissolve
                player_name "..."
                show debbie f_breakfast_standing_sad_talk
                deb "Vocês dois, por favor, não lutariam na mesa do café da manhã?!"
                hide debbie with dissolve
                deb "Eu simplesmente não entendo de onde ela tira esse temperamento..."
            else:
                show jenny f_breakfast_angry
                show player f_diningroom_table_grumpy_food_left_talk
                player_name "Ela está apenas tentando ajudar!"
                show debbie f_breakfast_standing_sad
                player_name "Você sabe, meio que eu ia ajudá-lo com seu novo emprego..."
                player_name "... Mas agora estou pensando que não vou me incomodar."
                show player f_diningroom_table_grumpy_food_left
                show jenny f_breakfast_surprised
                jen "Isso não é"
                show jenny f_breakfast_surprised_down
                jen "Eu não queria"
                show player f_diningroom_table_worried_talk_high with dissolve
                player_name "{b}[jen_name]{/b} desculpe."
                show player f_magic_sit_stand_worried_talk
                player_name "Você não é?!"
                show player f_magic_sit_stand_worried
                show jenny f_breakfast_angry
                pause
                show player f_magic_sit_stand_worried_talk zorder 1
                player_name "Bem?!"
                show player f_magic_sit_stand_worried
                show jenny f_breakfast_upset_down_talk
                jen "Desculpa, {b}[deb_name]{/b}..."
                show jenny f_breakfast_upset_talk
                jen "... Eu só estou tendo um dia ruim."
                show jenny f_breakfast_upset
                show player f_diningroom_table_normal
                show debbie f_breakfast_standing_sad_talk
                deb "Está tudo bem querida. Compreendo."
                show debbie f_breakfast_standing_sad
                show jenny f_breakfast_upset_down
                pause
                show debbie f_breakfast_kiss_normal_talk b_breakfast_kiss zorder 0 with dissolve
                deb "Obrigado docinho."
                show debbie f_breakfast_kiss_kiss
                show player f_diningroom_table_surprised_left_low
                player_name "!!!"
                show player f_diningroom_table_normal of_diningroom_table_blush
                show jenny f_breakfast_eyeroll
                hide debbie with dissolve
                pause
                show jenny f_breakfast_upset_talk
                jen "Você sabe, eu gostei de você melhor antes de crescer uma espinha dorsal..."
                show jenny f_breakfast_upset
                show player f_magic_sit_stand_worried_talk of_empty
                player_name "Não, você não."
                show player f_magic_sit_stand_worried
                show jenny f_breakfast_eyeroll
                jen "Tanto faz..."
    show jenny f_breakfast_upset_talk
    jen "Antes que você {b}venha para o meu quarto esta tarde{/b}, pegue  meu {b}pop-up no sótão e pegue meu uniforme da alegria{/b}."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Por quê?!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "Porque eu vou usá-lo para o show hoje."
    show jenny f_breakfast_upset
    show player f_diningroom_table_surprised_left
    player_name "!!!"
    show player f_magic_sit_stand_normal_talk
    player_name "Mesmo?!"
    show player f_magic_sit_stand_laugh
    pause
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_eyeroll
    jen "Sim, perv..."
    show jenny b_breakfast_gettingup a_empty f_breakfast_getup_upset_talk with dissolve
    jen "Não se esqueça."
    hide jenny with dissolve
    pause
    show player f_magic_sit_stand_laugh
    player_name "( Hmm, Eu me pergunto o que vamos fazer quando ela usar seu antigo traje de líder de torcida? )"
    return

label dining_room_jenny_pissed_at_blowjob:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_dinner_sitting a_dinner_sitting_resting f_magic_sit_stand_worried zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    jen "..."
    show player f_magic_sit_stand_worried_talk
    player_name "Bom Dia."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Sim, Bom dia"
    show jenny f_breakfast_upset_down
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "Você vai me pagar por ontem?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_angry_talk
    jen "Ahh, você quer ser pago para gozar na minha garganta, hein?"
    show jenny f_breakfast_angry
    if M_jenny.get("dominance")<= 0:
        show player f_magic_sit_stand_worried_talk
        player_name "Eu disse, que me arrependi..."
        show player f_magic_sit_stand_worried
        show jenny f_breakfast_upset_down
        pause
        show player f_magic_sit_stand_worried_talk
        player_name "Você sabe, você gozou na minha boca também!"
        show player f_magic_sit_stand_worried
        show jenny f_breakfast_upset_down_talk
        jen "Haha, Oh sim!"
        jen "eu esqueci disso..."
        show jenny f_breakfast_upset_down
        show player f_magic_sit_stand_worried_talk
        player_name "Você praticamente me afogou!"
        show player f_magic_sit_stand_worried
        show jenny f_breakfast_laugh
        jen "HAHAHAAH!"
    else:
        show player f_magic_sit_stand_worried_talk
        player_name "{b}[jen_name]{/b}, I warned you!"
        show jenny f_breakfast_angry_talk
        jen "Sim, bem, é difícil se concentrar no que você está dizendo!"
        jen "Você é muito bom em"
        show jenny f_breakfast_upset_down_talk
        jen "deixa pra lá."
        show jenny f_breakfast_upset_down
        show player f_magic_sit_stand_worried_talk
        player_name "Muito bom em quê?"
        player_name "... Chupando sua buceta?"
        show player f_magic_sit_stand_worried
        show jenny f_breakfast_upset_down_talk
        jen "Eu não disse isso..."
        show jenny f_breakfast_upset_down
        show player f_magic_sit_stand_normal_talk
        player_name "Mmm, você meio que disse..."
        show player f_magic_sit_stand_normal
        show jenny f_breakfast_upset_down_talk
        jen "Cale-se."
        show jenny f_breakfast_upset_down
        pause
        show player f_magic_sit_stand_worried_talk
        player_name "Então você vai me pagar ou o quê?"
    show jenny f_breakfast_upset_down_talk
    show player f_magic_sit_stand_worried
    jen "{b}*Suspiro*{/b} Está bem."
    show jenny a_breakfast_dressed_money f_breakfast_upset_talk with dissolve
    jen "Eu acho que você ganhou."
    show jenny a_breakfast_dressed_phone f_breakfast_upset_down with dissolve
    show player f_magic_sit_stand_normal_talk
    player_name "Obrigado."
    show player f_diningroom_table_shy_down
    pause
    show jenny f_breakfast_upset_down_talk
    jen "Você sabe, meus fãs realmente gostaram desse show."
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_normal_talk
    player_name "Sim?"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_upset_down_talk
    jen "Tem mais do que o dobro das visualizações que o nosso vídeo de punheta tem."
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_normal_talk
    player_name "Isso é ótimo!"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_grin_talk
    jen "Sim, isso significa que você vai chupar mais buceta."
    show jenny f_breakfast_grin
    if M_jenny.get("dominance") <= 0:
        show player f_diningroom_table_surprised_left
        player_name "!!!"
        show player f_magic_sit_stand_normal_talk
        player_name "OK Sorte a minha."
        show player f_magic_sit_stand_normal
        show jenny f_breakfast_grin_talk
        jen "Sorte e pouco perdedor..."
    else:
        show player f_magic_sit_stand_normal_talk
        player_name "... E você vai estar chupando meu pau."
        show player f_magic_sit_stand_normal
        show jenny f_breakfast_grin_down_talk
        jen "Sim talvez."
        show jenny f_breakfast_grin_down
        show player f_magic_sit_stand_normal_talk
        player_name "Haha!"
        show player f_magic_sit_stand_normal
        show jenny f_breakfast_upset_talk
    jen "Apenas não vá pensando que eu gosto"
    show jenny f_breakfast_surprised
    show player f_diningroom_table_worried_high
    deb "Do que vocês estão falando?"
    player_name "!!!" with hpunch
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_normal_talk
    show jenny f_breakfast_surprised_down
    deb "Ouvir falando {b}[firstname]{/b} foi comer alguma coisa?"
    show debbie f_breakfast_standing_normal
    show player f_diningroom_table_worried_talk_high
    player_name "eu..."
    show jenny f_breakfast_surprised_back
    show player f_magic_sit_stand_worried_talk
    player_name "Nós Hammm..."
    show player f_magic_sit_stand_worried
    jen "Pêssegos!"
    show player f_magic_sit_stand_worried_talk
    player_name "Hã?!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_surprised
    jen "Eu comprei alguns pêssegos no outro dia..."
    show jenny f_breakfast_normal_talk
    jen "... {b}[firstname]{/b} estava comendo meus pêssegos."
    show jenny f_breakfast_normal
    show player f_diningroom_table_worried_high
    show debbie f_breakfast_standing_normal_talk
    deb "Ahh, Eu amo pêssegos!"
    deb "Eles são tão suculentos!"
    show debbie f_breakfast_standing_normal
    show player f_magic_sit_stand_laugh
    player_name "{b}*Snort*{/b}"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_grin_talk
    jen "Hehe, você deveria tê-lo visto quando ele terminou."
    jen "{b}[firstname]{/b} é um comedor desleixado."
    show jenny f_breakfast_grin
    show player f_diningroom_table_normal_high
    show debbie f_breakfast_standing_normal_talk
    deb "Hehe, o rosto dele estava todo bagunçado?"
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_laugh
    jen "Ele ainda tinha alguns em seu cabelo!"
    show jenny f_breakfast_grin
    show debbie f_breakfast_standing_laugh
    deb "Haha!"
    show debbie f_breakfast_standing_normal
    pause
    show debbie f_breakfast_standing_normal_talk
    deb "É legal você estar compartilhando com {b}[firstname]{/b}."
    deb "Um dia, vocês, crianças, vão perceber o quão afortunado você é por ter um ao outro."
    show debbie f_breakfast_standing_normal
    show player f_diningroom_table_normal_talk_high
    player_name "Hehe, você acha?"
    show player f_diningroom_table_normal_high
    show jenny f_breakfast_grin_talk
    jen "Okay, certo."
    show jenny f_breakfast_grin
    show debbie f_breakfast_standing_laugh
    deb "Agora quem quer bacon?!"
    show debbie f_breakfast_standing_normal
    show player f_diningroom_table_normal_talk_high
    player_name "Oh, euu!"
    show player f_diningroom_table_normal_high
    show debbie f_empty b_breakfast_potatoes3 with dissolve
    show jenny f_breakfast_eyeroll
    pause
    scene black with fade
    return

label dining_room_jenny_pissed_at_handjob:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_dinner_sitting a_dinner_sitting_resting f_magic_sit_stand_worried zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause 
    jen "..."
    show player f_magic_sit_stand_worried_talk
    player_name "Você ainda está chateada comigo?"
    show player f_magic_sit_stand_worried
    jen "Hmm?"
    show jenny f_breakfast_upset_down_talk
    jen "Oh."
    jen "Bom dia idiota!"
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_worried_talk
    player_name "Você ainda está brava..."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_angry_talk
    jen "Claro que estou louco!"
    jen "Você é nojento!"
    show jenny f_breakfast_angry
    show player f_magic_sit_stand_worried_talk
    player_name "Olha, eu não queria gozar em você! Foi só"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "Shhh!!!"
    jen "Não tão alto manequim, {b}[deb_name]{/b} vai ouvir você!"
    show jenny f_breakfast_upset
    show player f_diningroom_table_worried_talk_high
    player_name "Certo, desculpe."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_angry_talk
    jen "Eu tive que lavar roupa por sua causa!"
    jen "Você sabe que eu odeio lavar roupa!"
    show jenny f_breakfast_angry
    show player f_magic_sit_stand_worried_talk
    player_name "eu pensei que {b}[deb_name]{/b} lavou a sua roupa?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_angry_talk
    jen "Bem, eu não posso entregar ela um monte de lençóis, sujos cheios de porra para lavar eu posso?!"
    show jenny f_breakfast_angry
    show player f_magic_sit_stand_worried_talk
    player_name "Não, acho que não..."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_eyeroll
    jen "Idiota."
    show jenny f_breakfast_upset
    if M_jenny.get("dominance") <= 0:
        player_name "..."
        show player f_magic_sit_stand_worried_talk
        player_name "Sério, me desculpe!"
        show player f_magic_sit_stand_worried
    else:
        show player f_magic_sit_stand_worried_talk
        player_name "Não seja uma vadia."
        show player f_magic_sit_stand_worried
        show jenny f_breakfast_upset_talk
        jen "Ugh."
    show jenny f_breakfast_upset_talk
    jen "Tanto faz."
    jen "Da próxima vez que isso acontecer, VOCÊ ESTÁ lavando meus lençóis!"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "próxima vez?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "Bem, sim..."
    show jenny f_breakfast_normal_talk
    jen "We made mad bank yesterday!"
    show jenny f_breakfast_normal
    show player f_magic_sit_stand_worried_talk
    player_name "Mesmo?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_normal_talk
    jen "Aqui."
    show jenny a_breakfast_dressed_money with dissolve
    jen "Sua parte."
    show jenny f_breakfast_normal
    show player f_magic_sit_stand_normal_talk
    player_name "Obrigado!"
    show player f_magic_sit_stand_normal
    show jenny a_breakfast_dressed_spoon f_breakfast_normal with dissolve
    pause
    show player f_magic_sit_stand_normal_talk
    player_name "Então, quando é o nosso próximo show?"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_normal_talk
    jen "A qualquer momento {b}a tarde{/b} funciona para mim."
    jen "Somente {b}venha para o meu quarto{/b}."
    show jenny f_breakfast_normal
    show player f_magic_sit_stand_normal_talk
    player_name "Impressionante!"
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_normal_talk with dissolve
    show player f_diningroom_table_normal_high
    show jenny f_breakfast_normal_low
    deb "Quem está com fome?"
    show debbie f_breakfast_standing_normal
    show player f_diningroom_table_normal_talk_high
    player_name "Euuu!"
    show player f_diningroom_table_normal_high
    show debbie f_breakfast_standing_normal_talk
    deb "Hehe!"
    deb "Aqui vai, querido."
    show debbie b_breakfast_potatoes3 f_empty with dissolve
    show player f_diningroom_table_normal
    pause
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_normal_talk with dissolve
    deb "Vocês estão se dando bem?"
    show debbie f_breakfast_standing_normal
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_sad
    pause
    show player f_diningroom_table_normal_talk
    player_name "Sim muito bem?"
    show jenny f_breakfast_normal_low
    show player f_diningroom_table_normal_high
    show debbie f_breakfast_standing_normal_talk
    deb "Bom."
    deb "Aquece meu coração, vocês dois passando tempo juntos."
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_eyeroll
    show player f_diningroom_table_normal_talk_high
    player_name "Obrigado, {b}[deb_name]{/b}."
    show jenny f_breakfast_normal_low
    show player f_diningroom_table_normal_high
    deb "Mmhmm."
    show player f_diningroom_table_shy_down
    hide debbie with dissolve
    pause
    call screen money_popup(100)
    $ player.get_money(100)
    scene black with fade
    return

label dining_room_jenny_cedric_upset:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_normal_low zorder 1
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    show player 323e zorder 0 at Position(xpos=610,ypos=770) with dissolve
    player_name "Bom Dia."
    hide player
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating b_dinner_sitting zorder 0 at Position(align=(0,0))
    with dissolve
    jen "..."
    pause
    show jenny f_breakfast_upset_down_talk
    show player f_diningroom_table_surprised_left_food a_dinner_sitting_resting
    jen "Idiota!!!" with hpunch
    jen "Grr!"
    show jenny f_breakfast_upset_down
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "Qual é o seu problema?"
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_angry_talk
    jen "Porra {b}Cedric{/b}!"
    show jenny f_breakfast_angry
    show player f_diningroom_table_surprised_talk_food
    player_name "{b}Cedric{/b}, seu ex-namorado?"
    show player f_diningroom_table_surprised_left_food
    show jenny f_breakfast_angry_talk
    jen "Você conhece alguma outra pessoa chamada {b}Cedric{/b}?!"
    show jenny f_breakfast_angry
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "Não."
    show player f_diningroom_table_grumpy_food_left_talk
    pause
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_eyeroll
    jen "... Idiota."
    show jenny f_breakfast_upset
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "Por que você é sempre tão puta comigo?"
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_upset_talk
    jen "Umm, Não sei ... Por que você é sempre tão pervertido comigo?"
    show jenny f_breakfast_upset
    show player f_diningroom_table_surprised_left_food
    deb "O que está acontecendo aqui?" with hpunch
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_sad with dissolve
    show player f_diningroom_table_surprised_high_food
    player_name "..."
    show jenny f_breakfast_upset_talk
    jen "Nada, {b}[deb_name]{/b}."
    show jenny f_breakfast_upset
    show debbie f_breakfast_standing_sad_talk
    deb "Eu ouvi gritos."
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_surprised_talk_high_food
    player_name "Ela está apenas gritando com seu celular como uma pessoa maluca."
    show player f_diningroom_table_surprised_high_food
    show jenny f_breakfast_angry_talk
    jen "Dane-se, {b}[firstname]{/b}!"
    show jenny f_breakfast_angry
    show debbie f_breakfast_standing_sad_talk
    deb "Ei, pare com isso, os dois!"
    show debbie f_breakfast_standing_sad
    show jenny f_breakfast_upset_down
    show player f_diningroom_table_surprised_talk_high_food
    player_name "Desculpa, {b}[deb_name]{/b}."
    show player f_diningroom_table_surprised_high_food
    jen "..."
    show debbie f_breakfast_standing_sad_talk
    deb "Por que você está gritando com o seu telefone? {b}[jen_name]{/b}?"
    show debbie f_breakfast_standing_sad
    show jenny f_breakfast_upset_down_talk
    jen "{b}*Suspiro*{/b} Não é nada..."
    jen "... {b}Cedric{/b} está apenas se recusando a responder meus textos."
    show jenny f_breakfast_upset_down
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "Eu não o culpo."
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_angry
    show debbie f_breakfast_standing_sad_talk
    deb "{b}[firstname]{/b}!"
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_surprised_high_food
    player_name "..."
    show player a_dinner_sitting_bowl f_diningroom_table_shy_down with dissolve
    show debbie f_breakfast_standing_sad_talk
    deb "Eu pensei que você terminou com {b}Cedric{/b}?"
    show debbie f_breakfast_standing_sad
    show jenny f_breakfast_upset_talk
    jen "eu fiz."
    show jenny f_breakfast_upset
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    show debbie f_breakfast_standing_sad_talk
    deb "Então, por que você está mandando mensagens para ele?"
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting with dissolve
    show jenny f_breakfast_upset_talk
    jen "Eu preciso dele para"
    show player f_diningroom_table_surprised_left_food
    show jenny f_breakfast_sad_talk
    pause
    show jenny f_breakfast_upset_talk
    jen "{b}*Ahem*{/b} Eu preciso da ajuda dele ... Com o trabalho."
    show jenny f_breakfast_upset
    show player a_dinner_sitting_bowl f_diningroom_table_shy_down with dissolve
    show debbie f_breakfast_standing_normal_talk
    deb "Oh."
    show debbie f_breakfast_standing_normal
    show player f_magic_sit_stand_normal_talk with dissolve
    player_name "{b}Cedric{/b} vai ajudá-la a transcrever?"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_angry
    pause
    show player f_magic_sit_stand_normal_talk
    player_name "Você ainda está fazendo isso, certo?"
    show player f_magic_sit_stand_normal
    jen "..."
    show player a_dinner_sitting_bowl f_diningroom_table_shy_down with dissolve
    show debbie f_breakfast_standing_normal_talk
    deb "Por que você não liga para ele, querida?"
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_upset_talk
    jen "Eu tenho tentado, ele não responder."
    show jenny f_breakfast_upset
    show debbie f_breakfast_standing_normal_talk
    deb "Bem, por que você não"
    show debbie f_breakfast_standing_normal
    "{b}*Chiar*{/b}"
    show debbie f_breakfast_standing_sad
    pause
    show player f_diningroom_table_worried_high
    show debbie f_breakfast_standing_sad_talk
    deb "Oh, tiro!"
    hide debbie with dissolve
    deb "Eu esqueci do café da manhã!"
    show player f_diningroom_table_shy_down
    show jenny f_breakfast_grin
    pause
    show jenny f_breakfast_grin_talk
    jen "Parece que você vai comer bacon queimado hoje, perdedor."
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_worried_talk
    player_name "Ainda é melhor que esse cereal que você está comendo."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_grin_talk
    jen "Tanto faz."
    show jenny f_breakfast_upset_down
    show player a_dinner_sitting_bowl f_diningroom_table_shy_down with dissolve
    pause
    pause
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    show jenny f_breakfast_angry_talk
    jen "Filho da puta!"
    show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting with dissolve
    jen "Você vai para {b}o ginásio{/b} e diga a esse idiota para me ligar?"
    show jenny f_breakfast_angry
    show player f_diningroom_table_surprised_talk_food
    player_name "Hã?"
    player_name "De jeito nenhum!"
    show player f_diningroom_table_surprised_left_food
    show player f_magic_sit_stand_normal_talk
    show jenny f_breakfast_upset_talk
    jen "Ahh, Vamos {b}[firstname]{/b}."
    show jenny f_breakfast_upset
    show player f_diningroom_table_surprised_talk_food
    player_name "Eu odeio esse cara!"
    player_name "Ele sempre me trata como uma criancinha."
    show player f_diningroom_table_surprised_left_food
    show jenny f_breakfast_grin_talk
    jen "Bem, comparado a ele, você é um garotinho."
    show jenny f_breakfast_grin
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "Absolutamente não."
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_angry_talk
    jen "VAMOS!"
    show jenny f_breakfast_angry
    pause
    show jenny f_breakfast_upset_talk
    jen "E se eu ficar nua para você de novo?"
    show jenny f_breakfast_upset
    show player f_diningroom_table_surprised_talk_food
    player_name "Completamente nua?"
    show player f_diningroom_table_surprised_left_food
    show jenny f_breakfast_eyeroll
    jen "Foi o que eu disse, manequim."
    show jenny f_breakfast_upset
    show player f_diningroom_table_surprised_talk_food
    player_name "Posso tocar?"
    show player f_diningroom_table_surprised_left_food
    show jenny f_breakfast_upset_talk
    jen "{b}*Suspiro*{/b} Eu suponho..."
    jen "... Mas apenas meus peitos."
    show jenny f_breakfast_upset
    if M_jenny.get("dominance") <= 0:
        show player f_magic_sit_stand_laugh od_dinner_sitting_boner
        player_name "Feito!"
    else:
        show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
        pause
        show player f_diningroom_table_grumpy_food_left_talk with dissolve
        player_name "Esqueça, eu tenho coisas melhores para fazer."
        show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting
        show jenny f_breakfast_angry
        pause
        jen "Grr!!"
        show jenny f_breakfast_angry_talk
        jen "Tudo bem, ok?!"
        show jenny f_breakfast_upset_talk
        jen "Você pode tocar o que quiser..."
    show player f_magic_sit_stand_normal
    show jenny b_breakfast_gettingup f_breakfast_getup_upset_talk a_empty with dissolve
    jen "Vamos lá, vamos!"
    show jenny f_breakfast_getup_upset
    show player f_magic_sit_stand_normal_talk
    player_name "Assim que terminar o café da manhã."
    show jenny b_breakfast_pulling f_empty
    hide player
    hide player_dick
    with dissolve
    player_name "!!!"
    hide jenny with dissolve
    jen "Agora não!"
    $ player.go_to(L_home_kitchen)
    scene expression player.location.background_closeup with None
    show jenny b_dressed_pulling2 a_empty f_upset at flip
    show jenny at Position (xpos=-150)
    show debbie
    with dissolve
    player_name "Ei, pare de me puxar!"
    show jenny b_dressed_pulling1
    show debbie f_normal_talk
    deb "O café da manhã está quase pronto se vocês dois quiserem-"
    show debbie f_surprised
    pause
    show debbie f_normal_talk
    deb "Vocês estão indo para algum lugar?"
    show debbie f_normal
    show jenny f_normal_talk
    jen "{b}[firstname]{/b} vai falar com {b}Cedric{/b} para mim."
    show jenny f_normal
    show debbie f_normal_talk
    deb "Bem, isso é legal da parte dele."
    show debbie f_normal
    pause
    show jenny b_dressed_pulling2
    player_name "Espere um segundo, eu quero o meu café da manhã"
    show jenny b_dressed_pulling1 f_upset_talk
    jen "Cale-se!"
    show jenny f_upset
    pause
    show debbie f_laugh
    deb "Estou feliz que vocês dois estão finalmente passando tempo juntos!"
    hide jenny
    hide player
    with dissolve
    show debbie f_normal
    pause
    show debbie f_normal_talk
    deb "Já era hora de se ligarem um pouco..."
    hide debbie with dissolve
    pause
    $ player.go_to(L_home_sisbedroom)
    scene expression player.location.background_closeup with None
    show jenny b_dressed_pulling2 a_empty f_upset
    player_name "Ack!"
    show player 12 at left
    show jenny b_dressed a_dressed_hips f_upset
    with dissolve
    player_name "Qual é a pressa?!"
    player_name "Eu prometo, vou falar com"
    show player 11
    show jenny b_pull1 a_empty f_grin_down with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    show player 10
    player_name "... to..."
    show player 11
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show jenny b_naked a_naked_panties_remove f_grin_down with dissolve
    player_name "..."
    show jenny b_naked_panties_remove_down f_empty a_empty with dissolve
    pause
    show jenny b_naked f_upset_talk a_naked_hips with dissolve
    jen "eu preciso que chame {b}Cedric{/b} o mais rápido possível!"
    show jenny f_eyeroll
    jen "Então vamos nos apressar e acabar com isso..."
    show jenny f_gross
    if M_jenny.get("dominance") <= 0:
        player_name "..."
        show jenny f_upset_talk
        jen "Você vai tocá-los ou o que?!"
        show jenny f_gross
        player_name "Hmm?"
        show jenny f_eyeroll a_naked_breasts with dissolve
        pause
        show jenny f_gross a_naked_hips with dissolve
        show player 22
        player_name "OH!"
        show player 14
        player_name "Certo."
        hide player
        show jenny b_groping_naked_touch_talk a_groping_naked_hips f_upset
        with dissolve
        player_name "Uau!"
        show jenny b_groping_naked_touch with dissolve
        pause
        player_name "Eles são muito legais!"
        show jenny f_upset_talk
        jen "Me diga algo que eu não sei..."
        show jenny f_upset
        pause
        show jenny f_upset_talk b_groping_naked_suck_pre with dissolve
        jen "Os caras sempre amam"
        show jenny f_nipple1 b_groping_naked_suck a_groping_naked_up_clench
        jen "!!!" with hpunch
        jen "O que você é"
        pause
        show jenny f_nipple2
        jen "Ahh..."
        pause
        jen "I didn't-"
        pause
        jen "Ffffuuu-"
        pause
        jen "Ngghhh!!"
        show jenny f_upset_talk b_groping_naked_cover
        show player 24 at left
        with dissolve
        jen "Tudo bem, pare!!"
        show jenny f_upset
        show player 10
        player_name "Qual é o problema?"
        show player 5
        show jenny f_upset_talk
        jen "Isso é muito por hoje!"
        jen "Vá falar com {b}Cedric{/b}."
        show jenny f_upset
        show player 12
        player_name "Ugh, tudo bem."
        player_name "Onde você disse que eu poderia encontrá-lo?"
        show player 5
        show jenny f_upset_talk
        jen "Ele provavelmente estará no {b}ginásio{/b}."
        jen "Esse estupido está sempre no {b}ginásio{/b}."
        show jenny f_upset
        show player 17
        player_name "estou a caminho."
        hide player with dissolve
        pause
        show jenny b_groping_naked_orgasm a_empty f_orgasm_nipple3 at Position (yoffset=66) with dissolve
        jen "( Hmm, nada mal para um pouco perdedor virgem... )"
        pause
        scene black with fade
    else:

        show player 14
        player_name "Ok."
        hide player
        show jenny f_nipple1 b_groping_naked_suck a_groping_naked_up_clench
        jen "!!!" with hpunch
        pause
        show jenny f_nipple2
        jen "Jesus, você está apenas pulando para a direita"
        jen "Ahh!"
        pause
        show jenny f_nipple3
        jen "Mmm."
        pause
        show jenny f_nipple1 b_groping_naked_finger
        jen "Ah Merda!"
        show jenny f_nipple2
        pause
        jen "Ffffuuu-"
        pause
        jen "Eu vou!"
        show player 11 at Position (xpos=300)
        show jenny b_groping_naked_orgasm a_empty f_orgasm_nipple2 at Position (yoffset=66)
        jen "Ngghhh!!!" with flash
        pause
        pause
        show jenny b_groping_naked_cover a_groping_naked_up_clench f_upset_talk
        jen "Haah ... Porra!"
        show jenny f_upset
        show player 10
        player_name "Você acabou de gozar?"
        show player 5
        show jenny f_angry_talk
        jen "O que? NÃO!"
        show jenny f_angry
        show player 17
        player_name "Sim, você fez! Olhe meus dedos!"
        show player 734 with dissolve
        show jenny f_angry_talk
        jen "Cale-se!"
        show jenny f_angry
        show player 13
        pause
        show jenny f_angry_talk
        jen "Isso é muito por hoje!"
        show jenny f_angry
        show player 14
        player_name "Hehe, você acabou de esguichar na minha mão!"
        show player 13
        show jenny f_angry_talk
        jen "Eu falei cala a boca!!!"
        jen "Vá falar com {b}Cedric{/b}."
        show jenny f_angry
        show player 10
        player_name "Ugh, tudo bem."
        show player 12
        player_name "Onde você disse que eu poderia encontrá-lo?"
        show player 5
        show jenny f_upset_talk
        jen "Ele provavelmente estará no {b}ginásio{/b}."
        jen "Esse estupido está sempre em {b}o ginásio{/b}."
        show jenny f_upset
        show player 12
        player_name "Indo."
        hide player with dissolve
        pause
        show jenny b_groping_naked_orgasm a_empty f_orgasm_nipple3 at Position (yoffset=66) with dissolve
        jen "( De onde diabos veio isso?! )"
        scene black with fade
    return

label dining_room_jenny_have_breakfast_3:
    scene expression game.timer.image("dining_room{}")
    show debbie b_breakfast_sitting a_breakfast_rest f_breakfast_sitting_normal zorder 1
    show player b_dinner_sitting a_dinner_sitting_resting f_diningroom_table_normal_talk zorder 0 at Position(align=(0,0)) with dissolve
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    player_name "Mmm, aquilo foi tão bom {b}[deb_name]{/b}!"
    player_name "Você é a melhor cozinheira do mundo inteiro!"
    show player f_diningroom_table_normal
    show debbie f_breakfast_sitting_laugh
    deb "Ah, hehe!"
    show debbie f_breakfast_sitting_normal_talk
    deb "Obrigado querido."
    show debbie f_breakfast_sitting_normal
    show player f_diningroom_table_normal_talk
    player_name "Você quer ajuda com os pratos?"
    show player f_diningroom_table_normal
    show debbie f_breakfast_sitting_normal_talk
    deb "Oh, não..."
    deb "Eu posso lidar bem com isso. Não se preocupe!"
    deb "Estou de bom humor, agora que {b}[jen_name]{/b} encontrou um emprego."
    deb "Eu estava tão preocupado com ela!"
    show debbie f_breakfast_sitting_normal
    show player f_magic_sit_stand_laugh
    player_name "Heh, sim."
    show player f_diningroom_table_normal
    show debbie f_breakfast_sitting_normal_talk
    deb "Transcrevendo..."
    deb "Eu não sabia que ela tinha isso nela!"
    show debbie f_breakfast_sitting_normal
    show player f_magic_sit_stand_worried_talk
    player_name "Uh Hã..."
    show player f_diningroom_table_shy_down
    show debbie f_breakfast_sitting_normal_talk
    deb "Oh, me desculpe por ficar tagarelando."
    deb "Tenho certeza que você tem um milhão de coisas que você preferiria fazer do que me ouvir."
    show debbie f_breakfast_sitting_normal
    show player f_magic_sit_stand_worried_talk
    player_name "Não, não mesmo!"
    show player f_diningroom_table_normal_talk
    player_name "eu gosto"
    show player f_diningroom_table_normal
    show debbie f_breakfast_sitting_normal_talk
    deb "Você pode ir agora e tenha um bom dia, certo?"
    show debbie f_breakfast_sitting_normal
    pause
    show player f_diningroom_table_normal_talk
    player_name "Ok."
    show player f_diningroom_table_normal
    pause
    show player f_diningroom_table_normal_talk
    player_name "Obrigado novamente pelo café da manhã."
    show player f_diningroom_table_normal
    show debbie f_breakfast_sitting_normal_talk
    deb "Foi um prazer, querido."
    hide player with dissolve
    $ player.go_to(L_home_entrance)
    scene expression player.location.background_blur
    show player f_worried
    with dissolve
    player_name "( Eu não posso acreditar {b}[deb_name]{/b} caiu nessa história de transcrição... )"
    pause
    show player a_dressed_thinking f_thinking with dissolve
    player_name "( Hmm, eu imagino o que {b}[jen_name]{/b} está realmente fazendo? )"
    hide player with dissolve
    return

label dining_room_jenny_have_breakfast_2:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_normal_low zorder 1
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    show player 323e zorder 0 at Position(xpos=610,ypos=770) with dissolve
    player_name "Bom dia."
    hide player
    show player b_dinner_sitting a_dinner_sitting_bowl f_diningroom_table_shy_down zorder 0 at Position(align=(0,0))
    with dissolve
    pause
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_resting with dissolve
    pause
    show player f_diningroom_table_grumpy_food_left_talk with dissolve
    player_name "Olá?!"
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_upset_down_talk
    jen "Hmm, o que?!"
    show jenny f_breakfast_upset_down
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "Qual é o seu problema?"
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_upset_down_talk
    jen "Nada, me deixe em paz."
    show jenny f_breakfast_upset_down
    show player a_dinner_sitting_bowl f_diningroom_table_shy_down with dissolve
    player_name "..."
    pause
    show jenny f_breakfast_eyeroll
    jen "Ugh, este estupido {b}Sluttygram{/b} é uma perda de tempo!"
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_worried_talk with dissolve
    player_name "Essas fotos não ajudaram?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Eles fizeram, mas isso não está me fazendo dinheiro suficiente..."
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_worried_talk
    player_name "Sim, bem {b}Sluttygram{/b} é muito pequena batata em comparação com o que está lá fora..."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "O que você quer dizer?"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Você percebe que a pornografia existe, certo?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "Sim, então?"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Por que alguém pagaria um bom dinheiro para ver fotos sensuais sem nudez quando elas podem assistir a pornografia pesada, de graça?!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_eyeroll
    jen "Umm, Eu não sei ... Que tal porque eu sou gostosa e essas perolas pornô não são?!"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_laugh
    player_name "Você está brincando certo?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_angry_talk
    jen "Não cale a boca!"
    show jenny b_breakfast_gettingup f_breakfast_getup_upset_talk a_empty with dissolve
    jen "Não finja que você não acha que eu sou gostosa!"
    show jenny f_breakfast_getup_upset
    show player f_diningroom_table_surprised_forward
    player_name "..."
    show jenny f_breakfast_getup_angry_talk
    jen "Diz!"
    show jenny f_breakfast_getup_angry
    return

label dining_room_jenny_have_breakfast_2_youre_hot:
    show player f_magic_sit_stand_worried_talk
    player_name "Você é sexy."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_getup_angry_talk
    jen "Droga, certo!"
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down with dissolve
    show player a_dinner_sitting_bowl f_diningroom_table_shy_down with dissolve
    pause
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    pause
    show player f_diningroom_table_grumpy_food_left_talk with dissolve
    player_name "Mas ainda é pequenas batatas."
    show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting
    show jenny f_breakfast_upset_down_talk
    jen "Sim Sim..."
    show jenny f_breakfast_upset_down
    pause
    show jenny f_breakfast_eyeroll
    jen "Grr, eu preciso de mais dinheiro!!!"
    show jenny f_breakfast_upset_down
    pause
    show player a_dinner_sitting_bowl f_diningroom_table_shy_down with dissolve
    show jenny f_breakfast_upset
    pause
    show jenny f_breakfast_upset_talk
    jen "Venha comigo."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk with dissolve
    player_name "Onde?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "Para o meu quarto, manequim."
    jen "Eu tenho uma proposta para você."
    hide jenny with dissolve
    show player f_magic_sit_stand_worried_talk
    player_name "Uhh, ok."
    show player f_magic_sit_stand_worried
    player_name "( Espero não ter irritado ela... )"
    hide player with dissolve
    return

label dining_room_jenny_have_breakfast_2_no:
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    pause
    show player f_diningroom_table_grumpy_food_left_talk a_dinner_sitting_resting with dissolve
    player_name "Uau, você está tão desesperada por atenção?"
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_getup_upset_talk
    jen "O que?!"
    jen "Isso não é"
    show jenny f_breakfast_getup_angry
    pause
    show jenny f_breakfast_getup_angry_talk
    jen "CALE-SE!"
    show jenny f_breakfast_getup_angry
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "Hehe  você me chamou de patético..."
    show player f_diningroom_table_grumpy_food_left
    jen "Grrr!!"
    hide jenny with dissolve
    show player f_diningroom_table_looking_down_food
    pause
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_sad_talk with dissolve
    deb "O que aconteceu com ela esta manhã?"
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_surprised_talk_high_food
    player_name "Quem sabe?"
    show player f_diningroom_table_surprised_high_food
    show debbie f_breakfast_standing_sad_talk
    deb "Todo este negócio de trabalho deve realmente estar estressando ela"
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_surprised_talk_high_food
    player_name "Sim talvez."
    show player f_diningroom_table_surprised_high_food
    show debbie f_breakfast_standing_sad_talk
    deb "Falou alguma coisa."
    deb "Aqui está mais um café da manhã, querido."
    show debbie b_breakfast_potatoes3 f_empty with dissolve
    pause
    show debbie b_breakfast_potatoes f_breakfast_standing_normal with dissolve
    show player f_diningroom_table_surprised_talk_high_food
    player_name "Obrigado, {b}[deb_name]{/b}!"
    show player b_dinner_sitting a_dinner_sitting_bowl f_diningroom_table_shy_down with dissolve
    hide debbie with dissolve
    pause
    player_name "( Eu provavelmente deveria ir e verificar {b}[jen_name]{/b}... )"
    player_name "( Eu não estava tentando ser má, ela realmente sabe como apertar meus botões. )"
    player_name "( Não até depois de comer este delicioso café da manhã! )"
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    return

label dining_room_sis_breakfast_started:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_normal_low zorder 1
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    show player 323d zorder 0 at Position(xpos=610,ypos=770)
    with fade
    player_name "( Hã. {b}[jen_name]{/b} já está acordada? )"
    player_name "( Ela geralmente dorme mais. )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
