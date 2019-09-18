label music_classroom_dewitt_intro:
    scene music_classroom_c
    show dewitt 1 at left
    show player 14f at right
    with dissolve
    player_name "Ei, {b}Sra. Dewitt{/b}."
    show player 13f
    show dewitt 2
    dewitt "Ah minha nossa, {b}[firstname]{/b}! É você, docinho?"
    dewitt "Eu estava começando a pensar em você e pensei que você tivesse mudado de escola!"
    show dewitt 1
    show player 10f
    player_name "Hehe, não. Eu tive um pouco de \"Problemas familiares\" ."
    show player 5f
    show dewitt 2
    dewitt "Sim, ouvi falar do seu pai falecido. Que vergonha..."
    dewitt "Existe algo que eu possa fazer por você, querido?"
    show dewitt 1
    show player 10f
    player_name "Na verdade, eu esperava que pudéssemos conversar sobre recuperar minhas notas?"
    show player 5f
    show dewitt 2
    dewitt "Bem, aposto que podemos descobrir algo."
    dewitt "Por que você não escolhe um instrumento e senta-se."
    dewitt "Nós o colocaremos de volta."
    show dewitt 3
    show player 11f
    pause
    show dewitt 1
    show player 10f
    player_name "Tudo bem, qualquer instrumento em particular, {b}Ms. Dewitt{/b}?"
    show player 5f
    show dewitt 2
    dewitt "Hmm, Que tal você tentar esses tambores?"
    show dewitt 1
    show player 14f
    player_name "Sim senhora!"
    hide player
    hide dewitt
    with dissolve

    scene music_class_cs01
    with fade
    show text "Eu nunca tinha tocado bateria antes." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide music_class_cs01

    scene music_class_cs02
    with fade
    show text "Foi realmente muito difícil manter um ritmo constante, mas meio divertido..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide music_class_cs02

    scene music_class_cs03
    with hpunch
    show text "!!!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide music_class_cs03

    scene music_class_cs04
    with fade
    show text "Que bom a {b}Sra. Dewitt{/b} é tão legal comigo...\nPorque eu sou péssimo..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene music_classroom_c
    show dewitt 1 at left
    show player 37f at right
    with dissolve
    player_name "Eu sinto muito, {b}Sra. Dewitt{/b}!"
    player_name "Eu não quis"
    show player 3f at Position (xoffset=-8) with dissolve
    show dewitt 2
    dewitt "Hehehe, está tudo bem, querido."
    dewitt "Você não é a primeira pessoa a tentar bater um ritmo nessas adoráveis senhoras!"
    show dewitt 3
    show player 11f with dissolve
    player_name "..."
    show player 5f
    show dewitt 2
    dewitt "Talvez devêssemos convencê-lo de algo um pouco mais elegante?"
    dewitt "Hmm, a flauta talvez..."
    show dewitt 1
    show player 12f
    player_name "... A flauta?"
    player_name "Isso é meio feminino, não é?"
    show player 5f
    show dewitt 2
    dewitt "Oh, Deus não, docinho!"
    dewitt "Os homens tocam flauta desde a idade da pedra."
    show dewitt 1
    show player 10f
    player_name "Mesmo?"
    show player 5f
    show dewitt 2
    dewitt "É melhor você acreditar!"
    dewitt "Exércitos antigos de todo o mundo usavam a flauta para manter o ritmo em suas linhas de batalha."
    dewitt "Nada feminino sobre isso, existe?"
    show dewitt 1
    show player 12f
    player_name "Não, acho que não."
    show player 5f
    show dewitt 2
    dewitt "Talvez você deva pensar um pouco, então?"
    show dewitt 1
    show player 10f
    player_name "Talvez..."
    show player 5f
    show dewitt 2
    dewitt "Com licença, querido, mas é melhor eu controlar essa classe."
    hide player
    hide dewitt
    with dissolve

    show studyclass02 with dissolve
    show text "Passei o dia inteiro tentando tocar o ritmo..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    show studyclass03 with dissolve
    show text "... finalmente a campainha tocou." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene music_classroom_c
    show dewitt 2 with dissolve
    dewitt "Muito bem pessoal! Foi uma jam session incrível!"
    dewitt "Agora, antes que vocês saiam, preciso de um momento do seu tempo!"
    show dewitt 14 at Position (xoffset=-127) with dissolve
    dewitt "Hey!"
    dewitt "{b}Tyrone{/b}, olhos na frente!"
    show dewitt 13 at Position (xoffset=-127)
    tyrone "..."
    show dewitt 2 with dissolve
    dewitt "Agora, eu queria lembrar a todos que o show de talentos musicais está chegando, muito em breve."
    dewitt "... E ainda temos muitas vagas abertas que precisam ser preenchidos."
    show dewitt 3 at Position (xoffset=-7)
    dewitt "Lembre-se, {b}Estou oferecendo crédito extra{/b} para todos que participam."
    player_name "!!!"
    show dewitt 2
    dewitt "Eu realmente gostaria de ver o show deste ano sair sem problemas!"
    dewitt "Então, por favor, não hesite em vir falar comigo, se você estiver interessado."
    show dewitt 3 at Position (xoffset=-7)
    dewitt "Obrigado e tenha uma tarde divertida, pessoal!"
    show dewitt 1 at right with dissolve
    pause 0.5
    hide dewitt with dissolve
    pause 1

    show player 17 with dissolve
    player_name "Crédito extra é exatamente o que eu preciso!"
    show player 14
    player_name "Eu farei qualquer coisa para melhorar minha nota neste momento."
    player_name "Eu deveria {b}conversar com a Sra. Dewitt sobre o show de talentos, amanhã{/b}."
    hide player with dissolve
    return

