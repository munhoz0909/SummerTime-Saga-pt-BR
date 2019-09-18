label science_classroom_first_visit:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    with dissolve
    player_name "Ei, {b}Miss Okita{/b}."
    show player 1
    show okita 3
    okita "Aí está você, {b}[firstname]{/b}. Você tem alguma idéia de quanto você estar atrasado na minha classe?!"
    show player 5
    okita "Suas notas são as mais baixas possíveis. Espero que você tenha uma boa desculpa!"
    show player 10
    show okita 4
    player_name "Sim, meu uh ... Meu pai morreu."
    show player 5
    show okita 3
    okita "... Oh."
    show okita 5
    okita "Estou envergonhada. Desculpe, por ouvir isso {b}[firstname]{/b}."
    show player 10
    show okita 4
    player_name "Ninguém te contou?"
    show player 5
    show okita 9
    okita "Você não espera que eu ouça todas as fofocas que esses simplórios trazem pela minha porta, não é?"
    show okita 4
    player_name "..."
    show okita 5
    okita "Eu juro meu QI. caiu vinte pontos desde que aceitei este trabalho estúpido..."
    show okita 11
    okita "... Imbecis Contech."
    show player 10
    show okita 4
    player_name "Cuntech?"
    show player 5
    show okita 5
    okita "deixa pra lá."
    show player 10
    show okita 4
    player_name "... Ok, bem, eu estava esperando que você tivesse um jeito de eu recuperar minhas notas."
    player_name "Crédito extra ou algo assim?"
    show player 5
    show okita 2
    okita "Crédito extra?"
    show okita 2b
    okita "... Não, eu não faço crédito extra."
    show player 10
    show okita 1
    player_name "A sério? Não há nada que eu possa fazer?"
    player_name "Existe algo em que eu possa ajudá-la?"
    show player 5
    show okita 10
    okita "Hmm..."
    show okita 2
    okita "... Eu duvido. Você conhece a abiogênese?"
    show player 10
    show okita 1
    player_name "Abio QUE?"
    show player 11
    show okita 8
    okita "..."
    show okita 2
    okita "Você já fez algum trabalho com Neutrinos?"
    show player 10
    show okita 1
    player_name "Que diabos são os Neutrinos?"
    show player 11
    show okita 7
    okita "Oh, Eu não sei!"
    okita "Eu tenho um experimento complicado envolvendo Monopólos Magnéticos. Talvez você possa me ajudar com isso, né?"
    show player 10
    show okita 6
    player_name "Você está falando inglês agora?"
    show player 11
    show okita 7
    okita "Hehe, bem me desculpe, {b}[firstname]{/b}. Eu diria que você está preso a outro objeto por um plano inclinado, enrolado helicoidalmente em torno de um eixo."
    show player 34
    show okita 6
    player_name "..."
    show player 35
    player_name "Hã?"
    show player 11
    show okita 2b
    okita "Você está ferrado..."
    show player 12
    show okita 1
    player_name "Ugh, isso é uma merda!"
    show player 5
    show okita 5
    okita "Mmm hmm. Vou te dizer o que..."
    okita "Acabamos de dar uma olhada nos processos reprodutivos dos dípteros comuns."
    show player 10
    show okita 4
    player_name "... Diptera?"
    show player 11
    show okita 3
    okita "Mosca doméstica."
    show player 10
    show okita 4
    player_name "Ohh."
    show player 5
    show okita 5
    okita "E hoje estamos começando nossa introdução à química básica."
    okita "Então, por que você não começa com isso e eu tentarei criar uma maneira de você obter uma nota de aprovação antes do final do semestre."
    show player 11
    show okita 3
    okita "Isso soa aceitável?"
    show player 10
    show okita 4
    player_name "Sim, acho que é tudo o que posso esperar neste momento."
    show player 1
    show okita 7
    okita "Agora, isso pode ser a coisa mais inteligente que um aluno já disse nessa sala de aula!"
    show player 5
    show okita 4
    player_name "..."
    show okita 5
    okita "Vá começar, {b}[firstname]{/b}."
    show okita 3
    okita "... E por favor siga as instruções do livro didático."
    show player 10
    show okita 4
    player_name "*Suspiro*"
    player_name "Sim, senhora."
    return

label science_classroom_cutscene:
    scene location_school_science_cutscene01
    with fade
    show text "Hmm, Eu quero saber porque {b}Miss Okita{/b} é sempre tão mal-humorada?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Ela parecia bastante inflexível quanto ao crédito extra." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene location_school_science_cutscene02
    with fade
    show text "Aposto que posso mudar de idéia!\nEu só preciso provar que não sou tão estúpido quanto ela me percebe..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Isso não deve ser muito difícil!\nIsso é apenas química básica e eu sou bastante inteligente, afinal..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... O que poderia dar errado?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene location_school_science_cutscene03
    with fade
    show text "( !!! )" at Position (xpos= 512, ypos= 700) with hpunch
    with dissolve
    pause
    hide text
    with dissolve
    return

