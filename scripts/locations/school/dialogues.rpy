label school_diane_delivery_3:
    scene school
    show player 166 at left with dissolve
    player_name "Ufa, quase lá..."
    show player 168b
    ann "SEGURE BEM LÁ!" with hpunch
    show player 168c
    player_name "Hmm?"
    show player 168b
    show annie 5 at right with dissolve
    ann "Onde você acha que vai com todo esse leite?"
    show annie 6
    show player 168
    player_name "Ei {b}Annie{/b}."
    player_name "Eu devo entregar isso na cafeteria."
    show player 167
    show annie 5
    ann "Acho que não."
    show annie 6
    show player 166
    player_name "O que? Por que?"
    show player 165
    show annie 5
    ann "{b}Sra. Smith{/b} Não disse nada para mim sobre uma entrega de leite hoje."
    show annie 6
    show player 166
    player_name "... assim?"
    player_name "Tenho certeza {b}Sra. Smith{/b} não fala sobre cada pequena coisa que está acontecendo na escola..."
    show player 165
    show annie 3
    ann "Uhh, sim, ela faz."
    ann "Eu sou seu segundo em comando."
    show annie 1
    player_name "..."
    show player 166
    player_name "Veja {b}Annie{/b}, isso é muito pesado. Você pode por favor sair do meu caminho?"
    player_name "Tenho certeza que é para ir ao refeitório."
    show player 165
    show annie 4
    ann "Eu disse não!"
    ann "Não até eu limpar com {b}Sra. Smith{/b}."
    show annie 1
    player_name "..."
    show annie 3
    ann "Vamos lá, ela está no escritório dela."
    hide annie with dissolve
    show player 166
    player_name "{b}Seu escritório no terceiro andar?!{/b}"
    player_name "Você pode pelo menos me ajudar a carregar isso?"
    show player 165
    ann "Não!"
    pause
    show player 168c
    player_name "{b}*Suspiro*{/b}"
    hide player with dissolve
    return

label school_erik_intro_started:
    scene outside_school_b
    show duo 6 at left with dissolve
    show mia 1 at right with dissolve
    player_name "Ei, {b}Mia{/b}!"
    show duo 1 at left
    show mia 4 at right
    mia "Ei, {b}[firstname]{/b}! Fico feliz em ver que você está de volta!"
    mia "Ei, {b}Erik{/b}! Como foi o seu final de semana?"
    show duo 10 at left
    show mia 1 at right
    eri "Eu fiquei principalmente no meu quarto..."
    show duo 1 at left
    show mia 3 at right
    mia "Isso é legal. Às vezes eu gosto de passar o tempo sozinha também!"
    show mia 4 at right
    mia "E você, {b}[firstname]{/b}? O que você tem feito?"
    show mia 2 at right
    show duo 9 at left
    player_name "Bem, eu não tenho certeza se você ouviu ou não, mas meu {b}pai{/b} faleceu. Então eu tenho lidado com isso..."
    show mia 6 at right
    mia "Ah sim. Eu ouvi da minha mãe..."
    show duo 15 at left
    mia "Eu não queria mencionar isso. Me desculpe, você teve que passar por isso. Estou feliz que você esteja de volta!"
    show mia 2 at right
    player_name "Obrigado. Eu vou ficar bem. Não se preocupe."
    show mia 4 at right
    mia "Ouça, eu estava procurando alguém para {b} me ajudar a se preparar para os exames finais{/b}, então..."
    show duo 7 at left
    mia "... Se você estiver interessado, me avise!"
    show duo 8 at left
    show mia 1 at right
    player_name "Uhh, claro ... eu acho?"
    player_name "Onde você quer se encontrar? A biblioteca?"
    show duo 1
    show mia 6
    mia "Umm, Eu teria que perguntar aos meus pais, primeiro."
    mia "Eles provavelmente não vão me deixar ir."
    mia "Eu não estou autorizada a ficar até tarde depois da escola ou ver amigos fora da minha casa."
    show mia 2
    show duo 9
    player_name "Mesmo?! Isso é uma merda!"
    show duo 7
    show mia 3
    mia "Sim... hehe, hehe."
    show duo 7
    show mia 6
    mia "De qualquer forma, seria mais fácil se você viesse até minha casa para estudar..."
    show mia 3 at right
    mia "Você sabe onde eu moro, por isso, basta ir quando quiser!"
    show duo 7 at left
    show mia 4 at right
    mia "É melhor eu ir embora. {b}Aula de ciências{/b} está começando em breve!"
    show duo 1
    mia "{b}A professora Okita{/b} disse que a experiência de laboratório {b}de hoje{/b} será desafiadora."
    mia "Isso significa que provavelmente vai levar horas para ser concluída."
    show mia 1
    show duo 10
    eri "Ugh. Não me lembre..."
    show duo 1
    show mia 4
    mia "Falo com vocês depois pessoal!"
    hide mia with dissolve
    hide duo with dissolve
    return

label school_roxxy_shower_event:
    scene school
    show jersey 10 with dissolve
    player_name "( Woah! é difícil respirar! )"
    player_name "( É tão quente aqui... )"
    show jersey 33 at Position(xoffset=22) with fastdissolve
    player_name "( ... Eu estou todo suado! )"
    player_name "( Eu deveria {b}tomar banho{/b} antes de ir para a minha próxima aula. )"
    return

label school_roxxy_intense_gymercise:
    scene school
    show erik 28 at right
    show player 1 at left
    with dissolve
    eri "Ei, {b}[firstname]{/b}."
    show erik 27
    show player 14
    player_name "Ei, {b}Erik{/b}."
    player_name "Por que você está vestindo suas roupas de ginástica?"
    show erik 28
    show player 11
    eri "{b}Treinadora Bridget{/b} quer falar com você!"
    eri "Ela está esperando na pista."
    show erik 27
    show player 10
    player_name "Porra, é provavelmente sobre todo o treinamento que eu perdi ... Ela vai me matar!"
    show erik 28
    show player 5
    eri "Melhor se apressar!"
    show erik 27
    show player 10
    player_name "Sim, obrigado por me avisar, cara!"
    show erik 29
    show player 11
    eri "Sem problema cara!"
    show erik 27
    hide player with dissolve
    pause
    show erik 28
    eri "Boa sorte!"
    hide erik with dissolve
    return

label school_bissette_challenge:
    scene school
    show player 34 with dissolve
    player_name "( Eu deveria  {b}falar com Miss Bissette sobre essa aula particular{/b}. )"
    player_name "( Eu não consigo entender nada do material em sala de aula... )"
    player_name "( ...Eu acho que estou muito atrasado para me recuperar sozinho. )"
    player_name "( Um pouco de ajuda extra não seria ruim certo... )"
    show player 4 at Position (xoffset=5) with dissolve
    player_name "( ...E eu posso receber essa recompensa se eu fizer bem no teste final! )"
    hide player with dissolve
    return

label school_mia_glasses_favor:
    scene school
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia "Ei, {b}[firstname]{/b}."
    show mia 7
    show player 14
    player_name "Ei, {b}Mia{/b}."
    show player 12
    player_name "Como está seu pai?"
    show player 5
    show mia 10
    mia "Ele está bem. eu acho que..."
    show mia 51 with dissolve
    mia "Minha mãe estava limpando seu escritório ontem à noite e encontrou esses óculos velhos..."
    show mia 7
    show player 446
    with dissolve
    pause
    show player 448
    player_name "Legal de Aviadores!"
    player_name "Ele ainda usa?"
    show player 13
    show mia 50
    with dissolve
    mia "Ele costumava, mas isso foi há muito tempo."
    mia "Eu estava pensando que talvez ele gostaria de usá-los novamente."
    show mia 50b
    show player 14
    player_name "Isso é bom."
    show player 13
    show mia 50
    mia "Na verdade, eu queria saber se você poderia deixá-lo no trabalho dele?"
    mia "Eu tenho que estar em algum lugar mais tarde e não terei tempo para entregar sozinha."
    show mia 50b
    show player 10
    player_name "Hã? Você quer que {b}eu{/b} vá?"
    show player 5
    show mia 50
    mia "Por que não?"
    mia "Vocês dois parecem estar se dando tão bem..."
    mia "...E ele ficaria feliz em vê-lo novamente, tenho certeza!"
    mia "Desde que você falou com ele, ele está se saindo muito melhor."
    show mia 50b
    show player 12
    player_name "Ehh... Sim, suponho que poderia deixá-lo no trabalho dele."
    show player 447
    show mia 10
    with dissolve
    mia "Obrigada, é muito gentil de sua parte fazer isso por mim."
    show mia 7
    show player 448
    player_name "Não tem problema, não me importo de visitá-lo."
    show player 447
    show mia 10
    mia "Até mais tarde então!"
    show mia 7
    show player 448
    player_name "Thau."
    show unlock54 at truecenter with dissolve
    pause
    hide unlock54 with dissolve
    hide player
    hide mia
    with dissolve
    return

label school_erik_bullying_2_started:
    scene school
    show dexter 9 at right with dissolve
    eri "Ugh!!"
    eri "Me deixar ir... {b}Dexter{/b}!"
    dex "Sem chance, gordinho."
    dex "Você ainda não me deu sua lição de casa."
    dex "Eu acho que você não recebeu a mensagem."
    eri "Eu te disse! Eu já entreguei! Eu não tenho mais isso!"
    dex "Pois bem, acho que você vai ter que me dar outra coisa..."
    dex "Quanto dinheiro você tem ?"
    eri "O que?!"
    dex "Eu disse, quanto dinheiro você vai me dar, Antes de eu enfiar seu rosto em um armário!!"
    eri "!!!"
    eri "{b}Dexter{/b}! Eu... Eu..."
    show player 15 at left with dissolve
    show dexter 10
    player_name "EI!!!"
    player_name "Deixe-o em paz, {b}Dexter{/b}!"
    show player 16
    show dexter 9
    dex "Olha, se não é seu amigo perdedor."
    show dexter 10
    show player 15
    player_name "{b}Dexter{/b}, pare de mexer com {b}Erik{/b}."
    show player 16
    show dexter 9
    dex "Por quê? Você gostaria de ficar no lugar dele?"
    player_name "..."
    show dexter 12 with dissolve
    dex "Passo acima, {b}[firstname]{/b}."
    show dexter 13
    dex "Vamos ver o que você tem!"
    return

label school_erik_bullying_2_started_dex_pass:
    show dexter 14
    show player 387 with dissolve
    player_name "Eu não tenho medo de você {b}Dexter{/b}!"
    show player 388
    show dexter 15
    dex "Bem, você deveria estar com medo ... ESTÁ!"
    hide player
    hide dexter
    show dexter 16 at left
    with dissolve
    pause
    show dexter 17 at right with dissolve
    player_name "Haiii!!"
    hide dexter
    show player 390 at left
    show dexter 18 at right
    with dissolve
    dex "Arghh!!"
    dex "Você ... seu pequeno ... merda..."
    show dexter 15 with dissolve
    show player 389
    player_name "!!!"
    show player 391
    show dexter 19 with hpunch
    pause
    hide player
    show dexter 20 at left
    with dissolve
    dex "Não tão rápido desta vez, né?!"
    dex "eu vou te mostrar..."
    hide player
    with dissolve

    scene school_fight_cs1 with fade
    show text "Mesmo depois de todos os meus treinamentos recentes na academia,\n{b}Dexter{/b} ainda era forte demais para mim...\n...mas eu sei agora que posso machucá-lo..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text

    scene school_fight_cs2 with fade
    show text "...E então tudo ficou escuro." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text

    scene black with fade
    pause

    scene school with None
    show mia 24 at left
    show dexter 21 at Position (xpos=713)
    with dissolve
    mia "{b}[firstname]{/b}!! Você está bem?!"
    show mia 23
    pause
    show mia 28 with dissolve
    mia "Qual é o seu problema, {b}Dexter{/b}?"
    mia "Você realmente o machucou!"
    show mia 27
    show dexter 22
    dex "Não é da tua conta!"
    dex "Ele que se intrometeu onde não devia!!"
    show dexter 23
    show roxxy 30 at right with dissolve
    rox "{b}Dexter{/b}?"
    show roxxy 29
    show dexter 24
    dex "O que?!"
    show dexter 23
    show mia 23 with dissolve
    show roxxy 27
    rox "..."
    show roxxy 28
    rox "Umm.... {b}Dexter{/b}, o que está acontecendo?"
    rox "Você fez isso?"
    show roxxy 29
    show mia 27 with dissolve
    show dexter 24
    dex "Nada está acontecendo!!"
    show dexter 12
    dex "Acabei de terminar de ensinar esta merda uma lição."
    show dexter 23
    show roxxy 30
    rox "Mesmo? Você tinha que fazer isso agora? No corredor?"
    show roxxy 29
    show dexter 24
    dex "Cale-se, {b}Roxxy{/b}."
    dex "Vamos. Vamos sair daqui!"
    show roxxy 27
    dex "Eu tenho coisas melhores para fazer do que assistir a um monte de idiotas por aí."
    hide dexter
    hide roxxy
    with dissolve
    hide mia
    show eve 9 at Position (xpos=75)
    show mia 23 at left
    show judith 40 at Position (xpos=600)
    show erik 50 at Position (xpos=900)
    with dissolve
    jud "Oh meu deus! O que aconteceu?!"
    show judith 41
    show eve 10
    eve "{b}Dexter{/b} é um idiota."
    eve "Ele foi longe demais desta vez."
    show eve 9
    hide erik
    show teacher 15 at Position (xpos=700)
    show erik 50 at Position (xpos=900)
    with dissolve
    bis "!!!"
    bis "O que está acontecendo aqui?"
    bis "O que há de errado com {b}[firstname]{/b}?"
    show teacher 14
    show mia 26 with dissolve
    mia "Ele entrou em uma briga com {b}Dexter{/b} e {b}Dexter{/b} bateu nos armários."
    mia "Ele ainda está respirando. Eu espero que ele esteja bem."
    show mia 25
    bis "..."
    show teacher 15
    bis "Nós deveríamos chamar a ambulância!"
    $ playSound()
    scene black with fade
    hide mia
    hide eve
    hide teacher
    hide erik
    hide judith
    return

label school_erik_bullying_2_started_dex_fail:
    show dexter 14 at right with dissolve
    show player 6 at left with dissolve
    player_name "[dex_warn]Não quero brigar com você {b}Dexter{/b}!"
    show player 23 with dissolve
    player_name "[dex_warn]Eu só quero que você deixa o {b}Erik{/b} em paz..."
    show player 22
    show dexter 15
    dex "Serio?"
    show dexter 14
    show player 10
    player_name "[dex_warn]Isso é tudo..."
    show player 22
    show dexter 12 with dissolve
    dex "Hã!"
    dex "Você e Fraco e patético..."
    dex "...Assim como seu pai!"
    hide dexter
    with dissolve
    show player 24
    player_name "[dex_warn]..."
    hide player
    with dissolve
    return

