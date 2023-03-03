import sys
import time
import pygame

ANCHO = 640
ALTO = 480
color_azul = (0, 0, 64) # color azul en rgb
color_blanco= (255, 255, 255)



class Escena:
    def __init__(self):
        "Inicialización"
        self.proximaEscena = False
        self.jugando = True

    def leer_evento(self,eventos):
        "Lee la lista de todos los eventos"
        pass
    def actualizar(self):
        "Calculos  logica"
        pass

    def dibujar(self, pantalla):
        "Dibuja los objetos en pantalla"
        pass

    def cambiar_escena(self, escena):
        "Selecciona la nuev escena a ser desplagada"
        self.proximaEscena = escena

class Director:
    def __init__(self, titulo = "", res = (ANCHO, ALTO)):
        pygame.init()
        # inicializando pantlla
        self.pantalla = pygame.display.set_mode(res)

        #Configurar titulo de la pantalla
        pygame.display.set_caption(titulo)
        #crear reloj
        self.reloj = pygame.time.Clock()
        self.escena = None
        self.escenas = {}

    def ejecutar(self, escena_inicial, fps = 60):
        self.escena = self.escenas[escena_inicial]
        jugando = True
        while jugando:
            self.reloj.tick(fps)
            eventos = pygame.event.get()
            #revisar todos los eventos
            for evento in eventos:
                # si se presiona la tachita de la barra del titulo
                if evento.type == pygame.QUIT:
                    # cerrar el videojuego
                    jugando = False
            
            self.escena.leer_eventos(eventos)
            self.escena.actualizar()
            self.escena.dibujar(self.pantalla)

            self.elegirEscena(self.escena.proximaEscena)

            if jugando:
                jugando = self.escena.jugando

            pygame.display.flip()
        
        time.sleep(3)
    
    def elegirEscenas(self, proximaEscena):
        if proximaEscena:
            if proximaEscena not in self.escenas:
                self.agregarEscena(proximaEscena)
            self.escena = self.escenas[proximaEscena]

    def agregarEscena(self, escena):
        escenaClase = "Escena"+escena
        escenaObj = globals()[escenaClase]
        self.escenas[escena] = escenaObj()


class Bolita(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # cargar imagen
        self.image = pygame.image.load("img/bolita.png")
        # Obtener rectanguki de ka imagen
        self.rect = self.image.get_rect()
        # posicion inicial centrada en pantalla
        self.rect.centerx = ANCHO/2
        self.rect.centery = ALTO/2
        # Establecer velocidad inicial
        self.speed =[3,3]

    def update(self):
        #evitar que salga por abajo y arriba
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        # Evitar que salga por la derecha e izquierda
        elif self.rect.right >= ANCHO or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        

        #mover en base actual y velocidad
        self.rect.move_ip(self.speed)


class Paleta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # cargar imagen
        self.image = pygame.image.load("img/paleta.png")
        self.rect = self.image.get_rect()
        # posicion inicial centrada en antalla en X
        self.rect.midbottom = (ANCHO /2, ALTO -20)

        # Establecer velocidad inicial
        self.speed =[0,0]
    
    def update(self, evento):
        # Buscar si se presiono flecha izquierda
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5, 0]
        # Buscar si se presiono flecha derecha
        elif evento.key == pygame.K_RIGHT and self.rect.right < ANCHO:
            self.speed = [5, 0]
        else:
            self.speed = [0, 0]
        
         #mover en base actual y velocidad
        self.rect.move_ip(self.speed)

class Ladrillo(pygame.sprite.Sprite):
    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        # cargar imagen
        self.image = pygame.image.load("img/ladrillo.png")
        # Obtener rectanguki de ka imagen
        self.rect = self.image.get_rect()
        # Posicion inicial, provista ecternamente
        self.rect.topleft = posicion

class Muro(pygame.sprite.Group):
    def __init__(self, cantidadLadrillos):
        pygame.sprite.Group.__init__(self)
        pos_x = 0
        pos_y = 20
        for i in range(cantidadLadrillos):
            ladrillo = Ladrillo((pos_x, pos_y))
            self.add(ladrillo)

            pos_x = pos_x + ladrillo.rect.width
            if pos_x >= ANCHO:
                pos_x = 0
                pos_y = pos_y + ladrillo.rect.height

# FUncion llamada tras dejar ir la bolita
def juego_terminado():
    fuente = pygame.font.SysFont("Arial", 72)
    texto = fuente.render("Juego terminado F", True,(255, 255, 255))
    texto_rect = texto.get_rect()
    texto_rect.center = [ANCHO / 2, ALTO / 2]
    pantalla.blit(texto, texto_rect)
    pygame.display.flip()

    # Pausar por tres segundos
    time.sleep(3)
    # Salir
    sys.exit()

def mostrar_puntuacion():
    fuente = pygame.font.SysFont("Consolas", 20)
    texto = fuente.render(str(puntuacion).zfill(5), True,(255, 255, 255))
    texto_rect = texto.get_rect()
    texto_rect.topleft = [0, 0]
    pantalla.blit(texto, texto_rect)

def mostrar_vidas():
    fuente = pygame.font.SysFont("Consolas", 20)
    cadena = "Vidas: " + str(vidas).zfill(2)
    texto = fuente.render(cadena, True, color_blanco)
    texto_rect = texto.get_rect()
    texto_rect.topright = [ANCHO, 0]
    pantalla.blit(texto, texto_rect)


# ajustar repeticion de evento de tecla presionada
pygame.key.set_repeat(30)

bolita = Bolita()
jugador = Paleta()
muro = Muro(50)
puntuacion = 0
vidas = 3
esperando_saque = True

while True:
    # Establecer FPS
    reloj.tick(60)

    
        
        # Buscar eventos del teclado
        elif evento.type == pygame.KEYDOWN:
            jugador.update(evento)
            if esperando_saque == True and evento.key == pygame.K_SPACE:
                esperando_saque = False
                if bolita.rect.centerx < ANCHO / 2:
                    bolita.speed = [3, -3]
                else:
                    bolita.speed = [-3, -3]    
    # actualizar la posicion de la bolita
    if esperando_saque == False:
        bolita.update()
    else:
        bolita.rect.midbottom = jugador.rect.midtop
    
    # colision entre bolita y jugador
    if pygame.sprite.collide_rect(bolita, jugador):
        bolita.speed[1] = -bolita.speed[1]

    # colision de la bolita con el muro
   
    lista =  pygame.sprite.spritecollide(bolita, muro, False)
    if lista:
        ladrillo = lista[0]
        cx = bolita.rect.centerx
        if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
            bolita.speed[0] = -bolita.speed[0]
        else:
            bolita.speed[1] = -bolita.speed[1]
        muro.remove(ladrillo)
        puntuacion = puntuacion + 10

    # revisar si la bolita sale de la oantalla
    if bolita.rect.top > ALTO:
        vidas = vidas - 1
        esperando_saque = True
    
    
   

    
    #rellenar la pantalla
    pantalla.fill(color_azul)
    # Mostrar puntuacion
    mostrar_puntuacion()
    # Mostrar vidas
    mostrar_vidas()
    # dibujar bolita en pantalla        
    pantalla.blit(bolita.image, bolita.rect)

    # Dibujar jugador en pantalla
    pantalla.blit(jugador.image, jugador.rect)
    # Dibujar los ladrillos
    muro.draw(pantalla)
    # actualizar elementos en pantalla
    pygame.display.flip()
    
    if vidas <= 0:
        juego_terminado()