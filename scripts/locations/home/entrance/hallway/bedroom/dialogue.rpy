label bedroom_jenny_pregnant_and_peeing:
    show player f_worried_talk with dissolve
    player_name "Uau, eu tenho que fazer xixi!"
    hide player with dissolve
    player_name "Oh cara! Oh cara!"
    scene black with fade
    pause .5
    scene expression L_home_shower.background_blur with None
    show jenny b_towel a_towel_pregnant_touch f_gross at flip
    show jenny at Position (xpos=500)
    with dissolve
    pause
    show jenny f_gross_talk
    jen "{b}*Suspiro*{/b} Porra grávida golpes..."
    show jenny f_gross
    show player f_worried with dissolve
    pause
    show player f_surprised_low a_dressed_surprised_up_both with dissolve
    player_name "!!!"
    hide jenny
    show jenny b_towel a_towel_pregnant_touch f_gross
    with dissolve
    show player f_worried_talk a_dressed_rub with dissolve
    player_name "Oi {b}[jen_name]{/b}..."
    player_name "Como você está se sentindo?"
    show player f_surprised_teeth
    show jenny f_angry_talk
    jen "Grávida!"
    jen "O que você quer?"
    show jenny f_angry
    show player f_worried_talk
    player_name "Umm, eu só"
    show player f_worried
    show jenny f_angry_talk
    jen "... E é melhor você não dizer sexo porque eu estou lhe dizendo agora, eu vou sentar na sua pequena cabecinha e esmagá-la como um melão!"
    show jenny f_angry
    show player f_worried_talk
    player_name "Não, eu realmente preciso fazer"
    show player f_worried
    show jenny f_angry_talk
    jen "Apenas olhe o que você fez comigo!"
    jen "Eu juro, nunca mais vou transar depois dessa merda!"
    show jenny f_angry
    show player f_worried_talk a_dressed_pocket with dissolve
    player_name "{b}[jen_name]{/b}, por favor eu realmente preciso"
    show player f_surprised_teeth_down
    show jenny f_gross_talk
    jen "Não, não se incomode em implorar ... Não vai funcionar!"
    jen "Como eu deveria me sentir sexy, parecendo um balão de aniversário inflado?!"
    show jenny f_gross
    show player f_shock
    player_name "{b}[jen_name]{/b}, pare de falar!!!"
    show player f_surprised_teeth
    show jenny f_surprised
    pause
    show jenny f_gross_talk
    jen "Qual é o seu problema?!"
    show jenny f_gross
    show player f_shock a_dressed_surprised_up_both with dissolve
    player_name "Preciso urinar droga!!!"
    show player f_surprised_teeth_down a_dressed_surprised with dissolve
    show jenny f_surprised
    jen "Oh..."
    show jenny f_angry_talk
    show player f_surprised_teeth
    jen "Bem, por que você não me avisou antes?!"
    show jenny f_eyeroll
    jen "Sheesh."
    show jenny f_gross_talk
    jen "Mova isso!"
    hide jenny with dissolve
    pause
    show player f_worried
    player_name "( Cara, eu achava o humor dela ruim antes da gravidez, Agora ela parece uma bomba relogio... )"
    show player f_grin a_dressed_thinking with dissolve
    player_name "( Espero que a criança não saia com chifres! )"
    hide player with dissolve
    return

label bedroom_jenny_weird_relationship:
    show player f_worried
    player_name "( Hmm, Eu não entendo {b}[jen_name]{/b}... )"
    player_name "( Por que ela é tão estranha sobre o nosso relacionamento? )"
    show player f_thinking a_dressed_thinking with dissolve
    pause
    show player f_worried a_dressed_pocket with dissolve
    player_name "( {b}Eu deveria falar com ela sobre isso...{/b} )"
    player_name "( {b}Ela geralmente está lá embaixo tomando café da manhã{/b} de manhã. )"
    hide player with dissolve
    return

label bedroom_jenny_bedroom_intrusion_1:
    scene expression "backgrounds/location_home_bedroom_cutscene13.jpg" with dissolve
    pause
    scene expression "backgrounds/location_home_bedroom_cutscene13b.jpg" with dissolve
    pause
    jen "Psst, {b}[firstname]{/b}..."
    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    player_name "!!!"
    player_name "O quê"
    player_name "Droga, {b}[jen_name]{/b}..."
    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jen "Hehehehe!"
    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    player_name "{b}*Suspiro*{/b} Você realmente precisa parar de fazer isso."
    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jen "A, pobrezinho..."
    jen "Se apresse, {b}o café da manhã está pronto.{/b}"
    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    player_name "Verdade?"
    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jen "Então, acredite em mim, você vai precisar da sua força hoje."
    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    player_name "O que isso significa?"
    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jen "Isso significa, levante-se, perdedor!"
    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    player_name "..."
    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jen "Vamos lá, {b}mova essa bunda vamos para o andar de baixo{/b}!"
    scene expression "backgrounds/location_home_bedroom_cutscene16.jpg" with dissolve
    player_name "Ugh!"
    return

label bedroom_jenny_bedroom_intrusion_2:
    show player f_worried_talk
    player_name "eu acho, {b}Eu deveria descer e ver o que ela está falando{/b}..."
    hide player with dissolve
    return

label bedroom_jenny_give_cunni:
    if store._in_replay is not None:
        $ player.location = L_home_bedroom
        scene expression "backgrounds/location_home_bedroom_telescope_window.jpg" with None
        $ game.timer.tick(0)
        show jenny b_telescope_rub a_telescope_rub f_empty
        show player b_telescope_laying_back a_telescope_side f_telescope_lay_worried at Position (align=(0,0))
        pause
    show player f_telescope_lay_worried_talk
    player_name "Então, você vai começar a se masturbar, aqui mesmo no meu quarto?"
    show player f_telescope_lay_worried
    show jenny f_telescope_normal_talk b_telescope_rub_look with dissolve
    jen "Hehe, Por que não?"
    show jenny b_telescope_rub f_empty with dissolve
    jen "Não é nada que você não tenha visto antes..."
    show player f_telescope_lay_worried_talk
    player_name "Sim mas"
    show player f_telescope_lay_worried
    pause
    show jenny f_telescope_normal_talk b_telescope a_telescope_down with dissolve
    jen "Na verdade, você está certo."
    jen "Por que se masturbar quando eu poderia facilmente fazer você lanchar na minha caixa?"
    show player f_telescope_lay_worried_talk
    player_name "Hã?!"
    show player f_telescope_lay_worried
    show jenny b_telescope_undress a_empty f_empty with dissolve
    pause
    show player f_telescope_lay_surprised

    show jenny b_telescope_standing_panties f_telescope_standing_grin_talk with dissolve
    if mrsj.over(mrsj_private_yoga):
        jen "Ela está fazendo um show para você e você vai retribuir o favor."
    else:
        jen "Eu quero o mesmo que ela estar recebendo, E você vai me dar."
    show jenny f_telescope_standing_grin
    if M_jenny.get("dominance") <= 0:
        show player f_telescope_lay_worried_talk
        player_name "Eu ?"
        show player f_telescope_lay_worried
        show jenny f_telescope_standing_grin_talk
        jen "Sim."
        jen "Vamos, perdedor!"
        jen "Eu vou gozar toda essa sua cara idiota!"
    else:
        show player f_telescope_lay_worried_talk
        player_name "Sério?"
        show player f_telescope_lay_worried
        show jenny f_telescope_standing_grin_talk
        jen "Sim."
        show jenny f_telescope_standing_grin
        show player f_telescope_lay_worried_talk
        player_name "Talvez se você me pedir com jeitinho."
        show player f_telescope_lay_worried
        show jenny f_telescope_standing_gross_down_talk at Position (align=(0,0))
        jen "Ugh, você ainda está nessa merda?!"
        show jenny f_telescope_standing_gross_down
        show player f_telescope_lay_skeptical_talk
        if randomizer() > 50:
            player_name "Se você quer voltar a se masturbar, se prepare..."
        else:
            player_name "Eu não sou seu pequeno escravo, {b}[jen_name]{/b}..."
        show player f_telescope_lay_skeptical
        show jenny f_telescope_standing_gross_down_talk
        jen "Grr, Você é uma dor na bunda!"
        jen "Està bem."
        show jenny f_telescope_standing_angry_pouting
        pause
        show jenny f_telescope_standing_eyeroll
        jen "{b}[firstname]{/b}, você poderia por favor lamber minha buceta?"
        show jenny f_telescope_standing_gross_down
        show player f_telescope_lay_laugh
        player_name "Haha, certo!"
        show player f_telescope_lay_skeptical
        pause
        show jenny f_telescope_standing_gross_down_talk
        jen "Apenas vamos!"
    jump jenny_cunni_repeat

label bedroom_jenny_perv_on_tammy_notice:
    scene expression player.location.background_blur with None
    show player f_grin with dissolve
    player_name "( Hmm, Eu me pergunto se {b}Sra. Johnson{/b} está fazendo sua rotina de yoga? )"
    player_name "( Eu geralmente posso vê-la através do meu {b}telescopio{/b}. )"
    hide player with dissolve
    return

label bedroom_jenny_morning_visit:
    scene expression "backgrounds/location_home_bedroom_cutscene13.jpg" with dissolve
    pause
    scene expression "backgrounds/location_home_bedroom_cutscene14.jpg" with hpunch
    jen "Ei, acorde perdedor!"
    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg" with dissolve
    player_name "Hmm?"
    player_name "A fala sério {b}[jen_name]{/b}, não isso de novo..."
    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jen "O que você está fazendo hoje?!"
    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    player_name "Eu não sei ...tentando Dormir?"
    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jen "Ok, certo."
    jen "{b}Venha para o meu quarto esta tarde{/b}."
    jen "Meus fãs querem outro show."
    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    player_name "Está bem ... Apenas vá embora!"
    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jen "Não seja, idiota!"
    scene expression "backgrounds/location_home_bedroom_cutscene16.jpg" with dissolve
    pause
    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg" with dissolve
    jen "{b}Meu quarto esta tarde{/b}!"
    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    player_name "Eu disse, tudo bem!"
    player_name "Sheesh."
    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jen "Hahahaah!"
    scene expression player.location.background_closeup with None
    show player 7 at left
    with dissolve
    pause
    show player 101 with dissolve
    player_name "( Eu acho que é melhor eu passar no quarto da {b}[jen_name] esta tarde{/b}. )"
    pause
    player_name "( Eu me pergunto o que ela planejou desta vez? )"
    hide player with dissolve
    return

