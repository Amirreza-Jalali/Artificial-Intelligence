import numpy as np

class Boid:
    def init(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def cohesion(self, boids):
        perception_radius = 100
        steering = np.zeros(2)
        total_neighbors = 0
        for boid in boids:
            distance = np.linalg.norm(self.position - boid.position)
            if boid != self and distance < perception_radius:
                steering += boid.position
                total_neighbors += 1
        if total_neighbors > 0:
            steering /= total_neighbors
            steering = (steering - self.position) / 100
        return steering

    def alignment(self, boids):
        perception_radius = 100
        steering = np.zeros(2)
        total_neighbors = 0
        for boid in boids:
            distance = np.linalg.norm(self.position - boid.position)
            if boid != self and distance < perception_radius:
                steering += boid.velocity
                total_neighbors += 1
        if total_neighbors > 0:
            steering /= total_neighbors
            steering = (steering - self.velocity) / 8
        return steering

    def separation(self, boids):
        perception_radius = 50
        steering = np.zeros(2)
        total_neighbors = 0
        for boid in boids:
            distance = np.linalg.norm(self.position - boid.position)
            if boid != self and distance < perception_radius:
                diff = self.position - boid.position
                steering += diff / distance
                total_neighbors += 1
        if total_neighbors > 0:
            steering /= total_neighbors
        return steering

    def update(self, boids):
        cohesion_force = self.cohesion(boids)
        alignment_force = self.alignment(boids)
        separation_force = self.separation(boids)
        
        # تعیین سرعت جدید بر اساس نیروهای محاسبه شده
        acceleration = cohesion_force + alignment_force + separation_force
        self.velocity += acceleration
        self.position += self.velocity

def main():
    num_boids = 50
    boids = []
    for _ in range(num_boids):
        position = np.random.rand(2) * 200 - 100
        velocity = np.random.rand(2) * 2 - 1
        boid = Boid(position, velocity)
        boids.append(boid)

    num_iterations = 100

    for _ in range(num_iterations):
        for boid in boids:
            boid.update(boids)

        # نمایش موقعیت دلفین‌ها
        for boid in boids:
            print(boid.position)

if name == 'main':
    main()

    