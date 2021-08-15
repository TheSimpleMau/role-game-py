#######################################
######By Mauricio Olguín Sánchez ######
#######################################

#############################################
#Primero, vamos a importar todo lo necesario#
#############################################

#Este modulo es para los personajes ascii que van apareciendo
import cowsay
#Este modulo nos permite medir el tiempo en el programa y poder "pausarlo"
import time
#Este nos permite importar la funcion system para poder limpiar la pantalla
import os
#Este modulo nos permite dar ese toque de aleatoriedad para las deciciones y caminos que se van a tomar
import random
#Por último, este modulo nos permite escribir letras con un formato de arte ascii
import art

###NOTA: Al incio del prorgama, se ejecutará en la terminal el comando 'sl', el cual hace que aparezca el tren.
#Por lo que habrá que instalar ese comando manualmente en tu terminal


###Las siguientes variables serán simplemente para añandir arte ascii al programa
CLOSE_CHEST = '''
                  .--------------------------------...
               ,'-------------------------------,'   |
              /                                /     |
             /________________________________/    ,'|
             |               ..               |  ,'  |
             |___________-==/88\==-___________|,' /) |.
             |  \    \     ((  ))     /    /  |  (/  |-. .
             |   \    \     \{}/     /    /   |    .' .  .
          . '|    \    \     )(     / _  /    |    ,   .  .
         . . |\    \    \    \/    _.( ~-.   /|\ ,' .   . .
       ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
        .  `    .     .       .  ,'\. ~-  . , .  .  .   .
           .  `   .     ,   .      , ~~-.' .  .    .
'''


OPEN_CHEST = r'''
                                        /\
                                        )(
                                       /{}\
                                      (    )
                         ,----------_____....----.--------,
                _____.....-----~~~~~             |_______/ `
               |                                 |      /  |
               |          H A Z                  |     /
               |                                 |   /   /
                |                                 | _/   /
                |            G A N A D O          |,'|~~
               ,|                                ,'  |
             ,'_|_____________________________:,' /) |.
             |  \    \                /    /  |  (/  |_. .
             |   \    \     {}       /    /   |    .' .  .
          . '|    \    \            / _  /    |    ,   .  .
         . . |\    \    \          _.( ~-.   /|\ ,' .   . .
       ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
        .  `    .     .       .  ,'\. ~-  . , .  .  .   .
           .  `   .     ,   .      , ~~-.' .  .    .
'''

NORMAL_CHEST = '''
      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
      ▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░██
      ▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░██
      ▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░██
      ▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░██
      ▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░██
      ▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░██
      ▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░██
      ▓▓░░▒▒▒▒▒▒▒▒░░▓▓░░░░▓▓▒▒░░▒▒░░░░▒▒░░██
    ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒
░░▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒
░░▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒
░░▒▒▒▒▓▓░░▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓░░▓▓▒▒▒▒
░░▒▒▒▒▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░▓▓▒▒▒▒
░░▒▒▒▒▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▒▒▒▒
░░▒▒▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒▒▒
░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒
░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
  ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
'''


NUCLEAR_EXPLOSION = r'''
          _ ._  _ , _ ._
        (_ ' ( `  )_  .__)
      ( (  (    )   `)  ) _)
     (__ (_   (_ . _) _) ,__)
         `~~`\ ' . /`~~`
              ;   ;
              /   \
_____________/_ __ \_____________'''


KEY_LOCK = r'''
     .--------.
    / .------. \
   / /        \ \
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  | YALE |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'
'''


PAD_LOCK = '''
|-------|
| 1 2 3 |
| 5 6 7 |
| 8 9 0 | 
|_______|
'''