label bedroom_jenny_pissed_at_handjob:
    show player 4 with dissolve
    player_name "( Hmm, Eu me pergunto se {b}[jen_name]{/b} ainda está chateada comigo? )"
    player_name "( Ela é provavelmente vai {b}lá embaixo tomar café da manhã{/b} agora mesmo. )"
    player_name "( Talvez eu deva ir lá {b}falar com ela{/b}? )"
    hide player with dissolve
    return

label bedroom_jenny_spy_on_mia_telescope:
    scene expression player.location.background_closeup with None
    show player 33 with dissolve
    player_name "Hmm, eu imagino o que {b}Mia{/b} está fazendo esta manhã?"
    player_name "Eu geralmente posso vê-la através {b}meu telescópio{/b}."
    hide player with dissolve
    return

label bedroom_jenny_buy_bad_monster:
    scene expression player.location.background_closeup with None
    show player 4 with dissolve
    player_name "( Hmm, se eu conseguir para {b}[jen_name]{/b} um novo brinquedo, aposto que ela vai fazer um novo vídeo na {b}CAMslut{/b} page. )"
    player_name "( Ela não mencionou um nome {b}Monstro Ruim{/b} no {b}diário{/b}? )"
    show player 403 with dissolve
    if player.has_item('badmonster'):
        player_name "( Eu deveria ver se tem na {b}Pink{/b}! )"
    else:
        player_name "( Eu deveria ir comprar {b}Monstro Ruim{/b} para ela! )"
    hide player with dissolve
    return

label bedroom_jenny_checked_for_new_video:
    scene expression player.location.background_closeup with None
    show player 4 with dissolve
    player_name "( Hmm, talvez haja um limite para quanto ela pode economizar? )"
    player_name "( Isso faria sentido, os videos salvos são principalmente promocionais depois de tudo... )"
    player_name "( Só mais uma maneira de atrair mais assinantes. )"
    pause
    show player 17 with dissolve
    player_name "( Eu aposto se eu {b}comprar um novo brinquedo{/b} ela faria um novo vídeo! )"
    pause
    show player 34
    player_name "(Ela não mencionou um nome {b}Monstro Ruim{/b} no {b}diario{/b}? )"
    if player.has_item('badmonster'):
        player_name "( Eu deveria ir para {b}Pink{/b}! )"
    else:
        player_name "( Eu deveria comprar {b}Monstro Ruim{/b} para ela! )"
    hide player with dissolve
    return

label bedroom_jenny_new_video_notice:
    scene expression player.location.background_closeup with None
    show player 403 with dissolve
    player_name "( Eu não chequei o perfil de {b}[jen_name]{/b}... )"
    player_name "( Eu me pergunto se ela salvou algum novo vídeo? )"
    hide player with dissolve
    return

label bedroom_jenny_hack_computer_notice:
    scene expression player.location.background_closeup with None
    show player 34 with dissolve
    player_name "( Hmm, este pode ser um bom momento para verificar {b}[jen_name]{/b}. )"
    player_name "( Se ela está dormindo, eu deveria ser capaz de {b}checar seu laptop e bisbilhotar{/b}. )"
    hide player with dissolve
    return

label bedroom_jenny_snoopin_laptop_notice:
    scene expression player.location.background_closeup with None
    show player 4 with dissolve
    player_name "( Hmm, tem que haver alguma maneira eu posso descobrir o que {b}[jen_name]{/b} está fazendo por esse dinheiro? )"
    pause
    show player 13 with dissolve
    player_name "( Ela poderia ter escrito alguma coisa naquele {b}diário dela{/b}... )"
    player_name "( Eu só tenho que {b}esperar até ela tomar banho{/b}então eu posso{b}esgueirar-se para o quarto dela{/b} e verificar. )"
    hide player with dissolve
    return

label bedroom_jenny_get_a_toy:
    scene expression "backgrounds/location_home_bedroom_cutscene13.jpg" with dissolve
    jen "{b}[firstname]{/b}!"
    player_name "Zzz..."
    scene expression "backgrounds/location_home_bedroom_cutscene14.jpg"
    jen "EI DOOFUS!" with hpunch
    player_name "!!!"
    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg" with dissolve
    player_name "O que?"
    player_name "Qual é o seu problema?!"
    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jen "Eu preciso de você para algo."
    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    player_name "Não pode esperar?!"
    player_name "Estou tentando dormir!"
    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jen "Não, não pode esperar."
    jen "Apresse-se, perdedor!"
    scene expression "backgrounds/location_home_bedroom_cutscene13.jpg" with dissolve
    player_name "( Ugh, Estou tão cansado... )"
    scene expression "backgrounds/location_home_bedroom_cutscene14.jpg" with fastdissolve
    jen "Não volte a dormir!"
    jen "Levante-se, coloque algumas calças e coloque sua bunda preguiçosa em marcha!"
    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg" with dissolve
    player_name "Sim, sim ... estou indo."
    player_name "Sheesh."
    scene expression "backgrounds/location_home_bedroom_cutscene16.jpg" with dissolve
    player_name "{b}*Uaaaaaa....*{/b}"
    player_name "É melhor que valha a pena..."
    return

label bedroom_jenny_pics_afterthought:
    scene expression player.location.background_closeup with None
    show player 17 with dissolve
    player_name "( Cara, aquelas fotos de {b}[jen_name]{/b} estavam tão excitantes! )"
    player_name "( Eu gostaria de poder dar outra olhada nelas... )"
    pause
    show player 4 with dissolve
    player_name "( Hmm, Você sabe o que? )"
    player_name "( {b}Eu acho que ela deixa a porta do quarto destrancada enquanto toma banho{/b}. )"
    show player 17 with dissolve
    player_name "( eu poderia {b}esgueirar-se e encontrar sua câmera{/b}, preciso ser rápido. )"
    show player 13
    pause
    player_name "( Eu só preciso {b}esperar até que ela esteja no chuveiro{/b}. )"
    hide player with dissolve
    return

label bedroom_jenny_breakfast_notice:
    scene expression player.location.background_closeup with None
    show player 14 with dissolve
    player_name "Uau, algo cheira delicioso!"
    player_name "{b}[deb_name]{/b} Deve estar cozinhando o café da manhã lá embaixo."
    player_name "{b}Eu deveria ir dar uma olhada{/b}!"
    hide player with dissolve
    return

label bedroom_diane_breeding_candidate:
    scene expression game.timer.image("bedroom{}")
    show player 14 with dissolve
    player_name "Ontem à noite foi uma loucura!"
    player_name "Eu me pergunto se {b}Diane{/b} já saiu?"
    player_name "{b}Eu deveria procurar por ela no andar de baixo, ela geralmente está na cozinha com [deb_name]{/b}."
    hide player with dissolve
    return


label bedroom_diane_barn_news:
    scene expression game.timer.image("bedroom{}")
    show player 34 with dissolve
    dia "Dance Comigo!!"
    deb "{b}Diane{/b}!"
    pause
    show player 35
    player_name "O que diabos está acontecendo lá embaixo?"
    show player 34
    deb "Hahaha!"
    show player 12
    player_name "Eu deveria ir dar uma olhada."
    hide player with dissolve
    return

label bedroom_diane_debbie_dinner:
    scene expression game.timer.image("bedroom{}")
    show player 5 with dissolve
    deb "{b}[firstname]{/b}?!"
    deb "Você ainda está dormindo?!"
    player_name "Hmm?"
    show player 10
    player_name "Soa como {b}[deb_name]{/b} precisa de mim..."
    show player 9 at Position (xoffset=40) with dissolve
    pause
    show player 10 with dissolve
    player_name "Eu deveria ir ver o que ela quer."
    hide player with dissolve
    return

label bedroom_diane_get_augmentation:
    scene expression game.timer.image("bedroom{}")
    show player 5f with dissolve
    "{b}*Knock Knock*{/b}"
    show player 10f
    player_name "Hã?"
    show player 5f
    deb "{b}[firstname]{/b}?"
    deb "Posso falar com você por um segundo?"
    show player 14f
    player_name "Sim, vamos lá, {b}[deb_name]{/b}."
    show player 13f at right with dissolve
    pause
    show debbie 1f at left with dissolve
    show player 14f
    player_name "Bom Dia."
    show player 13f
    show debbie 2f
    deb "Bom dia, querido."
    show debbie 1f
    show player 14f
    player_name "Estás bem?"
    show player 13f
    show debbie 2f
    deb "Bem, acabei de desligar o telefone estava comversando com {b}Diane{/b}."
    show debbie 1f
    show player 11f
    player_name "!!!"
    show player 10f
    player_name "{b}*Gole*{/b} O que ela tem a dizer?"
    show player 5f
    show debbie 3f
    deb "Ela simplesmente não conseguia parar de falar sobre o quão grande você está fazendo com seu jardim!"
    show debbie 1f
    show player 10f
    player_name "Serio?"
    show player 5f
    show debbie 2f
    deb "Sim e aparentemente você tem ajudado ela com um novo empreendimento também?"
    show debbie 1f
    show player 17f
    player_name "Ahh, sim. Um pouco."
    show player 13f
    show debbie 2f
    deb "Eu nem sabia que ela tinha começado um novo negócio..."
    show debbie 1f
    player_name "..."
    show player 10f
    player_name "Ela disse mais alguma coisa?"
    show player 5f
    show debbie 2f
    deb "Hmm."
    deb "Oh, Uhh..."
    deb "Ela queria que eu te dissesse, não se preocupar com o seu pequeno incidente..."
    show debbie 1f
    show player 11f
    player_name "!!!"
    show debbie 13f
    deb "Aconteceu alguma coisa?"
    show debbie 14bf
    show player 24f
    player_name "... Sim, meio que."
    player_name "..."
    show debbie 13f
    deb "Bem, não me deixe em suspense!"
    show debbie 14bf
    show player 25f
    player_name "Amm, Eu prefiro não falar sobre isso ... Se está tudo bem?"
    show player 24f
    show debbie 13f
    deb "Claro que está tudo bem, querido."
    deb "Nós não precisamos."
    show debbie 14bf
    show player 5f
    player_name "..."
    show debbie 2f
    deb "De qualquer forma, ela aparentemente conseguiu outro grande cliente para o seu negócio e ela realmente poderia usar sua ajuda."
    deb "Eu acho que ela vai te oferecer um aumento."
    show debbie 1f
    show player 12f
    player_name "Um aumento?"
    show player 5f
    show debbie 3f
    deb "Hehe, Sim!"
    hide player
    show debbie 4bf at right
    with dissolve
    deb "Você está crescendo tão rápido!"
    deb "Estou tão orgulhosa de você, querido!"
    show debbie 5f
    player_name "Obrigado, {b}[deb_name]{/b}."
    show debbie 2f at left
    show player 13f at right
    with dissolve
    deb "É melhor você chegar lá!"
    show debbie 1f
    show player 14f
    player_name "Sim, eu acho melhor."
    hide player
    hide debbie
    with dissolve
    return

