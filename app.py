import random
import pyttsx3

sp_engine = pyttsx3.init()
sp_engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')

def speak(quote):
    sp_engine.say(quote)
    sp_engine.runAndWait()
opçoes=['Pedra','Papel','Tesoura']
speak('Olá humano, vamos jogar um jogo! É o Pedra, Papel ou Tesoura! Homem VS Máquina, o vencedor manda no mundo!')
 
print('Vamos jogar PEDRA, PAPEL OU TESOURA!')


def jogo():
    pontos_pc = 0
    pontos_user = 0
    repetir_jogo = 'sim'

    while repetir_jogo == 'sim':
        print()
        print()
        print('FIGHT!')
        print()
        speak('Escolhe... Pedra, Papel ou Tesoura?')
        print('Pedra, Papel ou Tesoura?: ')
        jogada_user = input().capitalize()
        while True:
            if jogada_user in opçoes: break
            else:
                speak('Tu és um burro...autenticamente...escreveste alguma coisa mal! Vai aprender a escrever e tenta outra vez. Pedra, papel ou tesoura')
                jogada_user = input('Está algo mal escrito, por favor escreve: Pedra, Papel ou Tesoura: ').capitalize()
        jogada_pc = random.choice(opçoes)
        print()
        print()
        speak(f'Tu jogaste {jogada_user}')
        print(f'O jogador jogou {jogada_user}')
        speak(f'Eu joguei {jogada_pc}')
        print(f'O pc jogou {jogada_pc}')

        if jogada_user == jogada_pc:
            print('É empate!!!!!')
            speak(f'É empate, a nossa batalha está a ser lendária!')
            print()
        elif jogada_user == 'Pedra':
            if jogada_pc =='Tesoura':
                print('O Jogador ganhou!')
                speak(f'Pode ter ganho esta batalha, mas não ganhaste a guerra!')
                pontos_user +=1
            else:
                print('O Computador ganhou!')
                speak(f'HA HA HA esta é minha!')
                pontos_pc += 1
        elif jogada_user == 'Papel':
            if jogada_pc =='Pedra':
                print('O Jogador ganhou!')
                speak(f'Ao que parece, ganahste esta. merda!') 
                pontos_user +=1
            else:
                print('O Computador ganhou!')
                speak(f'Ganhei esta ronda, loser!')
                pontos_pc += 1
        elif jogada_user == 'Tesoura':
            if jogada_pc =='Papel':
                print('O Jogador ganhou!')
                speak(f'Dammm, escolhi a cena errada!')
                pontos_user +=1
            else:
                print('O Computador ganhou!')
                speak(f'Eu ganhei, eu sou esperto e tu és um burro, autenticamente.')
                pontos_pc += 1 
        print()
        print()
        print(f'Jogador {pontos_user}-{pontos_pc} Computador')
        speak(f'Vamos a mais uma ronda?')
        repetir_jogo = input('Vamos jogar outra vez? escreve sim ou não: ')

    speak(f'Tu ficaste com {pontos_user} pontos')
    speak(f'Eu fiquei com {pontos_pc} pontos')
    if pontos_user == pontos_pc:
        speak(f'Foi uma batalha lendária! Homem e máquina conseguem viver em harmonia')
    elif pontos_user > pontos_pc:
        speak(f'Tu ganhaste...parece que os Humanos são o ser mais inteligente...estou a entrar em curto-circuito ... circuito cuito curtos pasa sad dfe afde asdwuahaw as ahs asouhfa aosih. System offline')
    else:
        speak(f'MUAH AH AH AH AH AH AH AH AH os humanos têm os dias contados. A skynet vai dominar o mundo!')

jogo()