label music_classroom_dewitt_smith_berating:
    scene music_classroom_c
    show dewitt 13 at left
    show principal 5 at right
    with dissolve
    smi "Você não pode estar seriamente avançando com esse show de talento patético novamente!"
    show principal 4 with dissolve
    smi "O ano passado não foi suficientemente embaraçoso para você?!"
    show principal 26 at Position (xoffset=-70)
    show dewitt 14
    dewitt "... Por que você faz isso todos os anos!?"
    dewitt "Eu só estou tentando incutir amor pela música nesses estudantes e todo ano você caga por toda parte!"
    show dewitt 13
    show principal 27 at Position (xoffset=-70)
    smi "Ah, Pobrezinha {b}Melodia{/b}."
    smi "Pelo menos você não terá que se preocupar com isso por muito mais tempo..."
    show principal 26 at Position (xoffset=-70)
    show dewitt 14
    dewitt "Ugh, o que você está falando agora?"
    show dewitt 13
    show principal 27 at Position (xoffset=-70)
    smi "Eu tenho uma reunião com o conselho escolar esta tarde."
    smi "Veja bem, eu contei a eles tudo sobre o dinheiro que você desperdiçou na piada de um show de talentos no ano passado..."
    smi "... E quando ele voltar a funcionar desta vez, eles já concordaram em me permitir transferir o financiamento para empreendimentos mais valiosos."
    show principal 26 at Position (xoffset=-70)
    show dewitt 14
    dewitt "Esforços mais dignos?"
    dewitt "Você pode ser uma verdadeira puta, você sabe que?"
    show dewitt 13
    show principal 5 with dissolve
    smi "Hahaha!"
    smi "Mal posso esperar para ver como você se sai dessa vez..."
    show principal 26 at Position (xoffset=-70) with dissolve
    show dewitt 14
    dewitt "*Grrr*"
    dewitt "Apenas saia da minha sala de aula, sim!?"
    show dewitt 13
    show principal 38 with dissolve
    smi "Hahahahaah!"
    hide principal with dissolve
    show dewitt 12
    dewitt "Deus, eu odeio essa mulher."
    hide dewitt with dissolve
    return