label bedroom_mc_start_just_wokeup:
    scene expression game.timer.image("bedroom{}")
    show player 7 with dissolve
    player_name "{b}*Uaaaaaa....*{/b}"
    show player 8
    player_name "Merda... Eu odeio acordar cedo."
    show player 9
    player_name "( Nenhuma mensagem de texto de {b}Erik{/b}. Talvez ele ainda esteja dormindo. )"
    player_name "( Vou da uma passada na casa dele, A caminho da escola. )"
    hide player 9 with dissolve
    return

label bedroom_mc_weekday_just_wokeup:
    scene expression game.timer.image("bedroom{}")
    show player 7 with dissolve
    player_name "{b}*Uaaaaaa....*{/b}"
    show player 8
    window hide
    pause
    show player 9
    player_name "( Eu deveria me preparar para a escola... )"
    hide player with dissolve
    return

label bedroom_mc_weekend_just_wokeup:
    scene expression game.timer.image("bedroom{}")
    show player 7 with dissolve
    player_name "{b}*Uaaaaaa....*{/b}"
    show player 8
    window hide
    pause
    show player 9
    player_name "( O que devo fazer neste fim de semana... )"
    hide player with dissolve
    return

label bedroom_erik_bullying:
    scene black with fade
    deb "Querido?"
    pause
    deb "Acorde, querido."
    scene expression game.timer.image("bedroom{}") with fade
    show debbie 14f at left
    show player 101bf at right
    with dissolve
    player_name "Hã? {b}[deb_name]{/b}? Que horas são?"
    show player 100bf
    show debbie 13f
    deb "{b}Sra. Johnson{/b} está na porta pedindo para te ver."
    show debbie 14f
    show player 101bf
    player_name "{b}Sra. Johnson{/b}? que ela que de mim?"
    show player 100bf
    show debbie 13f
    deb "Ela não falou muito, mas quer falar com você antes de sair para o dia."
    show debbie 14f
    show player 101bf
    player_name "Está bem. Deixe-me vestir e eu vou sair em breve."
    show player 100bf
    show debbie 13f
    deb "Tudo bem..."
    show debbie 14f
    pause
    show debbie 13f
    deb "Há algo que eu precise saber, {b}[firstname]{/b}?"
    show debbie 14f
    player_name "..."
    show player 101bf
    player_name "Eu não tenho ideia de porque ela está aqui também {b}[deb_name]{/b}."
    show player 100bf
    deb "..."
    show debbie 13f
    deb "Ok, Querido."
    hide debbie
    hide player
    with dissolve
    return

label bedroom_mia_tattoo_help:
    scene expression game.timer.image("bedroom{}")
    show player 35 with dissolve
    player_name "( Eu tenho que fazer algo legal para sua ideia de tatuagem. )"
    show player 34
    player_name "Hmm..."
    show player 35
    player_name "( Talvez eu possa usar um dos {b}cavaletes na aula de arte{/b}! )"
    show player 33
    player_name "( Eu posso usá-lo para chegar a um bom design para ela. )"
    show player 8 with dissolve
    pause
    show player 7 with dissolve
    player_name "{b}*Uaaaaaa....*{/b}"
    show player 101 with dissolve
    player_name "eu deveria dormir."
    hide player with dissolve
    show unlock53 at truecenter with dissolve
    pause
    hide unlock53 with dissolve
    return

label bedroom_mia_strip_aftermath_grounded:
    scene expression game.timer.image("bedroom{}")
    show player 24 with dissolve
    player_name "( Eu não posso acreditar que não serei capaz de ver {b}Mia{/b} não mais. )"
    show player 25
    player_name "( Seus pais não confiam em mim. )"
    show player 35
    player_name "( Talvez eu possa fazer as pazes com eles de alguma forma... )"
    hide player with dissolve
    return

label bedroom_mia_concerning_visit:
    scene expression game.timer.image("bedroom{}")
    show player 4 with dissolve
    pause
    show player 30 at Position (xoffset=-6) with dissolve
    player_name "( me pergunto que {b}Mia{/b} está fazendo. )"
    show player 12 at Position (xoffset=-6)
    player_name "( Já faz alguns dias, e eu não ouvi nada dela... )"
    player_name "( ...Talvez eu deva visitá-la e ver como ela está... )"
    hide player with dissolve
    return

label bedroom_mia_urgent_message:
    scene expression game.timer.image("bedroom{}")
    show player 12 with dissolve
    player_name "Hã?"
    show player 9 at Position (xoffset=40) with dissolve
    pause
    show player 14 with dissolve
    player_name "( Parece que recebi uma mensagem de texto... )"
    hide player with dissolve
    return

label bedroom_mia_angelicas_impatience:
    scene expression game.timer.image("bedroom{}")
    show player 55f at Position (xoffset=-12) with dissolve
    player_name "*Uaaaaaa....*"
    show player 56f with dissolve
    player_name "( Eu deveria me preparar para )"
    show player 11f
    "*Knock knock*"
    show debbie 2f at left
    show player 13f
    with dissolve
    deb "Hã?"
    deb "Tem alguém no andar de baixo que está aqui?"
    show debbie 1f
    show player 30f
    player_name "{b}Erik{/b}?"
    show player 11f
    show debbie 2f
    deb "Não, querido. É uma dama!"
    deb "Ela diz que vocês dois falaram antes..."
    show debbie 1f
    show player 10f
    player_name "o que?"
    player_name "Mas quem"
    show player 5f
    show debbie 2f
    deb "Ela está esperando lá embaixo. Por que você não se veste e desce{/b}."
    hide debbie with dissolve
    show player 12f
    player_name "uma dama?!"
    show player 4f at Position (xoffset=-6) with dissolve
    player_name "Hã..."
    hide player with dissolve
    return

label bedroom_mia_angelicas_home_visit:
    scene expression game.timer.image("bedroom{}")
    show player 13f at right
    show debbie 2f at left
    deb "Querido?"
    show debbie 1f
    show player 17f
    player_name "Bom Dia, {b}[deb_name]{/b}."
    show player 13f
    show debbie 2f
    deb "Bom dia."
    deb "Aquela simpática senhora do outro dia está lá embaixo novamente."
    show debbie 1f
    show player 11f
    player_name "..."
    show player 12f
    player_name "Quem?"
    show player 5f
    show debbie 3f
    deb "Venha agora, dorminhoco. A freira está aqui novamente."
    show debbie 1f
    show player 22f
    player_name "!!!"
    deb "Apresse-se para que você possa encontrá-la no andar de baixo."
    hide debbie with dissolve
    show player 10f
    player_name "O que ela vai querer agora?"
    hide player with dissolve
    return

label bedroom_mia_angelicas_final_home_visit:
    scene expression game.timer.image("bedroom{}") with fade
    show player 55f at Position (xoffset=-12) with dissolve
    player_name "*Uaaaaaa....*"
    show player 56f with dissolve
    player_name "Eu deveria me preparar para"
    show player 11f
    "*Knock knock*"
    show debbie 2f at left
    show player 13f
    with dissolve
    deb "Hã?"
    deb "Essa freira está aqui de novo..."
    show debbie 1f
    show player 30f
    player_name "Novamente?"
    show player 24f
    pause
    show debbie 13f
    deb "Eu estive querendo te perguntar..."
    deb "O que exatamente você está fazendo para a igreja?"
    show debbie 14f
    show player 11f
    player_name "..."
    show debbie 13f
    deb "Quero dizer, estou surpreso em ver uma freira visitando tanto..."
    show debbie 14bf
    show player 29f at Position (xoffset=-35) with dissolve
    player_name "Sim, tudo está bem."
    player_name "Ela apenas ... vem trazer alguns recados."
    player_name "( Sim, heh ... heh... )"
    show player 3f at Position (xoffset=-35)
    show debbie 14f
    deb "..."
    show debbie 13f
    deb "Bem, pelo menos você está fazendo algo de bom para a comunidade..."
    show player 5f with dissolve
    show debbie 2f
    deb "Eu suponho que eu não deveria estar preocupada."
    show debbie 3f
    deb "Que mal poderia ser, você passar tempo na igreja?"
    hide debbie with dissolve
    show player 11f
    player_name "..."
    show player 37f at Position (xoffset=-41) with dissolve
    player_name "( Você não tem ideia... )"
    hide player with dissolve
    return

label bedroom_mom_overheard:
    scene expression game.timer.image("bedroom{}")
    show player 34 with dissolve
    player_name "...{b}*voz distante*{/b}..."
    show player 35
    player_name "( É {b}[deb_name]{/b} no telefone? )"
    show player 12
    player_name "( ...Ela parece estar com raiva ... Ela está gritando? )"
    show player 10
    player_name "( Eu deveria ir ver se ela está bem. )"
    hide player with dissolve
    return

label bedroom_mom_doorbell:
    scene expression game.timer.image("bedroom{}")
    show player 12 with dissolve
    player_name "( Campainha está tocando, alguém está na porta. )"
    player_name "( Deve ser {b}Erik{/b} precisando de alguma coisa... )"
    hide player with dissolve
    return

label bedroom_mom_movie_afterthoughts:
    scene expression game.timer.image("bedroom{}")
    show player 5
    player_name "Bem, isso foi super estranho!"
    player_name "Não tem como ela não ter notado..."
    player_name "Quero dizer, ela não disse nada."
    player_name "... mas definitivamente ficou desconfortável."
    show player 11
    player_name "eu espero que {b}[deb_name]{/b} não esteja chateada comigo..."
    player_name "..."
    show player 24
    player_name "Eu vou me preocupar com isso amanhã. Agora eu preciso dormir um pouco."
    hide player with dissolve
    return