label science_classroom_after_cutscene:
    scene location_school_science_closeup
    show player 428 zorder 4 at Position(xpos=0.35, ypos=1.0)
    show playerb 1 zorder 5 at Position(xpos=0.35, ypos=0.765)
    with dissolve
    pause
    show player 108f
    player_name "... Opa."

    show player 5
    show mia 43f zorder 6 at Position(xpos=0.65, ypos=1.0)
    show mial 1f zorder 7 at Position (xoffset=162)
    with dissolve
    mia "Oh minha nossa, {b}[firstname]{/b}!"
    show mia 8
    show erik 53f zorder 0 at Position(xpos=0.15, ypos=1.0)
    show erikl 1 zorder 1 at Position(xpos=0.14, ypos=1.0)
    with dissolve
    eri "Caramba, cara! Você está certo?"
    show erik 51f
    show player 10
    player_name "Eu ... Sim, acho que sim..."
    show player 5
    pause

    show okita 11 zorder 8 at Position(xpos=0.8, ypos=1.0) with dissolve
    okita "A sério, {b}[firstname]{/b}!?!"
    hide mia
    hide mial
    with dissolve
    show erik 53f
    show player 23
    show mia 43 zorder 2 at Position(xpos=0.5, ypos=1.0)
    show mial 1 zorder 3 at Position(xpos=0.51, ypos=1.0)
    with dissolve
    okita "Quão difícil é seguir as instruções de um livro de química escrito para crianças!?"
    show player 22
    show okita 11b
    player_name "..."
    show okita 11
    okita "Você poderia ter queimado a escola inteira!"
    show player 10
    show okita 11b
    player_name "Eu sinto Muito, {b}Miss Okita{/b}. Eu não"
    player_name "... Não sei o que aconteceu!"
    show player 5
    show okita 11
    okita "Você não sabe o que aconteceu?!"
    show okita 11b
    pause
    show okita 11
    okita "Eu vou te contar o que aconteceu!"
    okita "Você perdeu seus privilégios! Foi o que aconteceu!!!"
    show player 24
    show okita 11b
    player_name "Oh, cara..."
    show player 25
    show okita 11
    okita "Eu juro, eu não posso tirar meus olhos de vocês macacos por um instante..."
    okita "O fato de você poder se vestir de manhã desafia toda lógica!"
    show player 24
    show okita 11b
    player_name "Ugh, pelo menos eu já estou falhando. Nada me resta a perder, realmente."
    show player 5
    show okita 11
    okita "Oh, sempre há algo que eu poderia"
    show okita 8
    okita "..."
    show okita 9
    okita "Hã."

    hide okita
    with dissolve
    show okita 10cf zorder 8 at Position(xpos=0.85, ypos=1.0)
    okita "Ele não tem nada a perder..."
    show okita 10bf
    show mia 8f
    pause
    show okita 10cf
    okita "... e ele está desesperado."
    show player 10
    show okita 10bf
    player_name "Uhh, {b}Miss Okita{/b}?"
    show player 5
    okita "..."
    show okita 10cf
    okita "Ele é teimoso também."
    okita "... e engenhoso."
    show okita 10bf
    player_name "..."
    show okita 10cf
    okita "Sim, isso pode funcionar bem."
    show okita 10bf
    show erik 51f
    show mia 43
    mia "Umm, Senhora? Você sabe que podemos ouvi-lo, certo?"
    show mia 8bf
    hide okita with dissolve
    show okita 8 zorder 8 at Position(xpos=0.8, ypos=1.0) with dissolve

    okita "Hmm?"
    show okita 3
    okita "Oh, sim Sim!"
    show okita 11
    okita "Vocês, crianças, voltam ao trabalho."
    okita "[firstname], você acabou de assistir {b}Mia{/b} e {b}Erik{/b} para hoje."
    okita "Eu não quero que você sopre mais nada."
    show okita 11b
    show player 10
    player_name "... sim, senhora."
    show player 5
    show okita 11
    okita "... E venha me ver depois que a aula terminar."
    okita "Eu só posso ter uma maneira de você aumentar suas notas depois de tudo."
    hide okita with dissolve
    show okita 4f at Position(xpos=0.85, ypos=1.0) with dissolve
    pause
    hide okita with dissolve

    player_name "..."
    hide mia
    hide mial
    with dissolve
    show mia 8 zorder 6 at Position(xpos=0.65, ypos=1.0)
    show mial 1f zorder 7 at Position (xoffset=162)
    with dissolve
    show erik 53f
    eri "Isso soou meio sinistro..."
    show erik 51f
    show mia 43f
    mia "Sim, realmente."
    show erik 53f
    show mia 8
    eri "Aquela mulher assusta a porcaria de mim."
    show erik 51f
    show player 10
    player_name "Bem, não pode ser pior do que falhar..."
    show player 5
    show erik 53f
    eri "Não sei cara..."
    show erik 51f
    show mia 43f
    mia "Eu espero que você esteja certo."
    show mia 8
    show player 24
    player_name "..."

    return

label science_classroom_mia_return_favor:
    scene school_science_c02
    show player 13 at left
    show mia 10 at right
    show mial 1f at right
    with dissolve
    mia "{b}[firstname]{/b}!"
    show mia 7
    show player 14
    player_name "Ei, {b}Mia{/b}."
    show player 12
    player_name "Como está sua perna?"
    show player 13
    show mia 9
    mia "Oh, está tudo bem ... Só um pouco dolorida, ha ha."
    show mia 10
    mia "Já está bem melhor e tirei o curativo!"
    show mia 7
    show player 17
    player_name "Legal! Como se parece?"
    show player 13
    show mia 10
    mia "Eu queria te mostrar, na verdade ... E te agradecer por me ajudar."
    show mia 7
    show player 10
    player_name "Aqui?"
    show player 11
    show mia 9
    mia "Não aqui, bobo!"
    show mia 7
    show player 17
    player_name "Ha ha."
    show player 13
    show mia 10
    mia "{b}Venha para o meu quarto esta noite{/b} e eu vou te mostrar."
    show mia 7
    show player 14
    player_name "Ok, eu vou passar lá!"
    show player 13
    show mia 10
    mia "Ótimo! Vejo você então!"
    hide player
    hide mia
    hide mial
    with dissolve
    return

