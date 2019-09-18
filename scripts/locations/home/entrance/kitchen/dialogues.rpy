label kitchen_jenny_final_breakfast:
    scene expression player.location.background_closeup with None
    show jenny f_upset at flip
    show jenny at Position (xpos=150)
    show debbie f_sad_talk at Position (xpos=600)
    with fade
    deb "Seria um sofrimento {b}[jen_name]{/b}..."
    deb "Eu nunca quis que você partisse em primeiro lugar!"
    show debbie f_sad
    show jenny f_eyeroll
    jen "Bem, eu quero conseguir um lugar sò meu.."
    show jenny f_sad_talk
    jen "Mais Eu não estou pronto ainda."
    show jenny f_sad
    show debbie f_normal_talk
    deb "Isso é Bom, querida."
    deb "Você está convidada a ficar aqui para sempre."
    show debbie f_laugh
    deb "Deus sabe, Você poderia ser de grande a ajuda!"
    show debbie f_normal
    show jenny f_normal_talk
    jen "Sim, isso é exatamente o que eu estava pensando e com o meu trabalho indo tão bem, eu poderia  gastar mais algumas centenas por mês."
    show jenny f_normal
    show debbie f_normal_talk
    deb "Isso seria maravilhoso, querida!"
    show debbie f_normal
    show player f_normal_talk at Position (xpos=450) with dissolve
    player_name "O que está acontecendo?"
    show player f_normal
    show debbie f_normal_talk
    deb "Bom dia, querido!"
    deb "Nós estávamos falando sobre {b}[jen_name]{/b} mudar."
    show debbie f_normal
    show player f_shock
    player_name "O QUE?!"
    show player f_worried_talk
    player_name "Você está saindo?!"
    show player f_worried
    show jenny f_grin at unflip
    show jenny at Position (xpos=-200)
    with dissolve
    show debbie f_laugh
    deb "Oh, não não não!"
    show debbie f_normal_talk
    deb "Eu quis dizer, ela não está saindo."
    show debbie f_normal
    show jenny f_normal_talk
    jen "Sim, decidi ficar aqui mais um pouco."
    jen "Economizar algum dinheiro, sabe?"
    show jenny f_normal
    show debbie f_normal_talk
    deb "Não é maravilhoso, {b}[firstname]{/b}?!"
    show debbie f_normal
    show player f_normal_talk
    player_name "Sim, maravilhoso!"
    show player f_normal with None
    hide jenny
    show debbie b_robe_hug3 a_empty f_empty
    with dissolve
    deb "Estou tão orgulhosa de você, querida!"
    show debbie b_robe_hug4
    jen "Obrigada, {b}[deb_name]{/b}..."
    show debbie f_normal_talk b_robe a_robe_mug
    show jenny at flip
    show jenny b_dressed a_dressed_hips at Position (xpos=250)
    with dissolve
    deb "Por que vocês dois não vão se sentar à mesa e eu vou preparar alguns ovos e bacon?"
    show debbie f_normal
    show jenny f_normal_talk
    jen "Tudo bem."
    hide jenny with dissolve
    show player f_laugh
    player_name "Mmm, isso parece ótimo!"
    hide player with dissolve
    $ player.go_to(L_home_diningroom)
    scene expression game.timer.image("dining_room{}")
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 3
    show player b_magic_sit_stand_dressed f_magic_sit_stand_worried a_magic_sit_stand_resting zorder 1 at Position (align=(0,0))
    show jenny f_magic_sit_stand_phone_upset a_magic_sit_stand_phone b_magic_sit_stand_dressed zorder 1 at Position (align=(0,0))
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "Então uhh..."
    player_name "Sobre a noite passada..."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "Ugh, você não vai começar com essa besteira de namoro de novo, vai?"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Por que você está sendo tão esquisita sobre isso?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_angry_talk
    jen "Umm, você é o único sendo estranho!"
    show jenny f_breakfast_upset_talk a_magic_sit_stand_hip_spoon with dissolve
    jen "Eu não estou interessado em namorar você, {b}[firstname]{/b}..."
    jen "Estamos fazendo sexo e ganhando muito dinheiro, por que isso não é suficiente para você?!"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Você realmente não quer mais?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "O que, como casamento e filhos?!"
    jen "Uma casinha de tijolos com uma cerca branca?"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_normal_talk
    player_name "... Isso sería legal."
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_gross_talk
    jen "Eca, não me faça vomitar!"
    show jenny f_breakfast_gross
    show player f_magic_sit_stand_worried
    player_name "..."
    show jenny f_breakfast_upset
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_normal_talk zorder 2 with dissolve
    show player f_diningroom_table_normal_high
    deb "Tudo bem, quem está com fome?!"
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_upset_talk
    jen "Bem aqui!"
    show jenny f_breakfast_upset
    show debbie b_breakfast_potatoes3 f_empty with dissolve
    show player f_diningroom_table_normal
    pause
    show debbie b_breakfast_potatoes f_breakfast_standing_normal_talk with dissolve
    show player f_diningroom_table_shy_down
    deb "Do que vocês estavam falando?"
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_upset_talk
    jen "Nada importante."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried
    player_name "..."
    show player f_diningroom_table_worried_talk_high
    player_name "Na verdade, acabei de perder meu apetite."
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_worried_high
    show jenny f_breakfast_eyeroll
    jen "Ugh, Então, agora você está louco?"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried
    deb "..."
    show player f_diningroom_table_worried_talk
    player_name "Posso ser desculpado?"
    show player f_diningroom_table_worried
    show debbie f_breakfast_standing_sad_talk
    deb "Claro..."
    deb "Está tudo bem, querido?"
    show debbie f_breakfast_standing_sad
    show player f_magic_sit_stand_tired_talk
    player_name "Sim eu estou bem."
    hide player with dissolve
    show debbie f_breakfast_standing_sad_talk
    deb "O que está acontecendo com vocês dois?"
    show debbie f_breakfast_standing_sad
    show jenny f_breakfast_upset_talk
    jen "Não é nada, {b}[deb_name]{/b}."
    jen "É o {b}[firstname]{/b} Sendo apenas um grande bebê..."
    show jenny f_breakfast_upset
    $ player.go_to(L_home_entrance)
    scene expression player.location.background_closeup with None
    show player f_worried with dissolve
    player_name "( Bem, isso poderia ter sido melhor... )"
    pause
    show player f_skeptical
    player_name "( Ela é tão teimosa! )"
    player_name "( Mesmo que ela quisesse ela, nunca admitiria. )"
    show player f_tired
    player_name "( *Suspiro* )"
    show player f_worried
    player_name "( Eu deveria apenas {b}da-lhe algum espaço{/b}... )"
    player_name "( ... Talvez ela me procure?)"
    hide player with dissolve
    return

label kitchen_jenny_helping_with_breakfast_confront_her:
    show debbie f_normal_talk
    deb "Querido, você vem?"
    show debbie f_normal
    show player 10 with dissolve
    player_name "Na verdade, só lembro de algo que preciso fazer."
    show player 5
    show debbie f_sad_talk
    deb "Oh."
    show debbie f_sad
    show player 10
    player_name "Verificação de chuva?"
    show player 5
    show debbie f_normal_talk
    deb "Certo!"
    show debbie f_normal
    show player 14
    player_name "Obrigado, {b}[deb_name]{/b}."
    show player 5
    hide debbie with dissolve
    player_name "( {b}[jen_name]{/b} disse que ela estava subindo as escadas para tomar um banho. )"
    player_name "( Eu deveria me apressar se eu quero pegá-la! )"
    hide player with dissolve
    return

label kitchen_jenny_helping_with_breakfast_let_it_go:
    show player 4 with dissolve
    player_name "( Hmm, tanto faz. )"
    show player 5 with dissolve
    player_name "( {b}*Suspiro*{/b} Eu provavelmente não deveria me preocupar muito com isso. )"
    player_name "( Quero dizer, pelo menos ela está dando dinheiro para {b}[deb_name]{/b} agora... )"
    player_name "( Isso é importante. )"
    deb "Querido, você vem?"
    show player 14
    player_name "Sim!"
    show player 13
    player_name "( Eu deveria ir para a sala de jantar e me juntar com a {b}[deb_name]{/b} para o café da manhã. )"
    hide player with dissolve
    return

label kitchen_jenny_helping_with_breakfast:
    scene expression player.location.background_closeup with None
    show debbie f_normal_talk
    show jenny at flip
    show jenny at Position (xpos=150)
    with dissolve
    deb "Bem, claro que estou feliz que você vai começar a contribuir, querida."
    deb "Estou apenas curiosa sobre esse novo trabalho que você tem?"
    show debbie f_normal
    show jenny f_eyeroll
    jen "Ugh, não é nada  de especial {b}[deb_name]{/b}..."
    show jenny f_normal
    show debbie f_normal_talk
    deb "Transcrevendo, você disse?"
    show debbie f_normal
    show jenny f_normal_talk
    jen "Sim."
    show jenny f_normal
    show debbie f_normal_talk
    deb "O que você está transcrevendo?"
    show debbie f_normal
    show jenny f_normal_talk
    jen "Não sei, {b}[deb_name]{/b}..."
    show jenny f_normal
    pause
    show jenny f_normal_talk
    jen "Chamadas de atendimento ao cliente e outras coisas."
    show jenny f_normal
    show debbie f_laugh
    deb "Oh, isso é legal!"
    show debbie f_normal
    show jenny f_normal_talk
    jen "Não, é muito chato."
    jen "Mais paga um bom dinheiro."
    show jenny f_normal
    show player 13 at left
    show debbie f_normal_talk
    deb "Estou orgulhosa de você, querida."
    show debbie f_normal
    show jenny f_eyeroll
    jen "Hã."
    show jenny f_normal
    show player 14
    player_name "O que está acontecendo?"
    show player 13
    show debbie f_normal_talk
    deb "{b}[jen_name]{/b} estava apenas me contando sobre seu novo trabalho."
    show debbie f_normal
    show player 12
    player_name "Sério?"
    show player 91 with None
    show jenny f_angry a_dressed_crossed at unflip
    show jenny at Position (xpos=-250)
    with dissolve
    show debbie f_normal_talk
    deb "Ela está transcrevendo coisas pela internet."
    show debbie f_normal
    show player 92
    player_name "Você não diz..."
    show player 91
    show debbie f_normal_talk
    deb "Parece muito interessante."
    show debbie f_normal with None
    show jenny f_normal_talk at flip
    show jenny at Position (xpos=150)
    with dissolve
    jen "Não é."
    show jenny f_normal
    show debbie f_normal_talk
    deb "Por que você não vem tomar café da manhã com {b}[firstname]{/b} e comigo."
    deb "Você pode nos contar tudo sobre isso."
    show debbie f_normal
    show jenny f_upset_talk
    jen "Ehh, não obrigada."
    jen "Eu preciso de um banho."
    hide jenny with dissolve
    pause
    show debbie f_sorry_talk
    deb "Tudo bem, querido."
    show debbie f_normal_talk
    deb "Você vai se juntar a mim, não vai {b}[firstname]{/b}."
    show debbie f_normal
    show player 14
    player_name "Sim claro!"
    hide player
    show debbie f_empty a_empty b_robe_hug1
    with dissolve
    deb "Aww, você é um menino tão bom!"
    show debbie b_robe_hug2 with dissolve
    player_name "obrigado {b}[deb_name]{/b}."
    player_name "Você vai em frente, eu estarei lá."
    show debbie b_robe_hug1 with dissolve
    deb "Certo, docinho."
    show player 13
    hide debbie
    with dissolve
    pause
    show player 5f with dissolve
    pause
    player_name "( Transcrevendo, né? )"
    show player 90f
    player_name "( Ela é tão cheia de porcaria... )"
    player_name "( ... E ela está mentindo para {b}[deb_name]{/b} sobre isso. )"
    return

