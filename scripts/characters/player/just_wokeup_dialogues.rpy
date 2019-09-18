label player_jenny_sleepover_mcbedroom:
    scene expression "backgrounds/location_home_bedroom_cutscene19.jpg" with fade
    pause
    scene expression "backgrounds/location_home_bedroom_cutscene20.jpg" with dissolve
    player_name "!!!"
    scene expression "backgrounds/location_home_bedroom_cutscene21.jpg" with dissolve
    player_name "Você está indo?"
    if M_jenny.get("jenny_girlfriend_first_time"):
        $ M_jenny.set('jenny_girlfriend_first_time', False)
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg" with dissolve
        jen "Sim, o sol acabou, o que significa que seu tempo acabou."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Oh."
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "Além disso, {b}[deb_name]{/b} Estarei acordado em breve e não quero que ela me encontre aqui."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Você dormiu bem?"
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "Eu fiz, na verdade."
        jen "Apesar do seu ronco alto e louco."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "O que?!"
        player_name "Eu não ronco!"
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "Heh, seja qual for."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Podemos fazer isso de novo?"
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "Claro, contanto que você esteja pagando."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Mas"
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "Mais tarde, perdedor."
    else:
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg" with dissolve
        jen "Sim, {b}[deb_name]{/b} vai subir em breve."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Ok."
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "Lembre-se de vir por {b}meu quarto{/b} esta tarde para o nosso show."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Tudo bem eu vou."
        scene black with fade
        pause
    return

label player_jenny_sleepover_sisbedroom:
    scene expression player.location.background_blur
    show jenny b_panties a_naked_hips f_upset
    show player b_underwear a_naked_sides f_normal_talk
    player_name "Bom Dia!"
    show player f_normal
    show jenny f_eyeroll
    jen "Sim Sim..."
    show jenny f_upset_talk
    jen "Dá o fora, preciso de um banho."
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Sheesh, é então e assim?"
    player_name "Você não é uma pessoa muito divertida para acordar ao lado..."
    show player f_skeptical
    show jenny f_upset_talk
    jen "Bem, o que você quer que eu faça?!"
    jen "O café da manhã ou algo assim?"
    jen "Seja real."
    show jenny f_upset
    show player f_worried_talk
    player_name "Eu nunca pediria para você fazer isso, {b}[jen_name]{/b}..."
    show player f_laugh
    player_name "... Eu provei sua comida, é horrível."
    show player f_grin
    show jenny f_eyeroll a_naked_crossed with dissolve
    jen "Foda-se"
    show jenny f_upset
    show player f_laugh
    player_name "Hahaah!"
    hide player with dissolve
    show jenny f_gross_talk
    jen "Idiota."
    show jenny f_gross
    return

label bedroom_sis_webcam_show:

    show player 4 with dissolve
    player_name "Hmm..."
    player_name "( eu imagino o que {b}[jen_name]{/b} está fazendo agora. )"
    show player 1
    player_name "( Talvez eu pudesse me conectar a {b}webcam{/b} do meu computador... )"
    hide player with dissolve
    return

label bedroom_bissette_roxxy_jenny_mentoring:
    show player 12 with dissolve
    player_name "{b}Roxxy{/b} deveria se encontrar com {b}[jen_name]{/b} para uma sessão de torcida."
    show player 10
    player_name "{b}Eu deveria ir para casa{/b} ,Ver o que a {b}[jen_name]{/b} estar fazendo."
    hide player with dissolve
    return

label bedroom_dewitt_make_replacement_guitar:
    if game.timer.is_dark():
        show player 14 with dissolve
        player_name "Eu acho que tenho tudo que preciso para fazer minha guitarra falsa."
        show player 4
        player_name "Eu preciso lembrar de montá-lo na garagem amanhã."
        hide player with dissolve
    else:
        show player 14 with dissolve
        player_name "Eu acho que tenho tudo que preciso para fazer minha guitarra falsa."
        player_name "Eu deveria voltar para a minha garagem para que eu possa começar a trabalhar nisso."
        hide player with dissolve
    return

label bedroom_sis_telescope_1:

    show player 4 with dissolve
    player_name "( Eu me pergunto o que {b} Erik {/b} está fazendo agora. )"
    player_name "( Eu devo usar meu {b} telescópio {/b} e ver o que ele está fazendo... )"
    hide player with dissolve
    return

label bedroom_sis_telescope_2:

    show player 4 with dissolve
    player_name "( Gostaria de saber o que {b} Mia {/b} está fazendo agora. )"
    player_name "( Eu devo usar meu {b} telescópio {/b} e ver o que ela está fazendo... )"
    hide player with dissolve
    return

label bedroom_sis_telescope_3:

    show player 4 with dissolve
    player_name "( Eu me pergunto o que {b} a Sra. Johnson {/b} está fazendo agora. )"
    player_name "( Eu devo usar meu {b} telescópio {/b} e ver o que ela está fazendo... )"
    hide player with dissolve
    return

label bedroom_master_somrak_training:

    show player 4 with dissolve
    player_name "( Eu me pergunto se {b} Mestre Somrak {/b} está pronto para me treinar novamente. )"
    hide player with dissolve
    return

label bedroom_roxxy_spin_bottle:
    show player 17 with dissolve
    player_name "{b}Roxxy{/b} e as meninas queriam que eu visitasse a praia esta tarde."
    player_name "Eu deveria ir lá agora!"
    return

label bedroom_roxxy_spin_bottle_no_goldschwagger:
    show player 4 with dissolve
    player_name "( Eu também ainda preciso falar com {b}Capitão Terry{/b} sobre {b}GoldSchwagger{/b} para {b}Becca{/b}. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