label science_classroom_okita_has_items:
    scene location_school_science_closeup02
    show xtra 36 zorder 6
    show mial 8 zorder 5 at Position (xpos=0.7225, ypos=1.055)
    show okita 94 zorder 3 at Position(xpos=0.45, ypos=1.0)
    show okitag 1f zorder 4 at Position(xpos=0.5, ypos=0.385)
    with dissolve
    mia "Tudo bem, então eu acabei de adicionar o peróxido de hidrogênio..."
    show mial 5

    okita "Mmmhmm..."
    show player 14 zorder 0 at Position(xpos=0.15, ypos=1.0)
    show playerl 1 zorder 1 at Position(xpos=0.1475, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.165, ypos=0.35)
    with dissolve
    player_name "Ei, {b}Miss Okita{/b}, Eu tenho "
    show player 10
    player_name "... Oh."
    show okita 3
    show okitag 1 at Position(xpos=0.4, ypos=0.385)
    with dissolve
    show player 11
    show mial 7
    okita "[firstname]! Já era hora de você aparecer!"
    show player 10
    show okita 4
    player_name "... Desculpa?"
    show player 11
    show mial 8
    mia "Oi, {b}[firstname]{/b}!"
    show player 2
    show mial 7
    player_name "Oi {b}Mia{/b}!"
    player_name "{b}Miss Okita{/b}, Eu tenho"
    show player 11
    show okita 9
    okita "Sim Sim! Eu estou bem ciente."
    show okita 5
    okita "Eu estava ajudando a {b}Mia{/b} aqui com a química dela. Por que você não vem se juntar a nós?"
    show player 10
    show okita 4
    player_name "Eu pensei que não era permitido tocar no equipamento de química?"
    show player 11
    show okita 5
    okita "Oh, você definitivamente não tem permissão para tocar, apenas observe..."
    show okita 4
    show mial 8
    mia "Vamos {b}[firstname]{/b}. Eu vou te mostrar como se faz!"
    show player 2
    show mial 7
    player_name "Sim, ok!"
    show player 110f at Position(xpos=0.25, ypos=1.0)
    show playerl 1 at Position(xpos=0.2475, ypos=1.0)
    show playerg 1 at Position(xpos=0.265, ypos=0.35)
    show okita 94 at Position(xpos=0.45, ypos=1.0)
    show okitag 1f at Position(xpos=0.5, ypos=0.385)
    with dissolve
    show mial 5
    pause
    show mial 6
    mia "Agora onde eu estava?"
    show mial 5
    okita "..."
    show mial 3 at Position (xpos=0.71, ypos=1.055)
    mia "Hmm, Acho que devo adicionar um pouco de fermento em seguida."
    show mial 4 at Position (xpos=0.695, ypos=1.055)
    okita "..."
    show okita 95
    okita "... Espere um segundo."
    show mial 5 at Position (xpos=0.7225, ypos=1.055)
    hide okita
    hide okitag
    show okita 98 zorder 3 at Position(xpos=0.475, ypos=1.015) with dissolve
    okita "O que você acabou de adicionar!?"
    show player 109f
    show okita 97
    show mial 6
    mia "Uhh..."
    show okita 98
    okita "Você acabou de adicionar fermento a isso?"
    show player 108f
    show okita 97
    show mial 6
    show okitagf 2 zorder 7 at Position(xpos=0.6025, ypos=0.835)
    okita "..."
    show okita 98b
    show okitagf 3 at Position(xpos=0.6, ypos=0.835)
    okita "( !!! )" with hpunch
    show player 23
    show mial 9 with dissolve
    pause
    show okitagf 2 zorder 7 at Position(xpos=0.6025, ypos=0.835)
    show okita 98c with dissolve
    pause
    hide okitagf
    pause



    scene location_school_science_closeup
    show okita 11 zorder 3 at Position(xpos=0.75, ypos=1.0)
    show okitagf 1 zorder 4 at Position(xpos=0.725, ypos=0.68)
    show mia 45 zorder 5 at Position(xpos=0.35, ypos=1.0)
    show mial 1 zorder 6 at Position(xpos=0.3625, ypos=1.0)
    show player 11 zorder 0 at Position(xpos=0.15, ypos=1.0)
    show playerl 1 zorder 1 at Position(xpos=0.1475, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.165, ypos=0.35)
    with dissolve
    okita "Inacreditável!"
    okita "Estou completamente encharcada!"
    show okita 11b
    mia "..."
    player_name "..."
    show okita 11
    okita "A incompetência nesta escola é surpreendente!"
    okita "Ninguém pode fazer nada certo!?"
    show okita 11b
    show mia 46
    mia "Me desculpe, senhora."
    mia "Eu devo ter olhado a página errada..."
    show mia 45
    show okita 11
    okita "Eu não quero ouvir suas desculpas!"
    hide okita
    hide okitagf
    show okita 19 zorder 3 at Position(xpos=0.76, ypos=1.0)
    with dissolve
    show player 23
    player_name "( !!! )" with hpunch
    pause
    show okitagf 4 zorder 4 at Position(xpos=0.7175, ypos=0.42)
    show okita 21 at Position(xpos=0.75, ypos=1.0)
    with dissolve
    okita "Você tem sorte que eu guardo uma muda de roupa aqui na escola."
    show player 11
    show okita 20
    mia "..."
    player_name "..."


    show okita 21
    okita "Estou toda pegajosa!"

    okita "Repugnante..."
    okita "Eu preciso de um banho!"
    show okita 20
    show mia 43
    mia "Desculpe, {b}Miss Okita{/b}. Eu não quis..."
    show mia 45
    show player 10
    player_name "Está tudo bem, {b}Mia{/b}. Não"
    show player 11
    show okita 21
    okita "Não está bem! Eu vou estar deduzindo pontos da sua nota para isso, {b}Mia{/b}!"
    show okita 20
    show mia 46
    mia "Sim, senhora."
    show okita 21
    okita "Agora pegue sua bunda em casa!"
    hide mia
    hide mial
    with dissolve
    okita "{b}[firstname]{/b}!!!"
    show player 10 at Position(xpos=0.35, ypos=1.0)
    show playerl at Position(xpos=0.3475, ypos=1.0)
    show playerg at Position(xpos=0.365, ypos=0.35)
    with dissolve
    show okita 20
    player_name "Sim, senhora?"
    show player 11
    show okita 21
    okita "Volte e me veja amanhã."
    okita "Quero começar nosso trabalho imediatamente."
    show player 10
    show okita 20
    player_name "Sim, senhora."
    $ game.timer.tick(2)
    return

label science_classroom_okita_has_glasses:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    with dissolve
    player_name "{b}Miss Okita{/b}, Eu tenho eles!"
    player_name "Eu tenho as lentes que você queria!"
    show player 1
    show okita 3
    okita "Deixe-me ver!"

    show okita 16 with dissolve
    okita "Sim, estes devem servir."
    show okita 14
    okita "Tudo bem, venha aqui e comece a montar."
    show player 10
    show okita 15
    player_name "Uau, você quer que eu os construa?"
    show player 11
    show okita 9 with dissolve
    okita "Obviamente."
    show player 10
    show okita 4
    player_name "But I can't do that!"
    show player 11
    show okita 5
    okita "Por que não?"
    show player 10
    show okita 4
    player_name "Eu pensei que estes eram importantes? Você deveria fazê-lo."
    show player 11
    show okita 5
    okita "Não, isso é trabalho de macaco."
    show okita 9
    okita "{b}Tori Okita{/b} não faz trabalho de macaco..."
    show okita 4
    player_name "..."
    show player 10
    player_name "E se eu estragar alguma coisa?"
    show okita 5
    okita "As instruções estão ali!"
    show okita 3
    okita "Você pode seguir instruções simples?!"
    show player 11
    show okita 4
    player_name "... Sim."
    show player 10
    show okita 5
    okita "Bem, então mostre alguma espinha dorsal e comece a trabalhar."
    show player 16
    show okita 4
    player_name "..."
    show player 12
    player_name "Está bem."

    return