label kitchen_jenny_sluttygram_pics:
    $ player.go_to(L_home_diningroom)
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_dinner_sitting a_dinner_sitting_bowl f_diningroom_table_shy_down zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    pause 
    show jenny f_breakfast_upset_down_talk
    show player f_diningroom_table_surprised_left_food a_dinner_sitting_resting with dissolve
    jen "Oh, que diabos!"
    show jenny f_breakfast_upset_down
    show player f_diningroom_table_surprised_talk_food
    player_name "O que você está fazendo?"
    show player f_diningroom_table_surprised_left_food
    jen "..."
    show jenny f_breakfast_upset_down_talk
    jen "Eu não posso acreditar o quão estúpido essas pessoas são!"
    show jenny f_breakfast_upset_down
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "Ahh, olá?!"
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_angry_talk
    jen "O que?!"
    show jenny f_breakfast_angry
    show player f_diningroom_table_surprised_talk_food
    player_name "Eu perguntei o que você está fazendo?"
    show player f_diningroom_table_surprised_left_food
    show jenny f_breakfast_eyeroll
    jen "Nada."
    show jenny f_breakfast_upset_talk
    jen "Apenas cale a boca e vá embora..."
    jen "... Imbecil"
    show jenny f_breakfast_upset_down
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "Ugh, Está bem"
    hide player
    show player 323c at Position(xpos=610,ypos=770)
    with dissolve
    player_name "Eu não sei porque você tem que ser uma puta, todo o tempo"
    show player 323d
    show jenny f_breakfast_upset_down_talk
    jen "Espere um segundo!"
    show jenny f_breakfast_upset_down
    player_name "..."
    show jenny f_breakfast_upset_down_talk
    jen "O que você sabe sobre mídia social?"
    show jenny f_breakfast_upset_down
    show player 323e
    player_name "Hã?"
    player_name "Por quê?"
    show player 323b
    show jenny f_breakfast_upset_down_talk
    jen "Sentar-se."
    show jenny f_breakfast_upset_down
    show player 323c
    player_name "... Ok."
    hide player
    show player b_dinner_sitting a_dinner_sitting_bowl f_magic_sit_stand_worried zorder 0 at Position(align=(0,0))
    with dissolve
    show jenny f_breakfast_upset_down_talk
    jen "Eu fiz uma conta neste site onde caras perdedores, Pagam meninas Bonitas para postar fotos de si mesmos."
    show jenny f_breakfast_grin_talk a_breakfast_dressed_phoneshow with dissolve
    jen "Tenho certeza que você já ouviu falar disso, você é um perdedor Total..."
    scene expression "backgrounds/location_home_diningroom_sluttygram.jpg" with dissolve
    player_name "{b}Sluttygram{/b}, a sério?!"
    player_name "Este é o seu dinheiro brilhante fazendo ideia?"
    pause
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phoneshow f_breakfast_upset_talk zorder 1
    show player b_dinner_sitting a_dinner_sitting_resting f_magic_sit_stand_worried zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    jen "Sim, então?!"
    show jenny a_breakfast_dressed_phone with dissolve
    jen "Vamos, estou com calor!"
    show jenny f_breakfast_eyeroll
    jen "Bem eu sou mais Sexy que todas essas cadelas!"
    show jenny f_breakfast_upset_talk
    jen "Eu deveria estar no topo desse site!"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Bem, você é muito cheio de si mesmo, não é?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_grin_talk
    jen "Pfft, diz o cara que não para de me perverter!"
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_worried_talk
    player_name "Hmm, justo."
    player_name "Então qual é o problema?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_normal_talk
    jen "O problema é que eu tenho essa conta ativa há algumas semanas e mal consegui seguidores!"
    show jenny f_breakfast_normal
    show player f_magic_sit_stand_worried_talk
    player_name "Bem, essas coisas levam tempo ... Você não consegue apenas um milhão de seguidores da noite para dia."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_normal_talk
    jen "Isso é uma merda!"
    jen "Não tenho tempo para esperar, preciso de dinheiro agora!"
    show jenny f_breakfast_normal
    show player f_magic_sit_stand_worried_talk
    player_name "Eu não sei o que te dizer..."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Quero dizer, olhe para todos os seguidores que esta skank tem!"
    show jenny f_breakfast_upset_down
    pause
    show jenny f_breakfast_upset_down_talk
    jen "E essa e a Primeira!"
    show jenny f_breakfast_upset a_breakfast_dressed_phoneshow with dissolve
    show player f_diningroom_table_surprised_left_low
    pause
    show jenny f_breakfast_upset_down_talk a_breakfast_dressed_phone with dissolve
    show player f_magic_sit_stand_worried
    jen "... E ai meu deus, olhe para aquela!"
    show jenny f_breakfast_upset a_breakfast_dressed_phoneshow with dissolve
    show player f_magic_sit_stand_normal_talk
    player_name "Eu estou olhando."
    show player f_diningroom_table_surprised_left_low
    show jenny f_breakfast_upset_talk
    jen "Ela parece que caiu da árvore feia e bateu em cada galho no caminho..."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_normal_talk
    player_name "Mmm, Eu não sei ... Ela parece muito boa para mim!"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_upset_talk a_breakfast_dressed_phone with dissolve
    jen "A única razão pela qual você está dizendo isso, É porque, os seios dela estão a mostra..."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Não!"
    show player f_magic_sit_stand_normal
    pause
    show player f_magic_sit_stand_normal_talk
    player_name "... Essa não é a única razão."
    player_name "Agora que você mencionou, todas essas garotas estão postando fotos são muito mais provocantes do que a suas.."
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_sad_talk
    jen "Provocante?"
    show jenny f_breakfast_grin
    pause
    show jenny f_breakfast_grin_talk
    jen "Quer dizer sacanagem?"
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_normal_talk
    player_name "Claro."
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_sad
    pause
    show jenny f_breakfast_sad_talk
    jen "Você acha que eu deveria postar algumas fotos mais Sexy?!"
    show jenny f_breakfast_sad
    show player f_magic_sit_stand_worried_talk
    player_name "Não, eu acho que você deveria conseguir um emprego como uma pessoa normal."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_angry
    pause
    show jenny f_breakfast_angry_talk
    jen "De jeito nenhum, esqueça isso!"
    jen "Come with me."
    show jenny b_breakfast_gettingup a_empty f_breakfast_getup_upset with dissolve
    show player f_magic_sit_stand_worried_talk
    player_name "Hã?"
    hide player
    show jenny b_breakfast_pulling f_empty with dissolve
    player_name "Onde estamos"
    hide jenny with dissolve
    jen "Cale a boca e venha."
    scene black with dissolve
    $ player.go_to(L_home_sisbedroom)
    label jenny_taking_pictures_replay:
    if store._in_replay is not None:
        $ player.location = L_home_sisbedroom
    scene expression player.location.background_closeup with None
    show player 12 at left
    show jenny
    with dissolve
    player_name "O que diabos estamos fazendo?!"
    show player 90
    show jenny f_upset_talk a_dressed_camera_give with dissolve
    jen "Nós vamos tirar algumas fotos safadas para meu idiota {b}Sluttygram{/b} ,Para que eu possa obter mais perdedores com tesão para se inscrever no meu feed!"
    show player 728b
    show jenny f_upset a_dressed_hips
    with dissolve
    player_name "Onde você conseguiu uma câmera digital?!"
    show player 728
    show jenny f_upset_talk
    jen "Não é da sua conta, idiota."
    show jenny f_upset
    show player 728b
    player_name "É nisso que você gastou meu dinheiro?!"
    hide jenny with dissolve
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    show jenny b_bed_dressed a_bed_dressed_tie f_bed_normal_low with dissolve
    jen "..."
    show jenny b_bed_tied a_bed_tied_knot with dissolve
    player_name "{b}[jen_name]{/b}, isso é estupido!"
    player_name "Por que você simplesmente não volta para {b}Consum-R{/b} ,E pergunte se você pode ter seu antigo emprego de volta?!"
    show jenny a_bed_tied_down with dissolve
    player_name "Tenho certeza que eles vão"
    pause
    show jenny b_bed_back_tied a_bed_back_down f_bed_lay_back_normal_low with dissolve
    player_name "Eles vão"
    show jenny a_bed_back_pull f_bed_lay_back_normal_talk with dissolve
    jen "Que tal isso?"
    show jenny f_bed_lay_back_normal
    player_name "..."
    player_name "Você sabe, no segundo pensamento."
    player_name "Eu acho que a {b}Sluttygram{/b} ,E uma idéia é maravilhosa e estou totalmente a bordo com este plano agora."
    show jenny f_bed_lay_back_grin_talk
    jen "Ahh, Cale a boca e tire as fotos, perdedor!"
    call screen jenny_photo1

label kitchen_jenny_sluttygram_pics_post_photo1:
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    show jenny b_bed_back_tied a_bed_back_down f_bed_lay_back_normal_talk
    with fade
    jen "Como estou?"
    show jenny f_bed_lay_back_grin_talk
    jen "Está Sexy, certo?"
    show jenny f_bed_lay_back_grin
    player_name "Sim!"
    show jenny f_bed_lay_back_grin_talk
    jen "Você provavelmente deveria tirar uma boa foto da minha bunda também."
    jen "Eu aposto que esses perdedores vão gostar."
    show jenny f_bed_lay_back_grin
    call screen jenny_photo2

label kitchen_jenny_sluttygram_pics_post_photo2:
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    show jenny b_bed_back_tied a_bed_back_down f_bed_lay_back_grin_talk
    with fade
    jen "Tudo bem, hora do grande final."
    jen "Certifique-se de ter um bom tiro."
    show jenny f_bed_lay_back_grin
    player_name "Puta merda Isso é incrível!"
    show jenny f_bed_lay_back_grin_talk
    jen "Sim Sim. Apresse-se."
    call screen jenny_photo3

label kitchen_jenny_sluttygram_pics_post_photo3:
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["02_unlocked"] = True
    $ player.go_to(L_home_sisbedroom)
    scene expression player.location.background_closeup with None
    show jenny b_tied f_normal_talk a_tied_hips
    show player 727 at left
    with dissolve
    jen "Tudo bem, deixa eu ver!"
    show player 13
    show jenny f_normal_low a_tied_camera_look
    with dissolve
    jen "..."
    show jenny f_normal_talk
    jen "Ah sim, se isso não Atrair mais seguidores, nada mais vai."
    show jenny f_grin_talk
    jen "Essas Cadelas estão prestes a aprender que elas não são tão sexy!"
    show jenny f_grin_down
    pause
    show player 14
    player_name "Eu acho que você arruinou sua camisa..."
    show player 13
    show jenny f_normal_talk
    jen "Hã?"
    show jenny f_normal_low
    pause
    show jenny f_grin_talk
    jen "Sim, tanto faz. Eu tenho mais camisas."
    show jenny f_upset_talk
    jen "Por que você ainda esta aqui?!"
    show jenny f_upset
    show player 12
    player_name "O que você quer dizer?"
    show player 5
    show jenny f_upset_talk
    jen "Saia, eu terminei com você."
    show jenny f_upset
    show player 12
    player_name "Que diabos eu só"
    show player 90
    show jenny f_angry_talk
    jen "Adeus, pervertido!"
    show jenny f_angry
    player_name "..."
    show player 24
    player_name "{b}*Suspiro*{/b}"
    hide player with dissolve
    show jenny f_grin_down
    pause
    show jenny f_laugh
    jen "Porra, eu sou tão Gostosa!"
    scene black with dissolve
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 13 with dissolve
    player_name "( Eu não posso acreditar que acabou de acontecer. )"
    player_name "( Ela estava sendo legal por alguns minutos lá. )"
    show player 17
    player_name "( E ela praticamente tirou a roupa para mim! )"
    pause
    show player 5
    player_name "( Pena que ela voltou ao modo de cadela depois que eu tirei as fotos... )"
    show player 13
    player_name "( Ah bem. )"
    pause
    show player 4 with dissolve
    player_name "( Eu me pergunto se eu posso conseguir uma cópia dessas fotos de alguma forma? )"
    hide player with dissolve
    $ game.timer.tick()
    $ M_jenny.trigger(T_jenny_took_pictures)
    $ game.main()

