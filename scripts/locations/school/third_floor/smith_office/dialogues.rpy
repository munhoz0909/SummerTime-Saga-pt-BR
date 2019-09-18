label principals_office_delivery_invoice:
    scene office_clear
    show ronda chair at Position (xoffset=-320,yoffset=-55)
    show principal 22_23f at Position(xpos = 600, ypos = 764)
    player_name "!!!" with hpunch
    player_name "O que"
    show principal 25f
    smi "Qual o significado disso?!"
    show principal 24f
    ann "Sinto muito, senhora!"
    scene expression game.timer.image("office{}")
    show annie 3f at Position (xpos=375)
    show player 168b at left
    show titty 1f at right
    show principal 26 at Position (xpos=614)
    with dissolve
    ann "Eu não percebi!"
    show annie 9f
    show principal 27
    smi "Você sabe que não deve me interromper quando estou disciplinando os malfeitores!"
    show principal 26
    ron "Eu não fiz nada de errado!"
    show principal 2
    smi "SILENCIO!"
    show principal 1
    ann "..."
    show principal 28 at Position (xoffset=-54) with dissolve
    smi "O que é isso {b}[firstname]{/b} O que está carregando?"
    show principal 26 with dissolve
    show annie 1f
    show player 168c
    player_name "{b}*Gole*{/b} É uhh, leite ... senhora."
    player_name "E para cafeteria."
    show player 168b
    show annie 9f
    show principal 27
    smi "Oh certo, a entrega que eu pedi."
    smi "O que está fazendo no meu escritório?!"
    show principal 26
    show player 168c
    player_name "{b}Annie{/b} disse"
    show player 168b
    show principal 27
    smi "Eu não ligo para o que {b}Annie{/b} diz!"
    show annie 6f
    smi "Leve isso para o refeitório, imediatamente!"
    show principal 26
    show player 168c
    player_name "{b}*Suspiro*{/b} Descendo as escadas?"
    show player 168b
    show principal 27
    smi "... Algum problema?"
    show principal 26
    show player 168c
    player_name "Eu ... desculpe, é muito pesado e eu já carreguei até aqui..."
    show player 168b
    show principal 27
    smi "Ugh..."
    show principal 28 at Position (xoffset=-54) with dissolve
    smi "Apenas {b}peça Ronda{/b} e ela o ajudará a carregar para baixo."
    show principal 26 with dissolve
    ron "O que?! Por que eu tenho que ajudar"
    show principal 27
    smi "É uma punição boa o suficiente para você eu estou cansado de ouvir sua boca falando!"
    show principal 26
    show player 168c
    player_name "Ok."
    hide titty
    hide principal
    hide player
    hide annie
    with dissolve
    return

label principals_office_no_entry:
    scene expression game.timer.image("office{}")
    show principal 5 at right with dissolve
    show player 1 at left with dissolve
    smi "O que você está fazendo aqui?!"
    show player 11 at left
    show principal 3 at right
    player_name "Oh... umm..."
    show player 21 at left
    player_name "Eu estava ... procurando o banheiro!"
    show player 22 at left
    show principal 4 at right
    smi "Não se faça de bobo comigo, {b}[firstname]{/b}!"
    smi "Eu não acabei de mandar você ir pára a aula??!"
    show player 10 at left
    show principal 1 at right
    player_name "Bem..."
    show player 22 at left
    show principal 2 at right
    smi "Agora saia do meu {b}ESCRITORIO{/b}!!!"
    hide player 22 at left with dissolve
    hide principal 2 at right with dissolve
    return

label principals_office_no_entry_night:
    scene expression L_school_floor3.background_blur
    show player 10 with dissolve
    player_name "Eu não posso ir lá agora..."
    hide player with dissolve
    return

