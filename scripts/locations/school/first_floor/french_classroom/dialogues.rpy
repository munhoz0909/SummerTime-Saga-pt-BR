label french_classroom_bissette_intro:
    scene french_class_c
    show player 1 at left with dissolve
    show teacher 2 at right with dissolve
    bis "Aí está você.!"
    show player 2 at left
    show teacher 1 at right
    player_name "Olá, {b}Miss Bissette{/b}!"
    show player 2 at left
    show teacher 5 at right
    bis "Ouça, {b}[firstname]{/b}, Eu sei que você teve alguns assuntos pessoais para cuidar, e é por isso que você esteve ausente ultimamente..."
    bis "...Mas tudo bem?"
    show player 24 at left
    show teacher 4 at right
    player_name "Sim. Eu acho que deveria estar bem..."

    show player 5
    show teacher 5
    bis "Você não é o único atrasado nas matérias você sabe."
    show teacher 4
    show player 10
    player_name "Éssa e a classe mais difícil que temos, eu acho."
    show player 5
    show teacher 2
    bis "Bem, se você precisar de alguma coisa, me avise."
    show teacher 1
    show player 14
    player_name "Obrigado, {b}Miss Bissette{/b}."
    show player 5
    show teacher 3
    bis "Oh! Isto me lembra!"
    show teacher 2
    bis "Estou implementando uma nova oportunidade de aprendizado para aqueles que tentam recuperar o atraso."
    show teacher 1
    show player 10
    player_name "Oh Sim?"
    show player 5
    show teacher 12
    bis "Vai ser um pouco mais ... um em um tipo de aprendizado..."
    bis "...E eu espero que isso estimule os estudantes."
    show teacher 13
    show player 14
    player_name "I see."
    show player 13
    show teacher 2
    bis "Por que você não toma o seu lugar e eu vou discutir isso na frente da classe."
    show teacher 1
    show player 14
    player_name "Ok."
    hide player
    hide teacher
    scene black
    with fade

    scene french_class_cs9
    with fade
    show text "{b}Miss Bissette{/b} teve um anúncio naquele dia.\nEla planejou recompensar o aluno que mostrou mais melhoria na aula após o teste final.\nEla até ofereceu aulas particulares para qualquer um que estivesse interessado." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide french_class_cs9
    scene black
    with fade

    show studyclass02 with dissolve
    show text "Passei o dia inteiro tentando alcançar meus estudos..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    show studyclass03
    with dissolve
    show text "...até que o sino tocou." at Position (xpos= 512, ypos = 700) with dissolve
    pause

    hide text
    scene black
    with fade

    pause 0.5

    show studyclass04 with dissolve
    show text "Eu esqueci o quanto a aula de francês me deixa sonolento.\nFoi uma luta para se concentrar na lição." at Position (xpos= 512, ypos = 700) with dissolve
    pause

    hide text
    show studyclass05
    with dissolve
    show text "Mas eu sempre posso contar com meus colegas para me manter acordado..." at Position (xpos= 512, ypos = 700) with dissolve
    pause

    hide text
    show studyclass06
    with dissolve
    show text "Eles estão me criticando ultimamente...\nProvavelmente, porque eu acabei de voltar e agora eu sou o centro das atenções..." at Position (xpos= 512, ypos = 700) with dissolve
    pause

    hide text
    show studyclass07
    with dissolve
    show text "Não me entenda mal embora. Eu posso ficar firme..." at Position (xpos= 512, ypos = 700) with dissolve
    pause

    hide text
    show studyclass08
    with hpunch
    show text "...mas eu acho que é assim que a escola vai.\nBem, pelo menos o dia acabou e eu posso ir para casa agora..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene french_class_c
    show teacher 2
    with dissolve
    bis "E antes de todos vocês saírem."
    bis "Qualquer aluno interessado nas sessões de reforço escolar, {b}venha falar comigo no meu escritório ou amanhã na aula!{/b}"
    show teacher 3
    bis "Au revoir!"
    hide teacher with dissolve
    return

label french_classroom_bissette_tutoring:
    scene french_class_c
    show player 5 with dissolve
    player_name "( Eu deveria falar com a {b}Miss Bissette{/b} sobre aulas particulares. )"
    player_name "( Eu vou precisar de ajuda se eu quiser passar na aula de francês. )"
    hide player with dissolve
    return

label french_classroom_bissette_study:
    scene french_class_c
    show teacher 1 at right
    show player 14 at left
    with dissolve
    player_name "Ok, eu estou pronto para começar a lição, {b}Miss Bissette{/b}."
    show player 13
    show teacher 3
    bis "Genial!"
    show teacher 2
    bis "Fique depois da aula e nós começaremos."
    show teacher 1
    show player 14
    player_name "Sim obrigado."
    hide player
    hide teacher
    with dissolve

    show studyclass02 with dissolve
    show text "Eu passo o dia inteiro tentando alcançar meus estudos..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    show studyclass03 with dissolve
    show text "...até que o sino tocou." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene classroom_night
    show teacher 7 at right
    show desk 5 at Position (xpos = 400, ypos = 768)
    with dissolve
    bis "Você está pronto para nossa primeira aula?"
    bis "sozinho."
    bis "Together."
    show teacher 9
    show desk 6
    player_name "Uhh, Sim?"
    show desk 5
    show teacher 7
    bis "Ah ah ah, voce fala frances?"
    show teacher 9
    show desk 6
    player_name "Oh! Umm, sim?"
    show desk 5
    show teacher 7
    bis "Muito bom!"
    bis "Agora, você já viu os termos atribuídos?"
    show teacher 9
    show desk 6
    player_name "Sim, eu os examinei."
    show desk 5
    show teacher 7
    bis "Quais estão incomodando você?"
    show teacher 9
    show desk 6
    player_name "Bem, eu não sou muito bom na pronúncia."
    show desk 4
    player_name "Como ... Como você diz essa palavra?"
    show desk 3
    show teacher 7f at Position (xpos=300) with dissolve
    bis "Ah, isso é velo ou la bicicletada."
    bis "Isso significa bicicleta."
    hide teacher
    show desk 8 at Position (xoffset=-29)
    with dissolve
    player_name "!!!"
    show desk 9 at Position (xoffset=-27) with dissolve
    bis "Aqui, repita depois de mim {b}[firstname]{/b}."
    show desk 10 at Position (xoffset=-27) with dissolve
    bis "Vi-loo"
    show desk 11 at Position (xoffset=-27)
    player_name "...Velow."
    show desk 10 at Position (xoffset=-27)
    bis "Não VI-loo."
    show desk 11 at Position (xoffset=-27)
    player_name "Vv...velo"
    show desk 10 at Position (xoffset=-27)
    bis "Quase, você só precisa pronunciar agora."
    show desk 11 at Position (xoffset=-27)
    player_name "...Velo."
    show desk 10 at Position (xoffset=-27)
    bis "Tres bien, mon bel homme!"
    show desk 9 at Position (xoffset=-27) with dissolve
    bis "Você está aprendendo muito rapidamente."
    show desk 11 at Position (xoffset=-27) with dissolve
    player_name "Obrigado, {b}Miss Bissette{/b}. Você é uma boa professora!"
    show desk 9 at Position (xoffset=-27) with dissolve
    bis "Ah, un tel charmeur!"
    show desk 8 at Position (xoffset=-29) with dissolve
    bis "Um jovem tão bem educado."
    show desk 9 at Position (xoffset=-27) with dissolve
    bis "Agora vamos passar para a próxima palavra."
    scene black with fade
    pause 1
    scene classroom_night
    show teacher 7 at right
    show desk 1 at Position (xpos = 400, ypos = 768)
    with dissolve
    bis "Você fez tão bem, {b}[firstname]{/b} mas está ficando tarde."
    show teacher 10
    bis "Nós deveríamos fazer isto em um outro dia, ok?"
    show teacher 9
    show desk 2
    player_name "Uau, já é tarde?"
    player_name "Eu perdi totalmente a noção do tempo."
    show desk 1
    show teacher 7
    bis "Oui, a hora, voa quando você está se divertindo!"
    bis "Você sabe, {b}[firstname]{/b}. Estou tão feliz que você se inscreveu para minhas aulas."
    bis "Isso me enche de alegria, ajudando jovens estudantes como você a ter sucesso."
    show teacher 10
    bis "É por isso que eu me tornei professora de francês."
    show teacher 9
    show desk 2
    player_name "Sim, tenho sorte de você ser minha professora {b}Miss Bissette{/b}."
    show desk 1
    show teacher 7
    bis "Ohh, tu flattes..."
    bis "Você está me fazendo corar."
    bis "Apenas continue praticando e eu acho que você será recompensado em algum momento."
    bis "Quem sabe, você pode até ganhar essa recompensa especial..."
    show teacher 9
    show desk 2
    player_name "Sim, senhora."
    show desk 1
    show teacher 7
    bis "Agora vá para casa {b}[firstname]{/b}."
    show teacher 10
    bis "Au revoir!"
    show teacher 9
    show desk 2
    player_name "Boa noite, {b}Miss Bissette{/b}."
    hide desk
    hide teacher
    with dissolve
    return