label school_roxxy_intro_started:
    scene school with fade
    show duo 1 at left
    show dexter 1 at Position (xpos=700)
    show roxxy 4 at right
    with dissolve
    rox "... Então {b}Becca{/b} jogou seu retentor no banheiro!"
    show dexter 3
    dex "Bahahahahahah!"
    show roxxy 3d
    rox "..."
    show roxxy 3c
    rox "... Ugh, O que vocês dois perdedores estão olhando?!"
    show dexter 2 at Position (xoffset=-2)
    show roxxy 3b
    show duo 2 at left
    eri "Eu acho que nós estamos olhando para o QI combinado de 2."
    show duo 3 at left
    player_name "HA HA HA HA!!"
    show roxxy 31
    rox "Como?!"
    show roxxy 3b
    show dexter 8 at Position (xoffset=-2)
    dex "... Eu não entendi?"
    show dexter 2 at Position (xoffset=-2)
    show duo 7 at left
    show roxxy 30
    rox "Eles estão nos chamando de idiotas..."
    show roxxy 29
    show dexter 8 at Position (xoffset=-2)
    dex "Eles estão?!"
    show dexter 6 at Position (xoffset=-119) with dissolve
    dex "Ei! Você está nos chamando de idiota?!"
    show dexter 5 at Position (xoffset=-119)
    show duo 10
    show roxxy 3b
    eri "Eu ... Não, eu não ... quero dizer, eu não faria..."
    show duo 11
    show dexter 4 at Position (xoffset=-20) with dissolve
    dex "Porque eu vou esmagar seu rosto, seu merda!"
    show duo 4
    show dexter 2 at Position (xoffset=-2) with dissolve
    show roxxy 3
    rox "...E por que {b}VOCÊ ESTAVA{/b} rindo?"
    show roxxy 2
    rox "O perdedor do seu pai, Não se matou ou algo assim?"
    show roxxy 1g
    show duo 9
    eri "..."
    show player 15 at left
    player_name "Pelo menos eu {b}tive{/b} um pai..."
    player_name "... E eu não moro em um {b}TRAILER{/b}!!"
    show player 16
    show roxxy 3c
    rox "!!!" with hpunch
    show roxxy 3
    rox "... Você está morto!"
    rox "Dexter, pega ele!!!"
    show roxxy 3d
    show player 11
    show dexter 8 at Position (xoffset=-2)
    dex "Espere, {b}Roxxy{/b}. {b}Diretora Smith{/b} está vindo..."
    dex "Se eu for pego lutando novamente, {b}Treinadora Bridget{/b} disse que vai me expulsar da equipe."
    hide dexter with dissolve
    show roxxy 3c
    show player 16
    rox "Pfft, Está bem..."
    show roxxy 3
    rox "... Isso não acabou, {b}[firstname]{/b}!"
    rox "Eu vou lidar com você mais tarde!"
    hide roxxy with dissolve
    pause
    hide player
    show duo 1 at left
    show principal 5 at right with dissolve
    smi "Vocês dois! Venha pra cá, {b}AGORA MESMO{/b}!!!"
    show duo 11 at left
    smi "O que você ainda está fazendo no maldito corredor??!"
    show duo 12 at left
    show principal 3 at right
    eri "Desculpe, {b}Diretora Smith{/b}! Nós estamos conversando!"
    show duo 11 at left
    show principal 4 at right
    smi "Ah, {b}[firstname]{/b}! Finalmente retornou para nós vejo..."
    show duo 6
    show principal 1 at Position(xpos=0.935, ypos=1.0)
    player_name "Sim, senhora."
    show duo 7
    show principal 27
    smi "Bem, está na hora! Você tem alguma idéia de quanto suas notas caíram?!"
    show duo 9
    show principal 1
    player_name "... Eles têm?"
    show duo 10
    eri "Isso não parece justo!"
    eri "Você não conhece o pai dele?"
    show duo 11
    show principal 2
    smi "Isso é o bastante, jovem!"
    show principal 4 at right
    smi "Eu sugiro que você pegue sua bunda para a aula antes de encontrá-lo sentado em detenção!"
    show duo 10
    show principal 1 at Position(xpos=0.935, ypos=1.0)
    eri "..."
    show duo 12
    show principal 4 at right
    smi "... E quanto a você {b}[firstname]{/b}. Precisamos discutir suas notas fracassadas!"
    smi "Eu quero você no andar de cima, no meu escritório, imediatamente!"
    show duo 9
    show principal 1 at Position(xpos=0.935, ypos=1.0)
    player_name "Sim, {b}Diretora Smith{/b}."

    hide principal
    hide duo
    with dissolve
    show player 5 at left
    show erik 3b at right
    eri "Cara, ela é pura maldade..."
    show player 2
    show erik 1
    player_name "Ah, Sim."
    show player 1
    show erik 5
    eri "Estou falando sério! Ela é como a Evil Ice Queen da Whorecraft!"
    show player 2
    show erik 1
    player_name "Bem, {b}É melhor eu ir até o escritório dela{/b} antes de seu humor piorar."
    show player 1
    show erik 5
    eri "Boa sorte, cara..."
    show player 2
    show erik 1
    player_name "... Obrigado."
    show player 1
    show erik 4
    eri "Ah, quase me esqueci!"
    eri "{b}Eu deixei um presente no seu armário{/b}!"
    show player 2
    show erik 1
    player_name "Mesmo?"
    show player 1
    show erik 4
    eri "Fico feliz em ter você de volta, cara!"
    show player 2
    show erik 1
    player_name "Obrigado, {b}Erik{/b}!"
    show player 34
    player_name "Hmm..."
    show player 10
    player_name "... Você sabe, eu não me lembro da minha {b}combinação do cadeado{/b}."
    show player 11
    show erik 5
    eri "Você não escreveu?"
    show player 10
    show erik 1
    player_name "Não, mas eu acho que deveria, né?"
    show player 11
    show erik 5
    eri "Você provavelmente vai ter que {b}falar com a {b}Diretora Smith{/b} sobre isso{/b}."
    show player 10
    show erik 1
    player_name "Ugh, você está certo..."
    player_name "vejo você mais tarde, {b}Erik{/b}."
    show player 11
    show erik 5
    eri "Sim, até mais, {b}[firstname]{/b}."
    return

label school_hallway_dewitt_talent_show_ask_annie:
    scene school
    show player 4f with dissolve
    player_name "( Eu me pergunto com quem devo falar primeiro? )"
    show player 9f at left with dissolve
    pause
    pause
    show player 22 at left
    show annie 4 at right
    with hpunch
    ann "{b}[firstname]{/b}, pare de vadiagem no corredor!"
    show annie 1
    show player 12
    player_name "{b}Annie{/b}, Eu acabei de entrar no corredor..."
    show player 5
    show annie 5
    ann "Tanto faz. Corra para a próxima aula antes de eu te escrever!"
    show annie 6
    show player 12
    player_name "Tudo bem! Sheesh..."
    show player 10
    player_name "Oh, Ei! Espere um segundo!"
    player_name "Você não toca um instrumento ou canta?"
    show player 5
    show annie 3
    ann "Eu faço. por que?"
    show annie 1
    show player 10
    player_name "Bem, {b}Ms. Dewitt{/b} está procurando pessoas para o show de talentos."
    show player 5
    show annie 5
    ann "Sim, estou bem ciente."
    show annie 6
    player_name "..."
    show player 10
    player_name "Você gostaria de fazer parte disso?"
    show player 5
    show annie 9
    ann "Pfft, absolutamente não!"
    show annie 5
    ann "Você percebe a {b}Diretora Smith{/b} está tentando fazer com que esse show estúpido seja cancelado, certo?"
    show annie 6
    show player 12
    player_name "Sim, eu ouvi."
    show player 5
    show annie 3
    ann "Então não tem como eu participar disso!"
    show annie 1
    show player 12
    player_name "Você nem sempre tem que ouvir a {b}Diretora Smith{/b}, {b}Annie{/b}."
    show player 5
    show annie 5
    ann "Sou chefe do comitê disciplinar, monitor oficial do salão e a {b}Diretora Smith{/b} segundo no comando!"
    show annie 3
    ann "É meu dever jurado seguir suas ordens."
    show annie 1
    show player 12
    player_name "Isto não é o exército, {b}Annie{/b}..."
    show player 11
    show annie 7
    ann "SILÊNCIO!"
    show annie 1
    show player 10
    player_name "Mas"
    show player 11
    show annie 5
    ann "{b}Diretora Smith{/b} quer que o show seja cancelado e os planos foram colocados em movimento."
    show annie 6
    show player 12
    player_name "... Planos?"
    show player 5
    show annie 9
    ann "Grr, Eu falei demais."
    show annie 1
    show player 11
    player_name "..."
    show annie 5
    ann "Eu sugiro que você desista do show de talentos. Isso não vai acontecer, garanto-lhe."
    show annie 8
    ann "Agora saia do meu caminho para que eu possa terminar minha patrulha!"
    hide annie with dissolve
    show player 12
    player_name "Que trabalho maluco..."
    hide player with dissolve
    return

label school_dewitt_school_sneak_mission:
    scene expression game.timer.image("outside_school{}")
    show player 32f with dissolve
    player_name "( Onde diabos está {b}Erik{/b}? )"
    player_name "( Ele deveria estar aqui agora... )"
    show player 31f
    show erik 5 at right with dissolve
    eri "{b}[firstname]{/b}?"
    show erik 52
    show player 10 at left with dissolve
    player_name "Aí está você!"
    player_name "Por que demorou tanto?"
    show player 5
    show erik 4
    eri "Desculpe cara! Eu estava pilhando uma vila Orcette e eu meio que perdi a noção do tempo..."
    show erik 1
    show player 12
    player_name "... Hã?"
    player_name "Isso é coisa de videogame?!"
    show player 5
    show erik 5
    eri "... Sim."
    show erik 1
    show player 37 with dissolve
    player_name "..."
    show player 38 with dissolve
    player_name "Vamos apenas focar na missão, {b}Erik{/b}."
    show player 5 with dissolve
    show erik 5
    eri "Qual é a nossa missão?"
    show erik 52
    show player 239_240 with dissolve
    pause
    show player 618 at Position (xoffset=35) with dissolve
    player_name "Temos que invadir a sala da {b}Diretora Smith{/b} e aplicar isso {b}solução adesiva{/b} para as cadeiras do escritório."
    show player 617 at Position (xoffset=35)
    show erik 5
    eri "É a mesma coisa que fizemos na classe {b}Miss Okita{/b}um tempo atrás?"
    show erik 52
    show player 618 at Position (xoffset=35)
    player_name "Sim. {b}Kevin{/b} fez isso por mim."
    show player 617 at Position (xoffset=35)
    show erik 5
    eri "Essa coisa é muito forte!"
    eri "... E você quer colocar na cadeira da {b}Diretora Smith{/b}?"
    eri "Ela não vai ficar presa?"
    show erik 52
    show player 17 with dissolve
    player_name "Hehe, esse é o tipo de cara, cara."
    show player 13
    show erik 3b
    eri "Oh, certo."
    show erik 3c
    pause
    show erik 3b
    eri "Bem, liderar da maneira que eu acho..."

    scene outside_school_night02a with dissolve
    show text "A escola estava fechada, mas eu estava determinado a encontrar um ponto de entrada em algum lugar.\nTalvez uma dessas janelas do piso principal funcionasse?" at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene black with dissolve
    pause 0.5

    show outside_school_night02b with dissolve
    show text "{b}Erik{/b} não era o parceiro ideal para uma missão secreta, mas ainda assim estava feliz em tê-lo junto.\nNão há como eu ter conseguido isso sem ele." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene black with dissolve
    pause 0.5

    scene outside_school_night02c with dissolve
    show text "Como {b}Erik{/b} ajudou-me através da janela Eu não pude deixar de sentir que tudo isso tinha sido muito fácil...\n... Houve certamente algo sinistro sobre a escola hoje à noite." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    $ playMusic()
    hide text with dissolve

    scene black
    with dissolve
    pause 0.5

    scene school_night with dissolve
    player_name "!!!"
    player_name "Shh, Eu ouço algo."

    scene cult_event 1
    with Dissolve(0.3)
    eri "..."
    eri "!!!"
    scene cult_event 2
    with Dissolve(0.3)
    player_name "Shhh!"
    player_name "Fique quieto..."
    scene cult_event 3
    with Dissolve(0.3)
    window hide
    pause
    scene cult_event 4
    with Dissolve(0.3)
    scene school_night
    show player 22 at left
    show erik 51 at right
    with dissolve
    pause
    show player 10
    player_name "O que?"
    player_name "Quem era aquele?"
    player_name "... E onde eles estão indo?"
    show player 5
    show erik 53
    eri "Eu não gosto disso, {b}[firstname]{/b}!"
    eri "Nós devemos sair daqui!"
    show erik 52
    show player 10
    player_name "Acalme-se, cara."
    player_name "Eles não sabem que estamos aqui."
    show player 5
    show erik 53
    eri "O que você acha que está acontecendo com as roupas assustadoras?"
    show erik 52
    show player 10
    player_name "Não sei."
    show player 92
    player_name "Acho que devemos segui-los."
    show player 90
    show erik 53
    eri "Você é louco?!"
    show erik 52
    show player 92
    player_name "Vai ficar bem, {b}Erik{/b}!"
    player_name "Apenas fique atrás de mim e fique quieto!"
    show player 90
    show erik 2 with dissolve
    eri "{b}*Suspiro*{/b}"
    show erik 3 with dissolve
    eri "... Está bem."
    hide player
    hide erik
    with dissolve
    return

label school_dewitt_pre_talent_show_chat:
    scene school
    show kevin 23 at Position (xpos=600)
    show eve 6 at right
    with dissolve
    show player 13 at left with dissolve
    eve "Ali está ele!"
    show eve 5
    show kevin 22 with dissolve
    kev "Finalmente!"
    kev "Como tudo foi na noite passada?"
    show kevin 23 with dissolve
    show eve 2b
    eve "Nós estávamos começando a nos preocupar se você foi pego ou algo assim..."
    show eve 5
    show player 14
    player_name "Não. Tudo correu bem."
    player_name "Vocês viram {b}Diretora Smith{/b} e {b}Annie{/b} esta manhã?"
    show player 13
    show kevin 9b
    kev "Não por algum tempo."
    kev "Você acha que elas estão realmente presas em seu escritório?!"
    show kevin 23
    show player 17
    player_name "acredito que sim."
    show player 13
    show eve 6
    eve "Haha! Isso é tão incrível!"
    show eve 5
    show player 14
    player_name "Onde está a {b}Miss Dewitt{/b}?"
    show player 13
    show eve 6
    eve "Ela está no {b}Auditório{/b} preparando para o show."
    show eve 5
    show kevin 9b
    kev "Nós estávamos nos preparando para ajudá-la."
    show kevin 23
    show eve 6
    eve "Sim, por que você não vem com a gente?"
    show eve 5
    show player 14
    player_name "Hmm, Vou checar o escritorio da  {b}Diretora Smith{/b} primeiro."
    player_name "Eu quero ter certeza de que não haverá surpresas."
    show player 13
    show kevin 9b
    kev "Sim, provavelmente é uma boa ideia."
    show kevin 23
    show eve 2b
    eve "... Apenas me prometa que você será cuidadoso {b}[firstname]{/b}."
    show eve 1
    show player 17
    player_name "Eu vou."
    show player 13
    show eve 2b
    eve "Encontre-nos no {b}Auditório{/b} quando terminar."
    hide eve
    hide kevin
    hide player
    with dissolve
    return

label school_weekend_lock:
    scene expression game.timer.image("outside_school{}")
    show player 12 with dissolve
    player_name "( É {b}fim de semana{/b}. )"
    player_name "( A escola está {b}fechada{/b} até {b}Segunda-feira{/b}. )"
    hide player 12 with dissolve
    return

label night_closed_school:
    if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
        $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    scene expression game.timer.image("outside_school{}")
    if False:
        if M_erik.get("webcam help"):
            $ player.go_to(L_school_hall)
            call expression game.dialog_select("school_erik_webcam_quest")
            call expression game.dialog_select("school_erik_webcam_quest_sneak_in")

            $ game.main()
        else:

            call expression game.dialog_select("school_erik_webcam_quest_need_help")
    else:

        call expression game.dialog_select("school_closed")
    call expression game.dialog_select("map_dialogue")

label school_closed:
    show player 2 with dissolve
    player_name "( A {b}Escola{/b} Está fechado à noite ... Eu devo voltar amanhã. )"
    hide player 2 with dissolve
    return

label school_hallway:
    $ player.go_to(L_school_hall)
    $ game.main()

label school_locker_smith_go_to_locker:
    scene expression game.timer.image("school{}") with None
    show player 11f at right
    show annie 3f at Position(xpos=0.3, ypos=1.0)
    with dissolve
    ann "Tudo bem, vamos acabar com isso."
    show annie 17 with dissolve
    pause
    show annie 18 at Position(xpos=0.24, ypos=1.0) with dissolve

    show player 10f
    player_name "Uau, essa chave abre todos os armário ?"
    show player 11f
    show annie 17 at Position(xpos=0.3, ypos=1.0) with dissolve
    pause
    show annie 3f with dissolve
    ann "Pfft, esta chave abre todas as fechaduras e portas da escola."
    show player 10f
    show annie 1f
    player_name "Sério?!"
    show player 11f
    show annie 5f
    ann "Duh, é por isso que é chamado de {b}Chave mestra{/b}."
    show player 10f
    show annie 6f
    player_name "Por que você tem uma?"
    show player 11f
    show annie 5f
    ann "Umm, porque todos os dias eu ajudo a {b}Diretora Smith{/b} mantendo todas as crianças na linha!?"
    show player 12f
    show annie 6f
    player_name "Crianças? Somos da mesma idade..."
    show player 16f
    show annie 3f
    ann "... Ok, certo. Todo mundo por aqui é tão imaturo."
    show player 10f
    show annie 1f
    player_name "Então você tem a {b}Chave mestra{/b} com você o tempo todo?"
    show player 11f
    show annie 3f
    ann "Claro que não! a {b}Diretora Smith mantém em seu escritório{/b} mas nós nunca precisamos usá-lo."
    show player 10f
    show annie 1f
    player_name "Nunca?"
    show player 11f
    show annie 4f
    ann "Ninguém mais é burro o suficiente para perder sua combinação de armários..."
    show annie 3f
    ann "Apresse-se e pegue o que você precisa."
    ann "Nós vamos nos atrasar para o {b}Atletismo{/b}!"
    show player 10f
    show annie 1f
    player_name "Sim Sim. eu Vou."
    return

