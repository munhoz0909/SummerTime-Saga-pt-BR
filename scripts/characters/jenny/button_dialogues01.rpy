label jenny_button_gf_experience_stay_in:
    show player f_normal_talk
    player_name "Fique."
    show player f_normal
    show jenny f_normal_talk
    jen "Você só quer ficar por aqui?"
    show jenny f_normal
    show player f_worried_talk
    player_name "Péssima ideia?"
    show player f_worried
    show jenny f_normal_talk
    jen "Soa um pouco chato..."
    show jenny f_grin_talk
    jen "... Mas pelo menos não vou ter que me preocupar com alguém nos vendo juntos."
    show jenny f_grin
    show player f_worried_talk
    player_name "Tenho certeza que ninguém se importaria, {b}[jen_name]{/b}..."
    show player f_worried
    show jenny f_grin_talk
    jen "Sim, tanto faz."
    show jenny f_grin
    pause
    jen "Hmm."
    hide player
    show jenny b_dressed_pulling1 a_empty f_grin_talk
    with dissolve
    jen "Venha comigo."
    show jenny b_dressed_pulling2 f_grin
    player_name "Onde estamos indo?"
    hide jenny with dissolve
    jen "Andar de baixo."
    scene black with fade
    pause
    scene expression "backgrounds/location_home_livingroom_couch08.jpg" with None
    show expression "backgrounds/location_home_livingroom_couch08b.png" with None
    show jenny b_front_undies a_front_lap f_front_left_talk
    show player b_front a_front_down f_front_right zorder 1
    with dissolve
    if M_diane.finished_state(S_diane_barn_news):
        jen "eu acho {b}Diane{/b} está trabalhando até tarde."
        jen "Sorte nossa, nós temos o sofá para nós mesmos."
    else:
        jen "Parece {b}[deb_name]{/b} está dormindo."
        jen "Sorte nossa, nós temos o sofá so para nós"
    show jenny f_front_forward a_front_remote with dissolve
    if M_jenny.get("jenny_girlfriend_first_time"):
        show player f_front_right_talk
        player_name "Então, o que estamos fazendo?"
        show player f_front_right
        show jenny f_front_forward_talk
        jen "Você disse que queria sair, não é?"
        show jenny f_front_forward
        show player f_front_right_talk
        player_name "Sim."
        player_name "Você quer assistir a um filme de kung-fu?"
        show player f_front_right
        show jenny f_front_left_talk
        jen "Eu espero que você esteja brincando..."
        show jenny f_front_left
        show player f_front_shy_right_talk
        player_name "Você não gosta de kung-fu?"
        show player f_front_shy_right
        show jenny f_front_left_talk
        jen "Heh, nenhuma garota gosta de kung-fu..."
        show jenny f_front_left
        show player f_front_shy_right_talk
        player_name "Isso não é verdade!"
        show player f_front_shy_right
        show jenny f_front_eyeroll a_front_down with dissolve
        jen "Confie em mim."
        jen "É verdade."
        show jenny f_front_forward
        pause
        show jenny f_front_left_talk
        jen "O que você está fazendo?!"
        show jenny f_front_left
        show player f_front_right_talk
        player_name "Eu pensei que seria legal segurar sua mão..."
        show player f_front_right
        show jenny f_front_left_talk
        jen "... Você quer segurar minha mão?"
        show jenny f_front_left
        show player f_front_shy_right_talk
        player_name "Sim?"
        show player f_front_shy_right
        show jenny f_front_left_talk
        jen "O que você tem doze anos?!"
        show jenny f_front_left
        show player f_front_surprised_right
        player_name "..."
        show player f_front_shy_right_talk
        player_name "Tudo bem, tanto faz."
        player_name "Esqueça."
        show player f_front_shy_right
        show jenny f_front_eyeroll
        jen "{b}*Suspiro*{/b} Não me desculpe."
        show jenny f_front_left_talk
        jen "Eu não sou muito bom nessa coisa toda de namorada...."
        show player a_front_hold_hands
        show jenny a_empty
        with dissolve
        jen "Lá."
        show player f_front_right
        show jenny f_front_left
        pause
        show jenny f_front_left_talk
        jen "Feliz agora?"
        show jenny f_front_left
        show player f_front_right_talk
        player_name "Sim."
        show player f_front_right a_front_down
        show jenny f_front_forward a_front_remote
        with dissolve
        pause
        show player f_front_forward
        show jenny f_front_forward_talk
        jen "Oh, aqui vamos nós!"
        show player a_front_hold_hands
        show jenny f_front_forward a_empty
        with dissolve
        player_name "..."
        show player f_front_forward_talk
        player_name "O que é isso?"
        show player f_front_forward
        show jenny f_front_forward_talk
        jen "É essa velha sitcom chamada, \"Pals.\""
        jen "{b}[deb_name]{/b} e eu costumava assistir o tempo todo quando era pequena."
        show jenny f_front_forward
        show player f_front_forward_talk
        player_name "É sobre o que?"
        show player f_front_forward
        show jenny f_front_forward_talk
        jen "Um grupo de seis amigos que moram em Manhattan."
        show jenny f_front_forward
        show player f_front_forward_talk
        player_name "Parece chato."
        show player f_front_forward
        show jenny f_front_laugh
        jen "Não, é muito engraçado!"
        show jenny f_front_forward
        show player f_front_right_talk
        player_name "Você sabe, desde que eu sou o único que paga dinheiro para isso ... Você não acha que eu deveria controlar o controle remoto?"
        show player f_front_right
        show jenny f_front_laugh
        jen "Ok, você definitivamente nunca teve uma namorada antes..."
        player_name "..."
        jen "Haha!"
        show jenny f_front_left
        show player f_front_right_talk
        player_name "Você deveria ser legal, lembra?"
        show player f_front_right
        show jenny f_front_left_talk
        jen "Sim, sim ... Ok!"
        show jenny b_front_cuddle a_empty f_front_cuddle_look zorder 2
        show player f_front_surprised_right a_front_down
        with dissolve
        player_name "!!!"
        show jenny f_front_cuddle_look_up_talk
        jen "Apenas cale a boca e assista, {b}[firstname]{/b}."
        jen "É muito engraçado, você vai ver."
        show jenny f_front_cuddle_look
        show player f_front_forward_talk
        player_name "Ok..."
        show player f_front_forward
        pause
        show jenny f_front_cuddle_look_up_talk
        jen "Oh, este é aquele em que Matt coloca o peru de ação de graças em sua cabeça!"
        show jenny f_front_cuddle_look
        show player f_front_forward_talk
        player_name "O quê?"
        player_name "Por que alguém colocaria um peru na cabeça?"
        show player f_front_forward
        show jenny f_front_cuddle_look_up_talk
        jen "Ele está tentando assustar seu colega de quarto!"
        show jenny f_front_cuddle_look
        pause
        show player f_front_forward_talk
        player_name "Uau, quem é essa?!"
        show player f_front_forward
        show jenny f_front_cuddle_look_up_talk
        jen "Oh ela?"
        jen "Isso é Courtney e você provavelmente acha que ela é super gostosa, grande surpresa..."
        show jenny f_front_cuddle_look_up
        show player f_front_forward_talk
        player_name "Quer dizer, ela é bonita..."
        show player f_front_right_talk_low
        player_name "Não tão bonita quanto você."
        show player f_front_forward
        show jenny f_front_cuddle_look_up_talk
        jen "Oh, barf!"
        jen "Você diz coisas idiotas às vezes..."
        show jenny f_front_cuddle_look_up
        show player f_front_gross_down_talk
        player_name "Desculpa."
        show player f_front_gross_down
        jen "..."
        show jenny f_front_cuddle_look_up_talk
        jen "Não, está tudo bem."
        show jenny f_front_cuddle_look_up
        show player f_front_low
        pause
        show jenny f_front_cuddle_look_up_talk
        jen "Obrigada {b}[firstname]{/b}."
        show jenny f_front_cuddle_look
        show player f_front_right_talk_low
        player_name "Seja bem-vindo."
        show player f_front_forward
        pause
        show player f_front_forward_laugh
        player_name "Hahaha!"
        show player f_front_forward
        pause
        show player f_front_forward_talk
        player_name "Ok, você estava certo."
        player_name "Isso é muito engraçado!"
        show player f_front_forward
        show jenny f_front_cuddle_look_up_talk
        jen "Hehe, Eu te disse!"
        show jenny f_front_cuddle_look
        show player f_front_forward_talk
        player_name "Por que não me lembro de você e {b}[deb_name] {/b}assistindo isso?"
        show player f_front_forward
        show jenny f_front_cuddle_look_up_talk
        jen "Pprovavelmente porque você estava sempre fazendo coisas com {b}seu pai{/b}..."
        show jenny f_front_cuddle_look_up
        show player f_front_forward_talk
        player_name "Sim, acho que isso faz sentido."
        show player f_front_forward
        show jenny f_front_cuddle_look_up_talk
        jen "É um daqueles shows que é mais divertido de assistir com outras pessoas."
        show jenny f_front_cuddle_look
        show player f_front_forward_talk
        player_name "Eu posso ver isso."
        show jenny f_front_cuddle_look_up with None
        show player f_front_forward a_empty
        show expression "characters/player/layeredimage/player_arms_a_front_cuddle.png" zorder 2
        with dissolve
        pause
        show jenny f_front_cuddle_look_up_talk
        jen "Isso é legal."
        show jenny f_front_cuddle_look_up
        show player f_front_forward_talk
        player_name "Sim é."
        show player f_front_forward
        pause
        hide player
        show jenny b_front_kiss f_empty
        hide expression "characters/player/layeredimage/player_arms_a_front_cuddle.png"
        with dissolve
        player_name "!!!"
        pause
        show player b_front_kiss_talk a_empty f_front_kiss_talk
        show jenny b_front_kiss_talk f_front_kiss
        with dissolve
        player_name "Para o que foi aquilo?"
        show player f_front_kiss
        show jenny f_front_kiss_talk
        jen "Sem motivo."
        jen "Eu apenas senti isso."
        show jenny f_front_kiss
        show player f_front_kiss_talk
        player_name "Heh, bem, você sente vontade de fazer um pouco mais?"
        show player f_front_kiss
        show jenny f_front_kiss_talk
        jen "Taaalvez..."
        hide player
        show jenny b_front_kiss a_empty f_empty
        with dissolve
        jen "Mmm."
        pause
        scene black with fade
        pause
        scene expression "backgrounds/location_home_livingroom_couch08.jpg"
        show expression "backgrounds/location_home_livingroom_couch08b.png"
        show player b_front a_empty f_front_forward
        show jenny b_front_cuddle a_empty f_front_cuddle_look
        show expression "characters/player/layeredimage/player_arms_a_front_cuddle.png"
        with fade
        pause
        show jenny f_front_cuddle_look_up_talk
        jen "Tudo bem, estou ficando com sono..."
        show jenny b_front_undies a_front_lap f_front_left
        show player a_front_down
        hide expression "characters/player/layeredimage/player_arms_a_front_cuddle.png"
        with dissolve
        show player f_front_right
        player_name "Hmm?"
        show player f_front_right_talk
        player_name "Tudo bem, você pode dormir se quiser."
        player_name "Estou interessado em ver o que vem a seguir."
        show player f_front_right
        show jenny a_front_remote f_front_forward_talk with dissolve
        jen "Heh, nós já assistimos três episódios..."
        show jenny f_front_left_talk
        jen "... E além disso, sou sua namorada, lembra?"
        show jenny f_front_left
        show player f_front_right_talk
        player_name "Sim?"
        show player f_front_right
        show jenny f_front_left_talk
        jen "Então sua namorada está lhe dizendo que é hora de dormir!"
        jen "Vamos lá!"
        hide jenny with dissolve
        show player f_front_right_talk
        player_name "Ok, ok..."
        show player f_front_right
        jen "Hehehe!"
        player_name "( Ela saiu com pressa... )"
        player_name "( {b}Eu deveria me apressar em subir escadas atrás dela.{/b} )"
        hide player with dissolve
    else:
        show player f_front_right_talk
        player_name "Então estamos assistindo \"Pals.\" novamente?"
        player_name "Eu gostei desse show."
        show player f_front_right a_front_hold_hands
        show jenny f_front_left_talk a_empty
        with dissolve
        jen "Bem, nós definitivamente não estamos assistindo filmes de kung-fu..."
        show player f_front_forward
        show jenny f_front_forward
        pause
        show jenny f_front_forward_talk
        jen "Aqui vamos nós."
        show jenny b_front_cuddle a_empty f_front_cuddle_look zorder 2
        show player f_front_low a_front_down
        with dissolve
        player_name "!!!"
        show player f_front_forward a_empty
        show expression "characters/player/layeredimage/player_arms_a_front_cuddle.png" zorder 3 with dissolve
        pause
        show jenny f_front_cuddle_look_up_talk
        jen "Ah, esse é outro bom episódio!"
        show jenny f_front_cuddle_look
        scene black with fade
        pause
        scene expression "backgrounds/location_home_livingroom_couch08.jpg"
        show expression "backgrounds/location_home_livingroom_couch08b.png"
        show jenny b_front_kiss a_empty f_empty
        with fade
        pause
        jen "Mmm..."
        show player b_front_kiss_talk f_front_kiss a_empty
        show jenny b_front_kiss_talk f_front_kiss_talk
        with dissolve
        jen "Ok, vamos lá em cima!"
        show jenny f_front_kiss
        show player f_front_kiss_talk
        player_name "Já?"
        show jenny b_front_undies a_front_remote f_front_forward_talk with dissolve
        show player f_front_right b_front a_front_down with dissolve
        jen "Vamos lá {b}[firstname]{/b}, sua namorada precisa desse seu pau grande!"
        show jenny f_front_left
        show player f_front_right_talk
        player_name "Bem, quando você coloca dessa maneira..."
        show player f_front_right
        show jenny f_front_left_talk
        jen "Vamos lá!"
        hide jenny with dissolve
        show player f_front_right_talk
        player_name "Está bem, está bem..."
        show player f_front_right
        jen "Hehehe!"
        player_name "( {b}Eu deveria me apressar para subir depois dela.{/b} )"
        hide player with dissolve
    return