label french_classroom_bissette_smith_report:
    scene french_class_c
    show teacher 4 at right
    show principal 28f at left
    with dissolve
    smi "{b}Miss Bissette{/b}, Eu estava esperando o seu relatório de meio de mandato na minha mesa esta manhã."
    show principal 29f
    show teacher 15
    with dissolve
    bis "Je suis desole! Completamente deslizou minha mente!"
    show teacher 4 with dissolve
    show principal 27f at Position (xoffset=70)
    smi "Sim, bem, eu quero isso em minhas mãos até o final do dia!"
    show principal 28f with dissolve
    smi "...E é melhor que haja uma melhoria em relação à média do ano passado!"
    smi "A cidade não vai continuar nos financiando se nossos alunos estiverem falhando em suas aulas!"
    show principal 29f with dissolve
    show teacher 5
    bis "Oui, {b}Directrice Smith{/b}. Eu criei um novo método para inspirar os alunos."
    bis "Certamente, isso aumentará o interesse deles na aula de francês."
    show teacher 4
    show principal 27f at Position (xoffset=70)
    smi "Haha! Você não poderia inspirar um cachorro a latir..."
    show principal 29f
    show teacher 19
    bis "Mais, Madame... Com certeza você"
    show teacher 18
    show principal 27f at Position (xoffset=70)
    smi "Só me consiga esse relatório ou eu enviarei seu traseiro fedorento de volta para qualquer merda francesa da qual você tenha saído!"
    show principal 28f with dissolve
    smi "Eu entendi?!"
    show principal 29f with dissolve
    show teacher 5
    bis "...Oui, {b}Directrice Smith{/b}."
    hide principal with dissolve
    show teacher 20
    pause
    show teacher 19 at center with dissolve
    bis "Vieille Chienne en colere!"
    show teacher 18f with dissolve
    pause
    show player 10 at left with dissolve
    player_name "{b}Miss Bissette{/b}?"
    show player 5
    show teacher 5 at right with dissolve
    bis "Oh, mon Dieu!"
    show teacher 1
    show player 11
    player_name "..."
    show teacher 3
    bis "{b}[firstname]{/b}, você me assustou!"
    show teacher 1
    show player 10
    player_name "Desculpe..."
    show player 12
    player_name "Está tudo bem?"
    show teacher 4
    player_name "eu pude ouvir a {b}Diretora Smith{/b} do final do corredor..."
    show player 5
    show teacher 5
    bis "Oui. Ela está apenas querendo ver seus alunos se interessarem mais pelos franceses."
    show teacher 4
    show player 12
    player_name "Bem, ela não tem que ser tão má com isso."
    show player 5
    show teacher 3
    bis "Oh, {b}[firstname]{/b}. Você é sempre tão gentil comigo..."
    show teacher 17 zorder 1 with dissolve
    show player 11
    player_name "!!!" with hpunch
    show teacher 16
    bis "Você sabe, eu tenho vontade de falar com você sobre a próxima tarefa para suas sessões de tutorial."
    show teacher 17
    player_name "*Gole*"
    show player 10
    player_name "Tudo bem, o que você tem em mente?"
    show player 5
    show teacher 16
    bis "eu quero que você {b}escreva alguns parágrafos sobre sua comida favorita, em Francês{/b}."
    bis "Então nós vamos passar por isso juntos, sim?"
    show teacher 17
    show player 14
    player_name "Parece bom para mim."
    show player 13
    show teacher 16
    bis "... E se você escrever bem..."
    bis "Talvez eu esteja lhe dando um sabor da minha recompensa especial, sim?"
    show teacher 17
    show player 14
    player_name "Sim, Ok!"
    show player 13
    show teacher 3 at center with dissolve
    bis "Tres bien! É melhor você começar então."
    bis "Au revoir, {b}[firstname]{/b}!"
    hide teacher with dissolve
    show player 10
    player_name "Eu me pergunto qual seria a recompensa?"
    show player 5
    player_name "..."
    show player 35 with dissolve
    player_name "...E que comida devo escrever?"
    show player 14 with dissolve
    player_name "{b}Hora de visitar a biblioteca{/b} mais uma vez, eu acho."
    player_name "Aquela bibliotecária foi muito prestativa. Talvez ela pudesse encontrar um livro sobre {b}comida francesa{/b} para mim?"
    hide player with dissolve
    return