label bedroom_mom_afterthoughts_two:
    scene location_home_bedroom_night_blur
    show player 13
    player_name "( Isso foi muito excitante! )"
    player_name "( seios da {b}[deb_name]{/b} tem gosto tão bom... )"
    player_name "( ... E ela ficou molhada o suficiente para meu short absorver! )"
    show player 5
    player_name "( ... )"
    player_name "( Ela meio que se apavorou no final. )"
    player_name "( Eu deveria ter me desculpado mais? )"
    player_name "( ... )"
    show player 13
    player_name "( Não faz sentido se preocupar com isso agora. Eu deveria dormir um pouco. )"
    hide player with dissolve
    return

label bedroom_mom_note:
    scene expression game.timer.image("bedroom{}")
    show player 7 with dissolve
    player_name "{b}*Uaaaaaa....*{/b}"
    show player 101 with dissolve
    player_name "eu deveria dormir."
    hide player with dissolve
    return

label bedroom_mom_note_just_wokeup:
    scene expression game.timer.image("bedroom{}")
    show player 7 with dissolve
    player_name "{b}*Uaaaaaa....*{/b}"
    show player 11
    player_name "!!!"
    show player 10
    player_name "Alguém deixou um {b}Bilhete{/b} na tela do meu computador?"
    hide player with dissolve
    return

label bedroom_mom_chores:
    scene expression game.timer.image("bedroom{}")
    show player 4 with dissolve
    if randomizer() < 50:
        player_name "Eu me pergunto se {b}[deb_name]{/b} precisa de ajuda em casa."
        player_name "Eu deveria ir perguntar a ela..."
    else:
        player_name "Eu me pergunto se {b}[deb_name]{/b} precisa da minha ajuda com qualquer outra coisa..."
    hide player with dissolve
    return

label bedroom_mom_search_panties:
    scene expression game.timer.image("bedroom{}")
    show player 4 with dissolve
    player_name "( Eu não consigo parar de pensar no outro dia no porão... )"
    player_name "( {b}[deb_name]{/b} realmente parecia estar gostando dessa massagem. )"
    player_name "( Suas pernas são tão macias e bem torneadas... )"
    show player 11
    player_name "( Pensando bem. A loção estava em sua gaveta de calcinha. )"
    player_name "( Eu gostaria de dar mais uma olhada! )"
    show player 13
    player_name "( Talvez agora seja um bom momento. )"
    hide player with dissolve
    return

label bedroom_mom_kissing_practice:
    scene expression game.timer.image("bedroom{}")
    show player 4 with dissolve
    player_name "Eu continuo tendo sonhos impertinentes envolvendo {b}[deb_name]{/b}."
    player_name "Está me deixando louco!"
    show player 5
    player_name "..."
    player_name "Eu deveria {b}falar com ela{/b} sobre isso..."
    hide player with dissolve
    return

label bedroom_bissette_french_food_assignment:
    scene expression game.timer.image("bedroom{}")
    show player 12 with dissolve
    player_name "Eu deveria fazer minha tarefa de francês."
    show player 14
    player_name "Eu tenho tudo que preciso para terminar agora."
    hide player with dissolve
    return

label bedroom_sis_couch_1:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "( Eu ouço alguém no corredor ... é a {b}[jen_name]{/b} na porta? )"
    show player 4
    player_name "( Eu me pergunto se ela está tramando alguma coisa. )"
    hide player with dissolve
    return

label bedroom_sis_couch_3:
    scene expression game.timer.image("bedroom{}")
    show player 4 with dissolve
    player_name "( Eu me pergunto se há um {b}novo vídeo pornô{/b} na TV hoje à noite. )"
    show player 26
    player_name "( Eu deveria tentar dar uma olhada enquanto todos estão dormindo... )"
    hide player with dissolve
    return

label bedroom_study01:
    if M_bissette.is_state(S_bissette_french_food_assignment):
        call expression game.dialog_select("bedroom_bissette_french_food_assignment_after")
        $ M_bissette.trigger(T_bissette_do_assignment)
        $ game.timer.tick()

    elif M_bissette.is_state(S_bissette_do_poem_assignment):
        call expression game.dialog_select("bedroom_bissette_do_poem_assignment")
        $ M_bissette.trigger(T_bissette_do_assignment)
        $ game.timer.tick()
    else:

        scene expression game.timer.image("bedroom{}")
        if M_bissette.between_states(S_bissette_find_food_book, [S_bissette_got_dexters_eriks_books, S_bissette_got_eriks_martinez_books, S_bissette_got_martinez_eriks_books]):
            call expression game.dialog_select("bedroom_bissette_find_books")
        else:

            call expression game.dialog_select("bedroom_no_school_work")
    $ game.main()

label bedroom_bissette_french_food_assignment_after:
    if not game.timer.is_dark():
        scene studybedroom01
    else:
        scene studybedroom02
    with fade
    show text "O livro era tudo que alguém gostaria de saber sobre o queijo.\nTudo, desde preparar, cozinhar e comer todos os tipos de queijos...\n...Mas eu finalmente consegui juntar alguns parágrafos que deveriam agradar {b}Ms. Bissette{/b}." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve
    return

label bedroom_bissette_do_poem_assignment:
    if not game.timer.is_dark():
        scene studybedroom01
    else:
        scene studybedroom02
    with fade
    show text "Escrever esse poema mostrou ser bastante difícil.\n...Eu parecia estar tendo dificuldade em manter meu foco.\nMas depois de várias horas e poucas ... pausas. Eu finalmente consegui colocar algo no papel!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide studybedroom01
    hide studybedroom02
    with dissolve
    scene expression game.timer.image("bedroom{}")
    show player 511 with dissolve
    player_name "Finalmente!"
    player_name "Espero que isso seja bom o suficiente para impressionar {b}Senhora. Bissette{/b}..."
    player_name "Eu só preciso {b}imprimi-lo{/b} no {b}laboratório de informática{/b} e entregá-lo."
    hide player with dissolve
    return

label bedroom_bissette_find_books:
    show player 73 with dissolve
    player_name "( Eu primeiro preciso pegar na escola o {b}livro didático{/b} antes que eu possa terminar meu {b}dever de casa{/b}... )"
    player_name "( Eu provavelmente posso encontrá-lo no local {b}biblioteca{/b}. )"
    hide player with dissolve
    return

label bedroom_no_school_work:
    show player 1 with dissolve
    player_name "( Eu não tenho nenhum trabalho escolar. )"
    hide player with dissolve
    return

label mia_midnight_text:
    call expression game.dialog_select("mia_midnight_text_dialogue")
    $ M_mia.trigger(T_mia_message)
    $ game.main()

label mia_midnight_text_dialogue:
    scene expression game.timer.image("bedroom{}")
    show player 442 with dissolve
    player_name "{b}Mia{/b}!? Pedindo ajuda?"
    player_name "O que é isso tudo?"
    player_name "Ela está com problemas?"
    show player 443
    player_name "..."
    show player 442
    player_name "Talvez eu deva {b}vê-la agora{/b}... Só para ter certeza que ela está bem."
    hide player with dissolve
    return

label mia_urgent_text:
    call expression game.dialog_select("mia_urgent_text_dialogue")
    $ M_mia.trigger(T_mia_message)
    $ game.main()

label mia_urgent_text_dialogue:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "Ela não consegue encontrar o pai dela?"
    player_name "É melhor eu ir ver o que está acontecendo..."
    hide player with dissolve
    return

label bed_locked:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "( Eu ainda tenho algo que preciso fazer antes de ir dormir... )"
    hide player 10 with dissolve
    $ game.main()

label bedroom_check_on_mom:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "( Eu deveria checar a {b}[deb_name]{/b}... )"
    hide player 10 with dissolve
    $ game.main()

label bedroom_sleeping_jerk_off_roxxy:
    $ M_player.set("sex speed", .4)
    scene expression game.timer.image("backgrounds/location_home_bedroom_jerk{}.jpg")
    show player 496c_496d_496e_496d_496c zorder 0 at Position(xpos=0.3375, ypos=0.875)
    show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0) with dissolve
    pause
    show roxxy dream 1 zorder 2 at Position(xpos=0.735, ypos=0.85) with dissolve
    pause
    show roxxy dream 2 with dissolve
    rox "Mmm, Olà {b}[firstname]{/b}..."
    rox "Estou tão feliz que você veio me ver pra me animar!"
    show roxxy dream 1 with dissolve
    player_name "..."
    show roxxy dream 2 with dissolve
    rox "Eu simplesmente não consigo manter a cabeça no lugar  ultimamente..."
    rox "Você foi tão útil, acho que você merece uma recompensa!"
    rox "Eu sei, que tal uma coisa especial, apenas para os seus olhos?"
    rox "Você gostaria, {b}[firstname]{/b}?"
    show roxxy dream 1 with dissolve
    $ M_player.set("sex speed", .3)
    show player 496c_496d_496e_496d_496c
    player_name "Você aposta que eu faria!"
    show roxxy dream 2 with dissolve
    rox "Hehe, bem você pode deitar e curtir o show!"
    rox "Continue acariciando aquele pau grande para mim {b}[firstname]{/b}!"
    show roxxy dream 3 with dissolve
    $ M_player.set("sex speed", .2)
    show player 496c_496d_496e_496d_496c
    rox "Me dê um C!"
    "C!"
    rox "Me dê um U!"
    "U!"
    rox "Me dê um M!"
    "M!"
    show player 496f
    rox "O que é esse feitiço?!"
    show player 496g
    player_name "HNNGGG!!!" with flash
    rox "Yay!!!"
    show player 496h
    hide jerkbubble
    hide roxxy dream
    player_name "Haah... Haaa..."
    player_name "Uuuhh Cara, estou coberto..."
    pause
    player_name "{b}Roxxy{/b} é tão quente!"
    return

label bedroom_sleeping_jerk_off_jenny:
    $ M_player.set("sex speed", .4)
    scene expression game.timer.image("backgrounds/location_home_bedroom_jerk{}.jpg")
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c zorder 0 at Position(xpos=0.3375, ypos=0.875) with None
    show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0)
    show jenny b_dream01 f_dream_talk a_empty zorder 2
    with dissolve
    jen "Olá, {b}[firstname]{/b}!"
    jen "Eu sei que posso ser malvada às vezes..."
    show jenny b_dream02 with dissolve
    jen "... Mas você sabe que eu realmente quero você, certo?"
    show jenny f_empty
    player_name "Você?"
    show jenny f_dream_talk
    jen "Mmhmm, Eu te quero tanto!"
    show jenny f_empty
    pause
    show jenny f_dream_talk
    jen "Eu quero  tão grande..."
    jen "Grosso..."
    jen "DURO..."
    show jenny f_empty
    player_name "Oh Deus!"
    show jenny f_dream_talk
    jen "Pênis"
    show jenny f_empty
    show player 496g with flash
    player_name "HNNGGG!!!"
    show player 496h
    hide jerkbubble
    hide jenny
    with dissolve
    player_name "Haah... Haah..."
    player_name "Uuuhh cara, estou coberto..."
    return