label jenny_button_gf_experience_start:
    show player f_flirt_talk a_dressed_money with dissolve
    player_name "Here."
    show player f_flirt a_dressed_pocket
    show jenny f_sexy_talk_down a_money
    with dissolve
    if M_jenny.get("jenny_girlfriend_first_time"):
        jen "Eu não posso acreditar que estou fazendo isso..."
    else:
        jen "Heh, é o que eu gosto de ver!"
    show jenny f_sexy a_dressed_hips with dissolve
    jen "..."
    show jenny f_eyeroll
    jen "{b}*Suspiro*{/b} Então, o que você quer fazer?"
    show jenny f_normal
    return

label jenny_button_gf_experience_no_money_repeat:
    show player f_flirt_talk
    player_name "Bem, nem tudo."
    show player f_flirt
    show jenny f_upset_talk
    jen "Desde quando você está quebrado?!"
    show jenny f_upset
    show player f_normal_talk
    player_name "Não sei..."
    show jenny f_eyeroll
    jen "{b}*Suspiro*{/b} Tudo bem, apenas me dê tudo o que você tem e vamos fazer isso..."
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Mesmo?"
    show player f_surprised
    show jenny f_upset_talk
    jen "Sim!"
    show jenny f_upset
    return

label jenny_button_gf_experience_no_money_first:
    show player f_flirt_talk
    player_name "Bem, nem tudo."
    show player f_flirt
    show jenny f_upset
    jen "..."
    show jenny f_upset_talk
    jen "Eu te disse quinhentos dólares!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Mas eu não tenho muito..."
    show player f_worried
    show jenny f_eyeroll
    jen "Ah, isso é muito triste para você."
    show jenny f_grin_talk
    jen "{b}Volte quando tiver dinheiro{/b}, doofus."
    show jenny f_grin
    show player f_sad_talk_down
    player_name "{b}*Suspiro*{/b} está bem."
    show player f_tired
    return

label jenny_button_gf_experience_nevermind:
    show player f_worried_talk
    player_name "pensamento, não estou interessado agora."
    show player f_worried
    show jenny f_upset_talk
    jen "Não perca meu tempo {b}[firstname]{/b}!"
    show jenny f_upset
    return

label jenny_button_gf_experience_evening:
    show player f_flirt_talk
    player_name "Quer fazer isso?"
    show player f_flirt
    show jenny f_grin_talk
    jen "Oh, você quer que a namorada tenha uma experiência hoje à noite?"
    jen "Eu espero que você tenha trazido dinheiro..."
    show jenny f_grin
    return

label jenny_button_gf_experience_day:
    show player f_magic_sit_stand_flirt_talk
    player_name "Quer fazer isso?"
    show player f_magic_sit_stand_flirt
    show jenny f_magic_sit_stand_upset_talk
    jen "Não agora!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried
    player_name "Hmm?"
    show jenny f_magic_sit_stand_grin_talk
    jen "Me chame {b}mais tarde esta noite{/b}!"
    show jenny f_magic_sit_stand_grin
    show player f_magic_sit_stand_normal_talk
    player_name "Oh, certo."
    show player f_magic_sit_stand_normal
    show jenny f_magic_sit_stand_grin_talk
    jen "Não esqueça de trazer o {b}quinhentos dólares{/b} ou!"
    show jenny f_magic_sit_stand_grin
    return

label button_jenny_have_a_surprise_no:
    show player f_worried_talk
    player_name "Não, eu quero a coisa real."
    show player f_worried
    show jenny f_eyeroll
    jen "Sim, não está acontecendo, perdedor."
    show jenny f_upset_talk
    jen "Deixe-me saber quando você chegar aos seus sentidos..."
    show jenny f_upset
    return

label button_jenny_have_a_surprise_yes:
    show player f_normal_talk
    player_name "Sim."
    show player f_normal
    show jenny f_grin_talk
    jen "Então nós temos um acordo!"
    jen "{b}Volte esta noite com quinhentos dólares{/b} e sou toda sua."
    show jenny f_grin
    show player f_worried_talk
    player_name "Por que não podemos começar agora?"
    show player f_worried
    show jenny f_upset_talk
    jen "Uhh, porque é hora do camshow e paga mais do que quinhentos dólares, idiota!"
    show jenny f_upset
    show player f_sad_talk_down
    player_name "... Està bem."
    show player f_tired
    return

label button_jenny_have_a_surprise_necklace:
    show player f_normal_talk
    player_name "Eu tenho uma surpresa para você!"
    show player f_normal
    show jenny f_eyeroll
    jen "Bem, é melhor que seja algo legal!"
    show jenny f_upset
    show player f_shy_down a_dressed_backpack with dissolve
    pause
    if player.has_item("crystal_necklace"):
        show player f_laugh a_dressed_necklace1 with dissolve
    elif player.has_item("pearl_necklace"):
        show player f_laugh a_dressed_necklace3 with dissolve
    else:
        show player f_laugh a_dressed_necklace2 with dissolve
    player_name "Ta da!"
    show player f_normal
    show jenny f_surprised
    jen "..."
    show jenny f_gross_talk
    jen "Eca!"
    show jenny f_gross
    show player f_worried_talk
    player_name "Você não gosta disso?"
    show player f_tired
    show jenny f_gross_talk a_dressed_crossed with dissolve
    jen "Ei, não!"
    show jenny f_gross
    player_name "..."
    show jenny f_gross_talk
    jen "Por que diabos você me compraria isso?!"
    show jenny f_gross
    show player f_tired_talk
    player_name "Eu apenas pensei, talvez fosse convencê-la "
    show player f_worried
    show jenny f_upset_talk
    jen "Oh meu Deus, você está tentando me convidar para um encontro novamente?!"
    show jenny f_gross
    show player f_tired a_dressed_pocket with dissolve
    player_name "..."
    show jenny f_eyeroll
    jen "Que porra, {b}[firstname]{/b}?!"
    show jenny f_upset_talk
    jen "{b}*Suspiro*{/b} Ok, primeiro de tudo, você tem um péssimo gosto..."
    jen "Esse colar parece barato que inferno!"
    show jenny f_upset
    player_name "..."
    show jenny f_upset_talk
    jen "Quero dizer honestamente, se por algum milagre você realmente conseguir uma namorada um dia ... Você deveria apenas dar dinheiro e deixá-la"
    show jenny f_surprised
    jen "..."
    show player f_worried_talk
    player_name "Deixe-a o que?"
    show player f_worried
    show jenny f_grin_talk a_dressed_hips with dissolve
    jen "Oh meu Deus, eu tive uma ideia brilhante!"
    show jenny f_grin
    player_name "..."
    show jenny f_grin_talk
    jen "Eu estou pensando, já que você é obviamente patético e desesperado por uma namorada..."
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Ei, isso não é"
    show player f_worried
    show jenny f_grin_talk
    jen "Eu {i}poderia{/i} estar disposta a {b}agir{/b}... Por uma modesta taxa de curso."
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Espere um segundo."
    player_name "Você está seriamente sugerindo que eu te pague para ser minha namorada?"
    show player f_skeptical
    show jenny f_grin_talk
    jen "Não, estou sugerindo que você me pague {i}faz de conta{/i} que sou sua namorada..."
    show jenny f_grin
    player_name "..."
    show player f_skeptical_talk
    player_name "Por que eu faria isso?"
    show player f_skeptical
    show jenny f_laugh
    jen "Porque como eu disse, você é patético e desesperado."
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Eu não sou!"
    show player f_skeptical
    show jenny f_laugh
    jen "Hahahaah,, você é sim!"
    show jenny f_grin
    player_name "..."
    show jenny f_grin_talk
    jen "Além disso, isso me dará a chance de trabalhar na minha atuação!"
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Sim, você é uma atriz terrível..."
    show player f_skeptical
    show jenny f_angry_talk
    jen "{b}*suspiro*{/b} Foda-se você!"
    jen "Eu sou uma atriz incrível!"
    show jenny f_angry
    show player f_sad_talk_down
    player_name "Ok, certo."
    show player f_sad
    show jenny f_grin_talk a_dressed_hips_touch1 at Position (xpos=440) with dissolve
    jen "Vamos lá, isso seria uma desculpa perfeita para passarmos mais tempo juntos."
    show jenny f_grin
    show player f_worried_talk
    player_name "o que você está fazendo?"
    show player f_worried
    show jenny f_grin_talk a_dressed_hips_touch2 with dissolve
    jen "Eu realmente quero fazer isso, {b}[firstname]{/b}..."
    jen "Deixe-me mostrar-lhe o que realmente sinto por você."
    show jenny f_grin
    player_name "..."
    show jenny f_grin_talk
    jen "Eu não quero mais esconder..."
    show player f_surprised
    jen "Eu quero dizer ao mundo todo o quanto eu me importo com você!"
    jen "Como eu penso em você o tempo todo..."
    jen "Seu rosto bonito, seus braços fortes ... Seu adorável corte de cabelo!"
    show jenny f_grin
    show player f_worried_talk
    player_name "Mesmo?"
    show player f_worried
    jen "Mhmm."
    show jenny f_grin_talk
    jen "Eu quero segurar sua mão, {b}[firstname]{/b}!"
    show jenny f_grin
    show player f_normal
    player_name "..."
    show jenny f_grin_talk
    jen "Eu quero provar seus lábios..."
    jen "... Adormecer em seus braços."
    show jenny f_grin
    player_name "..."
    show jenny f_grin_talk
    jen "Eu quero te dizer que eu te amo!"
    show jenny f_grin
    show player f_normal_talk
    player_name "eu quero isso também!"
    pause
    hide jenny
    show jenny f_laugh
    with dissolve
    jen "Pfft, HAHAHAHAHAAAH!!"
    show player f_surprised
    player_name "..."
    show player f_angry_talk
    player_name "Isso não é engraçado, {b}[jen_name]{/b}!"
    show player f_angry
    jen "Você deveria ter visto seu rosto!!"
    jen "HAHAHAAH!{b}*Snobar*{/b}"
    show player f_angry_talk
    player_name "Você é uma puta!"
    show player f_angry
    show jenny f_grin_talk
    jen "Você é quem disse que eu não poderia agir como uma boa atriz!"
    jen "Admita, eu sou muito boa!"
    show jenny f_grin
    show player f_tired
    player_name "..."
    show jenny f_grin_talk
    jen "Eu poderia ser a namorada  Pelo preço certo."
    show jenny f_grin
    show player f_tired_talk
    player_name "{b}*Suspiro*{/b} Quanto você quer?"
    show player f_tired
    show jenny f_grin_talk
    jen "Mmm, digamos quinhentos dólares para a noite."
    show jenny f_grin
    show player f_surprised_talk
    player_name "Quinhentos!!"
    player_name "Isso é muito, {b}[jen_name]{/b}!"
    show player f_surprised
    show jenny f_eyeroll
    jen "Oh, por favor ... É uma mudança idiota."
    show jenny f_grin_talk
    jen "Diga-lhe o que, eu vou jogar amanhã de manhã também."
    show jenny f_grin
    show player f_normal_talk
    player_name "Você quer dizer que ficará comigo a noite toda?"
    show player f_normal
    show jenny f_grin_talk
    jen "Isso é o que você quer, não é?"
    show jenny f_grin
    return

