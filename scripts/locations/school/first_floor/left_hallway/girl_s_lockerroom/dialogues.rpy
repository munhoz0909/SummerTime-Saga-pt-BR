label girls_lockerroom_judith_in_girls_bathroom:
    scene girl_lockerroom
    show player 106 at left with dissolve
    player_name "Uau! Há um grande buraco no chão aqui..."
    player_name "( Não é à toa que eles tiveram que fechar esse vestiário! )"
    show player 90
    player_name "..."
    show player 10
    player_name "( Ainda consigo ouvir soluços. )"
    player_name "( Definitivamente tem {b}alguém aqui{/b}... )"
    hide player 10 with dissolve
    return

label girls_lockerroom_judith_toilet_first_intro:
    scene expression game.timer.image("backgrounds/location_school_locker_room_broken_stall{}.jpg")
    show judith 11 zorder 1 at Position( xpos = 310, ypos = 768) with dissolve
    window hide
    pause
    show player 106f zorder 0 at Position (xpos = 639, ypos = 768) with dissolve
    player_name "!!!"
    jud "{b}*Soluço*{/b}"
    show player 108
    player_name "{b}Judith{/b}?!"
    show judith 13
    show player 109
    jud "...Ei, {b}[firstname]{/b}."
    show judith 12
    show player 108
    player_name "Você está bem?"
    show judith 13
    show player 109
    jud "Eu só queria ficar longe de todos."
    show judith 12
    show player 108
    player_name "O que você quer dizer?"
    show judith 13
    show player 109
    jud "Ninguém gosta de mim ... E todo mundo tira sarro do meu corpo..."
    jud "...então pelo menos aqui Ninguém vai zombar de mim."
    show judith 12
    show player 108
    player_name "Você não pode deixar essas pessoas chegarem até você dessa maneira!"
    show judith 13
    show player 109
    jud "Eles estão certos eu sou feia..."
    return

label girls_lockerroom_judith_toilet_first_not_ugly:
    show player 111
    show judith 12
    player_name "Eu não acho que você é feia!!"
    show judith 15
    show player 110
    jud "...Mesmo?"
    show judith 14
    show player 111
    player_name "sim verdade!"
    player_name "Eu acho que você está muito bem!"
    show judith 15
    show player 110
    jud "Isso é ... a melhor coisa que alguém me disse..."
    show judith 14
    show player 111
    player_name "Bem, estou apenas sendo sincero ... E tenho certeza de que não sou o único que acha isso!"
    player_name "Você apenas tem que ignorar todas as coisas negativas na escola."
    show judith 15
    show player 110
    jud "acho que você está certo..."
    show judith 14
    show player 111
    player_name "De qualquer forma, devemos sair daqui e voltar para a aula."
    show judith 17
    show player 106f
    jud "Espere!!"
    jud "Fique aqui um pouco mais ... perto de {b}mim{/b}..."
    return

label girls_lockerroom_judith_toilet_first_ok:
    show judith 16
    show player 111
    player_name "Oh... Ok."
    show judith 17
    show player 110
    jud "Você se lembra do outro dia em que..."
    jud "...Nós dois estávamos no vestiário? junto com a {b}Annie{/b}?"
    show judith 16
    show player 111
    player_name "Sim"
    show judith 17
    show player 110
    jud "Bem, eu ... gostei do jeito que você me olhou."
    show judith 16
    show player 106f
    player_name "!!!"
    show judith 17
    jud "Não eram apenas seus olhos ... Seu corpo também estava reagindo."
    show judith 16
    player_name "..."
    show judith 17
    jud "Foi meu {b}seios{/b} que te fez ... Tão feliz? {b}Lá em baixo{/b}?"
    show judith 16
    show player 111
    player_name "Eu ... me desculpe!"
    show judith 17
    show player 106f
    jud "Não se desculpe!!"
    jud "...Eu realmente gostei e..."
    jud "...Fiquei imaginando se eu poderia vê-lo novamente?"
    return

label girls_lockerroom_judith_toilet_first_sure:
    show judith 16
    show player 111
    player_name "eu acho..."
    show judith 17
    show player 106f
    jud "Me deixe fazê-lo."
    hide player
    show judith 18 at Position(xpos = 447, ypos = 768)
    player_name "!!!"
    show judith 19
    window hide
    pause
    show judith 20
    window hide
    pause
    show judith 21
    window hide
    pause
    show judith 22
    window hide
    pause
    show judith 24
    jud "É tão legal..."
    jud "...E grosso."
    show judith 23
    player_name "{b}*Gasp*{/b}"
    show judith 24
    jud "Eu simplesmente amo como se sente na minha mão..."
    show judith 25_23
    pause 4
    jud "..."
    show judith 23
    jud "Você gostaria de tocar meus seios?"
    return