label principals_office_smith_intro:
    scene expression game.timer.image("office{}")
    show player 10 at left
    show principal 1 zorder 0 at Position(xpos=0.65, ypos=1.0)
    show annie 1 zorder 1 at right
    with dissolve
    player_name "Você queria me ver, {b}Diretora Smith{/b}?"
    show player 11
    show principal 27
    smi "De fato, {b}[firstname]{/b}."
    smi "Precisamos discutir suas notas e se você pretende ou não se formar."
    show player 10
    show principal 1
    player_name "É tão ruim assim?"
    show player 11
    show principal 4b with dissolve
    smi "Dê uma olhada você mesmo..."
    show expression ReportCard() zorder 2 with dissolve
    show player 23
    player_name "( !!! )" with hpunch
    pause
    hide expression ReportCard() with dissolve
    show player 10
    show principal 1 with dissolve
    player_name "Oh cara, estou ruim em tudo?!"
    show player 11
    show principal 27
    smi "eu te disse..."
    show principal 1
    show annie 3
    ann "É o que acontece quando você falta a escola por um mês!"
    show player 10
    show annie 1
    player_name "Eu não estava faltando! Meu pai morreu!"
    show player 11
    show principal 2
    smi "Fique em silencio, {b}Annie{/b}!"
    show principal 1
    show annie 3
    ann "Desculpe senhora."
    show principal 27
    show annie 1
    smi "... Independentemente das circunstâncias."
    smi "Você precisará {b}encontrar uma maneira de elevar essas notas{/b} se você não quiser repetir no próximo ano."
    smi "Eu sugiro você que {b}fale com seus professores{/b} sobre recuperar o que você perdeu."
    smi "Talvez elas possam criar algumas {b}crédito extra{/b} atribuições ou algo assim?"
    show player 10
    show principal 1
    player_name "Sim ok."
    show player 11
    show principal 27
    smi "Faça o que for preciso!"
    show player 10
    show principal 1
    player_name "Sim, senhora."
    show player 11
    show principal 27
    smi "Bom, agora vai para a aula."
    show player 10
    show principal 1
    player_name "... Na verdade, senhora?"
    show player 11
    show principal 27
    smi "Yes?"
    show player 10
    show principal 1
    player_name "Esqueci a combinação no meu armário. Você pode me ajudar a abrir?"
    show player 11
    show annie 4
    ann "Como assim, você esqueceu?!"
    ann "Todos foram instruídos no início do ano a escrever suas combinações!"
    show player 10
    show annie 1
    player_name "Eu umm..."
    player_name "eu perdi a combinação!"
    show player 11
    show annie 5
    ann "Pfft, típico."
    show annie 1
    show principal 27
    smi "Isso é muito decepcionante, {b}[firstname]{/b}."
    smi "Teremos que lhe dar uma nova fechadura."
    show principal 1
    player_name "..."
    show principal 27
    smi "Mandarei {b}Annie{/b} para baixo com a {b}Chave mestra{/b} agora..."
    smi "Eu sugiro que você obtenha tudo o que precisa agora."
    smi "Pode demorar um pouco até que o novo bloqueio chegue."
    show player 10
    show principal 1
    player_name "Sim, senhora."
    show player 11
    show principal 27
    smi "Vá para lá de uma vez, E leve sua bunda para a aula depois que terminar!"
    $ M_smith.trigger(T_smith_go_to_locker)
    $ game.main()
    return

label principals_office_smith_go_to_locker:
    scene expression game.timer.image("office{}")
    show player 11 at left
    show principal 1 zorder 0 at Position(xpos=0.65, ypos=1.0)
    show annie 4 zorder 1 at right
    with dissolve
    ann "Não {b}Diretora Smith{/b} vou em seguida?!"
    show annie 3
    ann "Vá para {b}seu armário{/b} e eu te encontro lá!"
    $ game.main()
    return

label principals_office_smith_no_desk:
    scene expression game.timer.image("office{}")
    show player 11 at left
    show principal 1 zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    smi "O que você está fazendo?"
    show principal 2
    smi "Dê o fora do meu escritório!" with hpunch
    $ game.main()
    return