label science_classroom_okita_has_glasses_try_again:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    player_name "Tudo bem, {b}Miss Okita{/b}. Eu acho que vou fazer melhor desta vez."
    show player 1
    show okita 9
    okita "Você não poderia fazer pior."
    show player 16
    show okita 4
    player_name "..."
    show player 12
    player_name "Vou conseguir desta vez, eu sei!"

    show player 16
    show okita 5
    okita "Bem, terá que esperar até depois da aula. Vá tomar o seu lugar, {b}[firstname]{/b}."

    show player 2
    show okita 4
    player_name "Estou pronto, vamos fazer isso!"
    show player 1
    show okita 5
    okita "Por todos os meios."
    return

label science_classroom_okita_has_glasses_int_pass:
    $ persistent.cookie_jar["Okita"]["unlocked"] = True
    $ persistent.cookie_jar["Okita"]["gallery"]["01_unlocked"] = True
    scene location_school_science_cutscene05
    with fade
    show text "Então eu comecei a trabalhar." at Position(xpos=512, ypos=700) with dissolve
    pause
    hide text
    with dissolve
    scene location_school_science_closeup02
    show xtra 36 zorder 4
    show player 538f zorder 0 at right
    show okita 1f zorder 3 at Position(xpos=0.4, ypos=1.0)
    with dissolve
    player_name "Tudo bem!"

    show player 540f with dissolve
    player_name "Um par de oculares Okitatron, pronto para teste!"
    show player 540bf
    show okita 3f
    okita "Hmm, você verificou o selo na carcaça?"
    show player 538f with dissolve
    show okita 1f
    player_name "Oh, certo! Ok, um segundo."
    show player 538bf
    show okita 4f
    okita "..."
    show kevin 8f zorder 1 at Position(xpos=0.15, ypos=1.0)
    show kevinl 1 zorder 2 at Position(xpos=0.15, ypos=1.0)
    with dissolve
    pause
    show kevin 9f
    kev "Com licença, {b}Miss Okita{/b}?"
    show kevin 8f
    show okita 5f
    okita "E verifique se a unidade de energia está carregada!"
    show kevin 9f
    show okita 4f
    kev "Umm, {b}Miss Okita{/b}? Você poderia nos ajudar com alguma coisa?"
    show kevin 8f
    show okita 9f
    okita "Ugh."
    show okita 3 at Position(xpos=0.5, ypos=1.0) with dissolve

    okita "Sim, {b}Kevin{/b}. O que é isso?"
    show kevin 9f
    show okita 4
    kev "{b}Ronda{/b} e eu estava trabalhando na tarefa que você distribuiu durante a aula hoje e nos deparamos com um problema."
    show kevin 8f
    show okita 9
    okita "*Suspiro*"
    show okita 5
    okita "Claro que você fez..."
    show okita 3
    okita "Muito bem. Vamos fazer isso na minha mesa. {b}[firstname]{/b} está trabalhando em algo importante para mim."
    hide kevin
    hide kevinl
    with dissolve
    hide okita
    with dissolve
    pause
    hide player
    show player 538f with dissolve
    player_name "Hmm..."
    player_name "Tudo parece bem."
    show player 539f with dissolve

    player_name "Isso é legal!"
    scene location_school_science_closeup
    show xtra 38b zorder 6 with dissolve
    show okita 4 zorder 0 at right
    show kevin 9f zorder 2 at Position(xpos=0.25, ypos=1.0)
    show kevinl 1 zorder 3 at Position(xpos=0.2535, ypos=1.0)
    show ronda b_casual a_casual_sides f_normal o_labcoat1 zorder 4 at flip
    show ronda at Position (xpos=300)
    with dissolve

    player_name "Hmm, todas as funções parecem estar funcionando..."
    player_name "..."
    player_name "Só precisa testar a câmera."
    show xtra 38
    show kevinl 1b
    show ronda o_labcoat2
    show okitax 1 zorder 1 at Position(xpos=0.86, ypos=1.0)
    pause 0.25
    show xtra 38b
    show kevinl 1
    show ronda o_labcoat1
    hide okitax
    pause 1
    player_name "O que"
    show okita 5
    show kevin 8f
    player_name "... Isso apenas?"
    show xtra 38
    show kevinl 1b
    show ronda o_labcoat2
    show okitax 1 zorder 1 at Position(xpos=0.86, ypos=1.0)
    pause 0.25
    show xtra 38b
    show kevinl 1
    show ronda o_labcoat1
    hide okitax
    pause 0.25
    show xtra 38
    show kevinl 1b
    show ronda o_labcoat2
    show okitax 1 zorder 1 at Position(xpos=0.86, ypos=1.0)
    pause 0.25
    show xtra 38b
    show kevinl 1
    show ronda o_labcoat1
    hide okitax
    pause 1.5
    player_name "Eles ficaram nus por um segundo..."
    show okita 4
    show kevin 9f
    player_name "..."
    player_name "Talvez se eu segurar o botão?"
    show xtra 38
    show kevinl 1b
    show ronda o_labcoat2
    show okitax 1 zorder 1 at Position(xpos=0.86, ypos=1.0)
    pause 1
    player_name "( !!! )" with hpunch
    player_name "Uau!"
    player_name "São como óculos reais de raios-X!"
    pause
    player_name "... Eu não acho que isso deveria acontecer."
    pause
    show okita 5
    show kevin 8f
    player_name "eu consigo ver {b}Miss Okita's{/b}... "
    pause
    player_name "... E olhe para o corpo da {b}Ronda{/b}! Ela é tão em forma!"
    pause
    player_name "..."
    show okita 4
    show kevin 9f
    player_name "Oh meu Deus! eu consigo ver {b}Kevin{/b}..."
    pause
    hide ronda
    show kevin 8 at Position(xpos=0.15, ypos=1.0)
    show kevinl 1bf at Position(xpos=0.1485, ypos=1.0)
    with dissolve
    show okita 9
    player_name "Uh oh, eu entendi preso neste modo!"
    hide kevin
    hide kevinl
    hide okita
    hide okitax
    show okita 4 zorder 0
    show okitax 1 zorder 1 at Position(xpos=0.49, ypos=1.0)
    with dissolve
    player_name "Ela está voltando!!!"
    player_name "Não não não!"
    scene location_school_science_closeup02
    show player 22f zorder 0 at right
    show playerg 2f zorder 1 at Position(xpos=0.83, ypos=0.35)
    show okita 5f at left
    with dissolve
    okita "Bem?"
    show player 11f
    show okita 4f
    player_name "..."
    show okita 11f
    okita "{b}[firstname]{/b}!?"
    show player 10f
    show okita 11bf
    player_name "Sim?"
    show player 11f
    show okita 11f
    okita "Qual o problema com você?!"
    okita "Me dê os óculos!"
    show player 10f
    show okita 11bf
    player_name "Oh, Certo..."
    hide playerg
    show player 540cf
    with dissolve
    player_name "Aqui."
    show player 11f
    show okita 4f
    show okitag 4f at Position(xpos=0.17, ypos=0.525)
    with dissolve
    player_name "..."
    show okita 3f
    okita "Por que tudo é verde?"
    show okita 4f
    pause
    show okita 3f
    okita "... E por que você"
    show okita 8f
    show player 22f
    pause
    show okita 3f
    okita "Hã."
    okita "Isso é peculiar."
    show player 11f
    show okita 4f
    player_name "..."
    show okita 3f
    okita "... Muito peculiar."
    show okita 5f
    with dissolve
    okita "{b}[firstname]{/b}, você ainda tem o código no meu escritório?"
    show okita 4f
    show player 11f
    player_name "Sim, {b}Miss Okita{/b}."
    show player 73f
    pause
    show player 459f
    pause
    show player 461f
    show okita 5f
    okita "Então me {b}encontre lá em cima no meu escritório{/b}."
    show okita 4f
    show player 460f
    player_name "Huh?"
    show player 461f
    show okitag 4 at Position(xpos=0.09, ypos=0.525)
    show okita 5 at left
    with dissolve
    okita "Agora mesmo."

    hide okitag
    hide okita
    hide player
    show player 11f
    with dissolve
    pause
    show player 10f
    player_name "Uh... Ok."
    show player 11f
    player_name "( Eu me pergunto por que ela quer me ver em seu escritório? )"

    return