STAIRS = '''
              A. S U B I R                                 B. B A J A R
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa,                            []
8                           8"b,    "Ya                          []
8                           8  "b,    "Ya                        []
8                    aaaaaaa8,   "b,    "Ya                      []
8                    8"b,    "Ya   "8""""""8                     []
8                    8  "b,    "Ya  8      8                     []
8             aaaaaaa8,   "b,    "Ya8      8    _______________  []         _________________
8             8"b,    "Ya   "8"""""""      8    _______________) []        (_______________
8             8  "b,    "Ya  8             8     !     !     !   []        '  !     !     !
8      aaaaaa88,   "b,    "Ya8             8     !     !     !   []       ,!  !     !     !
8      8"b,    "Ya   "8"""""""             8     !     !     !   []      ! !  !     !     !
8      8  "b,    "Ya  8                    8     !_____!_____!___[]_____'!_!__!_____!_____!_____
8aaaaaa8,   "b,    "Ya8                    8                     []__,_!_!_!
8"b,    "Ya   "8"""""""                    8                     []_!__!_!|
8  "b,    "Ya  8                           8                    ,[]_!__!_!
8,   "b,    "Ya8                           8                  ,! []_!__!|
"Ya   "8"""""""                           8                 ,! ! []_!__!
"Ya  8                                  8                  ! ! ! []_!|
    "Ya8                                  8               !! ! !|[]_|
    """""""""""""""""""""""""""""""""""""                 !!!._|_[]
                                                          !!!|!_.[]
                                                          !|!_!__[]!.
                                                          !_!_!__[]! !.
                                                          !_!_!__[]! ! `.
                                                           |!_!__|]! ! ! `.
                                                            |_!__|]! ! ! ! `.
                                                              |____|_! ! ! !  `
                                                                |____|_! ! ! !
                                                                 []____|_! ! !
                                                                 []______|_! !
                                                                 []________|_!
                                               __________________[]__________|____________________
'''


DOORS = '''
            __________               __________
           |  __  __  |             |  __  __  |
           | |  ||  | |             | |  ||  | | 
           | |  ||  | |             | |  ||  | | 
           | |__||__| |             | |__||__| | 
           |()__  __  |             | |__  __()|
           | |  ||  | |             | |  ||  | | 
           | |  ||  | |             | |  ||  | | 
           | |  ||  | |             | |  ||  | | 
           | |  ||  | |             | |  ||  | | 
           | |__||__| |             | |__||__| | 
           |__________|             |__________| 
            IZQUIERDA                 DERECHA
'''


CASTEL = '''
                             -|             |-
         -|                  [-_-_-_-_-_-_-_-]                  |-
         [-_-_-_-_-]          |             |          [-_-_-_-_-]
          | o   o |           [  0   0   0  ]           | o   o |
           |     |    -|       |           |       |-    |     |
           |     |_-___-___-___-|         |-___-___-___-_|     |
           |  o  ]              [    0    ]              [  o  |
           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________
_____----- |     ]              [ ||||||| ]              [     |
           |     ]              [ ||||||| ]              [     |
       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_
      ( (__________------------_____________-------------_________) )
'''

LETTERS = [
'''
Ⓐ .\n
''',
'''
Ⓑ .\n
''',
'''
Ⓒ .\n
'''
]


WALL_SECRET = '''
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|____|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|____|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_____|___|___|_____|____|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__|___|___|___|___|___|___|___|_____|___|___|__
_|___|__|__.   .-. .-.   .   .-. .-. .-. .-. .-.   .-. .-. .-. . . .-. . .   . . . . .  . .-. .-. .-. .-.|___|___|_
_|___|__|__|   |-| `-.   |   |-   |  |(  |-| `-.    |   |  |-  |\| |-  |\|   |\| | | |\/| |-  |(  | | `-. ___|___|_
_|___|__|__`-' ` ' `-'   `-' `-'  '  ' ' ` ' `-'    '  `-' `-' ' ` `-' ' `   ' ` `-' '  ` `-' ' ' `-' `-'|___|___|_
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|____|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|____|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_____|___|___|_____|____|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__|___|___|___|___|___|___|___|_____|___|___|__
'''


WALL_WITHOUT_SECRET = '''
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|____|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|____|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_____|___|___|_____|____|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__|___|___|___|___|___|___|___|_____|___|___|__
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|____|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|____|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_____|___|___|_____|____|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__|___|___|___|___|___|___|___|_____|___|___|__
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|____|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|____|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_____|___|___|_____|____|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__|___|___|___|___|___|___|___|_____|___|___|__
'''



############################################################
######Ahora, vamos a definir las funciones necesarias######
############################################################