label jenny_button_what_are_you_writing:
    show player f_worried_talk
    player_name "O que você está escrevendo?"
    show player f_worried
    show jenny f_upset_talk
    jen "Não é da sua conta, idiota!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Eu estou apenas curioso"
    show player f_surprised_teeth a_dressed_up
    show jenny f_angry_talk a_dressed_crossed
    with dissolve
    jen "SAIA!!!"
    show jenny f_angry
    hide player with dissolve
    return

label jenny_button_what_are_you_writing_2:
    show player f_worried_talk
    player_name "O que você está escrevendo?"
    show player f_worried
    show jenny f_upset_talk
    jen "Não é da sua conta."
    show jenny f_upset
    show player f_normal_talk
    player_name "Aww, vamos lá ... estou curioso."
    show player f_normal
    show jenny f_upset_talk
    jen "De jeito nenhum, {b}[firstname]{/b}!"
    show player f_worried
    jen "Esses são meus pensamentos particulares!"
    show jenny f_upset
    show player f_skeptical_talk a_dressed_up with dissolve
    player_name "Tudo bem, tudo bem ... Sheesh!"
    show player f_skeptical a_dressed_pocket with dissolve
    return

label jenny_button_nevermind_evening:
    show player f_worried_talk
    player_name "Eu acho que vou indo então..."
    show player f_worried
    show jenny f_eyeroll
    jen "Deus, você é um perdedor."
    show jenny f_upset
    show player f_skeptical a_dressed_thinking with dissolve
    player_name "..."
    show jenny f_angry_talk a_dressed_crossed with dissolve
    jen "Dá o fora!!"
    show jenny f_angry
    hide player with dissolve
    return

label jenny_button_nevermind_evening_2:
    show player f_skeptical_talk
    player_name "Mmm, esqueça."
    show player f_laugh
    player_name "Eu tenho outras coisas para fazer hoje."
    show player f_normal
    show jenny f_eyeroll
    jen "Okay, certo!"
    show jenny f_grin_talk
    jen "O que diabos você faz?"
    show jenny f_laugh
    show player f_tired
    jen "Além de sentar no seu quarto e brincar com o seu minúsculo pequeno dingus?"
    if M_jenny.get("dominance") <= 0:
        player_name "..."
        jen "Hahaha!"
        show jenny f_grin
        show player f_tired_talk a_dressed_wave with dissolve
        player_name "Seja como for, estou saindo."
        show player f_tired a_dressed_pocket with dissolve
        show jenny f_grin_talk
        jen "Tchau, perdedor!"
        show jenny f_grin
        hide player with dissolve
    else:
        show player f_skeptical
        player_name "..."
        show jenny f_grin
        show player f_flirt_talk a_dressed_point with dissolve
        player_name "Não é tão pequeno e você deveria saber."
        player_name "Você brinca com isso mais do que eu hoje em dia..."
        show player f_flirt a_dressed_pocket with dissolve
        show jenny f_surprised
        jen "!!!"
        show jenny f_surprised_back
        jen "Isso não é verdade"
        show jenny f_angry_talk a_dressed_crossed with dissolve
        jen "Và se ferrar"
        show jenny f_angry
        show player f_laugh
        player_name "Haha!"
        show jenny f_angry_talk
        jen "Vá embora!"
        show jenny f_angry
        show player f_flirt_talk
        player_name "Com prazer."
        hide player with dissolve
    return

label jenny_button_fool_around_evening:
    show player f_flirt_talk a_dressed_point with dissolve
    player_name "Quer brincar?"
    show player f_flirt a_dressed_pocket with dissolve
    show jenny f_normal_talk
    jen "{b}Jane{/b} pode entrar a qualquer momento."
    show jenny f_normal
    show player f_flirt_talk
    player_name "a sim?"
    show player f_flirt
    show jenny f_upset_talk
    jen "Então não agora, {b}[firstname]{/b}..."
    show jenny f_normal_talk
    jen "... Me pergunte de novo {b}mais tarde.{/b}"
    show jenny f_normal
    show player f_tired_talk
    player_name "Ok."
    show player f_tired
    return

label button_jenny_fool_around_pool_repeat:
    show player f_normal_talk
    player_name "Quer brincar?"
    show player f_normal
    show jenny f_grin_talk
    jen "Você quer me foder na piscina de novo?"
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Ehh, eu não sei ... Você quase me afogou da última vez!"
    player_name "Vamos subir e fazer no seu quarto."
    show player f_normal
    show jenny f_grin_talk
    jen "Não, eu quero fazer aqui!"
    show jenny f_grin
    show player f_worried
    pause
    show player f_worried_talk
    player_name "Na cadeira então?"
    show player f_worried
    show jenny f_upset_talk
    jen "Você está brincando?! {b}[deb_name]{/b} nos veria totalmente!!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Sim mas..."
    show player f_worried
    show jenny f_grin_talk
    jen "Você vai ficar bem, seu grande bebê!"
    jen "Vamos lá!"
    hide jenny with dissolve
    pause
    show player f_tired_talk
    player_name "{b}*Suspiro*{/b} Droga..."
    hide player with dissolve
    jump jenny_pool_sex_intro