label science_classroom_okita_has_glasses_int_fail:
    scene location_school_science_cutscene05
    with fade
    show text "Então eu comecei a trabalhar." at Position(xpos=512, ypos=700) with dissolve
    pause
    hide text
    with dissolve
    scene location_school_science_cutscene05b
    with fade
    show text "[int_warn]Hmm, essa coisa deveria estar funcionando?" at Position(xpos=512, ypos=700) with dissolve
    pause
    hide text
    with dissolve
    scene location_school_science_closeup
    show player 16 zorder 0 at left
    show playerl 1 zorder 1 at Position(xpos=0.152, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.17, ypos=0.3475)
    show okita 11 at right
    okita "Não, não é absolutamente proibido fumar!"
    show player 12
    show okita 11b
    player_name "... Me desculpe!"
    player_name "Eu te disse, não estou qualificado para trabalhar em algo assim!"
    show player 16
    show okita 11
    okita "É melhor descobrir isso e rápido!"
    okita "... Caso contrário, você pode esquecer de passar na minha aula."
    show player 12
    show okita 11b
    player_name "Ugh, bem! Vou tentar de novo amanhã."
    show player 16
    show okita 9
    okita "Sim Sim. Apenas volte aqui e termine logo."
    show okita 11
    okita "... E anima-se, você vai conseguir!?"
    hide okita with dissolve
    show player 24 at Position(xpos=0.35, ypos=1.0)
    show playerl 1 zorder 1 at Position(xpos=0.502, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.52, ypos=0.3475)
    with dissolve
    player_name "*Suspiro*"
    show player 25
    player_name "{b}Acho que devo ir para casa e trabalhar na minha inteligência{/b}..."


    return

label science_classroom_mia_strip_aftermath:
    scene school_science_c02
    show player 5 at left
    show mia 12 at right
    show mial 1f at right
    with dissolve
    mia "Ei, {b}[firstname]{/b}..."
    show mia 8
    show player 10
    player_name "{b}Mia{/b}!"
    player_name "Desculpe pela outra noite."
    show player 12
    player_name "Está tudo bem em casa?"
    show player 5
    show mia 12
    mia "Na verdade, eu queria falar sobre isso."
    show mia 8
    show player 11
    player_name "..."
    show mia 12
    mia "Agora estou proibida de passar tempo com os amigos ... e especialmente você."
    mia "Minha mãe diz que eu tenho que estar em casa depois da escola e não falar com você..."
    show mia 8
    show player 10
    player_name "...Mas {b}Mia{/b} eu"
    show player 11
    show mia 12
    mia "Não podemos conversar, desculpe..."
    hide mia
    hide mial
    with dissolve
    show player 24
    player_name "Eu não queria te meter em problemas..."
    hide player with dissolve
    return

label science_classroom_okita_has_faptic:
    scene location_school_science_closeup
    show player 1 at left
    show okita 3 at right
    with dissolve
    okita "Você entendeu?"
    show player 506 with dissolve
    show okita 4
    player_name "Eu tenho aqui, Sra. Okita.."

    show player 505
    show okita 3
    okita "Hmm, algo parece errado..."
    show okita 5
    okita "Isso é o que {b}June{/b} conseguiu?"
    show okita 4
    show player 10 with dissolve
    player_name "Err, sim, senhora."
    show player 11
    show okita 10b at Position(xpos=0.98, ypos=1.0) with dissolve
    okita "..."
    show okita 5 at right with dissolve
    okita "Talvez seja apenas minha imaginação então."
    player_name "..."
    show okita 4
    okita "Muito bem, fique depois da aula e nós vamos começar no cinto."
    show player 10
    show okita 5
    player_name "Ok."




    scene location_school_science_closeup
    show player 1 at left
    show okita 3 at right
    with dissolve
    okita "Tudo bem, {b}[firstname]{/b}. Apenas siga as instruções."
    show okita 5
    okita "... E tente não estragar tudo."
    show player 25
    show okita 4
    player_name "*Suspiro* Sim, senhora."

    return

label science_classroom_okita_has_faptic_try_again:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    player_name "Tudo bem, {b}Miss Okita{/b}. Eu acho que vou fazer melhor desta vez."
    show player 1
    show okita 9
    okita "Você não poderia fazer nada pior."
    show player 16
    show okita 4
    player_name "..."
    show player 12
    player_name "Vou conseguir fazer funcionar desta vez, eu sei!"

    show player 16
    show okita 5
    okita "Bem, terá que esperar até depois da aula. Vá se sentar, {b}[firstname]{/b}."

    show player 2
    show okita 4
    player_name "Estou pronto, vamos fazer isso!"
    show player 1
    show okita 5
    okita "Por todos os meios."
    return