label kitchen_jenny_have_breakfast:
    scene expression player.location.background_closeup with None
    show player 14 at left
    show debbie
    with dissolve
    player_name "Bom dia {b}[deb_name]{/b}."
    hide player
    show debbie b_robe_hug1 a_empty f_empty
    with dissolve
    deb "Bom dia Docinho."
    pause
    show player 14 at left
    hide debbie
    show debbie
    with dissolve
    player_name "Mmm, café da manhã cheira maravilhoso!"
    show player 13
    show debbie f_laugh
    deb "Hehe, está quase pronto."
    show debbie f_normal_talk
    deb "{b}Por que você não vai se sentar à mesa?{/b} eu vou levar para você."
    show debbie f_normal
    show player 14
    player_name "Impressionante, obrigado {b}[deb_name]{/b}!"
    show player 14f with dissolve
    player_name "( {b}[deb_name]{/b} faz o melhor café da manhã! )"
    hide player
    hide debbie
    with dissolve
    $ player.go_to(L_home_diningroom)
    scene expression game.timer.image("dining_room{}") with None
    show jenny b_breakfast_dressed a_breakfast_dressed_spoon f_breakfast_normal_low zorder 1
    show player b_dinner_sitting a_dinner_sitting_resting f_diningroom_table_normal zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    show player f_magic_sit_stand_normal_talk
    player_name "Bom dia."
    show player f_magic_sit_stand_normal
    jen "Mmhmm."
    show player f_magic_sit_stand_tired_talk
    player_name "Por que você está comendo cereal?"
    player_name "Você não viu {b}[deb_name]{/b} cozinhar café da manhã?"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_eyeroll
    jen "Sim, mas recentemente me disseram que preciso crescer e me sustentar, lembra?"
    show jenny f_breakfast_normal_low
    show player f_diningroom_table_surprised_left
    player_name "..."
    show player f_magic_sit_stand_normal_talk
    player_name "Você ainda está se irritando com isso?"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_normal_low_talk
    jen "Eu não estou fazendo beicinho."
    show jenny f_breakfast_normal_low
    show player f_magic_sit_stand_normal_talk
    player_name "Sim você é."
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_normal_low_talk
    jen "AHH, Cale-se."
    show jenny f_breakfast_normal_low
    pause
    pause
    show jenny f_breakfast_normal_talk
    jen "Ei, me empresta sessenta dólares."
    show jenny f_breakfast_normal
    show player f_magic_sit_stand_worried_talk
    player_name "Hã?!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "Eu disse, me empresta sessenta dólares."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Porque você que esse dinheiro?!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_eyeroll
    jen "Ugh, Isso não é da sua conta!"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Umm, é o meu dinheiro ... Então sim, é o meu negócio!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "{b}*Suspiro*{/b} Olha, eu sei como ganhar dinheiro, mas preciso comprar algo primeiro."
    jen "Eu pagarei você de volta."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_normal_talk
    player_name "Okay, certo."
    player_name "Como você vai me pagar de volta?!"
    player_name "Você nem tem emprego."
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_angry_talk
    jen "Não seja um idiota, {b}[firstname]{/b}!"
    show jenny f_breakfast_upset_talk
    jen "eu sei {b}Diane{/b} está pagando demais por qualquer coisa que você esteja fazendo em sua casa."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_normal_talk
    player_name "Estou cuidando do jardim dela."
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_grin_talk
    jen "Ahh, seja qual for."
    jen "Não me importo."
    jen "O ponto é, você pode emprestar sessenta dólares."
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_worried_talk
    player_name "De jeito nenhum!"
    player_name "Eu preciso de cada centavo que posso conseguir."
    player_name "Eu tenho que fazer aulas no próximo ano, lembra?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_angry_talk
    jen "Grr, Está bem!"
    jen "Eu vou lembrar disso!"
    show jenny f_breakfast_angry
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_normal with dissolve
    pause
    show jenny f_breakfast_normal_low
    show player f_diningroom_table_normal_high
    show debbie f_breakfast_standing_normal_talk
    deb "Aqui querido."
    show debbie b_breakfast_potatoes3 f_empty with dissolve
    show player f_diningroom_table_normal_talk
    player_name "Obrigado, {b}[deb_name]{/b}."
    show debbie b_breakfast_potatoes f_breakfast_standing_normal_talk
    show player a_dinner_sitting_bowl f_diningroom_table_shy_down
    with dissolve
    deb "Você quer que eu faça um prato pra você, {b}[jen_name]{/b}?"
    show debbie f_breakfast_standing_normal
    show jenny b_breakfast_gettingup a_empty f_breakfast_getup_upset_talk with dissolve
    jen "Não, eu não."
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating
    hide jenny
    with dissolve
    pause
    show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting with dissolve
    show debbie f_breakfast_standing_sad_talk
    deb "Qual é o problema com ela?"
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_surprised_talk_high_food
    player_name "Ela ainda está chateada com a outra noite."
    show player f_diningroom_table_surprised_high_food
    show debbie f_breakfast_standing_sad_talk
    deb "{b}*Suspiro*{/b} Eu deveria ir e pedir desculpas a ela."
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_surprised_talk_high_food
    player_name "Não você não deveria, {b}[deb_name]{/b}."
    player_name "Ela é a única a ser uma cadela."
    show player f_diningroom_table_surprised_high_food
    show debbie f_breakfast_standing_sad_talk
    deb "{b}[firstname]{/b}!"
    deb "Não fala assim da {b}[jen_name]{/b}!"
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_surprised_talk_high_food
    player_name "Desculpa, {b}[deb_name]{/b}."
    player_name "... Ela é totalmente embora."
    show player f_diningroom_table_surprised_high_food
    show debbie f_breakfast_standing_normal_talk
    deb "Apenas coma seu café da manhã."
    show debbie f_breakfast_standing_normal
    show player f_diningroom_table_normal_talk_high
    player_name "Mais uma vez obrigado por isso, é delicioso!"
    show player f_diningroom_table_normal_high
    show debbie f_breakfast_standing_normal_talk
    deb "Você é bem-vindo, querido."
    scene black with dissolve
    hide player
    hide debbie
    hide expression "characters/jenny/layeredimage/jenny_breakfast_table.png"
    return

label kitchen_diane_3way_aftermath:
    scene expression "backgrounds/location_home_kitchen_day_closeup.jpg"
    show jenny a_dressed_juice f_gross zorder 2 at flip
    show jenny at Position (xpos=200)
    show debbie 11b zorder 1 at right
    with dissolve
    deb "Você deixaria, {b}[jen_name]{/b}!"
    show debbie 10b
    show jenny f_upset_talk
    jen "Não, eu não entendo isso!"
    jen "Você vai mesmo deixar {b}Diane{/b} ficar?!"
    jen "Ela estava fodendo {b}[firstname]{/b}!"
    jen "Bem ali na nossa sala!!"
    show jenny f_gross
    show debbie 11b
    deb "Eu te disse, eu lidei com isso."
    show debbie 10b
    show jenny f_upset_talk
    jen "Você lidou com isso?!"
    jen "O que isso mesmo"
    show jenny f_upset
    show player 14 at left with dissolve
    player_name "Bom dia!"
    show player 13
    show jenny f_gross at unflip
    show jenny at Position (xpos=-200)
    show debbie 2
    deb "Bom dia, querido!"
    show debbie 1
    show player 14
    player_name "Que cheiro gostoso aqui!"
    show player 13
    show debbie 3
    deb "Hehe, Eu estou fazendo o seu favorito!"
    show debbie 1
    show player 14
    player_name "Panquecas de rosto sorridente?!"
    show player 13
    show debbie 2
    deb "E três tiras de bacon!"
    show debbie 1
    show player 17
    player_name "Humm delicioso!!"
    show player 18
    show debbie 3
    deb "Hehe!"
    hide player
    show debbie 4
    show jenny at flip
    show jenny at Position (xpos=0)
    with dissolve
    pause
    show jenny f_eyeroll
    jen "Ugh!"
    show jenny f_upset_talk
    jen "Vocês estão ficando mais e mais estranhos todos os dias!"
    show jenny f_gross
    pause
    show jenny f_upset_talk
    jen "Tanto faz."
    jen "Eu nem me importo mais!"
    hide jenny with dissolve
    jen "Esquisitos!"
    show debbie 1
    show player 5f at left
    with dissolve
    pause
    deb "Não ligue para ela {b}[firstname]{/b}."
    show player 5 with dissolve
    show debbie 2
    deb "Ela está apenas sendo dramática."
    deb "Você sabe como ela é..."
    show debbie 1
    show player 10
    player_name "Sim."
    show player 13
    pause
    show player 14
    player_name "Já {b}Diane{/b} saiu hoje de manhã?"
    show player 13
    deb "Hmm?"
    show debbie 2
    deb "Ahh, sim ... Ela foi embora antes do sol nascer."
    deb "Disse que queria ter uma vantagem no dia."
    deb "Parece que ela vai ter muito trabalho esperando por você."
    show debbie 1
    show player 29 with dissolve
    player_name "Ah, Sim ... Trabalho."
    show player 13 with dissolve
    show debbie 2
    deb "Vamos, é melhor termos alguma comida em você."
    deb "Você vai precisar de muita energia para acompanhar {b}Diane{/b}!"
    show debbie 1
    show player 14
    player_name "Okay, {b}[deb_name]{/b}."
    hide player
    hide debbie
    with dissolve
    return

label kitchen_diane_breeding_candidate:
    scene expression "backgrounds/location_home_kitchen_day_closeup.jpg"
    show player 14 at left
    show jenny a_dressed_juice zorder 2 at flip
    show jenny at Position (xpos=200)
    show debbie 1 zorder 1 at right
    with dissolve
    player_name "Bom Dia."
    show player 13
    show jenny f_eyeroll
    show debbie 2
    deb "Bom dia, querido!"
    show debbie 1
    show jenny f_upset
    show player 10
    player_name "Onde está a {b}Diane{/b}?"
    show player 13 with None
    show jenny at unflip
    show jenny zorder 0 at Position (xpos=-200)
    with dissolve
    deb "Hmm?"
    show debbie 2
    deb "Ah, ela saiu cedo esta manhã, toda animada com alguma coisa."
    show debbie 1
    show player 14
    player_name "Animada?"
    show player 13
    show debbie 2
    deb "Sim, ela estava ainda mais animada do que a manhã em que seu celeiro terminou."
    show debbie 1
    show player 14
    player_name "Mesmo?"
    show player 13
    show jenny f_upset_talk
    jen "Ela é tão estranha..."
    show jenny f_upset
    show debbie 13
    deb "Silêncio."
    show debbie 14
    show jenny f_eyeroll
    jen "Bem ela é!"
    show jenny f_upset
    show debbie 13
    deb "{b}[jen_name]{/b}!"
    show debbie 14b
    pause
    show debbie 2
    deb "{B}Diane{/b} disse a você o que está acontecendo?"
    show debbie 1
    show player 29 with dissolve
    player_name "Humm..."
    player_name "Não."
    show player 14 with dissolve
    player_name "Eu provavelmente deveria ir até lá e ver o que ela está aprontando..."
    show player 13
    show debbie 2
    deb "Bem, espere agora."
    deb "Você precisa do seu café da manhã!"
    show debbie 1
    show player 14
    player_name "Não, tudo bem."
    player_name "Eu não estou com muita fome."
    show player 13
    show debbie 2
    deb "Não é bom ficar sem o café da manhã, {b}[firstname]{/b}."
    show debbie 1
    show player 14
    player_name "Mesmo {b}[deb_name]{/b}, Estou bem."
    player_name "Obrigado!"
    show player 13
    deb "..."
    show debbie 2
    deb "Okay."
    show debbie 1
    show player 14
    player_name "Eu vou te ver mais tarde esta noite."
    show player 13
    show debbie 2
    deb "Tenha cuidado, docinho."
    show debbie 1
    hide player with dissolve
    pause
    show jenny f_gross
    jen "..."
    show jenny f_upset_talk
    jen "Algo estranho está acontecendo com esses dois."
    show jenny f_upset
    show debbie 2
    deb "O que você quer dizer?"
    show debbie 1 with None
    show jenny at flip
    show jenny at Position (xpos=0)
    with dissolve
    jen "..."
    show debbie 2
    deb "Eles estão apenas animados com o novo negócio."
    show debbie 1
    show jenny f_upset_talk
    jen "Ok, certo."
    show jenny f_upset
    show debbie 14
    deb "Hmm?"
    show jenny f_upset_talk
    jen "Ugh, nada. deixa pra lá."
    jen "Eu estarei no meu quarto."
    hide jenny with dissolve
    show debbie 13
    deb "Certo querida."
    hide debbie with dissolve
    return