label french_classroom_bissette_hand_in_assignment:
    scene french_class_c
    show teacher 1 at right
    show player 14 at left
    with dissolve
    player_name "Eu terminei a tarefa!"
    player_name "Eu escrevi sobre o fromage."
    show player 13
    show teacher 2
    bis "Oh! Você gosta do queijo francês?"
    show teacher 1
    show player 14
    player_name "Todo queijo realmente..."
    show player 13
    show teacher 2
    bis "Hehe, Você sabe o que vai bem com o queijo não é?"
    show teacher 1
    show player 10
    player_name "...Umm, biscoitos?"
    show player 5
    show teacher 3
    bis "Não é bobo, vinho francês!"
    show teacher 12
    bis "Talvez um dia pudéssemos provar uma garrafa juntos?"
    bis "Mas primeiro devemos continuar praticando seu francês."
    bis "Fique depois da aula hoje e devemos ter o quarto só para nós."
    bis "Só você e eu, sim?"
    show teacher 13
    show player 26
    player_name "Sim, senhora."
    show player 13
    show xtra 21 at left
    show teacher 2
    bis "Oh, e antes de se sentar, adicione a foto ao quadro-negro."
    bis "Farei com que os outros alunos escrevam seus favoritos também."
    hide player
    hide xtra
    hide teacher
    with dissolve

    scene french_class_cs14
    with fade
    show text "Eu senti como se estivesse realmente ficando muito bom com o francês.\nEu estava entendendo mais e mais a cada dia.\nA aula particular com a {b}Miss Bissette{/b} tinha definitivamente feito a linguagem mais interessante." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve

    show studyclass02 with dissolve
    show text "Passei o dia inteiro tentando alcançar meus estudos..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    show studyclass03 with dissolve
    show text "...até que o sino tocou." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene classroom_night
    show desk 12 at Position (xpos = 400, ypos = 768)
    with dissolve
    bis "Estou muito orgulhosa de sua última missão."
    bis "Você está se tornando bastante ... fluente."
    show desk 13
    player_name "Sim? Estou feliz que você gostou. Eu trabalhei muito duro nisso."
    show desk 12
    bis "Tenho certeza que você fez, mon bel homme."
    bis "Você está pronto para a próxima aula de reforço?"
    show desk 13
    player_name "Yes."
    show desk 12
    bis "Vamos falar mais algumas palavras."
    scene black with fade

    scene classroom_night
    show desk 16 at Position (xpos = 400, ypos = 768)
    bis "Sua pronúncia está ficando muito boa, {b}[firstname]{/b}."
    bis "Eu acho que você definitivamente ganhou..."
    show desk 19 with dissolve
    bis "...Estou tão orgulhosa de você."
    show desk 20 with dissolve
    bis "Oh, mon Dieu!"
    bis "Todo esse novo conhecimento crescendo..."
    bis "Ce qu'il est enorme ce lapin..."
    show desk 19 with dissolve
    player_name "..."
    show desk 14 with dissolve
    bis "Qual é o problema, {b}[firstname]{/b}?"
    show desk 15
    player_name "E se alguém..."
    show desk 14
    bis "Ah, Tellement mignon..."
    show desk 17 with dissolve
    bis "Não se preocupe."
    show desk 18 with dissolve
    bis "Aqui."
    bis "Isto deve tirar sua mente de suas preocupações..."
    player_name "*Gole*"
    show desk 24 with dissolve
    player_name "Sim..."
    show desk 25 with dissolve
    pause
    show desk 26 with dissolve
    bis "Oh, oui! Joue avec mes seins, {b}[firstname]{/b}!"
    show desk 24 with dissolve
    player_name "Você tem certeza, a {b}Diretora Smith{/b} não vai entrar?"
    show desk 5 at Position (xoffset=-58)
    show teacher 10c at right
    with dissolve
    bis "Oh non! j'ai oublie!"
    bis "Eu esqueci de entregar o relatório de meio de mandato!"
    bis "Me perdoe, {b}[firstname]{/b}. Temo que devemos parar por hoje."
    show teacher 10b
    show desk 6 at Position (xoffset=-58)
    player_name "Ok, {b}Miss Bissette{/b}..."
    show desk 5 at Position (xoffset=-58)
    show teacher 10c
    bis "Vamos retomar isso da próxima vez, sim?"
    bis "Eu terei uma nova tarefa esperando por você amanhã."
    show teacher 10b
    show desk 6 at Position (xoffset=-58)
    player_name "Certo, {b}Miss Bissette{/b}."
    show desk 5 at Position (xoffset=-58)
    show teacher 10
    bis "Au revoir, mon petit lapin!"
    show teacher 9
    show desk 6 at Position (xoffset=-58)
    player_name "Au revoir."
    hide desk
    hide teacher
    with dissolve
    return

label french_classroom_bissette_poem_assignment:
    scene french_class_c
    show player 13 at left
    show teacher 2 at right
    with dissolve
    bis "Bonjour, {b}[firstname]{/b}!"
    show teacher 1
    show player 14
    player_name "Bonjour, {b}Miss Bissette{/b}."
    show player 13
    show teacher 2
    bis "Comentário allez-vous?"
    show teacher 1
    show player 14
    player_name "Oh umm, estou indo bem."
    show player 13
    show teacher 3
    bis "Maravilhoso!"
    show teacher 2
    bis "Você está aprendendo o francês tão rapidamente!"
    show teacher 1
    show player 14
    player_name "Sim, acho que sua aula está realmente ajudando."
    show player 13
    show teacher 12
    bis "Ah, devemos continuar com as lições, sim?"
    show teacher 13
    show player 14
    player_name "Com prazer."
    show player 13
    show teacher 12
    bis "Eu estou pensando que você vai aproveitar esta próxima tarefa..."
    show teacher 13
    show player 14
    player_name "Oh, Mesmo?"
    show player 13
    show teacher 12
    bis "Oui, beaucoup..."
    bis "Você está familiarizado com romance francês?"
    show teacher 13
    show player 10
    player_name "Não, não realmente..."
    show player 11
    show teacher 16 zorder 1 with dissolve
    bis "On apprend alors!"
    bis "Os franceses fazem os melhores amantes do mundo!"
    show teacher 17
    show player 26
    player_name "...Oh? Eu não sabia disso..."
    show player 13
    show teacher 16
    bis "Oui, {b}[firstname]{/b}, isso é conhecido!"
    bis "Então, para lhe dar uma visão sobre isso ... Você precisa {b}escrever um poema romântico em francês!{/b}"
    show teacher 17
    show player 10
    player_name "Err, Eu não sei, senhora. Eu nunca escrevi nada assim antes."
    player_name "Eu nem saberia como começar..."
    show player 13
    show teacher 25 with dissolve
    bis "Não seja Ridículo!"
    show teacher 26 with dissolve
    bis "Você é natural, eu tenho fé em você {b}[firstname]{/b}!"
    show teacher 27 with dissolve
    show player 14
    player_name "Hehe. ok, {b}Miss Bissette{/b}."
    show player 13
    show teacher 25 with dissolve
    bis "Tres Bien, mon bel homme!"
    show teacher 26 with dissolve
    bis "Eu sei que você vai escrever algo que derreta meu coração!"
    show teacher 16 with dissolve
    bis "Volte para mim quando terminar."
    bis "Talvez você finalmente vai ganhar a recompensa que você está procurando, sim?"
    show teacher 17
    show player 11
    player_name "*Gole*"
    show player 26
    player_name "Sim! Ok!"
    show player 13
    show teacher 16
    bis "Estou ansiosa por isso!"
    show teacher 17
    show player 14
    player_name "Eu voltarei em breve, {b}Miss Bissette{/b}."
    show player 13
    show teacher 16
    bis "Au revoir, {b}[firstname]{/b}."
    hide teacher with dissolve
    show player 29 with dissolve
    player_name "Uau!!!"
    player_name "Ok, eu acho {b}Eu deveria ir para a biblioteca{/b} e ver o que posso encontrar sobre poesia e romance franceses."
    hide player with dissolve
    return

