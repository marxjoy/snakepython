import sys, pygame, random, math
pygame.init()

a=80
size = width, height = a*13, a*9

punkty=0
screenColor = 20, 250, 250

screen = pygame.display.set_mode(size)

class Apple:
    x=a
    y=a
    color=250,0,0
    def apear(self):
        self.x=random.randrange(0,width-a,a)
        self.y=random.randrange(0,height-a,a)
    def drawApple(self):
        appleRect = (self.x,self.y,a,a)
        pygame.draw.rect(screen,self.color, appleRect)

class Snake:
    x=0
    y=0
    speed = [0, 0]
    color = 0, 0, 0
    colorHead = 100,0,10
    body=[[x, y]]
    def drawSnake(self):
        snakeRect = (self.x,self.y,a,a)
        pygame.draw.rect(screen,self.colorHead, snakeRect)
        pom=[]
        new=[self.x, self.y]
        for i in range(0, len(self.body)):
            pom=self.body[i]
            self.body[i]=new
            new=pom
        for i in range(1, len(self.body)):
            snakeTailRect = (self.body[i][0],self.body[i][1],a,a)
            pygame.draw.rect(screen,self.color, snakeTailRect)

    def vector(self, n):
        if n==1:
            self.speed[1]=-a
            self.speed[0]=0
        if n==2:
            self.speed[0]=a
            self.speed[1]=0
        if n==3:
            self.speed[1]=a
            self.speed[0]=0
        if n==4:
            self.speed[0]=-a
            self.speed[1]=0
    def move(self):
        self.x+=self.speed[0]
        self.y+=self.speed[1]
        new=(self.x,self.y)

    def eat(self):
        self.body.append([self.x, self.y])

snake = Snake()
apple= Apple()

def checkCollision(snake, apple):
    tabX = [snake.x, apple.x]
    tabX.sort()
    tabY = [snake.y, apple.y]
    tabY.sort()
    return (tabX[1]-tabX[0] < a) and (tabY[1]-tabY[0] < a)

def checkWallCollision(snake):
    return (snake.x<=0-a) or (snake.x-a/2>=width) or (snake.y<=0-a) or (snake.y>=height)

def checkTailCollision(snake, tail):
    x=tail[0]
    y=tail[1]
    tabX = [snake.x, x]
    tabX.sort()
    tabY = [snake.y, y]
    tabY.sort()
    return (tabX[1]-tabX[0] < a) and (tabY[1]-tabY[0] < a)

def gameOver():
    gameOver=True

gameOver=False

while 1:
    screen.fill(screenColor)
    if (checkWallCollision(snake)):
        gameOver=True
    if (checkCollision(snake,apple)):
        punkty+=1
        apple.apear()
        snake.eat()

    snake.drawSnake()
    snake.move()

    for i in range(1,len(snake.body)):
        if checkTailCollision(snake, snake.body[i]):
            gameOver=True

    apple.drawApple()
    pygame.display.update()
    pygame.time.delay(180)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == (pygame.K_w):
                snake.vector(1)
            if event.key == (pygame.K_s):
                snake.vector(3)
            if event.key == (pygame.K_a):
                snake.vector(4)
            if event.key == (pygame.K_d):
                snake.vector(2)
            if event.key == (pygame.K_ESCAPE):
                sys.exit()

    if gameOver:
        while 1:
            font = pygame.font.SysFont("comicsansms", 72)
            content="Game Over: SCORE:  " + str(punkty)
            text = font.render(content, True, (0, 128, 0))
            screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == (pygame.K_ESCAPE):
                        sys.exit()