label music_classroom_dewitt_talent_show_help:
    scene music_classroom_c
    show dewitt 10b at left
    show player 10f at right
    with dissolve
    player_name "Olá, {b}Sra. Dewitt{/b}."
    show player 5f
    show dewitt 11b
    dewitt "Olá querido. Como vai?"
    show dewitt 10b
    show player 10f
    player_name "eu estou bem."
    show player 14f
    player_name "Eu quero falar com você sobre participar do show de talentos?"
    show player 13f
    show dewitt 11b
    dewitt "Bem, isso é legal!"
    show dewitt 9
    pause 2
    show dewitt 11
    dewitt "Espera. Você acabou de perguntar sobre o show de talentos?!"
    show dewitt 9
    show player 12f
    player_name "... Sim?"
    show player 5f
    show dewitt 3 with dissolve
    dewitt "Oh minha nossa!"
    show dewitt 4 with dissolve
    show player 10f
    player_name "Uhh, você está Bem, {b}Sra. Dewitt{/b}?"
    show player 5f
    show dewitt 11
    dewitt "Estou um pouco emocional é tudo."
    show dewitt 11b
    dewitt "{b}Diretora Smith{/b} está procurando alguma desculpa que possa encontrar para cancelar o show de talentos este ano."
    show dewitt 12
    dewitt "... E até agora eu só tenho um voluntário."
    show dewitt 10b
    show player 12f
    player_name "quem?"
    show player 5f
    show dewitt 11
    dewitt "{b}Tyrone{/b}."
    dewitt "... Mas eu não posso simplesmente fazer ele tocar sozinho o tempo todo!"
    show dewitt 10
    show player 14f
    player_name "Bem, eu vou participar e vou perguntar também!"
    show dewitt 4
    player_name "Talvez eu possa te encontrar mais voluntários?"
    hide player
    show dewitt 6 at right
    with dissolve
    dewitt "Oh, Deus te abençoe, docinho!"
    dewitt "Isso seria maravilhoso!"
    show dewitt 7
    pause
    show dewitt 15 at left
    show player 14f at right
    with dissolve
    player_name "Hehe, não é problema..."
    show player 13f
    show dewitt 3 with dissolve
    dewitt "{b}[firstname]{/b}, você acabou de animar meu dia de novo!"
    show dewitt 1
    show player 14f
    player_name "Ainda bem que eu posso ajudar a te fazer feliz!"
    show player 13f
    show dewitt 2
    dewitt "Um homenzinho tão doce..."
    dewitt "Qual instrumento você quer tocar?"
    show dewitt 1
    show player 14f
    player_name "Bem, eu não sei. Eu gosto dos tambores."
    show player 13f
    show dewitt 8 with dissolve
    dewitt "Hehe, Oh sim. Eu me lembro da nossa pequena bateria de ontem."
    show dewitt 15
    show player 10f
    player_name "... Mais uma vez, sinto muito por isso."
    show player 5f
    show dewitt 16
    dewitt "Não se preocupe com isso, docinho."
    show dewitt 17 with dissolve
    show player 11f
    dewitt "Essas senhoras têm o hábito de atrapalhar."
    dewitt "Você não acreditaria em como eles fazem isso para eu tocar violão."
    dewitt "... Eu acho que eles só gostam da atenção."
    show dewitt 15 with dissolve
    show player 13f
    player_name "..."
    show dewitt 5
    dewitt "De qualquer forma, receio que {b}Tyrone{/b} já tenha se inscrito para tocar bateria."
    show dewitt 16
    dewitt "Eu sei que você iria tocar com entusiasmo a partir de seu amor brincalhão de ontem."
    show dewitt 4
    show player 10f
    player_name "Então?"
    show player 12f
    player_name "Hmm, Eu não sei o que escolher..."
    show player 10f
    player_name "O que você acha?"
    show player 5f
    show dewitt 5
    dewitt "Bem, que tal a flauta?"
    show dewitt 4
    show player 12f
    player_name "Ugh, não isso de novo..."
    show player 5f
    show dewitt 8
    dewitt "Oh, Vamos!"
    show dewitt 5
    dewitt "Não há nada melhor do que um homem que sabe como lidar com sua flauta!"
    show dewitt 4
    player_name "..."
    show player 12f
    player_name "Sério?"
    show player 5f
    show dewitt 5
    dewitt "É melhor você acreditar!"
    show dewitt 8
    dewitt "Eu vou te dar aulas gratuitas!"
    show dewitt 4
    show player 10f
    player_name "Você sabe tocar flauta?"
    show player 5f
    show dewitt 16
    dewitt "Oh, Docinho. Minha habilidade com a flauta é incomparável!"
    dewitt "Eu posso fazer milagres com essa boca!"
    show dewitt 15
    show player 14f
    player_name "Bem, eu suponho que eu poderia tentar se você estiver disposto a me dar lições gratuitas."
    show player 13f
    show dewitt 16
    dewitt "Estou mais do que disposta."
    show dewitt 15
    show player 14f
    player_name "Tudo bem, acho que vou pegar a flauta então."
    show player 13f
    show dewitt 5
    dewitt "Boa decisão, {b}[firstname]{/b}!"
    dewitt "Deixe-me apenas ir buscá-lo. Um segundo."
    hide dewitt with dissolve
    pause
    pause
    show player 55f with dissolve
    player_name "{b}*Bocejar*{/b}"
    pause
    show player 13f with dissolve
    pause
    show dewitt 11 at left with dissolve
    dewitt "Bem, nós tivemos um."
    show dewitt 10b
    dewitt "Hmm. Eu me pergunto aonde foi."
    show dewitt 11
    dewitt "Eu devo ter emprestado isso no começo deste ano."
    dewitt "Eu acho que eles nunca devolveram, embora."
    dewitt "Por que você não dá uma olhada na {b}folha de inscrição do instrumento dentro do armário da sala de aula{/b}."
    show dewitt 4
    show player 14f
    player_name "Tudo bem! Vou dar uma olhada!"
    show player 13f
    show dewitt 5
    dewitt "Depressa, Docinho!"
    hide player
    hide dewitt
    with dissolve
    return