#Esta primer función nos  ayudará a darle establecer la "dificultad" del juego.
#Aunque en realidad solo es establecer que porcentaje aumentará teniendo en cuenta una porcentaje aleatorio
def dificulty():
    os.system('clear')
    cowsay.cow('Antes de empezar con el juego, dime, en una escala del 1 al 3. Qué tan suertudo te sientes?')
    print('''
1 = Con mucha suerte pa, venga daleee 😁
2 = Ni bien ni mal, como Bad Bunny 😑
3 = Hoy es un mal día 😩
''')
    try:
        lucky = int(input('\n Hoy me siento... : '))
    except ValueError:
        print('Valor no valido >:|\nVuelve ejecutar el programa.')
        exit()
    if lucky == 1:
        return 0.2
    elif lucky == 2:
        return 0.15
    elif lucky == 3:
        return 0.1
    else:
        print('EValor no valido >:|\nVuelve ejecutar el programa.')
        exit()


#Esta función si que nos va a decir que tanta "suerte" vas a tener durante el juego.
#Es decir, esta función la utilizaremos para las secciones en donde tengamos una situación de aleatoriedad
def lucky_percentage(lucky:float)->float:
    return random.random()+lucky


#Ahora, vamos a hacer nuestra primera sección del juego, esta es el primer acetijo que se nos presenta en el juego (tomando en cuenta que iniciamos en el lado izquierdo)
def acertijo_uno():
    os.system('clear')
    cowsay.trex('Un caballo blanco entró en el Mar Negro. Cómo salió?')
    print(f'''OPCIONES:
{LETTERS[0]} Mojado.
{LETTERS[1]} Negro.
{LETTERS[2]} Los caballos no pueden nadar.''')
    answer = str(input('\n Mi resupuesta es: ')).lower()
    if answer == 'a':
        return 1
    else:
        return 0


#Este es el segundo acertijo, este acertijo se nos aparecerá cuando estemos al final del juego
def acertijo_dos():
    os.system('clear')
    cowsay.stegosaurus('Sabes de alguna letrita, que si la vuelta le das, enseguida se convierte de consonante en vocal?')
    print(f'''OPCIONES:
{LETTERS[0]} La letra o
{LETTERS[1]} La letra n
{LETTERS[2]} La letra m''')
    answer = str(input('\n Mi respuesta es: ')).lower()
    if answer == 'b':
        return 1
    else:
        return 0


#Por último, este acertijo es el que se nos aparece si es 
# que el anterior no aparece, de igual manera, al final del juego
def acertijo_tres():
    os.system('clear')
    cowsay.stegosaurus('Qué es lo que produce la siguiente sentencia en Python?')
    print('''a = '1'
b = '2'
print(a+b)\n\n''')
    print(f'''OPCIONES:
{LETTERS[0]} 3
{LETTERS[1]} 12
{LETTERS[2]} ValueError''')
    answer = str(input('\n Mi respuesta es: ')).lower()
    if answer == 'b':
        return 1
    else:
        return 0


#Esta funcion nos sirve para cuando tenemos el caso de que fallamos algún acertijo.
def golpear(lucky):
    os.system('clear')
    percentage = lucky_percentage(lucky)
    os.system('clear')
    cowsay.kitty('Lo siento, pero haz fallado, te llevaré al calabozo')
    print(f'''QUÉ HARAS?
{LETTERS[0]} Rendirte
{LETTERS[1]} Golpearlo y huir''')
    answer = str(input('Mi respuesta es: ')).lower()
    if answer == 'b':
        if percentage >= 0.9:
            return 1
        else:
            return 0.5
    else:
        return 0


#Ahora, esta función engloba los dos posibles acertijos que nos pueden aparecer al final 
# del juego cuando escogemos o simplemente entramos por la puerta que necesita una llave
def puerta_llave(lucky):
    percentage = lucky_percentage(lucky)
    os.system('clear')
    if percentage > 0.5:
        answer = acertijo_dos()
    elif percentage < 0.5:
        answer = acertijo_tres()
    if answer == 1:
        return 1
    else:
        return 0