label button_jenny_fool_around_pool_first:
    if store._in_replay is not None:
        $ player.location = L_home_backyard
        scene expression player.location.background_closeup
        show jenny f_upset b_swimsuit a_swimsuit_hips
    show player f_normal_talk
    player_name "Quer brincar?"
    show player f_normal
    show jenny f_normal_talk
    jen "Não, eu estou ocupada."
    show jenny f_normal
    show player f_skeptical_talk
    player_name "Ocupada com o que?"
    show player f_skeptical
    show jenny f_upset_talk
    jen "Este é o meu tempo sozinha, imbecil."
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Seu tempo sozinha?"
    show player f_skeptical
    show jenny f_normal_talk
    jen "Sim, estou me reconectando com a natureza!"
    show jenny f_normal
    show player f_worried
    player_name "..."
    show player f_skeptical_talk
    player_name "{b}[jen_name]{/b}, você está apenas sentada no nosso quintal tirando fotos de seus peitos..."
    show player f_skeptical
    show jenny f_grin_talk
    jen "Eles ficam ótimos nesse biquíni, não estão?"
    show jenny f_grin
    show player f_tired_talk
    player_name "{b}*Suspiro*{/b}você é tão estranha!"
    show player f_skeptical
    show jenny f_upset_talk
    jen "Foda-se {b}[firstname]{/b}!"
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Por que você não gosta de nadar ou algo assim?"
    show player f_skeptical
    show jenny f_upset_talk
    jen "Por que diabos eu iria querer ir"
    show jenny f_surprised
    pause
    show jenny f_grin_talk
    jen "Espere um segundo,o que {b}[deb_name]{/b} està fazendo agora?"
    show jenny f_grin
    show player f_worried_talk
    player_name "Uhh, eu não sei?"
    player_name "Provavelmente limpando a casa ou lavando roupa."
    show player f_worried
    show jenny f_sexy
    jen "Hmm."
    show player f_worried_talk
    player_name "Por que você está olhando assim para mim?"
    show player f_worried
    show jenny f_grin_talk
    jen "Vamos nadar."
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Really?!"
    show player f_skeptical
    show jenny f_grin_talk
    jen "Sim, vamos..."
    show jenny f_grin
    show player f_normal_talk
    player_name "Impressionante, deixe-me correr para pegar minha roupa de banho!"
    show player f_normal
    show jenny f_laugh
    jen "Você não precisa de roupa de banho!"
    show jenny f_grin_talk
    jen "Apenas tire a roupa e entre!"
    show jenny f_grin
    show player f_worried_talk
    player_name "Quer dizer,  sem roupas mergulhando?"
    show player f_worried
    show jenny f_eyeroll
    jen "Duh."
    show jenny f_grin
    show player f_worried_talk
    player_name "E se {b}[deb_name]{/b} entrar aqui?!"
    show player f_worried
    show jenny f_laugh
    jen "Heh, então ela vai descobrir o que um perdedor pervertido você é..."
    show jenny f_grin
    show player f_angry
    player_name "..."
    show jenny f_grin_talk
    jen "Não seja uma garotinha, ela está ocupada limpando a casa!"
    show jenny f_grin
    show player f_worried_talk
    player_name "Tudo bem, mas só se você tirar a roupa também!"
    show player f_worried
    show jenny f_grin_talk
    jen "Està bem."
    jen "Você primeiro."
    show jenny f_grin
    show player f_worried_talk
    player_name "Està bem."
    show player b_dressed_changing a_empty f_empty with dissolve
    pause
    show player b_dressed_changing2 a_empty f_empty with dissolve
    pause
    show player b_underwear a_naked_sides f_skeptical_talk with dissolve
    player_name "Você não vai começar a se despir?"
    show player f_skeptical
    show jenny f_grin_talk
    jen "Mmm, naaah."
    show jenny f_grin
    show player f_skeptical_talk
    player_name "O que?!"
    show player f_skeptical
    show jenny f_laugh
    jen "Hahaha!"
    scene expression "backgrounds/location_home_backyard_pool_closeup_day.jpg"
    show jenny b_pool_enter a_empty f_empty with dissolve
    pause
    show jenny b_pool_edge f_homepool_edge_player_normal at Position (align=(0,0)) with dissolve
    player_name "Ei, você disse que também ficaria nua!"
    show jenny f_homepool_edge_player_grin_talk
    jen "Sim, bem, eu menti."
    show jenny f_homepool_edge_player_grin
    player_name "..."
    show jenny f_homepool_edge_player_grin_talk
    jen "Apenas pare de choramingar e entre aqui..."
    show jenny f_homepool_edge_player_grin
    show player b_pool_undress a_empty f_empty with dissolve
    player_name "Alright, fine!"
    show jenny b_pool f_homepool_player_surprised with dissolve
    jen "Whoa, não se atreva"
    show player b_pool_jumping1
    show jenny b_pool_cover f_homepool_player_nipple2
    with dissolve
    player_name "BALA DE CANHÃO!!!"
    jen "{b}[firstname]{/b}!!!"
    show player b_pool_jumping2 with dissolve
    pause
    show jenny b_pool f_homepool_player_angry_talk
    show player b_pool_under
    with dissolve
    jen "Seu idiota!"
    show jenny f_homepool_player_angry
    show player b_pool f_homepool_jenny_laugh at Position (align=(0,0)) with dissolve
    player_name "Hahahahaaah!"
    show player f_homepool_jenny_normal
    show jenny f_homepool_player_angry_talk
    jen "Grrr, Você é tão chata!"
    show jenny f_homepool_player_angry
    show player f_homepool_jenny_normal_talk
    player_name "Você merece, você é mentirosa."
    show player f_homepool_jenny_normal
    show jenny b_pool_hair with dissolve
    jen "..."
    show jenny b_pool with dissolve
    show player f_homepool_jenny_normal_talk
    player_name "Então agora o que?"
    show player f_homepool_jenny_normal
    show jenny f_homepool_player_upset_talk
    jen "Bem, eu ia transar com você, mas depois daquela bala de canhão, estou tendo dúvidas..."
    show jenny f_homepool_player_upset
    if M_jenny.get("dominance") <= 0:
        show player f_homepool_jenny_surprised
        player_name "!!!"
        show player f_homepool_jenny_worried_talk
        player_name "Mesmo?"
        show player f_homepool_jenny_worried
        show jenny f_homepool_player_upset_talk
        jen "{b}*Sigh*{/b} Sim, mas agora você vai ter que implorar..."
        show jenny f_homepool_player_angry
        show player f_homepool_jenny_worried_talk
        player_name "Por favor?"
        show player f_homepool_jenny_worried
        show jenny f_homepool_player_grin_talk
        jen "Vá em frente, você sabe o que eu quero ouvir..."
        show jenny f_homepool_player_grin
        show player f_homepool_jenny_worried_talk
        player_name "{b}*Suspiro*{/b} Por favor, {b}Princesa [jen_name]{/b}?"
        show player f_homepool_jenny_worried
        show jenny f_homepool_player_grin_talk
        jen "Por favor, o que?"
        show jenny f_homepool_player_grin
        show player f_homepool_jenny_worried_talk
        player_name "Por favor faça sexo comigo?"
        show player f_homepool_jenny_worried
        show jenny f_homepool_player_grin_talk
        jen "Hmm, Tudo bem ... Isso foi bom o suficiente."
    else:
        show player f_homepool_jenny_skeptical_talk
        player_name "Ok, certo."
        show player f_homepool_jenny_skeptical
        show jenny f_homepool_player_angry_talk
        jen "Estou falando sério, quero um pedido de desculpas!"
        show jenny f_homepool_player_angry
        show player f_homepool_jenny_skeptical_talk
        player_name "Ok, te digo uma coisa."
        player_name "Você pede desculpas por mentir para mim e depois eu peço desculpas por ter espirrado agua em você."
        show player f_homepool_jenny_skeptical
        show jenny f_homepool_player_angry_pouting
        jen "..."
        show player f_homepool_jenny_laugh
        player_name "Então vamos fazer sexo, vamos negociar?"
        show player f_homepool_jenny_normal
        show jenny f_homepool_player_angry_talk
        jen "Dane-se!"
        show jenny f_homepool_player_angry
        show player f_homepool_jenny_normal_talk
        player_name "Sim, essa é a ideia."
        show player f_homepool_jenny_normal
        show jenny f_homepool_player_upset_talk
        jen "Não, quero dizer"
        show jenny f_homepool_player_upset
        show player f_homepool_jenny_laugh
        player_name "Hehe!"
        show player f_homepool_jenny_normal
        show jenny f_homepool_player_eyeroll
        jen "Ugh, você é tão, não é engraçado..."
        show jenny f_homepool_player_upset
        show player f_homepool_jenny_normal_talk
        player_name "Bem, poderíamos simplesmente pular as desculpas e ir direto para o sexo?"
        show player f_homepool_jenny_normal
        show jenny f_homepool_player_upset_talk
        jen "Fine."
    show jenny b_pool_plunge1 f_homepool_player_grin with dissolve
    pause
    hide player
    show jenny b_pool_plunge2 f_homepool_plunge_player_sexy_down
    with dissolve
    pause
    jump jenny_pool_sex_intro

label button_jenny_wanna_watch_porn:
    show player f_normal_talk
    player_name "Você quer assistir porno juntos?"
    show player f_normal
    show jenny f_grin_talk
    jen "Oh, você gosta disso, né?"
    show jenny f_grin
    show player f_normal_talk
    player_name "Definitivamente."
    player_name "Eu pensei que talvez esta noite pudéssemos"
    show player f_normal
    show jenny f_grin_talk
    jen "Pfft!"
    show jenny f_eyeroll
    jen "Eu sei exatamente o que poderíamos fazer..."
    show jenny f_grin
    show player f_worried_talk
    player_name "Isso é um sim?"
    show player f_worried
    show jenny f_upset_talk
    jen "Não, é um talvez ... Se eu quiser."
    show jenny f_upset
    show player f_worried_talk
    player_name "... E se você não fizer?"
    show player f_worried
    show jenny f_laugh
    jen "Então eu acho que você vai ter que fazer com você mesmo, não vai, pequeno perdedor?"
    jen "Hahahaah!"
    show jenny f_grin
    player_name "..."
    return

label button_jenny_fool_around_diningroom_first:
    if store._in_replay is not None:
        $ player.location = L_home_diningroom
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_dinner_sitting a_dinner_sitting_resting f_magic_sit_stand_worried zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    show player f_magic_sit_stand_normal_talk
    player_name "Quer brincar?"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_upset_talk at Position(align=(0,0))
    jen "O quê aqui?"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Não!"
    player_name "Quero dizer, vamos lá para cima e podemos"
    show jenny f_breakfast_grin a_breakfast_dressed_rub with dissolve
    show player f_magic_sit_stand_surprised
    player_name "!!!" with hpunch
    show jenny f_breakfast_grin_talk
    jen "E se eu quiser bem aqui?"
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_worried_talk
    player_name "Você não pode estar falando sério!!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_grin_talk
    jen "Por que não?"
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_worried_talk
    player_name "{b}[deb_name]{/b} está cozinhando bem perto da sala!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_grin_talk
    jen "So?"
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_worried_talk
    player_name "Ela vai nos matar!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_grin_talk
    jen "Ela não precisa saber..."
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_worried_talk
    player_name "Ok, certo!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_eyeroll a_breakfast_dressed_crossed with dissolve
    jen "Você é um covarde..."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Não, eu não sou!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_grin_talk
    jen "Então prove isso!"
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_worried_talk
    player_name "Hã?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_grin_talk a_breakfast_dressed_yell with dissolve
    jen "Ei, {b}[deb_name]{/b}?!"
    show jenny f_breakfast_grin a_breakfast_dressed_crossed with dissolve
    deb "Hã?"
    show player f_magic_sit_stand_worried_talk
    player_name "O que você "
    if store._in_replay is not None:
        jump jenny_dining_room_sex_intro
    return

label button_jenny_fool_around_diningroom_repeat:
    show player f_magic_sit_stand_normal_talk
    player_name "Quer brincar?"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_grin_talk at Position(align=(0,0))
    jen "Você quer se divertir?"
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_normal_talk
    player_name "Sim, vamos "
    show player f_magic_sit_stand_surprised
    show jenny f_breakfast_grin_talk
    jen "Ei, {b}[deb_name]{/b}?!"
    show jenny f_breakfast_grin
    deb "Hã?"
    show player f_magic_sit_stand_worried_talk
    player_name "Não, eu não quero"
    return

label jenny_button_leave_final_morning:
    show player f_magic_sit_stand_worried_talk
    player_name "Eu só vou te ver mais tarde ... Ok?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Sim, tanto faz."
    jen "Até mais."
    show jenny f_magic_sit_stand_upset
    hide player with dissolve
    return

label jenny_button_leave_final_bedroom:
    show player f_normal_talk
    player_name "Desculpa."
    show player f_normal
    show jenny f_upset_talk
    jen "Ugh, que porra, {b}[firstname]{/b}?!"
    jen "Você está me fazendo perder dinheiro!"
    show jenny f_gross
    show player f_skeptical_talk
    player_name "Você não pode fazer um sem mim?"
    show player f_skeptical
    show jenny f_eyeroll
    jen "Sim..."
    show jenny f_upset_talk
    jen "... Mas eles pagam mais quando esse grande pau seu está envolvido!"
    show jenny f_upset
    show player f_normal_talk
    player_name "Eu volto amanhã, ok?"
    show player f_normal
    show jenny f_upset_talk
    jen "Você e um, idiota."
    show jenny f_upset
    hide player with dissolve
    return

label jenny_button_ask_movie_date:
    scene expression player.location.background_closeup with None
    show player f_normal_talk
    show jenny f_normal
    player_name "Ei, você deveria se vestir."
    show player f_normal
    show jenny f_gross_talk
    jen "Vestir-se?!"
    show jenny f_grin_talk
    jen "Você geralmente quer que eu tire as roupas, não as coloque..."
    show jenny f_grin
    show player f_laugh
    player_name "Hah, sim eu sei, mas eu tenho uma surpresa para você."
    show player f_normal
    show jenny f_sad_talk
    jen "Hã?"
    show jenny f_sad
    show player f_normal_talk
    player_name "Eu encontrei aquele cara que está espionando você."
    show player f_normal
    show jenny f_sad_talk
    jen "Mesmo?"
    show jenny f_sad
    show player f_normal_talk
    player_name "Sim, ele se desculpou e nos ofereceu ingressos de cinema gratuitos!"
    show player f_normal
    show jenny f_surprised
    jen "..."
    jen "Você quer que eu veja um filme ... Com você?"
    show jenny f_sad
    show player f_normal_talk
    player_name "Sim?"
    show player f_normal
    show jenny f_sad_talk
    jen "Em público..."
    show jenny f_sad
    show player f_worried_talk
    player_name "Sim?!"
    show player f_worried
    jen "..."
    show jenny f_upset_talk a_dressed_crossed
    jen "{b}*Suspiro*{/b} Nós temos que?"
    show jenny f_upset
    show player f_normal_talk
    player_name "Vamos lá, vai ser legal!"
    show player f_normal
    show jenny f_eyeroll
    jen "Ugh, Està bem."
    show jenny f_upset_talk
    jen "Mas eu vou escolher o filme!"
    show jenny f_upset
    show player f_normal_talk
    player_name "Ok."
    show player f_normal
    show jenny f_upset_talk
    jen "E eu quero pipoca!"
    show jenny f_upset
    show player f_surprised
    player_name "..."
    show jenny f_upset_talk
    jen "E vermes gummy!"
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Ok, sheesh!"
    show player f_skeptical
    show jenny f_eyeroll
    pause
    hide player with dissolve
    return

label jenny_button_movie_date:
    scene expression player.location.background_closeup with None
    show player f_skeptical_talk
    show jenny f_normal
    player_name "Apresse-se e se vestir, {b}nós temos um filme para assistir{/b}."
    show player f_normal
    show jenny f_upset_talk
    jen "Ugh, Eu te ouvi pela primeira vez!"
    show jenny f_upset
    hide player with dissolve
    return