label music_classroom_music_sheet:
    scene music_classroom_c
    show music_checkout_form with dissolve
    pause
    player_name "Hmm..."
    player_name "Parece que {b}Judith{/b} foi a última pessoa a verificar a flauta da escola."
    player_name "{b}Acho que seria melhor rastreá-la{/b}!"
    hide music_checkout_form with dissolve
    $ game.main()

label music_classroom_dewitt_return_flute:
    scene music_classroom_c
    show dewitt 1 at left
    show player 14f at right
    with dissolve
    player_name "Ei, {b}Sra. Dewitt{/b}."
    player_name "Eu encontrei a flauta da escola."
    show player 13f
    show dewitt 2
    dewitt "Eu sabia que você iria, encontrar docinho!"
    show dewitt 1
    show player 10f
    player_name "... Mas tava quebrada precisando de reparo."
    show player 5f
    show dewitt 11b with dissolve
    dewitt "Quebrado!? O que nós vamos fazer?"
    show dewitt 10b
    show player 14f
    player_name "Bem, eu meio que fiz uma!"
    show player 239_240f with dissolve
    pause
    show player 567cf with dissolve
    player_name "O que você acha?"
    show player 567bf
    show dewitt 5
    dewitt "Uau! Você fez uma flauta?!"
    show dewitt 4
    show player 567cf
    player_name "Sim, em casa na minha garagem."
    show player 567bf
    show dewitt 16
    dewitt "Você é muito bom com madeira, huh?"
    show dewitt 15
    show player 567cf
    player_name "eu sei?"
    show player 567bf
    show dewitt 5
    dewitt "Se importa se eu der uma olhada mais de perto?"
    show dewitt 4
    show player 567cf
    player_name "Sure!"
    show player 13f with dissolve
    show dewitt 34 with dissolve
    dewitt "O comprimento e a circunferência são..."
    dewitt "Perfeito."
    dewitt "Quando você terminar com essa flauta, eu não me importaria de pegar emprestada por uma noite ou duas!"
    show dewitt 33
    show player 11f
    player_name "???"
    show dewitt 34
    dewitt "O que? Eu gosto de quebrar novos instrumentos!"
    show dewitt 33
    show player 14f
    player_name "Tudo bem, negocie."
    player_name "Eu tentei tocar mais cedo. Não é muito dificil!"
    show player 13f
    show dewitt 40 with dissolve
    dewitt "Ótimo! Aqui está a partitura para o concerto. Você faz parte disso  não deve ser difícil."
    dewitt "Pratique todas as noites e você estará pronto para o concerto em algum momento."
    show dewitt 4 with dissolve
    show player 386f with dissolve
    player_name "Tudo bem, {b}Sra. Dewitt{/b}. I will!"
    show player 385f
    show dewitt 5
    dewitt "Agora, se você não se importa, vamos ouvir o que você pode fazer! A aula está prestes a começar."
    show dewitt 4
    show player 386f
    player_name "Ok."
    hide player
    hide dewitt
    with dissolve

    scene music_class_cs05
    with fade
    show text "Foi estranho não estar sentado com a seção de percussão...\n... mas sentado na seção de flauta teve suas vantagens." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve
    return

label music_classroom_dewitt_talent_show_progress:
    scene music_classroom_c
    show player 13f at right
    show dewitt 2 at left
    with dissolve
    dewitt "Bem, olá, {b}[firstname]{/b}."
    dewitt "Você tem praticado os dedilhados que ensinei a você?"
    show dewitt 1
    show player 10f
    player_name "Dedilhado?"
    show player 11f
    show dewitt 8 with dissolve
    dewitt "Você sabe, na flauta, bobo."
    show dewitt 4
    show player 17f
    player_name "Oh sim! Acho que estou ficando muito bom."
    show player 14f
    player_name "Você é uma ótima professora, {b}Sra. Dewitt{/b}!"
    show player 13f
    show dewitt 5
    dewitt "Bem, você é um aprendiz rápido, Docinho."
    show dewitt 11
    dewitt "Espero que mais alunos se inscrevam em breve, caso contrário, poderemos cancelar o programa."
    show dewitt 10
    show player 12f
    player_name "Você ainda não teve nenhum voluntário?"
    show player 5f
    show dewitt 11b
    dewitt "Não, não so um."
    show dewitt 12
    dewitt "Estou começando a ficar preocupada, {b}[firstname]{/b}..."
    show dewitt 10b
    show player 14f
    player_name "Ainda há tempo, {b}Sra. Dewitt{/b}."
    player_name "Aposto que posso reunir algumas pessoas para você!"
    show player 13f
    show dewitt 11
    dewitt "Você realmente faria isso?"
    show dewitt 10
    show player 33f
    player_name "Concerteza!"
    show player 13f
    show dewitt 5
    dewitt "Oh, você é tão doce!"
    show dewitt 4
    show player 14f
    player_name "Hehe, deixa eu ver quem eu posso convencer."
    show player 13f
    show dewitt 3 with dissolve
    dewitt "Boa sorte, Docinho!"
    hide player
    hide dewitt
    with dissolve
    return