label french_classroom_bissette_hand_in_poem_assignment_pre:
    scene french_class_c
    show teacher 1 at right
    show player 386 at left
    with dissolve
    player_name "Aqui, {b}Miss Bissette{/b}. Eu terminei o poema."
    show player 13 with dissolve
    show teacher 23 with dissolve
    bis "Superbe!"
    bis "Oh, comme c'est beau!"
    bis "Sim, isso vai fazer bem."
    bis "A aula é um deleite."
    show teacher 24
    show player 10
    player_name "Hã? O que você quer dizer?"
    show player 5
    show teacher 2 with dissolve
    bis "Bem, você vai recitar durante a aula, sim?"
    show teacher 1
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "De jeito nenhum!"
    show player 11
    show teacher 12
    bis "Quoi? Venha agora, {b}[firstname]{/b}."
    bis "Suas palavras são lindas ... Seria errado não compartilhar uma coisa dessas, sim?"
    show teacher 13
    show player 10
    player_name "Absolutamente não! Eu ficaria muito envergonhado!"
    show player 22
    show teacher 2
    bis "Ah, não seja tão medroso, {b}[firstname]{/b}."
    show teacher 11
    pause
    show teacher 2
    bis "Já sei! Eu vou te dar uma parceira para ler com você!"
    bis "Isso é vai ser menos embaraçoso, ok?"
    show teacher 1
    show player 12
    player_name "... Na verdade não."
    show player 23
    show teacher 19
    bis "{b}Roxxy{/b}, acorde!"
    show player 22
    show teacher 18
    rox "Hmm?"
    show teacher 19
    bis "Fille paresseuse! Acorda, eu disse!"
    show teacher 18
    rox "O que?!"
    show teacher 19
    bis "Venha cá!"
    show teacher 20
    pause
    pause
    show roxxy 27f at Position (xpos=500) with dissolve
    show player 24
    show teacher 19
    bis "Desde que você não pode ser incomodada para escrever um poema para a aula, você estará recitando um poema com {b}[firstname]{/b} aqui."
    show teacher 18
    show roxxy 30f
    rox "Uhh, não eu não vou."
    show roxxy 29f
    show player 22
    show teacher 19
    bis "Sim você vai!"
    show teacher 18
    show roxxy 30f
    rox "Eu não me importo com essa tarefa estúpida!"
    show roxxy 29f
    show teacher 19
    bis "Quoi?! Comment oses-tu!"
    bis "Você vai chegar até lá e ler ou vai para a detenção até o final do prazo!"
    bis "Comprenez vous?!"
    show teacher 20
    show roxxy 30f
    rox "A sério?!"
    show roxxy 29f
    show teacher 19
    bis "AGORA!"
    show teacher 18
    show roxxy 30f
    rox "Grrr, está bem!"
    hide roxxy with dissolve
    show player 10
    player_name "Umm, {b}Miss Bissette{/b}?"
    show player 5
    show teacher 2
    bis "Sim, {b}[firstname]{/b}?"
    show teacher 1
    show player 10
    player_name "Eu realmente não quero fazer isso..."
    show player 5
    show teacher 2
    bis "Aww mas é tão lindo..."
    show teacher 16 zorder 1 with dissolve
    bis "Faça isso por mim, mon bel homme!"
    show teacher 26 with dissolve
    bis "... Eu vou te dar uma recompensa especial se você fizer isso..."
    show teacher 27
    show player 25
    player_name "{b}*Suspiro*{/b}"
    show player 24
    player_name "... Tudo bem, eu vou fazer isso."
    show player 5
    show teacher 12 at center
    bis "Tres bien!"
    bis "estou tão orgulhosa!"
    show teacher 1
    hide player with dissolve
    show teacher 2
    bis "Não não! Em francês! Agora vamos começar!"
    hide teacher with dissolve

    scene french_class_cs11
    with fade
    show text "Eu não estava animado para recitar meu poema na frente da turma.\n...mas {b}Roxxy{/b} realmente me ajudou.\nNinguém se importava com a fragilidade do poema; Não com {b}Roxxy{/b} tropeçando em todas as outras palavras." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve

    scene french_class_cs13
    with fade
    show text "No momento em que chegamos ao fim {b}Roxxy{/b} estava muito envergonhada.\nNossos colegas estavam rindo de suas habilidades de pronúncia pobres.\nEla estava para explodir! Eu não me lembro de tê-la visto tão brava..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve
    return

label french_classroom_bissette_hand_in_poem_assignment_roxxy_sex:
    scene french_class_c
    show player 13 at Position (xpos=500)
    show roxxy 29f at left
    show teacher 2 at right
    with dissolve
    bis "Tres Bien!"
    bis "{b}[firstname]{/b}, seu francês foi perfeito!"
    show teacher 1
    show player 14
    player_name "Obrigado, {b}Miss Bissette{/b}."
    show player 13
    show teacher 19
    bis "... E {b}Roxxy{/b}..."
    bis "... Bem, você tentou."
    show teacher 18
    rox "Grrr..."
    show teacher 2
    bis "Muito bem, é para hoje todo mundo."
    bis "Lembre-se de estar completando sua lição de casa e eu vou te ver amanhã, sim?!"
    hide teacher
    with dissolve
    show player 25f with dissolve
    player_name "...{b}Roxxy{/b}, Me desculpe por isso!"
    show player 11f
    show roxxy 3f with dissolve
    rox "EU A ODEIO!!!"
    show roxxy 29f
    show player 10f
    player_name "... {b}Roxxy{/b}, a sério! Você tem que se acalmar..."
    show player 11f
    show roxxy 31f
    rox "ACALME-SE?!"
    rox "Eu não vou me acalmar!"
    show roxxy 30f
    show player 24f
    rox "Aquela boca de piroca tem algum tipo de prazer doentio de me envergonhar!"
    rox "Skank francês!"
    rox "Ela tem sorte de eu não chutar a bunda dela aqui agora!"
    show roxxy 29f
    show teacher 19 at right with dissolve
    bis "Que se passe-t-il!?"
    bis "O que é isso  porque está gritando!?"
    show teacher 18
    show player 22
    show roxxy 30f
    rox "Eu não posso acreditar que você me fez fazer isso!"
    rox "Você sabe o quanto estou envergonhada?!"
    show roxxy 29f
    show teacher 12
    bis "Bah, não seja tão bebê..."
    bis "{b}[firstname]{/b} escreveu um lindo poema!"
    show teacher 19
    bis "Você deveria estar se desculpando com ele por sua recitação desajeitada."
    show teacher 13
    show roxxy 31f
    rox "QUE?! Ele não é aquele que você montou para parecer ridículo!"
    show roxxy 3f
    show teacher 19
    bis "Shush toi!!"
    bis "Não é minha culpa você se envergonhar com seu pobre francês!"
    bis "Você é aquela que se recusa a fazer seus estudos!"
    show teacher 18
    show roxxy 30f
    rox "Grrrr!!!"
    rox "Eu não vou esquecer isso!"
    hide roxxy with dissolve
    show teacher 19
    bis "Bom! Lembre-se, como uma razão para levar seus estudos mais a sério!"
    show teacher 18
    show player 25
    player_name "Uau, eu nunca a vi tão louca antes..."
    show player 5
    show teacher 12
    bis "Você deveria falar com ela, {b}[firstname]{/b}."
    bis "Ensine-a a estar mais no controle de seu temperamento..."
    show teacher 13
    show player 34
    player_name "..."
    show player 5
    show teacher 12
    bis "... Mas primeiro, começamos suas aulas, sim?"
    show teacher 13
    show player 14
    player_name "Sim! Ok!"
    show player 13
    show teacher 12
    bis "Tres Bien! Venha e sente-se comigo!"
    scene black with fade
    return