label kitchen_diane_barn_news:
    scene expression "backgrounds/location_home_kitchen_day_closeup.jpg"
    show jenny a_dressed_juice f_gross
    show diane nightgown_dip
    with dissolve
    deb "Hahaha!"
    show jenny f_normal_talk
    jen "Vocês são tão esquisitos ... eu vou sair daqui."
    show jenny f_normal zorder 1 at Position (xpos=100)
    show diane b_nightgown a_nightgown_sides f_smirk_talk at Position (xpos=400)
    show debbie 1 zorder 2 at right
    with dissolve
    dia "Ah, qual é o problema princesa?"
    show jenny at flip
    show jenny at Position (xpos=600)
    with dissolve
    dia "Você está com ciúmes?"
    show diane f_smirk
    show jenny f_eyeroll
    jen "Psh."
    show jenny f_normal at unflip
    show jenny at Position (xpos=100)
    with dissolve
    show diane f_smirk_talk
    dia "Não fique mal-humorada, vou levá-lo para dar uma volta também."
    show diane f_smirk a_nightgown_slap
    show jenny f_surprised_back
    jen "!!!" with hpunch
    show diane f_laugh a_nightgown_sides
    show jenny f_upset_talk at flip
    show jenny at Position (xpos=640)
    with dissolve
    jen "De jeito nenhum!"
    show jenny f_upset
    dia "Hahaha, olhe para essa bochechas rosadass!"
    show debbie 3
    deb "Haha!"
    show jenny f_eyeroll
    jen "Ugh, shuddup!"
    show jenny f_upset
    show player 14 at left with dissolve
    player_name "O que está acontecendo?"
    show player 13
    show debbie 1
    show diane f_normal_talk
    dia "{b}[firstname]{/b}!!!"
    show diane f_normal
    show debbie 2
    deb "Bom dia querido."
    show debbie 1
    show diane f_laugh
    dia "Está feito, está feito, é Feitooooo!!!"
    show diane f_cheese
    show player 13
    player_name "Hmm?"
    show player 17
    player_name "Espere, você quer dizer que o celeiro está pronto?!"
    show player 13
    show diane f_normal_talk
    dia "Bingo!"
    dia "{b}Richard{/b} apenas liguei para avisar que tudo está pronto."
    show diane f_normal
    show jenny f_eyeroll
    jen "Eu não entendi."
    show jenny f_normal_talk
    jen "Eu prefiro ter uma casa, Do que um estúpido celeiro."
    show jenny f_normal
    show diane f_smirk_talk
    dia "Sim, bem, eu prefiro ter uma colega de quarto divertido, do que um pisco azedo."
    show diane f_smirk
    show debbie 13
    deb "{b}*Suspiro*{/b} Vocês dois..."
    show debbie 14
    show player 14
    player_name "Estou animado!"
    show player 13
    show diane f_normal_talk
    dia "See!!"
    dia "{b}[firstname]{/b} sabe como reagir a boas notícias!"
    hide player
    show diane nightgown_hug2
    show jenny f_gross at unflip
    show jenny at Position (xpos=350)
    with dissolve
    dia "Obrigada, {b}[firstname]{/b}!"
    show diane nightgown_hug3
    player_name "Sim."
    show diane nightgown_hug4
    show jenny f_upset_talk
    jen "Ugh, tanto faz."
    jen "Eu estarei no meu quarto."
    hide jenny with dissolve
    pause
    show diane b_nightgown a_nightgown_sides at Position (xpos=250)
    show player 14 at left
    with dissolve
    player_name "Então, estamos indo para lá?"
    show player 13
    show diane f_normal_talk
    dia "Pode apostar que vamos!"
    show diane f_normal
    show debbie 2
    deb "Ah ah ah!"
    show diane at flip
    show diane at Position (xpos=750)
    with dissolve
    deb "Depois do café da manhã!"
    show debbie 1
    show diane f_laugh
    dia "Ahh mas maaamaaaãe!"
    show diane f_normal
    show debbie 2
    deb "{b}Diane{/b}, é a refeição mais importante do dia."
    show debbie 1
    show diane f_normal_talk
    dia "Eu tenho esperado quase trinta anos por isso, eu vou!"
    dia "Nós vamos ter que comer um jantar extra esta noite!"
    show diane at unflip
    show diane f_smirk_talk at Position (xpos=250)
    with dissolve
    dia "Certo, {b}[firstname]{/b}?!"
    show diane f_smirk
    show player 29 with dissolve
    player_name "Eu Hamm..."
    show player 3
    show debbie 3
    deb "Hahaha, bem tudo bem."
    show debbie 2
    show diane at flip
    show diane at Position (xpos=750)
    with dissolve
    deb "Vá se divertir."
    show player 13
    hide debbie
    show diane f_normal_talk b_nightgown_hug1 a_empty at flip
    show diane at Position (xpos=904)
    with dissolve
    dia "Obrigada!"
    show debbie 1 at right
    show diane b_nightgown a_nightgown_sides f_normal_talk at unflip
    show diane at Position (xpos=250)
    with dissolve
    dia "Vamos lá, {b}[firstname]{/b}!"
    dia "{b}Vamos dar uma olhada no novo celeiro!{/b}"
    hide diane with dissolve
    show debbie 2
    deb "Apenas certifique-se de se vestir primeiro!"
    show debbie 1
    show player 14
    player_name "Hehe, Eu nunca a vi tão animada..."
    show player 13
    show debbie 2
    deb "Sim, é melhor você ir com ela."
    hide player
    show debbie 4
    with dissolve
    pause
    show debbie 5
    player_name "Tudo bem, eu vou te ver hoje à noite {b}[deb_name]{/b}."
    show debbie 2 with dissolve
    deb "Certo!"
    hide debbie with dissolve
    return