label jenny_button_come_to_my_room:
    show player f_flirt_talk
    player_name "Por que você não vem ao meu quarto hoje à noite?"
    show player f_flirt
    show jenny f_sexy_talk
    jen "Heh, oh você gostaria disso, não é?"
    show jenny f_sexy
    if M_jenny.get("dominance") <= 0:
        show player f_worried_talk
        player_name "Sim."
        show player f_worried
        show jenny f_grin_talk a_dressed_crossed with dissolve
        jen "Você vai me implorar por isso?"
        show jenny f_grin
        show player f_worried_talk
        player_name "eu acho..."
        player_name "Eu se você quiser."
        show player f_worried
        show jenny f_laugh
        jen "Hahahaah!"
    else:
        show player f_flirt_talk
        player_name "Sim ... eu perguntei, não?"
        show player f_flirt
        show jenny f_laugh
        jen "Hehehe!"
        show jenny f_sexy
        show player f_flirt_talk
        player_name "Você também gosta e sabe disso."
        show player f_grin
        show jenny f_eyeroll
        jen "Sim, tanto faz."
        show jenny f_sexy
        pause
        show player f_flirt_talk
        player_name "Você é a única que está sempre desmaiando por causa do meu pau..."
        show player f_flirt
        show jenny f_upset_talk a_dressed_crossed with dissolve
        jen "Eu não!"
        show jenny f_upset
        show player f_laugh
        player_name "Hah, você faz totalmente!"
        show jenny f_angry_pouting
        pause
        show player f_flirt_talk
        player_name "Apenas ... Pare de ser teimosa e venha para o meu quarto hoje à noite!"
        show player f_flirt
    show jenny f_sexy_talk
    jen "Sim, eu posso passar por là..."
    show jenny f_grin
    pause
    show jenny f_grin_talk
    jen "... {b}{i}E SE{/i}{/b} Eu me sinto assim."
    show jenny f_grin
    return

label button_jenny_pool_talk:
    scene expression player.location.background_closeup with None
    show jenny b_swimsuit a_swimsuit_hips
    show player f_normal_talk
    player_name "Bom Dia."
    show player f_normal
    show jenny f_normal_talk
    jen "Ei."
    show jenny f_normal_low
    pause
    show player f_normal_talk
    player_name "Você quer que eu mova o guarda-chuva para que você possa tomar sol?"
    show player f_normal
    show jenny f_normal_talk
    jen "O que?"
    jen "Oh, nah..."
    show jenny f_normal
    show player f_worried_talk
    player_name "Mas"
    show player f_worried
    show jenny f_laugh
    jen "Eu não estou aqui para bronzear, seu idiota..."
    show jenny f_normal_talk
    jen "Apenas tentando relaxar."
    show jenny f_normal
    show player f_normal_talk
    player_name "Oh."
    show player f_normal
    show jenny f_eyeroll
    jen "Além disso, não me bronzeio"
    show jenny f_normal
    show player f_worried_talk
    player_name "Não?"
    show player f_worried
    show jenny f_normal_talk
    jen "Eu apenas queimo."
    show jenny f_normal
    show player f_laugh
    player_name "Heh, eu também."
    show player f_normal
    show jenny f_normal_low
    pause
    show player f_worried_talk
    player_name "Então... {b}[deb_name]{/b} queria que eu te perguntasse"
    show player f_surprised
    show jenny f_normal
    player_name "..."
    show player f_skeptical a_dressed_point with dissolve
    show jenny f_upset_down_talk
    jen "O que você é"
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Quem é aquele?"
    show player f_skeptical a_dressed_pocket
    show jenny at flip
    show jenny f_upset at Position (xpos=1000)
    with dissolve
    jen "Hmm?"
    scene expression "backgrounds/location_home_backyard_cutscene01.jpg" with dissolve
    player_name "That guy over there..."
    player_name "O que ele está fazendo?"
    scene expression player.location.background_closeup with None
    show player f_surprised
    show jenny b_swimsuit a_swimsuit_hips f_angry_talk at flip
    show jenny at Position (xpos=475)
    with dissolve
    jen "Mais uma vez, seu filho da puta assustador?!"
    jen "Esta é a terceira vez, este mês!"
    jen "Meu namorado vai chutar sua bunda perseguidora!"
    show jenny f_angry
    scene expression "backgrounds/location_home_backyard_cutscene01.jpg" with dissolve
    bub "Namorado?!"
    scene expression "backgrounds/location_home_backyard_cutscene02.jpg" with dissolve
    bub "Whaaaaaagghh!!!"
    "{b}*THUMP*{/b}" with hpunch
    scene expression player.location.background_closeup with None
    show jenny f_angry_talk b_swimsuit a_swimsuit_crossed
    show player f_worried
    jen "Não fique aí parado, vá socar aquele cara!"
    show jenny f_angry
    show player f_worried_talk
    player_name "Você acabou de me chamar de seu namorado?"
    show player f_worried
    show jenny f_gross_talk
    jen "A sério?!"
    show jenny f_angry_talk
    jen "Há algum pervertido me espionando e você está preocupado com isso?!"
    show jenny f_angry
    show player f_worried_talk
    player_name "certo ... desculpe."
    show player f_worried
    show jenny f_angry_talk
    jen "Apresse-se antes que ele se afaste!"
    show jenny f_angry
    hide player with dissolve
    scene expression "backgrounds/location_home_backyard_cutscene03.jpg" with dissolve
    "Corri para o local onde o perseguidor estava, mas ele já estava Correndo."
    "Ele era mais rápido do que parecia ... Não havia como eu pegá-lo."
    scene expression player.location.background_closeup with None
    show player b_dressed_catch_breath a_empty f_empty with dissolve
    player_name "Haah... Haah..."
    show jenny f_angry_talk b_swimsuit a_swimsuit_crossed with dissolve
    jen "Onde està esse bastardo?!"
    show jenny f_angry
    show player f_tired_talk b_dressed a_dressed_pocket with dissolve
    player_name "Ele fugiu..."
    show player f_tired
    show jenny f_eyeroll
    jen "Ugh, droga!"
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Quem era esse cara?!"
    show player f_skeptical
    show jenny f_upset_talk
    jen "Eu não sei, apenas um esquisito que continua me espionando quando estou aqui na beira da piscina..."
    show jenny f_upset
    show player f_normal
    pause
    show jenny f_upset_talk
    jen "Cara, eu gostaria de pegar ele e dar uma lição!"
    show jenny f_angry_pouting
    show player f_grin
    pause
    show jenny f_gross
    pause
    show jenny f_upset_talk
    jen "Por que você está olhando assim para mim?!"
    show jenny f_upset
    show player f_laugh
    player_name "Você me chamou de namorado."
    show player f_grin
    show jenny f_upset_talk
    jen "Oh meu Deus..."
    jen "Eu só estava tentando assustar esse cara!"
    show jenny f_gross
    show player f_laugh
    player_name "Hehe, certeza de que você estava..."
    show player f_grin
    show jenny f_eyeroll
    jen "Isso so em seus sonhos, perdedor."
    hide jenny with dissolve
    show player f_laugh
    player_name "Bem, isso não é uma coisa muito legal para dizer ao seu namorado..."
    jen "Screw you, {b}[firstname]{/b}!"
    player_name "Hahahaah!"
    show player f_surprised_down
    player_name "( Hmm? )"
    show player b_dressed_pickup a_empty f_empty with dissolve
    pause
    show player a_dressed_ticket b_dressed f_surprised_down with dissolve
    player_name "( É um {b}bilhete de cinema do teatro local{/b}... )"
    show player f_skeptical
    player_name "( Eu me pergunto se esse cara deixou cair? )"
    show player f_surprised_down
    pause
    player_name "( É para {b}hoje mais tarde{/b}. )"
    player_name "( Talvez {b}eu o encontre lá?{/b} )"
    hide player with dissolve
    return

label jenny_button_fool_around:
    show player f_worried_talk
    player_name "Quer brincar?"
    show player f_worried
    show jenny f_normal_talk
    jen "Inferno sim, eu faço!"
    show player f_normal
    show jenny f_grin_down b_pull1 a_empty with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show player f_surprised
    pause
    show jenny f_grin_down b_naked a_naked_panties_remove with dissolve
    pause
    show jenny b_naked_panties_remove_down a_empty f_empty with dissolve
    pause
    show jenny b_naked a_naked_hips f_grin with dissolve
    pause
    show jenny f_grin_talk
    jen "O que você está esperando?"
    hide player
    show jenny b_groping_naked_suck_pre a_groping_naked_up with dissolve
    show jenny b_groping_naked_suck a_groping_naked_up_clench f_surprised with dissolve
    jen "!!!"
    pause
    show jenny f_nipple3
    jen "Mmm..."
    pause
    show jenny b_groping_naked_touch_talk a_empty with dissolve
    player_name "Você tem os melhores peitos, sempre!"
    show jenny b_groping_naked_touch_look a_groping_naked_hips f_laugh
    jen "Hehe, eu sei."
    show jenny b_groping_naked_suck_pre a_groping_naked_up f_nipple3 with dissolve
    pause
    show jenny b_groping_naked_suck a_groping_naked_up_clench f_nipple1 with dissolve
    jen "Haah!"
    jen "Isso é incrível..."
    show jenny f_nipple3
    pause
    show jenny b_groping_naked_finger with dissolve
    jen "Ngghhh..."
    pause
    show jenny f_nipple2
    jen "Pooorra..."
    show jenny f_nipple3
    pause
    show jenny f_nipple2
    jen "Você só vai me provocar?"
    jen "Vamos fazer um camshow!"
    show jenny f_nipple3
    return

label jenny_button_fool_around_not_today:
    show jenny b_groping_naked_touch_talk a_empty f_surprised with dissolve
    player_name "Desculpe, eu não tenho tempo hoje."
    show jenny b_groping_naked_touch_look a_groping_naked_hips f_upset_talk
    jen "Mmm, a sério?!"
    jen "Então porque diabos somos nós?"
    show jenny b_groping_naked_finger a_groping_naked_up_clench f_nipple1 with dissolve
    jen "Haaah!"
    show jenny f_nipple2
    jen "Porra!"
    show jenny f_nipple3
    pause
    show jenny f_nipple2
    jen "Eu vou"
    show jenny f_nipple3
    pause
    show jenny b_groping_naked_squirt f_orgasm_squirt_nipple2 at Position (align=(0,0))
    jen "NGGHHH!!!" with flash
    pause
    show jenny b_groping_naked_orgasm f_orgasm_nipple3 a_empty
    show player at Position (xpos=700)
    with dissolve
    jen "Haah... Haah..."
    show jenny f_orgasm_grin_talk
    jen "Idiota."
    show jenny f_orgasm_grin
    show player f_grin
    player_name "Hehe."
    show player f_normal
    show jenny b_naked a_naked_side f_normal_talk with dissolve
    jen "Ufa, eu preciso me deitar..."
    show jenny f_normal
    show player f_normal_talk
    player_name "Eu vou te ver mais tarde, {b}[jen_name]{/b}."
    show player f_normal
    show jenny f_normal_talk
    jen "Até mais."
    show jenny f_normal
    hide player with dissolve
    return