label girls_lockerroom_judith_toilet_first_yes:
    player_name "sim! Eu adoraria..."
    show judith 33
    player_name "..."
    show judith 34
    player_name "Uau..."
    show judith 35
    jud "Continue!"
    jud "Toque-os ... Mas seja gentil! Eles são realmente sensíveis..."
    show judith 36_37_38
    pause 4
    show judith 39 with hpunch
    jud "*Gemendo*"
    player_name "!!!"
    show judith 33
    jud "É demais. Meu corpo fica tremendo quando você toca meus mamilos..."
    show judith 4f zorder 1 at Position( xpos = 310, ypos = 768)
    show player 112 zorder 0 at Position (xpos = 639, ypos = 768)
    player_name "Eu não quis te machucar."
    show player 13f
    show judith 5f
    jud "Não, está bem! Foi muito bom ... eu sou apenas muito sensível..."
    show judith 4f
    show player 10f
    player_name "Talvez devêssemos parar..."
    show player 13f
    show judith 5f
    jud "Sim ... Obrigada por ficar comigo, me sinto muito melhor..."
    show judith 2f
    jud "...E se você quiser, poderíamos fazer isso de novo..."
    show judith 4f
    show player 17f
    player_name "Eu adoraria!"
    show judith 5f
    show player 13f
    jud "Até mais tarde."
    hide player
    hide judith
    with dissolve
    return

label girls_lockerroom_judith_toilet_first_should_stop:
    show judith 24
    player_name "Acho que deveríamos parar..."
    show judith 6f zorder 1 at Position( xpos = 310, ypos = 768)
    show player 112 zorder 0 at Position (xpos = 639, ypos = 768)
    player_name "Não podemos nos atrasar para a aula e {b}Annie{/b} poderia nos ver aqui..."
    show player 13f
    show judith 2f
    jud "Compreendo. Obrigada por ficar comigo..."
    show judith 3f
    jud "...E se você quiser, poderíamos fazer isso de novo..."
    show judith 4f
    show player 17f
    player_name "Eu adoraria!"
    show player 13f
    show judith 5f
    jud "Vejo você mais tarde então."
    return

label girls_lockerroom_judith_toilet_first_cant:
    show judith 16
    show player 108
    player_name "Eu não posso fazer isso agora, {b}Judith{/b}..."
    player_name "Além disso, devemos realmente ir ... Eu não quero me atrasar e {b}Annie{/b} poderia nos ver aqui..."
    show judith 13
    show player 109
    jud "Oh..."
    jud "Você pode ir então. Eu vou ficar aqui um pouco mais, eu acho..."
    show player 111
    show judith 14
    player_name "Tudo bem, eu te vejo mais tarde então."
    return

label girls_lockerroom_judith_toilet_should_leave:
    show judith 16
    show player 108
    player_name "Deveríamos mesmo ir ... Não quero me atrasar e {b}Annie{/b} poderia nos ver aqui..."
    show judith 13
    show player 109
    jud "Oh..."
    jud "Você pode ir então. Eu vou ficar aqui um pouco mais, eu acho..."
    show judith 14
    show player 111
    player_name "Tudo bem, eu te vejo mais tarde então."
    return

label girls_lockerroom_judith_toilet_first_ugly:
    show judith 12
    show player 108
    player_name "Eu sei, mas você tem que aprender a lidar com isso!"
    show player 109
    jud "..."
    show judith 11
    jud "{b}*Soluço*{/b}"
    show player 108
    player_name "Eu sinto Muito..."
    show player 106f
    jud "Eu só quero ficar sozinha agora."
    show player 108
    player_name "Te vejo depois, então..."
    return

label girls_lockerroom_judith_toilet_not_here:
    scene expression game.timer.image("backgrounds/location_school_locker_room_broken_stall{}.jpg")
    show player 11 with dissolve
    player_name "..."
    show player 10
    player_name "( {b}Judith{/b} não está aqui. )"
    player_name "( Ela deve estar no corredor ou em casa. )"
    show player 108f
    player_name "( Eu deveria pedir para ela entrar para {b}alguma diversão{/b}. )"
    hide player 108f
    return

