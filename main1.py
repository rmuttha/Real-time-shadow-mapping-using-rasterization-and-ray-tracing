# Author: Rutuja Muttha
# Project: PROCEDURAL GENERATION WITH RAY TRACING

import numpy as np
import random
from PIL import Image

# Constants
WIDTH, HEIGHT = 800, 600
FOV = np.pi / 3
MAX_DEPTH = 5

# Vector operations
def normalize(v):
    return v / np.linalg.norm(v)

def reflect(I, N):
    return I - 2 * np.dot(I, N) * N

def sphere_intersect(center, radius, ray_origin, ray_dir):
    b = 2 * np.dot(ray_dir, ray_origin - center)
    c = np.linalg.norm(ray_origin - center)**2 - radius**2
    discriminant = b**2 - 4*c
    if discriminant < 0:
        return False, None
    t1 = (-b + np.sqrt(discriminant)) / 2
    t2 = (-b - np.sqrt(discriminant)) / 2
    if t1 > 0 and t2 > 0:
        return True, min(t1, t2)
    return False, None

# Scene Setup
def generate_scene(num_spheres=10):
    spheres = []
    for _ in range(num_spheres):
        center = np.array([random.uniform(-5, 5), random.uniform(0, 5), random.uniform(5, 15)])
        radius = random.uniform(0.5, 1.5)
        color = np.random.rand(3)
        spheres.append((center, radius, color))
    return spheres

# Ray tracing
def trace_ray(ray_origin, ray_dir, spheres, depth=0):
    if depth >= MAX_DEPTH:
        return np.array([0, 0, 0])

    nearest_t = np.inf
    hit_obj = None
    hit_point = None
    normal_at_hit = None

    for center, radius, color in spheres:
        hit, t = sphere_intersect(center, radius, ray_origin, ray_dir)
        if hit and t < nearest_t:
            nearest_t = t
            hit_obj = (center, radius, color)
            hit_point = ray_origin + ray_dir * t
            normal_at_hit = normalize(hit_point - center)

    if hit_obj is None:
        return np.array([0.2, 0.7, 1.0])  # Background color

    center, radius, color = hit_obj
    reflection_dir = reflect(ray_dir, normal_at_hit)
    reflection_color = trace_ray(hit_point + normal_at_hit * 1e-5, reflection_dir, spheres, depth + 1)
    
    return color * 0.8 + reflection_color * 0.2

# Main rendering loop
def render(spheres):
    aspect_ratio = WIDTH / HEIGHT
    screen = np.zeros((HEIGHT, WIDTH, 3))

    for y in range(HEIGHT):
        for x in range(WIDTH):
            px = (2 * (x + 0.5) / WIDTH - 1) * np.tan(FOV / 2) * aspect_ratio
            py = (1 - 2 * (y + 0.5) / HEIGHT) * np.tan(FOV / 2)
            ray_dir = normalize(np.array([px, py, -1]))
            screen[y, x] = np.clip(trace_ray(np.array([0, 0, 0]), ray_dir, spheres), 0, 1)
    
    return screen

# Procedural generation of the scene
spheres = generate_scene()

# Render the image
image = render(spheres)
image = (image * 255).astype(np.uint8)
img = Image.fromarray(image)
img.show()
