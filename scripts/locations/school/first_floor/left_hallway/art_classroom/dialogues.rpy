label art_classroom_ross_start:
    scene location_school_art_closeup
    show player 2f at right
    show ross 1 at left
    player_name "Oi, {b}Miss Ross{/b}."
    show player 1f
    show ross 2
    ross "Bem olá, {b}[firstname]{/b}!"
    show ross 25 with dissolve
    ross "Eu ouvi sobre o seu pai..."
    ross "Coitado, eu tenho orado por você."
    show ross 24
    show player 2f
    player_name "Uhh, Obrigado!"
    show player 1f
    show ross 25
    ross "Oh, não tem problema, querido."
    ross "Você me deixa saber se há alguma coisa que eu possa fazer por você."
    show player 2f
    show ross 24
    player_name "Bem, na verdade, pode haver algo que você possa fazer."
    player_name "Eu preciso de um jeito de {b}melhorar meu grau de arte{/b}."
    show player 1f
    show ross 25
    ross "Oh sim, suas notas caiu um pouco durante a sua ausência."
    ross "É muito ruim. Você estava no topo da turma antes de sair..."
    show player 10f
    show ross 24
    player_name "Eu tava?!"
    show player 11f
    show ross 11
    ross "Ah, não seja modesto {b}[firstname]{/b}! Você tem talento para a arte!"
    show player 2f
    show ross 10
    player_name "Hehe, Sim, eu acho..."
    show player 1f
    show ross 11
    ross "Tenho certeza de que podemos encontrar alguma maneira de melhorar sua nota."
    show ross 2 with dissolve
    ross "Hmm, por que não falamos sobre isso depois da aula hoje?"
    show player 2f
    show ross 1
    player_name "Isso parece ótimo! Muito obrigado, {b}Miss Ross{/b}!"
    show player 1f
    show ross 2
    ross "Nós iremos {b}pegue uma laje de barro{/b} e sente-se para começarmos a meditação pré-aula."
    show player 10f
    show ross 1
    player_name "Meditação?"
    show player 11f
    show ross 2
    ross "Claro! Temos que relaxar nossas mentes e alinhar nossos chakras se quisermos que nossa criatividade flua corretamente!"
    show player 10f
    show ross 1
    player_name "Ugh. Sim, senhora."
    return

label art_classroom_mia_find_easel:
    scene art_classroom_b
    show player 4 with dissolve
    player_name "Hmm..."
    show player 12 with dissolve
    player_name "Vamos ver se consigo encontrar um {b}cavalete{/b} Eu poderia usar para desenhar algumas idéias de tatuagem..."
    hide player with dissolve
    return

label easel_dialogue_mia_show_tattoo:
    show player 14 with dissolve
    player_name "( Eu deveria mostrar o desenho que fiz para {b}Mia{/b} primeiro, antes de fazer outro. )"
    hide player with dissolve
    return

label easel_dialogue_mia_draw_tattoo_intro:
    scene school_art_tattoos
    player_name "Hmm..."
    player_name "( O que devo desenhar para {b}Mia{/b}... )"
    return

label easel_dialogue_mia_draw_tattoo_drawn:
    hide player with dissolve
    scene school_art_cs01
    with fade
    show text "Eu desenhei tantas fotos antes...\n...Mas, fazendo algo assim para {b}Mia{/b} me deixou super nervoso!\nEu espero que seja o que ela quer..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide school_art_cs01
    with dissolve
    scene art_classroom_b
    show player 381 with dissolve
    player_name "Não é ruim!"
    show player 386
    player_name "( Eu deveria ir e mostrar {b}Mia{/b} o que eu fiz. )"
    player_name "( Espero que ela goste... )"
    hide player with dissolve
    return