label science_classroom_okita_has_faptic_int_pass:

    scene location_school_science_closeup
    show player 550 at left
    show okita 4 at right
    with dissolve
    player_name "É isso aí! Eu tenho isso!"
    show player 549
    show okita 5
    okita "Vamos ver isso."
    show player 1
    show okita 23
    with dissolve
    pause
    show okita 22
    okita "Hmm, sim ... tudo parece correto."
    show okita 23
    pause
    show okita 22
    okita "Vamos ao meu escritório para esta próxima parte, [firstname]."
    okita "Os testes exigirão um pouco de privacidade..."
    show player 10
    show okita 23
    player_name "... Privacidade?"
    hide okita with dissolve
    show player 11
    pause
    show player 10
    player_name "Eu me pergunto o que ela quis dizer com isso?"
    return

label science_classroom_okita_has_faptic_int_fail:
    scene location_school_science_closeup
    show player 11 zorder 0 at left
    show playerl 1 zorder 1 at Position(xpos=0.152, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.17, ypos=0.3475)
    show okita 11 at right
    okita "Sério mesmo?!"
    show player 10
    show okita 11b
    player_name "Me desculpe, eu não sei o que!"
    show player 11
    show okita 11
    okita "Grr... Bem, é melhor você descobrir!"
    okita "Eu preciso dessa coisa trabalhando!"
    okita "... Caso contrário, você pode esquecer de passar na minha aula."
    show player 12
    show okita 11b
    player_name "Ugh, bem! Vou tentar de novo amanhã."
    show player 16
    show okita 9
    okita "Sim Sim. Volte aqui e termine em breve."
    show okita 11
    okita "... E anime-se, vai da certo ok!?"
    hide okita

    show player 24 at Position(xpos=0.35, ypos=1.0)
    show playerl 1 zorder 1 at Position(xpos=0.502, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.52, ypos=0.3475)
    with dissolve
    player_name "{b}Eu deveria ir para casa e trabalhar na minha inteligência{/b} novamente."

    return

label button_okita_tinkering_belt:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    with dissolve
    player_name "Você já fez algum progresso com o cinturão?"
    show player 1
    show okita 5
    okita "Ainda não, ainda estou trabalhando nisso..."
    show player 1
    show okita 4
    player_name "Tudo bem, acho que vou voltar a falar com você amanhã."
    return