#Esta función engloba también lo que puede pasar en caso de que escogamos o simplemente
#solo podamos pasar por esta puerta.
def puerta_numero(lucky):
    os.system('clear')
    percentage = lucky_percentage(lucky)
    if percentage < 0.95:
        print('Analizando un poco, te acuerdas de la frase que había en la pared y te perguntas')
        print('Cuántos letras tenía la frase?')
        answer = int(input('\n La frase tenia: '))
        if answer == len('LASLETRASTIENENNÚMEROS'):
            return 1
        else:
            return 0
    else:
        os.system('clear')
        print('''Abres la puerta, ves el cofre, es E N O R M E, así que corres por el.
Y justo en el momento en cuando lo vas a abrir... tu mamá te despierta.''')
        art.tprint('GAME OVER')
        exit()
        

#Y por último, esta funcion, dependiendo de lo que tengas, es decir, si obtuviste la llave,
#pasaste por la frase o incluso si no tienes nigúna, las opciones que se te pueden presentar
#en cada caso.
def dos_puertas(key_door,wall_phrase,lucky):
    os.system('clear')
    print('Ahora, tienes en frente dos puertas, una necesita una llave para abrirse, la otro un código con números...')
    time.sleep(5)
    if key_door == 1 and  wall_phrase == 1:
        print(f'''Que puerta quieres tomar?
{LETTERS[0]} Puerta con llave
{KEY_LOCK}
{LETTERS[1]} Puerta con números
{PAD_LOCK}
''')
        answer = str(input('\n Tomaré la puerta: ')).lower()
        if answer == 'a':
            answer_2 = puerta_llave(lucky)
            if answer_2 == 1:
                os.system('clear')
                print('Correcto. Te deja pasar el guardia y... Ahí esta el cofre!!!')
                print(OPEN_CHEST)
                exit()
            else:
                answer_3 = golpear(lucky)
                if answer_3 == 1:
                    os.system('clear')
                    print('Noqueas al guardia y... Haz encontrado el cofre!!!')
                    print(OPEN_CHEST)
                    exit()
                else:
                    os.system('clear')
                    cowsay.kitty('No hubieras hecho eso')
                    print(art.text2art('El gato saca una pistola y te balacea'))
                    art.tprint('GAME OVER')
        else:
            answer_2 = puerta_numero(lucky)
            if answer_2 == 1:
                os.system('clear')
                print('Correcto, te deja pasar el guardia y... Ahí esta el cofre!!!')
                print(OPEN_CHEST)
                exit()
            else:
                answer_3 = golpear(lucky)
                if answer_3 == 1:
                    os.system('clear')
                    print('Noqueas al guardia y... Haz encontrado el cofre!!!')
                    print(OPEN_CHEST)
                    exit()
                else:
                    os.system('clear')
                    cowsay.kitty('Eso no es de chavitos bien eh')
                    print('El gato le pide a su guarura que te de una madrinita')
                    art.tprint('GAME OVER')
                    exit()
    elif key_door == 1 and wall_phrase == 0:
        print('Como solo tienes una llave, decides abrir esa puerta y...')
        print(KEY_LOCK)
        time.sleep(5)
        answer_2 = puerta_llave(lucky)
        if answer_2 == 1:
            os.system('clear')
            print('Correcto. Te deja pasar el guardia y... Ahí esta el cofre!!!')
            print(OPEN_CHEST)
            exit()
        else:
            answer_3 = golpear(lucky)
            if answer_3 == 1:
                os.system('clear')
                print('Noqueas al guardia y... Haz encontrado el cofre!!!')
                print(OPEN_CHEST)
                exit()
            else:
                os.system('clear')
                cowsay.kitty('Noooo!!! le diste al boton')
                cowsay.tux('Boton?')
                time.sleep(7)
                os.system('clear')
                print(NUCLEAR_EXPLOSION)
                art.tprint('GAME OVER')
                exit()
    elif key_door == 0 and wall_phrase == 1:
        print('Como no tienes una llave, intentas con la puerta que necesita un número y...')
        print(PAD_LOCK)
        time.sleep(5)
        answer_2 = puerta_numero(lucky)
        if answer_2 == 1:
            print('Correcto, te deja pasar el guardia y... Ahí esta el cofre!!!')
            print(OPEN_CHEST)
            exit()
        else:
            answer_3 = golpear(lucky)
            if answer_3 == 1:
                os.system('clear')
                print('Noqueas al guardia y... Haz encontrado el cofre!!!')
                print(OPEN_CHEST)
                exit()
            else:
                os.system('clear')
                cowsay.kitty('No hubieras hecho eso bro')
                print('El gato saca un interruptor y...')
                time.sleep(10)
                print(NUCLEAR_EXPLOSION)
                art.tprint('GAME OVER')
                exit()
    elif key_door == 0 and wall_phrase == 0:
        print('Como no conces el número para la puerta y tampóco tienes una llave, no hay forma de pasar...')
        time.sleep(5)
        os.system('clear')
        cowsay.turkey('Vaya que haz tenido muy mala suerte (y es probable que muy malos caminos)')
        art.tprint('GAME OVER')
        exit()