label school_hallway_smith_unlocked_locker:
    scene expression game.timer.image("school{}") with None
    show player 34
    with dissolve
    player_name "( Hmm, então {b}Diretora Smith tem uma chave mestra em seu escritório em algum lugar{/b}. )"
    player_name "( ... {b}Isso seria útil ter em mãos{/b}! )"
    player_name "( ... )"
    player_name "( Algo para pensar sobre. )"
    player_name "( Por enquanto, eu deveria ir para o {b}vestiarios dos meninos{/b} se trocar para o {b}Atletismo{/b}. )"

    return

label school_erik_webcam_quest:
    show player 14 at left
    show erik 1 at right
    player_name "Ei!"
    show player 17
    player_name "Eu pensei que você não iria aparecer."
    show player 1
    show erik 4
    eri "Eu disse a {b}Sra. Johnson{/b} Fui ver um filme no shopping..."
    show player 17
    show erik 1
    player_name "Legal."
    show player 11
    show erik 5
    eri "Mas eu não posso ficar fora por muito tempo: tenho que estar em casa antes de dormir."
    show player 92
    show erik 1
    player_name "Você tem hora de dormir?!"
    show player 91
    show erik 3
    eri "... Eu só não gosto de chatear a {b}Sra. Johnson{/b}, você sabe?"
    show player 113
    show erik 1
    player_name "De qualquer forma, temos que ser rápidos e tranquilos!"
    show player 1
    show erik 5
    eri "Existe um alarme?"
    show erik 1
    show player 2
    player_name "Não devemos nos preocupar com isso se usarmos a janela!"
    player_name "Apenas me acompanhe..."
    hide player
    hide erik
    hide ui
    scene black
    return

label school_erik_webcam_quest_sneak_in:
    with dissolve
    with Pause(0.5)
    show outside_school_night02a with dissolve
    show text "Depois de algum convencimento, {b}Erik{/b} me seguiu para o lado direito da escola.\nCorremos rapidamente pelo pátio em direção a uma das janelas do andar principal." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene black with dissolve
    with Pause(0.5)

    show outside_school_night02b with dissolve
    show text "Eu tive que dar {b}Erik{/b} um impulso primeiro.\n Eu tenho que dizer, foi muito mais difícil do que eu pensava..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene black with dissolve
    with Pause(0.5)

    show outside_school_night02c with dissolve
    show text "Foi então a minha vez, quando eu pulei para dentro e entrei...\n Nós finalmente chegamos, e ninguém nos viu." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    $ playMusic()
    hide text with dissolve

    hide outside_school_night02a
    hide outside_school_night02b
    hide outside_school_night02c
    scene black
    with dissolve
    with Pause(0.5)
    scene school_night with dissolve
    player_name "!!!"
    player_name "Eu ouço alguém vindo..."
    scene cult_event 1
    with Dissolve(0.3)
    eri "O que?"
    scene cult_event 2
    with Dissolve(0.3)
    player_name "Shhh!"
    player_name "Fique quieto..."
    scene cult_event 3
    with Dissolve(0.3)
    window hide
    pause
    scene cult_event 4
    with Dissolve(0.3)
    scene school_night
    show player 22 at left
    show erik 5 at right
    with dissolve
    eri "Tenho um mau pressentimento sobre isso..."
    show player 10
    show erik 1
    player_name "Sim, algo está acontecendo aqui."
    show player 11
    show erik 5
    eri "O que eles estão fazendo na escola tão tarde?"
    eri "... E vestindo essas roupas estranhas?"
    show player 92
    show erik 1
    player_name "Vamos segui-los e ver para onde eles estão indo."
    show player 91
    show erik 5
    eri "Serio? Porque eu estava pensando que talvez devêssemos sair..."
    show player 26
    show erik 3
    player_name "Não seja um frango!"
    player_name "Além disso, ainda não terminamos o que viemos fazer aqui..."
    show player 91
    show erik 2
    eri "{b}*Suspiro*{/b}"
    show erik 3
    eri "Está bem..."
    hide player 91 with dissolve
    hide erik 3 with dissolve
    return

label school_erik_webcam_quest_need_help:
    show player 114 with dissolve
    player_name "Hmm..."
    show player 10
    player_name "( Eu vou precisar de {b}ajuda{/b} entrando na escola à noite. )"
    hide player 10 with dissolve
    return

label school_roxxy_dexter_argument:
    scene school
    show eve 2 at right
    show kevin 23f at Position (xpos=500)
    with dissolve
    eve "Sim, eles estão discutindo agora!"
    show eve 5
    show kevin 9bf
    kev "Hah, eles são os piores..."
    kev "Eles totalmente merecem um ao outro!"
    show kevin 23f
    show eve 2
    eve "eu sei direito..."
    eve "Vamos, devemos dar uma olhada antes que acabe."
    show eve 5
    show kevin 9bf
    kev "... Eu estou bem. Seu drama estúpido não faz nada por mim..."
    show kevin 23f
    show player 14 at left with dissolve
    player_name "O que está acontecendo caras?"
    show player 13
    show kevin 9b with dissolve
    kev "Ei, Bruh!"
    show kevin 23
    show eve 4 with dissolve
    eve "Ei, {b}[firstname]{/b}."
    show eve 2 with dissolve
    eve "{b}Roxxy{/b} e {b}Dexter{/b} estão causando alguma cena grande ao longo da {b}quadra de basquete.{/b}"
    eve "Eu estava prestes a dar uma olhada."
    eve "... Quer vir"
    show eve 5
    show player 14
    player_name "Sim, ok."
    player_name "Vamos lá."
    show player 13
    show kevin 9b
    kev "Vejo vocês mais tarde!"
    hide player
    hide kevin
    hide eve
    with dissolve
    return

label school_roxxy_dexter_confront:
    scene school
    show player 5 at left
    show dexter 1 at right
    show dexter 4
    with dissolve
    dex "{b}[firstname]{/b}!"
    show dexter 2 with dissolve
    show player 10
    player_name "Cara. Aqui vamos nós..."
    player_name "O que você quer, {b}Dexter{/b}?"
    show player 5
    show dexter 6 with dissolve
    dex "Você estava olhando {b}Roxxy{/b} no banho?!"
    show dexter 5
    show player 12
    player_name "Quem te disse isso?"
    show player 11
    show dexter 8 with dissolve
    dex "... {b}Becca{/b}!"
    show dexter 6 with dissolve
    dex "É verdade?"
    show dexter 2 with dissolve
    show player 10
    player_name "Não!"
    player_name "Eu fui tomar banho depois da aula de ginástica."
    player_name "Não é minha culpa {b}Roxxy{/b} você já estava lá!"
    show player 5
    dex "..."
    show dexter 6 with dissolve
    dex "Então você estava pervertendo ela!"
    show dexter 2 with dissolve
    show player 10
    player_name "Hã?"
    show player 12
    player_name "Não!"
    player_name "Você não estava ouvindo?!"
    player_name "Olha cara, eu não estava lá pervertendo {b}Roxxy{/b}..."
    player_name "Eu precisava tomar banho!"
    player_name "Eu prometi a ela que não olharia."
    show player 11
    dex "..."
    hide player
    show dexter 7 at left

    player_name "{b}*Gurt*{/b}" with hpunch
    show player 89 at left
    show dexter 1 at right
    show dexter 6
    with dissolve
    dex "Deixa {b}Roxxy{/b} sozinha!"
    show dexter 5
    show player 88
    player_name "{b}*Weeze*{/b}"
    show dexter 6
    dex "Ela é minha!"
    dex "Compreende?!"
    show dexter 5
    player_name "{b}*Gasp*{/b}"
    show player 89
    show dexter 4 with dissolve
    dex "Vá perto dela novamente e eu vou bater na sua cara!"
    show dexter 2 with dissolve
    show player 88
    player_name "{b}*tosse tosse*{/b}"
    show player 10 with dissolve
    player_name "... Eu pensei que vocês dois estavam terminados?"
    show player 90
    show dexter 8
    dex "... Hã?"
    dex "Quem disse isso?"
    show dexter 2
    show player 10
    player_name "Você disse!"
    player_name "No outro dia, na {b}quadra de basquete{/b}."
    show player 90
    show dexter 6 with dissolve
    dex "Não acabou!"
    dex "Ela vai se desculpar e vamos voltar a ficar juntos."
    show dexter 2 with dissolve
    show player 10
    player_name "... Eu não tenho tanta certeza."
    show player 90
    show dexter 15 at Position (xoffset=2) with dissolve
    dex "Você quer outro?!"
    show dexter 14 at Position (xoffset=2)
    show player 88 with dissolve
    player_name "{b}*tosse*{/b}... Por favor não."
    show player 89
    show dexter 15 at Position (xoffset=2)
    dex "Então fique longe da minha garota!"
    dex "Entendeu!"
    show dexter 14 at Position (xoffset=2)
    show player 10 with dissolve
    player_name "... É, eu entendi."
    show player 90
    show dexter 15 at Position (xoffset=2)
    dex "Isso foi o que eu pensei!"
    hide dexter with dissolve
    show player 16
    player_name "( ... )"
    player_name "( Você vai ter o que merece um dia {b}Dexter{/b}. )"
    hide player with dissolve
    return

label school_roxxy_assignment:
    scene school
    show teacher 18f at left
    show roxxy 33 zorder 1 at right
    with dissolve
    rox "Não, {b}Miss Bissette{/b}! Estou te implorando aqui!"
    rox "Por favor, não me falhe!"
    show roxxy 32
    show teacher 19f
    bis "Eu tenho dito a você, menina boba!"
    bis "Transformar-se no trabalho de outro aluno é indesculpável!"
    bis "Estou cansado de dizer essas coisas!"
    show teacher 18f
    show roxxy 33
    rox "Vamos lá! Tem que haver algo que eu possa fazer!"
    rox "Apenas me dê mais uma chance!"
    show roxxy 32
    show teacher 3f
    bis "Hã!"
    show teacher 19f
    bis "Eu já te dei muitas chances!"
    show teacher 18f
    show roxxy 33
    rox "Eu vou estudar e fazer o trabalho sozinha desta vez."
    rox "Eu prometo!"
    rox "Apenas mais uma chance!"
    show roxxy 32
    show teacher 20f
    bis "..."
    show player 13f zorder 0 at Position (xpos=650) with dissolve
    show teacher 2f
    bis "{b}[firstname]{/b}!"
    bis "Este é um bom momento, sim?!"
    show teacher 5f
    bis "{b}Roxanne{/b} foi pega tentando entregar {b}sua lição de casa{/b}!"
    show teacher 19f
    bis "... Isso depois de eu contar a ela \"Eu falo com você, se você fizer isso de novo!\""
    bis "Agora ela está querendo mais uma chance!"
    show teacher 5f
    bis "O que diz você?"
    bis "Eu deveria estar dando a ela essa chance?"
    show teacher 4f
    rox "..."
    show player 11f
    player_name "..."
    show player 10f
    player_name "Eu uhh..."
    player_name "... Sim?"
    show player 5f
    show teacher 20f
    bis "Hmm..."
    pause
    show teacher 2f
    bis "Você é muito gentil, {b}[firstname]{/b}!"
    show teacher 12f
    bis "... Mas você também é fofo demais para recusar!"
    show roxxy 1e
    show player 13f
    bis "Muito bem."
    show teacher 19f
    bis "Esta é a sua última chance {b}Roxanne{/b}!"
    show teacher 18f
    show roxxy 1d
    rox "Ufa, obrigada!"
    show roxxy 1e
    show teacher 19f
    bis "... E para ter certeza que você faz as coisas direito..."
    show teacher 3f
    bis "{b}[firstname]{/b} aqui vai ser o seu parceiro de estudo!"
    show player 22f
    show teacher 1f
    show roxxy 3c with dissolve
    rox "O que?!"
    rox "De maneira nenhuma tá enlouquecendo que está acontecendo!"
    show roxxy 3d
    show teacher 3f
    bis "Ah ah ah!"
    show teacher 2f
    bis "O que aconteceu com, \"Eu farei qualquer coisa!\" Hmm?"
    show teacher 1f
    show roxxy 2
    rox "... Sim mas..."
    show roxxy 3c
    rox "... Por que ele?!"
    show roxxy 14
    if M_bissette.is_state(S_bissette_end):
        show teacher 12f
        bis "{b}[firstname]{/b} aqui é meu melhor aluno!"
        bis "Quem melhor para te ajudar com seus estudos, sim?"
        show teacher 13f
    else:
        show teacher 2f
        bis "{b}[firstname]{/b} está tentando fazer o trabalho bem."
        bis "Parece apropriado que você deveria estar ajudando um ao outro para alcançar, sim?"
        show teacher 1f
    show player 10f
    player_name "Eu realmente tenho que fazer isso?"
    show player 5f
    show teacher 2f
    bis "Foi sua ideia dar-lhe outra chance!"
    bis "Eu espero que você tenha certeza que ela realmente estuda!"
    show teacher 1f
    show player 24f
    player_name "{b}*Suspiro*{/b}"
    player_name "Ok..."
    show teacher 3f
    bis "Tres Bien!"
    show teacher 2f
    bis "Eu deixo você para isso!"
    hide teacher with dissolve
    show player 5 at left with dissolve
    show roxxy 29
    rox "..."
    player_name "..."
    show roxxy 30
    rox "Ugh, isso é uma merda!"
    show roxxy 29
    show player 10
    player_name "Apenas relaxe ... Não vai ser tão ruim."
    player_name "Eu irei para seu trailer mais tarde e nós acabaremos com isso rapidamente..."
    show player 5
    show roxxy 2
    rox "Você quer vir para o meu trailer?"
    show roxxy 3
    rox "Eu não quero você lá!"
    show roxxy 3d
    show player 10
    player_name "Você prefere ir à biblioteca ou algo assim??"
    show player 5
    show roxxy 3c
    rox "... E ser visto em público com VOCÊ..."
    rox "Eca, não."
    show roxxy 14
    show player 12
    player_name "Bem então..."
    show player 11
    dex "Ei, {b}Missy{/b}! Voce viu {b}Roxxy{/b} hoje?!"
    missy "Sim, ela estava a caminho para ver {b}Miss Bissette{/b}..."
    show roxxy 2b
    rox "!!!" with hpunch
    show roxxy 2c
    rox "Oh merda!"
    rox "Umm..."
    rox "Esconde!"
    scene expression "backgrounds/location_school_cutscene03.jpg"
    with fade
    show text "Antes que eu soubesse o que estava acontecendo {b}Roxxy{/b} tinha aberto meu armário e me empurrava para dentro." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene school
    show roxxy 7f at left
    show dexter 8 at right
    with dissolve
    dex "Aí está você."
    show dexter 2
    show roxxy 11f with dissolve
    rox "... Sim estou aqui. Estás bem?"
    show roxxy 9f
    show dexter 8
    dex "Apenas pensei em ver se você estava pronto para se desculpar?"
    show dexter 2
    show roxxy 11f
    rox "Pfft, pedir desculpas por quê?"
    show roxxy 9f
    show dexter 6 with dissolve
    dex "Você sabe o que!"
    dex "Você me chamou de nomes!"
    show dexter 2
    show roxxy 11f
    rox "Você quer dizer estúpido?"
    dex "..."
    show roxxy 5f with dissolve
    rox "Bem, não seja tão estúpido e eu não vou te chamar de idiota ... idiota."
    show roxxy 6f with dissolve
    dex "Grrr..."
    show dexter 6
    dex "PARE DE CHAMAR DE ESTÚPIDO!" with hpunch
    show dexter 5
    show roxxy 10f with dissolve
    rox "... Ou o que?"
    show roxxy 7f with dissolve
    show dexter 2 with dissolve
    dex "..."
    show dexter 8
    dex "Você tem sorte de ser minha namorada!"
    dex "Se alguém mais fala assim comigo assim..."
    show dexter 4
    dex "Eu esmagaria seu rosto!" with hpunch
    show dexter 2
    show roxxy 11f
    with dissolve
    rox "Uh hã."
    rox "Você está choramingando?"
    show roxxy 9f
    show dexter 8
    dex "Tanto faz."
    dex "Você vai se desculpar eventualmente."
    show dexter 6 with dissolve
    dex "Apenas lembra-te. Até que você faça, não me peça por nada'!"
    show dexter 2 with dissolve
    show roxxy 10f
    rox "Como se eu precisa-se de qualquer coisa de você!"
    rox "Você provavelmente iria estragar tudo, mesmo se eu fizesse!"
    show roxxy 6f with dissolve
    dex "..."
    show dexter 4 with dissolve
    dex "Rrraaaggh!!!" with hpunch
    show dexter 6 with dissolve
    dex "Você é uma vadia!"
    hide dexter with dissolve
    show roxxy 7f
    rox "..."
    show roxxy 1b at right with dissolve
    rox "Tudo bem, saia, {b}[firstname]{/b}."
    show roxxy 1
    pause
    show player 12 at left with dissolve
    player_name "Você acha uma boa ideia irrita-lo assim?"
    show player 5
    show roxxy 1b
    rox "Hã?"
    show roxxy 3c
    rox "Tanto faz. Foda-se ele! Ele é um idiota!"
    show roxxy 3d
    show player 10
    player_name "Sim, mas ele não é exatamente a pessoa mais estável do mundo..."
    player_name "Por que você está namorando com ele?"
    show player 12
    player_name "Você está fora do seu alcance!"
    show player 5
    show roxxy 2
    rox "Pfft, por favor. Estou fora do campeonato de todos!"
    rox "Namorar {b}Dexter{/b} significa que ninguém mais mexe comigo."
    show roxxy 1h
    rox "É apenas mais fácil."
    show roxxy 1g
    show player 10
    player_name "Sim, mas ele é tão..."
    show player 5
    show roxxy 2
    rox "... Estúpido?"
    show roxxy 1
    show player 17
    player_name "Haha, Sim!"
    show player 13
    show roxxy 4
    rox "Hahaha!"
    show roxxy 1
    pause
    show player 11
    player_name "..."
    rox "..."
    show player 10
    player_name "{b}*Ahem*{/b} Então eu acho que {b}Eu irei ao seu trailer hoje à noite{/b}?"
    show player 5
    show roxxy 30
    rox "{b}*Suspiro*{/b} Está bem."
    rox "Só não espere muito de mim com o estudo. Não é meu forte."
    show roxxy 29
    show player 14
    player_name "Não se preocupe. Eu vou te mostrar as cordas!"
    show player 13
    rox "..."
    show player 36 with dissolve
    player_name "Até mais {b}esta noite{/b}."
    show player 13
    show roxxy 30
    rox "... Uh hã."
    show roxxy 29
    hide player with dissolve
    rox "..."
    pause
    show roxxy 1g
    pause
    return

