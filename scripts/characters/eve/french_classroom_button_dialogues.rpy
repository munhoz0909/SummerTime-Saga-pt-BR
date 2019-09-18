label eve_classroom_dialogue_eve_intro:
    scene classroom
    show evedesk 1 at left
    with fade
    eve "Uau ... eu pensei que você estava morto, com certeza!"
    show evedesk 2
    player_name "O que? Como assim?"
    show evedesk 1
    eve "Não sei ... Você está desaparecido o mês todo e as pessoas começaram a inventar rumores sobre como sua família havia sido assassinada ou algo assim ..."
    show evedesk 3
    player_name "Ugh ... Não é nada disso!"
    show evedesk 4
    eve "Eu imaginei. As pessoas gostam de fofocar, e essa escola é apenas uma grande piada."
    eve "Fico feliz que nosso último ano esteja quase no fim ..."
    show evedesk 5
    player_name "Sim, eu sei o que você quer dizer."
    show evedesk 6
    eve "Você deveria sair conosco no {b} park {/b} em algum momento ... Evite todos esses idiotas na escola e relaxe, sabe?"
    show evedesk 5
    eve "Certifique-se de vir à {b} noite {/b} ... geralmente é quando vamos lá."
    player_name "Ehh ... Eu acho que eu poderia ir uma noite."
    show evedesk 6
    eve "Você decide. Faça o que você quiser!"
    show evedesk 4
    eve "Oh, ei, você ouviu o anúncio da {b}Miss Bissette's{/b} sobre uma recompensa especial?"
    show evedesk 1
    eve "Ou você estava dormindo nessa parte?"
    show evedesk 3
    player_name "Ei! Eu estava acordado ... nessa parte."
    show evedesk 4
    eve "Eu me pergunto qual será a recompensa."
    eve "Ela realmente não falou muito sobre isso. Provavelmente algo estúpido de qualquer maneira."
    eve "Eu já estou indo muito bem, então nem vale a pena tentar."
    show evedesk 2
    player_name "Por que não?"
    show evedesk 6
    eve "Como está indo de um B para um A seria uma coisa muito melhor?"
    eve "Você seria mais provável ganhar ..."
    show evedesk 5
    player_name "Eu?"
    show evedesk 1
    eve "Bem, sim ... você está ruim agora, não está?"
    eve "Você pode melhorar muito."
    show evedesk 6
    eve "Além disso, {b} Miss Bissette {/b} favorece homens de qualquer maneira."
    eve "Você deve considerar seriamente."
    hide evedesk with dissolve
    return

label eve_classroom_dialogue_intro:
    show evedesk 4 at left with dissolve
    eve "Olá, {b}[firstname]{/b}."
    show evedesk 5
    player_name "Oi, {b}Eve{/b}."
    show evedesk 4
    eve "E aí?"
    return

label eve_classroom_dialogue_talent_show_help:
    show evedesk 5
    player_name "Você toca algum instrumento?"
    show evedesk 4
    eve "Não, eu não toco nenhum instrumento. Eu sempre quis aprender, mas não tive tempo, sabia?"
    show evedesk 5
    player_name "Ok, bem, e quanto a cantar?"
    show evedesk 1
    eve "Oh, umm..."
    show evedesk 4
    eve "Yeah, I like to sing I guess. I dunno if I'm any good though."
    show evedesk 5
    player_name "I bet you are! You should sign up for the talent show with me!"
    show evedesk 3
    player_name "We're really hurting for more volunteers."
    show evedesk 1
    eve "... Yeah, I dunno."
    eve "You want me to sing in front of the entire school? That sounds pretty embarassing."
    eve "... And I haven't sang in awhile. Not since my karaoke machine broke."
    eve "I'm quite out of practice."
    show evedesk 5
    player_name "Hmm..."
    player_name "You know, I think my friend {b}Erik{/b} has a {b}karaoke machine{/b} in his basement."
    show evedesk 4
    eve "Oh, yeah?"
    show evedesk 5
    player_name "Totally! You should come over sometime and practice!"
    show evedesk 4
    eve "Heh, you want me to sing for you and your friend?"
    show evedesk 5
    player_name "Nah, we can all sing together! C'mon, we'll do it tonight, it'll be fun!"
    eve "..."
    show evedesk 4
    eve "Alright, I guess I can stop by for a little while."
    show evedesk 5
    player_name "Awesome! {b}I'll meet you at Erik's house{/b} tonight."
    return

label eve_classroom_dialogue_adehsive:
    show evedesk 5
    player_name "What was the plan again?"
    show evedesk 4
    eve "You're supposed to meet {b}Kevin{/b} in the {b}science lab after class{/b}."
    eve "Remember?"
    show evedesk 5
    player_name "Oh, that's right. Thanks, {b}Eve{/b}!"
    return

label eve_classroom_dialogue_bissettes_reward:
    show evedesk 5
    player_name "Are you going to sign up to be tutored by {b}Miss Bissette{/b}?"
    show evedesk 4
    eve "I'm already doing pretty well so it's not even worth trying."
    show evedesk 2
    player_name "Why not?"
    show evedesk 6
    eve "How is going from a B to an A much improvement?"
    eve "You'd be more likely to win..."
    show evedesk 5
    player_name "Me?"
    show evedesk 1
    eve "Well, yeah... you're failing right now aren't you?"
    eve "You've got lots of room for improvement."
    show evedesk 6
    eve "Plus, {b}Miss Bissette{/b} favors guys anyway."
    eve "You should seriously consider it."
    return

label eve_classroom_dialogue_hang_out:
    show evedesk 5
    player_name "Where did you say you hung out at?"
    show evedesk 4
    eve "My friends and {b}I hang out at the park{/b}."
    eve "Just make sure you {b}come by at night{/b}... it's usually when we go out there."
    show evedesk 5
    player_name "Alright. I might stop by one night."
    show evedesk 6
    eve "It's up to you. Do whatever you want!"
    return

label eve_classroom_dialogue_leave:
    show evedesk 5
    player_name "Nothing, just wanted to say hello."
    show evedesk 4
    eve "Oh. Talk to you later then."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