label judith_toilet_replay:
    scene expression game.timer.image("toilet_stall{}")
    show judith 14 zorder 1 at Position( xpos = 310, ypos = 768)
    show player 111 zorder 0 at Position (xpos = 639, ypos = 768) with dissolve
    player_name "Ei!"
    show judith 15
    show player 110
    jud "Eu estava esperando que você viesse me ver..."
    jud "Alguém viu você entrar aqui?"
    show judith 14
    show player 108
    player_name "Acho que não?"
    show judith 14
    show player 110
    jud "Oh, DEUS..."
    jud "Emm...O que você sente vontade de fazer?"
    call screen judith_stage01

label judith_kiss:
    show player 108
    show judith 14
    player_name "Hmm... Você já beijou alguém?"
    show judith 15
    show player 110
    jud "Você quer dizer, como um ... Beijo, beijo?"
    show judith 14
    show player 17f
    player_name "Bem, sim!"
    show judith 13
    show player 110
    jud "Na verdade não..."
    show judith 14
    show player 17f
    player_name "Vamos tentar!"
    show judith 4f
    show player 110
    jud "..."
    hide player
    show judith 31_32 at Position ( xpos = 380, ypos = 768)
    with dissolve
    pause 4
    show judith 5f zorder 1 at Position( xpos = 320, ypos = 768)
    show player 13f zorder 0 at Position (xpos = 640, ypos = 768)
    with dissolve
    jud "Isso foi bom..."
    show judith 4f
    show player 17f
    player_name "Parece um pouco estranho, eu acho. Ha ha."
    show judith 5f
    show player 11f
    jud "Vamos fazer outra coisa!"
    show judith 4f
    show player 14f
    player_name "Ok..."
    call screen judith_stage02

label judith_handjob:
    show player 111
    show judith 16
    player_name "Poderíamos fazer como da última vez, eu acho?"
    show judith 17
    show player 106f
    jud "Me deixe fazê-lo."
    hide player
    show judith 18 at Position(xpos = 465, ypos = 768)
    player_name "!!!"
    show judith 19
    window hide
    pause
    show judith 20
    window hide
    pause
    show judith 21
    window hide
    pause
    show judith 22
    window hide
    pause
    show judith 24
    jud "É tão legal..."
    jud "...E grosso."
    show judith 23
    player_name "{b}*Gasp*{/b}"
    show judith 24
    jud "Eu simplesmente amo como se sente na minha mão..."
    show judith 25_23
    pause 4
    player_name "Isso é tãããão bom!"
    show judith 24
    jud "Você quer que eu pare?"
    call screen judith_stage03

label judith_keepgoing:
    show judith 25_23
    pause 4
    player_name "Isso é tãããão bom!"
    show judith 24
    jud "Você quer que eu pare?"
    call screen judith_stage03

label judith_playwithtits:
    show judith 33
    jud "..."
    show judith 35
    jud "Você gosta de senti-los?"
    show judith 34
    player_name "Sim..."
    show judith 36
    player_name "Seus seios são tão agradáveis e macios..."
    show judith 36_37_38
    pause 4
    show judith 39 with hpunch
    jud "{b}*Gemendo*{/b}"
    player_name "!!!"
    show judith 35
    jud "Você quer tentar outra coisa?"
    call screen judith_stage03

