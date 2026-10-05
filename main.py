import pygame
import random

pygame.init()

# Oyna
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚀 Samoviy O'yin")

clock = pygame.time.Clock()

# Ranglar
BLACK = (5, 5, 25)
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 60, 60)

# Font
font = pygame.font.SysFont("arial", 30)

# Kema
player = pygame.Rect(375, 500, 50, 60)
player_speed = 7

# Elektr o'qlari
bullets = []

# Asteroidlar
asteroids = []

score = 0
running = True
spawn_timer = 0


def draw_spaceship():
    """🚀 Kosmik kemani chizish"""

    # Kemaning tanasi
    pygame.draw.polygon(
        screen,
        BLUE,
        [
            (player.centerx, player.top),
            (player.left, player.bottom),
            (player.centerx, player.bottom - 15),
            (player.right, player.bottom)
        ]
    )

    # Oyna
    pygame.draw.circle(
        screen,
        CYAN,
        (player.centerx, player.top + 22),
        8
    )

    # 🔥 Dvigatel
    pygame.draw.polygon(
        screen,
        YELLOW,
        [
            (player.centerx - 8, player.bottom - 5),
            (player.centerx, player.bottom + 18),
            (player.centerx + 8, player.bottom - 5)
        ]
    )


def shoot():
    """⚡ Elektr toki otish"""

    x = player.centerx
    y = player.top

    bullet = {
        "x": x,
        "y": y,
        "length": 30
    }

    bullets.append(bullet)


def create_asteroid():
    x = random.randint(20, WIDTH - 20)

    asteroid = pygame.Rect(
        x - 20,
        -40,
        40,
        40
    )

    asteroids.append(asteroid)


while running:

    clock.tick(60)

    # Hodisalar
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # ⚡ SPACE
            if event.key == pygame.K_SPACE:
                shoot()

    # Klaviatura
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= player_speed

    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    # Ekrandan chiqib ketmasin
    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH

    # Asteroid yaratish
    spawn_timer += 1

    if spawn_timer > 35:
        create_asteroid()
        spawn_timer = 0

    # Elektr o'qlari
    for bullet in bullets[:]:

        bullet["y"] -= 12

        if bullet["y"] < 0:
            bullets.remove(bullet)

    # Asteroidlar
    for asteroid in asteroids[:]:

        asteroid.y += 4

        # Kema bilan urilish
        if asteroid.colliderect(player):

            running = False

        # Pastga chiqib ketsa
        if asteroid.top > HEIGHT:

            asteroids.remove(asteroid)

    # ⚡ Elektr o'qi asteroidga tegishi
    for bullet in bullets[:]:

        bullet_rect = pygame.Rect(
            bullet["x"] - 5,
            bullet["y"],
            10,
            bullet["length"]
        )

        for asteroid in asteroids[:]:

            if bullet_rect.colliderect(asteroid):

                if bullet in bullets:
                    bullets.remove(bullet)

                if asteroid in asteroids:
                    asteroids.remove(asteroid)

                score += 10

                break

    # Ekranni tozalash
    screen.fill(BLACK)

    # 🌟 Yulduzlar
    for i in range(80):

        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)

        pygame.draw.circle(
            screen,
            WHITE,
            (x, y),
            1
        )

    # ☄️ Asteroidlar
    for asteroid in asteroids:

        pygame.draw.circle(
            screen,
            RED,
            asteroid.center,
            20
        )

    # ⚡ ELEKTR TOKI
    for bullet in bullets:

        x = bullet["x"]
        y = bullet["y"]

        # Asosiy chaqmoq
        points = [
            (x, y),
            (x - 8, y + 10),
            (x + 5, y + 15),
            (x - 6, y + 25),
            (x, y + 30)
        ]

        pygame.draw.lines(
            screen,
            CYAN,
            False,
            points,
            5
        )

        # Yorqin markaz
        pygame.draw.lines(
            screen,
            WHITE,
            False,
            points,
            2
        )

    # 🚀 Kema
    draw_spaceship()

    # ⭐ Ball
    score_text = font.render(
        f"⭐ Ball: {score}",
        True,
        WHITE
    )

    screen.blit(
        score_text,
        (20, 20)
    )

    pygame.display.flip()


pygame.quit()
# ⚡ Elektr o'qi asteroidga tegishi
for bullet in bullets[:]:

    bullet_rect = pygame.Rect(
        bullet["x"] - 5,
        bullet["y"],
        10,
        bullet["length"]
    )

    for asteroid in asteroids[:]:

        if bullet_rect.colliderect(asteroid):

            if bullet in bullets:
                bullets.remove(bullet)

            if asteroid in asteroids:
                asteroids.remove(asteroid)

            score += 10

            break