label principals_office_annie_trouble:
    scene expression game.timer.image("office{}")
    show principal 6 at right
    show player 11 at left
    with dissolve
    ann "{b}Diretora Smith{/b}?"
    show principal 7 at right
    smi "O que é isso?"
    show principal 6 at right
    ann "Relatando reincidentes como você pediu!"
    show principal 9 at right
    smi "{b}[firstname]{/b}?"
    show principal 8 at right
    ann "Sim, senhora. Ele estava sendo inapropriado no vestiário!"
    show principal 9 at right
    smi "Você já não tem problemas suficientes?"
    smi "Com suas notas reprovadas em tudo..."
    show player 10 at left
    show principal 13
    player_name "Uh, Sim, senhora!"
    show player 11 at left
    show principal 9
    smi "... E, no entanto, você sente a necessidade de causar problemas no vestiário também?"
    show principal 7 at right
    smi "O que aconteceu exatamente, {b}Annie{/b}?"
    show principal 6 at right
    ann "Bem... ele ... Ele estava mostrando partes inapropriadas do corpo para as garotas no vestiário, senhora."
    show principal 9 at right
    smi "É verdade {b}[firstname]{/b} ?"
    show player 10 at left
    player_name "Bem ... eu posso explicar!"
    show player 22 at left
    show principal 10 at right with hpunch
    smi "{b}SILÊNCIO{/b}!!!"
    show principal 9 at right
    show player 5 at left
    smi "...Eu preciso ver exatamente o que aconteceu. Mostre-me agora."
    show principal 6 at right
    ann "Senhora, não vai funcionar..."
    ann "Isso só parece acontecer quando ... ele vê mulheres {b}nuas{/b}, Senhora."
    show principal 7 at right
    smi "Bem, o que você está esperando, {b}Annie{/b}?"
    smi "Você vai ter que ajudá-lo com isso."
    show principal 11 at right
    show player 11 at left
    ann "{b}O que??!{/b}"
    show principal 12 at right
    smi "Você foi quem testemunhou a infração..."
    smi "...É seu {b}dever{/b} executar o relatório!"
    player_name "Realmente não precisamos fazer isso"
    show principal 10 at right
    show player 22 at left
    smi "Ninguém vai embora até eu receber um relatório completo! Faça isso, ou vocês dois estão em {b}DETENÇÃO{/b}!!!"
    show principal 13 at right
    ann "..."
    show player 8 at left
    show principal 14 at right
    window hide
    pause
    show player 63 at left
    show principal 15 at right
    window hide
    pause
    show principal 16 at right
    show player 64 at left
    smi "Agora, olhe para aqueles {b}seios firmes{/b} dela..."
    show principal 17 at right
    smi "Você quer ... chupar eles? {b}[firstname]{/b}?"
    show player 65 at left
    player_name "..."
    show player 66 at left
    window hide
    pause
    show player 66 at left with hpunch
    window hide
    pause
    show player 67 at left
    smi "Aqui vejamos..."
    show principal 18 at right
    smi "É o bastante, {b}Annie{/b}. Você pode sair agora..."
    show principal 5 at right with dissolve
    smi "assim!..."
    smi "Isto é o que eu tenho ouvido sobre esse tempo todo."
    hide player 67 at left
    show principal 19 at left
    with dissolve
    smi "Você ganhou uma reputação na escola..."
    smi "Eu posso ver porque..."
    smi "...isso tem sido uma..."
    show principal 20 at left
    window hide
    pause
    show principal 21 at left with hpunch
    window hide
    pause
    smi "...Distração!"
    show player 69 at left
    show principal 1 at right
    with dissolve
    player_name "Me desculpe, senhora!"
    player_name "Isso não vai acontecer novamente, eu prometo!"
    show principal 5 at right
    show player 68 at left
    smi "Tudo bem jovem: ouça..."
    smi "Não vou mandá-lo para detenção, contanto que você mantenha esse...seu \"problema\"  ... para si mesmo."
    smi "Minha prioridade é ordem e disciplina nesta escola, e pretendo mantê-la assim!"
    show principal 1 at right
    show player 69 at left
    player_name "Sim, {b}Diretora Smith{/b}!"
    show principal 2 at right
    show player 68 at left
    smi "Agora saia do meu {b}ESCRITORIO{/b}!!"
    hide player 68 at left with dissolve
    hide principal 2 at right with dissolve
    $ renpy.end_replay()
    return