label jenny_button_really_staying:
    show player f_magic_sit_stand_worried_talk b_magic_sit_stand_dressed a_magic_sit_stand_resting
    with dissolve
    player_name "Você realmente está gostando de mim?"
    show player f_magic_sit_stand_worried
    show jenny b_magic_sit_stand_dressed a_magic_sit_stand_hip_spoon f_magic_sit_stand_upset_talk with dissolve
    jen "Foi o que eu disse, não foi?"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Sim, mas eu pensei que você odiava isso aqui?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Mmm, não é tão ruim ... Agora que tenho dinheiro rolando."
    jen "{b}[deb_name]{/b} não está na minha bunda sobre encontrar um emprego mais e eu recebo três refeições gratuitas por dia..."
    show jenny f_magic_sit_stand_grin
    pause
    show jenny f_magic_sit_stand_grin_talk
    jen "... E todas as minhas necessidades sexuais estão sendo atendidas."
    show jenny f_magic_sit_stand_grin
    show player f_magic_sit_stand_normal_talk
    player_name "Ah sim?"
    show player f_magic_sit_stand_normal
    show jenny f_magic_sit_stand_upset_talk
    jen "Apenas não pense que sou sua namorada ou algo assim!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried
    player_name "..."
    show jenny f_magic_sit_stand_upset_talk
    jen "Você tem um bom pau, mas isso é tudo que eu estou interessada..."
    jen "Entendeu?!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "eu acho."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_grin_talk
    jen "Bom."
    show jenny f_magic_sit_stand_grin
    return

label jenny_button_nevermind_2:
    show player f_skeptical_talk
    player_name "Mmm, esqueça."
    player_name "Eu tenho outras coisas para fazer hoje."
    show player f_skeptical
    show jenny f_eyeroll
    jen "Ok, certo!"
    show jenny f_grin_talk
    jen "O que diabos você está fazendo?"
    show jenny f_laugh
    jen "Além de sentar no seu quarto e brincar com o seu minúsculo pequeno dingus?"
    show jenny f_grin
    if M_jenny.get("dominance") <= 0:
        show player f_worried
        player_name "..."
        show jenny f_laugh
        jen "Hahaha!"
        show player f_skeptical_talk
        player_name "Seja como for, eu estou saindo."
        show player f_worried
        show jenny f_grin_talk
        jen "Tchau, perdedor!"
        show jenny f_grin
        hide player with dissolve
    else:
        show player f_angry
        player_name "..."
        show player f_angry_talk
        player_name "Não é tão pequeno e você deveria saber."
        show player f_laugh
        player_name "Você brinca com isso mais do que eu hoje em dia..."
        show player f_grin
        show jenny f_surprised
        jen "!!!"
        jen "Isso não é"
        show jenny f_angry_talk a_magic_crossed with dissolve
        jen "Foda-se!"
        show jenny f_angry_pouting
        show player f_laugh
        player_name "Haha!"
        show player f_normal
        show jenny f_angry_talk
        jen "Vá embora!"
        show jenny f_angry
        show player f_normal_talk
        player_name "Com prazer."
        hide player with dissolve
    return

label jenny_button_nothing_2:
    show player f_magic_sit_stand_worried_talk
    player_name "Apenas converssando."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Cerrrto."
    show jenny f_breakfast_upset_down
    hide player with dissolve
    return

label jenny_button_warming_up:
    show player f_magic_sit_stand_normal_talk b_magic_sit_stand_dressed a_magic_sit_stand_resting
    with dissolve
    player_name "Finalmente você está gostando de mim?"
    show player f_magic_sit_stand_normal
    show jenny b_magic_sit_stand_dressed a_magic_sit_stand_hip_spoon f_magic_sit_stand_eyeroll with dissolve
    jen "Pfft, porra não!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried
    player_name "..."
    show jenny f_magic_sit_stand_upset_talk
    jen "... Mas você está me fazendo um bom dinheiro, por isso estou disposto a aturar você."
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Okay, certo."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Isso não significa que você vai conseguir uma fatia maior dos lucros!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Oh, eu nunca ousaria pensar nisso..."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Não seja um burro esperto!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Por que você não pode simplesmente admitir que está gostando de mim?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_laugh
    jen "Hã!"
    show jenny f_magic_sit_stand_upset_talk
    jen "Continue sonhando, idiota!"
    show jenny f_magic_sit_stand_upset
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "Tanto faz."
    show player f_magic_sit_stand_worried
    return

label button_jenny_not_swimming:
    show player f_worried_talk
    player_name "Não está nadando?"
    show player f_worried
    show jenny f_upset_talk
    jen "Uhh, não."
    jen "A água está congelando!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Ahhh, vamos."
    player_name "Qual é o motivo ter uma piscina, se você nunca vai usar?!"
    show player f_worried
    show jenny f_eyeroll
    jen "Você só quer me ver toda molhada."
    show jenny f_upset
    show player f_laugh
    player_name "Sim, você me pegou."
    show player f_normal
    show jenny f_gross_talk
    jen "Perv."
    show jenny f_gross
    return

label jenny_button_nevermind:
    show player f_worried_talk
    player_name "Eu acho que vou indo então..."
    show player f_worried
    show jenny f_upset_talk
    jen "Deus, você é um perdedor."
    show jenny f_upset
    show player f_angry
    player_name "..."
    show jenny f_angry_talk
    show player f_surprised
    jen "Dá o fora!!"
    show jenny f_angry
    hide player with dissolve
    return

label jenny_button_just_saying_hi:
    show player f_worried_talk
    player_name "Só queria dizer oi."
    show player f_worried
    show jenny f_upset_talk
    jen "... A sério?!"
    jen "Não perca seu tempo {b}[firstname]{/b}."
    show jenny f_upset
    show player f_worried_talk
    player_name "Não podemos apenas"
    show player f_surprised
    show jenny f_angry_talk
    jen "Não!!!" with hpunch
    jen "Nós não podemos \"somente!\""
    jen "Me mostre algum dinheiro ou dê o fora, perdedor!"
    show jenny f_angry
    show player f_skeptical_talk
    player_name "Ugh, bem..."
    show player f_skeptical
    return

label jenny_button_nothing:
    show player f_magic_sit_stand_worried_talk
    player_name "Apenas tentando ser amigável..."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "{b}*bufar*{/b} Sim, tanto faz."
    jen "Eu não preciso de um amigo, idiota..."
    jen "eu preciso de dinheiro!"
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_laugh
    player_name "Boa sorte com isso."
    hide player with dissolve
    return

label jenny_button_you_and_phone:
    show player f_magic_sit_stand_worried_talk
    player_name "Ninguém nunca lhe disse que é rude olhar para o seu telefone durante uma conversa?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "O que você é minha mãe?!"
    show jenny f_breakfast_eyeroll
    jen "{i}É rude olhar para o telefone{/i}."
    show jenny f_breakfast_upset_down_talk
    jen "Você parece uma velha senil..."
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_tired_talk
    player_name "..."
    show jenny f_breakfast_upset_down_talk
    jen "Loser."
    show jenny f_breakfast_upset_down
    return

label jenny_button_just_curious:
    show player f_magic_sit_stand_worried_talk
    player_name "Apenas curioso como as coisas estão indo."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "Sim, ótimo."
    jen "Por que você se importa existe uma razão para isso?!"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Bem, nós somos meio que ... Família, agora."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_eyeroll
    jen "Pfft, dificilmente..."
    show jenny f_breakfast_upset_talk
    jen "Apenas coma seu café da manhã e deixe-me."
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_tired_talk
    player_name "Tudo bem."
    show player f_diningroom_table_shy_down
    return

label jenny_dialogue_make_a_deal_breakfast:
    show player f_magic_sit_stand_normal_talk b_magic_sit_stand_dressed a_magic_sit_stand_resting
    with dissolve
    player_name "Vamos fazer um acordo."
    show player f_magic_sit_stand_normal
    show jenny b_magic_sit_stand_dressed a_magic_sit_stand_hip_spoon f_magic_sit_stand_upset_talk with dissolve
    jen "Não aqui, você e um idiota..."
    jen "{b}[deb_name]{/b} pode nos pegar."
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Oh, certo."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Me encontre {b}durante a tarde.{/b}"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_normal
    pause
    show jenny f_magic_sit_stand_upset_talk
    jen "... E traga o dinheiro!"
    show jenny f_magic_sit_stand_upset
    hide player with dissolve
    return

label button_jenny_camshow:
    show jenny f_upset_talk
    jen "Vamos, nós temos um show para fazer não perca tempo."
    show jenny f_upset
    show player f_worried_talk
    player_name "Ok."
    show player f_worried
    return