label french_classroom_bissette_hand_in_poem_assignment_no_roxxy_sex:
    scene french_class_c
    show player 13 at Position (xpos=500)
    show roxxy 29f at left
    show teacher 2 at right
    with dissolve
    bis "Tres Bien!"
    bis "{b}[firstname]{/b}, seu francês foi perfeito!"
    show teacher 1
    show player 14
    player_name "Obrigado, {b}Miss Bissette{/b}."
    show player 13
    show teacher 19
    bis "... E {b}Roxxy{/b}..."
    bis "... Bem, você tentou."
    show teacher 18
    rox "Grrr..."
    show teacher 2
    bis "Muito bem, é para hoje todo mundo."
    bis "Lembre-se de estar completando sua lição de casa e eu vou te ver amanhã, sim?!"
    hide teacher with dissolve
    show player 25f with dissolve
    player_name "...{b}Roxxy{/b}, Me desculpe por isso!"
    show player 11f
    show roxxy 3f with dissolve
    rox "Cale-se!"
    show roxxy 29f
    show player 10f
    player_name "...Estou apenas tentando te acalmar!"
    show player 11f
    show roxxy 31f
    rox "EU DISSE CALA A BOCA!"
    rox "Eu não posso acreditar que ela me fez ler essa besteira na frente de toda a turma!"
    show roxxy 30f
    show player 24f
    rox "Ugh, e com você e todas as pessoas!"
    rox "Repugnante!"
    rox "Você tem sorte de eu não chutar sua bunda aqui agora!"
    show roxxy 29f
    show teacher 19 at right with dissolve
    bis "Que se passe-t-il!?"
    bis "O que é isso porque está gritando!?"
    show teacher 18
    show player 22
    show roxxy 30f
    rox "Eu não posso acreditar que você me fez fazer isso!"
    rox "Você sabe o quão embaraçoso foi!?"
    show roxxy 29f
    show teacher 12
    bis "Bah, não seja um bebê assim..."
    bis "{b}[firstname]{/b} escreveu um belo poema!"
    show teacher 19
    bis "Você deveria estar se desculpando ele por sua recitação desajeitada."
    show teacher 13
    show roxxy 31f
    rox "Pedir desculpas?! Para ele?! Você está fora de sua mente!"
    show roxxy 3f
    show teacher 19
    bis "Shush toi!!"
    bis "Não é nossa culpa você se envergonhar com seu pobre francês!"
    bis "Você é aquela que se recusa a fazer seus estudos!"
    show teacher 18
    show roxxy 30f
    rox "Grrrr!!!"
    rox "Eu não vou esquecer isso!"
    hide roxxy with dissolve
    show teacher 19
    bis "Bom! Lembre-se, como uma razão para levar seus estudos mais a sério!"
    show teacher 18
    show player 25
    player_name "Uau, eu nunca a vi tão louca antes..."
    show player 5
    show teacher 12
    bis "Não se preocupe com ela, {b}[firstname]{/b}."
    bis "Ela vai superar isso."
    show teacher 13
    show player 34
    player_name "..."
    show player 5
    show teacher 12
    bis "Agora, acho que é hora de começarmos suas aulas, sim?"
    show teacher 13
    show player 14
    player_name "Sim! OK!"
    show player 13
    show teacher 12
    bis "Tres Bien! Venha e sente-se comigo!"
    scene black with fade
    return

label french_classroom_bissette_hand_in_assignment_intro_continue:
    show studyclass02 with dissolve
    show text "Passei o dia inteiro tentando alcançar meus estudos..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    show studyclass03 with dissolve
    show text "...até que o sino tocou." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene classroom_night
    show desk 16 at Position (xpos = 400, ypos = 768)
    bis "Seu progresso com o frances é muito impressionante, {b}[firstname]{/b}."
    bis "Eu acho que você vai se sair muito bem no grande exame."
    show desk 15
    player_name "Acredito que sim! Eu realmente preciso passar essa classe."
    show desk 19 with dissolve
    bis "Aww, mon bel homme..."
    show desk 20
    bis "Não fique tão ansioso..."
    player_name "*Gole*"
    show desk 16 with dissolve
    bis "Você sabe, eu me lembro de te prometer uma recompensa especial por recitar hoje, sim?"
    show desk 15
    player_name "Concerteza..."
    show desk 16
    bis "Seu poema foi realmente lindo, sabe?"
    bis "A língua francesa foi feita para poesia. Você não acha?"
    show desk 15
    player_name "Sim, senhora."
    show desk 16
    bis "Eu realmente gostei da parte que você escreveu sobre o beijo."
    show desk 15
    player_name "Oh... aquela parte?"
    show desk 16
    bis "Você conheceu o beijo francês de uma maneira especial?"
    show desk 15
    player_name "Mmm... Hã? Quero dizer, eles fazem?"
    show desk 16
    bis "Oui, eles chamam de beijo francês e tudo..."
    show desk 15
    player_name "Oh sim, eu já ouvi falar disso."
    show desk 16
    bis "Você já tentou o beijo francês antes?"
    return

label french_classroom_bissette_hand_in_poem_assignment_have_kissed:
    scene classroom_night
    show desk 15
    player_name "Sim, um pouquinho."
    show desk 16
    bis "Oh vraiment?"
    show desk 15
    bis "Você deve me mostrar o que sabe!"
    player_name "Mesmo?"
    show desk 16
    bis "Oui."
    show desk 27 at Position (xpos=342) with dissolve
    pause
    show desk 28 with dissolve
    pause
    show desk 31_32 with dissolve
    pause
    pause
    show desk 30
    bis "{b}[firstname]{/b}!"
    bis "Eu estou muito impressionado!"
    bis "Onde você aprendeu a beijar assim?"
    show desk 29
    player_name "Oh, você sabe ... Aqui e ali..."
    show desk 30
    bis "Hehe, bem. Guarde seus segredos. Apenas contanto que você me dê mais beijos!"
    show desk 31_32 with dissolve
    pause
    pause
    return

label french_classroom_bissette_hand_in_poem_assignment_havent_kissed:
    scene classroom_night
    show desk 15 at Position (xpos=400)
    player_name "Não..."
    show desk 16
    bis "Oh, Je dois t'apprendre!"
    show desk 15
    player_name "...Você quer me ensinar?"
    show desk 16
    bis "Oui."
    show desk 27 at Position (xpos=342) with dissolve
    pause
    show desk 28 with dissolve
    pause
    show desk 31_32 with dissolve
    pause
    pause
    show desk 30
    bis "Tres Bien, {b}[firstname]{/b}..."
    bis "Você é natural pelo que estou vendo."
    show desk 29
    player_name "Sim, obrigado!"
    show desk 31_32 with dissolve
    pause
    pause
    return