label principals_office_dewitt_paint_trail:
    if M_dewitt.is_state(S_dewitt_paint_trail):
        scene smith_office_spying
        show annie spying 1
        show principal spying 2
        with dissolve
        smi "Você deveria ter visto seus rostos!"
        smi "Devastação completa e absoluta!"
        smi "Hahaha!"
        show principal spying 1
        show annie spying 2
        ann "Eles acreditavam que era {b}Tyrone{/b} e sua gangue como você planejou?"
        show annie spying 1
        show principal spying 2
        smi "Não, {b}Dewitt{/b} sabe que eu tive algo a ver com isso, mas ela não pode provar nada."
        show principal spying 1
        show annie spying 3
        ann "Sinto muito, senhora. Eu tentei o meu melhor para parecer um monte de vanda-los."
        show annie spying 1
        show principal spying 2
        smi "Sim, sim, tenho certeza que você fez."
        smi "Eu simplesmente não consigo tirar essa imagem da minha mente!"
        smi "Pobrezinha {b}Dewitt{/b} À beira das lágrimas."
        smi "Seu talento bobo mostra em frangalhos!"
        show principal spying 3
        smi "Mmm..."
        show principal spying 2
        smi "Na verdade, está me deixando meio excitada."
        smi "Por que você não vem aqui e me ajuda."
        show principal spying 1
        show annie spying 3
        ann "Claro senhora."
        show annie spying 4
        show principal spying 4
        with dissolve
        pause
        show annie spying 5 with dissolve
        pause
        show principal spying 3
        smi "Ahh, é isso aí."
        smi "Boa garota..."
        smi "Hehehehe, Mal posso esperar para ver o rosto dela quando, Eu dizer que a diretoria conseguiu seu financiamento!"
        scene black with fade

        scene outside_smith_office
        show kevin 24 at Position (xpos=800)
        show player 107 at Position (xpos=400)
        with dissolve
        kev "Mano a {b}Diretora Smith{/b} , Estar por trás disso!"
        show kevin 23
        player_name "..."
        show kevin 24
        kev "Que mega cadela!"
        kev "Temos que fazer algo!"
        show kevin 23
        player_name "..."
        show kevin 24
        kev "{b}[firstname]{/b}?"
        kev "{b}[firstname]{/b}?!"
        show kevin 23
        pause 1
        show kevin 25 at Position (xoffset=-82) with hpunch
        kev "Mano!"
        show kevin 23
        show player 12 with dissolve
        player_name "Ei! Relaxa, cara!"
        show player 5
        show kevin 24
        kev "Estou tentando falar com você!"
        show kevin 23
        show player 12
        player_name "Desculpe, mas você viu o que elas estão fazendo lá agora?!"
        show player 5
        show kevin 24
        kev "Uh, sim e é super nojento!"
        kev "{b}Diretora Smith{/b} é um homem do diabo, aposto que ela cheira a enxofre!"
        show kevin 23
        show player 113
        player_name "{b}Annie{/b} não parece se importar..."
        show player 114
        show kevin 24
        kev "Vamos está ficando tarde, E você deve se encontrar com a {b}Eve{/b} no parque, lembra?!"
        show kevin 23
        show player 113
        player_name "Espera, só mais cinco minutos..."
        show player 114
        show kevin 24
        kev "Vamos, antes de sermos pegos, pervertendo!"
        hide kevin
        hide player
        with dissolve
    else:

        scene smith_office_spying
        show annie spying 5
        show principal spying 3
        with dissolve
        smi "Você está ficando muito boa nisso, meu bichinho."
        smi "Mmm, a simm!"
        smi "Ahh!"
        scene black with fade
    return

