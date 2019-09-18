label second_floor_first_visit:
    scene expression player.location.background_blur with None
    show player 13 at left
    show kevin 2 at right
    with dissolve
    kev "Ah, {b}[firstname]{/b}?!"
    kev "Quando é que voltaste?"
    show kevin 1
    show player 14
    player_name "Ei, {b}Kevin{/b}."
    player_name "Hoje é meu primeiro dia."
    show player 13
    show kevin 2
    kev "Bem, mano."
    show kevin 2c with dissolve
    kev "Bom te ver!"
    show player 19 with dissolve
    pause
    show player 3
    show kevin 2d
    with dissolve
    kev "Sinto muito pelo {b}seu pai{/b} a propósito..."
    show kevin 2e
    show player 10 with dissolve
    player_name "Sim, obrigado."
    show player 5
    pause
    show player 14
    player_name "O que há com o avental?"
    show player 13
    show kevin 2 with dissolve
    kev "Ugh, {b}Sra. Smith{/b} me colocou em serviço de cafeteria até eu aumentar minha nota com  a classe da {b}Miss Okita{/b} ..."
    show kevin 1
    show player 10
    player_name "Você está ruim em ciência?"
    show player 13
    show kevin 2
    kev "Bem, eu não estou ruim ainda, mas definitivamente não está parecendo bom, mano."
    show kevin 1
    show player 14
    player_name "Isso é uma merda cara."
    show player 13
    show kevin 2
    kev "Conte-me sobre isso!"
    kev "Eu não tenho um bom treino há semanas!"
    show kevin 1
    show player 14
    player_name "Oh, sim?"
    player_name "Ainda andando por aquela academia?"
    show player 13
    show kevin 2
    kev "Você sabe, mano!"
    show kevin 2b with dissolve
    kev "Não posso deixar essas armas sem polimento, posso?"
    show player 14
    player_name "Hehe, não, acho que não..."
    show player 13
    show kevin 2 with dissolve
    kev "Oh, Isto me lembra!"
    kev "Temos esse novo {b}Muay Thai{/b} treinador lá."
    kev "O nome dele é {b}Master Somrak{/b}."
    kev "Ele é como um grande mestre ou algo com todos os seus ensinamentos antigos..."
    kev "É muito legal!"
    show kevin 1
    show player 14
    player_name "{b}Muay Thai{/b}?"
    show player 13
    show kevin 2
    kev "Sim, mano!"
    kev "Você sabe, tipo, {b}kickboxing{/b} e outras coisas."
    show kevin 1
    show player 14
    player_name "Mesmo?"
    show player 13
    show kevin 2
    kev "Você deveria ir lá e dar uma olhada!"
    show kevin 1
    show player 29 with dissolve
    player_name "Oh, Não sei..."
    show player 3
    show kevin 2
    kev "Vamos lá mano!"
    kev "Você tem que ter esse corpo em forma."
    kev "As pessoas exigem bolo de carne, não bolo de doce!"
    show kevin 1
    show player 10 with dissolve
    player_name "Eh?"
    player_name "Eu acho que eu poderia dar uma olhada..."
    show player 13
    show kevin 2
    kev "Esse é o espírito, mano!"
    kev "Quem sabe, você pode até chutar a bunda de {b}Dexter{/b} depois de ter algumas aulas em seu currículo."
    show kevin 1
    show player 14
    player_name "Ok, certo."
    show player 13
    pause
    show player 14
    player_name "Eu deveria ir, cara."
    player_name "{b}Sra. Smith{/b} está me esperando lá em cima {b}no escritório dela{/b}."
    show player 13
    show kevin 2
    kev "Oh merda, mano ... eu não sabia disso!"
    kev "É melhor você se apressar antes de acabar na lanchonete comigo."
    show kevin 1
    show player 36 with dissolve
    player_name "Até mais, {b}Kevin{/b}."
    show player 13 with dissolve
    show kevin 2
    kev "Visitar a {b}cafeteria{/b} mais tarde e podemos conversar."
    show kevin 1
    show player 14
    player_name "Tudo bem."
    hide player
    hide kevin
    with dissolve
    return

label second_floor_okita_dose_smith:
    scene expression game.timer.image("backgrounds/location_school_second{}_blur.jpg")
    show player 35
    player_name "Hmm, eu acho que a {b}Diretora Smith{/b} entra no {b}Salão dos professores{/b} para {b}beber café{/b} nas tardes."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