label button_okita_tinkered_belt:
    $ persistent.cookie_jar["Okita"]["gallery"]["03_unlocked"] = True
    scene location_school_science_closeup
    show player 2 at left
    show okita 1 at right
    with dissolve
    player_name "Você fez algum progresso com o cinturão?"
    show player 1
    show okita 2
    okita "Eu reduzi o problema a algumas possibilidades. Traga-me o controle remoto da minha mesa e eu vou lhe mostrar."
    show player 2
    show okita 1
    player_name "Certo."
    hide player with dissolve
    pause
    pause
    show player 536 at left with dissolve
    pause
    show player 537
    player_name "Tudo bem, agora o que-"
    show player 536
    smi "Tori!!!" with hpunch
    smi "Onde você está, sua detestável sabe tudo?!"
    show okita 3
    okita "Oh ótimo..."
    show okita 5
    okita "Vá sentar, {b}[firstname]{/b}. Eu vou lidar com ela."
    show okita 11
    okita "E esconda esse controle remoto!"
    show player 2 with dissolve
    show okita 11b
    player_name "Ok, {b}Miss Okita{/b}!"


    scene location_school_science_cutscene06
    with fade
    show text "Receio que a curiosidade tenha me superado..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... Mas em minha defesa." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene location_school_science_cutscene07
    with fade
    show text "Eu não sabia que ela estava usando o cinto naquele momento!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... Pobre, {b}Miss Okita{/b}." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_school_science_closeup
    show okita 11bf zorder 1 at Position(xpos=0.28, ypos=1.0)
    show principal 28 zorder 2 at right
    with dissolve
    smi "Eu sei que você está trabalhando naqueles dispositivos estúpidos novamente nas minhas costas!"
    show okita 9f
    show principal 29 at Position(xpos=0.95, ypos=1.0) with dissolve
    okita "Eu não tenho a menor idéia do que você está falando..."
    show okita 11bf
    show principal 2
    smi "NÃO ME MENTIRA, {b}TORI{/b}!" with hpunch
    show principal 28 at right with dissolve
    smi "Seu escritório está desbloqueado novamente e alguém estava bisbilhotando minhas gavetas!"
    smi "Eu sei que você teve ajuda e eu quero saber quem era!"
    show okita 11f
    show principal 29 at Position(xpos=0.95, ypos=1.0) with dissolve
    okita "Você tem algum.."
    show okita 76f at Position(xpos=0.32, ypos=1.0) with dissolve
    okita "*gasp*" with hpunch
    show okita 77f at Position(xpos=0.28, ypos=1.0) with dissolve
    pause
    show okita 80f
    pause
    show okita 77f

    okita "Você tem algum..."
    show okita 78f
    smi "..."
    show principal 27
    smi "O que?!"
    smi "... Que som é esse?!"
    show okita 79f
    show principal 29
    okita "Ahh..."
    show okita 77f
    okita "Você tem alguma ... Alguma prova?"
    show principal 27
    show okita 78f
    smi "Ainda não!"
    show principal 28 at right with dissolve
    smi "Mas se houver algum, é melhor você acreditar que eu o encontrarei!"
    show principal 29 at Position(xpos=0.95, ypos=1.0) with dissolve
    okita "Mmmm."
    show okita 79f

    okita "Oooohh, Haaaaaaah..."
    show okita 78f
    show principal 27
    smi "O que diabos é o problema com você?!"
    smi "Você está agindo ainda mais estranho do que o habitual..."
    show principal 29
    okita "Hmm?"
    show okita 77f
    okita "Não, nada..."
    show okita 79f
    okita "... Nada é..."
    okita "... Estou bem."
    show okita 81f
    okita "Ooooh, Uau!!!"
    show okita 78f
    show principal 28 at right with dissolve
    smi "Eu tenho que te lembrar, que ninguém mais iria contratar sua bunda arrogante!?"
    smi "Esta é sua última parada, {b}Tori{/b}!"
    smi "Depois disso, você estará trabalhando na janela de fast food para o salário mínimo!"
    smi "Nós temos um entendimento aqui?!?"
    show okita 79f
    show principal 29 at Position(xpos=0.95, ypos=1.0) with dissolve
    okita "Simmmm!! simmmmm!!!"
    show okita 81f
    okita "AHHHHH!!!"
    okita "Simmmmm!!!!"
    show okita 81f at Position(xpos=0.3, ypos=1.25)
    okita "Oooohh..."
    show okita 79f at Position(xpos=0.32, ypos=1.35)

    smi "( !!! )" with hpunch
    show okita 78f
    show principal 27
    smi "O que há com você hoje?!"
    show okita 77f
    show principal 29
    okita "Haaah, haaah..."
    okita "Nada ... eu só..."
    show okita 78f
    pause
    show okita 77f
    okita "Haaah, haaah..."
    okita "Eu só ... Não me sinto ... Tão bom..."
    okita "Preciso ... Ir deitar."
    show okita 78f
    show principal 27
    smi "Meu deus, {b}Tori{/b}."

    smi "Alguém venha aqui e ajude {b}Miss Okita{/b} para o escritório dela!"
    show player 10 zorder 0 at left
    show principal 29
    player_name "Eu eu vou fazer isso."
    show player 11
    player_name "..."
    show principal 27
    smi "Bem?! Não fique aí parado! e ajude logo!"
    hide player
    hide okita
    show principal 29
    show okita 81c at Position(xpos=0.35, ypos=1.0)
    with dissolve
    pause
    show okita 81b at Position(xpos=0.15, ypos=1.0)

    okita "Oooh, é muito..."
    okita "Eu vou..."
    hide okita
    hide principal
    show principal 29
    with dissolve
    okita "EU VOU!"
    show principal 27
    smi "Vou substituir por hoje."
    smi "Aproveite enquanto durar, {b}Tori{/b}! Vou ter esse cadeado recodificado até o final da semana!"
    smi "Este é o seu último aviso e eu quero dizer isso!"



    scene location_school_office4_day_closeup
    show okita 81b at Position(xpos=0.55, ypos=1.0)
    with dissolve
    okita "Haaah!!! Simm!!"
    okita "Oh, Eu vou..."
    show okita 81c
    player_name "Qual é o seu problema?"
    show okita 81b
    okita "The remote!!"

    okita "OOOOHHHHH!!!"
    show okita 81c
    player_name "Hã?"
    hide okita
    show player 11 zorder 1 at Position(xpos=0.25, ypos=1.0)
    show okita 81 zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    okita "Desligue isso! Desligue isso!"
    show player 10
    show okita 78
    player_name "Desligar o que?"
    show player 11
    show okita 79
    okita "O CINTO! DESLIGUE ISSO!"
    show player 10
    show okita 78
    player_name "Quer dizer que você está usando agora?!"
    show player 11
    show okita 79
    okita "SIM! CALA A BOCA DESLIGAR! POR FAVOR!!!"
    show player 29 with dissolve
    show okita 78
    player_name "Eu deixei o controle remoto lá no meu jaleco."
    show player 3
    show okita 81
    okita "OOOH! NÃO POSSO TOMAR OUTRO!"
    show okita 81e with dissolve
    okita "AJUDE-ME A DESAPARECER!"
    show okita 81d
    show player 10 with dissolve
    player_name "... Você quer que eu?"
    show okita 81e
    okita "TIRE AGORA!"
    show player 520 at Position(xpos=0.4, ypos=1.0)
    show okita 81d
    player_name "Ahh, imediatamente, senhora!"
    player_name "..."
    player_name "Uau, essa coisa está vibrando como um louco!"
    show okita 81e
    okita "SE APRESSE!!"
    show okita 81d
    pause
    show okita 81g
    show player 550 at Position(xpos=0.25, ypos=1.0) with dissolve
    player_name "Got it!"
    show player 549
    okita "Haaah... Haaah..."
    okita "Isso foi ... eu nunca..."
    okita "Uau!"
    okita "Estou toda molhada!"
    show player 550
    show okita 83 at Position(xpos=0.62, ypos=1.0) with dissolve
    player_name "Sim, o cinto está todo molhado também..."
    show player 549
    show okita 82
    okita "Haaah... Haaah..."
    okita "Não consigo sentir minhas pernas..."
    show okita 84
    okita "Haaah... Haaah..."
    okita "Eu preciso deitar."
    show okita 83
    show player 10 at Position(xpos=0.22, ypos=1.0) with dissolve
    player_name "Posso te dar alguma coisa??"
    show okita 84
    show player 11
    okita "Hã?"
    okita "Oh, não."
    show okita 83
    pause
    show okita 82
    okita "Eu estou bem. Muito bom..."
    show okita 84
    okita "Apenas volte para a aula. Podemos falar depois."
    show player 10
    show okita 83
    player_name "Tudo bem."
    return