label principals_office_dewitt_smith_office_trap:
    scene expression game.timer.image("office{}")
    show erik 51 at right
    show player 12 at left
    with dissolve
    player_name "Você olha a porta enquanto eu aplico o adesivo, tudo bem?"
    show player 5
    show erik 53
    eri "Sim, ok."
    eri "Apenas se apresse, cara. Eu quero sair daqui..."
    show erik 52
    show player 12
    player_name "I will."
    hide player
    hide erik
    with dissolve

    scene smith_office_cs01
    with fade
    show text "Eu me certifiquei de que as cadeiras estivessem coladas no chão antes de passar para as almofadas.\nNão havia como eu deixar a {b}Diretora Smith{/b} e {b}Annie{/b} estragar o {b}Show de talentos{/b}.\nNão depois de todo o trabalho duro que colocamos nele!\nNão parei até que toda última gota do adesivo tivesse sido usada." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene smith_office_night_b
    show erik 52 at right
    show player 14 at left
    with dissolve
    player_name "Tudo bem, isso deve ser o suficiente."
    show player 17
    player_name "Também desconectei o telefone dela da tomada, para que não houvesse maneira de pedir ajuda.!"
    show player 13
    show erik 54
    eri "Pensamento agradável!"
    show erik 53
    eri "Agora vamos sair daqui, {b}[firstname]{/b}!"
    show erik 52
    show player 14
    player_name "Sim, estou bem atrás de você!"
    hide player
    hide erik
    with dissolve

    scene expression game.timer.image("outside_school{}")
    show player 13 at left
    show erik 53 at right
    with dissolve
    eri "Ufa."
    eri "Nunca mais vamos fazer isso de novo, ok?"
    show erik 52
    show player 14
    player_name "Hehe, Sim."
    player_name "Pelo menos conseguimos o que viemos fazer aqui."
    show player 13
    show erik 54
    eri "Missão bem sucedida!"
    show erik 1
    show player 14
    player_name "Obrigado pela ajuda, {b}Erik{/b}."
    show player 13
    show erik 4
    eri "Sem problemas {b}[firstname]{/b}."
    show erik 1
    show player 14
    player_name "Vejo você mais tarde!"
    show player 13
    show erik 7 with dissolve
    eri "Até mais!"
    hide player
    hide erik
    with dissolve
    return

label principals_office_dewitt_trap_check_up:
    scene office_clear
    show annie 19
    with dissolve
    ann "... É um ótimo plano, senhora!"
    ann "Vai acabar com esse estúpido show de talentos de uma vez por todas."
    show annie 20
    smi "Sim, desde que você não estrague tudo de novo..."
    show annie 19
    ann "Mas eu não..."
    ann "... Sim, senhora."
    show annie 20
    smi "Basta ir fazer os preparativos!"
    show annie 19
    ann "Imediatamente, senhora!"
    show annie 20b with dissolve
    ann "..."
    ann "estou presa!"
    show annie 20c with dissolve
    smi "O que?"
    show annie 20b with dissolve
    ann "Não consigo sair da minha cadeira!"
    show annie 20c with dissolve
    smi "Pare de brincar, {b}Annie{/b}. Não temos tempo a perder!"
    show annie 20b with dissolve
    ann "Estou seriamente presa à cadeira!"
    show annie 20c with dissolve
    smi "Oh pelo amor de Deus!"
    show annie 21
    smi "( !!! )" with hpunch
    smi "QUE DIABOS?!"
    smi "Eu também estou presa!!!"
    smi "Como isso é possível?!"
    ann "..."
    smi "{b}Annie{/b} traga sua bunda aqui e me ajude!"
    ann "Eu não posso, eu também estou presa!"
    scene black with fade

    scene outside_smith_office
    show player 107 at Position (xpos=400)
    with dissolve
    pause
    show player 17f at Position (xoffset=100) with dissolve
    player_name "( Funcionou! )"
    show player 14f at Position (xoffset=100)
    player_name "( Não há como elas interferirem com o {b}Show de talentos{/b} agora! )"
    player_name "( Elas ficarão presas lá discutindo até que alguém as encontre. )"
    player_name "( É melhor eu ir para o {b}auditório{/b} rapido, Ou vão sentir minha falta nas apresentações. )"
    hide player with dissolve
    return

