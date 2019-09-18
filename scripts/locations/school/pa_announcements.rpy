label pa_announcement:
    if random.randint(1,100) < 5 and not game.timer.is_dark() and not game.timer.is_weekend() and M_smith.get("school intro done"):
        scene expression player.location.background_blur
        call expression "pa_announcement_{}".format(random.randint(1,23))
    return

label pa_announcement_1:
    show player 35b
    PA "Atenção Seniors:"
    PA "O final do prazo está se aproximando rapidamente e você sabe o que isso significa..."
    PA "Chegou a hora de encontrar uma data e ir à pista de dança no nosso Baile Anual de Irmandades!"
    PA "Esperamos ver todos vocês lá!"
    player_name "..."
    return

label pa_announcement_2:
    show player 35b
    PA "Atenção Estudantes:"
    PA "Este é um lembrete de que o PDA é estritamente proibido nos corredores do Summerville College..."
    PA "Portanto, mantenham suas mãos e, mais importante, seus genitais para si mesmos!"
    PA "Obrigado e tenha um ótimo dia!"
    player_name "..."
    return

label pa_announcement_3:
    show player 35b
    PA "Atenção:"
    PA "{b}Diretora Smith{/b}, você tem um grande pacote esperando por você em seu escritório."
    show player 35
    PA "Eu repito."
    PA "{b}Diretora Smith{/b}, você tem um grande pacote esperando por você em seu escritório."
    player_name "..."
    return

label pa_announcement_4:
    show player 35b
    PA "Atenção Estudantes:"
    PA "O dia do taco na cafeteria foi cancelado, devido a uma unidade de refrigeração com defeito."
    PA "Chili será servido como um substituto."
    show player 35
    PA "... Em uma nota não relacionada. Qualquer pessoa que mostre sinais de intoxicação alimentar deve ser levada imediatamente ao escritório principal."
    PA "Obrigado e tenha um bom dia!"
    player_name "..."
    return

label pa_announcement_5:
    show player 35b
    PA "Faculdade de Atenção:"
    PA "Quem deixou os brownies na sala dos professores é solicitado a se reportar a {b}Diretora Smith{/b} escritório o mais cedo possível."
    show player 35
    PA "Eu repito."
    PA "Quem deixou os brownies na sala dos professores é solicitado a se reportar a {b}Diretora Smith{/b} escritório o mais cedo possível."
    PA "Thank you!"
    player_name "..."
    return

label pa_announcement_6:
    show player 35b
    PA "Atenção Estudantes:"
    PA "Este é um lembrete de que o assédio moral é uma desaprovação fortemente aqui no Summerville College."
    PA "Qualquer pessoa que sinta que está sendo intimidado é incentivado a relatar a situação ao nosso representante de bem-estar, {b}Dexter{/b}."
    PA "Obrigado e tenha um bom dia!"
    player_name "..."
    return

label pa_announcement_7:
    show player 35b
    PA "Faculdade de Atenção:"
    PA "Este é um lembrete de que bebidas alcoólicas são estritamente proibidas no Somerville College."
    PA "Isso inclui escritórios pessoais."
    show player 43
    PA "Obrigado e tenha um bom dia!"
    player_name "..."
    return

label pa_announcement_8:
    show player 35b
    PA "Atenção Estudantes:"
    PA "Gostaríamos de convidar todos para que apóiem nossa equipe de basquete da escola."
    PA "Quero dizer, claro. Eles são 0-12 nesta temporada, mas isso não significa que não podemos mostrar nosso orgulho escolar, participando!"
    show player 43
    PA "Venha torcer para que eles consigam conquistar sua primeira vitória da temporada!"
    player_name "..."
    return

label pa_announcement_9:
    show player 35b
    PA "Atenção Estudantes:"
    PA "Ainda estamos procurando preencher alguns pontos da equipe de atletismo de Summerville."
    PA "Fale com o treinador Bridget se você estiver interessado em representar sua escola na pista!"
    PA "... Nenhum Wussies permitido."
    show player 35
    player_name "..."
    return

label pa_announcement_10:
    show player 35b
    PA "Atenção Estudantes:"
    PA "Este é um lembrete de que desfigurar a propriedade da escola é um crime!"
    PA "... E qualquer aluno pego fazendo isso será entregue às autoridades competentes."
    PA "Obrigado e tenha um bom dia!"
    player_name "..."
    return

label pa_announcement_11:
    show player 35b
    PA "Atenção Estudantes:"
    PA "Os DVDs de Educação Sexual roubados do escritório da Coach Bridget ainda não foram encontrados.."
    show player 43
    PA "Se alguém tiver alguma informação sobre o paradeiro do DVD ou a pessoa que o roubou."
    PA "Por favor, reporte-se ao treinador Bridget imediatamente!"
    PA "Obrigado e tenha um bom dia!"
    player_name "..."
    return