label french_classroom_bissette_hand_in_poem_assignment_continue:
    scene classroom_night
    show desk 31_32 at Position (xpos=342)
    bis "Mmm..."
    bis "Mon bel homme..."
    bis "Você está me deixando toda excitada..."
    player_name "*Gole*"
    bis "Talvez devêssemos levar isso"
    show desk 33 with hpunch
    "*Bzzt*"
    smi "{b}Miss Bissette{/b}!"
    "*Bzzt*"
    "*Bzzt*"
    smi "Onde está voce? Você esqueceu a nossa reunião?!"
    smi "Não me faça descer até lá e arrastar sua bunda magra para o meu escritório!"
    smi "VEM AQUI NESSE INSTANTE!"
    "*Bzzt*"
    show desk 30
    bis "Sacrebleu! O que ela quer agora?!"
    bis "*Ahem* Eu sinto Muito, {b}[firstname]{/b}. Parece que devemos parar mais uma vez."
    show desk 29
    player_name "Está tudo bem, {b}Miss Bissette{/b}. Compreendo."
    show desk 31_32 with dissolve
    pause
    show desk 30
    bis "Mmm, Ta {b}bouche{/b} est magique!"
    show desk 29
    player_name "Hã?"
    show desk 30
    bis "Sua {b}boca{/b} é mágica!"
    show desk 29
    player_name "Oooh, {b}bouche{/b} significa {b}boca{/b}?"
    show desk 30
    bis "Oui."
    show desk 27 with dissolve
    pause
    show teacher 10 at right
    show desk 5
    with dissolve
    bis "eu quero que você {b}Venha ao meu escritório depois da aula amanhã{/b}."
    bis "Há mais uma coisa que eu quero sua ajuda antes do exame."
    show teacher 9
    show desk 6
    player_name "Certo."
    player_name "Vejo você amanhã, {b}Miss Bissette{/b}."
    show desk 5
    show teacher 10
    bis "Au revoir, mon bel homme."
    hide teacher with dissolve
    player_name "..."
    show desk 34
    player_name "Ufa, isso foi demais!"
    hide desk with dissolve
    return

label french_classroom_bissette_smith_final_report:
    scene french_class_c
    show teacher 1 at right
    show principal 27f at left
    show principal 27f at Position (xoffset=70)
    with dissolve
    smi "Eu não sei como você conseguiu, mas a média de pontos está aumentando."
    show principal 26f at Position (xoffset=70)
    show teacher 2
    bis "Eu te disse que eu poderia inspirá-lo!"
    show teacher 1
    show principal 27f at Position (xoffset=70)
    smi "Sim, bem. Não pense que é uma desculpa para começar a faltar!"
    show principal 26f at Position (xoffset=70)
    show teacher 2
    bis "Não se preocupe, meus alunos me dão 110%%!"
    show player 14 at Position (xpos=500)
    player_name "Bom Dia, {b}Miss Bissette{/b}."
    show player 113
    player_name "...E {b}Diretora Smith{/b}."
    show player 13
    show teacher 12
    bis "Bonjour, {b}[firstname]{/b}."
    show teacher 13
    show player 114
    show principal 29f
    smi "Hmph."
    hide player with dissolve
    show principal 26f at Position (xoffset=70)
    show teacher 12
    bis "... Alguns me dão até mais do que 110%%!"
    show teacher 13
    show principal 29f
    smi "..."
    show principal 28f with dissolve
    smi "Apenas lembre-se, eu estou de olho em você!"
    hide principal
    hide teacher
    with dissolve
    return

label europe_map_dialogue:
    scene expression "backgrounds/location_school_french_map.jpg"
    player_name "..."
    player_name "Parece certo..."
    player_name "{b}Miss Bissette{/b} ainda não notou alguém substituir seu mapa da Europa."
    pause
    $ A_europe.unlock()
    $ game.main()

label french_class_roxxy_lolipop_intro:
    scene french_class_c
    show roxxy 6f at Position (xpos=500)
    show teacher 19 at right
    with dissolve
    bis "Eu espero que você esteja tendo algo para mim hoje!"
    bis "Você não pode continuar com a aparição de mãos vazias {b}Roxanne{/b}!"
    show teacher 18
    show roxxy 10f at Position (xoffset=9) with dissolve
    rox "Ugh, todos me chamam de {b}Roxxy{/b}..."
    rox "Não {b}Roxanne{/b}!"
    show roxxy 6f with dissolve
    show teacher 5
    bis "Por que isso?"
    bis "Seu nome é {b}Roxanne{/b}..."
    bis "Está dizendo isso nos registros da escola!"
    show teacher 4
    show roxxy 7f
    rox "{b}*Suspiro*{/b}"
    show roxxy 5f
    rox "Olha, vou fazer o dever de casa pra você hoje, tudo bem?!"
    show roxxy 10f at Position (xoffset=9) with dissolve
    rox "... Saia da minha bunda, por favor!"
    show roxxy 6f with dissolve
    show teacher 18
    bis "Hmm?"
    show teacher 19
    bis "Eu não estou fazendo nada demais..."
    show teacher 18
    show roxxy 7f
    rox "..."
    show teacher 19
    bis "Basta ter sua lição de casa pronta para a aula, sim?"
    show teacher 18
    show roxxy 11f at Position (xoffset=9) with dissolve
    rox "Eu disse que vou terminar!"
    show roxxy 9f at Position (xoffset=9)
    show teacher 19
    bis "... Putain, mais quelle branleuse..."
    hide teacher with dissolve
    pause
    show player 13 at left
    show roxxy 10f at Position (xoffset=9)
    rox "Grr, boca de piroca estúpida..."

    show roxxy 7 at Position (xpos=600) with dissolve
    rox "!!!"
    show roxxy 10 at Position (xoffset=-9) with dissolve
    rox "Você novamente!"
    show roxxy 3b with dissolve
    show player 11
    player_name "..."
    show roxxy 3c
    rox "Por que parece que você está sempre por perto?!"
    show roxxy 3d
    show player 10
    player_name "Não sei?"
    player_name "Não é exatamente uma escola grande..."
    show player 5
    show roxxy 2
    rox "Bem, estou ficando enjoada de ver sua cara idiota!"
    show roxxy 1
    rox "..."
    show roxxy 1h
    rox "... Espere um segundo."
    rox "Você tem o {b}Dever de casa francês{/b} para hoje?"
    show roxxy 1g
    show player 12
    player_name "... Sim."
    show player 5
    rox "..."
    show roxxy 47 with dissolve
    rox "{b}*Ahem*{/b}"
    show roxxy 48
    rox "Eu disse idiota?"
    rox "Porque o que eu quis dizer foi..."
    rox "... Bonito!"
    rox "Sim, é isso!"
    show roxxy 47
    show player 11
    player_name "..."
    show roxxy 48
    rox "Você já trabalhou?"
    show roxxy 47
    show player 12
    player_name "Por que você está agindo estranha?"
    show player 5
    rox "..."
    show player 12
    player_name "... Ah, Entendir."
    player_name "Você quer o meu {b}Dever de casa francês{/b}."
    show player 90
    show roxxy 50b with dissolve
    pause
    show roxxy 50 with dissolve
    rox "Bem, se você está oferecendo..."
    show roxxy 49
    player_name "Hmph..."
    show player 30
    player_name "... E o que eu ganho?"
    show player 90
    show roxxy 50
    rox "Uhh, o privilégio de ajudar a garota mais bonita da escola?"
    show roxxy 49
    player_name "..."
    show player 30
    player_name "Você realmente acha que é a garota mais bonita da escola?"
    show player 17
    player_name "Haha!"
    show roxxy 31
    rox "{b}*Gasp*{/b} como?!" with hpunch
    rox "... Eu vou"
    show roxxy 3d
    show player 12
    player_name "Você vai o que?!"
    show player 90
    show roxxy 29
    rox "..."
    show roxxy 3
    rox "Grr, você vai me ajudar ou não?!"
    show roxxy 29
    show player 35
    player_name "Hmm, Eu suponho que eu poderia deixar você copiar meu trabalho."
    show player 34
    show roxxy 4
    return