#Ahora, vamos a pasar a todos los caminos que se 
#puede seguir si es que llegamos a la parte de la sala de cofres.
def sala_cofres(lucky):
    os.system('clear')
    print('Cuando entras al sotano, vez que es una sala llena de cofres... pero de los normales, no el que buscas.')
    print(f'''Así que se te ocurren dos ideas, revisar solo un cofre aleatoriamente y ver si tiene algo adentro y después regresar
o puedes revisar todos los cofres para ver si es que encuentras algo mejor, pero eso solo hará que pierdas el tiempo y tengar que 
irte del castillo sin el cofre que buscas.
Así que, al final te decides por...
{LETTERS[0]} Revisar un cofre y regrasar
{LETTERS[1]} Revisar todos los cofres e irte del castillo
{NORMAL_CHEST}''')
    answer = str(input('\n Mi elección es: ')).lower()
    if answer == 'a':
        percentage = lucky_percentage(lucky)
        if percentage < 0.7:
            print(f'Abres el cofre número {random.randint(1,1001)} (sin saber que ese era el número del cofre) y te das cuenta que hay una llave adentro')
            print('Tal vez pueda que esa llave nos sirva despues...')
            time.sleep(10)
            return 1
        else:
            print(f'Abres el cofre número {random.randint(1,1001)} (sin saber que ese era el número del cofre) y no encuentras nada :/')
            print('Sin perder más tiempo, sales de esa sala y regresas al para subir las otras escaleras')
            time.sleep(10)
            return 0
    elif answer == 'b':
        print(f'''Empiezas a abrir cofres, uno a uno, pero en el
cofre número {random.randint(1,1001)} empieza a sonar algo y...''')
        time.sleep(6)
        os.system('clear')
        print(NUCLEAR_EXPLOSION)
        art.tprint('GAME OVER')
        exit()

#Por último, un paso antes de la sala de cofres, hay que escoger si vamos a bajar o subir las escaleras.
#Entonces, aquí hay que revisar simplemente que decición tomará el usuario, esto para que en la función
#donde tengamos el juego completo no sea tan larga.
def camino_up_down(lucky):
    os.system('clear')
    print('Ahora, vez que hay dos caminos, uno que sube y otro que baja, tal vez a un sotano, así que decides...')
    print(f'''
{STAIRS}''')
    way = str(input('\n Mi camino será: ')).lower()
    if way == 'a':
        return 0
    if way == 'b':
        sala = sala_cofres(lucky)
        if sala == 1:
            return 1
        else:
            return 0

###################################
######Comienzo de la historia######
###################################

#Esta función es solo para que, nuevamente, 
#no tengamos tanto código en nuestra función principal del juego.
#La función lo que hace es simplemente 
#una pequeña historia introductoria al juego
def begin_story():
    os.system('clear')
    cowsay.cow('Este juego se basa en tomar desciones... y de tu suerte. Así que SUERTE!!!')
    time.sleep(5)
    os.system('clear')
    os.system('sl -l')
    os.system('clear')
    cowsay.tux('Por fin llego al castillo')
    time.sleep(5)
    os.system('clear')
    print(CASTEL)
    time.sleep(3)
    os.system('clear')
    cowsay.tux('Ahí esta el tesóro')
    time.sleep(4)
    os.system('clear')
    print(CLOSE_CHEST)
    time.sleep(3)
    os.system('clear')
    cowsay.daemon('ALTO AHÍ!!!')
    time.sleep(4)
    os.system('clear')
    cowsay.daemon('Yo se que lo que quieres es el tesoro, pero no será tan fácil')
    time.sleep(4)
    os.system('clear')
    cowsay.daemon('Tendrás que escojer un camino y de ahí, tu suerte lo decidrá')
    time.sleep(4)