label pa_announcement_12:
    show player 35b
    PA "Atenção amantes da música:"
    PA "{b}Miss Dewitt{/b} ainda procura pessoas talentosas para ajudá-la a formar uma banda escolar."
    PA "Se você tiver algum interesse, informe-a depois da aula."
    PA "Obrigado e tenha um bom dia!"
    show player 35
    player_name "..."
    return

label pa_announcement_13:
    show player 35b
    PA "Atenção Estudantes:"
    PA "Miss Okita gostaria de lembrar aos alunos que o jaleco e os óculos de segurança devem ser usados dentro do laboratório da escola o tempo todo."
    PA "Qualquer pessoa que não cumprir esta regra estará sujeita a uma ação disciplinar rigorosa."
    PA "Obrigado e tenha um bom dia!"
    show player 35
    player_name "..."
    return

label pa_announcement_14:
    show player 35b
    PA "Atenção:"
    PA "Para o proprietário do Conda Hivic vermelho, número da licença - 637 5chw1f7y."
    PA "Seu carro está estacionado ilegalmente e será rebocado se você não o mover imediatamente."
    show player 35
    PA "... Novamente."
    PA "Para o proprietário do Conda Hivic vermelho, número da licença - 637 5chw1f7y."
    PA "Seu carro está estacionado ilegalmente e será rebocado se você não o mover imediatamente."
    PA "Obrigado!"
    player_name "..."
    return

label pa_announcement_15:
    show player 35b
    PA "Atenção Amantes da arte:"
    PA "{b}Miss Ross{/b} oferecerá uma palestra especial única para os alunos neste sábado."
    PA "... Intitulado: 'Encontrando a felicidade em tudo!'"
    PA "Os participantes são incentivados a trazer lanches."
    PA "Obrigado e tenha um bom dia!"
    show player 43
    player_name "..."
    return

label pa_announcement_16:
    show player 35b
    PA "Atenção:"
    PA "Senhorita Bissette, sua presença é solicitada imediatamente no terceiro andar."
    PA "Temos relatos de um odor desagradável que emana do seu escritório."
    show player 35
    PA "eu repito."
    PA "Miss Bissette para o terceiro andar, imediatamente."
    PA "Obrigado!"
    player_name "..."
    return

label pa_announcement_17:
    show player 35b
    PA "Atenção Estudantes:"
    PA "Este é um lembrete de que material pornográfico não é permitido nas dependências da escola."
    show player 43
    PA "... E sim, isso inclui desenhos nus de personagens de fantasia de pele verde."
    PA "Obrigado e tenha um bom dia!"
    player_name "..."
    return

label pa_announcement_18:
    show player 35b
    PA "Atenção Estudantes:"
    PA "Este é um lembrete de que a descoberta de propriedades da escola é expressamente proibida."
    PA "... A menos que seja esse pedaço de impressora de merda no laboratório de informática."
    PA "Nesse caso, é expressamente encorajado!"
    show player 43
    PA "Obrigado e tenha um bom dia!"
    player_name "..."
    return

label pa_announcement_19:
    show player 35b
    PA "Atenção Estudantes:"
    PA "Recebemos várias reclamações envolvendo roubo de calcinhas usadas do vestiário."
    PA "Incentivamos qualquer pessoa com informações sobre esses incidentes a se apresentar imediatamente."
    PA "Obrigado e tenha um bom dia!"
    show player 35
    player_name "..."
    return

label pa_announcement_20:
    show player 35b
    PA "Atenção Cheerleaders:"
    PA "A prática desta noite foi suspensa em favor do que a treinadora Bridget chamou de - Real Sports."
    PA "Obrigado e tenha um bom dia!"
    show player 43
    player_name "..."
    return

label pa_announcement_21:
    show player 35b
    PA "Atenção Jogadores de basquete:"
    PA "Um jockstrap pequeno xtra xtra foi encontrado abandonado após o treino na noite passada."
    PA "Se o proprietário da dita cinta esportiva quiser recuperá-la, consulte o escritório principal o mais rápido possível.."
    PA "Obrigado e tenha um bom dia!"
    show player 43
    player_name "..."
    return

label pa_announcement_22:
    show player 35b
    PA "Atenção Estudantes:"
    PA "Este é um lembrete de que seus armários pessoais não são para armazenamento de alimentos."
    PA "Por favor, seja atencioso com os outros e limpe essas coisas repugnantes de vez em quando..."
    PA "Obrigado e tenha um bom dia!"
    show player 35
    player_name "..."
    return

label pa_announcement_23:
    show player 35b
    PA "Atenção Estudantes:"
    PA "Este é um lembrete de que o acesso ao telhado é estritamente proibido."
    PA "Quando perguntado sobre o assunto, {b}Diretora Smith{/b} comentou: 'Este não é o Japão, seus malditos...'"
    PA "Obrigado e tenha um bom dia!"
    show player 43
    player_name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