label french_class_roxxy_lolipop_just_once:
    show player 12
    player_name "... Mas não pense que eu vou te dar o meu trabalho o tempo todo."
    player_name "Eu posso sentir um pouco de pena de você, mas isso não significa que eu vou deixar você andar por cima de mim."
    show player 90
    show roxxy 2
    rox "Você sente muito por mim?!"
    show roxxy 1
    show player 10
    player_name "Bem, você está prestes a ser reprovada na escola..."
    show player 5
    show roxxy 3c
    rox "Dane-se, {b}[firstname]{/b}..."
    show roxxy 3d
    show player 11
    player_name "..."
    show player 10
    player_name "Você quer o dever de casa ou não?"
    show player 5
    show roxxy 3
    rox "... Sim."
    show roxxy 3d
    show player 14
    player_name "... peça, \"Por favor.\""
    show player 13
    show roxxy 3c
    rox "!!!"
    show roxxy 3b
    rox "..."
    show player 12
    player_name "Ah que saber ... Esqueça!"
    show player 90
    show roxxy 3
    rox "Não, espere!"
    show roxxy 3b
    rox "..."
    show roxxy 3c
    rox "... Por favor."
    show roxxy 3d
    show player 12
    player_name "Por favor, o que?"
    show player 90
    show roxxy 3
    rox "{b}*Suspiro*{/b}"
    show roxxy 3c
    rox "Por favor, posso copiar sua lição de casa."
    show roxxy 3b
    show player 4 with dissolve
    player_name "..."
    show player 12
    player_name "Sim, ok."
    player_name "Eu vou {b}pegar no meu armário{/b}."
    player_name "Volto logo."
    hide player with dissolve
    rox "..."
    show roxxy 3
    rox "Idiota..."
    hide roxxy with dissolve
    return

label french_class_roxxy_lolipop_for_lolipop:
    show player 14
    player_name "Se você me der seu pirulito..."
    show player 13
    show roxxy 3c
    rox "O que?"
    show roxxy 3d
    show player 14
    player_name "Esse pirulito que você estava chupando."
    show player 12
    player_name "Me dê isto."
    show player 90
    show roxxy 10 at Position (xoffset=-9) with dissolve
    rox "..."
    show roxxy 11 at Position (xoffset=-9)
    rox "A sério?"
    show roxxy 10 at Position (xoffset=-9)
    show player 17
    player_name "Sim."
    show player 13
    show roxxy 13 at Position (xoffset=-55) with dissolve
    rox "Uhh, isso é muito estranho, mas tudo bem..."
    show roxxy 12 at Position (xoffset=-55)
    show player 90
    player_name "..."
    show player 92
    player_name "Não está molhado o suficiente."
    show player 90
    show roxxy 13 at Position (xoffset=-55)
    rox "!!!"
    rox "Você é nojento!"
    show roxxy 12 at Position (xoffset=-55)
    show player 92
    player_name "Ei, você quer o dever de casa ou não?"
    show player 90
    rox "..."
    show roxxy 13 at Position (xoffset=-55)
    rox "Está bem!"
    show roxxy 7 with dissolve
    pause
    show roxxy 8 at Position (xoffset=-2) with dissolve
    pause
    show roxxy 12 at Position (xoffset=-55) with dissolve
    rox "Aqui, Perv!"
    show player 97
    show roxxy 3b
    with dissolve
    player_name "Obrigado!"
    show player 93 with dissolve
    show player 94
    player_name "Eu vou {b}pegar no meu armário{/b}."
    player_name "Volto logo."
    hide player with dissolve
    show roxxy 14
    rox "..."
    show roxxy 3c
    rox "Esquisito..."
    hide roxxy with dissolve
    return

label frenchclassroom_roxxy_dexter_alcohol_fight:
    scene french_class_c
    show player 4 at left
    with dissolve
    player_name "( Hmm? )"
    show player 5 with dissolve
    player_name "( É {b}Roxxy{/b} matando aula hoje? )"
    player_name "( Isso não é bom, {b}Miss Bissette{/b} pode expulsar ela... )"
    show eve 2 at right with dissolve
    eve "{b}[firstname]{/b}!"
    show eve 5
    show player 14
    player_name "Oi, {b}Eve{/b}."
    player_name "Estás bem?"
    show player 13
    show eve 2
    eve "{b}Roxxy{/b} e {b}Dexter{/b} estão indo novamente para a {b}quadra de basquete{/b}!"
    show player 11
    eve "Vamos, vamos sentir falta!"
    show eve 5
    show player 10
    player_name "Novamente?!"
    player_name "Tudo bem vamos."
    hide player
    hide eve
    with dissolve
    return

