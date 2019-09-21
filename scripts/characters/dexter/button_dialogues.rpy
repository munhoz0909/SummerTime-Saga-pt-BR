label button_dexter_talent_show:
    show dexter 1
    show player 10
    player_name "Hey {b}Dexter{/b}, Você toca algum instrumento?"
    show player 5
    show dexter 2
    dex "Huh?"
    show player 12
    player_name "I-N-S-T-R-U-M-E-N-T-O. Você sabe, como para a música ... Você joga qualquer?"
    show player 5
    show dexter 8
    dex "Pareço algum geek da banda meio que lhe?!"
    show dexter 2
    show player 12
    player_name "Ehh, não? Eu só pensei que talvez você tivesse um talento escondido para bater os tambores ou algo?"
    show player 5
    show dexter 6 with dissolve
    dex "Eu gostaria de bater em seu rosto estúpido com meus punhos ..."
    dex "Você acha que faria alguma música?"
    show dexter 5
    show player 29 with dissolve
    player_name "Heh, eu estava de saída ..."
    show player 3
    show dexter 4 with dissolve
    dex "Sim, é melhor você!"
    return

label button_dexter_challenge:
    show player 12
    player_name "Estou aqui para desafiá-lo, {b}Dexter{/b}."
    show player 5
    show dexter 3
    dex "Ha ha!"
    dex "Para quê?!"
    show dexter 1
    show player 10
    player_name "Para uh..."
    show player 5
    show dexter 3
    dex "Você sabe que eu te bater em qualquer coisa."
    show dexter 4 with dissolve
    dex "Agora cai fora antes de me decidir a bater a merda fora de você."
    return

label button_dexter_library_book:
    show player 10
    player_name "Hey, umm, {b}Dexter{/b}..."
    show player 5
    show dexter 3
    dex "O que você quer imbecil?"
    show dexter 1
    show player 10
    player_name "Você se lembra onde deixou o livro da biblioteca que você check-out..."
    show player 5
    show dexter 8
    dex "Livro da biblioteca?"
    show dexter 4 with dissolve
    dex "Eu não disse que você sair daqui, {b}[firstname]{/b}?"
    dex "Ou você quer um sanduíche da junta!"
    show dexter 2 with dissolve
    show player 12
    player_name "Certo, certo, eu vou!"
    hide dexter with dissolve
    show player 10f at center with dissolve
    player_name "Pergunto-me se o bibliotecário cometeu um erro?"
    show player 5f
    player_name "..."
    show player 12f
    player_name "Ele poderia estar mentindo. {b}I deve verificar seu armário{/b}!"
    player_name "Esperemos que ele está lá, caso contrário eu não sei o que eu vou fazer..."
    return

label button_dexter_nothing:
    show player 10
    player_name "I ... uhh ... não queria incomodá-lo."
    player_name "Eu preciso ir para a aula."
    show player 5
    show dexter 3
    dex "Corra junto, perdedor."
    return

label dexter_button_pushups:
    show player 16 at left
    show dexter 12 at right
    with dissolve
    dex "Oh, você quer uma revanche huh?"
    dex "Não tem problema, nerd!"
    dex "Eu vou te mostrar como se faz!"
    show dexter 11
    scene gym
    show player 16 at left
    show dexter 11 at right
    with dissolve
    bri "Tudo bem, rapazes. Você sabe o que fazer!"
    bri "Último homem de pé vitórias!"
    show dexter 12
    dex "Hahaha,assista e aprenda ... NERD!"
    hide player
    hide dexter
    with dissolve
    bri "VAI!"
    return

label dexter_button_pushups_rematch:
    show player 5 at left
    show dexter 15 at right
    with dissolve
    dex "Como sobre uma revanche, nerd?!"
    show dexter 14
    show player 12
    player_name "O que?! Vamos lá, cara ... Você perdeu."
    player_name "Apenas siga em frente."
    show player 5
    show dexter 12 with dissolve
    dex "Psh, você tem medo você vai perder?"
    show dexter 11
    show player 12
    player_name "Não."
    show player 90
    show dexter 28 with dissolve
    dex "{b}[firstname]'s{/b} uma galinha, todo mundo!"
    show dexter 11 with dissolve
    show player 12
    player_name "... Tch, bem."
    player_name "Vamos fazer isso!"
    hide player
    hide dexter
    with dissolve
    return

label button_dexter_intro_beginning:
    show player 5 at left
    show dexter 3 at right
    with dissolve
    dex "Wchapéu que você está olhando, perdedor?!"
    show dexter 1
    show player 10
    player_name "Nada."
    show player 5
    show dexter 3
    dex "Sim, está certo!"
    dex "Continue andando puta!"
    dex "Hahahaha!"
    hide dexter with dissolve
    show player 12
    player_name "Ugh, ele é um idiota..."
    hide player with dissolve
    return