label kitchen_diane_dinner:
    scene location_home_kitchen_day_blur
    show player 14 at left
    show debbie 1 at right
    with dissolve
    player_name "Oi, {b}[deb_name]{/b}. Eu tenho o {b}peixe{/b} que você queria."
    show player 13
    show debbie 2
    deb "Obrigada Docinho! Agora eu posso terminar o jantar."
    deb "Eu vou deixar você saber quando terminar, ok?"
    show player 203

    scene black

    scene expression L_home_entrance.background
    show diane b_classy a_classy_sides f_normal_talk at Position (xpos=600)
    show debbie 91f
    with dissolve
    dia "Mmm, é {b}truta do mar{/b} está cheirando?!"
    dia "Você fez?!"
    show diane f_normal
    show debbie 93f
    deb "Claro que sim!"
    deb "Eu sei como tratar minha garota certo!"
    show diane f_laugh
    show debbie 91f
    dia "Oh meu Deus, eu poderia te beijar agora mesmo!"
    show player 203 at left with dissolve
    show diane f_normal_talk
    dia "Aí está ele..."
    dia "... O {b}homem da casa{/b}!"
    show diane f_normal
    show player 14
    player_name "Oi, {b}Diane{/b}."
    show player 17
    player_name "Esse vestido fica ótimo em você!"
    show diane f_laugh
    show player 203
    dia "Pare com isto!"
    show player 13
    show diane f_normal
    show debbie 93f
    deb "Ele é bem o pequeno encantador, não é?"
    show diane f_normal_talk
    show debbie 91f
    dia "Eu não sei como você consegue manter suas mãos longe dele!"
    dia "Onde está sua outra inquilina? Ela vai se juntar a nós esta noite, Ou ela teve uma reunião com as Cadelas de summerville para participar?"
    show player 10
    show diane f_normal
    player_name "Não, ela vai comer com a gente."
    show player 12
    player_name "... Ela só está lá em cima se preparando."
    show player 203
    show diane f_laugh
    dia "Princesa Típica..."
    show diane f_normal_talk
    dia "Bem, eu não estou esperando por ela! principalmente porque {b}[deb_name]{/b} fez {b}Truta do mar{/b} no menu!"
    show debbie 92f
    show diane f_normal
    deb "Ei, seja legal!"
    show debbie 93f
    deb "Ela não é tão ruim quanto você pensa..."
    show debbie 91f
    show diane f_laugh
    dia "Ahh, se você diz."
    show debbie 93f
    show diane f_normal
    deb "Agora vocês dois se sentam enquanto eu pego uma garrafa de vinho!"
    show debbie 92f
    deb "Eu tenho uma nova marca Eu quero que vocês aprecie."
    hide debbie
    hide diane
    with dissolve
    show player 14
    player_name "Eu deveria me juntar a elas na {b}Sala de jantar{/b}."
    player_name "{b}[deb_name]{/b} a comida cheira delicioso!"
    hide player
    with dissolve

    $ player.go_to(L_home_diningroom)
    scene location_home_dining
    show player b_dinner_sitting a_dinner_sitting_resting f_diningroom_table_normal zorder 0 at Position(align=(0,0))
    show diane b_dinner a_dinner_normal f_dinner_normal
    show jenny b_dinner_casual_side f_empty a_dinner_casual_side1 at Position (align=(0,0))
    show jenny at Position (xpos=300)
    show debbie 65 at Position(xpos=887)
    show table 1 zorder 2 at Position(xpos=0.4976,ypos=0.7630)
    with fade
    deb "... A escola realmente mudou tanto assim?!"
    deb "É uma coisa boa que você tem {b}[firstname]{/b} para te ajudar, hã?"
    show jenny a_dinner_casual_side2 with dissolve
    deb "Parece que ele está sempre lá hoje em dia."
    show debbie 64
    show jenny b_dinner_casual f_breakfast_surprised a_breakfast_dressed_spoon with dissolve
    show player f_magic_sit_stand_laugh
    show diane f_dinner_normal_talk
    dia "Bem, há tanto trabalho que precisa ser feito entre o jardim e o negócio de leite."
    dia "... E ele realmente mostrou uma aptidão para isso também!"
    show diane f_dinner_normal
    show player f_diningroom_table_normal
    show debbie 65
    deb "Verdade?"
    show jenny f_breakfast_gross
    show debbie 64
    show diane f_dinner_normal_talk a_dinner_hand with dissolve
    show player f_magic_sit_stand_normal
    dia "Ah sim."
    dia "Você deveria estar realmente orgulhosa dele, {b}[deb_name]{/b}!"
    dia "Ele é um jovem tão responsável."
    show jenny b_dinner_casual_side f_empty a_dinner_casual_side1 with dissolve
    show player f_diningroom_table_surprised_left a_dinner_sitting_touch1
    show diane f_dinner_normal a_dinner_hand2 b_dinner_open
    with dissolve
    player_name "( !!! )"
    show jenny a_dinner_casual_side2 with dissolve
    show diane f_dinner_normal_talk
    dia "... E muito esperto..."
    dia "... E forte..."
    show player f_diningroom_table_surprised_teeth_left a_dinner_sitting_touch2
    show diane a_dinner_hand3
    with dissolve
    dia "... E gentil."
    show jenny a_dinner_casual_side1 with dissolve
    show diane f_dinner_normal
    player_name "{b}*Gole*{/b}"
    show debbie 65
    deb "Ah, claro que tenho orgulho dele!"
    if M_mom.finished_state(S_mom_diane_visit) or store._in_replay is not None:
        show debbie 67 with dissolve
        deb "Ele tem me ajudado muito também."
        show debbie 68 with dissolve
        player_name "( !!! )"
        show debbie 69 with dissolve
        pause
        show debbie 71 with dissolve
        deb "Ajudando com as tarefas..."
        deb "... Fazendo manutenção em casa..."
        show debbie 69 with dissolve
        pause
        show debbie 71 with dissolve
        deb "... Ele está cuidando tão bem da {b}[jen_name]{/b} e de mim."
        show debbie 69 with dissolve
        player_name "Hehehe, eu"
        show debbie 68 with dissolve
        player_name "... Quer dizer, é"
    show player od_dinner_sitting_boner
    show jenny f_breakfast_gross_talk b_dinner_casual a_breakfast_dressed_spoon
    show debbie 64
    with dissolve
    jen "Ugh, toda essa merda dovey lovey vai me fazer vomitar..."
    show diane f_dinner_annoyed_left_talk
    dia "Nós não precisamos de comentários da galeria de amendoim, {b}[jen_name]{/b}..."
    dia "Apenas coma seu jantar e fique quieta."
    show diane f_dinner_normal
    show jenny f_breakfast_eyeroll
    jen "Psh, seja qual for..."
    show jenny f_breakfast_gross
    pause
    show jenny f_breakfast_gross_talk
    jen "Vocês estão agindo de forma estranha."
    show jenny f_breakfast_gross
    pause
    jen "Hmm..."
    show jenny f_breakfast_grin_down_talk a_dinner_casual_drop with dissolve
    jen "... Oops."
    show jenny b_dinner_casual_bending f_empty a_empty at Position (xpos=200)
    show diane f_dinner_annoyed_left
    with dissolve
    pause
    show expression "backgrounds/location_home_dining_under.jpg"
    hide table
    hide diane
    show diane dinner_under_hand
    jen "( !!! )" with hpunch
    pause
    scene location_home_dining
    show player b_dinner_sitting a_dinner_sitting_touch2 f_diningroom_table_surprised_teeth_left od_dinner_sitting_boner zorder 0 at Position(align=(0,0))
    show diane b_dinner_open a_dinner_hand3 f_dinner_annoyed_left
    show debbie 64 at Position(xpos=880)
    show table 1 zorder 2 at Position(xpos=0.4976,ypos=0.7630)
    if M_jenny.finished_state(S_jenny_catch_her_jilling) or store._in_replay is not None:
        show jenny f_breakfast_gross b_dinner_casual a_breakfast_dressed_spoon at Position (xpos=300)
        with dissolve
        jen "( ... )"
    else:
        show jenny b_dinner_casual f_breakfast_surprised a_breakfast_dressed_spoon at Position (xpos=300)
        with dissolve
        jen "( Que porra... )"
    show debbie 65
    show diane f_dinner_normal
    deb "Então você teve alguma sorte em encontrar um novo local de trabalho?"
    show debbie 64
    show jenny b_dinner_casual_bending f_empty a_empty at Position (xpos=200) with dissolve
    dia "Hmm?"
    show player f_magic_sit_stand_normal
    show diane f_dinner_normal_talk a_dinner_touch1
    with dissolve
    dia "Não, infelizmente não há nada disponível perto da cidade."
    show diane f_dinner_normal a_dinner_touch
    show debbie 64d
    show player f_diningroom_table_normal
    deb "Por favor, me diga que você não vai realmente se afastar de nós..."
    show jenny f_breakfast_gross b_dinner_casual a_breakfast_dressed_spoon at Position (xpos=300)
    show debbie 64c
    show diane f_dinner_normal_talk a_dinner_touch1
    show player f_magic_sit_stand_normal
    with dissolve
    dia "Bem, não se eu puder ajudar!"
    show jenny f_breakfast_surprised
    dia "{b}[firstname]{/b} na verdade, veio com uma boa ideia no outro dia..."
    show diane f_dinner_normal
    show debbie 65
    show jenny f_breakfast_normal_closed a_dinner_casual_facepalm with dissolve
    deb "Ah sim"
    show debbie 64
    show diane f_dinner_normal_talk
    dia "Por que comprar um celeiro fora da cidade que nem se encaixa no meu modelo de negócios?"
    dia "Não seria muito melhor construir um personalizado na terra que eu já possuo?"
    show diane f_dinner_normal
    show debbie 64b
    show player f_diningroom_table_normal
    deb "Hmm?"
    show debbie 65
    deb "Você não tem terra suficiente para construir um celeiro, {b}Diane{/b}..."
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Bem, não, ainda não..."
    dia "... Mas uma vez que eu demoli a casa, eu acho"
    show diane f_dinner_normal
    show debbie 67 with dissolve
    show player f_diningroom_table_normal
    deb "Você vai demolir sua casa?!"
    show debbie 64c with dissolve
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Claro, por que não?"
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "Não sei."
    deb "É uma casa tão legal..."
    show debbie 64
    show diane f_dinner_laugh
    show player f_magic_sit_stand_normal
    dia "Ahh, não é tão legal assim!"
    show diane f_dinner_normal_talk
    dia "É muito grande para mim e, além disso, tudo o que faz é me lembrar daquele ex-marido idiota..."
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "Ok, mas onde você vai morar?"
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Eu não tenho certeza sobre essa parte ainda..."
    dia "Quer dizer, tenho certeza de que posso encontrar algo, mas não tenho tempo de pensar sobre isso."
    dia "Se eu vou fazer isso, vou ter que começar a construir imediatamente!"
    dia "Caso contrário, arrisco a perder minha base de clientes..."
    show diane f_dinner_normal
    deb "..."
    show debbie 65
    show player f_diningroom_table_normal
    deb "Você conhece alguém capaz de construir algo assim?"
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Claro!"
    dia "Uma das minhas melhores clientes é casada com um carpinteiro."
    show diane f_dinner_normal
    show player f_magic_sit_stand_normal_talk
    player_name "Hmm?"
    player_name "Ah, Você quer dizer pai da {b}Annie{/b}?"
    show player f_magic_sit_stand_normal
    show diane f_dinner_normal_talk
    dia "Sim, o nome dele é {b}Richard{/b}, certo?"
    show diane f_dinner_normal
    show player f_magic_sit_stand_normal_talk
    player_name "Sim."
    player_name "Ele não parece ser um cara muito legal..."
    show player f_magic_sit_stand_normal
    show diane f_dinner_normal_talk a_dinner_touch
    dia "Bem, tudo bem."
    dia "Eu não preciso que ele seja legal!"
    dia "Eu só preciso que ele seja competente..."
    dia "... E barato!"
    show diane f_dinner_laugh a_dinner_touch1
    show debbie 66
    dia "Haha!"
    deb "Haha!"
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "Bem, você sempre pode ficar aqui conosco enquanto procura um novo lugar, sabe?"
    show debbie 64
    show jenny f_breakfast_surprised with dissolve
    jen "( !!! )"
    show jenny f_breakfast_gross_talk
    show player f_diningroom_table_surprised_left
    show diane a_dinner_normal with dissolve
    jen "O que como?!"
    show jenny f_breakfast_gross
    show diane f_dinner_normal_talk
    dia "Eu não quero ser um incômodo..."
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "Não é incômodo!"
    deb "Você é praticamente da família e mais do que bem-vinda para ficar o tempo que precisar!"
    show debbie 64
    show jenny f_breakfast_gross_talk
    show player f_diningroom_table_surprised_left
    jen "{b}[deb_name]{/b}, Eu realmente não acho que seja uma boa ideia"
    show jenny f_breakfast_gross
    show diane f_dinner_annoyed_left_talk
    dia "Shh, ninguém está falando com você..."
    show diane f_dinner_normal
    show jenny f_breakfast_gross
    show debbie 65
    show player f_diningroom_table_normal
    deb "Eu acho uma ótima ideia!"
    deb "Vai dar a vocês garotos a chance de se relacionar com {b}Diane{/b}."
    deb "Além disso, podemos realmente usar a ajuda extra por aqui, mesmo que seja apenas temporário..."
    show debbie 64
    show jenny f_breakfast_gross_talk
    show player f_diningroom_table_surprised_left
    jen "Onde ela vai dormir?!"
    show jenny f_breakfast_gross
    show debbie 65
    show player f_diningroom_table_normal
    deb "Nós vamos descobrir algo."
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "O sofá me serviria bem."
    show diane f_dinner_normal
    show jenny f_breakfast_eyeroll
    show player f_diningroom_table_surprised_left
    jen "Ugh, esta é uma ideia idiota!"
    show jenny f_breakfast_gross
    show diane f_dinner_annoyed_left_talk
    dia "Ei, estou falando com {b}[deb_name]{/b} Curtiu isso!"
    show diane f_dinner_annoyed_left zorder 1
    show jenny f_breakfast_gross
    jen "..."
    show jenny f_breakfast_gross_talk
    jen "Tanto faz."
    jen "Eu vou para meu quarto."
    show jenny b_dinner_walking f_empty a_empty zorder 0 at Position (xpos=500) with dissolve
    pause
    hide jenny with dissolve
    pause
    show player f_magic_sit_stand_normal
    show diane f_dinner_normal_talk
    dia "Sheesh, essa menina precisa aprender alguma lição de respeito..."
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "Oh, {b}Diane{/b}... Deixe ela."
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Estou falando sério!"
    dia "Meus pais nunca me permitiria falar assim."
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "É só uma fase."
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Se você diz..."
    show diane f_dinner_normal
    show player f_diningroom_table_normal_talk
    player_name "É verdade {b}Diane{/b} realmente vai morar com a gente?"
    show player f_diningroom_table_normal
    show debbie 65
    deb "Certo!"
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Apenas me dê alguns dias para resolver os planos de construção"
    show diane f_dinner_normal
    show debbie 66
    show player f_diningroom_table_normal
    deb "Isso é tão excitante!"
    show debbie 65
    show player f_magic_sit_stand_normal
    deb "Será como aquelas festas do pijama que costumávamos ter quando éramos meninas!"
    show diane f_dinner_laugh
    show debbie 66
    dia "Hahaha!"
    deb "Hahaha!"
    scene black with fade
    hide diane
    hide player
    hide table
    hide debbie
    scene location_home_entrance_night_blur
    show diane b_classy a_classy_sides f_normal_talk
    show debbie 91f
    show player 203 at left
    with dissolve
    dia "Bem, acho que vou para casa e começo a arrumar as malas!"
    show diane f_normal
    show debbie 92f
    deb "Eu mal posso esperar!"
    show debbie 91f
    show diane f_laugh
    dia "Hehe, nem eu!"
    hide debbie
    show diane dinner_hug4
    with dissolve
    dia "Eu vou te ver muito em breve."
    show diane dinner_hug3
    deb "Tenha cuidado ao ir para casa!"
    show debbie 91f
    show diane b_classy a_classy_sides f_normal_talk
    with dissolve
    dia "Eu sempre tenho."
    show debbie 91 at Position (xoffset=100)
    hide player
    show diane dinner_hug2
    with dissolve
    dia "Venha logo, {b}[firstname]{/b}."
    dia "Eu definitivamente vou precisar de sua ajuda com tudo isso."
    show diane dinner_hug1
    player_name "Sim, Senhora."
    show debbie 91f
    show player 13 at left
    show diane b_classy a_classy_sides f_shamed_talk_smile
    with dissolve
    dia "E diga a princesa que eu disse tchau."
    show diane f_normal
    show debbie 93f
    deb "Hehe, eu vou."
    hide debbie
    hide diane
    hide player
    with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["03_unlocked"] = True
    $ renpy.end_replay()
    return

label kitchen_diane_debbie_dinner_outfit:
    pause
    deb "Ah!"
    deb "{b}[firstname]{/b}, antes de ir, você tem um segundo?"
    show player 14
    show debbie 61
    player_name "Claro, {b}[deb_name]{/b}. O que você precisa?"
    show player 1
    show debbie 62
    deb "Eu tenho uma roupa nova para o jantar hoje à noite e queria ter sua opinião."
    deb "Deixe-me ir colocá-lo será bem rápido."
    hide debbie with dissolve
    scene home_livingroom_b
    show player 14
    player_name "Estou animado para ver {b}[deb_name]{/b} toda bem vestida!"
    show player 11
    deb "Querido!"
    deb "Estou pronta!"
    show player 2
    player_name "Chegando!"
    hide player with dissolve
    return

label kitchen_diane_meet_debbie_kitchen:
    scene location_home_kitchen_day_blur
    show debbie 2 at right with dissolve
    show player 203 at left with dissolve
    deb "Aí está você!"
    show debbie 3
    deb "Eu preciso da sua ajuda com algo..."
    show debbie 2
    show player 11
    deb "{b}Diane{/b} está vindo para o jantar hoje à noite."
    deb "... E eu preciso de você para pegar uma {b}Truta do mar{/b} no {b}Pier{/b}."
    deb "Eu quero cozinhar para ela algo especial e {b}Truta do mar{/b} é seu favorito absoluto!"
    show debbie 1
    show player 2
    player_name "Essa é uma boa surpresa!"
    player_name "Vai ser bom para ela sair de sua casa por algum tempo."
    player_name "Eu me preocupo com ela às vezes ... Sozinha lá."
    player_name "Eu deveria ir para o {b}Pier{/b} e pegar alguma {b}Truta do mar{/b} no meu caminho para casa."
    scene homekitchen
    show player 1 at left
    show debbie 62 at right
    with dissolve
    deb "Obrigada Docinho."
    return