#########################################
######Ahora sí, el inicio del juego######
#########################################

#Esta es la función principal, donde estarán todas las otras funciónes
#que definimos. Esto nos ayudará para que, el camino a seguia el jugador
#pueda ser fácil de implementar y además también se puedan escojer diferentes
#caminos y podamos ganar.
#Por poner un ejemplo, si escogemos el camino de la derecha, podría ser que obtengamos
#la frase, y digammos que también bajamos al sotano. Entonces, tendríamos que ir
#guardando esos datos, en algún lugar. Es por eso que tenemos algunas variables inicales y
#que con el pasar de las deciciones y casos que se van presentando, se vaya guardadndo.
def game():
    lucky = dificulty()
    try:
        begin_story()
    except KeyboardInterrupt:
        pass
    key_door = 0
    wall_phrase = 0
    os.system('clear')
    cowsay.daemon('Así que... cual sera tu camino Por la izquierda o la derecha?')
    print(DOORS)
    easter_egg_1 = time.time()
    way = str(input('\n Mi camino será por la: '))
    easter_egg_2 = time.time()
    if easter_egg_2-easter_egg_1 >= 60:
        os.system('clear')
        time.sleep(1.5)
        cowsay.daemon('Sabes que, dejalo así mejor carnal, me caiste bien, pasale directo al cofre')
        time.sleep(6)
        os.system('clear')
        print(OPEN_CHEST)
        cowsay.tux('Eso fue demasiado fácil... ha decir verdad')
        exit()
    else:
        pass
    if way == 'derecha':
        os.system('clear')
        percentage = lucky_percentage(lucky)
        time.sleep(1.5)
        print('Camina por un pasillo muy muy largo... demasiado largo a decir verdad')
        time.sleep(5)
        if percentage > 0.6:
            print('Y no pasa nada...')
            time.sleep(5)
            key_door = camino_up_down(lucky)
            time.sleep(1.5)
            dos_puertas(key_door,wall_phrase,lucky)
        else:
            percentage = lucky_percentage(lucky)
            if percentage > 0.5:
                print('Pero de repente, ves que en la pared esta escrito lo siguiente:')
                print(WALL_SECRET)
                print("Piensas 'hmm, esto P U E D E que sea un pista'... ")
                wall_phrase = 1
                time.sleep(15)
                key_door = camino_up_down(lucky)
                dos_puertas(key_door,wall_phrase,lucky)
            else:
                print('Y la pared parece que la acaban de lavar...')
                print(WALL_WITHOUT_SECRET)
                time.sleep(7)
                key_door = camino_up_down(lucky)
                dos_puertas(key_door,wall_phrase,lucky)
    elif way == 'izquierda':
        os.system('clear')
        time.sleep(1.5)
        percentage = lucky_percentage(lucky)
        if percentage < 0.6:
            time.sleep(1.5)
            answer = acertijo_uno()
            if answer == 1:
                key_door = camino_up_down(lucky)
                time.sleep(1.5)
                dos_puertas(key_door,wall_phrase,lucky)
            else:
                time.sleep(1.5)
                answer_two = golpear(lucky)
                if answer_two == 1:
                    time.sleep(1.5)
                    key_door = camino_up_down(lucky)
                    time.sleep(1.5)
                    dos_puertas(key_door,wall_phrase,lucky)
                elif answer_two == 0.5:
                    time.sleep(1.5)
                    cowsay.kitty('No hubieras hecho eso bro')
                    print('El gato saca un filero y te mata')
                    art.tprint('GAME OVER')
                    exit()
                elif answer == 0:
                    time.sleep(1.5)
                    cowsay.kitty('En verdad te voy a comer')
                    print(art.text2art('El gato te muerde una pierna y te traga'))
                    art.tprint('GAME OVER')
                    exit()
        else:
            key_door = camino_up_down(lucky)
            time.sleep(1.5)
            dos_puertas(key_door,wall_phrase,lucky)
    else:
        print('Valor no valido >:|\nVuelve ejecutar el programa.')


#Al final, solo tendrémos que poner nuestro entry point, por si es que queremos exportar
#este juego a otro programa y no tengamos errores.
if __name__ == '__main__':
    game()