label button_dexter_intro:
    show player 5 at left
    show dexter 3 at right
    with dissolve
    dex "Eu pensei que eu cheirei uma vadia!"
    show dexter 2
    show player 12
    player_name "parafuso you, {b}Dexter{/b}..."
    show player 90
    show dexter 6 with dissolve
    dex "O QUE que você disse?!"
    show dexter 4 with dissolve
    show player 11
    dex "Você quer que eu bater o seu burro para fora, aqui mesmo,?!"
    show dexter 2 with dissolve
    player_name "..."
    show dexter 3
    dex "Sim, isso é o que eu pensava."
    show dexter 6 with dissolve
    dex "É melhor ficar longe da minha menina!"
    show dexter 2 with dissolve
    show player 5
    player_name "..."
    show dexter 4 with dissolve
    dex "Você me ouve, cadela?!"
    show dexter 2 with dissolve
    return

label button_dexter_intro_final:
    show player 90 at left
    show dexter 2 at right
    with dissolve
    dex "..."
    show player 12
    player_name "Sinto muito, você disse alguma coisa, {b}Dexter{/b}?"
    show player 91
    show dexter 8
    dex "Não!"
    show dexter 2
    show player 12
    player_name "Yeah, isso é o que eu pensava."
    show player 91

    dex "..."
    return

label button_dexter_basketball_final:
    show player 12
    player_name "Ainda jogando basquete?"
    show player 91
    dex "..."
    show player 12
    player_name "Vocês já conseguiu ganhar um jogo?"
    show player 91
    show dexter 8
    dex "Eu não quero falar sobre isso!"
    show dexter 2
    show player 12
    player_name "Eu só estou tentando-"
    show player 11
    show dexter 8
    dex "Me deixe em paz, {b}[firstname]{/b}!"
    hide dexter with dissolve
    pause
    show player 10
    player_name "Sheesh, tudo bem."
    hide player with dissolve
    return

label button_dexter_basketball:
    show player 12
    player_name "Ainda jogar basquete?"
    show player 90
    show dexter 3
    dex "Claro, eu nasci para jogar!"
    show dexter 1
    show player 12
    player_name "Você já ganhou um jogo?"
    show player 90
    show dexter 3
    dex "Psh, Yeah. Como uma centena de milhões ..."
    show dexter 1
    show player 12
    player_name "Okay, certo! Vocês são terríveis ..."
    show player 90
    show dexter 4 with dissolve
    dex "EI! Você quer uma junta sanduíche, perdedor ?!"
    show dexter 2 with dissolve
    player_name "..."
    show dexter 3
    dex "O que faz uma pequena cadela como você sabe sobre basquete de qualquer maneira?!"
    dex "É um esporte de homem!"
    show dexter 1
    show player 17
    player_name "Oh, bem, então, não é de admirar por isso que as senhoras não podem ganhar um jogo."
    show player 13
    show dexter 3
    dex "Hã? Eu não-"
    dex "Oh, você acha que é engraçado?!"
    show dexter 8
    dex "Que tal se eu bater alguns dos seus dentes?!"
    show player 5
    dex "Isso seria muito engraçado, não é ?!"
    show dexter 2
    return

label button_dexter_whatever:
    show player 12
    player_name "Tch, Yeah. Seja como for, o homem..."
    hide player with dissolve
    pause
    show dexter 8
    dex "Hey, eu não estou brincando {b}[firstname]{/b}!"
    dex "Fique longe de, {b}Roxxy{/b}!"
    dex "Ela é minha!"
    hide dexter
    hide player
    with dissolve
    return

label button_dexter_behaving:
    show player 12
    player_name "Eu confio em você está se comportando-se."
    show player 90
    show dexter 8
    dex "... sim."
    show dexter 2
    show player 12
    player_name "Você se lembra o que acontece, se eu te pego brincando com meus amigos de novo, certo?"
    show player 92
    player_name "Você precisa de um lembrete?!"
    show player 91
    show dexter 8
    dex "NÃO!"
    dex "Eu lembro..."
    show dexter 2
    show player 92
    player_name "Boa."
    show player 91
    return

label button_dexter_run_along:
    show player 12
    player_name "Corra ao longo agora, {b}Dexter{/b}."
    show player 91
    dex "..."
    show dexter 8
    dex "GRRRR!!!"
    hide dexter with dissolve
    pause
    show player 17
    player_name "Hahaha!"
    player_name "Eu gosto do novo {b}Dexter{/b}!"
    hide player with dissolve
    return
# TRADUZIDO