label kitchen_sis_telescope_1:
    scene homekitchen
    show player 1 at left
    show debbie 2 at right
    with dissolve
    deb "Oi Docinho"
    deb "Com fome, Tem café da manhã?"
    show debbie 51 at Position(xpos=1025)
    show player 10
    player_name "Não sei se tenho tempo, {b}[deb_name]{/b}."
    if game.timer.is_weekend():
        player_name "Eu tenho que me encontrar com {b}Erik{/b} em sua casa..."
    else:
        player_name "Estou atrasado para a escola."
    show player 11
    show debbie 52
    deb "Querido, você tem que comer!"
    show player 11
    if game.timer.is_weekend():
        deb "Eu não me importo se seu amigo {b}Erik{/b} esperar o dia todo..."
    else:
        deb "Eu não me importo se sua escola, Me ligar para reclamar sobre você estar atrasado..."
    show player 1
    deb "Você não pode simplesmente sair com o estômago vazio!"
    show player 14
    show debbie 51
    player_name "Eu acho que poderia demorar alguns minutos para comer alguma coisa..."
    show player 1
    show debbie 2
    deb "Eu preparei alguns cereais para você na {b}sala de jantar{/b}."
    hide player
    hide debbie
    with dissolve
    return

label kitchen_mom_start:
    scene expression game.timer.image("homekitchen{}")
    show player 1 at left with dissolve
    show debbie 2 at right with dissolve
    deb "Bom dia, querido! Eu te fiz um café da manhã!"
    deb "Eu pensei que você gostaria de algo especial para o seu primeiro dia de volta à escola."
    show player 2
    show debbie 1
    player_name "Obrigado, {b}[deb_name]{/b} mas eu não estou com muita fome e estou atrasado para a escola...."
    show player 1
    show debbie 2
    deb "Você tem certeza? Eu fiz o seu favorito..."
    deb "Panquecas de cara feliz com três tiras de baaaacon!"
    show debbie 1
    show player 10
    player_name "O cara..."
    show player 11
    player_name "..."
    show player 10
    player_name "Não, eu realmente não deveria..."
    player_name "eu acho que {b}Erik{/b} dormiu novamente e eu não quero me atrasar no meu primeiro dia de volta."
    show player 11
    show debbie 3
    deb "Hah, novamente?"
    show player 1
    show debbie 2
    deb "Bem, eu acho que é melhor você ir então."
    show player 2
    show debbie 1
    player_name "Sim, obrigado de qualquer maneira, {b}[deb_name]{/b}!"
    show player 1f with dissolve
    show debbie 2
    deb "Sem problemas, docinho oh! Espere!"
    show player 1 with dissolve
    player_name "Hmm?"
    show debbie 3
    deb "eu quase esqueci!"
    show debbie 2
    deb "Falei com minha amiga {b}Diane{/b} ,Ontem ela mencionou que precisa de {b}ajuda com o jardim dela{/b} durante o verão!"
    show player 10
    show debbie 1
    player_name "Hmm, Eu não sei muito sobre jardinagem {b}[deb_name]{/b}..."
    show player 11
    show debbie 3
    deb "O vamos lá é fácil! {b}Diane{/b} ,pode te ensinar e se você fizer um bom trabalho ela também vai te pagar!"
    show debbie 2
    deb "Pode ser uma boa maneira de ganhar dinheiro para a faculdade, você não acha?"
    show player 10
    show debbie 1
    player_name "Sim, eu acho que você está certa."
    show player 2
    player_name "Eu deveria ir visitá-la, ver o que ela quer que eu faça."
    show debbie 2
    deb " Bom Menino!"
    hide player
    show debbie 4b
    with dissolve
    deb "Eu sei que estas últimas semanas foram difíceis..."
    deb "Mas o seu {b}Pai{/b} gostaria que você continuasse, sabe?"
    deb "Você vai passar por isso. Eu prometo que as coisas vão melhorar."
    show debbie 5b
    player_name "Sim, eu sei. obrigado {b}[deb_name]{/b}..."
    deb "Queixo Erguido querido! Estou aqui por você."
    hide debbie with dissolve
    return

label kitchen_mom_dinner:
    scene location_home_kitchen_day_blur
    show debbie 2 at right with dissolve
    show player 203 at left with dissolve
    deb "Aí está você!"
    show debbie 3
    deb "Eu preciso da sua ajuda com algo..."
    show debbie 2
    show player 11
    deb "Minha amiga {b}Diane{/b} Virá para o jantar hoje à noite."
    deb "... E eu preciso de você para pegar uma {b}Truta do mar{/b} no {b}Pier{/b}."
    deb "Eu quero cozinhar algo especial Para ela, É o favorito dela!"
    show debbie 1
    show player 2
    player_name "{b}Diane{/b} Essa é uma boa surpresa!"
    player_name "Vai ser bom para ela sair de casa por algum tempo..."
    player_name "Eu me preocupo com ela às vezes ...sozinha lá."
    player_name "Eu deveria ir para o {b}Pier{/b} e pegar uma {b}Truta do mar{/b} no caminho de casa."
    scene homekitchen
    show player 1 at left
    show debbie 62 at right
    with dissolve
    deb "{b}[firstname]{/b}, antes de ir, você tem um segundo?"
    show player 14
    show debbie 61
    player_name "Claro, {b}[deb_name]{/b}. Do que você precisa?"
    show player 1
    show debbie 62
    deb "Eu tenho uma roupa nova para o jantar hoje à noite e queria ter sua opinião."
    deb "Deixe-me ir colocá-lo Será bem rápido."
    hide debbie with dissolve
    scene home_livingroom_b
    show player 14
    player_name "Estou animado para ver {b}[deb_name]{/b} bem vestida!"
    show player 11
    deb "Querido!"
    deb "Estou pronta!"
    show player 2
    player_name "Chegando!"
    hide player with dissolve
    return

label kitchen_mom_debt_call:
    scene expression game.timer.image("homekitchen{}")
    show debbie 6 at right with dissolve
    deb "Eu já te disse! Eu não {b}SEI{/b} onde o dinheiro está..."
    deb "Eu não tinha ideia de que ele estava envolvido nisso!"
    show debbie 7 at right
    deb "Mas"
    show debbie 6 at right
    deb "Eu não tenho isso!!"
    show debbie 7 at right
    deb "..."
    show debbie 6 at right
    deb "Isso foi uma {b}ameaça{/b}?!"
    deb "Eu estou desligando agora. Não ligue de volta aqui novamente."
    show debbie 8 at right with hpunch
    deb "Apenas nos deixe {b}EM PAZ!!!{/b}"
    show debbie 9 at right
    show player 10 at left with dissolve
    player_name "..."
    player_name "...{b}[deb_name]{/b}?"
    player_name "...Você está bem?"
    show player 5 at left
    show debbie 11 at right
    deb "Eu estou bem querido."
    show debbie 10 at right
    show player 10 at left
    player_name "Você tem certeza, Não parece bem?..."
    show player 5 at left
    show debbie 11 at right
    deb "Não é nada para você se preocupar..."
    show debbie 10 at right
    show player 5 at left
    player_name "..."
    show player 10 at left
    player_name "Eu poderia tentar encontrar outro emprego. Talvez eu possa arrumar algum dinheiro para você."
    show player 5 at left
    show debbie 11 at right
    deb "Não."
    deb "Seu {b}Pai{/b} não iria querer isso, querido."
    deb "Você precisa manter seu foco na escola e {b}Economizar seu dinheiro para mensalidade{/b}."
    show debbie 10 at right
    show player 10 at left
    player_name "Sim mas {b}[deb_name]{/b}, eu posso ajudar..."
    hide player 10 at left
    show debbie 12 at right
    with dissolve
    deb "Ah Querido..."
    deb "Apenas deixe-me cuidar disso e tudo ficará bem, ok? eu prometo."
    hide debbie with dissolve
    return

label kitchen_mom_diane_visit:
    scene homekitchen_secret
    show diane b_kitchen a_empty f_normal_talk
    show debbie 59f at Position(xpos=0.3318,ypos=1.000)
    dia "... Eu não vejo o problema. Não é bom que ele esteja te ajudando em casa?"
    show diane f_normal
    show debbie 60f
    deb "Eu sei, é só..."
    deb "Ele tem sido tão ... carinhoso comigo ultimamente..."
    show diane f_laugh
    show debbie 59f
    dia "Isso não é surpreendente, ele acabou de perder a única família que ele já teve..."
    show diane f_normal_talk
    dia "Ele provavelmente só precisa de alguém com quem possa se sentir próximo..."
    dia "Especialmente com todas essas outras coisas que estão acontecendo com vocês."
    show diane f_normal
    show debbie 17f at Position(xpos=0.3318,ypos=1.1130)
    deb "Não é isso. Tem mais! É o jeito que ele olha para mim, você entende?"
    show debbie 59f at Position(xpos=0.3318,ypos=1.000)
    show diane f_surprised
    dia "..."
    show diane f_normal_talk
    dia "O que você quer dizer?"
    show diane f_normal
    show debbie 60f
    deb "Bem, há pouco tempo atrás eu comecei a notar coisas..."
    show diane f_normal_talk
    show debbie 59f
    dia "...O que você que dizer?"
    show diane f_normal
    show debbie 60f
    deb "Ele está sempre ficando com ereção perto de mim..."
    deb "... E me tocando ... de certas maneiras."
    show diane f_surprised
    show debbie 59f
    dia "..."
    show debbie 60f
    deb "... E no outro dia, encontrei-o brincando consigo mesmo; Na minha cama!"
    deb "... Com minha calcinha!"
    show diane f_normal_talk
    show debbie 59f at Position(xpos=0.3318,ypos=1.000)
    dia "O que você fez?!"
    show diane f_normal
    show debbie 60f
    deb "Nós discutimos isso!"
    deb "Eu disse a ele para não fazer esse tipo de coisa no meu quarto, mas..."
    show diane f_normal_talk
    show debbie 59f
    dia "Mas o que?"
    show diane f_normal
    show debbie 60f at Position(xpos=0.3318,ypos=1.000)
    deb "Eu peguei ele de novo! Ele pediu desculpas e começou a falar sobre os impulsos que ele não podia controlar..."
    show diane f_normal_talk
    show debbie 59f
    dia "Ok, então o que você disse?"
    show diane f_surprised
    show debbie 17f at Position(xpos=0.3318,ypos=1.1130)
    deb "... Eu meio que ... Deixei ele terminar."
    show diane f_normal_talk
    show debbie 20f at Position(xpos=0.3318,ypos=1.1130)
    dia "Você assistiu ele se masturbar?"
    show diane f_normal
    show debbie 60f at Position(xpos=0.3318,ypos=1.000)
    deb "Eu não sabia o que fazer!"
    deb "Eu pensei que talvez ele estivesse fora de sí..."
    deb "... Você sabe?"
    show diane f_normal_talk
    show debbie 59f
    dia "Isso é tão desobediente..."
    show diane f_normal
    show debbie 60f
    deb "Tem mais..."
    show diane f_normal_talk
    show debbie 59f
    dia "Mais?!"
    dia "Sério?!"
    dia "Conte-me!"
    show diane f_surprised
    show debbie 60f
    deb "Diane..."
    show diane f_normal_talk
    show debbie 59f
    dia "{b}[deb_name]{/b}, Conte-me!"
    show diane f_surprised
    show debbie 60f
    deb "... Nós tomamos banho juntos."
    show diane f_normal_talk
    show debbie 59f
    dia "Uau..."
    show diane f_teasing
    dia "... Como ele está?"
    show diane f_surprised
    show debbie 60f
    deb "Diane!!"
    show diane f_laugh
    show debbie 59f
    dia "O que?!"
    show diane f_thinking
    dia "Não aja como uma puritana! Nós dois sabemos que você está morrendo de vontade de me dizer!"
    show diane f_surprised
    show debbie 60f
    deb "... {b}*Suspiro*{/b}"
    show diane f_teasing
    show debbie 59f
    dia "Você tocou nele?"
    show diane f_smirk
    show debbie 60f
    deb "... Sim."
    deb "Eu meio que o empurrei para baixo e para cima..."
    show diane f_teasing
    show debbie 59f
    dia "Você fez tudo isso?"
    show diane f_smirk
    show debbie 60f
    deb "...Sim Até ele gozar."
    show debbie 59f
    if not M_diane.finished_state(S_diane_drunken_garden_work):
        show diane f_teasing
        dia "Então, como foi?"
        show diane f_smirk
        show debbie 60f
        deb "... Como foi?"
        show diane f_teasing
        show debbie 59f
        dia "Sentir o {b}Pau{/b} ,dele {b}[deb_name]{/b}! É grande?"
        show diane f_smirk
        show debbie 60f
        deb "( !!! )"
        show debbie 59f
        deb "..."
        show diane f_explain
        dia "Não fique tímida comigo agora, garota. Desembucha!"
        show debbie 60f
        show diane f_smirk
        deb "{b}Diane{/b}, ele tem o maior... {b}Pau{/b} Que eu já vi!"
        show diane f_teasing
        show debbie 59f
        dia "... Você não diz?!"
    show diane f_laugh
    dia "Estou surpresa que você parou na Mastubarção..."
    show diane f_smirk
    show debbie 16f at Position(xpos=0.3318,ypos=1.1130)
    deb "{b}Diane{/b}, ele é só uma criança!"
    show diane f_teasing
    show debbie 15f
    dia "Pfft, ele está na faculdade!"
    show diane f_smirk
    show debbie 16f
    deb "Sim, mas tenho idade suficiente para ser a {b}Mão{/b} dele!"
    show diane f_laugh
    show debbie 15f
    dia "... Mas {b}você não É mãe{/b}, dele {b}[deb_name]{/b}!"
    show diane f_normal
    show debbie 16f
    deb "Ah, eu sei, {b}Diane{/b}..."
    show diane f_surprised
    show debbie 15f
    dia "Ele obviamente quer isso."
    show diane f_normal
    show debbie 16f
    deb "Por favor, me diga que não estou fazendo algo terrivelmente errado..."
    show diane f_normal_talk
    show debbie 15f
    dia "A decisão é sua, mas..."
    dia "Eu acho que você deveria relaxar e aproveitar um pouco. Quem se importa com a diferença de idade?"
    show diane f_normal
    show debbie 16f
    deb "Mesmo? Você não acha que é errado?"
    show diane f_normal_talk
    show debbie 15f
    dia "Não. Eu não vejo o mal nisso!"
    show diane f_normal
    show debbie 16f
    deb "Eu suponho que não estamos machucando ninguém ... E nós dois somos adultos."
    show diane f_laugh
    show debbie 15f
    dia "Além disso, tudo isso é muito {b}EXCITANTE{/b}!"
    show diane f_normal
    show debbie 16f
    deb "Você é uma influência tão ruim! Eu não sei porque eu te escuto!"
    show diane f_normal_talk
    show debbie 15f
    dia "... Porque você sabe que estou certa! Apenas dê uma chance. Quem sabe talvez isso seja uma coisa boa?"
    show diane f_normal
    show debbie 62f at Position(xpos=0.3318,ypos=1.000)
    deb "Sim, suponho que tudo é possível..."
    show diane f_normal_talk
    show debbie 61f
    dia "Tudo bem, é melhor eu ir para casa. Está ficando tarde."
    show diane f_teasing
    dia "Continuaremos essa conversa em outra hora. Eu quero todos os detalhes suculentos para o meu banco de espancamento!"
    show diane f_normal
    show debbie 62f
    deb "{b}Diane{/b}! Você é terrível!"
    deb "Por que você não vem jantar algum dia? Eu adoraria te ver mais vezes!"
    show debbie 61f
    show diane f_normal_talk
    dia "Seria bom, {b}[deb_name]{/b}. Contanto que eu não seja a única a cozinhar!"
    dia "Boa sorte querida."
    scene expression L_home_entrance.background
    show player 5
    player_name "( Isso ... foi muito para absorver. )"
    player_name "( {b}[deb_name]{/b} Parecia realmente está muito confusa, Sobre tudo que aconteceu... )"
    show player 203
    player_name "( É ela disse que está gostando. )"
    player_name "( De qualquer maneira, Estou feliz {b}Diane{/b} Acha que está tudo bem, para nós fazendo essas coisas! )"
    return