label school_roxxy_missing_outfit:
    scene school
    show becca 1 at Position(xpos=315)
    show missy 2b at left
    show roxxy 3c zorder 1 at right
    with dissolve
    rox "... Ugh, vocês duas acharam?"
    show roxxy 3b
    show becca 2
    becca "Não."
    show becca 1
    show missy 2
    missy "Tem certeza de que você não deixou em casa?"
    show missy 2b
    show roxxy 3c
    rox "Claro que tenho certeza, {b}Missy{/b}!"
    rox "O que, eu pareço um estúpida ou algo assim?"
    show roxxy 3b
    show becca 3
    show missy 1b
    missy "Eu não disse isso!"
    show missy 3
    show becca 3b
    becca "Você poderia muito bem ter dito..."
    show becca 3
    show missy 2
    missy "Só estou tentando ajudar!"
    show missy 2b
    show becca 4
    becca "Hahaha, pior ajuda de sempre!"
    show becca 5
    show roxxy 30
    rox "{b}*Suspiro*{/b} Suponho que alguma de vocês trouxeram um uniforme extra?"
    show roxxy 29
    show becca 2
    becca "Não. Meu back-up está na lavagem."
    show becca 3
    show missy 1b
    missy "Sim, eu também não trouxe o meu."
    show missy 1
    show becca 8
    becca "{b}Missy{/b} peitos minúsculos, seu uniforme não iria caber em você de qualquer maneira..."
    show becca 7
    show missy 4
    missy "Shuddup, Skank!"
    show missy 2b
    show becca 4
    becca "Hahaha, Não se preocupe. Você vai atingir a puberdade um dia..."
    show becca 5
    show roxxy 3c
    rox "{b}*Suspiro*{/b} Vocês duas não valem nada, sabiam?"
    show roxxy 3b
    show becca 2
    becca "Pssh, tanto faz."
    show becca 1
    show missy 2
    missy "Não é nossa culpa que você deixou seu uniforme em casa!"
    show missy 2b
    show roxxy 30
    rox "Eu acho, nós vamos ter que ir e buscar."
    show roxxy 3b
    show becca 2b with dissolve
    becca "Que?!"
    becca "Quer que a gente vá até sua casa agora?!"
    show becca 1 with dissolve
    show missy 2
    missy "Não, foda-se isso!"
    show missy 2b
    show roxxy 3c
    rox "Vamos lá, vadias idiotas.!"
    rox "Não quero ir sozinha!"
    show roxxy 3b
    show missy 2
    missy "De maneira nenhuma!"
    missy "Se eu faltar outra lição francesa, {b}Miss Bissette{/b} vai me dedurar para meus pais..."
    show missy 2b
    show becca 3b
    becca "Ooh, sua mãe gritaria totalmente se isso acontecesse!"
    show becca 3
    show missy 1b
    missy "Eu sei, certo?"
    show missy 1
    show roxxy 2
    rox "Tudo bem, nós vamos sem você... Certo {b}Becca{/b}?"
    show roxxy 1
    show becca 2b with dissolve
    becca "..."
    show roxxy 3b
    rox "Sério?!"
    show roxxy 3c
    show becca 2 with dissolve
    becca "Está muito quente para andar até o seu trailer!"
    becca "... Além disso, seu primo me assusta.."
    show becca 1
    show roxxy 31
    show missy 2b
    rox "Vocês são péssimos!"
    show roxxy 3d
    show player 14f zorder 0 at Position (xpos=600) with dissolve
    player_name "Ei, garotas!"
    player_name "O que está acontecendo?"
    show player 13f
    show becca 2
    becca "... Umm, Por que está falando conosco?"
    show becca 1
    show player 11f
    show missy 1b
    missy "Alerta de nerd!"
    show missy 1
    show roxxy 27 with dissolve
    rox "..."
    show player 5 with dissolve
    show roxxy 28
    rox "Esqueci-me do meu {b}Cheerleading uniforme{/b} Em casa."
    show roxxy 1n
    rox "... E \"Minhas amigas\" aqui, são bons demais para ir comigo para obtê-lo."
    show roxxy 1m
    show player 5f with dissolve
    show missy 1b
    missy "Ei, eu faria se não fosse por {b}Miss Bissette{/b}!"
    show missy 1
    show roxxy 1n
    rox "... Tanto faz."
    show roxxy 1m
    show player 10 with dissolve
    player_name "Eu irei com você.."
    show roxxy 1k
    player_name "... Você sabe, se você quiser?"
    show player 5
    show roxxy 1i
    show becca 2b with dissolve
    becca "Eca..."
    becca "Por que ela iria querer ir a qualquer lugar com você, garoto nerd?!"
    show becca 1 with dissolve
    show roxxy 1j
    rox "..."
    pause
    show roxxy 1l
    rox "... Tudo bem, vamos lá."
    show roxxy 1k
    show player 13
    show becca 2b with dissolve
    becca "Que!?!"
    becca "Você vai mesmo com esse perdedor?"
    show becca 1
    show roxxy 3
    with dissolve
    rox "Bem, eu não quero atravessar a cidade sozinha!"
    rox "... E já que vocês duas não virão..."
    show roxxy 3c
    show player 5
    rox "... Que escolha eu tenho?"
    show roxxy 3b
    show becca 2
    show player 5f with dissolve
    becca "Sim, mas quero dizer... Olha só para ele...."
    becca "... Ele é tão..."
    show becca 1
    show missy 8
    missy "... Perdição?"
    show missy 7
    show becca 4
    becca "Haha, Sim!"
    show becca 5
    show missy 3
    show player 12f
    player_name "Isso nem é uma palavra!"
    show player 90f
    show roxxy 3c
    rox "Ugh, Vocês dois parem já?!"
    rox "Vamos {b}[firstname]{/b}. Vamos acabar com isso.."
    hide roxxy with dissolve
    player_name "..."
    show player 12f
    player_name "... Até mais, saco de puta!"
    hide player with dissolve
    show becca 1
    becca "..."
    show becca 3
    show missy 6
    missy "Pfft, hahaha!"
    show missy 7
    show becca 2f at Position (xpos=400) with dissolve
    becca "Do que está rindo?!"
    show becca 1f
    show missy 6
    missy "... Aquele nerd acabou de te chamar de saco de puta!"
    show missy 7
    show becca 2f
    becca "Umm, Ele nos chamou de vagabundas, retardada."
    show becca 1f
    show missy 3
    missy "..."
    show missy 5
    missy "Oh, Certo..."
    show missy 4
    missy "Ei, não me chame de retardada, sua vadia!"
    scene black with fade
    return

label school_roxxy_return_to_school:
    scene school
    show player 14 at Position (xpos=500)
    show roxxy 23 at right
    show roxxy_outfit cheer at right
    with dissolve
    player_name "Parece que fizemos a tempo.."
    show player 13
    show roxxy 24
    rox "... Obrigado pela sua ajuda hoje."
    show roxxy 23
    show player 14
    player_name "Não é um problema, {b}Roxxy{/b}!"
    show player 13
    show becca 5 at Position(xpos=315)
    show becca_outfit cheer at Position (xpos=315)
    show missy 1b at left
    show missy_outfit cheer at left
    with dissolve
    show player 13f at Position (xpos=600) with dissolve
    missy "Ei, você achou?!"
    show missy 1
    show becca 6
    becca "... Uhh, Obviamente."
    becca "Ela está usando, não é?"
    show becca 5
    show missy 2
    missy "Oh, shuddup!"
    show missy 2b
    show becca 8
    becca "O que o geek ainda está fazendo aqui?"
    show becca 7
    show player 5f
    show roxxy 23b
    rox "... Não diga nomes."
    show roxxy 23
    show becca 2
    becca "Hã?"
    show becca 1
    show roxxy 24
    rox "... Ele é um cara legal.."
    show roxxy 23
    show becca 8
    becca "O que, você está apaixonada por ele agora ou algo assim?"
    show becca 7
    show roxxy 23c
    rox "Pfft, não!"
    show roxxy 24
    rox "Ele só me ajudou a sair do congestionamento hoje é tudo e acho que você deveria ser mais gentil com ele."
    show roxxy 23
    show becca 4
    becca "Hah, whatever!"
    show becca 8
    becca "Eu acho que você tem uma pequena queda por {b}[firstname]{/b}!"
    show becca 4
    becca "Haha!"
    show becca 8
    becca "O que você acha, {b}Missy{/b}?"
    show becca 7
    show missy 8
    missy "... Sim, ele é meio fofo."
    show missy 7
    show becca 3
    becca "!!!" with hpunch
    show becca 3b
    show missy 3
    becca "Isso não foi o que eu quis dizer!"
    show becca 2
    becca "Qual é o problema com vocês dois?!"
    show becca 1
    show missy 1
    rox "..."
    show becca 2
    becca "Ugh, Eu vou praticar!"
    hide becca
    hide becca_outfit cheer
    with dissolve
    show missy 2
    missy "{b}Becca{/b}, aguarde!"
    missy "... Eu não entendi a pergunta!"
    hide missy
    hide missy_outfit cheer
    with dissolve
    rox "..."
    show player 10 at Position (xpos=500) with dissolve
    player_name "... Obrigado por dizer que."
    show player 13
    show roxxy 23b
    rox "Hã?"
    show roxxy 24
    rox "Oh, certo."
    rox "Tanto faz."
    rox "Não deixe isso ir à sua cabeça!"
    show roxxy 23b
    rox "Eu não gosto de você nem nada. Eu apenas aprecio sua ajuda é tudo."
    show roxxy 23
    show player 14
    player_name "Ok."
    player_name "Eu acho que vou te ver por aí."
    show player 13
    show roxxy 24
    rox "Sim, vamos ver..."
    hide roxxy
    hide roxxy_outfit cheer
    with dissolve
    player_name "( Bem, esse foi um dia louco... )"
    player_name "( Eu acho que a {b}Roxxy{/b} está começando a gostar de mim! )"
    show player 18
    player_name "( Eu deveria procurar mais oportunidades para me aproximar dela. )"
    return

label school_roxxy_trailer_park_trouble:
    scene school
    show annie 3 at right
    show roxxy 3df zorder 1 at left
    with dissolve
    ann "O manual do aluno é muito claro sobre este assunto!"
    ann "Os alunos não têm permissão para usar seus celulares enquanto estiverem na propriedade da escola."
    show annie 1
    show roxxy 3f
    rox "Vá embora, seu intrometido parvo psicótico!"
    show roxxy 3df
    show player 10f zorder 0 at Position (xpos=500) with dissolve
    player_name "O que está acontecendo?"
    show player 5f
    show roxxy 3f
    rox "Estou tendo uma crise aqui!"
    show roxxy 3df
    show player 5 at Position (xpos=400) with dissolve
    show annie 5
    ann "Irrelevante!"
    ann "Não há telefones celulares na propriedade da escola e isso é propriedade da escola!"
    show annie 3
    ann "Você tem que guardá-lo!"
    show annie 1
    show roxxy 3f
    rox "Saia de perto, {b}Annie{/b} ou juro que vou lhe dar uma, bem na cara!"
    show roxxy 3bf
    show annie 5
    ann "Pfft, você não me assusta..."
    show annie 6
    ann "..."
    show annie 5
    ann "... Estou entendendo {b}Diretora Smith{/b}!"
    hide annie with dissolve
    show roxxy 3df
    show player 10f at Position (xpos=600) with dissolve
    player_name "O que aconteceu?"
    show player 5f
    show roxxy 33f
    rox "Aparentemente, os policiais apareceram e prenderam {b}minha mãe{/b}!"
    show roxxy 32f
    show player 10f
    player_name "O que?!"
    player_name "Por que eles fariam isso?"
    show player 11f
    show roxxy 33f
    rox "Eu não sei!"
    rox "Eu tenho que ir para casa..."
    show roxxy 32f
    player_name "..."
    show player 10f
    player_name "Você quer que eu vá com você?"
    show player 5f
    show roxxy 32f
    rox "..."
    show roxxy 1lf
    rox "Você realmente faria isso?"
    show roxxy 32f
    show player 10f
    player_name "... Claro, eu não me importo!"
    show player 5f
    rox "..."
    show roxxy 1lf
    rox "Obrigada, {b}[firstname]{/b}."
    rox "Vamos, vamos sair daqui antes {b}Annie{/b} volta."
    show roxxy 32f
    show player 12f
    player_name "Logo atrás de você."
    hide roxxy
    hide player
    with dissolve
    return