label bedroom_sleeping_jerk_off_diane:
    $ M_player.set("sex speed", .4)
    scene expression game.timer.image("backgrounds/location_home_bedroom_jerk{}.jpg")
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c zorder 0 at Position(xpos=0.3375, ypos=0.875) with None
    show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0)
    show diane dream1 zorder 2
    with dissolve
    dia "Olá bonitão."
    dia "Eu estava esperando que você aparecesse hoje."
    dia "Mmm, meus legumes não são suficientes para mim {b}[firstname]{/b}..."
    dia "Eu quero sentir aquele pau grande e grosso que você tem..."
    player_name "Tem certeza?"
    dia "A sim!"
    pause
    show diane dream2 with dissolve
    dia "É isso, garanhão."
    dia "Cuide do meu jardim especial!"
    pause
    dia "Eu preciso da sua semente."
    dia "Por favor, {b}[firstname]{/b}!"
    player_name "Oh Deus!"
    pause
    dia "Por favor, eu preciso tanto!"
    dia "Enche-me!!!"
    show player 496g with flash
    player_name "HNNGGG!!!"
    show player 496h
    hide jerkbubble
    hide diane
    with dissolve
    player_name "Haah... Haah..."
    pause
    player_name "Atirar ... em toda parte..."
    return

label bedroom_sleeping_jerk_off_debbie:
    $ M_player.set("sex speed", .4)
    scene expression game.timer.image("backgrounds/location_home_bedroom_jerk{}.jpg")
    show player 496 zorder 0 at Position(xpos=0.3375, ypos=0.875)
    pause
    show player 496b
    player_name "... {b}[deb_name]{/b} é tão bonito."
    player_name "Eu simplesmente não consigo parar de pensar nisso."
    player_name "... sobre ela."
    player_name "Mmm, Deus, eu a quero tanto!"
    show player 496c
    show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0) with dissolve
    pause
    show debbied 1 zorder 2 at Position(xpos=0.735, ypos=0.85) with dissolve
    pause
    show debbied 2
    deb "Bem, olá ..."
    show debbied 1
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    show debbied 2
    deb "Oh meu Deus ... Isso é para mim?"
    deb "... É tão grande!"
    show debbied 1
    pause
    show debbied 2
    deb "... e grosso."
    show debbied 3 with dissolve
    deb "Mmm, você vai me dar?"
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    deb "Me dê isto, {b}[firstname]{/b}!"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / 1)
    show debbied 4_5
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    pause
    show player 496f
    player_name "OH!"
    show player 496g with flash
    player_name "HHHNNNGGGG, HHuuuUUHH!!"
    show player 496h
    hide jerkbubble
    hide debbied
    player_name "Haaaah... Haaaah..."
    player_name "Uuuhh cara, estou gozando..."
    return

label bedroom_sleeping_jerk_off_mia:
    $ M_player.set("sex speed", .4)
    scene expression game.timer.image("backgrounds/location_home_bedroom_jerk{}.jpg")
    show player 496 zorder 0 at Position(xpos=0.3375, ypos=0.875)
    pause
    show player 496b
    player_name "{b}Mia{/b} é tão fofa!"
    player_name "Eu não posso esperar para vê-la novamente..."
    pause
    player_name "... Aquele corpo bonito dela."
    player_name "Mmm..."
    show player 496c
    show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0) with dissolve
    pause
    show miad 1 zorder 2 at Position(xpos=0.735, ypos=0.8) with dissolve
    pause
    show miad 2
    mia "Ei, {b}[firstname]{/b}!"
    show miad 1
    pause
    show miad 2
    mia "Uau, eu nunca vi um desses antes!"
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    mia "Eles são tão grandes assim?!"
    show miad 1
    pause
    show miad 2
    mia "Eu estava realmente esperando que você fosse meu primeiro {b}[firstname]{/b}."
    show miad 1
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    pause
    show miad 2
    mia "Você acha que vai caber?"
    mia "... Na minha..."
    show miad 1
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    pause
    show miad 2
    mia "...Na minha buceta?"
    show player 496f
    player_name "OH!"
    show player 496g with flash
    player_name "HHHNNNGGGG, HHuuuUUHH!!"
    show player 496h
    hide jerkbubble
    hide miad
    player_name "Haaaah... Haaaah..."
    player_name "Uuuhh cara, estou gozando..."
    return

label bedroom_sleeping_debbie_movie_night:
    scene expression game.timer.image("bedroom{}")
    show player 101b with dissolve
    player_name "Acho que ouvi {b}[deb_name]{/b} fazendo algo lá embaixo."
    hide player with dissolve
    return

label bedroom_sleeping_debbie_sleepover:
    scene expression game.timer.image("bedroom{}")
    show player 101b with dissolve
    player_name "Talvez eu deva dormir ao lado de {b}[deb_name]{/b} esta noite."
    player_name "Ela disse que eu poderia visitá-la à noite se eu quisesse..."
    hide player with dissolve
    return

label bedroom_sleeping_erik_thief_pre:
    scene location_home_bedroom_cutscene01 with fade
    pause
    "{b}*Thump*{/b}"
    scene bedroom_cs03 with dissolve
    "{b}*Thump Thump*{/b}"
    player_name "..."
    scene bedroom_cs04 with dissolve
    player_name "Que barulho é esse?"
    scene bedroom_night with fade
    show player 101bf
    player_name "( Parece que vem de fora. )"
    player_name "( ... deve ser {b}Erik's{/b} no quintal, talvez? )"
    show player 100bf
    return

label bedroom_sleeping_erik_thief_use_telescope:
    show player 101bf
    player_name "( Eu provavelmente deveria ir dar uma olhada. )"
    show player 100f
    player_name "Hmm..."
    show player 101bf
    player_name "( Vou dar uma olhadinha pelo meu telescópio. )"
    hide player

    scene windowbackyardnight02a
    player_name "!?!"
    player_name "O que..."
    scene windowbackyardnight02b
    player_name "( É alguém se esgueirando no quintal do {b}Erik{/b} ?! )"
    player_name "( Esse é o {b}assaltante{/b} Eu tenho ouvido falar nas notícias! )"
    scene windowbackyardnight02c
    player_name "..."
    player_name "( Ele está indo para casa de {b}Erik{/b} )"

    scene bedroom_night with fade
    show player 101bf with dissolve
    player_name "( Isto é mau! )"
    player_name "( E se {b}Erik{/b} e {b}Sra. Johnson{/b} estão em perigo? )"
    player_name "( Eu deveria sair e ver o que ele está fazendo no jardim do {b}Erik{/b}.)"
    hide player with dissolve
    return

label bedroom_sleeping_erik_thief_sleep:
    show player 101f
    player_name "( Provavelmente é apenas algum animal. )"
    player_name "( Eu preciso dormir... )"
    hide player
    return

label bedroom_sleeping_erik_bullying_3_started:
    scene expression game.timer.image("bedroom{}")
    show player 12 with dissolve
    player_name "( Cara ... que dia. )"
    show player 17
    player_name "( Eu acho que o treinamento na academia está começando a valer a pena! )"
    pause
    show player 12
    player_name "( {b}Dexter{/b} nunca vai deixar isso passar. )"
    player_name "(... Eu vou precisar de todo o treinamento que conseguir! )"
    show player 8 with dissolve
    pause
    show player 7 with dissolve
    player_name "{b}*Uaaaaaa....*{/b}"
    show player 101 with dissolve
    player_name "( É melhor eu dormir um pouco. )"
    hide player with dissolve
    return

label bedroom_sleeping_dewitt_eve_karaoke:
    scene expression game.timer.image("bedroom{}")
    show player 14 with dissolve
    player_name "Eu deveria conhecer {b}Eve{/b} esta noite! na casa de {b}Erik{/b}."
    show player 30
    player_name "O sono terá que esperar."
    hide player with dissolve
    return

label bedroom_sleeping_dewitt_school_sneak_mission:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "Hoje à noite, eu ia esgueirar para a escola com {b}Erik{/b}."
    player_name "Eu não posso ir para a cama ainda."
    hide player with dissolve
    return

label bedroom_sleeping_mia_midnight_call:
    scene location_home_bedroom_cutscene01 with dissolve
    player_name "Zzz..."
    "{b}Bzzt{/b}!"
    player_name "..."
    "{b}Bzzzzzzt{/b}!"
    scene bedroom_cs04 with dissolve
    player_name "Hã"
    player_name "Esse é o meu celular?"
    scene black with fade
    pause
    scene bedroom_night
    show player 7 with dissolve
    pause
    show player 101
    player_name "Alguém está me mandando mensagens?"
    player_name "Eu deveria ver quem é..."
    hide player with dissolve
    return

label bedroom_sleeping_debbie_solo_dream:
    scene dream_debbie_04 with fade:
        ypos -707
        linear 4.0 ypos 0
    deb "Mmm..."
    deb "Oh, isso é maravilhoso, querido."
    player_name "..."
    player_name "Oh, {b}[deb_name]{/b}..."
    deb "eu quero você {b}[firstname]{/b}!"
    deb "Eu quero você dentro de mim!"
    player_name "{b}*Gole*{/b}"
    player_name "Serio"
    deb "Você não tem ideia! Me dê esse pau grande e duro, {b}[firstname]{/b}!"
    deb "Por favor, eu preciso disso!"
    player_name "..."
    deb "Faça isso agora! De Pressa! Eu não posso esperar mais!"
    scene dream_debbie_05 with dissolve:
        ypos 0
    pause
    player_name "Hnnggg!!" with flash
    pause
    scene dream_debbie_05 with flash:
        ypos 0
        linear 4.0 ypos -475
    player_name "... Oooooh..."
    pause

    scene location_home_bedroom_cutscene06 with fade
    pause
    scene location_home_bedroom_cutscene07
    player_name "..."
    scene location_home_bedroom_cutscene08
    player_name "Caralho..."
    pause
    scene location_home_bedroom_cutscene09
    pause
    player_name "Eu fiz uma bagunça..."
    player_name ".. Mas porcaria, isso foi intenso..."
    player_name "Tudo parecia tão real!"
    player_name "Arrgghh, Eu estou realmente fazendo isso!"
    player_name "Eu não consigo parar de pensar nela!"
    player_name "Eu quero abraçá-la e beijá-la..."
    player_name "Talvez eu deva tentar {b}conversar com{b}[deb_name]{/b} sobre beijar ela{/b}?"
    player_name "Ela parecia ter gostado, quando eu a beijei no shopping..."
    player_name "Hmm, é arriscado, mas acho que vale a pena tentar!"
    player_name "Eu posso enlouquecer se eu não fizer algo..."
    player_name "... Mas primeiro, devo me limpar e dormir mais um pouco."
    return