label principals_office_dewitt_office_night_visit_delay:
    scene expression game.timer.image("office{}")
    show annie 22f at left
    show principal 36 at right
    with dissolve
    ann "Você pode tirar essa almofada?"
    show annie 23f
    show principal 37
    smi "Agora não, idiota!"
    smi "O que eu quero é um relatório completo sobre quem fez isso!"
    smi "Quem arruinou minha cadeira ... e ... e meu traje!"
    smi "Meu lindo terno!"
    show principal 40 with dissolve
    smi "Basta olhar para o que eles fizeram!"
    smi "ENCONTRÁ-LOS!"
    scene black with fade

    scene outside_smith_office
    show player 107 at Position (xpos=400)
    with dissolve
    pause
    show player 17f at Position (xoffset=100) with dissolve
    player_name "( É melhor eu sair daqui antes que elas me vejam! )"
    hide player with dissolve
    return

label desk03_locked_dialogue:
    scene expression game.timer.image("office{}")
    if player.location.is_here(M_smith):
        show player 30 at left
        player_name "Hmmm... Eu me pergunto o que tem lá?"
        show player 22 at left with hpunch
        show principal 4 at right with dissolve
        smi "O que você está fazendo?"
        show principal 1 at right
        show player 29 at left
        player_name "Oh, Me desculpe ... eu só estava olhando!"
        show player 3 at left
        show principal 5 at right
        smi "Se eu {b}SEMPRE{/b} te pegar passando pelas minhas coisas..."
        show principal 2 at right
        smi "...pode ter certeza, você passará o resto do ano em {b}DETENÇÃO{/b}!!!"
    else:
        $ pass
    $ game.main()

label principle_drawer:
    scene principle_drawer
    show expression "objects/object_papers_01.png" at Position(xpos = 378, ypos = 526)
    player_name "..."
    player_name "O que há com todas aquelas ... coisas de couro ... aqui?"
    player_name "esquisito..."
    call screen principle_drawer

label principle_drawer_diane_delivery_3_fetch_invoice:
    scene expression game.timer.image("office{}")
    show player 167f at right
    show titty 1 at left
    show principal 28f at Position (xpos = 470)
    with dissolve
    smi "Ah, maravilhoso."
    smi "Essas são as novas {b}caixas de leite{/b}?"
    show player 168f
    show principal 26f at Position (xpos = 415)
    player_name "Umm... sim."
    show principal 27f
    show player 163f
    smi "Amostra do último lote..."
    smi "Foi muito ... delicioso. Você tem sorte, eu estou de bom humor."
    smi "Por favor, diga ao fornecedor de leite que estou dobrando nosso próximo pedido."
    smi "Continua fazendo. Os alunos adora esse leite!"
    show principal 26f
    show player 164f
    player_name "Ok! Onde posso colocar essas caixas?"
    show principal 27f
    show player 163f
    smi "Você pode dar a {b}Annie{/b}, ela vai cuidar delas."
    show principal 4f at Position (xpos = 470)
    show player 167f
    smi "Agora, saia do meu escritório, tenho alguns assuntos pendentes para tratar."
    show principal 26f at Position (xpos = 415)
    show player 168f
    player_name "Sim, {b}Diretora Smith{/b}!"
    hide principal
    hide titty
    hide player
    with dissolve
    $ M_diane.trigger(T_diane_delivery_3_got_invoice)
    $ game.main()