label school_roxxy_selling_meth_ask_roxxy:
    scene school
    show roxxy 14f at Position (xpos=500)
    show becca 1 at Position(xpos=315)
    show missy 1 at left
    show player 14f at right
    with dissolve
    player_name "Ei {b}Roxxy{/b}, Eu preciso falar com você!"
    show player 13f
    show becca 2
    becca "Ugh, saia perdedor!"
    show becca 1
    show missy 2
    missy "Sim, você não vê que ela tem problemas suficientes?!"
    show missy 2b
    show player 14f
    player_name "Acho que encontrei uma maneira de consertar tudo isso!"
    show player 13f
    show missy 2
    missy "Pfft, Ok, certo!"
    show missy 2b
    show becca 2
    becca "O que um nerd como você vai fazer?"
    show becca 1
    show roxxy 29f
    show player 12f
    player_name "Posso falar com você por um segundo?"
    show player 90f
    show becca 2
    becca "Eu disse saia perdedor!"
    show becca 1
    show missy 2
    missy "Sim saia"
    show missy 3
    show roxxy 30f
    rox "Vocês duas já deveriam calar a boca!"
    show player 11f
    rox "*Suspiro* Apenas vá para a aula, eu quero ouvi-lo."
    show roxxy 29f
    show player 13f
    show becca 2b with dissolve
    becca "Você está falando sério?"
    show becca 1
    show roxxy 3 at Position (xpos=600)
    with dissolve
    rox "Apenas vá!"
    show roxxy 3b
    show missy 2b
    show becca 2
    becca "Está bem!"
    show becca 3b
    becca "Vamos {b}Missy{/b}!"
    hide becca
    hide missy
    with dissolve
    pause
    show roxxy 3cf at Position (xpos=500) with dissolve
    rox "Então, como exatamente você vai consertar tudo isso?"
    show roxxy 3df
    show player 14f
    player_name "Bem, eu convenci{b}Clyde{/b} se entregar!"
    show player 13f
    show roxxy 30f
    rox "... Ótimo."
    show roxxy 3df
    show player 5f
    player_name "..."
    show player 10f
    player_name "É isso aí?"
    show player 5f
    show roxxy 3cf
    rox "Você esqueceu?"
    rox "Mesmo que ele confesse, {b}minha mãe{/b} vai ficar na prisão até o julgamento."
    rox "Ainda vamos perder o trailer."
    show roxxy 3df
    show player 14f
    player_name "Bem, eu tenho um plano para isso também!"
    player_name "{b}Clyde{/b} diz que ele tem mais do que suficiente, de Meth para fazer $50,000 dólares!"
    show player 13f
    show roxxy 2f
    rox "Pfft, {b}Clyde{/b} diz..."
    show roxxy 3cf
    show player 5f
    rox "Esse idiota mal pode amarrar os sapatos!"
    rox "... E você acha que ele pode realmente vender tudo isso de Meth?!"
    show roxxy 3df
    player_name "..."
    show player 10f
    player_name "Ele não faz isso o tempo todo?"
    show player 5f
    show roxxy 4f
    rox "Hahaha! Você está brincando comigo?"
    show roxxy 3cf
    rox "Ele cozinha, mas {b}minha mãe{/b} faz toda a venda!"
    show roxxy 3df
    show player 11f
    player_name "..."
    show roxxy 2bf
    rox "!!!"
    show roxxy 3cf
    rox "Eu nunca disse isso! Compreendo!"
    show roxxy 3df
    show player 10f
    player_name "Não se preocupe, não vou contar a ninguém."
    show player 5f
    show roxxy 30f
    rox "Olha, eu agradeço por você tentar ajudar, {b}[firstname]{/b}."
    show roxxy 3cf
    rox "... Mas é melhor você esquecer de mim e dos meus problemas!"
    hide roxxy with dissolve
    player_name "..."
    show player 4f
    player_name "( Bem, e agora? )"
    player_name "( Eu acho que eu deveria ir {b}Encontrar Clyde{/b}... )"
    hide player with dissolve
    return

label school_roxxy_shut_down_lab:
    scene school
    show roxxy 32f at Position (xpos=500)
    show becca 2 at Position(xpos=315)
    show missy 1 at left
    show player 13f at right
    with dissolve
    becca "Ugh, de volta?"
    show becca 1
    show missy 2
    missy "O que você quer agora, perdedor?!"
    show missy 2b
    show player 5f
    show roxxy 30f at Position (xoffset=34)
    rox "Oh. MEU DEUS."
    show roxxy 3 at Position (xpos=600) with dissolve
    rox "Vocês dois apenas cortariam isso?"
    rox "Não estou com disposição para tudo isso."
    show roxxy 3d
    show missy 3
    missy "..."
    show becca 2
    becca "... E daí? Nós devemos ser legais com esse nerd agora?"
    show becca 1
    show roxxy 3c
    rox "Vamos conversar."
    show roxxy 3d
    show player 13f
    show becca 2
    becca "Bem."
    show becca 3b
    becca "Vamos {b}Missy{/b} vamos embora {b}Roxxy{/b} e seu brinquedo de menino nerd para conversar."
    hide becca with dissolve
    show roxxy 3c
    rox "Ugh, pare de ser uma cadela, {b}Becca{/b}!"
    show roxxy 3d
    show missy 1b
    missy "Ei, espere por mim!"
    hide missy with dissolve
    pause
    show roxxy 3cf at Position (xpos=500) with dissolve
    rox "O que você quer, {b}[firstname]{/b}."
    show roxxy 3df
    show player 14f
    player_name "Trouxe uma coisa para você!"
    show player 239_240f with dissolve
    pause
    show player 650f with dissolve
    pause
    show roxxy 68bf
    show player 13f
    with dissolve
    rox "..."
    show roxxy 68cf
    rox "Deus ele é burro."
    show roxxy 1f f with dissolve
    show player 14f
    player_name "Hehe, Sim..."
    show player 13f
    show roxxy 2f
    rox "Eu pensei que tinha dito para você esquecer tudo isso?"
    show roxxy 1f f
    show player 14f
    player_name "Sim, você disse."
    show player 13f
    show roxxy 2f
    rox "Então, por que você ainda está"
    show roxxy 2bf
    show player 14f
    player_name "Trouxe outra coisa para você também!"
    show player 239_240f with dissolve
    pause
    show player 638bf
    rox "!!!" with hpunch
    show roxxy 80f at Position (xoffset=47)
    show player 13f
    with dissolve
    pause
    show roxxy 82f at Position (xoffset=47)
    rox "Puta merda!"
    rox "Eu nunca vi tanto dinheiro antes!"
    rox "Como você..."
    show roxxy 81f at Position (xoffset=47)
    show player 14f
    player_name "Clyde e eu vendemos o Meth ontem à noite."
    show player 13f
    show roxxy 82f at Position (xoffset=47)
    rox "Are you serious?!"
    show roxxy 81f at Position (xoffset=47)
    show player 14f
    player_name "Sim. Nós fizemos $60,000!"
    player_name "Isso deve bastar para salvar {b}sua mãe{/b} certo?"
    show player 13f
    show roxxy 80f at Position (xoffset=47)
    rox "..."
    show roxxy 1bf with dissolve
    rox "Não acredito que você fez tudo isso!"
    show roxxy 1f f
    rox "..."
    show roxxy 1bf
    rox "{b}[firstname]{/b}, por que você está fazendo tudo isso?!"
    rox "Você não me deve nada e eu só fui má com você."
    show roxxy 1f f
    show player 14f
    player_name "... Porque é a coisa certa a fazer."
    show player 13f
    show roxxy 1if at Position (xoffset=-34) with dissolve
    rox "..."
    show roxxy 1lf at Position (xoffset=-34)
    rox "Eu não sei o que dizer..."
    show roxxy 1kf
    show player 14f
    player_name "Você não precisa dizer nada."
    player_name "Vá e volte para casa."
    show player 13f
    pause
    hide player
    show roxxy 59f at right
    player_name "!!!" with hpunch
    rox "Obrigada, {b}[firstname]{/b}!"
    rox "Eu não vou esquecer isso!"
    hide roxxy
    show roxxy 1f f at Position (xpos=500)
    show player 14f at right
    with dissolve
    player_name "... Sem problemas!"
    show player 13f
    show roxxy 1bf
    rox "É melhor eu ir até a estação e encontrar minha {b}mãe{/b} !"
    rox "Falo com você em breve, ok?"
    show roxxy 1f f
    show player 14f
    player_name "Tudo bem. Boa sorte!"
    show player 13f
    hide roxxy with dissolve
    pause
    hide player
    show player 17f
    with dissolve
    player_name "( Uau! )"
    player_name "( {b}Roxxy{/b} me abraçou em público! )"
    show player 13f
    player_name "( Bem, meio que ... Ninguém estava por perto para vê-la... )"
    player_name "( ... Mas ainda é um progresso! )"
    player_name "( Eu deveria procurar mais oportunidades para passar um tempo com ela quando as coisas se acalmarem! )"
    hide player with dissolve
    return

label school_roxxy_give_exams:
    scene school
    show player 14 at left
    show roxxy 1 at right
    with dissolve
    player_name "Ei, {b}Roxxy{/b}!"
    show player 17
    player_name "Eu tenho uma coisa para você?"
    show player 13
    show roxxy 1b
    rox "Você quer dizer..."
    rox "Você tem os exames?"
    show roxxy 1
    show player 14
    player_name "Hehe, Sim!"
    player_name "Ela os mantinha no quarto, dá para acreditar?!"
    show player 239_240 with dissolve
    pause
    show player 643 with dissolve
    pause
    hide player
    show roxxy 59 at left
    with dissolve
    rox "Oh meu deus, você é o melhor {b}[firstname]{/b}!"
    player_name "!!!" with hpunch
    show roxxy 64b at right
    show player 14 at left
    with dissolve
    player_name "Err, Obrigado..."
    show player 13
    show roxxy 64c
    rox "Você sabe..."
    rox "Eu realmente gosto de um cara que não tem medo de mostrar sua garotinha."
    show roxxy 64b
    show player 10
    player_name "... A minha garotinha?"
    show player 5
    show roxxy 2b with dissolve
    rox "!!!"
    show roxxy 2c
    rox "Quero dizer, para não dizer ... eu sou sua garota ou qualquer coisa..."
    show roxxy 1
    show player 3 with dissolve
    player_name "..."
    show roxxy 2
    rox "Hehe, isso seria loucura, certo?"
    show roxxy 1
    show player 29
    player_name "Oh, Eu não sei"
    show player 3
    show roxxy 2
    rox "Quero dizer, você poderia imaginar você e eu?"
    rox "... Namorando?"
    show roxxy 1
    show player 24 with dissolve
    player_name "..."
    rox "..."
    show player 26
    player_name "Eu uhh..."
    show player 11
    show roxxy 2b
    ann "Você realmente acha que um dos alunos é responsável?"
    smi "... Bem, quem mais invadiria minha casa e roubaria apenas os exames?!"
    show roxxy 2c
    rox "Oh Merda!"
    rox "{b}Diretora Smith{/b} está vindo!"
    show roxxy 2b
    show player 10
    player_name "Você não pode deixá-la ver esses exames!"
    player_name "Temos que sair daqui!"
    show roxxy 2c at left
    show player 11f at Position (xpos=400)
    with dissolve
    rox "Não há tempo!"
    show roxxy 2b
    show player 10f
    player_name "O que você está fazendo"
    show player 11f
    show roxxy 3c
    rox "{b}Cale a boca e venha aqui!!!{/b}"
    show roxxy 3d
    show player 22f
    player_name "!!!"
    scene black with fade
    scene expression "backgrounds/location_school_cutscene04.jpg"
    with fade
    show text "... E assim fui arrastado para o meu armário pela {b}Roxxy{/b}!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene school
    show principal 26f at left
    show principal 26f at Position (xoffset=70)
    show annie 3 at right
    with dissolve
    ann "Então qual é o plano?"
    show annie 1
    show principal 4f with dissolve
    smi "Temos que receber esses exames de volta! Se o conselho descobrir isso, pode significar o fim de tudo que construí aqui!"
    show principal 26f at Position (xoffset=70) with dissolve
    show annie 3
    ann "Não se preocupe, senhora. Isso não vai acontecer!"
    show annie 1
    show principal 27f at Position (xoffset=70)
    smi "Claro que não vai acontecer! Você vai encontrar esses exames e trazer os responsáveis para mim para punição!"
    show principal 26f at Position (xoffset=70)
    show annie 3
    ann "... Sim, senhora."
    show annie 1
    show principal 27f at Position (xoffset=70)
    smi "Comece pesquisando nesses armários."
    smi "A merda pode ter escondido eles lá."
    show principal 26f at Position (xoffset=70)
    show annie 3
    ann "Imediatamente, senhora!"
    show annie 1
    show principal 4f with dissolve
    smi "... E não me falhe, {b}Annie{/b}!"
    smi "Você sabe o que acontece quando estou descontente..."
    show principal 26f at Position (xoffset=70) with dissolve
    show annie 6
    ann "..."
    show annie 5
    ann "Eu não vou falhar com você, senhora."
    show annie 6
    show principal 27f at Position (xoffset=70)
    smi "Muito bomd."
    smi "Agora comece a trabalhar!"
    hide annie
    hide principal
    with dissolve
    scene expression "backgrounds/location_school_locker_inside01.jpg"
    show player locker 3
    show roxxy locker 1
    player_name "!!!"
    show player locker 1
    player_name "{b}Annie está procurando nos armários!{/b}"
    player_name "Estamos totalmente ferrados!"
    show player locker 2
    show roxxy locker 2
    rox "Shh!!!"
    rox "Fique quieto!"
    show roxxy locker 3
    rox "... E pare de se contorcer!"
    show roxxy locker 1
    show player locker 1
    player_name "Desculpe, só estou pirando!"
    player_name "Nós vamos ser expulsos por isso, sabe?!"
    show player locker 2
    show roxxy locker 2
    rox "Você se acalmar!"
    show roxxy locker 1
    show player locker 4
    player_name "..."
    show player locker 7
    player_name "Sorry..."
    show player locker 2
    "Clang!"
    show player locker 3
    pause
    ann "Eca, o que são esses tecidos crocantes?!"
    show player locker 1
    player_name "Ela está chegando mais perto!"
    show player locker 8
    "Clang!"
    show player_boner locker 1 with dissolve
    pause
    show roxxy locker 2
    rox "Ei! Você está cutucando-"
    show player locker 9
    show player_boner locker 2
    show roxxy locker 4
    rox "!!!" with hpunch
    show roxxy locker 3
    rox "O que é isso?!"
    rox "Não me diga que é seu pau?"
    show roxxy locker 4
    show player locker 5
    player_name "..."
    "Clang!"
    show player locker 3
    show roxxy locker 6
    rox "Seu pau está duro agora?!"
    show roxxy locker 5
    show player locker 7
    player_name "Eu não posso evitar..."
    show player locker 5
    show roxxy locker 7
    rox "Como você pode pensar nisso agora?!"
    show roxxy locker 5
    show player locker 7
    player_name "Eu não sei! Eu não posso controlar isso!"
    show player locker 5
    show roxxy locker 7
    rox "Bem, ta muito duro"
    show roxxy locker 8
    hide player_boner
    rox "{b}*Gasp*{/b}"
    rox "Está tocando minha"
    show roxxy locker 9
    show player locker 2
    player_name "Pare de se mexer!"
    show player locker 1
    show roxxy locker 8
    "Clang!"
    $ M_roxxy.set('sex speed', .6)
    show roxxy locker 8_9
    show player locker 9
    player_name "Você está piorando!!"
    show player locker 8
    rox "... Está tocando minha buceta"
    show player locker 9
    player_name "{b}Roxxy{/b} pare de se mexer!"
    show player locker 3
    player_name "... Oh porcaria."
    player_name "Acho que somos o próximo armário..."
    show player locker 9
    player_name "Você tem que parar de esfregar em mim!"
    show player locker 8
    $ M_roxxy.set('sex speed', 2)
    show roxxy locker 8_9
    rox "Ahh... Fuuu..."
    pause
    jud "{b}Annie!{/b}"
    show player locker 3
    jud "Preciso de ajuda para abrir meu armário..."
    ann "Ugh, a sério?"
    ann "Você é uma dor na minha bunda."
    jud "Eu sei, me desculpe..."
    ann "Esta é a última vez!"
    jud "..."
    jud "O que você está procurando em todos os armário?"
    show player locker 4
    ann "deixa pra lá!"
    pause
    ann "Tudo bem, está aberto. Pegue suas coisas!"
    ann "Seu armário está bagunçado!"
    show player locker 8
    jud "..."
    ann "Isso é nojento..."
    ann "Qual o problema com você?!"
    jud "eu só"
    ann "É estritamente proibido manter os alimentos no seu armário!"
    show player locker 3
    ann "Vou ter que escrever para você..."
    jud "... Mas"
    ann "Sem desculpas, vamos lá!"
    ann "Estou levando você para {b}Diretora Smith{/b} Imediatamente!"
    show player locker 9
    ann "Aposto que você vai animá-la!"
    jud "Com uma Punição?"
    ann "Mova-se!"
    jud "... Que tipo de punição?!"
    pause
    $ M_roxxy.set('sex speed', .4)
    show roxxy locker 8_9
    rox "Mmm..."
    show player locker 7
    player_name "{b}*Huff*{/b} Você tem que ... Parar."
    player_name "eu acho que {b}Annie{/b} é... {b}*Puff*{/b}... Annie está saindo!"
    show player locker 8
    rox "Ahh!"
    show player locker 7
    player_name "{b}Roxxy{/b}?"
    player_name "O que você está fazendo?! Temos que ir!"
    show player locker 9
    rox "Shuddup! Shuddup! Shuddup!"
    $ M_roxxy.set('sex speed', .2)
    show roxxy locker 8_9
    player_name "O que aconteceu"
    show player locker 9
    show roxxy locker 10
    rox "Ngghhh!" with flash
    show player locker 8
    player_name "!!!" with hpunch
    rox "Haah... Haah..."
    rox "Puta merda!"
    rox "Isso foi..."
    show player locker 5
    player_name "..."
    show player locker 6
    player_name "{b}Roxxy{/b} nós temos que sair daqui antes {b}Annie{/b} volta!"
    show player locker 5
    show player_boner locker 2
    show roxxy locker 2
    with dissolve
    rox "Sim, ok."
    rox "Apenas ... Me ajude. Minhas pernas estão como gelatina agora..."
    scene black with fade
    scene school
    show roxxy 1k at right
    show player 10 at left
    with dissolve
    player_name "Isso foi muito perto!"
    show player 5
    rox "..."
    show roxxy 1l
    rox "Ufa, isso foi..."
    show roxxy 1m
    pause
    show roxxy 86 at left
    hide player with hpunch
    pause
    show roxxy 3b at right
    show player 15 at left
    with dissolve
    player_name "Ai!"
    show player 12
    player_name "Por que fez isso!"
    show player 90
    show roxxy 3c
    rox "Quem diabos fica com tesão em um momento como esse?!"
    show roxxy 3d
    show player 10
    player_name "Eu não sei?!"
    player_name "Isso aconteceu!"
    show player 12
    player_name "Eu não sou o único você não parava de se esfregar em mim!"
    show player 90
    show roxxy 3b
    pause
    show roxxy 86 at left
    hide player
    rox "Cale-se!" with hpunch
    show roxxy 3b at right
    show player 15 at left
    with dissolve
    player_name "Ai! Pare de me dar soco!"
    show player 16
    show roxxy 3
    rox "É melhor não contar a ninguém o que aconteceu naquele armário!"
    show roxxy 3c
    rox "Você me entendeu?!"
    show roxxy 3b
    show player 12
    player_name "É, eu entendi!"
    player_name "Apenas certifique-se de não ser pego com esses exames..."
    show player 90
    show roxxy 3
    rox "Eu vou me preocupar com os exames!"
    rox "Você apenas se concentra em manter a boca fechada!"
    rox "Se alguém descobrir, eu absolutamente morrerei!"
    show roxxy 29f with dissolve
    show player 12
    player_name "{b}*Suspiro*{/b} Você está muito preocupado com as opiniões de outras pessoas ... Você sabe disso?"
    show player 90
    show roxxy 30f
    rox "Apenas cale a boca, {b}[firstname]{/b}..."
    show roxxy 29f
    show player 12
    player_name "Bem. Eu tenho que ir para a minha próxima aula de qualquer maneira..."
    player_name "Até mais, {b}Roxxy{/b}."
    show player 90
    rox "..."
    show roxxy 30f
    rox "Bye."
    hide player
    hide roxxy
    with dissolve
    show roxxy 29f
    rox "..."
    show roxxy 32 with dissolve
    pause
    show roxxy 33
    rox "Isso foi incrível!"
    rox "... É tão..."
    rox "... Grande!"
    show roxxy 1g with dissolve
    rox "..."
    show roxxy 1h
    rox "Quem pensaria que ele estava carregando algo assim?!"
    show roxxy 32 with dissolve
    pause
    show roxxy 33
    rox "... Talvez eu esteja muito preocupada com a opinião de outras pessoas..."
    rox "Quero dizer, seria realmente tão ruim se eu começar a namorar {b}[firstname]{/b}?"
    show roxxy 1i
    rox "..."
    show roxxy 1l
    rox "Ah meu deus, eu acabei de perceber..."
    rox "{b}Missy{/b} estava certo sobre os nerds terem  paus grandes."
    show roxxy 84 with dissolve
    rox "..."
    rox "Ugh, se ela descobrir Será o fim..."
    hide roxxy with dissolve
    return

