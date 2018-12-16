class Apple:

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x * 44
        self.y = y * 44

    def draw(self, surface, image):
        image.fill((255, 0, 0))
        surface.blit(image, (self.x, self.y))