label principals_office_okita_get_keycode_morning:
    scene expression game.timer.image("office{}")
    show player 22 at left
    show principal 26 at right
    player_name "( Oh porcaria! Ela está aqui! )"
    smi "..."
    show principal 27
    smi "... Eu posso te ajudar com alguma coisa?"
    show player 10
    show principal 26
    player_name "Oh! eu só estava-"
    show player 29
    player_name "... Err, Eu estava ... apenas me perguntando..."
    show principal 2
    show player 3
    smi "Desembucha, {b}[firstname]{/b}?!"
    show principal 26
    pause
    show player 10
    player_name "Uhh, como vai você, {b}Diretora Smith{/b}?"
    show player 11
    smi "..."
    show principal 27
    smi "Ocupada."
    show principal 2
    smi "Agora saia!"
    show player 10
    show principal 26
    player_name "Y-yes, Ma'am!"


    return

label principals_office_okita_get_keycode_afternoon:
    scene expression game.timer.image("office{}")
    show player 1
    with dissolve
    player_name "( Ela não está aqui! Esta é a minha chance de encontrar esse código de chave! )"
    player_name "( {b}Eu deveria olhar em volta.{/b} )"
    return

label masterkey_taken:
    show expression "backgrounds/location_school_office_desk.jpg"
    show expression "boxes/popup_key3.png" at truecenter with dissolve
    $ player.get_item("master_key")
    pause
    hide expression "boxes/popup_key3.png" with dissolve
    $ game.main()

label keycode_note_taken:
    scene expression game.timer.image("office{}")
    show player 544
    with dissolve
    pause
    show player 543
    player_name "Aha! Tem que ser isso! {b}6219{/b}."
    show expression "backgrounds/location_school_office_desk.jpg"
    show expression "boxes/popup_item_note2.png" at truecenter with dissolve
    $ player.get_item("keycode_note")
    pause
    hide expression "boxes/popup_item_note2.png" with dissolve
    pause 1
    player_name "Agora eu só tenho que ir desbloquear o {b}Escritório da senhorita Okita{/b} para pegar todas as coisas que ela pediu."
    $ M_okita.trigger(T_okita_keycode_acquired)
    $ game.main()
    return

label tissue_taken:
    $ player.go_to(L_school_smithoffice)
    scene location_school_office_day_blur
    show player 528
    with dissolve
    pause
    show player 529
    player_name "Ugh, Oh cara..."

    player_name "Complicado!"
    show player 528
    pause
    show player 529
    player_name "Eu acho que isso vai funcionar..."
    player_name "É melhor eu sair daqui antes que a {b}Annie{/b} volta."
    show expression "boxes/popup_item_tissue1.png" at truecenter with dissolve
    $ player.get_item("tissue")
    pause
    hide expression "boxes/popup_item_tissue1.png" with dissolve
    pause 1

    $ game.main()

label desk_open:
    python:
        for image in renpy.get_showing_tags():
            renpy.hide(image)
    call screen desk_drawer

label principals_office_okita_get_ingredients_morning:
    scene expression game.timer.image("office{}")
    show player 22 at left
    with dissolve
    player_name "( Oh porcaria! Ela está aqui! )"
    show principal 3b at Position(xpos=0.85, ypos=1.0) with dissolve
    smi "..."
    show principal 27 at right with dissolve
    smi "... Eu posso te ajudar com alguma coisa?"
    show player 29 with dissolve
    show principal 26
    player_name "Oh! eu só estava-"
    player_name "... Err, Eu estava ... apenas me perguntando..."
    show player 3
    show principal 27 with dissolve
    smi "Desembucha, {b}[firstname]{/b}!"
    show player 29
    show principal 26
    player_name "Uhh, como vai você, {b}Diretora Smith{/b}?"
    show player 3
    smi "..."
    show principal 27
    smi "Ocupada."
    show player 22
    show principal 2
    with dissolve
    smi "Saia agora!" with hpunch
    show principal 1
    show player 10
    player_name "Sim, senhora!"

    return

label principal_trash:
    if M_okita.is_state(S_okita_get_ingredients) and not player.has_picked_up_item("tissue"):
        call screen principle_garbage
    else:
        scene location_school_office_day_blur
        show player 10
        player_name "Eu não quero olhar o lixo da diretora Smith."
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