label school_roxxy_dexter_flirt:
    scene school
    show player 13f at right
    show dewitt 43 at left
    with dissolve
    dewitt "Ah, {b}[firstname]{/b}. No momento ideal!"
    show dewitt 42
    show player 14f
    player_name "Ei, {b}Miss Dewitt{/b}."
    player_name "Maldição, isso é um monte de registros!"
    show player 13f
    show dewitt 41
    dewitt "Could you do me a favor and run these down to the auditorium for me?"
    dewitt "Eu estou fazendo uma palestra sobre acústica hoje mais tarde..."
    show dewitt 42
    show player 14f
    player_name "Claro, eu não me importo."
    show player 13f
    show dewitt 43
    dewitt "Ah, Obrigada docinho."
    hide dewitt
    show player 642f
    with dissolve
    pause
    player_name "( Hmm, {b}o auditório{/b} está abaixo do {b}corredor do lado direito no primeiro andar{/b}. )"
    player_name "( {b}Eu deveria ir lá agora.{/b} )"
    hide player with dissolve
    return

label school_roxxy_do_pushups_intro:
    scene school
    show player 13 at left
    show erik 4 at right
    with dissolve
    eri "{b}[firstname]{/b}!"
    show erik 1
    show player 14
    player_name "Oi, {b}Erik{/b}."
    player_name "E aí cara?"
    show player 13
    show erik 4
    eri "Oh, você sabe ... o de sempre."
    eri "Eu peguei este novo e doente pedaço de roupa durante um ataque ontem à noite!"
    show erik 1
    show player 12
    player_name "Codpiece?"
    show player 13
    show erik 4
    eri "É cara. As damas verdes adoram uma boa peça..."
    show erik 1
    show player 17
    player_name "... Haha, certo cara."
    show player 13
    show erik 4
    eri "Como foram as coisas no concurso de biquíni?"
    show erik 1
    show player 14
    player_name "Foi tão incrível!"
    player_name "Você deveria ter vindo comigo..."
    show player 13
    show erik 4
    eri "Então você tem que ver {b}Roxxy{/b} de biquíni apertado?"
    show erik 1
    show player 14
    player_name "Oh, você não tem ideia!"
    player_name "Ela parecia tão sexy, cara!"
    show player 13
    show erik 4
    eri "Legal!"
    eri "Você gosta mesmo dela, hein?"
    show erik 1
    show player 14
    player_name "... Sim. Ela é realmente uma pessoa muito legal."
    player_name "É apenas estava enterrada sob uma camada de maldade..."
    show player 13
    show erik 4
    eri "Hahaha!"
    eri "Ela realmente disse oi para mim esta manhã..."
    show erik 1
    show player 12
    player_name "Mesmo?"
    show player 13
    show erik 3b
    eri "Quero dizer, ela não sabia meu nome..."
    show erik 4
    eri "Mas ei, pelo menos ela não me chamou de nerd ou gordo."
    show erik 1
    show player 14
    player_name "Hehe, desculpa."
    show player 13
    show erik 4
    eri "Não mesmo! Foi uma grande melhoria."
    eri "Ela deve realmente gostar de você, {b}[firstname]{/b}!"
    show erik 1
    show player 14
    player_name "Sim, eu não sei."
    show player 13
    show erik 4
    eri "Vamos lá, cara."
    eri "Ela nem Costumava conversar conosco."
    eri "Agora ela está convidando você para uma festa com seus amigos."
    show erik 1
    show player 5
    player_name "..."
    show player 10
    player_name "Nós vamos nos atrasar para a academia..."
    show player 5
    show erik 3b
    eri "Oh, tiro! Você está certo."
    show erik 4
    eri "Vamos lá, você pode me contar tudo sobre o concurso de biquíni no caminho!"
    hide player
    hide erik
    with dissolve
    scene gym
    show player 13 at left
    show erik 3b zorder 1
    with dissolve
    eri "O top dela estalou?!"
    show erik 1
    show player 14
    player_name "Hehe, Sim."
    show player 13
    show erik 3b
    eri "O que você viu?..."
    show erik 1
    show player 14
    player_name "Seus seios!"
    show player 13
    show erik 4
    eri "... Uau!"
    show erik 1
    show player 14
    player_name "Não é grande coisa..."
    show player 13
    show erik 4
    eri "Ok, certo!"
    eri "Isso é tão incrível, cara!"
    eri "Eu gostaria de poder ter visto"
    show erik 1b
    show dexter 15 zorder 0 at right
    with dissolve
    show player 90
    dex "Bata garoto gordo."
    show dexter 14
    show erik 5b
    eri "Hã?"
    show erik 5b
    show player 12
    player_name "Nos deixe em paz, {b}Dexter{/b}..."
    show player 90
    show dexter 15
    dex "EU DISSE BATA, MENINO GORDO!"
    hide erik
    show dexter 21c
    with dissolve
    pause
    show dexter 21d with dissolve
    pause
    show dexter 14 with dissolve
    show player 15
    player_name "Que diabos, cara!"
    show player 16
    show dexter 15 with dissolve
    dex "Eu não te disse para deixar {b}Roxxy{/b} sozinha!"
    show dexter 14
    show player 5
    player_name "..."
    show dexter 15
    dex "Agora ouvi dizer que você a está incomodando na praia?!!"
    show dexter 13 at Position (xoffset=-18) with dissolve
    dex "Preciso bater em seu rosto?!"
    show dexter 14 with dissolve
    show player 12
    player_name "Saia de perto, {b}Dexter{/b}!"
    player_name "Ela me convidou."
    show player 90
    show dexter 12 with dissolve
    dex "Psh, Ok certo."
    dex "Por que ela iria querer ficar com um perdedor como você?"
    show dexter 11
    show player 12
    player_name "Eu sou o perdedor?!"
    player_name "Você é quem forçar as garotas, porque elas não pode agir..."
    show player 90
    show dexter 15 with dissolve
    dex "O que diabos você acabou de dizer?!"
    show dexter 14
    show player 15
    player_name "... Você me ouviu!"
    show player 12
    player_name "Você é patético, {b}Dexter{/b}!"
    show player 90
    show dexter 21b at Position (xpos=950) with dissolve
    dex "Você está morto, {b}[firstname]{/b}!"
    show dexter 14
    show bridget a_dressed_crossed f_angry_talk at Position (xpos=300) with dissolve
    bri "O que diabos está acontecendo aqui?!"
    show bridget a_dressed_crossed f_normal with dissolve
    show dexter 11
    dex "!!!"
    show player 12
    player_name "Nada, senhora."
    show player 90
    show bridget a_dressed_crossed f_angry_talk
    bri "Não parece nada!"
    show bridget a_dressed_crossed f_angry_talk with dissolve
    bri "{b}Dexter{/b}, quantas vezes tenho que dizer para não começar brigas durante a aula?!"
    show bridget a_dressed_crossed f_normal
    show dexter 22
    dex "Sim, mas treinadora ... Esta pequena barata foi"
    show dexter 21
    show bridget a_dressed_crossed f_angry_yell
    bri "Não quero ouvir!" with hpunch
    bri "Se vocês rapazes precisam resolver uma discussão, então vamos fazê-lo de maneira não violenta..."
    show bridget a_dressed_crossed f_normal
    show player 12
    player_name "... Como conversar?"
    show player 90
    show dexter 22
    dex "Eu não entendo"
    show dexter 21
    show bridget a_dressed_crossed f_angry_yell
    bri "Flexões!"
    show bridget a_dressed_crossed f_normal
    show player 10
    player_name "Hã?!"
    show player 5
    show bridget a_dressed_crossed f_angry_yell
    bri "Agora me dê cinquenta! Vocês dois!" with hpunch
    show bridget a_dressed_crossed f_normal
    show player 11
    player_name "!!!"
    dex "!!!"
    show bridget a_dressed_crossed f_angry_talk
    bri "Última pessoa em pé vence o argumento!"
    show bridget a_dressed_crossed f_normal
    show dexter 12
    dex "Este pequeno imbecil não pode fazer cinquenta flexões..."
    show dexter 11
    show player 12
    player_name "Aposto que posso fazer mais rápido que você."
    hide player with dissolve
    show dexter 12
    dex "Psh, Okay, certo."
    show dexter 11
    dex "..."
    hide dexter with dissolve
    pause
    show bridget a_dressed_whistle f_angry_yell with dissolve
    bri "Vai!"
    return

label school_roxxy_trailer_park_romance_intro:
    scene school
    show player 13 at left
    show roxxy 1b at right
    with dissolve
    rox "{b}[firstname]{/b}!"
    show roxxy 1
    show player 14
    player_name "Ei, {b}Roxxy{/b}."
    player_name "Estás bem?"
    show player 13
    show roxxy 1b
    rox "Eu estava esperando por você."
    show roxxy 1
    show player 10
    player_name "Você estava me esperando?"
    show player 5
    show roxxy 1b
    rox "Sim, achei que poderíamos ir juntos para a aula."
    show roxxy 1
    show player 12
    player_name "Mesmo?"
    show player 14
    player_name "Quero dizer, claro! Gostaria disso!"
    show player 13
    show roxxy 1b
    rox "Legal."
    show roxxy 1
    player_name "..."
    rox "..."
    show player 14
    player_name "Então você conseguiu seu troféu em casa?"
    show player 13
    show roxxy 4
    rox "Sim"
    show roxxy 1b
    rox "Eu tenho no meu quarto."
    rox "Eu ainda não acredito que venci..."
    show roxxy 1
    show player 14
    player_name "Bem, você conseguil!"
    player_name "As outras garotas não tiveram chance!"
    show player 13
    show roxxy 1b
    rox "Hehe, realmente?"
    show roxxy 1
    show player 14
    player_name "Claro."
    player_name "Você está fora da liga delas!"
    show player 13
    rox "..."
    show roxxy 1b
    rox "... Obrigada, {b}[firstname]{/b}."
    rox "Diga, eu estava pensando..."
    rox "... Se você não está muito ocupado..."
    show roxxy 1
    show player 5
    player_name "Hmm?"
    show roxxy 2
    rox "... Talvez você queira sair hoje à noite?"
    show roxxy 1
    show player 10
    player_name "Você quer sair comigo?"
    show player 5
    show roxxy 2
    rox "Só se você quiser!"
    rox "... Eu apenas pensei ... Talvez ... Você fosse à minha casa?"
    show roxxy 1b
    rox "Eu posso fazer pra você um jantar!"
    rox "Você sabe ... um agradecimento por toda a sua ajuda!"
    show roxxy 1
    show player 10
    player_name "Você pode cozinhar?"
    show player 5
    show roxxy 2
    rox "Não realmente..."
    show roxxy 1b
    rox "... Desculpe, eu não sou muito boa nisso."
    show roxxy 1
    show player 5
    player_name "Hmm?"
    show player 10
    player_name "O que você quer dizer?"
    show player 5
    show roxxy 2
    rox "... deixa pra lá."
    rox "Apenas esqueça que eu disse alguma coisa."
    show roxxy 1
    return

label school_roxxy_trailer_park_romance_no:
    show player 10
    player_name "Bem, eu faria {b}Roxxy{/b} mas eu tenho outros planos..."
    show player 5
    show roxxy 1l with dissolve
    rox "Oh, sim. Totalmente..."
    rox "Eu tenho toneladas de outras coisas para fazer também."
    show roxxy 1k
    show player 12
    player_name "... Talvez outra hora?"
    show player 5
    show roxxy 1l
    rox "Sim talvez. Veremos..."
    hide roxxy with dissolve
    pause
    show player 12
    player_name "Ela está agindo de forma estranha..."
    hide player with dissolve
    return

label school_roxxy_trailer_park_romance_yes:
    show player 10
    player_name "Espere, não!"
    show player 14
    player_name "Eu irei!"
    show player 13
    show roxxy 1b
    rox "Você irá?!"
    show roxxy 1
    show player 14
    player_name "Definitivamente! Estou apenas surpreso que você me perguntou é tudo."
    show player 13
    show roxxy 2
    rox "Hehe, Sim..."
    show roxxy 1
    player_name "..."
    rox "..."
    show roxxy 1b
    rox "Então eu acho que vou te ver a {b}tarde{/b} no {b}meu trailer{/b}?"
    show roxxy 1
    show player 14
    player_name "Parece bom."
    show player 13
    show roxxy 4
    rox "Impressionante! Não se esqueça!"
    show roxxy 1
    show player 14
    player_name "Hehe, Eu não vou."
    hide roxxy with dissolve
    pause
    show player 17
    player_name "( Uau, {b}jantar hoje à noite na casa de Roxxy{/b}! )"
    player_name "( Acho que somos realmente amigos agora! )"
    show player 13
    player_name "( Hmm, Eu me pergunto por que ela estava agindo tão estranho sobre isso? )"
    hide player with dissolve
    return