label art_classroom_ross_molding_clay_cutscene:
    scene location_school_art_cutscene03
    with fade
    show text "Foi bom estar de novo na aula de arte." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Eu sempre tive um jeito para isso." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene location_school_art_cutscene04
    with fade
    show text "Infelizmente, o mesmo não pode ser dito para os meus amigos..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_school_art_closeup
    show player 547f at right
    show ross 27 zorder 1 at left
    with dissolve
    ross "Deus, que linda girafa, {b}[firstname]{/b}!"
    show player 548f
    show ross 26
    player_name "Você acha?"
    show player 547f
    show ross 27
    ross "Simplesmente adorável!"
    show ross 13 with dissolve
    ross "É certamente muito - superdotado. Não é?"
    show player 10f with dissolve
    show ross 12
    player_name "Hã?"
    show player 11f
    show ross 13
    ross "Eu só quero dizer que é tão longo e grosso..."
    show player 2f
    show ross 12
    player_name "... Oh, você quer dizer o pescoço!"
    show player 1f
    show ross 11
    ross "Hehe, sim isso também. Está muito bem feito!"
    show ross 10
    player_name "..."
    show ross 11
    ross "Então, o que vamos fazer com essas notas baixas?"
    show ross 13
    ross "Eu posso pensar mais um bom uso para esssas mãos talentosas..."
    show player 11f
    show ross 12
    player_name "..."
    show ross 13
    ross "Talvez devêssemos começar um pouco depois da escola-"
    show ross 12
    smi "{b}Ross{/b}!!!" with hpunch
    show ross 24
    show player 22f
    smi "Onde você está, seu Quack!?"
    show player 11 zorder 0 at Position(xpos=0.45, ypos=1.0)
    show principal 2 at Position(xpos=0.75, ypos=1.0)
    with dissolve
    smi "É melhor você não estar fazendo meditação nua!"
    show principal 3b at Position(xpos=0.8, ypos=1.0) with dissolve
    pause
    show principal 27 at Position(xpos=0.75, ypos=1.0) with dissolve

    smi "Oh, aí está você!"
    show ross 23
    show principal 26
    ross "Com licença, estou com um aluno agora..."
    show ross 22
    show principal 27
    smi "Pfft. Ele vai ter que esperar."
    smi "Eu preciso falar com você sobre todas essas coisas que você pediu."
    show ross 25
    show principal 26
    ross "Você quer dizer o material de arte?"
    show ross 24
    show principal 27
    smi "Eu não sei! O que quer que seja esse material, isso não está acontecendo!"
    show ross 25b
    show principal 26
    ross "Mas..."
    show ross 24
    show principal 27
    smi "Olha, não é só no orçamento {b}Barbara{/b}."
    smi "Você vai ter que se virar sem essas coisas."
    show ross 25
    show principal 26
    ross "{b}Diretora Smith{/b}, precisamos desses suprimentos! Nosso equipamento está em frangalhos!"
    show ross 24
    show principal 27
    smi "Eu não posso te dar o que eu não tenho, agora posso?"
    show principal 26
    ross "..."
    show principal 28 at Position(xpos=0.7, ypos=1.0) with dissolve
    smi "Apenas seja grato por você ainda ter algum {b}Orçamento{/b} em absoluto."
    smi "Você tem alguma idéia de como é difícil vender essa porcaria hippie que você ensina na diretoria da escola?"
    show ross 25b
    show principal 26 at Position(xpos=0.75, ypos=1.0) with dissolve
    ross "... Mas a arte é importante para o crescimento de um indivíduo!"
    show ross 24
    show principal 27
    smi "Sim, claro que é..."
    smi "A resposta é não, {b}Barbara{/b}!"
    smi "Você só vai ter que desistir."
    hide principal
    with dissolve
    pause
    hide player
    show player 11f zorder 1 at right
    show ross 23
    with dissolve

    ross "Arrghh!"
    ross "Todo ano fica pior e pior!"
    show ross 22
    pause
    show mia 12b zorder 0 at Position(xpos=0.65, ypos=1.0) with dissolve

    mia "Você está certa, {b}Miss Ross{/b}?"
    show ross 11
    show mia 8b
    ross "Oh, Olá, {b}Mia{/b} querida."
    show ross 10
    show mia 12b
    mia "Eu ouvi {b}Diretora Smith{/b} gritando com você..."
    show mia 8b
    show player 10f
    player_name "Sim, definitivamente não soava bem."
    show player 11f
    show ross 25
    ross "Há tão pouco orçamento para a arte."
    show ross 25b
    ross "Fica cada vez menor a cada ano."
    show ross 25
    ross "Tenho medo de não ter um emprego em breve..."
    show ross 24
    show mia 12b
    mia "A sério?"
    mia "Ela não podem simplesmente cortar a aula de arte, podem?"
    show ross 25
    show mia 8b
    ross "Eu não iria passar a {b}Diretora Smith{/b}. Ela não tem respeito pelas coisas que eu ensino."
    show ross 25b
    ross "Se eu pudesse encontrar uma maneira de aumentar o financiamento um pouco..."
    show ross 24
    show player 10f
    player_name "Hmm, quanto dinheiro você precisaria?"
    show ross 25
    show player 11f
    ross "Não tenho certeza."
    show ross 24
    pause
    show mia 12b
    mia "Mil dólares ajudariam?"
    show mia 8b
    show ross 25
    ross "Hã? Sim, isso seria muito para pedir novos equipamentos, reabastecer as prateleiras de arte, e talvez até contratar alguns modelos reais para as crianças pintarem."
    ross "... Mas onde conseguiríamos esse tipo de dinheiro?"
    show ross 24
    show mia 62 at Position(xpos=0.585, ypos=1.0) with dissolve

    mia "Você poderia entrar no {b}concurso de arte do prefeito{/b}!"
    show mia 63
    show ross 11
    ross "{b}O prefeito{/b} está hospedando um concurso de arte?"
    show mia 62
    show ross 10
    mia "Sim, dê uma olhada."
    show flyer 1 zorder 3 with dissolve
    show mia 63
    pause
    hide flyer with dissolve

    show player 10f
    player_name "O primeiro lugar é mil dólares, né?"
    show player 2f
    player_name "{b}Miss Ross{/b}, você deveria entrar!"
    show player 1f
    show ross 27 with dissolve
    ross "Oh céus, não! Eu não teria chance de ganhar algo assim..."
    show ross 26
    show mia 7 at Position(xpos=0.65, ypos=1.0) with dissolve
    ross "..."
    show ross 27
    ross "... Mas o {b}[firstname]{/b} poderia."
    show ross 26
    show player 10f
    player_name "o que?!"
    player_name "De jeito nenhum! Eu não sou talentoso o suficiente para algo assim."
    show ross 11 with dissolve
    show player 11f
    ross "Absurdo! Você é o aluno mais talentoso que eu tive em muito tempo!"
    ross "Comigo te guiando, é praticamente uma coisa certa!"
    show ross 10
    show mia 9
    mia "Hehe, isso é tão emocionante!"
    show mia 10b
    mia "Você consegue, {b}[firstname]{/b}!"
    show mia 7
    show ross 11
    ross "Veja, {b}Mia{/b} aqui acredita em você! Vamos dar uma chance!"
    show player 10f
    show ross 10
    player_name "Não sei..."
    show player 11f
    show ross 27 with dissolve
    ross "E se eu prometesse aumentar suas notas?"
    show player 10f
    show ross 26
    player_name "Você aumentaria minhas notas?"
    show player 11f
    show ross 27
    ross "Tudo o que você tem a fazer é ficar até tarde para praticar suas técnicas comigo por algumas semanas e entrar no concurso."
    ross "Você faz isso e eu vou te dar um A+!"
    show player 10f
    show ross 26
    player_name "Um A+?!"
    player_name "Apenas por entrar?"
    show player 11f
    show ross 27
    ross "Está certo. Nós temos um acordo?!"
    show ross 26
    pause
    show player 2f
    player_name "Sim, ok. Eu vou fazer isso!"
    show player 1f
    show mia 9
    mia "Yay!"
    show mia 7

    hide player
    show ross 21 at Position(xpos=0.15, ypos=1.0) with dissolve
    ross "Oh, Eu sabia que você não me decepcionaria {b}[firstname]{/b}!"
    ross "Volte aqui {b}amanhã depois da aula{/b} e nós vamos começar!"
    show ross 11 at left
    show player 11f at right
    with dissolve
    ross "Tudo bem, {b}[firstname]{/b}?"
    show ross 10
    show player 10f
    player_name "Ok, {b}Miss Ross{/b}. Eu te vejo amanhã então."

    $ game.timer.tick()
    $ M_ross.trigger(T_ross_molded_clay)
    $ game.main()