label button_jenny_start_camshow_handjob:
    if store._in_replay is not None:
        $ player.location = L_home_sisbedroom
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["08_unlocked"] = True
    scene expression player.location.background_closeup with None
    show jenny f_upset_talk
    show player f_worried
    with dissolve
    jen "Você está pronto para fazer isso?"
    show jenny f_upset
    show player f_worried_talk
    player_name "Sim, eu acho."
    player_name "Estou um pouco nervoso..."
    show player f_worried
    show jenny f_upset_talk
    jen "Bem, homem!"
    jen "Meus assinantes estão esperando um desempenho duro de você e eu quero dizer isso literalmente!"
    show jenny f_upset
    show player f_worried_talk
    player_name "eu sei."
    show player f_worried
    show jenny f_upset_talk
    jen "Bem, se você sabe, por que suas roupas ainda estão?!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Hã?"
    show player f_worried
    show jenny f_grin_down b_pull1 a_empty with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show player f_surprised
    player_name "!!!"
    show jenny b_panties a_naked_hips f_upset with dissolve
    show jenny f_upset_talk
    jen "Vamos lá, vamos!"
    show jenny f_grin_down b_naked a_naked_panties_remove with dissolve
    show player f_worried_talk
    player_name "Ok."
    show player f_worried
    show jenny b_naked_panties_remove_down a_empty f_empty with dissolve
    pause
    scene black with fade
    pause
    scene expression "backgrounds/location_home_jennybedroom_cutscene05.jpg" with dissolve
    jen "Apenas sente-se na cama e coloque sua máscara."
    player_name "Sim, eu entendi."
    jen "E não tire a màscara!"
    player_name "Sim Sim..."
    jen "Estou falando sério, {b}[firstname]{/b}!"
    player_name "Eu não vou tirar a máscara!"
    scene black with fade
    pause
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show player b_bed_jenny_sit a_empty f_jenny_bed_sit_shy_down of_jenny_bed_sit_mask at Position (align=(0,0))
    show jenny o_under_body_laptop b_naked_bed_belly a_empty f_bed_facing_comp_sexy_talk_down at Position (align=(0,0))
    with dissolve
    jen "Apenas lembre-se de manter sua boca fechada e deixe-me cuidar de tudo."
    show jenny f_bed_facing_comp_sexy_down
    show player f_jenny_bed_sit_worried_talk
    player_name "Sim {b}[jen_name]{/b}, Eu entendi."
    show player f_jenny_bed_sit_shy_down
    show jenny f_bed_facing_comp_eyeroll
    jen "Bom, não esqueça!"
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Tudo bem, aqui vamos nós."
    show jenny b_naked_bed_bellytype f_bed_facing_comp_sexy_down with dissolve
    pause
    show player f_jenny_bed_sit_worried
    show jenny b_naked_bed_belly f_bed_facing_comp_sexy_talk_down with dissolve
    jen "Olá meninos!"
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_laugh
    jen "Hehe, Também senti falta de vocês."
    show player f_jenny_bed_sit_shy_down
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Não, claro que eu não estava brincando!"
    jen "Ele está sentado bem atrás de mim."
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Hmm, Não sei..."
    jen "Isso depende do quanto vocês me dão gorjeta."
    show jenny f_bed_facing_comp_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_facing_comp_laugh
    jen "Hehe, muito agradável!"
    show jenny f_bed_facing_comp_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Eu acho que devemos dar uma olhada no que eu trouxe para vocês, né?"
    show jenny o_laptop b_bed_side_laptop a_bed_side_laptop f_bedside_laptop_sexy_down with dissolve
    show player f_jenny_bed_sit_worried
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Não, ele não tem nome..."
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_laugh
    jen "Haha, porque não é importante!"
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Sim, ele está um pouco nervoso."
    show jenny b_bed_side f_bedside_upset_talk with dissolve
    jen "Você já relaxaria?!"
    jen "Abra e deixe-os ver você!"
    show jenny f_bedside_upset
    player_name "..."
    show player b_bed_jenny_sit_back f_jenny_bed_sit_back_worried of_jenny_bed_sit_back_mask with dissolve
    pause
    show jenny f_bedside_normal_talk
    jen "Aqui vamos nós!"
    show jenny b_bed_side_laptop f_bedside_laptop_sexy_talk_down with dissolve
    jen "Veja, ele é um aprendiz rápido."
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Ah, acho que você ficará agradavelmente surpreso!"
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Bem, vamos dar uma olhada, vamos?"
    show jenny b_bed_side f_bedside_normal_talk with dissolve
    jen "Deitar."
    show jenny f_bedside_normal
    show player b_bed_jenny_laying f_empty od_bed_jenny_laying_dick1 of_bed_jenny_laying_mask with dissolve
    pause
    show jenny a_bed_side_pull1 with dissolve
    pause
    show player od_empty
    show jenny a_bed_side_pull2
    with dissolve
    pause
    show jenny f_bedside_upset_talk a_bed_side_point
    show player od_bed_jenny_laying_dick2
    with dissolve
    jen "Você está brincando comigo?"
    jen "Por que você não està de pau duro?!"
    show jenny f_bedside_upset
    player_name "I can't help it!"
    show jenny b_bed_side_laptop a_bed_side_laptop f_bedside_laptop_sexy_talk_down with dissolve
    jen "{b}*Suspiro*{/b} Apenas me de um segundo pessoal..."
    show jenny b_bed_side a_bed_side_balls f_bedside_sexy_down
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick2.png"
    with dissolve
    player_name "!!!"
    pause
    show jenny f_bedside_sexy_talk_down
    jen "Vamos lá, cara grande ... É hora de sair e jogar!"
    show jenny f_bedside_sexy_down with None
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick2.png"
    show player od_bed_jenny_laying_dick4
    with dissolve
    show player od_bed_jenny_laying_dick5 with dissolve
    show player od_bed_jenny_laying_dick6 with dissolve
    pause
    show jenny b_bed_side_laptop a_bed_side_laptop f_bedside_laptop_sexy_talk_down with dissolve
    jen "Veja, eu disse a vocês que vocês não ficariam desapontados."
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Eu sei direito!"
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Hehe, vocês devem saber agora, eu não iria me contentar com nada menos..."
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Então, o que devo fazer a seguir?"
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Não, eu não penso assim."
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Mmm, nah..."
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Oh meu deus, de jeito nenhum Sam9..."
    jen "É a primeira vez dele na frente da câmera porra!"
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Sim, ok..."
    jen "Eu posso fazer isso."
    jen "Assim que eu vejo algumas dicas, é claro."
    show jenny f_bedside_laptop_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    pause
    show jenny b_bed_side f_bedside_normal_talk with dissolve
    jen "Parece que é o seu dia de sorte..."
    $ M_jenny.set("sex speed",0.4)
    show jenny a_bed_side_jerk f_bedside_sexy_down
    player_name "!!!" with hpunch
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    player_name "Puta merda!"
    show jenny f_bedside_laugh
    jen "Hehe!"
    show jenny f_bedside_sexy_down
    pause
    player_name "Isso é incrível!"
    show jenny f_bedside_sexy_talk_down
    jen "Duh."
    jen "O que, você acha que eu não sei o que estou fazendo?"
    show jenny f_bedside_sexy_down
    pause
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg" with None
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .1)
    show jenny_hj_mc
    show expression AnimatedImage("jenny_hj", [1,2,3,4,5,4,3,2], M_jenny) as jenny_hj at Position(xalign = 0.0, yoffset = 0)
    jen "Espero que vocês gostem de me ver acariciar esse GRANDE..."
    jen "CARNUDO..."
    "{b}*PING*{/b} {b}*PING*{/b}"
    jen "PÊNIS."
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jump jenny_hj_loop

label button_jenny_come_back_camshow:
    show player 10 at left
    player_name "Então, sobre aquele camshow comigo..."
    show player 5
    show jenny f_upset_talk
    jen "Eu te disse que tenho que promover primeiro."
    jen "{b}Volte amanhã a tarde{/b}, modelo!"
    hide player
    hide jenny
    with dissolve
    return

label jenny_button_bought_mask:
    scene expression player.location.background_closeup with None
    show player 13 at left
    show jenny f_upset_talk
    with dissolve
    jen "Você entendeu?"
    show jenny f_upset
    show player 14
    player_name "Sim."
    show player 239_240 with dissolve
    pause
    show player 736b with dissolve
    player_name "O que você acha?"
    show player 13
    show jenny f_gross_down_talk a_dressed_mask
    with dissolve
    jen "É rosa."
    show jenny f_gross_down
    show player 14
    player_name "Bem eu?"
    show player 13
    show jenny f_upset_talk
    jen "Meio feminino, você não acha?"
    show jenny f_upset
    show player 10
    player_name "Isso realmente importa?"
    show player 5
    show jenny f_eyeroll
    jen "Eu acho que não."
    show jenny f_upset a_dressed_mask_throw with dissolve
    show player 14
    player_name "Então quando começamos?"
    show player 13
    show jenny f_upset_talk a_dressed_hips with dissolve
    jen "Eu preciso promover um pouco primeiro."
    jen "Volte {b}amanhã à tarde{/b}, tudo bem?"
    show jenny f_upset
    show player 14
    player_name "Entendir."
    show player 13
    show jenny f_angry_talk
    jen "E é melhor você fazer um bom show!"
    jen "Eu tenho pensado muito nisto!"
    show jenny f_angry
    show player 10
    player_name "Ok."
    hide jenny with dissolve
    pause
    show player 17
    player_name "eu acho {b}Volto amanhã a tarde{/b} então..."
    hide player with dissolve
    return

label jenny_button_get_mask:
    scene expression player.location.background_closeup with None
    show player 5 at left
    show jenny f_upset_talk
    with dissolve
    jen "Você entendeu?"
    show jenny f_upset
    show player 10
    player_name "Eu entendir o que?"
    show player 5
    show jenny f_upset_talk
    jen "{b}A mascára{/b}, modelo?!"
    show jenny f_upset
    show player 10
    player_name "Oh, certo."
    show player 12
    player_name "Não, eu ainda estou trabalhando nisso."
    show player 5
    show jenny f_upset_talk
    jen "Ugh, bem sair do meu quarto então!"
    hide jenny with dissolve
    pause
    show player 4 with dissolve
    player_name "( Hmm, Eu me pergunto o que ela está planejando fazer para o público? )"
    pause
    player_name "( Eu vou ter que {b}pegar uma máscara{/b} se eu quiser descobrir... )"
    player_name "( Eu deveria {b}ir ao shopping e procurar por uma{/b}. )"
    hide player with dissolve
    return

label jenny_button_talked_to_cedric:
    if player.location == L_home_diningroom:
        scene expression game.timer.image("dining_room{}")
        show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    else:
        scene expression player.location.background_closeup with None
    show jenny f_magic_sit_stand_upset_talk b_magic_sit_stand_dressed a_magic_sit_stand_hip_spoon zorder 1
    show player b_magic_sit_stand_dressed f_magic_sit_stand_worried a_magic_sit_stand_resting zorder 1 at Position (align=(0,0))
    with dissolve
    jen "Você falou com Cedric?"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Sim."
    show player f_magic_sit_stand_worried
    pause
    player_name "..."
    show jenny f_magic_sit_stand_upset_talk
    jen "Bem?"
    jen "Por que diabos ele ainda não me ligou?!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Ele não vai ligar de volta."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Como!!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_skeptical_talk
    player_name "Ele disse, e citou, \"Eu não quero nada com essa vadia louca.\""
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk a_magic_sit_stand_crossed with dissolve
    jen "você està falando sério?"
    show jenny f_magic_sit_stand_upset
    player_name "Mmmhmm."
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "Desculpe."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_angry_talk
    jen "Bem, foda-se ele então!"
    show jenny a_magic_sit_stand_phone f_magic_sit_stand_phone_upset_talk with dissolve
    jen "Idiota idiota..."
    show jenny f_magic_sit_stand_phone_upset
    pause
    player_name "..."
    show jenny f_magic_sit_stand_angry a_magic_sit_stand_hip_spoon with dissolve
    jen "Grr!!!"
    hide jenny with dissolve
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "... Ok."
    show player f_magic_sit_stand_worried
    player_name "( Eu deveria deixar ela sozinha até ela se acalmar... )"
    hide player with dissolve
    $ M_jenny.set('sentar', 0)
    return

label button_jenny_talk_to_cedric:
    show player 10 at left
    player_name "Onde você disse que eu poderia encontrar {b}Cedric{/b}?"
    show player 5
    show jenny f_upset_talk
    jen "Ele provavelmente estará {b}no ginásio{/b}."
    jen "Essa cabeça de carne está sempre {b}no ginásio{/b}."
    show jenny f_upset
    show player 10
    player_name "Tudo bem, estou nisso."
    hide player
    hide jenny
    with dissolve
    return

label button_jenny_has_toy_electroclit:
    scene expression player.location.background_closeup with None
    show player 14 at left
    show jenny
    with dissolve
    player_name "Eu tenho o seu brinquedo."
    show player 13
    show jenny f_upset_talk
    jen "Já estava na hora!"
    show jenny f_upset
    show player 239_240 with dissolve
    pause
    show player 287 with dissolve
    player_name "É isso, certo?"
    show jenny f_upset_talk
    jen "Deixe-me ver isso!"
    return