label frenchclassroom_roxxy_ask_exam_copy:
    scene french_class_c
    show roxxy 32 at right
    show teacher 2f at left
    with dissolve
    bis "É bom que suas notas estejam finalmente melhorando, {b}Roxxy{/b}."
    bis "... Mas devo lembrá-lo sobre os próximos exames."
    bis "Eles vão fazer uma grande parte do seu grau geral."
    bis "Se você deixar de passá-los, temo que teremos que suspender você da torcida novamente..."
    show teacher 3f
    bis "Talvez para sempre desta vez."
    show teacher 1f
    show roxxy 2b with dissolve
    rox "!!!"
    show teacher 2f
    bis "Você deve estar estudando muito, sim?"
    bis "O exame cobrirá todo o material que aprendemos este ano."
    show teacher 3f
    bis "Incluindo as partes que você negligenciou."
    show teacher 1f
    show roxxy 2c
    rox "... mas"
    rox "Eu não..."
    show roxxy 3b
    show teacher 3f
    bis "Ah Ah Ah!"
    bis "Seu tempo é desperdiçado com essa discussão, {b}Roxxy{/b}."
    show teacher 12f
    bis "Melhor gastar seu tempo estudando, sim?"
    hide teacher with dissolve
    show roxxy 1o with dissolve
    pause
    show player 14 at left with dissolve
    player_name "Ei Roxxy"
    show player 11
    player_name "..."
    show player 10
    player_name "Está tudo bem?"
    player_name "Você parece meio triste."
    show player 5
    show roxxy 3 with dissolve
    rox "Ugh, essa boca de piroca vai me tirar da equipe novamente!"
    show roxxy 3d
    show player 12
    player_name "Do que você está falando?"
    show player 5
    show roxxy 3
    rox "{b}Miss Bissette{/b}!"
    rox "Se eu não passar no exame, eles vão me suspender novamente do time de líderes de torcida."
    show roxxy 3d
    show player 12
    player_name "... Achei que suas notas estavam melhorando?"
    show player 5
    show roxxy 2
    rox "Sim, mas eu preciso saber as coisas que cobrimos no início deste ano."
    show roxxy 3c
    rox "O que diabos eu vou fazer, {b}[firstname]{/b}?"
    rox "Cheerleading é a única parte da escola que eu realmente gosto."
    show roxxy 3d
    show player 10
    player_name "{b}Roxxy{/b}..."
    show player 5
    show roxxy 3
    rox "Eu não posso gastar todo o meu tempo estudando...."
    rox "... Não com tudo o que vem acontecendo em casa ultimamente."
    show roxxy 32 with dissolve
    player_name "..."
    show roxxy 33
    rox "O que eu vou fazer, {b}[firstname]{/b}?!"
    show roxxy 32
    show player 10
    player_name "Eu não sei."
    show player 5
    show roxxy 33b
    pause
    show roxxy 32
    show player 4 with dissolve
    player_name "Hmm..."
    show player 35 with dissolve
    player_name "... Ei, espere um segundo!"
    player_name "Seus amigos não disseram algo sobre a {b}Diretora Smith{/b} mantendo cópias dos exames em sua casa?"
    show player 13 with dissolve
    show roxxy 33
    rox "Hmm?"
    show roxxy 32
    show player 14
    player_name "{b}Becca{/b} e {b}Missy{/b}!"
    player_name "Elas estavam falando sobre isso no vestiário no outro dia..."
    show player 13
    show roxxy 33
    rox "Foram elas?"
    rox "... Eu costumo ignorar metade do que essas idiotas dizem."
    show roxxy 32
    show player 29 with dissolve
    player_name "Hehe, Tenho certeza que é disso que elas estavam falando."
    show player 13 with dissolve
    show roxxy 1l
    rox "... Mas você não pensa..."
    rox "Quero dizer, tem que ser feito, certo?"
    show roxxy 1k
    show player 10
    player_name "Hmm, Não sei."
    player_name "{b}Diretora Smith{/b} é uma aberração de controle depois de tudo."
    show player 14
    player_name "É possível que ela tenha cópias em sua casa."
    show player 13
    show roxxy 1g with dissolve
    rox "..."
    show roxxy 1h
    rox "Tudo bem, eu acho que você vai ter que entrar e encontrá-los para mim..."
    show roxxy 1g
    show player 23
    player_name "O que?! Eu?!"
    show player 22
    show roxxy 2
    rox "Bem, sim!"
    show roxxy 1
    show player 12
    player_name "De jeito nenhum!"
    player_name "São suas notas! vai você!"
    show player 90
    show roxxy 2c
    rox "Você vai me obrigar a fazer isso?!"
    show roxxy 2
    rox "Eu pensei que você fosse um homem de verdade..."
    show roxxy 1
    show player 5
    player_name "..."
    show roxxy 2
    rox "Um homem de verdade não faria a garota fazer coisas perigosas como essa!"
    show roxxy 1
    show player 10
    player_name "Bem, sim mas..."
    show roxxy 48 at Position (xoffset=-34) with dissolve
    show player 433
    rox "Vamos por favor, {b}[firstname]{/b}. Por favor..."
    show roxxy 47 at Position (xoffset=-34)
    player_name "..."
    show roxxy 48 at Position (xoffset=-34)
    rox "Você não vai ser meu cavaleiro de armadura brilhante mais uma vez?!"
    show roxxy 47 at Position (xoffset=-34)
    show player 427
    player_name "EU EU humm..."
    show player 434
    show roxxy 50c at Position (xoffset=-34) with dissolve
    rox "Basta pensar sobre o que {b}Becca{/b} e {b}Missy{/b} vai dizer quando eu lhes digo como você é corajoso."
    rox "Eu posso dizer a elas tudo sobre a próxima vez que estivermos juntos na praia!"
    show roxxy 50 at Position (xoffset=-23) with dissolve
    rox "Lembra da praia, {b}[firstname]{/b}?"
    rox "... Lembra do nosso joguinho de girar a garrafa?"
    show roxxy 49 at Position (xoffset=-23)
    show player 427 with dissolve
    player_name "{b}*Gole*{/b} Sim..."
    show player 434
    show roxxy 48 at Position (xoffset=-34)
    rox "Você vai me ajudar, não vai?"
    show roxxy 47 at Position (xoffset=-34)
    show player 427 with dissolve
    player_name "Uh hã..."
    show player 434
    show roxxy 4 with dissolve
    rox "Hehehe! Eu sabia que você faria!"
    rox "Obrigado, {b}[firstname]{/b}!"
    show roxxy 1
    show player 24
    player_name "{b}*Suspiro*{/b}"
    show player 10
    player_name "Eu acho, {b}devemos ir para a casa dela esta tarde{/b}?"
    show player 5
    show roxxy 2c
    rox "Hã?!"
    show roxxy 2
    rox "Não, essa é uma ideia terrível!"
    show roxxy 1
    show player 12
    player_name "Como é que é uma ideia terrível??"
    player_name "Ela vai estar aqui na escola."
    show player 90
    show roxxy 2
    rox "Você não pode invadir a casa de alguém em plena luz do dia!"
    rox "Os vizinhos vão chamar os policiais para você com certeza!"
    show roxxy 1
    show player 10
    player_name "Sim mas..."
    show player 5
    show roxxy 1b
    rox "Você deveria entrar {b}à noite{/b}!"
    rox "{b}Diretora Smith{/b} geralmente ela fica aqui até tarde, então você deve ter bastante tempo."
    show roxxy 1
    show player 30
    player_name "Espere um segundo..."
    player_name "Você vem comigo, certo?"
    show player 90
    show roxxy 50 at Position (xoffset=-23) with dissolve
    rox "Pfft, este corpo não foi feito para correr {b}[firstname]{/b}..."
    show player 433
    rox "Eu só te atrasaria."
    show roxxy 49 at Position (xoffset=-23)
    show player 434
    player_name "..."
    show roxxy 48 at Position (xoffset=-34) with dissolve
    rox "Além disso, um homem grande e forte como você..."
    rox "Não precisa de ajuda, não é?"
    show roxxy 47 at Position (xoffset=-34)
    show player 427
    player_name "... hum uh."
    show player 434
    show roxxy 2 with dissolve
    rox "Hehe, fico feliz em ouvir!"
    show roxxy 1
    show player 24
    player_name "{b}*Suspiro*{/b}"
    show player 10
    player_name "Ok, eu acho que {b}Eu vou invadir a casa da diretora Smith hoje à noite{/b}."
    show player 25
    player_name "... Sozinho."
    show player 5
    show roxxy 1b
    rox "Você consegue, {b}[firstname]{/b}!"
    show roxxy 2
    rox "{b}Só não esqueça os exames{/b}!"
    show roxxy 1
    show player 12
    player_name "Sim, eu não vou."
    show player 90
    show roxxy 4
    rox "Boa sorte!"
    hide roxxy
    hide player
    with dissolve
    pause
    show player 37 with dissolve
    player_name "..."
    player_name "Eu realmente concordei em entrar na casa da {b}Diretora Smith{/b}?!"
    show player 10 with dissolve
    player_name "Como diabos {b}Roxxy{/b} me convenceu a fazer?!"
    show player 4 with dissolve
    player_name "Lembro-me de pensar que era uma má ideia e depois..."
    show player 11 with dissolve
    pause
    show player 10
    player_name "as Mamas."
    show player 11
    pause
    show player 24
    player_name "Ela é astuta..."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