label bedroom_sleeping_debbie_night_visit:
    scene location_home_bedroom_cutscene01 with dissolve
    player_name "Zzz..."
    scene location_home_bedroom_cutscene02 with dissolve
    deb "( ... )"
    deb "( Eu não consigo dormir. )"
    deb "( Desde que eu vi ele, Se masturbando... )"
    deb "( Eu não consigo parar de pensar no seu pau )"
    deb "( eu só... )"
    deb "( ... )"
    define fadehold = Fade(0.5, 1.0, 0.5)

    scene location_home_bedroom_sex01
    show debbies 1
    with dissolve
    deb "( Eu não posso acreditar que estou tendo esses pensamentos... )"
    deb "( De estar com ele. Ele é apenas um jovem. )"
    deb "( ... Mas eu sou madura, O suficiente para saber o certo! )"
    show debbies 2
    deb "( Ele realmente não me quer! É apenas uma paixão idiota! )"
    deb "( Eu tenho idade suficiente para ser{b}Mãe{/b}dele! )"
    deb "( ... Mas o jeito que ele me faz sentir. )"
    show debbies 3
    deb "( A maneira como ele olha para mim com aqueles olhos famintos... )"
    show debbies 4
    deb "( ... Mmm, Eu preciso ver... )"
    show debbies 5
    deb "( Só uma espiada. )"
    show debbies 6
    deb "( ... )"
    show debbies 7_8
    pause 4
    show debbies 6
    deb "( É tão grande... )"
    show debbies 7_8
    deb "( ... E está ficando maior. )"
    deb "( Mmm... )"
    show debbies 9
    pause
    show debbies 10
    deb "( Eu tenho que ver isso! )"
    deb "( Ahh, é tão grosso... )"
    show debbies 11
    deb "( !!! )"
    show debbies 12
    deb "{b}*Respiração penosa*{/b}!"
    deb "( É tão inacreditável! )"
    deb "( {b}*Suspiro*{/b} O que eu vou fazer? )"
    deb "( Eu simplesmente não consigo tirar esse pau da minha cabeça! )"
    deb "( ... )"
    deb "( Faz tanto tempo desde que eu senti um... )"
    deb "( ... E eu sinto muita falta disso. )"
    deb "( Não seria ruim em tocar só um pouquinho...Só um pouquinho. Certo? )"
    deb "( Certamente, é desconfortável para ele. Basta ver como estar duro! )"
    show debbies 13
    pause
    show debbies 14
    pause
    deb "( ... E Tão duro... )"
    deb "( ... E grosso. )"
    show debbies 13
    deb "..."
    show debbies 13_14
    pause
    deb "( Oh Deus. O que eu estou fazendo?! )"
    deb "..."
    deb "( Estou acariciando seu pau! )"
    deb "( Hah ... e grande e suculento )"
    deb "( Assim como ele estava acariciando para mim mais cedo. )"
    pause
    deb "( Ele diz que me quer ... Ele me quer tanto que se masturba enquanto pensa em mim! )"
    deb "( Mmm... )"
    deb "( Ele quer me foder com esse pau )"
    show debbies 12
    deb "( ... )"
    show debbies 20
    deb "( O que há de errado comigo? )"
    show debbies 21
    deb "( Oh Deus! )"
    deb "( Eu preciso sair daqui! )"
    deb "( ... vai embora, {b}[deb_name]{/b}! )"
    show debbies 22 at Position(xpos = 544, ypos = 768)
    player_name "Hmm?"
    show debbies 23
    player_name "O que?"
    player_name "( tem alquem aqui? )"
    show debbies 24 at Position(xpos = 512, ypos = 768)
    player_name "( Hmm, não é nada. )"
    return

label bedroom_sleeping_debbie_night_visit_two:
    label mom_night_suck:
        scene location_home_bedroom_cutscene01 with dissolve
    player_name "Zzz..."
    scene location_home_bedroom_cutscene02 with dissolve
    pause
    scene location_home_bedroom_sex01
    show debbies 1
    with dissolve
    deb "( O que estou fazendo aqui de novo?! )"
    deb "( Por que não consigo parar de pensar em seu pênis? )"
    deb "( Eu continuo imaginando dentro de mim! )"
    show debbies 2
    deb "( ... )"
    deb "( ... Talvez Diane esteja certa; Talvez eu deva apenas relaxar e me soltar. )"
    deb "( Eu quero tanto isso... )"
    deb "( Mmm, Estou me molhando só de pensar nisso... )"
    show debbies 3
    deb "( Eu tenho que ver isso de novo! )"
    show debbies 4
    deb "( ... )"
    show debbies 5
    deb "( Ah, isso é tão errado ... O que você está fazendo?, {b}[deb_name]{/b}? )"
    show debbies 6
    deb "( É ainda maior do que eu me lembro... )"
    show debbies 7_8
    pause 4
    show debbies 6
    deb "( Mmm e está crescendo novamente... )"
    show debbies 7_8
    deb "( ... E Tão {b}Duro{/b}. )"
    deb "( ... )"
    deb "( ... Talvez eu pudesse apenas pegar um pouco... )"
    show debbies 9
    pause
    show debbies 10
    deb "( ... Quero dizer, deve ser desconfortável para ele. )"
    deb "( Estou apenas ajudando ele relaxar ... Isso é tudo. )"
    show debbies 11
    deb "( !!! )"
    show debbies 12
    deb "..."
    deb "( Oh Senhor, ajuda-me! )"
    deb "( Mmm... )"
    show debbies 13
    deb "( Eu simplesmente não consigo resistir a tocá-lo! )"
    deb "( É tão bom nas minhas mãos... )"
    show debbies 13_14
    deb "( É tão grosso... )"
    deb "( ... e suculento. )"
    deb "( ... )"
    deb "( Faz tanto tempo... )"
    deb "( eu quero... )"
    deb "( Eu quero provar! )"
    show debbies 15
    deb "( Eu {b}PRECISO{/b}provar! )"
    deb "( Só por um segundo! Isso não poderia machucar, certo? )"
    show debbies 16_17
    deb "( Sim!! )"
    deb "( Oh Deus, eu sinto muita falta disso! )"
    deb "( Estou tão excitada! )"
    show debbies 18
    player_name "{b}*Gemido*{/b}"
    show debbies 19
    deb "( !!! )" with hpunch
    deb "( Oh droga! Ele está acordando... )"
    deb "( ... )"
    show debbies 20
    deb "( O que eu estou fazendo?! )"
    deb "( Eu não posso deixar ele me ver assim! )"
    show debbies 21
    deb "( Eu tenho que sair daqui! )"
    show debbies 22 at Position(xpos = 544, ypos = 768)
    player_name "Hmm?"
    show debbies 23
    player_name "O que? "
    player_name "( Eu devo ta maluco? )"
    show debbies 24 at Position(xpos = 512, ypos = 768)
    player_name "( ... )"
    player_name "( Eu acho que não foi nada... )"
    $ renpy.end_replay()
    return

label bedroom_sleeping_debbie_midnight_noises:
    scene bedroom_cs01 with fade
    "Ha ha ha..."
    "{b}*BARULHO*{/b}"
    scene bedroom_cs03 with dissolve
    player_name "..."
    scene bedroom_cs04
    player_name "Quem está fazendo todo esse barulho do lado de fora?"
    scene bedroom_cs03
    player_name "..."
    player_name "......"
    scene bedroom_cs01 with dissolve
    pause
    "{b}*BARULHO*{/b}"
    scene bedroom_cs04 with dissolve
    player_name "O que está acontecendo?"

    scene bedroom_night
    show player 101b
    with dissolve
    player_name "Talvez eu deva ir ver o que está acontecendo."
    player_name "Parece que quem está lá fora não vai parar tão cedo."
    show player 8 with dissolve
    return

label bedroom_sleeping_debbie_night_visit_three:
    $ M_mom.set("sex speed", .175 / .75)
    scene location_home_bedroom_cutscene01 with dissolve
    player_name "Zzz..."
    scene location_home_bedroom_cutscene02 with dissolve
    pause
    scene location_home_bedroom_sex01
    show debbies 1
    with dissolve
    deb "( Ahh... )"
    deb "( estou aqui... )"
    show debbies 3
    deb "( O que eu estou fazendo! )"
    show debbies 4
    deb "( O QUE EU ESTOU FAZENDO!!! )"
    show debbies 5
    deb "( Mmm! )"
    deb "( Aqui vamos nòs! )"
    show debbies 6
    deb "( Ahh, eu quero isso muito duro... )"
    show debbies 7_8
    deb "( Fique duro para mim, querido... )"
    deb "( Por favor... )"
    show debbies 6
    pause
    show debbies 9
    pause
    show debbies 10
    deb "( ... )"
    show debbies 11
    deb "( !!! )"
    show debbies 12
    deb "..."
    deb "( Ahh, Estou queimando ... eu preciso disso!!! )"
    show debbies 15
    deb "( Mmm. )"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / .75)
    show debbies 16_17
    deb "( E! Tão bom! )"
    deb "( Eu sinto esse gosto! )"
    player_name "( Mmm. )"
    deb "{b}*Lamber*{/b}"
    show debbies 19
    player_name "Hmm?"
    show debbies 20b
    player_name "O que? "
    show debbies 20c at Position(xpos=0.53, ypos=1.0) with dissolve
    player_name "... {b}[deb_name]{/b}?"
    show debbies 20d
    deb "Está tudo bem, {b}[firstname]{/b}, sou eu."
    show debbies 20c
    player_name "... Ok."
    player_name "Mas o que"
    show debbies 20d
    deb "Shhh..."
    show debbies 20c
    player_name "{b}[deb_name]{/b}? O que você "
    show debbies 20e with dissolve
    deb "Silêncio, docinho, apenas relaxe..."
    player_name "..."


    deb "Eu preciso disso, {b}[firstname]{/b}!"
    deb "Eu preciso desse pau grande dentro de mim!!!"
    show debbies 20f at Position(xpos=0.5, ypos=1.0) with dissolve
    player_name "{b}*Gole*{/b}"
    deb "eu tentei..."
    deb "Eu tentei tanto resistir."
    deb "... Mas eu não posso!"
    show debbies 20g with dissolve
    deb "Por favor, não pense menos de mim..."
    pause
    show debbies 20h with hpunch

    player_name "... Ooohh!!"
    deb "Haaaaaaaah!"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / 1.75)
    show debbies 20h_20i_20j_20k_20l_20m_20n_20o
    deb "Oh Deus!!"
    pause
    deb "Nossa, é ainda melhor do que eu imaginava!"
    player_name "Ahh, {b}[deb_name]{/b} isso é tão bom!"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / 2)
    show debbies 20h_20i_20j_20k_20l_20m_20n_20o
    deb "Haah! {b}[firstname]{/b}! Oh, {b}[firstname]{/b}!"
    deb "Eu vou gozar!"
    show debbies 20h with flash
    deb "AAHHH!!"

    player_name "... Você está tremendo! Você está bem, {b}[deb_name]{/b}?!"
    deb "Haaah... Haaaah..."
    deb "... Não se preocupe, querido."
    show debbies 20h_20i_20j_20k_20l_20m_20n_20o
    deb "Continue, isso é tão bom!"
    player_name "..."
    deb "Me dê isto!!"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / 1.5)
    show debbies 20h_20i_20j_20k_20l_20m_20n_20o
    deb "OOOH Sim!!!"
    deb "É isso aí, Baby!!"
    deb "Me dê esse pau gordo!"
    return