label button_jenny_has_toy_electroclit_submissive:
    show player 11
    show jenny f_gross_down a_dressed_hips_toy2
    with dissolve
    jen "..."
    show jenny f_angry_talk
    jen "Esta é uma Electro Clit Light!"
    show jenny f_angry
    show player 10
    player_name "Isso é uma coisa ruim?"
    show player 5
    show jenny f_angry_talk
    jen "Sim, é uma coisa ruim!"
    jen "Quão estúpido é você?"
    show jenny f_angry
    show player 10
    player_name "Eu não sou"
    show player 5
    show jenny f_angry_talk
    jen "Não tem como essa coisa nunca vai me tocar!"
    jen "Por que você não me deu o modelo original, seu idiota?!"
    show jenny f_angry
    show player 24
    player_name "Eles estavam esgotados..."
    show jenny f_upset_talk
    jen "Okay, certo. Claro que eles estavam."
    show jenny f_angry
    show player 12
    player_name "Estou falando sério!"
    show player 90
    show jenny f_upset_talk a_dressed_crossed with dissolve
    jen "Estou pensando, o acordo está fechado..."
    show jenny f_upset
    show player 10
    player_name "O que?! Vamos lá {b}[jen_name]{/b}, Eu gastei um bom dinheiro nisso!"
    show player 5
    show jenny f_upset_talk
    jen "Isso não é problema meu."
    show jenny f_upset
    show player 10
    player_name "Por favor?"
    show player 40 with dissolve
    show jenny f_surprised
    jen "!!!"
    show jenny f_grin_talk
    jen "Ah, eu gosto disso ... Me implore um pouco mais!"
    show jenny f_grin
    show player 10 with dissolve
    player_name "A sério?"
    show player 5
    show jenny f_grin_talk
    jen "Implore ou o acordo está cancelado."
    show jenny f_grin
    show player 40 with dissolve
    player_name "{b}*Suspiro*{/b} Por favor, posso te ver nua?"
    show jenny f_grin_talk
    jen "Você tem que dizer, \"Eu sou um patético perdedor e serei um virgem para sempre.\""
    show jenny f_grin
    show player 12
    player_name "O que?! eu não vou"
    show player 11
    show jenny f_angry_talk
    jen "Faça isso ou saia!"
    show jenny f_angry
    show player 24
    player_name "..."
    show player 40 with dissolve
    player_name "Eu sou um patético perdedor e serei um virgem para sempre."
    show jenny f_laugh
    jen "Hahahahaha!"
    show player 24 with dissolve
    show jenny f_grin_talk
    jen "Tudo bem, contanto que você admita."
    jen "Eu acho que você ganhou um deleite."
    show jenny f_upset_talk b_pull1 a_empty with dissolve
    show player 13
    jen "Você só está procurando por um minuto!"
    show jenny b_pull2 f_empty with dissolve
    jen "Trazendo-me este pedaço idiota de brinquedo..."
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show jenny b_naked a_naked_panties_remove f_normal_low with dissolve
    pause
    show jenny b_naked_panties_remove_down a_empty f_empty with dissolve
    pause
    show jenny f_grin_talk a_naked_hips b_naked with dissolve
    jen "Lá vai você, pervertido."
    show jenny f_grin
    show player 428
    player_name "!!!"
    show jenny f_upset_talk
    jen "Tente não babar no meu tapete."
    show jenny f_gross
    show player 429
    player_name "Uau, você barbeia lá..."
    show player 426
    show jenny f_upset_talk
    jen "Não merda"
    jen "Apenas velhas senhoras e perdedores deixavam suas coisas crescerem."
    show jenny f_upset
    pause
    show jenny f_grin_talk
    jen "Esta é a primeira vagina que você já viu?"
    show jenny f_grin
    show player 29 with dissolve
    player_name "Bem, na verdade eu"
    show player 3
    show jenny f_eyeroll
    jen "Sim, claro que é. Que pergunta idiota de perguntar."
    show jenny f_grin_talk
    show player 426 with dissolve
    jen "Provavelmente será a última que você vai ver"
    jen "Fracassado."
    show jenny f_grin
    pause
    show jenny f_upset_talk
    jen "Tudo bem, acabou o tempo"
    show jenny f_upset
    show player 427
    player_name "Aww, vamos {b}[jen_name]{/b}... Só um pouco mais!"
    show player 427g
    show jenny f_angry_talk
    jen "Não!"
    show jenny f_upset_talk
    jen "Aperte os parafusos como se você não precisasse pedir mais!"
    jen "Da próxima vez, faça exatamente o que eu disser!"
    show jenny f_upset
    show player 427
    player_name "{b}*Suspiro*{/b} bem."
    show player 426
    show jenny f_angry_talk
    jen "Agora saia!"
    hide player
    hide jenny
    with dissolve
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 12 with dissolve
    player_name "( caralho,foi humilhante... )"
    show player 17
    player_name "( Eu tenho que vê-la nua embora. )"
    show player 401
    player_name "( Então, acho que valeu a pena? )"
    show player 403
    pause
    player_name "( Eu me pergunto o que ela está planejando fazer por dinheiro agora? )"
    hide player with dissolve
    return

label button_jenny_has_toy_electroclit_dominant:
    show jenny a_dressed_hips_asking f_upset
    show player 733b
    with dissolve
    player_name "Ah, ah!"
    player_name "Nós tivemos um acordo, lembra?"
    show player 733
    show jenny a_dressed_hips f_angry with dissolve
    jen "..."
    show player 733b
    player_name "Você está um pouco vestida, não acha?"
    show player 733
    show jenny f_eyeroll
    jen "{b}*Suspiro*{/b} bem."
    show jenny b_pull1 a_empty f_grin_down with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show player 733c
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show jenny b_naked a_naked_panties_remove f_grin_down with dissolve
    pause
    show jenny b_naked_panties_remove_down f_empty a_empty with dissolve
    pause
    show jenny b_naked f_upset_talk a_naked_hips with dissolve
    jen "Lá."
    jen "Agora deixe-me ver isso!"
    show jenny f_upset
    show player 733b
    player_name "Tudo bem, aqui está seu brinquedo."
    show jenny f_gross_down a_naked_hips_toy2
    show player 426
    with dissolve
    pause
    show jenny f_gross_down_talk
    jen "Ei, esta é a versão light..."
    show jenny f_angry_talk
    jen "Eu queria o original!"
    show jenny f_angry
    show player 429
    player_name "Desculpe, esse é o único que eles tinham."
    show player 426
    show jenny f_angry_talk
    jen "Bem, que porra {b}[firstname]{/b}!"
    jen "Essa coisa nunca vai me tocar!"
    show jenny f_angry
    show player 429
    player_name "Como eu disse, é a única coisa que eles tinham."
    player_name "Confie em mim, você tem sorte de estar recebendo isso."
    player_name "Eu tive que pular alguns aros para colocar minhas mãos nele."
    player_name "Agora pare de reclamar, você está arruinando isso pra mim!"
    show player 426
    show jenny f_eyeroll
    jen "Ugh, tanto faz..."
    show jenny f_upset a_naked_hips with dissolve
    show player 429
    player_name "Eu gosto de ver você depilada..."
    show player 426
    show jenny f_happy_talk_down
    jen "Você gosta?"
    show jenny f_angry_talk
    jen "Quero dizer, cale a boca!"
    jen "Eu não me importo com o que você gosta, perdedor!"
    show jenny f_angry_pouting
    show player 429
    player_name "Se você diz..."
    show player 426
    pause
    show player 83c with dissolve
    show jenny f_surprised_down_talk
    jen "!!!"
    jen "É nossa"
    show jenny f_surprised_down
    player_name "Hmm?"
    show player 83b
    player_name "Oh, desculpe."
    player_name "Eu não estou acostumado a"
    player_name "Bem, você é muito gostosa, sabe?"
    show player 83c
    show jenny f_surprised_down_talk
    jen "Isso não pode ser seu pau..."
    show jenny f_surprised_down
    show player 83b
    player_name "Uhh, Sim?"
    show player 83c
    show jenny f_upset_talk
    jen "De jeito nenhum!"
    jen "E hum"
    show jenny f_surprised_back a_naked_shocked with dissolve
    pause
    show player 83b
    player_name "É o que?"
    show player 83c
    show jenny f_angry_talk a_naked_hips with dissolve
    jen "Nada."
    jen "Nós terminamos aqui?"
    show jenny f_angry
    show player 83b
    player_name "Sim, acho que é bom o suficiente."
    show player 83c
    show jenny f_eyeroll
    jen "Graças a Deus."
    show jenny f_upset
    show player 83
    player_name "Está corando?"
    show player 83c
    show jenny f_angry_talk
    jen "Não!"
    jen "Saia!"
    show jenny f_angry
    show player 83b
    player_name "Sim, sim ... estou indo."
    show player 83c
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 83c with dissolve
    player_name "( Bem, isso foi quente! )"
    player_name "( Ela realmente parece me responder quando sou severo com ela e não a aceito. )"
    pause
    player_name "( Eu me pergunto o que ela está planejando por dinheiro? )"
    hide player with dissolve
    return

label button_jenny_get_toy_electroclit:
    show player 10 at left
    player_name "Que brinquedo você queria que eu pegasse de novo?"
    show player 5
    show jenny f_upset_talk
    jen "Você esqueceu ou algo assim?!"
    show jenny f_upset
    show player 10
    player_name "não, eu não fiz por"
    show player 5
    pause
    show player 12
    player_name "Ugh, jdiga-me!"
    show player 5
    show jenny f_upset_talk
    jen "Você é inútil, você sabe disso?"
    show jenny f_gross
    pause
    show jenny f_upset_talk
    jen "Vá para{b} Rosa{/b} no {b}segundo andar {/b} do {b}shopping {/b}e procure pelo {b}Electro Clit {/b}."
    show jenny f_upset
    show player 10
    player_name "Tudo bem."
    show player 5
    show jenny f_upset_talk
    jen "Preciso escrever de trás na sua testa para que você não se esqueça de novo?"
    show jenny f_upset
    show player 12
    player_name "Não, eu entendir desta vez."
    show player 5
    show jenny f_eyeroll
    jen "Sim certo."
    show jenny f_upset
    return

label jenny_dialogue_make_a_deal:
    menu:
        "Mamas.":
            if M_jenny.get("dominance") <= 0:
                show player 10 at left
                player_name "Posso ver seus peitos?"
                show player 5
                show jenny f_upset_talk
                jen "Eu não sei, você tem duzentos dólares?"
                show jenny f_upset
                if player.has_money(200):
                    show player 14
                    player_name "Sim."
                    show player 13
                    show jenny f_eyeroll
                    jen "{b}*Suspiro*{/b} Tudo bem, entregue-me."
                    show jenny f_upset
                    show player 41 with dissolve
                    pause
                    show player 13
                    show jenny f_grin_down a_dressed_money_counting
                    with dissolve
                    pause
                    show jenny f_upset_talk
                    $ player.spend_money(200)
                    jump repeat_boobies
                else:
                    jump player_no_money
            else:
                show player 10 at left
                player_name "Posso ver seus peitos?"
                show player 5
                show jenny f_upset_talk
                jen "Eu não sei, você tem duzentos dólares?"
                show jenny f_upset
                if player.has_money(200):
                    $ player.spend_money(200)
                    show player 10
                    player_name "Sim."
                    show player 5
                    show jenny f_upset_talk
                    jen "{b}*Sigh*{/b} Tudo bem, entregue-me."
                    show jenny f_upset
                    jump jenny_bedroom_jenny_go_to_her_room_dominant_has_money
                else:
                    show player 10
                    player_name "Eu não tenho duzentos!"
                    show player 5
                    show jenny f_upset_talk
                    jen "Bem, eu não estou mostrando meus peitos para nada menos que duzentos."
                    jen "Então é melhor você ir buscá-lo se quiser dar uma olhada nessas coisas..."
                    show jenny f_upset
                    show player 24
                    player_name "{b}*Suspiro*{/b} tudo bem."
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
        "Deixa pra lá.":
            label player_no_money:
            show player 10 at left
            player_name "Deixa pra lá."
            show player 5
            show jenny f_upset_talk
            jen "Pare de brincar, {b}[firstname]{/b}!"
            jen "Se você não tem dinheiro, saia."
            show jenny f_upset
            show player 12
            player_name "Tudo bem."
            hide player
            hide jenny
            with dissolve
    return

label jenny_dialogue_roxxy_pre:
    show player f_worried_talk
    player_name "Então sobre {b}Roxxy's{/b} rotina..."
    show player f_worried
    show jenny f_upset_talk
    jen "Você trouxe o dinheiro?"
    show jenny f_upset
    return

label jenny_dialogue_roxxy_pay:
    show player f_skeptical_talk
    player_name "Aqui."
    show player 41 at Position (xoffset=-130) with dissolve
    pause
    if M_jenny.pregnancy.stage > 1:
        show jenny f_grin_talk
    else:
        show jenny f_grin_talk a_money with dissolve
    jen "Perfeito."
    jen "Diga ela, pode vir me ver depois da aula amanhã."
    show jenny f_grin
    show player f_skeptical_talk with dissolve
    player_name "O nome dela é {b}Roxxy{/b}."
    show player f_worried
    show jenny f_gross_talk
    jen "Tanto faz."
    return

label jenny_dialogue_roxxy_do_not_pay:
    show player f_worried_talk
    player_name "Ainda não tenho."
    show player f_worried
    show jenny f_upset_talk
    jen "Bem, então vaza, estou ocupada."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