label kitchen_mom_kissing_practice:
    show player 2 at left
    show debbie 14b at right
    player_name "Ahh, vamos{b}[deb_name]{/b}!"
    player_name "Você é o única que disse que eu preciso sair e começar a namorar."
    player_name "Isso ajudaria se eu soubesse como beijar uma garota corretamente, Você não acha?"
    show player 1
    deb "..."
    show debbie 13
    deb "... Bem."
    deb "Sim, suponho que eu poderia lhe dar algumas dicas."
    show debbie 14
    show player 2
    player_name "eu realmente apreciaria isto, {b}[deb_name]{/b}."
    show player 1
    show debbie 73 at Position(xpos=0.85, ypos=1.0) with dissolve
    deb "Ok, humm ... Venha para perto de mim."
    show player 227c at Position(xpos=0.25, ypos=1.0) with dissolve
    show debbie 72
    player_name "Tudo bem."
    show player 227
    show debbie 73
    deb "Boa. Agora, incline-se, Bem assim."
    show player 227c zorder 1 at Position(xpos=0.30, ypos=1.0) with dissolve
    show debbie 72 zorder 0 at Position(xpos=0.80, ypos=1.0) with dissolve
    player_name "Ok."
    show player 227
    show debbie 73
    deb "... Feche os olhos e pressione suavemente seus lábios contra os meus..."
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    pause
    show debbie 79
    deb "Mmm."
    show debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause
    show player 227c
    player_name "Então como foi?"
    show player 227
    show debbie 77
    deb "... Uau."
    show player 227c
    show debbie 76
    player_name "Foi ruim?"
    show player 227
    show debbie 73
    deb "Não. Isso foi muito bom!"
    show player 227c
    show debbie 72
    player_name "Mesmo?!"
    show player 227
    show debbie 73
    deb "Sim. Tem certeza que esta é sua primeira vez?"
    show player 227c
    show debbie 72
    player_name "Sim. Você tem alguma dúvida?"
    show player 227
    deb "..."
    show debbie 73
    deb "Bem vamos ver..."
    deb "Não sei!"
    deb "Beije-me novamente e eu vou te mostrar um pequeno truque!"
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    pause
    show debbie 79
    pause
    show debbie 80c
    player_name "( !!! )" with hpunch
    show debbie 76 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    deb "..."
    show player 227c
    player_name "Uau!"
    player_name "Aquilo que você fez com a sua língua foi tão legal!"
    show player 227
    show debbie 75
    deb "Hehe, Sim."
    show debbie 73
    deb "É apenas uma coisinha que aprendir com o tempo..."
    show player 227c
    show debbie 72
    player_name "Hmm, Posso tentar?"
    show player 227
    show debbie 73
    deb ".... Hã."
    show player 227c
    show debbie 72
    player_name "Por favor?"
    show player 227c
    show debbie 73
    deb "Sim Está bem!"
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    pause
    show debbie 79
    pause
    show debbie 80b
    deb "( !!! )" with hpunch
    show debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    deb "..."
    show player 227c
    player_name "Então como foi?!"
    show player 227
    deb "Mmm..."
    show player 227c
    player_name "{b}[deb_name]{/b}?"
    show player 227
    show debbie 77
    deb "Oh, Desculpa!"
    show debbie 75
    deb "Isso foi MUITO bom, querido!"
    deb "Quero dizer, uau! Você vai ser um profissional, Quando sair para o mundo dos namorados!"
    show player 227c
    show debbie 76
    player_name "Mesmo? obrigado {b}[deb_name]{/b}!"
    show player 227
    deb "Mmmhmm."
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    pause
    show debbie 79
    pause
    show debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 233 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause 
    show debbie 77
    pause
    show debbie 74
    deb "Ah!"
    deb "Ah Meu deus..."
    show player 230
    player_name "..."
    show player 232
    player_name "Desculpa, {b}[deb_name]{/b}."
    player_name "Eu não queria..."
    show player 231
    show debbie 75
    deb "Hehe, tudo bem, querido. É perfeitamente compreensível."
    show debbie 73
    deb "É melhor darmos uma pausa."
    show player 232
    show debbie 72
    player_name "... Sim. OK."
    player_name "Você acha que, talvez, poderíamos fazer isso de novo algum dia?"
    show player 231
    deb "..."
    show player 232
    player_name "Você sabe ... Apenas para praticar?"
    show player 231
    show debbie 73
    deb "Eu suponho que estaria tudo bem."
    deb "Apenas para praticar!"
    show player 232
    show debbie 72
    player_name "Sim claro!"
    show player 231
    show debbie 73
    deb "Tudo bem. Sinta-se à vontade para me perguntar a qualquer momento."
    show player 232
    show debbie 72
    player_name "Obrigado {b}[deb_name]{/b}!"
    show player 231
    show debbie 73
    deb "Sem problemas, {b}[firstname]{/b}."
    show player 232
    show debbie 72
    player_name "Até mais!"
    hide debbie with dissolve
    show player 1 at Position(xpos=0.55, ypos=1.0) with dissolve
    player_name "..."
    show player 21f at Position (xpos=0.5, ypos=1.0) with dissolve
    player_name "Isso foi demais!"
    return

label kitchen_mom_dishes:
    scene expression player.location.background_closeup with None
    show debbie 116 at right
    with dissolve
    pause
    show debbie 117 at Position(xpos=1014)
    pause
    show debbie 116 at right
    pause
    show debbie 117 at Position(xpos=1014)
    pause
    show debbie 116 at right
    show player 1 at left with dissolve
    pause
    show debbie 117 at Position(xpos=1014)
    pause
    show debbie 119 at Position(xpos=1014)
    deb "Oi, querido!"
    show debbie 120
    show player 14
    player_name "Oi, {b}[deb_name]{/b}!"
    show debbie 119
    show player 1
    deb "Você precisa de algo?"
    deb "Eu só estou terminando os pratos..."
    show debbie 120
    return

label kitchen_mom_dishes_yes:
    show debbie 118
    show player 14
    player_name "Por que você não faz uma pausa por algum tempo?."
    player_name "Eu vou secar o resto."
    show debbie 119
    show player 1
    deb "Isso é muito fofo, mas você não precisa fazer isso."
    show debbie 118
    show player 14
    player_name "Não, tudo bem. Estou entediado de qualquer maneira."
    show debbie 119
    show player 1
    deb "Tudo bem. Se você está entediado..."
    show player 272
    show debbie 62
    deb "Basta secar e guardá-los no armário."
    show player 273
    show debbie 61
    player_name "Ok vou fazer isso."
    show debbie 63
    show player 272
    deb "Obrigado por ajudar por aqui {b}[firstname]{/b}."
    show player 274
    show debbie 61
    player_name "O prazer é meu, {b}[deb_name]{/b}."
    scene expression "backgrounds/location_home_cutscene01.jpg"
    show expression FilteredText("I don't think {b}[deb_name]{/b} had ever had help with dishes before... \nShe told me her late husband never did any work around the house and my {b}Dad{/b} only really helped with yard work or broken appliances. \nShe stayed with me in the kitchen until I was finished and we had a nice long chat. \nIt was nice getting to know {b}[deb_name]{/b} better...") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    return

label kitchen_mom_dishes_no:
    show player 14 at left
    show debbie 120 at Position(xpos=1014)
    player_name "OK. Eu voltarei mais tarde, então."
    return

