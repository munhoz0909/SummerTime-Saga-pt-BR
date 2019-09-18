label prom_poster:
    show expression game.timer.image("prom_poster_day{}")
    pause
    player_name "( O baile está chegando em breve. )"
    player_name "( Parece que seria um bom momento ... se eu tivesse um encontro. )"
    player_name "( É melhor eu me apressar e encontrar alguém. )"
    player_name "( Gostaria de saber quem eu poderia perguntar. )"
    $ game.main()

label school_righthallway_roxxy_go_in_auditorium:
    scene expression player.location.background_blur
    show player 642 at left
    show erik 4 at right
    with dissolve
    eri "Ei!"
    eri "E aí, cara?!"
    show erik 1
    show player 641
    player_name "Ei {b}Erik{/b}."
    player_name "Eu só estou levando esses registros para o {b}auditório{/b} para {b}Miss Dewitt{/b}..."
    show player 642
    show erik 4
    eri "Ah, à direita..."
    eri "Parece pesado!"
    show erik 1
    show player 641
    player_name "Um pouco sim."
    player_name "O que você está fazendo aqui?"
    show player 642
    show erik 4
    eri "Eu estava apenas indo para o auditório também."
    eri "Eu tenho uma pequena pausa antes da minha próxima aula e geralmente é quieto e escuro no {b}auditório{/b}."
    eri "O que é perfeito para jogar no meu computador de mão!"
    show erik 1
    show player 641
    player_name "Hmm, por que você precisa disso escuro e quieto?"
    show player 642
    show erik 5
    eri "Eu Err ... eu não sei."
    show erik 4
    eri "É apenas mais tranquilo, eu acho!"
    show erik 5
    eri "Você quer que eu ajude você a levar isso?"
    show erik 1
    show player 641
    player_name "Sem problemas."
    player_name "Qual o jogo que você esta jogando-"
    show player 642
    show erik 1b
    dex "Aww, Vamos lá {b}Becca{/b} deixe-me dar uma olhada..."
    player_name "..."
    show erik 3b
    eri "Espere um segundo. é o {b}Dexter{/b}?"
    show erik 52
    show player 641
    player_name "Sim, parece que é ele..."
    show player 642
    show erik 3b
    eri "O que diabos ele está fazendo no auditório?"
    show erik 52
    show player 641
    player_name "Não fasso idéia..."
    player_name "Devemos dar uma olhada!"
    show player 642
    show erik 3b
    eri "... Ehh, realmente?"
    show erik 52
    show player 641
    player_name "Sim cara. Vamos lá!"
    hide player
    hide erik
    with dissolve
    scene expression "backgrounds/location_school_assembly_hall_cutscene08.jpg"
    with fade
    show text "O que estava acontecendo na sala de reunião?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    pause
    scene assembly_hall_paint02_c
    show dexter 34
    show becca 2 at left
    with dissolve
    becca "{b}Dexter{/b} pare com isso!"
    becca "Ugh, foi para isso que você me chamou aqui?!"
    show becca 1
    show dexter 35
    dex "Hã?!"
    dex "Qual é o problema?"
    dex "{b}Roxxy{/b} e eu estou de folga e você está sempre vestindo essas blusas decotadas com os peitos pendurados..."
    dex "Apenas deixe-me ver por um segundo."
    show dexter 34
    show becca 2
    becca "De jeito nenhum!"
    becca "Estamos na escola!"
    becca "... E mesmo se não estivéssemos. Eu não gosto de você assim."
    show becca 1
    show dexter 35
    dex "Pare de fingir que não quer..."
    show dexter 34
    show becca 2
    becca "Não estou fingindo nada!"
    show becca 1
    show dexter 36
    dex "Ei, o que é isso no seu jeans?!"
    show becca 14 at Position (xoffset=86) with dissolve
    becca "Hmm?"
    show dexter 37 at left
    hide becca
    with dissolve
    becca "Ai! Que porra é essa? {b}Dexter{/b}!"
    show becca 14 at left
    show becca 14 at Position (xoffset=86)
    hide dexter
    show dexter 35
    with dissolve
    dex "Hahaha, Eu sempre pensei que você tinha uma bunda grande..."
    show dexter 34
    hide becca
    show dexter 38 at left
    with dissolve
    becca "Droga. Estou indo embora!"
    show dexter 40 with dissolve
    dex "Ei!"
    dex "Você não vai a lugar nenhum até eu ver esses peitos!"
    show dexter 39
    becca "O que diabos está acontecendo com você hoje?!"
    becca "Eu disse não!"
    show dexter 40
    dex "Ninguém me diz não!"
    scene black with fade
    scene expression game.timer.image("backgrounds/location_school_right_hall{}_blur.jpg")
    show player 12f at right
    show erik 51f
    with dissolve
    player_name "Nós temos que fazer alguma coisa!"
    show player 90f
    show erik 3bf
    eri "Mas... {b}Dexter{/b} vai nos matar!"
    show erik 51f
    show player 12f
    player_name "Nós não podemos apenas ficar aqui! Vamos lá!"
    hide player
    hide erik
    with dissolve
    scene assembly_hall_paint02_c
    show erik 51 at Position (xpos=950)
    show player 12f at Position (xpos=775)
    show dexter 34 at Position (xpos=400)
    show becca 16 zorder 1 at left
    with dissolve
    player_name "Afaste-se dela!"
    show player 90f
    show dexter 24 at Position (xoffset=47)
    dex "Hmm?!"
    show dexter 23 at Position (xoffset=47)
    show becca 17 with dissolve
    becca "Dane-se, {b}Dexter{/b}!"
    hide dexter
    show becca 18
    dex "Ghhurt!" with hpunch
    show dexter 41 at Position (xoffset=-80)
    show becca 2b
    with dissolve
    becca "Idiota!"
    show becca 19
    hide dexter with dissolve
    dex "*Tosse*"
    hide player
    show becca 21f at Position (xpos=421)
    with dissolve
    player_name "!!!"
    show erik 3b
    eri "Puta merda!"
    show erik 52
    show becca 19 at Position (xpos=400)
    show player 10f at Position (xpos=775)
    with dissolve
    player_name "{b}Becca{/b}, você está bem?"
    show player 11f
    show becca 20
    becca "{b}[firstname]{/b}!!!"
    becca "Eu só estava ... quero dizer, {b}Dexter{/b} estava..."
    show becca 19
    show player 12f
    player_name "Eu sei. Nós vimos..."
    show player 5f
    becca "..."
    show erik 4
    eri "Você acabou de chutar suas nozes para a lua!"
    eri "Isso foi demais!"
    show erik 1
    show becca 20
    becca "... Isso foi?"
    show becca 19
    show player 14f
    player_name "Haha, totalmente."
    show player 13f
    dex "Ugh... {b}*Tosse* *falar cuspindo*{/b}"
    show player 12f
    player_name "... Você tem certeza que está bem??"
    show player 5f
    show becca 20
    becca "{b}*Sniff*{/b} Sim, acho que sim..."
    becca "Eu nunca o vi agir assim antes!"
    show becca 19
    show player 12f
    player_name "Bem, não se preocupe. Eu não acho que ele vai tentar algo assim novamente..."
    show player 14f
    show dexter 41 zorder 0 at Position (xpos=400) with dissolve
    player_name "... Cara, você realmente o fez bem!"
    show player 13f
    dex "{b}*Tosse*{/b} Uhh... Minha ... Nads..."
    show roxxy 3cf at Position (xpos=75) with dissolve
    rox "O que diabos está acontecendo-"
    show roxxy 2cf
    rox "Qual é o problema com {b}Becca{/b}?"
    show roxxy 27f at Position (xoffset=34) with dissolve
    rox "..."
    show roxxy 28f at Position (xoffset=34)
    rox "... E por que você está segurando suas bolas, {b}Dexter{/b}?"
    show roxxy 27f at Position (xoffset=34)
    menu:
        "Contar {b}Roxxy{/b}.":
            show player 12f
            player_name "{b}Dexter{/b} estava tentando forçar {b}Becca{/b} fazer coisas com ele."
            show player 90f
            show becca 19f
            show roxxy 3cf
            with dissolve
            rox "... A sério?"
            show roxxy 3bf
            show erik 3b
            eri "Sim, nós vimos."
            show erik 52
            show roxxy 3f
            rox "Seu idiota!"
            rox "Qual é o problema com você?!"
            show roxxy 3bf
            show dexter 41 at Position (xoffset=2)
            dex "{b}*Suspiro* *Chiado*{/b} ... ajuda."
            show dexter 41 at Position (xoffset=0)
            show becca 20f
            becca "{b}*Chorando*{/b} {b}[firstname]{/b} correu e tentou detê-lo."
            show becca 19f
            show roxxy 2cf
            rox "Você enfretou {b}Dexter{/b}?"
            show roxxy 2bf
            show player 10f
            player_name "Err, meio..."
            show player 5f
            show roxxy 3cf
            rox "Você é louco?"
            rox "Você percebe que ele mataria você, certo?"
            show roxxy 3df
            show player 12f
            player_name "... Não?"
            show player 90f
            show roxxy 2f
            rox "Uhh, sim. Ele absolutamente te destruiria."
            rox "Não seja estúpido."
            show roxxy 1f f
            show dexter 41 at Position (xoffset=2)
            dex "Uhh... Você está tão morto {b}[firstname]{/b}..."
            show dexter 41 at Position (xoffset=0)
            show player 11f
            show roxxy 3f
            rox "Oh, Cale-se!"
            rox "Você não vai fazer nada!"
            show player 13f
            rox "Se isso acontecer, você será expulso com certeza!"
            rox "... E esse será o menor dos seus problemas!"
            show roxxy 3bf
            show dexter 41 at Position (xoffset=2)
            dex "..."
            show dexter 41 at Position (xoffset=0)
            show roxxy 3f
            rox "Uh Hã. Isso foi o que eu pensei."
            show roxxy 3cf
            rox "Vamos, {b}Becca{/b}. Eu vou levá-la para o vestiário."
            show roxxy 3df
            becca "..."
            show roxxy 3d with dissolve
            show becca 20f
            becca "Espere!"
            show becca 5 with dissolve
            pause
            show becca 22f at Position (xpos=457)
            hide player
            with dissolve
            show roxxy 3df
            player_name "!!!" with hpunch
            show becca 8 at Position (xpos=400)
            show player 13f at Position (xpos=775)
            with dissolve
            show roxxy 2bf
            becca "Obrigada."
            show becca 7
            show roxxy 1f f
            show player 14f
            player_name "Hehe, Eu realmente não fiz nada."
            show player 13f
            show becca 8
            becca "Sim, você fez!"
            becca "I..."
            becca "... novamente obrigada!"
            hide becca
            hide roxxy
            with dissolve
        "Permaneça em silencio.":

            show player 10f
            player_name "Eu uhh..."
            show player 5f
            player_name "..."
            show becca 20f with dissolve
            becca "{b}Dexter{/b} estava me forçando a fazer coisas indecentes!"
            show becca 19f
            show roxxy 3cf with dissolve
            rox "... A sério?"
            show roxxy 3bf
            show erik 3b
            eri "Sim, nós vimos."
            show erik 52
            show roxxy 3f
            rox "Seu idiota!"
            rox "Qual é o problema com você?!"
            show roxxy 3bf
            show dexter 41 at Position (xoffset=2)
            dex "{b}*Suspiro* *Chiado*{/b} ... ajuda."
            show dexter 41 at Position (xoffset=0)
            show becca 20 with dissolve
            becca "{b}*Chorando*{/b} {b}[firstname]{/b} correu e tentou detê-lo."
            show becca 19f with dissolve
            show roxxy 2cf
            rox "Você enfretou {b}Dexter{/b}?"
            show roxxy 2bf
            show player 10f
            player_name "Err, meio que..."
            show player 5f
            show roxxy 3cf
            rox "Você é louco?"
            rox "Você percebe que ele iria te matar, certo?"
            show roxxy 3df
            show player 10f
            player_name "... Não?"
            show player 5f
            show roxxy 2f
            rox "Uhh, sim. Ele absolutamente te destruiria."
            rox "Não seja estúpido."
            show roxxy 1f f
            show dexter 41 at Position (xoffset=2)
            dex "Uhh... Você está tão morto, {b}[firstname]{/b}..."
            show dexter 41 at Position (xoffset=0)
            show player 11f
            show roxxy 3f
            rox "Oh, Cale-se!"
            rox "Você não vai fazer nada!"
            rox "Se isso acontecer, você será expulso com certeza!"
            show player 5f
            rox "... E esse será o menor dos seus problemas."
            show roxxy 3bf
            show dexter 41 at Position (xoffset=2)
            dex "..."
            show dexter 41 at Position (xoffset=0)
            show roxxy 3cf
            rox "Uh Hã. Isso foi o que eu pensei."
            rox "Vamos, {b}Becca{/b}. Eu vou levá-lo para o vestiário."
            hide becca
            hide roxxy
            with dissolve
    show player 13f
    player_name "..."
    show erik 3b
    eri "... Então, você agora é amigo delas, não é?"
    show erik 52
    show player 14 at Position (xpos=700) with dissolve
    player_name "Sim tipo isto."
    show player 13
    show erik 4
    eri "Isso é tão incrível, cara!"
    show erik 1
    show dexter 41 at Position (xoffset=2)
    dex "{b}*Choramingar*{/b}"
    show dexter 41 at Position (xoffset=0)
    show player 11
    show erik 3b
    eri "... Uhh, nós provavelmente deveríamos sair daqui."
    show erik 52
    show player 12
    player_name "Sim vamos lá."
    hide player
    hide erik
    with dissolve
    scene school
    show player 13 at left
    show erik 4
    with dissolve
    eri "... Então, o que aconteceu após o ID falso?"
    show erik 1
    show player 14
    player_name "Acho que não posso dizer..."
    player_name "... Mas eu tenho ajudado {b}Roxxy{/b} com algumas coisas pessoais."
    show player 13
    eri "..."
    show erik 4
    eri "Oooh, Entendi. Dez quatro, cara."
    eri "Eu ouvi o que você está dizendo."
    show erik 1
    show player 14
    player_name "Hehe, o que? Acho que não..."
    show player 13
    show roxxy 3c at right with dissolve
    rox "Bem, isso foi uma bagunça..."
    show roxxy 3d
    show erik 1f with dissolve
    show player 10
    player_name "É {b}Becca{/b} está bem?"
    show player 5
    show roxxy 33 with dissolve
    rox "Sim, ela está bem."
    rox "Ela estava um pouco chocada é tudo."
    show roxxy 30 with dissolve
    rox "Não acredito que {b}Dexter{/b} fez isso!"
    rox "Quero dizer, ele fez muita merda no passado..."
    show roxxy 3c
    rox "... Mas nunca nada assustador!"
    show roxxy 3d
    show player 10
    player_name "Bem, eu estou feliz que {b}Erik{/b} e eu estava lá..."
    show player 5
    show roxxy 2
    rox "... Quem é {b}Erik{/b}?"
    show roxxy 1
    show erik 2f with dissolve
    eri "..."
    show player 12
    player_name "Umm, meu amigo {b}Erik{/b}..."
    show player 90
    show roxxy 1b
    rox "Oh, Certo!"
    rox "Desculpe, esqueci que você estava lá."
    show roxxy 1
    show erik 3bf with dissolve
    eri "... Tudo bem."
    show erik 1f
    show roxxy 1b
    rox "Então, eu ia te contar..."
    rox "As meninas e eu estamos fazendo um concurso de biquíni neste fim de semana caso você queira ir!"
    show roxxy 1
    show erik 51f
    show player 10
    player_name "Mesmo?"
    show player 14
    player_name "Isso parece incrível!"
    show player 13
    show roxxy 2
    rox "Eu sei direito?!"
    show roxxy 1b
    rox "Apenas venha para a praia {b}sábado à tarde{/b}!"
    show roxxy 1
    show erik 1f
    show player 14
    player_name "Tudo bem, eu estarei lá."
    show player 13
    show roxxy 1b
    rox "Hehe, legal."
    rox "Até mais, {b}[firstname]{/b}!"
    hide roxxy with dissolve
    pause
    show erik 4 with dissolve
    eri "Uau, cara!"
    eri "Um concurso de biquíni?!"
    eri "Isso é tão incrível!"
    show erik 1
    show player 14
    player_name "Você quer vir comigo?"
    show player 13
    show erik 3b
    eri "Ah, eu não posso."
    eri "Eu queria poder, mas eu tenho um ataque com minha guilda {b}sábado à tarde{/b}..."
    show erik 52
    show player 12
    player_name "A fala sério!"
    show player 14
    player_name "Vamos lá cara, pense em todos esses biquínis!"
    show player 13
    show erik 3b
    eri "Você é louco?! Não posso faltar um ataque da guilda no meu clã!"
    eri "Isso é 50 DKP MENOS!"
    show erik 52
    show player 10
    player_name "... Hã?"
    show player 5
    show erik 3b
    eri "É um grande negócio, cara!"
    show erik 52
    show player 14
    player_name "Hehe, tudo bem. Bem."
    player_name "Eu acho que vou sozinho então..."
    show player 13
    show erik 3b
    eri "Atire, eu tenho que ir ao laboratório de informática."
    show erik 3
    eri "Te vejo depois, cara."
    show erik 4
    show player 14
    player_name "Até a próxima, {b}Erik{/b}."
    hide player
    hide erik
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
