label bissette_book_search_2_books_left:
    show player 12 with dissolve
    player_name "Bem, mais dois livros pela frente."
    hide player with dissolve
    return

label bissette_book_search_1_book_left:
    show player 14 with dissolve
    player_name "Apenas um livro restante."
    hide player with dissolve
    return

label bissette_book_search_no_books_left:
    show player 14 with dissolve
    player_name "Ótimo! Esse é o último livro!"
    player_name "Agora só preciso devolvê-los à biblioteca!"
    hide player with dissolve
    return

label annie_locker_first_visit:
    player_name "Sim. Eu esperava tanto."
    player_name "{b}Annie{/b} é uma merda até {b}Diretora Smith{/b}."
    return

label dexter_locker_first_visit:
    player_name "É melhor não deixar {b}Dexter{/b} me ver aqui."
    player_name "Coisas típicas do atleta."
    player_name "Que bomba de ar de basquete estranha."
    return

label dexter_locker_book_search:
    player_name "Ele estava mentindo! Eu sabia!"
    return

label dexter_locker_book_found:
    scene dexter_locker
    show book_05_c with dissolve
    player_name "{b}Quick mafs{/b}?"
    player_name "Este é um livro para crianças pequenas..."
    player_name "Haha, eu acho que combina com seus punhos-"
    player_name "Nível de matemática!"
    player_name "Eu preciso sair daqui!"
    player_name "Algo sobre estar ao lado de {b}Dexter{/b} ou as coisas dele estão me deixando mais burro!"
    hide book_05_c with dissolve
    show expression game.timer.image("location_school_right_hall_day{}_blur")
    return

label erik_locker_first_visit:
    player_name "{b}Erik{/b} tem um monte de {b}Dungeon 'N Orcettes{/b} coisa."
    player_name "Também tem a lancheira dele."
    player_name "Sua landlady sempre leva um pouco de chocolate caseiro."
    player_name "Cara sortudo. Sua landlady com certeza deve gostar muito dele."
    return

label eve_locker_first_visit:
    player_name "Caramba! É melhor não deixar mais ninguém ver seu armário."
    player_name "Esses fones de ouvido com certeza parecem confortáveis."
    return

label eve_locker_drawing_pick_up:
    $ player.get_item("eve_drawing")
    call expression game.dialog_select("eve_locker_drawing_picked_up")
    $ player.location.call_screen(False)

label eve_locker_drawing_picked_up:
    scene eve_locker
    show closeup_drawing_01
    with dissolve
    player_name "Huh, isso é realmente bom!"
    player_name "... {b}Chad{/b} estava certo. É bem sexy!"
    player_name "Será que ela realmente pensa em usar algo assim??"
    show expression "boxes/popup_item_drawing1.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_item_drawing1.png"
    hide closeup_drawing_01
    with dissolve
    return

label judith_locker_first_visit:
    player_name "Mmm... {b}Jizz da montanha{/b}."
    player_name "Essas coisas podem certamente fazer uma bagunça."
    player_name "Deve ser todo o açúcar que o torna tão pegajoso."
    pause
    player_name "Ela deve gostar de vacas."
    player_name "eu também"
    player_name "Ei! Como ela conseguiu essa foto minha?"
    return

label take_judith_glasses:
    scene judith_locker
    player_name "Esse deve ser o seu conjunto de reposição."
    show expression "boxes/popup_item_glasses1.png" at truecenter with dissolve
    $ player.get_item("judith_glasses")
    pause
    player_name "Agora só preciso devolvê-los para Okita."
    pause
    $ game.main()

label take_broken_flute:
    scene judith_locker
    player_name "( Essa deveria ser a {b}flauta{/b} Judith pediu emprestada a Miss Dewitt. )"
    scene lefthall_c with fade
    $ player.get_item("broken_flute")
    call expression game.dialog_select("take_broken_flute_dialogue")
    $ M_dewitt.trigger(T_dewitt_get_flute)
    $ game.main()

label take_broken_flute_dialogue:
    show player 563f at left with dissolve
    player_name "Uau, essa coisa realmente foi achatada..."
    player_name "Está tuda dobrada!"
    show player 564f with dissolve
    pause
    show player 565f with dissolve
    player_name "Hmm, cheira engraçado também."
    show player 564f with dissolve
    show erik 5 at right with dissolve
    eri "Uhh, o que você está fazendo aí, cara?"
    show erik 52
    show player 22f at Position (xoffset=139) with hpunch
    player_name "!!!"
    show player 29 with dissolve
    player_name "Nada! Você me assustou!"
    show player 14 with dissolve
    player_name "O que você está fazendo?"
    show player 13
    show erik 5
    eri "Apenas indo para a minha próxima aula..."
    show erik 53
    eri "Isso era uma flauta?"
    show player 563
    show erik 3c
    with dissolve
    player_name "Sim. Bem, costumava ser de qualquer maneira."
    show player 562
    show erik 53
    eri "Definitivamente viu dias melhores..."
    show erik 3c
    show player 563
    player_name "Eu ia tocar para {b}Ms. Dewitt's{/b} no show de talentos."
    show player 13 with dissolve
    show erik 5
    eri "Hmm, bem, talvez você possa construir uma nova flauta?"
    show erik 52
    show player 10
    player_name "Você acha?"
    show player 5
    show erik 54
    eri "Concerteza!"
    show erik 4
    eri "Eu tive que construir uma flauta em um videogame uma vez."
    eri "Tudo o que você precisa é de um bom pedaço de madeira e uma broca para fazer todos os buracos."
    show erik 1
    show player 12
    player_name "Você construiu um em um videogame?"
    show player 5
    show erik 4
    eri "Totalmente! Eu usei para encantar todas as meninas orcs da vila!"
    eri "Então tivemos uma orgia gigante na cabana do chefe!"
    show erik 1
    show player 10
    player_name "Oh, isso é bom."
    show player 5
    show erik 4
    eri "Hehe, cara, era tudo menos legal. Posso assegurar-vos!"
    show player 13
    show erik 54
    eri "Pintos verdes são loucos no saco!"
    show erik 1
    show player 14
    player_name "Eu provavelmente deveria estar ocupado se eu vou construir uma flauta do zero."
    show player 13
    show erik 4
    eri "AH, certo. eu te vejo depois."
    show erik 1
    show player 14
    player_name "Obrigado, {b}Erik{/b}."
    show player 13
    show erik 4
    eri "Sem problemas, cara!"
    hide player
    hide erik
    with dissolve
    return

label kevin_locker_first_visit:
    player_name "Hã?"
    player_name "Parece a minha cinta esportiva perdida!"
    pause
    player_name "Eu não sabia que compramos o mesmo."
    return

label mia_locker_first_visit:
    player_name "O Armário da {b}Mia{/b} tem um cheiro bom."
    return

label mia_locker_first_visit_early_route:
    player_name "Ela tem uma vida tão boa."
    return

label mia_locker_first_visit_helping_parents:
    player_name "Eu deveria ajudar os pais dela a voltarem."
    return

label mia_locker_first_visit_helen_route:
    player_name "Eu me pergunto se eu deveria ter ajudado os pais dela a voltarem...."
    return

label ronda_locker_first_visit:
    player_name "Existe algum esporte em que ela não seja boa?"
    player_name "Aposto que ela nem precisa pagar pela faculdade."
    player_name "Ela provavelmente tem uma bolsa integral."
    return

label roxxy_locker_first_visit:
    player_name "Uau."
    player_name "{b}Roxxy{/b} armário é bom."
    player_name "Parece que ela abriu o selo em um novo pote de {b}Cherry Pops{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