label school_roxxy_dexter_basketball:
    scene school
    show player 5f with dissolve
    player_name "( Hmm, Não vejo {b}Dexter{/b} por aí... )"
    player_name "( Eu realmente espero que ele não tenha visto {b}Roxxy{/b} e eu dando uns amassos. )"
    player_name "( Ele vai querer brigar com certeza. )"
    show erik 4 at right
    eri "E aí, cara"
    show erik 5
    show player 6f at left
    player_name "Whaaaa!!!" with hpunch
    show player 22 with dissolve
    eri "Uau?!"
    show player 37 with dissolve
    eri "O que?"
    show erik 3b
    player_name "Ufa, desculpe cara."
    show player 38
    player_name "Você me assustou!"
    show player 5 with dissolve
    show erik 5
    eri "O que te deixou tão nervoso?"
    show erik 3b
    show player 10
    player_name "{b}*Suspiro*{/b} eu acho que {b}Dexter{/b} me viu saindo com {b}Roxxy{/b}..."
    show player 5
    show erik 5
    eri "!!!" with hpunch
    eri "Você ficou com {b}Roxxy{/b}?!"
    show erik 51
    show player 38 with dissolve
    player_name "Shh, fala baixo, cara!"
    show player 3
    show erik 53
    eri "Desculpe ... Cara, esta é uma notícia épica!"
    show erik 4
    eri "Meu melhor amigo está saindo com a garota mais popular da escola!"
    show erik 1
    show player 5 with dissolve
    player_name "..."
    show player 12
    player_name "Eu acho que você não ouviu a parte em que o esteroide dela, psicopata de um ex-namorado, nos viu juntos?"
    show player 5
    show erik 3b
    eri "Oh, certo."
    show erik 5
    eri "Sim, isso não é bom. {b}Dexter{/b} vai te matar cara..."
    show erik 52
    show player 12
    player_name "Eu sei! É por isso que estou nervoso!"
    player_name "Continuo esperando que ele me ataque toda vez que passo em uma sala de aula..."
    show player 5
    show erik 4
    eri "Bem, não se preocupe, cara. eu te dou cobertura!"
    eri "Podemos caminhar juntos e eu vou ter certeza de que ele não espreite você."
    show erik 1
    show player 10
    player_name "Hehe, Obrigado, {b}Erik{/b}..."
    show player 5
    show erik 5
    eri "Apenas esteja avisado, se tudo se resume a uma luta, eu vou ser menos do que inútil..."
    player_name "..."
    show erik 3b
    eri "Estou falando sério, cara ... Não me julgue tão severamente se eu fizer xixi nas calças e desmaiar!"
    show erik 1
    show player 17
    player_name "Hahaha!"
    show player 13
    show erik 4
    eri "Vamos lá, temos Ginásio na {b}quadra de basquete{/b} hoje. De jeito nenhum não deixa o {b}Dexter{/b} tenta iniciar uma briga na frente de {b}Treinadora Bridget{/b}."
    show erik 1
    show player 10
    player_name "Sim, espero que você esteja certo."
    hide player
    hide erik
    with dissolve
    scene basketball_b
    show kevin 23f at Position (xpos=500)
    show erik 52f at Position (xpos=300)
    show player 5 at left
    show bridget a_dressed_ball f_normal_talk at Position (xpos=650)
    with dissolve
    bri "... Agora eu sei que vocês provavelmente já viram os profissionais na TV..."
    bri "... Drible entre as pernas e passando pelas costas!"
    show bridget a_dressed_ball f_angry_talk
    bri "É um monte de bobagens!" with hpunch
    show bridget a_dressed_ball f_normal_talk
    bri "Basquete é tudo sobre os fundamentos!"
    bri "Reprodução inteligente, execução precisa"
    show bridget a_dressed_ball f_normal
    show kevin 32f
    kev "... E fazendo chover a partir da linha de 3 pontos!"
    show kevin 23f
    player_name "..."
    eri "..."
    show bridget a_dressed_ball f_angry_talk
    bri "Oh, então isso é uma grande piada para você, não é?"
    show bridget a_dressed_ball f_normal
    show kevin 34f with dissolve
    kev "{b}*Gole*{/b} ... Eu não quis dizer"
    show kevin 23f with dissolve
    show bridget a_dressed_ball f_normal_talk
    bri "Não não não. É minha culpa..."
    bri "... Eu não sabia que você era bom demais para os fundamentos do basquete..."
    show bridget a_dressed_ball f_normal
    show kevin 34f with dissolve
    kev "Não foi"
    show kevin 34bf
    show bridget a_dressed_ball f_angry_talk
    bri "Por que você não dá voltas pela quadra pelo resto da aula?"
    show bridget a_dressed_ball f_normal
    kev "!!!"
    show kevin 24f with dissolve
    kev "... Mas isso é 57 minutos..."
    show kevin 24bf
    show bridget a_dressed_ball f_normal_talk
    bri "Isso não é suficiente?"
    bri "Podemos sempre nos encontrar aqui depois da escola, se você quiser mais?"
    show bridget a_dressed_ball f_normal
    show kevin 24f
    kev "{b}*Suspiro*{/b} Não Senhora."
    show kevin 24bf
    show bridget a_dressed_ball f_normal_talk
    bri "Bom."
    show bridget a_dressed_ball f_angry_talk
    bri "iniciar!" with hpunch
    show bridget a_dressed_ball_whistle f_angry_yell
    hide kevin
    with dissolve
    pause
    show bridget a_dressed_ball f_normal_talk with dissolve
    bri "Hmm, agora onde eu estava?"
    show bridget a_dressed_ball f_normal
    show player 10
    player_name "{b}*Ahem*{/b} Fundamentos, senhora."
    show player 5
    show bridget a_dressed_ball f_normal_talk
    bri "Ahh, Sim."
    bri "Então basquete é tudo sobre o fundo"
    show bridget a_dressed_ball f_normal
    show player 22
    dex "Há o nerd que eu estou procurando!" with hpunch
    show player 23
    player_name "Oh, Merda..."
    show player 22
    show erik 5f
    eri "Uh oh..."
    show erik 51f
    show dexter 14 at right with dissolve
    show bridget a_dressed_ball f_normal_talk
    bri "O que no mundo?!"
    show bridget a_dressed_ball f_normal
    show dexter 15
    dex "Você acha que eu não ia descobrir, sua putinha?!"
    show dexter 14
    show bridget a_dressed_ball f_angry_talk
    bri "com licença! {b}Dext{/b}-"
    show bridget a_dressed_ball f_normal
    show dexter 13 at Position (xoffset=-18) with dissolve
    dex "Saia do meu caminho, garoto gordo, ou eu arranco essas sardas idiotas do seu rosto!" with hpunch
    show erik 64f with fastdissolve
    show erik 65f with fastdissolve
    show erik 66f with fastdissolve
    hide erik
    show dexter 15
    with dissolve
    dex "Eu vi você e aquela prostituta, ex-namorada minha!"
    show dexter 14
    show player 15
    player_name "Ei, não fale assim da {b}Roxxy{/b} se não!"
    show player 16
    show dexter 15
    dex "Eu direi o que diabos eu quiser!"
    dex "O que você vai fazer sobre isso, NERD?!"
    show dexter 14
    show player 11 at Position (xpos=-150)
    show bridget a_dressed_ball f_angry_talk at flip
    show bridget at Position (xpos=450)
    bri "Tudo bem, {b}Dexter{/b}, é melhor você fazer backup neste instante!" with hpunch
    bri "Isso não está acontecendo no meio da minha classe, senhor!"
    show bridget f_angry
    show dexter 15
    dex "... Mas {b}Treinadora{/b} você não entende..."
    dex "Este pedaço de merda-"
    show dexter 14
    show bridget a_dressed_ball f_angry_talk
    bri "Eu não quero ouvir isso, {b}Dexter{/b}!"
    bri "Você conhece as regras da minha turma!"
    bri "Nós resolvemos as coisas aqui sem violência!"
    show bridget f_angry
    show dexter 15
    dex "Ugh, isso não será resolvido até que o imbecil receba a surra que ele merece..."
    show dexter 14
    show bridget a_dressed_ball_throw f_normal with dissolve
    player_name "..."
    show bridget a_dressed_crossed f_normal
    show dexter 29
    with dissolve
    dex "Hmm?"
    show bridget a_dressed_crossed f_normal_talk
    bri "Então vencê-lo na quadra."
    hide bridget
    show player 16 at left
    with dissolve
    show dexter 30
    dex "Eu não entendo..."
    show dexter 29
    show player 12
    player_name "Ela está dizendo que devemos resolver isso com um jogo de basquete ... idiota."
    show player 16
    dex "!!!"
    show dexter 30
    dex "Oh, você está tão morto..."
    show dexter 33
    show player 647
    with dissolve
    dex "Bem!"
    show dexter 15 with dissolve
    dex "Você é bola, NERD!"
    hide player
    hide dexter
    with dissolve
    return

label school_roxxy_fight_dexter:
    scene expression game.timer.image("outside_school{}")
    show player 12 with dissolve
    player_name "É melhor garantir que estou preparado para uma luta antes de voltar para a escola."
    player_name "Não há duvidas, {b}Dexter{/b} estará procurando sangue depois do que aconteceu na quadra de basquete."
    show player 4 at Position (xoffset=7) with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "Vou precisar de muita {b}Agilidade{/b} para evitar seus ataques e {b}Força{/b} para colocá-lo no chão rápido."
    player_name "Caso contrário, não terei chance..."
    show player 5
    player_name "..."
    show player 38 at Position (xoffset=51) with dissolve
    player_name "Estou pronto para isso?!"
    show player 3 at Position (xoffset=26) with dissolve

    return

label school_roxxy_locker_sex:
    scene expression "backgrounds/location_school_locker_room_backpack_day_blur.jpg"
    show becca 6 at Position (xpos=315)
    show roxxy 1g at Position (xpos=600)
    show missy 7 at left
    with dissolve
    becca "... Isso é bom?!"
    show becca 5
    show roxxy 1h
    rox "Porra. Mente. Sopro!"
    show roxxy 1g
    show missy 5
    missy "Ooooh, Estou me molhando só de pensar nisso..."
    show missy 7
    show roxxy 1h
    rox "Tipo, oh meu Deus ... eu não consigo nem descrever como é."
    show roxxy 1g
    show becca 2
    becca "... Isso doi?"
    show becca 1
    show roxxy 2
    rox "Sim, muito no começo!"
    show missy 3
    show roxxy 1b
    rox "... Mas depois de um tempo dói menos..."
    show roxxy 1h
    rox "... E depois, ainda dói, mas de uma maneira REALMENTE boa!"
    show roxxy 1g
    show becca 5
    becca "Hmm..."
    show missy 8
    missy "Deus, isso é tão quente!"
    show missy 7
    show becca 3b
    becca "Parece muito quente..."
    show becca 5
    show roxxy 1h
    rox "Você não tem ideia!"
    show roxxy 1g
    becca "..."
    show missy 8
    missy "Então, quando vamos brincar com ele?!"
    show roxxy 2b
    show missy 7
    show becca 3b
    becca "{b}Missy{/b}!!!"
    show becca 3
    show missy 8
    missy "... O que?!"
    show roxxy 3d
    missy "Não aja como se não estivesse pensando a mesma coisa!"
    show missy 7
    show becca 26 with dissolve
    becca "..."
    show becca 24 with dissolve
    show roxxy 3c
    rox "... A sério?!"
    rox "Ele é {b}MEU{/b} maldito namorado! Por que eu deveria deixar vocês idiotas brincar com ele?!"
    show roxxy 3d
    show missy 1b
    missy "Uhh, porque somos suas idiotas idiotas!"
    show missy 8
    missy "... Além disso, todos sabemos que isso te excita..."
    show missy 7
    show roxxy 2b
    rox "!!!" with hpunch
    show roxxy 3c
    rox "Que diabos você está falando?!"
    show roxxy 3d
    show missy 8
    missy "Não minta!"
    show missy 7
    show becca 25
    becca "Nós duas vimos você brincando consigo mesmo durante nossos jogos de girar a garrafa, {b}Roxxy{/b}..."
    show becca 24
    show roxxy 2c
    rox "... Eu não!"
    show roxxy 2b
    show missy 1b
    missy "Você faz isso!!!"
    show missy 7
    show becca 25
    becca "Não é muito sutil..."
    show becca 24
    show roxxy 29
    rox "..."
    show roxxy 30
    rox "OK. Bem!"
    show roxxy 3c
    rox "Eu admito, é meio sexy assistir todo mundo brincando quando brincamos..."
    rox "Isso não significa que eu vou deixar você começar a transar com ele..."
    show roxxy 3d
    show becca 25
    becca "..."
    show missy 4
    missy "Por que não?!"
    show missy 2b
    show roxxy 3
    rox "Porque ele é {b}meu homem{/b}!"
    rox "Não é teu! é {b}MEU{/b}!"
    show roxxy 3b
    becca "..."
    show missy 8
    missy "Sim mas..."
    missy "Apenas pense sobre isso, {b}Roxxy{/b}."
    missy "{b}Becca{/b} nua ... De costas ... Seus seios pálidos e sardentos arfando de antecipação..."
    show missy 7
    show roxxy 1
    show becca 27 with dissolve
    becca "Antecipação?! Que diabos você está falando?!"
    show becca 26
    show missy 4
    missy "Cale-se! Estou tentando pintar uma foto aqui!"
    show missy 2b
    rox "..."
    show missy 8
    missy "{b}[firstname]{/b} com enorme pau latejante, esfregando contra seu clitóris enquanto ela geme e implora para você deixá-la ter..."
    show missy 7
    becca "..."
    show roxxy 1b
    rox "... Estou ouvindo."
    show roxxy 1
    show missy 8
    missy "{b}*Ahem*{/b}!!!"
    show missy 7
    show becca 27
    becca "What?!"
    show becca 26
    show missy 8
    missy "{b}Becca{/b} implora para deixá-la tê-lo..."
    show missy 7
    show becca 27
    becca "A sério?!"
    show becca 26
    show missy 4
    missy "Faça isso, cadela! Não estrague isso pra mim!"
    show missy 2b
    show becca 24 with dissolve
    becca "..."
    show becca 25
    becca "Por favor, deixe-me tê-lo {b}Roxxy{/b}..."
    show missy 7
    show roxxy 4
    rox "Hahaha, você realmente me imploraria por isso, {b}Becca{/b}?"
    show roxxy 1
    show becca 25
    becca "... Eu não sei."
    show becca 24
    show missy 8
    missy "Oh, ela totalmente faria! Veja como ela está excitada, só de pensar nisso..."
    show missy 7
    show becca 27 with dissolve
    becca "eu não estou!"
    show becca 26
    show missy 8
    missy "Puta, você está praticamente ofegante."
    show missy 7
    becca "..."
    show becca 24 with dissolve
    show roxxy 1g
    rox "Hmm."
    show roxxy 1h
    rox "... E você?!"
    show roxxy 1g
    show becca 26 with dissolve
    show missy 1b
    missy "Eu?!"
    show missy 1
    show roxxy 1h
    rox "Você vai me implorar também?"
    show roxxy 1g
    show missy 8
    missy "Eu farei o que você quiser que eu faça!"
    missy "Você quer que eu implore? Vou implorar."
    missy "Vou chupar seus peitos ou lamber sua buceta ... Inferno, vou jogar sua salada se você quiser!"
    missy "Contanto que você me deixe dar uma volta naquele enorme pau nerd dele!"
    show missy 7
    show roxxy 4
    rox "Hahahaha!"
    show roxxy 1g
    show missy 8
    missy "Vamos lá, você tem que admitir. Está bem excitante."
    missy "Suas próprias cadelas pessoais, dispostas a fazer o que quiser, para ter uma chance no pau do seu homem..."
    show missy 7
    show becca 27
    becca "Eu não estou jogando sua salada..."
    show becca 26
    show missy 2
    missy "Psh, você totalmente {b}Becca{/b}. Não minta!"
    show missy 7
    show becca 24 with dissolve
    becca "..."
    show roxxy 1h
    rox "Você realmente pensa muito nisso..."
    show roxxy 1h
    show missy 6
    missy "Ah, mais do que muita coisa, acredite em mim!"
    show missy 7
    rox "..."
    show missy 8
    missy "Então o que você diz?!"
    show missy 7
    rox "..."
    show roxxy 1g
    rox "... Talvez."
    show roxxy 1h
    show missy 3
    show becca 2
    becca "!!!"
    show missy 1b
    missy "{b}*Gasp*{/b} Mesmo?!"
    show missy 1
    show roxxy 1b
    rox "Teríamos que estabelecer algumas regras básicas..."
    rox "... Como vocês duas fazem tudo o que eu digo, sem argumentos."
    show roxxy 1g
    show missy 1b
    missy "Estou tão totalmente a bordo com isso!"
    show missy 1
    becca "..."
    show roxxy 1b
    rox "{b}Becca{/b}?"
    show roxxy 1
    show missy 7b with dissolve
    becca "!!!"
    show missy 1 with dissolve
    show becca 25
    becca "... Eu farei tudo o que você disser."
    becca "Sem argumentos..."
    show becca 24
    show roxxy 1h
    rox "... Mesmo se eu disser para você me chupar ou engolir toda a porra do {b}[firstname]{/b} ?"
    show roxxy 1g
    show missy 4
    missy "Claro que sim! Com prazer!"
    show missy 1b
    missy "O que você quiser, {b}Roxxy{/b}! Eu sou sua puta!"
    show missy 1
    becca "..."
    show roxxy 1b
    rox "{b}Becca{/b}?"
    show roxxy 1g
    show becca 25
    becca "... Sim, ok."
    show becca 24
    show roxxy 1h
    rox "Certo o que?!"
    show roxxy 1g
    show becca 25
    becca "Eu também serei sua vadia, ok?!"
    show becca 24
    show roxxy 4
    rox "Hahaha!"
    show roxxy 1h
    rox "...Hmm, vou pensar sobre isso."
    show roxxy 1g
    show missy 7
    missy "..."
    becca "..."
    show roxxy 1b
    rox "Agora, se você me der licença."
    show roxxy 1h
    rox "Eu vou encontrar com {b}meu homem{/b}!"
    hide roxxy with dissolve
    pause
    show becca 1f at Position (xpos=400) with dissolve
    show missy 4
    missy "Droga, eu esperava que ela concordasse imediatamente..."
    show missy 2b
    show becca 2f
    becca "... Eu também."
    show becca 1f
    show missy 1b
    missy "Veja, eu sabia que você estava nisso!"
    show missy 1
    show becca 2f
    becca "Cale-se!"
    show becca 1f
    show missy 8
    missy "Você é uma puta."
    show missy 7
    show becca 2f
    becca "Sim, bem ... Pelo menos eu não sou uma puta tão grande quanto você!"
    show becca 1f
    show missy 5
    missy "Tanto faz."
    show missy 2
    missy "Sua puta aqui pode ter acabado de nos marcar um encontro com {b}[firstname]{/b} E seu pau mágico!"
    missy "Você deveria estar me agradecendo agora!"
    show missy 2b
    show becca 7f
    becca "..."
    hide becca
    hide missy
    with dissolve

    scene school
    show player 13 at left
    with dissolve
    show roxxy 1b at right with dissolve
    rox "Aí está você!"
    show roxxy 1
    show player 14
    player_name "Oi, {b}Roxxy{/b}!"
    player_name "O que está rolando?"
    show player 13
    show roxxy 1h
    rox "Hehe, Eu estava pensando em você..."
    show roxxy 1g
    show player 14
    player_name "Oh Sim?"
    player_name "E o que você estava pensando?"
    show player 13
    show roxxy 1h
    rox "Oh, você sabe ... Quão forte e viril você é..."
    rox "... E como eu gostaria de montar seu pênis forte e duro aqui e agora."
    show roxxy 1g
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "O que?! nós não podemos fazer isso!"
    player_name "Estamos na escola!"
    show player 5
    show roxxy 4
    rox "Hehehe, Não se preocupe!"
    show roxxy 1h
    rox "Ninguém vai nos ver..."
    show roxxy 1g
    show player 11
    player_name "..."
    show roxxy 1h
    rox "eu tenho um plano!"
    hide roxxy with dissolve
    show player 12
    player_name "Hã?"
    hide player with fastdissolve

    scene expression "backgrounds/location_school_cutscene06.jpg"
    with fade
    show text "Novamente, {b}Roxxy{/b} me arrastou para o meu armário como uma boneca de pano!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene expression "backgrounds/location_school_locker_inside01.jpg"
    show player locker 1
    show roxxy locker 1b
    with dissolve
    player_name "Ótimo, estamos enfiados no meu armário novamente..."
    show player locker 2
    show roxxy locker 1
    rox "Hehe, cale a boca e tire seu pau!"
    show roxxy locker 1b
    show player locker 7
    player_name "Você está falando sério?!"
    show player locker 5
    show roxxy locker 1
    rox "Inferno sim, estou falando sério!"
    rox "Eu quero você dentro de mim, agora!"
    show roxxy locker 1b
    show player locker 6
    player_name "O que diabos você ficou tão excitada?!"
    show player locker 5
    show roxxy locker 1
    rox "Mmm, você descobrirá em breve."
    show roxxy locker 1b
    show player locker 11 with dissolve
    player_name "..."
    show player locker 12 with dissolve
    pause
    hide roxxy
    show player locker 13
    with dissolve
    rox "... Mas agora, quero que você se concentre..."
    show player locker 14 with dissolve
    pause
    rox "... Me fodendo sem sentido!"
    player_name "Ok..."
    show player locker 15
    rox "!!!" with hpunch
    rox "Ahhh..."
    return