label judith_cum:
    show judith 25_23
    pause 4
    show judith 26
    pause .3
    show judith 27
    jud "..."
    show judith 28
    jud "Uau, isso é muita porra!"
    show judith 29
    player_name "Desculpa! Eu não quis fazer uma bagunça..."
    show judith 28
    jud "Está bem..."
    jud "Eu sempre quis saber como é isso!"
    show judith 30
    player_name "Ha Ha ha!"
    show judith 5f zorder 1 at Position( xpos = 300, ypos = 768)
    show player 13f zorder 0 at Position (xpos = 623, ypos = 768)
    jud "Poderíamos fazer isso de novo..."
    show player 17f
    show judith 4f
    player_name "Concerteza!"
    show player 13f
    show judith 5f
    jud "Eu também..."
    show player 2f
    show judith 4f
    player_name "Deveríamos sair daqui..."
    show player 1f
    show judith 5f
    jud "Ok!"
    $ renpy.end_replay()
    $ M_judith.set("in bathroom", False)
    $ M_judith.unforce()
    $ persistent.cookie_jar["Judith"]["unlocked"] = True
    $ persistent.cookie_jar["Judith"]["gallery"]["02_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_school_lefthallway)
    $ game.main()

label judith_pullpants:
    show judith 24
    jud "Eu não estou ... Pronto para isso ainda."
    show judith 23
    player_name "Oh... Está bem! Nós não precisamos."
    show judith 24
    jud "Talvez outra hora..."
    jud "...Quando eu me sentir um pouco mais confortável."
    show judith 23
    player_name "Eu estou bem com isso."
    show judith 24
    jud "Podemos fazer algo mais?"
    call screen judith_stage03

label girls_lockerroom_roxxy_lockerroom_event:
    scene expression game.timer.image("location_school_locker_room_broken{}_blur")
    show missy 1 at Position (xpos=400)
    show becca 1 at left
    show roxxy 3 at right
    with dissolve
    rox "É besteira total!"
    show roxxy 3d
    show becca 2
    becca "Não acredito que a {b}treinadora bridget{/b} realmente te suspendeu da equipe!"
    show becca 1
    show missy 2
    missy "Sim, ela não percebe que o time vai chupar hardcore sem você?"
    show missy 1
    show becca 6
    becca "Bem, não somos tão ruins assim."
    show becca 1
    show missy 1bf with dissolve
    missy "... Por favor. Você não pode nem fazer um toque adequado no dedo do pé!"
    show missy 2bf
    show becca 2
    becca "Ei, eu também posso!"
    show becca 6
    becca "Eu simplesmente não gosto de fazê-las, porque isso deixa meus seios doloridos!"
    show becca 8
    becca "Você entenderia se não fosse tão esperta!"
    show becca 7
    show missy 4f
    missy "Dane-se, Skank! a {b}Roxxy{/b} bem e ela tem seios maiores do que o seus!"
    show missy 4bf
    show becca 8
    becca "Pfft, Sim, bem ... Todo mundo tem peitos maiores que o seus!"
    show becca 7
    show missy 4f
    missy "Oh, é isso! Eu vou"
    show roxxy 31
    rox "Vocês duas para com isso?"
    show missy 3 with dissolve
    show roxxy 3
    rox "Concentre-se em mim e nos meus problemas!"
    show roxxy 3d
    show missy 1b
    missy "Desculpe, {b}Roxxy{/b}."
    show missy 1
    show becca 2
    becca "Eu só não sei o que te dizer..."
    show becca 1
    show roxxy 3
    rox "Bem, eu não posso mais roubar a lição de casa daquela vaca de quatro olhos."
    rox "Se eu for pego novamente, eles vão me expulsar."
    show roxxy 3d
    show missy 3
    missy "..."
    show becca 2
    becca "É o {b}Dexter{/b}?"
    show becca 1
    show missy 1
    rox "..."
    show roxxy 2
    rox "Que tem ele?"
    show roxxy 1
    show becca 2
    becca "Ele é seu namorado, não é?"
    show becca 1
    show roxxy 3c
    rox "... Sim!"
    rox "Ele é estúpido demais para me ajudar com minha lição de casa, se é isso que você está pensando..."
    rox "... Ele mal consegue ler."
    show roxxy 3d
    show missy 6
    missy "Hahaha!"
    show roxxy 31
    rox "Cale-se, {b}Missy{/b}!"
    show roxxy 3b
    show missy 1b
    missy "... Desculpa."
    show missy 1
    show becca 2
    becca "Você não precisa dele para ajudá-la a fazer a lição de casa. Apenas peça ele para roubar alguém o dever de casa para você!"
    show becca 1
    show roxxy 29
    rox "... Hmm."
    show roxxy 30
    rox "Isso não é ruim."
    rox "Eu posso continuar da mesma maneira, mas sem nenhum risco."
    show roxxy 29
    show missy 2
    missy "... assim {b}Dexter{/b} realmente não pode ler?"
    show missy 1
    show roxxy 3
    rox "... {b}Missy{/b} largue."
    show roxxy 3d
    show missy 1b
    missy "Hehe, Me desculpe, é meio engraçado."
    show missy 1
    show becca 2
    becca "Quem se importa se ele sabe ler?"
    becca "Ele é o cara mais popular da escola E ele tem um carro!"
    show becca 1
    show roxxy 2
    rox "Sim."
    rox "... E ele tem idade suficiente para nos comprar álcool!"
    show roxxy 1
    show missy 8
    missy "Você está certa, isso é definitivamente uma vantagem!"
    show missy 7
    show becca 2
    becca "Então está tudo pronto então?"
    show becca 1
    show missy 1
    show roxxy 1b
    rox "Não exatamente."
    rox "{b}Dexter{/b} pode roubar trabalho para a {b}Cadela francesa{/b} e {b}Miss Ross{/b} é fácil o suficiente para agradar."
    rox "Eu só preciso dizer a ela que ela é bonita e fingir que estou interessada em sua arte estúpida."
    show roxxy 3c
    rox "... Mas o que eu vou fazer para {b}Miss Dewitt{/b} na classe?"
    show roxxy 1
    becca "..."
    show missy 1b
    missy "Apenas pegue a flauta com {b}Becca{/b} e eu fiz."
    show missy 1
    show roxxy 3c
    rox "Ugh, a sério?"
    show roxxy 1
    show missy 1b
    missy "Sim, não é tão difícil."
    missy "... E é uma boa prática, você sabe..."
    show missy 8
    missy "... Para boquetes!"
    show missy 7
    show roxxy 2
    rox "Pfft, Okay, certo!"
    show roxxy 1
    show missy 2
    missy "Estou falando sério!"
    show missy 5
    missy "... Ou bem, é isso que {b}Minha irmã{/b} diz..."
    show missy 1
    show roxxy 2
    rox "Tocar um instrumento musical e chupar pau são duas coisas completamente diferentes, sua puta burra."
    show roxxy 1
    show missy 3
    missy "..."
    show becca 2
    becca "Sim, e sua irmã não foi demitida de seu emprego na {b}Consum-R{/b} porque ela não podia contar o registro corretamente?"
    show becca 1
    show missy 2f with dissolve
    missy "Hã?"
    show missy 4f
    missy "... Não!"
    show missy 2f
    missy "Quero dizer..."
    show missy 4f
    missy "... Cale-se, {b}Becca{/b}!"
    show missy 2bf
    show becca 4
    becca "Pffftt!!!"
    show becca 8
    becca "\"Minha irmã diz...\""
    show becca 4
    becca "Hahaha!"
    show missy 2 with dissolve
    missy "Só estou dizendo para ir com a flauta e nós podemos ajudá-la a praticar."
    show missy 1
    becca "Hahaha!"
    show becca 1
    show missy 4f with dissolve
    missy "Eu falei cala a boca, {b}Becca{/b}!!"
    show missy 2bf
    show roxxy 2
    rox "Ugh, vocês duas calem a boca..."
    show missy 1 with dissolve
    show roxxy 1b
    rox "Vamos lá, é melhor seguirmos em frente ou a {b}Cadela francesa{/b} vai nos dar uma palestra com a boca dela novamente."
    show roxxy 1
    show becca 4
    becca "Haha!"
    hide becca
    hide missy
    hide roxxy
    with dissolve

    scene expression game.timer.image("lefthall{}")
    show player 23 at left with dissolve
    player_name "( Oh porcaria! Elas estão vindo para cá! )"
    show player 22
    show roxxy 1 at Position (xpos=500)
    show missy 1f at Position (xpos=700)
    show becca 2f at right
    with dissolve
    becca "Ei, você estava nos espionando?!"
    show becca 1f
    show roxxy 3c
    rox "Que diabos você estava fazendo pervertido!"
    show roxxy 3b
    show missy 8f
    missy "Ei, {b}[firstname]{/b}."
    show missy 7f
    show roxxy 3cf at Position (xoffset=-50) with dissolve
    becca "..."
    show missy 3f
    rox "..."
    show missy 2f
    missy "Quero dizer ... Sim, que porra está fazendo nerd?!"
    show roxxy 3c with dissolve
    show missy 1f
    show player 12
    player_name "Eu não estava"
    show player 22
    show roxxy 3
    rox "Não minta!"
    show roxxy 3d
    show becca 2f
    becca "Sim, é óbvio que você estava ouvindo!"
    show becca 1f
    show player 24
    player_name "... Bem."
    show player 12
    player_name "Sim eu estava ouvindo, feliz agora?"
    show player 24
    show roxxy 3
    rox "Eugh, você é um perdedor..."
    show roxxy 3d
    show player 12
    player_name "Você sabe, tendo o {b}Dexter{/b} roubando o dever de casa das pessoas não vai funcionar..."
    player_name "Os professores vão saber que você não escreveu."
    show player 16
    show becca 8f
    becca "Pfft, Oque você sabe?!"
    show becca 7f
    show roxxy 3c
    rox "... E por que você se importa?"
    show roxxy 3d
    show player 12
    player_name "Eu não ligo!"
    player_name "Divirta-se e prove que todo mundo está certo sobre você."
    player_name "Não vai me incomodar nem um pouco..."
    hide player with dissolve
    show roxxy 29
    rox "..."
    show missy 8f
    missy "Tchau, {b}[firstname]{/b}!"
    show missy 7f
    show roxxy 3cf at Position (xoffset=-50) with dissolve
    show becca 2f
    becca "Que diabos, {b}Missy{/b}?"
    show becca 1f
    show missy 2 with dissolve
    missy "... o que?"
    scene black
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
