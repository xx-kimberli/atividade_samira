import random

WIDTH = 800
HEIGHT = 600
TITLE = "Desvio Espacial"

nave = Actor('nave')
nave.pos = (WIDTH // 2, HEIGHT - 50)

meteoro = Actor('meteoro')
meteoro.x = random.randint(20, WIDTH - 20)
meteoro.y = 0

pontos = 0
fim_de_jogo = False

def draw():
    screen.clear()
    screen.fill((10, 10, 30))
    
    if not fim_de_jogo:
        nave.draw()
        meteoro.draw()
        screen.draw.text(f"Pontos: {pontos}", (20, 20), color="white", fontsize=30)
    else:
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2), color="red", fontsize=60)
        screen.draw.text(f"Pontuação Final: {pontos}", center=(WIDTH // 2, HEIGHT // 2 + 50), color="white", fontsize=30)

def update():
    global pontos, fim_de_jogo
    
    if fim_de_jogo:
        return

    velocidade_meteoro = 5 + (pontos // 5)
    meteoro.y += velocidade_meteoro

    if meteoro.top > HEIGHT:
        pontos += 1
        meteoro.x = random.randint(20, WIDTH - 20)
        meteoro.y = -50

    if nave.colliderect(meteoro):
        fim_de_jogo = True

def on_mouse_move(pos):
    if not fim_de_jogo:
        nave.x = pos