label science_classroom_dewitt_science_adhesive:
    scene school_science_c02
    show xtra 36f
    show xtra_lab_clip 46 at Position (xoffset=0,yoffset=0)
    show xtra_sticky_paper 46b at Position (xoffset=0,yoffset=0)
    show kevin labcoat 2 at right
    with dissolve
    show player 14 zorder 1 at Position (xoffset=-84)
    with dissolve
    player_name "Como está indo? {b}Kevin{/b}?"
    show player 13 at Position (xoffset=-84)
    show kevin labcoat 3 with dissolve
    kev "Não se preocupe, irmão! Eu entendi bem aqui."
    hide xtra_sticky_paper
    show kevin labcoat 4
    with dissolve
    show player 108f at Position (xoffset=-84)
    player_name "... É isso aí?"
    show player 111f at Position (xoffset=-84)
    player_name "deixa eu ver!"
    show player 617
    show kevinl 1f at Position (xoffset=350)
    show kevin 24 at Position (xoffset=-6)
    with dissolve
    kev "Uau! mano, tenha cuidado com essas coisas!"
    show kevin 33 at Position (xoffset=-6)
    show player 619
    player_name "Ugh!"
    show player 620 with dissolve
    pause
    show player 621 at Position (xpos=550) with dissolve
    player_name "!!!" with hpunch
    show kevin 33b at Position (xoffset=-6)
    kev "!!!"
    show player 622 with dissolve
    show kevin 24 at Position (xoffset=-6)
    kev "... Mano. Que porra é essa!"
    show kevin 33 at Position (xoffset=-6)
    show player 621 with dissolve
    player_name "Cara ... está preso!"
    show player 622 with dissolve
    show kevin 24 at Position (xoffset=-6)
    kev "Pfft, não brinca?!"
    kev "Eu te disse para ter cuidado!"
    show kevin 24b at Position (xoffset=-6)
    show player 621e with dissolve
    player_name "... Agora o que fazemos?!"
    show player 621c with dissolve
    show kevin 24 at Position (xoffset=-6)
    kev "Eu tenho que encontrar o solvente."
    show kevin 24b at Position (xoffset=-6)
    show player 621e with dissolve
    player_name "Quanto tempo isso vai levar?"
    show player 621c with dissolve
    show kevin 24 at Position (xoffset=-6)
    kev "Não sei, ela guarda uma garrafa por aqui em algum lugar!"
    kev "Seria muito mais fácil se a sua mão não estivesse presa no meu pau, mano!!"
    hide kevinl
    show kevin labcoat 2
    show player 621d
    with dissolve
    player_name "{b}*Suspiro*{/b}"
    player_name "Droga..."
    show player 621c with dissolve
    show eve 2bf zorder 0 at Position (xoffset=-340) with dissolve
    eve "!!!"
    show eve 6f at Position (xoffset=-340)
    eve "Estou interrompendo alguma coisa? Porque eu posso voltar mais tarde, se vocês, rapazes, precisarem de algum tempo sozinhos."
    show eve 5f at Position (xoffset=-340)
    show player 621f with dissolve
    player_name "Haha... Haha. Você é hilária, sabia disso?"
    show player 621c with dissolve
    show eve 6f at Position (xoffset=-340)
    eve "Como você conseguiu isso?!"
    show eve 5f at Position (xoffset=-340)
    show player 621d with dissolve
    show kevin labcoat 6 with dissolve
    player_name "Eu prefiro não falar sobre isso..."
    show player 621c with dissolve
    show eve 6f at Position (xoffset=-340)
    eve "Hahaha! Sim, eu aposto que não!"
    show eve 5f at Position (xoffset=-340)
    show kevin labcoat 7 with dissolve
    kev "Tudo bem, eu entendi!"
    show player 621e with dissolve
    player_name "Graças a Deus."
    show player 621b
    show kevin labcoat 8 with dissolve
    show player 621e
    player_name "O que agora?"
    show player 621c
    show kevinl 1f at Position (xoffset=350)
    show kevin 24 at Position (xoffset=-6)
    with dissolve
    kev "... Uh.Puxe, eu acho?"
    show player 622 with dissolve
    show kevin 33 at Position (xoffset=-6)
    pause
    show player 623 at Position (xoffset=-200) with dissolve
    show kevin 23 at Position (xoffset=-6)
    player_name "!!!"
    show eve 26 at Position (xoffset=-365) with hpunch
    eve "!!!"
    eve "... Isso não aconteceu apenas..."
    show player 625 at Position (xoffset=-205)
    player_name "..."
    show player 624 at Position (xoffset=-205)
    player_name "... Merda."
    show player 625 at Position (xoffset=-205)
    show kevin 32 at Position (xoffset=-6)
    kev "Hahahaha!"
    scene black with fade

    show popup_item_sticky1 at truecenter with dissolve
    pause
    hide popup_item_sticky1 with dissolve

    scene expression game.timer.image("outside_school{}") with fade
    show eve 2b at right
    show kevin 23 at Position (xpos=600)
    show player 13 at left
    with dissolve
    eve "Vocês realmente vão entrar no escritório da {b}Diretora Smith{/b} hoje à noite?!"
    show eve 1
    show player 10
    player_name "Você não vem?"
    show player 5
    show eve 6b
    eve "De jeito nenhum. Desculpa, {b}[firstname]{/b}."
    show eve 2b
    eve "Não me interpretem mal ... Eu gosto de um pouco de travessuras tanto quanto a próxima garota, mas essa é muito arriscada!"
    show eve 1
    show player 14
    player_name "Está bem, {b}Eve{/b}. {b}Kevin{/b} e eu vamos lidar com isso."
    show player 13
    show kevin 33
    kev "..."
    show player 10
    player_name "{b}Kevin{/b}?"
    show player 5
    show kevin 24
    kev "... Na verdade, acho que vou destacar essa parte também."
    show kevin 24b
    show player 12
    player_name "A sério?"
    player_name "O que?! Depois de toda a sua grande conversa anterior?"
    show player 5
    show kevin 22 with dissolve
    kev "... Desculpe, {b}[firstname]{/b}."
    show kevin 24b with dissolve
    show player 37 with dissolve
    player_name "..."
    show eve 2b
    eve "O que você vai fazer?"
    show eve 1
    show player 12 with dissolve
    player_name "Eu ainda estou pensando sobre isso."
    player_name "Não posso deixar a {b}Diretora Smith{/b} estragar o {b}Show de talentos{/b}!"
    show player 5
    show eve 2b
    eve "... Você realmente vai fazer isso sozinho?"
    show eve 1
    show player 10
    player_name "Eu acho que preciso."
    show player 5
    show kevin 33
    show eve 9f
    eve "..."
    show player 34
    kev "..."
    show player 35
    player_name "Não sei, talvez {b}Erik{/b} Me ajudará?"
    show player 5
    show kevin 24b
    show eve 2b
    eve "... {b}Erik{/b}?"
    eve "Hehe, você provavelmente seria melhor você ir sozinho o {b}Erik{/b} e um idiota!"
    show eve 1
    show player 12
    player_name "Ei, não fala isso do... {b}Erik{/b} ele é um cara legal!"
    player_name "... Ele não me deixaria na mão."
    show player 5
    show eve 9f
    show kevin 33
    eve "..."
    kev "..."
    show eve 2b
    eve "Você está certo {b}[firstname]{/b} Não tenho esse direito de falar dele desculpe."
    show eve 1
    show kevin 24
    kev "Sim, apenas..."
    kev "... Tenha cuidado, ok?"
    show kevin 24b
    show player 12
    player_name "eu vou ficar bem."
    hide eve
    hide kevin
    with dissolve
    pause
    show player 10
    player_name "... Eu deveria ir perguntar {b}Erik{/b} se ele vai me ajudar {b}esgueirar-se para a escola hoje à noite{/b}."
    player_name "É perigoso ir sozinho..."
    hide player with dissolve
    return

label science_classroom_microscope_dialogue:
    scene expression "backgrounds/location_school_science_flies_day.jpg"
    player_name "O que" with hpunch
    pause
    player_name "Que nojo..."
    player_name "Agora eu realmente não quero nenhuma mosca pousando em mim..."
    $ A_flies.unlock()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