label bedroom_sleeping_debbie_night_visit_three_loop:
    menu:
        "Continue." if keep_going < 2:
            $ keep_going += 1
            if M_mom.get("change angle"):
                show expression AnimatedImage("debbies", [170,171,172,173,174,175,176,177], M_mom) as debbies
            else:

                show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_mom) as debbies
            pause
            jump expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_loop")

        "Mudar o ângulo." if keep_going < 2:
            $ keep_going += 1
            if not M_mom.get("change angle"):
                $ M_mom.set("sex speed", .15)
                $ M_mom.set("change angle", True)
                hide debbies
                scene bedroom_sex_05
                show expression AnimatedImage("debbies", [170,171,172,173,174,175,176,177], M_mom) as debbies
                with fade
            else:

                $ M_mom.set("sex speed", ((.175 / .75) / 3) / 1.5)
                $ M_mom.set("change angle", False)
                hide debbies
                scene location_home_bedroom_sex01
                show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_mom) as debbies
                with fade
            pause
            jump expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_loop")
        "Gozar.":

            call expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_cum_pre")


            if M_player.is_set("pet cat"):
                scene location_home_bedroom_sleeping4 with fade
            else:
                scene location_home_bedroom_sleeping2 with fade

            if store._in_replay == None:
                show unlock11 at truecenter with dissolve
                $ renpy.pause()
                hide unlock11

            call expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_cum_after")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["10_unlocked"] = True
    $ M_mom.trigger(T_mom_midnight_fun)
    $ Sleep()
    $ M_player.set("just wokeup", False)
    $ game.main()

label bedroom_sleeping_debbie_night_visit_three_cum_pre:
    player_name "Oh, {b}[deb_name]{/b}... Eu vou..."
    player_name "... Eu vou!!"
    deb "Não pare !! Não pare"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / .075)
    scene location_home_bedroom_sex01
    show debbies 20p_20q
    with flash
    player_name "HHNNGGG!!!!!"

    deb "AAAAAAAAHHHH!!!"
    pause
    show debbies 20h

    player_name "{b}*Ofegante*{/b}"

    deb "Mmm..."
    show debbies 20r with dissolve
    deb "..."
    show debbies 20s with dissolve
    deb "Oh meu Deus..."
    show debbies 20t
    player_name "Isso foi incrível!"
    show debbies 20s
    deb "Hehe, foi realmente..."
    deb "..."
    deb "Eu sinto muito, querido!"
    deb "Eu não deveria ter feito isso..."
    show debbies 20t
    player_name "O que!? Não, não diga isso!"
    deb "..."
    player_name "Eu também queria isso!"
    show debbies 20s
    deb "... Você queria?"
    show debbies 20t
    player_name "Você não tem ideia! eu penso nisso ja faz tempo, praticamente não parava de pensar nisso!"
    show debbies 20s
    deb "... Mesmo?"
    show debbies 20t
    player_name "Sim!"
    player_name "eu te amo, {b}[deb_name]{/b}!"
    show debbies 20s
    deb "Eu também te amo, {b}[firstname]{/b}!"
    deb "..."
    deb "Ninguém nunca me fez gozar assim antes!"
    show debbies 20t
    player_name "Nunca?"
    show debbies 20s
    deb "Nunca. esse foi um orgasmo muito louco!"
    show debbies 20t
    player_name "Desculpe eu não aguentei segurar por muito tempo..."
    show debbies 20s
    deb "Não, você fez muito bem, querido! Especialmente pela primeira vez!"
    show debbies 20t
    player_name "... Primeira vez?"
    deb "..."
    player_name "Podemos fazer isso de novo? {b}[deb_name]{/b}?"
    show debbies 20s
    deb "Humm Querido, tem certeza de que é o que você quer?"
    show debbies 20t
    player_name "Claro!!!"
    player_name "{b}[deb_name]{/b}, e o que mais quero!"
    show debbies 20s
    deb "O meu Deus..."
    deb "Eu odeio admitir isso, mas sinto o mesmo!"
    deb "..."
    deb "Tudo bem querido..."
    deb "... Mas só podemos Fazer isso, Quando não tiver ninguém por perto!"
    deb "E você não pode dizer {b}PRA NINGUÉM{/b}! Especialmente {b}[jen_name]{/b}!"
    deb "Voce entendeu?!"
    show debbies 20t
    player_name "Sim entendir."
    show debbies 20s
    deb "{b}[firstname]{/b}, Estou falando sério! Você não pode dizer a ninguém sobre isso!"
    show debbies 20t
    player_name "Eu não vou {b}[deb_name]{/b}. eu prometo."
    show debbies 20s
    deb "Bom menino."
    deb "{b}*Bocejar*{/b}"
    deb "Estou exausta agora."
    show debbies 20t
    player_name "Sim eu também."
    show debbies 20s
    deb "Mmm, Eu poderia dormir aqui mesmo."
    show debbies 20t
    player_name "Sim dorme comigo esta noite, {b}[deb_name]{/b}."
    show debbies 20s
    deb "Eu acho que estaria tudo bem. Se eu sair antes da {b}[jen_name]{/b} acordar."



    scene location_home_bedroom_cutscene_sleep
    with fade
    show text "{b}[deb_name]{/b} e eu finalmente dormimos junto." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Foi espetacular! Todas as nossas ansiedades reprimidas evaporaram em um instante!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Nossas preocupações desapareceram quando ela adormeceu em meus braços." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... Acordamos na manhã seguinte sentindo melhor do que qualquer um de nós poderia lembrar." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    return

label bedroom_sleeping_debbie_night_visit_three_cum_after:

    scene location_home_bedroom_sex04
    show debbies 20u
    pause
    show debbies 20v
    player_name "{b}[deb_name]{/b}?"
    show debbies 20u
    player_name "..."
    show debbies 20v
    player_name "{b}[deb_name]{/b}, acorde."
    show debbies 20u
    deb "Hmm?"
    show debbies 20x
    deb "{b}*Bocejar*{/b} Já é de manhã?"
    show debbies 20w
    player_name "Temo que sim."
    show debbies 20x
    deb "Oh, eu dormi como uma pedra..."
    show debbies 20w
    player_name "Heh, sim, eu também."
    show debbies 20x
    deb "Mmm, tudo bem. Acho que é melhor eu sair daqui antes que {b}[jen_name]{/b} acorde."
    show debbies 20w
    player_name "Tem certeza de que não quer brincar um pouco mais?"
    show debbies 20x
    deb "Hehe, Não me provoca, querido. Esse seu pau grande é difícil de dizer não."
    show debbies 20w
    player_name "Eu nunca vou me cansar de ouvir isso!"
    show debbies 20x
    deb "Venha me encontrar mais tarde, ok?"
    scene black with fade
    return

label bedroom_sleeping_debbie_smith_dream:
    scene dream_debbie 1 at Position(ypos=1475) with fade
    deb "Bom dia, querido."
    deb "sou eu, {b}[deb_name]{/b}."
    player_name "{b}[deb_name]{/b}?"
    player_name "Onde estamos?"
    deb "Está bem. Tudo ficará bem..."
    deb "Deixe-me cuidar de você."
    scene dream_debbie 1_2:
        linear 5.0 ypos -707
    player_name "{b}[deb_name]{/b}..."
    player_name "O que você está fazendo..."
    deb "Tudo bem ... Eu só quero que você se sinta bem..."
    player_name "{b}[deb_name]{/b}... Isso é incrível!"
    scene dream_debbie 3
    player_name "( !!! )" with hpunch
    smi "{b}[firstname]{/b}!!!"
    scene dream_debbie 3:
        ypos -707
        linear 1.0 ypos 0
    smi "O que você está fazendo aqui?"
    smi "Você está dormindo?!"

    smi "Vá para a aula agora ou estou enviando sua bunda para {b}DETENÇÃO{/b}!"
    scene black with fade
    pause .2
    scene expression game.timer.image("bedroom{}")
    show player 264
    with dissolve
    player_name "{b}*Uaaaaaa....*{/b}"
    show player 265 with dissolve
    player_name "( !!! )"
    show player 266
    player_name "( Esse foi um sonho tão estranho! )"
    player_name "( {b}[deb_name]{/b} e eu estava fazendo coisas e ela estava nua! )"
    player_name "( Então {b}Principal Smith{/b}... )"
    show player 267 with hpunch
    player_name "( !!! )"
    show player 268
    player_name "( Isso é normal?! )"
    player_name "( Eu nunca tive esses tipos de sonhos com {b}[deb_name]{/b} antes... )"
    hide player with dissolve
    return