label school_roxxy_locker_sex_repeat:
    scene school
    show player 12 with dissolve
    player_name "... Agora, onde diabos ela está?!"
    show player 4 with dissolve
    rox "Pssst!"
    show player 11f
    player_name "!!!" with hpunch
    hide player with fastdissolve

    scene expression "backgrounds/location_school_cutscene06.jpg"
    with fade
    show text "Novamente, {b}Roxxy{/b} me arrastou para o meu armário como uma boneca de pano!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Eu não era o brinquedo dela, era?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene expression "backgrounds/location_school_locker_inside01.jpg"
    show player locker 8
    show roxxy locker 1
    with dissolve
    rox "Finalmente! Eu estava começando a pensar que você me criticou!"
    show roxxy locker 1b
    show player locker 6
    player_name "Sério, você quer fazer isso de novo?!"
    show player locker 5
    show roxxy locker 1
    rox "Absolutamente!"
    show roxxy locker 1b
    show player locker 6
    player_name "Você percebe o que aconteceria? Se fôssemos pegos fazendo sexo na escola?!"
    show player locker 5
    show roxxy locker 1
    rox "Sim, nós dois seríamos expulsos."
    show roxxy locker 1b
    player_name "... Exatamente!"
    show player locker 11 with dissolve
    pause
    show player locker 12 with dissolve
    pause
    hide roxxy
    show player locker 13
    with dissolve
    rox "Então não vamos ser pegos..."
    show player locker 14 with dissolve
    player_name "... Por que você não está preocupado?-"
    rox "{b}[firstname]{/b}, cale a boca e me foda!"
    show player locker 15
    player_name "Bem!" with hpunch
    return

label roxxy_locker_sex_loop_pre:
    scene expression "backgrounds/location_school_locker_inside01.jpg"
    $ M_roxxy.set("sex speed", .09)
    show expression AnimatedImage("roxxys_locker", [1,2,3,4,5,6,7,8,9,10], M_roxxy) as roxxys_locker with dissolve
    return

label roxxy_locker_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("roxxys_locker", [1,2,3,4,5,6,7,8,9,10], M_roxxy) as roxxys_locker
                $ animated = True
            pause 5
            call expression game.dialog_select("roxxy_locker_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "roxxys_locker {}".format(pose_list[pose_counter]) as roxxys_locker
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("roxxy_locker_hscene_dialog")
        $ animcounter += 1
    if M_roxxy.get("roxxy locker sex first"):
        $ M_roxxy.set("roxxy locker sex first", False)
    call screen roxxy_locker_sex_options

label roxxy_locker_hscene_dialog:
    $ random_count = randomizer()
    if animcounter == 0:
        if M_roxxy.get("roxxy locker sex first"):
            player_name "Shhh!!!"
            player_name "Você tem que ficar quieto ou alguém vai nos pegar!"
            rox "Eu sei!"
            rox "Não é exatamente fácil, você sabe!"
            player_name "Bem, então pare e eu vou te foder hoje à noite!"

        elif not M_roxxy.get("roxxy locker sex first"):
            if random_count > 33 and random_count <= 66:
                rox "Mmm, Eu amo esse pau, muito pra caralho!"
                player_name "Shh!!"
                rox "{b}*Whimper*{/b}"

            elif random_count > 66:
                rox "Aahh!!"

    elif animcounter == 1:
        if M_roxxy.get("roxxy locker sex first"):
            rox "Mmm..."

        elif not M_roxxy.get("roxxy locker sex first"):
            if random_count <= 33:
                rox "Mmm, isso é tão gostoso!"
                player_name "... Sim, eu sei."
                player_name "Estou suando como um louco."
                rox "Eww! Isso não foi o que eu quis dizer!"
                player_name "..."
                rox "Quero dizer, alguém poderia nos pegar totalmente aqui, porra!"
                player_name "..."
                rox "Foda-se, isso é quente!"
                player_name "Você é tão estranho às vezes..."
                rox "Hehehe, cale a boca e me foda mais forte!"

            elif random_count > 66:
                rox "Ooh, me foda, {b}[firstname]{/b}!"
                player_name "..."
                rox "Foda-me mais!!"
        else:

            rox "{b}[firstname]{/b}!!!"

    elif animcounter == 2:
        if M_roxxy.get("roxxy locker sex first"):
            player_name "{b}Roxxy{/b}!!!"
            rox "Cale a boca e me foda!"
            player_name "..."
            player_name "Fine!"
            $ M_roxxy.set("sex speed", .06)
            rox "Fuuuuuck..." with hpunch
            player_name "Fique quieto, vadia!"
            rox "{b}*Whimper*{/b}"

        elif not M_roxxy.get("roxxy locker sex first"):
            if random_count > 33 and random_count <= 66:
                player_name "Ai!"
                rox "... o que?!"
                player_name "Eu bati minha cabeça no topo do armário estúpido!"
                rox "Hahaha, não seja um bebê!"
                player_name "Bem, doeu!"
                rox "Sim, e você puxa meu cabelo também dói ... Você não me ouve reclamando."
                player_name "... Por que você não disse alguma coisa? Eu teria parado."
                rox "{b}*Gasp*{/b} Não ouse parar!"
                rox "Puxe com mais força!"

            elif random_count > 66:
                player_name "Shh!!! Alguém vai ouvir você!"
                rox "Eu não me importo!"
                rox "Deixe-me ouvir!"
                rox "Isso é tão bom pra caralho!!!"
                player_name "Droga, {b}Roxxy{/b}!"
                player_name "Eles vão nos expulsar!"
                rox "{b}*Whimper*{/b}"
                rox "... Bem."
        else:

            rox "Oh Deus, oh Deus, OH DEUS!!!"

    elif animcounter == 3:
        if M_roxxy.get("roxxy locker sex first"):
            rox "Oh Deus, Oh Deus, OH DEUS!!!"
            player_name "Cale a boca e goza!!!"

        elif not M_roxxy.get("roxxy locker sex first"):
            if random_count > 33 and random_count <= 66:
                player_name "..."
                rox "Mmm! fuuuuuck yessss!!!"
        else:

            if random_count > 50:
                rox "Haaah, Estou chegando perto."
                player_name "Eu não vou durar muito tempo!"
    return

label roxxy_locker_sex_cum:
    call expression game.dialog_select("roxxy_locker_sex_cum_pre")
    if M_roxxy.get("roxxy locker sex"):
        call expression game.dialog_select("roxxy_locker_sex_cum_repeat")
    else:

        call expression game.dialog_select("roxxy_locker_sex_cum_first")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Roxxy"]["unlocked"] = True
    $ persistent.cookie_jar["Roxxy"]["gallery"]["05_unlocked"] = True
    $ M_roxxy.trigger(T_roxxy_locker_sex)
    $ player.go_to(L_school_hall)
    $ game.timer.tick()
    $ game.main()

label roxxy_locker_sex_cum_pre:
    scene expression "backgrounds/location_school_locker_inside01.jpg"
    show player locker 15_15b
    player_name "Tch!" with flash
    rox "!!!"
    rox "{b}*Gasp*{/b}!!!"
    show player locker 15
    show xray_roxxy_locker at Position (align=(0,0))
    with dissolve
    pause
    hide xray_roxxy_locker
    show player locker 16
    with dissolve
    return

label roxxy_locker_sex_cum_first:
    player_name "Você está certo?"
    show player locker 17b with dissolve
    rox "Haah... Haah..."
    rox "Sim, apenas me dê um segundo..."
    rox "Ufa"
    show player locker 17
    player_name "Isso foi loucura."
    show player locker 17b
    rox "Sim, mas foi incrível, não foi?"
    show player locker 17
    player_name "Hehe, Sim..."
    show player locker 17b
    rox "Acho que talvez tenhamos que tentar isso novamente algum dia!"
    show player locker 17
    player_name "Hã?! De jeito nenhum!"
    player_name "E se formos pegos?!"
    show player locker 17b
    rox "Hehe, só teremos que ter cuidado..."
    show player locker 17
    player_name "..."
    show player locker 17b
    rox "Vamos, levante as calças e vamos sair daqui enquanto o salão está vazio!"
    show player locker 17
    player_name "{b}*Sigh*{/b}."
    scene black with fade

    scene school
    show player 14 at left
    show roxxy 1g at right
    with dissolve
    player_name "Sério, o que trouxe isso?!"
    show player 13
    show roxxy 4
    rox "Hehe, Eu não posso dizer."
    show roxxy 1g
    show player 14
    player_name "Por que não?!"
    show player 13
    show roxxy 1h
    rox "... Porque estou planejando uma surpresa para você!"
    show roxxy 1g
    show player 12
    player_name "Hã?"
    player_name "Que tipo de surpresa?"
    show player 13
    show roxxy 1h
    rox "Hehe, apenas o tipo de surpresa {b}meu homem{/b} merece..."
    show roxxy 1g
    show player 11
    player_name "..."
    show player 13
    show roxxy 1b
    rox "Lembre-se de {b}aparecer{/b} para a festa neste fim de semana!"
    show roxxy 1g
    show player 14
    player_name "{b}Você e as meninas fazendo coisa de praia de novo?{/b}."
    show player 13
    show roxxy 1h
    rox "Sempre."
    show roxxy 1g
    show player 14
    player_name "a sim {b}Sábado à noite{/b} na {b}a praia{/b}?"
    show player 13
    show roxxy 1b
    rox "Mmmhmm."
    rox "Não se atrase!"
    show roxxy 1
    show player 14
    player_name "Hehe, tudo bem."
    show player 13
    show roxxy 1h
    rox "Até logo, {b}[firstname]{/b}."
    show roxxy 1g
    show player 14
    player_name "Thau, {b}Roxxy{/b}."
    hide player
    hide roxxy
    with dissolve
    return

label roxxy_locker_sex_cum_repeat:
    player_name "Você está certa?"
    show player locker 17b with dissolve
    rox "Haah... Haah..."
    rox "Sim, apenas me dê um segundo..."
    rox "Ufa."
    show player locker 17
    player_name "Vamos lá, vamos sair daqui!"
    scene black with fade

    scene school
    show player 10 at left
    show roxxy 1g at right
    with dissolve
    player_name "Você sabe, nós realmente não podemos continuar fazendo isso!"
    show player 5
    show roxxy 1h
    rox "Por que não?!"
    show roxxy 1g
    show player 10
    player_name "Nós vamos ser pegos, {b}Roxxy{/b}!"
    show player 5
    show roxxy 2
    rox "Você se preocupa muito!"
    show roxxy 1g
    show player 16
    player_name "..."
    show roxxy 2
    rox "Não me olhe!"
    show roxxy 48 with dissolve
    rox "Vamos lá, você sabe que eu realmente gosto disso!"
    rox "Você não vai tirar isso de mim ... Você vai?!"
    show roxxy 47
    show player 14
    player_name "{b}*Suspiro*{/b} Tudo bem, tudo bem!"
    player_name "Apenas guarde seus peitos hipnóticos!"
    show player 13
    show roxxy 4 with dissolve
    rox "Hehehe, obrigado {b}[firstname]{/b}!"
    hide player
    show roxxy 92 at left
    with dissolve
    pause
    show roxxy 59e with dissolve
    player_name "Vamos lá, temos que ir para a aula..."
    show roxxy 59d
    rox "Ooh, Sim senhor..."
    rox "Hehehe!"
    hide roxxy with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