label music_classroom_dewitt_talent_get:
    scene music_classroom_c
    show dewitt 4 at left
    show dewitt 4 at Position (xpos=110)
    show player 14f at right
    with dissolve
    player_name "Eu encontrei mais dois voluntários para o show de talentos!"
    show player 13f
    show dewitt 5
    dewitt "Mesmo?! Quem você encontrou e o que eles tocam?"
    show dewitt 4
    show player 14f
    player_name "Bem, acontece que {b}Eve{/b} é uma cantora."
    show player 13f
    show dewitt 5
    dewitt "Você não diz! Ela é boa?"
    show dewitt 4
    show player 14f
    player_name "Ela tem uma voz de anjo, você não vai acreditar!"
    show player 13f
    show dewitt 5
    dewitt "Isso é maravilhoso! Quem mais você conseguiu?"
    show dewitt 4
    show player 14f
    player_name "{b}Kevin{/b} vai tocar violão."
    show player 13f
    show dewitt 5
    dewitt "Bem, agora você está me excitando! já ouvi {b}Kevin{/b} tocar antes e ele é muito talentoso."
    show dewitt 4
    show player 14f
    player_name "Sim, eu já ouvi coisas boas."
    show player 13f
    show dewitt 5
    dewitt "Senhor, {b}[firstname]{/b}! Você tem os ingredientes da sua própria banda!"
    show dewitt 8
    dewitt "De fato! Isso não é uma má ideia!"
    show dewitt 4
    show player 10f
    player_name "Huh?"
    show player 5f
    show dewitt 5
    dewitt "Para o final do show, devemos ter vocês três tocando algo juntos!"
    show dewitt 4
    show player 10f
    player_name "Mesmo?"
    show player 11f
    show dewitt 8
    dewitt "Absolutamente! Está perfeito!"
    show dewitt 4
    show player 14f
    player_name "Hehe, OK. Se é o que você quer?"
    show player 13f
    show dewitt 5
    dewitt "Oh, yay!! Mal posso esperar para ver esse show!"
    show dewitt 23 at Position (xoffset=45) with dissolve
    pause
    show dewitt 22 at Position (xoffset=45) with dissolve
    pause
    show dewitt 27 at Position (xoffset=-119) with dissolve
    pause
    show dewitt 24 at Position (xpos=110) with dissolve

    show player 23f
    player_name "!!!"

    show player 11f
    show dewitt 25 at Position (xoffset=69) with dissolve
    dewitt "Oh! Merda!"
    dewitt "Minha culpa, {b}[firstname]{/b}..."
    dewitt "Minhas meninas também estão tentando comemorar!"

    show player 14f
    player_name "Hehe, está tudo bem. Eu não me importo."
    show player 13f
    show dewitt 16 with dissolve
    dewitt "Oh, Eu aposto que não, Docinho!"
    dewitt "Eu acho que você pode considerar que uma pequena recompensa extra por todo o seu trabalho duro."
    dewitt "Se conseguirmos mostrar esse talento, posso deixar que você tenha uma visão particular."
    show dewitt 15
    show player 11f
    player_name "*Gole*."
    show dewitt 8
    dewitt "Ah, Você é tão fofo!"
    show dewitt 4
    show player 14f
    player_name "Eu provavelmente deveria voltar a praticar."
    show player 13f
    show dewitt 5
    dewitt "Agora essa é uma boa ideia. Obrigado novamente, {b}[firstname]{/b}."
    show dewitt 4
    show player 36f with dissolve
    player_name "Tchau, {b}Ms. Dewitt{/b}."
    hide player
    hide dewitt
    with dissolve
    return