label bedroom_debbie_sleepover_pre:
    $ M_mom.set("sex speed", .12)
    scene location_home_bedroom_sex01 with fade
    show debbies 1
    player_name "( ... )"
    deb "Querido?"
    deb "Você dormiu esperando por mim?"
    player_name "( ... )"
    show debbies 3
    pause
    show debbies 4
    pause
    show debbies 5
    pause
    show debbies 6
    deb "... Acorde, queridO."
    $ M_mom.set("sex speed", .09)
    show debbies 7_8
    deb "Mmm..."
    show debbies 6
    pause
    show debbies 9
    pause
    show debbies 10
    deb "( ... )"
    show debbies 11
    deb "( !!! )"
    show debbies 12
    pause
    show debbies 20b
    deb "{b}[firstname]{/b}?"
    player_name "... Hmm?"
    show debbies 20c at Position(xpos=0.53, ypos=1.0) with dissolve
    player_name "... {b}[deb_name]{/b}?"
    player_name "Porcaria, adormeci?"
    show debbies 20d
    deb "Hehe, tudo bem, queridO."
    show debbies 20c
    player_name "Você ainda quer?"
    show debbies 20e with dissolve
    deb "Não queremos acordar {b}[jen_name]{/b}!"
    player_name "Oh! ... Sim, desculpe-me."
    show debbies 20f at Position(xpos=0.5, ypos=1.0) with dissolve
    deb "Hehe..."
    deb "Está tudo bem, você está apenas animado. Estou animado também!"
    deb "Eu mal podia esperar {b}[jen_name]{/b} ir pra cama."
    show debbies 20g with dissolve
    player_name "Uau, {b}[deb_name]{/b}, você está encharcada!"
    deb "Eu te disse que estava animada."
    show debbies 20h with dissolve
    deb "Mmm..."
    deb "Agora, não vamos perder tempo ... Dê para mim, querido!"
    $ M_mom.set("sex speed", .06)
    show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_mom) as debbies
    $ animated = True
    return

label bedroom_debbie_sleepover:
    call expression game.dialog_select("bedroom_debbie_sleepover_pre")
    $ M_mom.set("change angle", False)
    jump expression game.dialog_select("bedroom_debbie_sleepover_loop")

label bedroom_debbie_sleepover_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_mom.get("change angle"):
                    scene bedroom_sex_05
                    show expression AnimatedImage("debbies", [170,171,172,173,174,175,176,177], M_mom) as debbies
                    with dissolve
                else:
                    scene location_home_bedroom_sex01
                    show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_mom) as debbies
                    with dissolve
                $ animated = True
            pause 5
            call expression game.dialog_select("bedroom_debbie_sleepover_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            if M_mom.get("change angle"):
                scene bedroom_sex_05
                $ pose_list = [170,171,172,173,174,175,176,177]
            else:
                scene location_home_bedroom_sex01
                $ pose_list = ["20h","20i","20j","20k","20l","20m","20n","20o"]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("bedroom_debbie_sleepover_hscene_dialog")
        $ animcounter += 1
    call screen bedroom_debbie_sleepover_options

label bedroom_debbie_sleepover_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        deb "Ahh!!!{p=1}{nw}"
        deb "Oh {b}[firstname]{/b}, é tão profundo!{p=2}{nw}"
        deb "Você gosta quando eu te aperto com minha buceta?{p=2}{nw}"
        player_name "Oh Deus, sim!{p=1}{nw}"
        deb "{b}[firstname]{/b}!{p=1}{nw}"
    elif animcounter == 0 and randomizer() > 50:
        deb "Oh Sim!!!{p=1}{nw}"
        deb "É isso aí, Baby! Foda minha buceta!{p=2}{nw}"
        deb "Mmm, você gosta disso?{p=1}{nw}"
        player_name "Sim, {b}[deb_name]{/b}!{p=1}{nw}"
        deb "Mais rápido, baby!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 50:
        deb "Oh Deus, isso é bom!{p=1}{nw}"
        deb "Quem é meu garoto travesso?{p=1}{nw}"
        player_name "Mmm, sou eu...{p=1}{nw}"
        deb "Está certo Baby! Me foda mais forte!{p=2}{nw}"
        player_name "Uuhh!! Você gosta desse pau duro, {b}[deb_name]{/b}?{p=2}{nw}"
        deb "Aaahh!! sim! simm! SIMMMMMMM!!{p=1}{nw}"
        deb "Me dê istoooooooo!{p=1}{nw}"
    return

label bedroom_debbie_sleepover_cum:
    call expression game.dialog_select("bedroom_debbie_sleepover_cum_dialogue")

    if M_player.is_set("pet cat"):
        scene location_home_bedroom_sleeping4 with fade
    else:
        scene location_home_bedroom_sleeping2 with fade

    show unlock11 at truecenter with dissolve
    pause
    $ Sleep()
    hide unlock11 with dissolve
    $ M_player.set("just wokeup", False)

    if randomizer() < 70 and not M_mom.is_state(S_mom_note):
        call expression game.dialog_select("bedroom_debbie_sleepover_after_random_70")
    else:

        call expression game.dialog_select("bedroom_debbie_sleepover_after_not_random")
        if not M_mom.is_set("basement sex"):
            call expression game.dialog_select("bedroom_debbie_sleepover_after_not_basement_sex")
            $ M_mom.trigger(T_mom_delay)
        hide player with dissolve
    $ game.main()

label bedroom_debbie_sleepover_cum_dialogue:
    player_name "... Oh!"
    player_name "{b}[deb_name]{/b}, Eu vou gozar..."
    deb "Faça isso, Baby! goza dentro de mim!"
    $ M_mom.set("sex speed", .4)
    scene location_home_bedroom_sex01
    show debbies 20p_20q
    with flash
    player_name "Uhhhuh!!!"
    deb "Hnnngg!!"
    deb "AAAAHHhh!!!"
    player_name "Shh! Você vai acordar {b}[jen_name]{/b}!"
    player_name "..."
    show debbies 20h with dissolve
    deb "Huhhh, huhhh, huhhh..."
    show debbies 20r with dissolve
    pause
    show debbies 20s with dissolve
    deb "Oh {b}[firstname]{/b}... isso foi..."
    show debbies 20t
    player_name "Surpreendente?"
    show debbies 20s
    deb "Ufa ... Sim!"
    deb "Mmm, Eu não posso sentir minhas pernas."
    pause
    deb "... eu te amo, {b}[firstname].{/b}"
    show debbies 20t
    player_name "eu também te amo, {b}[deb_name]{/b}. Você é icrível!"
    show debbies 20s
    deb "Obrigado querido."
    return

label bedroom_debbie_sleepover_after_random_70:
    scene location_home_bedroom_sex04
    show debbies 20u
    pause
    show debbies 20v
    player_name "Acorde, {b}[deb_name]{/b}."
    show debbies 20u
    deb "Mmm..."
    show debbies 20w
    player_name "O sol está no céu."
    show debbies 20x
    deb "Bom dia querido."
    show debbies 20w
    player_name "Você dormiu bem?"
    show debbies 20x
    deb "... Está brincando? Depois de ser fodida assim, eu dormi muito bem!"
    show debbies 20w
    player_name "Heh, eu também..."
    deb "..."
    show debbies 20x
    deb "Eu provavelmente deveria sair daqui antes de {b}[jen_name]{/b} levanta-se."
    show debbies 20w
    player_name "Sim..."
    show debbies 20x
    deb "Obrigado por uma grande noite, {b}[firstname]{/b}! Eu te amo!"
    show debbies 20w
    player_name "Eu também te amo, {b}[deb_name]{/b}!"
    scene black with fade
    return

label bedroom_debbie_sleepover_after_not_random:
    scene location_home_bedroom_day_blur
    show player 7
    pause
    show player 8
    pause
    show player 1
    player_name "..."
    show player 2
    player_name "Hmm, {b}[deb_name]{/b} deve ter acordado antes de mim e escapou..."
    player_name "Ufa, que noite! Eu dormi como um bebê..."
    return

label bedroom_debbie_sleepover_after_not_basement_sex:
    show player 10
    player_name "Hmm, o que é essa nota no monitor do meu computador?"
    player_name "...{b}[deb_name]{/b} Deixe eu ver isso?"
    return

label sleeping_locked:
    scene expression player.location.background_blur
    show player 35 at left
    if not erik.over(erik_intro):
        player_name "( Não posso dormir agora. Eu deveria ir para a escola antes que me atrase. )"
    else:
        player_name "(Eu ainda tenho algumas coisas para fazer hoje...)"
    $ game.main()

label tired_bedroom_dialogue:
    scene expression game.timer.image("bedroom{}")
    show player 55 with dissolve
    player_name "{b}*Uaaaaaa....*{/b}"
    show player 56
    player_name "( Estou muito cansado para isso... )"
    hide player 56
    $ game.main()

label M6_note:
    call expression game.dialog_select("M6_note_dialogue")
    $ M_mom.trigger(T_mom_read_note)
    $ game.main()

label M6_note_dialogue:
    scene expression game.timer.image("bedroom{}")
    show debbienote at Position (ypos=650) with dissolve
    pause
    hide debbienote with dissolve
    show player 11 with dissolve
    player_name "( {b}[deb_name]{/b} precisa de ajuda com a roupa? )"
    player_name "( Eu deveria ir ver o que é. )"
    hide player with dissolve
    return

label pet_cat:
    scene expression game.timer.image("bedroom{}")
    show cat 14 with dissolve
    player_name "Olá, [cat]!"
    show cat 12
    if randomizer() < 33:
        cat "Miau"
    elif randomizer() < 66:
        cat "Prrrr"
    else:
        cat "Brrrep"
    show cat 15 at Position(xoffset = -7)
    pause
    show cat 14
    if randomizer() < 15:
        player_name "Quem é uma boa gatinha?!"
    elif randomizer() < 30:
        player_name "Você só vai dormir o dia todo?"
    elif randomizer() < 45:
        player_name "O que você fez hoje, hein?"
    elif randomizer() < 60:
        player_name "Sua fofinha fofinha."
    elif randomizer() < 75:
        player_name "Aww, aconchega-se para gatinha!"
    elif randomizer() < 85:
        player_name "Ei, observe com essas garras!"
    elif randomizer() < 93:
        player_name "Eu deveria te dar um brinquedo, huh?"
    else:
        player_name "Eu adoro acariciar sua bucetinha..."
    show cat 16
    pause
    hide cat with dissolve
    $ game.main()

label cookies:
    scene expression game.timer.image("bedroom{}")
    show expression "objects/closeup_cookies.png" at left with dissolve
    player_name "( Uma caixa dos meus cookies favoritos! )"
    player_name "( Eu deveria mantê-los na minha mochila para o caso de ficar com fome. )"
    hide expression "objects/closeup_cookies.png" with dissolve
    show expression "boxes/popup_cookies.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_cookies.png" with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
