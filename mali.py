import pygame

# 定义游戏的常量
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# 定义游戏的角色
class Mario(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("mario.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 100

    def update(self):
        # 处理玩家的输入
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # 检测是否撞到障碍物
        for brick in bricks:
            if self.rect.colliderect(brick.rect):
                self.kill()

# 定义游戏的场景
class Scene(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load("background.png")
        self.mario = Mario()
        bricks = []
        for i in range(0, SCREEN_WIDTH // 50):
            bricks.append(Brick(i * 50, 0))
        self.add(self.background)
        self.add(self.mario)
        self.add(*bricks)

    def update(self):
        self.mario.update()

# 定义游戏的循环
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    scene = Scene()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        scene.update()
        scene.draw(screen)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