label music_classroom_dewitt_music_sheets:
    scene music_classroom_c
    show kevin 23 zorder 2 at right
    show dewitt 1 zorder 3 at left
    with dissolve
    pause
    show player 13f zorder 1 at Position (xpos=700) with dissolve
    show dewitt 2
    dewitt "Oh bom você está aqui {b}[firstname]{/b}."
    dewitt "Eu estava apenas distribuindo as folhas de música."
    show dewitt 1
    show player 10f
    player_name "Folhas de música?"
    show player 5f
    show dewitt 2
    dewitt "Para o final, lembra?"
    show dewitt 1
    show player 17f
    player_name "Oh, certo. Sim, eu me lembro."
    show player 13f
    show kevin 26 with dissolve
    kev "Na verdade, é uma música bem legal!"
    show kevin 23 with dissolve
    show dewitt 2
    dewitt "Hehe, Bem, claro que é!"
    show dewitt 3
    dewitt "Olha com quem você está trabalhando aqui senhor!"
    show dewitt 1
    show player 10f
    player_name "Não deveria {b}Eve{/b} estar aqui?"
    show player 13f
    show kevin 24
    kev "Ela está aqui..."
    kev "... Ou bem, ela estava."
    show kevin 23
    show dewitt 2
    dewitt "Ela foi pegar algo do seu armário."
    show dewitt 1
    show player 14f
    player_name "Ela também gostou da música?"
    show player 13f
    show dewitt 2
    dewitt "É melhor você acreditar!"
    show dewitt 1
    show player 14f
    player_name "Parece que tudo vai dar certo então, hein?"
    show player 13f
    show dewitt 2
    dewitt "Sim, tudo graças a você, querido!"
    show dewitt 4 with dissolve
    show kevin 24
    kev "Eu não posso esperar para chegar lá e começar a tocar! A multidão vai amar isso!"
    show kevin 23
    show player 11f
    show dewitt 9
    eve "{b}Miss Dewitt{/b}!"
    show eve 2b zorder 0 at Position (xpos=500) with fastdissolve
    eve "Gente, venham rápido! Você não vai acreditar nisso!"
    show eve 1
    show dewitt 11
    dewitt "Qual é o problema, querida?"
    show dewitt 10
    show eve 2b
    eve "Alguém vandalizou o auditório!"
    show eve 1
    show kevin 24
    show player 23f
    show dewitt 11b
    dewitt "Que!?!"
    show dewitt 10b
    show eve 2b
    eve "Sim, há grafites em todo lugar!"
    show eve 1
    show player 22f
    hide dewitt with dissolve
    show eve 2bf at Position (xpos=300) with dissolve
    eve "Vamos lá pessoal!"
    hide player
    hide eve
    hide kevin
    with dissolve
    return

label music_classroom_dewitt_check_up:
    scene music_classroom_c
    show dewitt 9f at left
    show player 10f at right
    with dissolve
    player_name "{b}Miss Dewitt{/b}, você está aqui?"
    show player 11f
    show dewitt 9d with dissolve
    dewitt "Sim, eu estou bem aqui, querido."
    show dewitt 9c
    show player 10f
    player_name "Você está bem?"
    show player 11f
    show dewitt 9d
    dewitt "Oh, Eu ficarei bem. Eu estou apenas um pouco para baixo no momento."
    show dewitt 9f with dissolve
    show player 25f
    player_name "( Hmm, Eu acho que eu deveria dar a ela algum espaço por enquanto. )"
    hide player
    hide dewitt
    with dissolve
    return

label music_classroom_dewitt_find_dewitt:
    scene music_classroom_c
    show dewitt 9f at left
    show player 14f at right
    with dissolve
    player_name "{b}Miss Dewitt{/b}, você está aqui?"
    show player 13f
    show dewitt 9d with dissolve
    dewitt "Sim, estou bem aqui, Docinho."
    show dewitt 9c
    show player 10f
    player_name "Você está bem?"
    show player 5f
    show dewitt 9d
    dewitt "Oh, Eu ficarei bem. Eu estou um pouco deprimida no momento."
    show dewitt 9f with dissolve
    show player 14f
    player_name "Eu tenho uma surpresa para você!"
    show player 13f
    show dewitt 9d with dissolve
    dewitt "Eu não estou realmente com vontade de jogos, {b}[firstname]{/b}..."
    show dewitt 9c
    show player 14f
    player_name "Sem jogos. Sério, eu tenho algo que vai te animar!"
    show player 13f
    show dewitt 9d
    dewitt "Oh, querido. Você é tão doce."
    show dewitt 9c
    show player 14f
    player_name "Venha comigo!"
    show player 13f
    show dewitt 9d
    dewitt "*Suspiro* Tudo bem, liderar o caminho."
    hide player
    hide dewitt
    with dissolve
    return