label kitchen_diane_debbie_evening_visit:
    scene expression "backgrounds/location_home_kitchen_secret.jpg"
    show diane b_kitchen a_empty
    show debbie 165bf at Position(xpos=0.3318,ypos=1.000)
    with dissolve
    deb "E você está descansanda bastante?"
    show debbie 169bf
    show diane f_lookup
    dia "... Sim mãe."
    show diane f_smirk
    show debbie 165f
    deb "Oh, quieto!"
    show debbie 164f
    show diane f_laugh
    dia "Haha!"
    show diane f_normal
    show debbie 165f
    deb "Eu só me preocupo com você é tudo."
    show debbie 164f
    show diane f_normal_talk
    dia "Eu sei, {b}[deb_name]{/b} e eu realmente aprecio isso..."
    dia "... But I've got everything under control, I promise!"
    dia "Eu me estabeleci em um bom horário de trabalho o {b}[firstname]{/b} foi certificando-se que eu cumpri."
    show diane f_normal
    show debbie 165bf
    deb "Ele não sabe ... Sobre... Você sabe..."
    show debbie 169bf
    show diane f_shamed_talk_smile
    dia "Mmm, Sim..."
    show diane f_shamed
    show debbie 165bf
    deb "{b}Diane{/b}..."
    show debbie 169bf
    show diane f_shamed_talk_smile
    dia "Eu não queria que ele descobrisse!"
    dia "Ele me pegou naquela noite que você mandou ele com a torta..."
    show diane f_shamed
    show debbie 169bf
    deb "..."
    show diane f_smirk_talk
    dia "Obrigado por isso, pelo caminho."
    show diane f_smirk
    show debbie 164bf at Position (xoffset=10) with dissolve
    deb "..."
    show diane f_laugh
    dia "Quer dizer, a torta foi deliciosa!"
    show diane f_smirk
    show debbie 165bf with dissolve
    deb "Você sabe, se você tivesse me dito o que você estava fazendo desde o início, eu nunca o teria mandado para trabalhar em seu jardim neste verão..."
    show debbie 169bf
    show diane f_laugh
    dia "Haha, bem, eu acho que é uma coisa boa que eu não te contei então, né?"
    show diane f_smirk
    deb "..."
    show diane f_normal_talk
    dia "E além disso, meu jardim nunca pareceu melhor."
    dia "Você deve ver o tamanho das culturas que o {b}[firstname]{/b} está produzindo!"
    show diane f_normal
    deb "..."
    show debbie 165bf
    deb "Você não tem ele lá com você enquanto você está fazendo isso, não é?"
    show debbie 169bf
    show diane f_surprised_down
    dia "O que?"
    show diane f_shamed_talk_smile
    dia "... Uhh, não. Normalmente não."
    show diane f_shamed
    show debbie 165bf
    deb "{b}Diane{/b}!!!"
    show debbie 169bf
    show diane f_shamed_talk_smile
    dia "O que?!"
    show diane f_shamed_talk
    dia "Você sabe como ele é!"
    dia "Tão determinado que ele tem que ajudar com cada coisinha..."
    show diane f_shamed_talk_smile
    dia "Ele continua aparecendo e pedindo para dar uma mão!"
    show diane f_shamed_talk_look
    dia "Então você vai levá-lo todo trabalhado sobre a minha saúde, então agora é praticamente impossível mantê-lo fora!"
    show diane f_shamed
    show debbie 165bf
    deb "Hmm, pode ser melhor se ele parar de trabalhar para você..."
    show debbie 169bf
    show diane f_shamed_talk
    dia "Ah, agora você está apenas sendo ridícula!"
    show diane f_shamed
    show debbie 165bf
    deb "Você não deveria estar expondo-o a"
    show debbie 169bf
    show diane f_shamed_talk
    dia "Ele não é mais um garoto, {b}[deb_name]{/b}!"
    show diane f_normal_talk
    dia "Eu acho que ele aguenta ver um par de mamas..."
    show diane f_normal
    deb "..."
    if M_mom.finished_state(S_mom_diane_visit):
        show diane f_smirk_talk
        dia "Além disso, as coisas que acontecem no meu galpão são bem mais simples do que as pequenas sessões de banho com ele!"
        show diane f_smirk
        show debbie 164bf at Position (xoffset=10)
        deb "!!!" with hpunch
        show debbie 166df with dissolve
        deb "Isso não é- !!"
        show debbie 166cf
        deb "{b}*Suspiro*{/b} Eu nunca deveria ter te falado sobre isso..."
        show debbie 166ef
        show diane f_laugh
        dia "Haha, por favor!"
        show diane f_smirk_talk
        dia "Com quem você tem que discutir essas coisas?!"
        dia "Além disso, acho super quente!"
        show diane f_smirk
        show debbie 165bf
        deb "Sim, estou ciente."
        show debbie 169bf
    else:
        show diane f_normal_talk
        dia "Você está realmente fazendo uma grande parte disso, {b}[deb_name]{/b}!"
        dia "{b}[firstname]{/b} é realmente maduro para a idade dele."
        show diane f_normal
        deb "..."
        show diane f_explain
        dia "Ele tem sido um perfeito cavalheiro sobre a coisa toda."
        show diane f_normal_talk
        dia "Você deveria passar mais tempo com ele e veria o que eu quero dizer."
        show diane f_normal
        show debbie 165bf
        deb "Você realmente acha que ele pode lidar com isso?"
        show debbie 169bf
        show diane f_laugh
        dia "Eu sou positiva!"
        show diane f_normal
        show debbie 166bf
        deb "( Hmm, talvez eu deva passar mais tempo com ele... )"
        show debbie 169bf
    show diane f_normal_talk
    dia "Olha, eu simplesmente não posso perder {b}[firstname]{/b} agora, {b}[deb_name]{/b}."
    dia "Não quando minha empresa está apenas decolando."
    show diane f_normal
    deb "..."
    show debbie 165bf
    deb "As coisas estão realmente indo bem, né?"
    show debbie 169bf
    show diane f_laugh
    dia "Melhor do que eu jamais imaginei!"
    show diane f_normal_talk
    dia "Eu já estou procurando maneiras de expandir."
    show diane f_normal
    show debbie 165bf
    deb "O que você quer dizer com expandir?"
    show debbie 169bf
    show diane f_normal_talk
    dia "Bem, conseguir um espaço de trabalho adequado para uma coisa."
    show diane f_normal
    show debbie 165bf
    deb "Área de trabalho?"
    show debbie 169bf
    show diane f_laugh
    dia "Yeah!"
    show diane f_thinking
    dia "Eu estava olhando para um pequeno celeiro mais adorável no outro dia, cerca de duas horas de carro fora da cidade."
    show diane f_normal_talk
    dia "Vou ter que te mandar as fotos."
    show diane f_normal
    show debbie 168f
    deb "Celeiro?!"
    deb "Você não pode estar falando sério!"
    show debbie 164f
    show diane f_explain
    dia "Heh eu estou falando sério!"
    show diane f_normal_talk
    dia "Você sabe que eu sempre quis um!"
    show diane f_normal
    show debbie 165f
    deb "Sim, mas você tem que admitir, este não é o tipo de gado que você imaginou enchendo-o com..."
    show debbie 164f
    show diane f_normal_talk
    dia "Verdade."
    show diane f_smirk_talk
    dia "... Isto é muito melhor do que eu planejei!"
    show diane f_smirk
    show debbie 168f
    deb "Oh meu Deus, você é tão esquisita..."
    show debbie 165f
    show diane f_laugh
    dia "Hahaha!"
    deb "Hahaha!"
    show diane f_normal
    deb "Então, para onde tudo isso está acontecendo?"
    deb "Você vai eventualmente começar a procurar mais mulheres para se juntar ao seu pequeno negócio de leite?"
    show debbie 164f
    show diane f_normal_talk
    dia "Sim talvez..."
    dia "Quer dizer, eu não estou lá ainda, mas é definitivamente algo que eu pensei sobre..."
    show diane f_smirk_talk
    dia "... Essa é a sua maneira de se voluntariar?"
    show diane f_smirk
    show debbie 168f
    deb "Pfft, Okay, certo!"
    show debbie 164f
    show diane f_laugh
    dia "Haha, Vamos lá!"
    show diane f_smirk
    show debbie 165f
    deb "De jeito nenhum!"
    deb "Eu não estou me metendo com todos os seus sonhos bobos."
    show debbie 164f
    show diane f_smirk_talk
    dia "Você é um cobertor tão molhado às vezes..."
    dia "... Mas veja, é por isso que eu preciso {b}[firstname]{/b} para continuar me ajudando!"
    dia "Ninguém mais vai trabalhar tão duro quanto ele..."
    show diane f_thinking
    dia "... Pelo menos ninguém que eu possa pagar."
    show diane f_normal
    show debbie 169bf
    deb "..."
    show debbie 165bf
    deb "Ugh, bem."
    deb "... Mas eu quero que você me prometa que não haverá nenhum negócio engraçado acontecendo!"
    show debbie 169bf
    show diane f_normal_talk
    dia "Oh meu Deus, pare de se preocupar!"
    dia "Eu vou estar no meu melhor comportamento, eu prometo."
    show diane f_normal
    show debbie 169bf
    deb "Hmmph."
    show debbie 169bf
    dia "..."
    show debbie 165bf
    deb "Duas horas?!"
    deb "São todos os celeiros que você está olhando tão longe?"
    show debbie 169bf
    show diane f_normal_talk
    dia "Bastante."
    dia "{b}Prefeito Garupa{/b} possui toda a terra da fazenda apenas fora da cidade e ele está se recusando a vender por algum motivo."
    dia "Então fui forçada a olhar um pouco mais."
    show diane f_normal
    show debbie 165bf
    deb "Meu Deus, o que eu vou fazer se você se mudar?"
    show debbie 169bf
    show diane f_normal_talk
    dia "Ahh, não fique toda boba ainda."
    dia "Ainda há tempo e quem sabe eu possa encontrar algo mais perto."
    show diane f_normal
    deb "..."
    show diane f_laugh
    dia "Se você continuar fazendo essa cara, vai congelar desse jeito..."
    show diane f_normal
    show debbie 168f
    deb "Heh, cala a boca!"
    show debbie 164f
    show diane f_laugh
    dia "Hahaha!"
    show diane f_surprised_down
    dia "Oh meu Deus, olha o tempo..."
    show diane f_normal_talk
    dia "Eu tenho que chegar em casa e bombear mais um lote antes de dormir."
    show diane f_normal
    show debbie 165f
    deb "Aww mas você acabou de chegar aqui!"
    show debbie 164f
    show diane f_shamed_talk_smile
    dia "I know, I'm sorry."
    show diane f_normal_talk
    dia "Eu te ligo amanhã, ok?"
    show diane f_normal
    show debbie 165f
    deb "Sim, ok."
    show debbie b_empty a_empty f_normal_talk at flip
    show debbie at Position (xpos=597)
    show diane b_hug_deb a_empty f_normal at Position (xpos=285)
    with dissolve
    deb "Tenha cuidado ao ir para casa."
    show diane f_normal_talk
    show debbie f_normal
    dia "eu vou."
    show debbie at unflip
    show debbie 164f at Position(xpos=0.3318,ypos=1.000)
    show diane f_laugh b_casual a_casual_sides at lright
    with dissolve
    dia "Não esqueça de experimentar o leite que eu trouxe para você!"
    show diane f_normal
    show debbie 165f
    deb "Ehh, vamos ver..."
    show debbie 164f
    show diane f_normal_talk
    dia "Estou falando sério, {b}[deb_name]{/b}!"
    dia "Coloque um respingo no seu café da manhã ou algo assim."
    dia "Você vai ficar viciada, estou te dizendo!"
    show diane f_normal
    show debbie 165f
    deb "Adeus, {b}Diane{/b}..."
    show debbie 164f
    show diane f_laugh
    dia "Hahaha! Até mais, {b}[deb_name]{/b}."
    scene black
    with fade
    hide diane
    hide debbie
    pause
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 5 at left with dissolve
    show diane b_casual a_casual_sides f_smirk_talk
    with dissolve
    dia "Olá {b}[firstname]{/b}!"
    dia "Suas orelhas estão queimando?"
    show diane f_smirk
    show player 10
    player_name "Hmm?"
    show player 5
    show diane f_smirk_talk
    dia "Nós estávamos falando sobre você..."
    show diane f_smirk
    show player 29 with dissolve
    player_name "Oh sim?"
    show player 3
    show diane f_smirk_talk
    dia "Você vem amanhã?"
    show diane f_smirk
    show player 29
    player_name "Eu não sei, talvez..."
    show player 3
    show diane f_smirk_talk
    dia "Bem, espero que sim."
    hide player
    show diane kiss_casual
    with dissolve
    pause
    show player 21 at left
    show diane f_smirk_talk b_casual a_casual_sides
    with dissolve
    dia "Eu vou precisar dessas mãos mágicas para um grande trabalho em breve..."
    show diane f_smirk
    show player 28
    player_name "{b}*Gole*{/b} ok."
    show player 21
    show diane f_laugh
    dia "Hehe."
    dia "Até mais, garanhão!"
    show diane f_smirk
    show player 29 with dissolve
    player_name "Tchau, {b}Diane{/b}."
    hide player
    hide diane
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