label leave_art_classroom:
    if not M_ross.is_state(S_ross_grab_clay):
        jump left_hall_dialogue
    else:

        scene location_school_art_closeup
        show player 2 with dissolve
        player_name "{b}Miss Ross{/b} quer que eu pegue um pedaço de barro e me sente."
        $ game.main()

label player_ross_magazines_3_left:
    show player 14 with dissolve
    player_name "Eu encontrei uma pilha de revistas!"
    player_name "Se eu puder encontrar mais duas pilhas deste tamanho, eu deveria ter o suficiente para fazer essa colagem de arte."
    hide player with dissolve
    $ player.get_item("magazines1")
    $ M_ross.trigger(T_ross_found_magazines)
    return

label player_ross_magazines_2_left:
    show player 14 with dissolve
    player_name "Agora eu só preciso encontrar mais uma pilha de revistas para {b}Miss Ross{/b}."
    hide player with dissolve
    $ player.remove_item("magazines1")
    $ player.get_item("magazines2")
    $ M_ross.trigger(T_ross_found_magazines)
    return

label player_ross_magazines_1_left:
    show player 14 with dissolve
    player_name "É isso aí! Eu deveria ter muitas revistas para começar a trabalhar na colagem de arte para {b}Miss Ross{/b}!"
    hide player with dissolve
    $ player.remove_item("magazines2")
    $ player.get_item("magazines")
    $ M_ross.trigger(T_ross_found_magazines)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