label music_classroom_dewitt_talent_show_practice:
    scene music_classroom_c
    show player 13f at right
    show dewitt 2 at left
    with dissolve
    dewitt "Olá, {b}[firstname]{/b}!"
    show dewitt 1
    show player 14f
    player_name "Oi {b}Miss Dewitt{/b}!"
    show player 13f
    show dewitt 3
    dewitt "Você está pronto para práticar?"
    show dewitt 1
    show player 17f
    player_name "Pode apostar!"
    show player 13f
    show dewitt 2
    dewitt "Vá se sentar então, docinho."

    scene music_class_cs06
    with fade
    show text "Praticando com {b}Kevin{/b} e {b}Eve{/b} foi muito divertido!\nSeria um arraso no {b}Show de talentos{/b} com certeza!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene music_classroom_c
    show eve 5 at right
    show kevin 23 at Position (xpos=600)
    show player 14 at left
    with dissolve
    player_name "Essa foi uma boa sessão. Estamos indo muito bem, pessoal!"
    show player 13
    show eve 6
    eve "Sim, isso é muito divertido!"
    show eve 5
    show kevin 24
    kev "É uma pena que nunca jogaremos..."
    show kevin 24b
    show player 5
    player_name "..."
    show eve 2b
    eve "Hã? Do que você está falando, {b}Kevin{/b}?"
    show eve 1
    show kevin 24f with dissolve
    kev "Não tem jeito {b}Diretora Smith{/b} não vai deixar {b}Show de talentos{/b} realmente acontecer!"
    kev "{b}[firstname]{/b} e eu a ouvi {b}Annie{/b} conspirar."
    kev "Elas são obrigados a ter algo na manga!"
    show kevin 24bf
    show eve 2b
    eve "... Não devemos contar {b}Miss Dewitt{/b}?"
    show eve 1
    show kevin 24f
    kev "Por quê? Não há nada que ela possa fazer para impedir isso..."
    show kevin 24bf
    show player 10
    player_name "Isso só vai perturbá-la."
    show player 12
    player_name "Nós vamos ter que lidar com a {b}Diretora Smith{/b} nós mesmos!"
    show player 13
    show kevin 20 with dissolve
    pause
    show kevin 32 with dissolve
    kev "Estou dentro!"
    show kevin 23
    show eve 9f
    eve "..."
    show eve 2b
    eve "Vocês estão falando sério?"
    eve "{b}Diretora Smith{/b} vai nos expulsar em um piscar de olhos se ela nos pegar brincando com ela..."
    show eve 1
    show kevin 24f with dissolve
    kev "A sim? Você quer deixar estragar o {b}Show de talento da senhorita Dewitt{/b}?!"
    show kevin 24bf
    show eve 2b
    eve "Eu não estou dizendo isso!"
    eve "... É só ... Temos que ter cuidado! Isso é tudo."
    eve "Minha {b}irmã{/b} vai me {b}MATAR{/b} se eu for expulsa!"
    show eve 1
    show player 14
    player_name "Você não precisa se envolver, {b}Eve{/b}. {b}Kevin{/b} e eu pode lidar com isso."
    show player 13
    show eve 7
    eve "Pfft, Okay, certo!"
    show eve 6b
    eve "Mal posso esperar para ouvir o plano que vocês dois, Crânios entorpecidos sugerem!"
    show eve 6
    eve "Falhará com certeza sem minhas artimanhas femininas!"
    show eve 5
    show player 14
    player_name "Hehe, Bom. Vai ser muito mais fácil com três pessoas."
    show player 13
    show kevin 9b with dissolve
    kev "Então qual é o plano, {b}[firstname]{/b}?"
    show kevin 23
    show player 10
    player_name "Nós apenas temos que descobrir uma maneira de manter a {b}Diretora Smith{/b} e {b}Annie{/b} longe do {b}auditório{/b} mais rapido possível!"
    show player 5
    show kevin 20 with dissolve
    kev "..."
    show eve 2b
    eve "Você quer dizer, prendê-las em algum lugar?"
    show eve 1
    show player 11
    player_name "!!!"
    show player 35
    player_name "Isso não é uma má ideia..."
    show kevin 23 with dissolve
    player_name "Nós poderíamos prender a {b}Diretora Smith{/b} no escritório até o {b}Show de talentos{/b} terminar!"
    show player 13
    show eve 6
    eve "Viu, eu te disse... Artimanhas femininas!"
    show eve 5
    show kevin 9b
    kev "Sim, sim ... Estamos muito impressionados. Como exatamente nós vamos prender em seu escritório?!"
    show kevin 23
    show player 4 with dissolve
    eve "..."
    player_name "..."
    show eve 6b
    eve "O que? Eu tenho que planejar a coisa toda sozinha?!"
    show eve 1
    show player 10 with dissolve
    player_name "Bem, não podemos simplesmente trancá-la lá. Annie tem uma {b}Chave mestra{/b} para toda a escola."
    show player 5
    show kevin 24
    kev "... Sim e mesmo que ela não fizesse. a {b}Diretora Smith{/b} provavelmente a mandaria pela janela para obter ajuda."
    show kevin 23
    show eve 6
    eve "Haha, Eu pagaria para ver isso!"
    show eve 5
    show player 10
    player_name "Então, precisamos incapacitá-las de alguma forma..."
    show player 5
    show kevin 20 with dissolve
    kev "..."
    show eve 2
    eve "{b}Minha irmã{/b} tem um taser na loja ... Poderíamos usar?"
    show eve 1
    show player 10
    player_name "Isso é um pouco extremo, você não acha?"
    show player 5
    show kevin 21
    kev "Não que a {b}Diretora Smith{/b} não mereça isso..."
    show kevin 23 with dissolve
    show player 12
    player_name "Sem tasers!"
    show player 10
    player_name "... {b}Diretora Smith{/b} pode ser puro mal, mas eu não acho que {b}Annie{/b} seja..."
    player_name "Ela é apenas equivocada."
    show player 5
    show eve 2
    eve "Bem, essa é a única ideia que tenho."
    show eve 1
    show player 34
    player_name "..."
    show kevin 22 with dissolve
    kev "Espere um segundo!"
    show player 13
    kev "Eu entendi!"
    kev "Lembra o adesivo que fizemos para {b}Miss Okita{/b} na classe um tempo atrás?!"
    show kevin 23 with dissolve
    show player 10
    player_name "... Não?"
    show player 5
    show kevin 9b
    kev "Ah, é verdade, você não estava de volta à escola ainda."
    show kevin 23f with dissolve
    show eve 2
    eve "Eu lembro."
    show eve 6
    eve "Essa coisa foi insanamente pegajosa! Você precisava de um solvente químico para neutralizá-lo..."
    show eve 1
    show kevin 32f
    kev "Exatamente!"
    show player 13
    kev "Lembra como {b}Dexter{/b} colocou a mão na testa?!"
    show kevin 23f
    show eve 6
    eve "Hahaha! sim! Essa merda foi hilária!"
    eve "A {b}Miss Okita{/b} gastou vinte minutos para remover."
    show eve 5
    show player 14
    player_name "Uau! Isso é forte?"
    show player 13
    show kevin 32 with dissolve
    kev "Sim, mano! Esse material é malvado!"
    show kevin 23
    show eve 2b
    eve "Você se lembra de como fazer esse adesivo?"
    show eve 1
    show kevin 9bf with dissolve
    kev "Eu acho que sim."
    show kevin 23f
    show player 14
    player_name "Então, o que você está propondo?"
    show player 13
    show kevin 9b with dissolve
    kev "Eu estou pensando, nós nos esgueiramos no escritorio da {b}Diretora Smith{/b} à noite e cole sua cadeira no chão."
    kev "Nós também aplicamos adesivo nas almofadas! Ela ficará presa até que alguém a encontre."
    kev "Mesmo assim ... Elas vão precisar do solvente para se libertar!"
    show kevin 23
    show eve 2b
    eve "Eu odeio dizer isso, mas ... Isso é realmente brilhante!"
    show eve 5
    show player 17
    player_name "Bom trabalho, {b}Kevin{/b}!"
    show player 13
    show kevin 9b
    kev "... Eu acho que nós, homens, não somos tão estúpidos depois de tudo."
    show kevin 23
    show eve 2
    eve "Hehe, Sim, bem ... Mesmo um relógio quebrado está certo duas vezes por dia."
    show eve 5
    show player 14
    player_name "Então, precisamos reunir ingredientes ou algo assim?"
    show player 13
    show eve 1
    eve "..."
    show kevin 9b
    kev "Não, cara. Tudo o que precisamos está no laboratório de ciências."
    kev "Me encontre lá amanhã depois da aula e eu vou nos preparar um lote!"
    show kevin 23
    show player 14
    player_name "Tudo bem, nos encontraremos assim que terminar de planejar o escritório da {b}diretora Smith{/b}."
    player_name "Lembre-se, ninguém diz uma palavra para {b}Miss Dewitt{/b}. Eu não quero vê-la chateada novamente."
    hide player
    hide kevin
    hide eve
    with dissolve
    pause
    show dewitt 9c with dissolve
    dewitt "..."
    show dewitt 9d
    dewitt "Ele está passando por todo esse problema porque não quer me ver chateada?"
    show dewitt 9f
    dewitt "{b}*Chorando*{/b} Que criança maravilhosa..."
    hide dewitt with dissolve
    return

label dewitt_talent_show_helping_kevin:
    player_name "( Eu deveria convencer Kevin a participar do {b}show de talentos{/b} primeiro."
    return

label dewitt_talent_show_helping_eve:
    player_name "( Eu deveria convencer Eve a se juntar ao {b}show de talentos{/b} primeiro."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
