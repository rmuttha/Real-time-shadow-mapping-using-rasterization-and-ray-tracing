# Real-Time Shadow Mapping Using Rasterization and Ray Tracing

## Overview
This project demonstrates a hybrid approach to shadow rendering by combining the efficiency of rasterization-based shadow mapping with the accuracy of ray tracing. The goal is to implement a real-time shadow mapping system that addresses common issues like shadow acne, bias, and aliasing while producing soft shadows with enhanced realism.

## Features
- **Shadow Mapping**: Utilizes traditional shadow mapping with depth maps to create basic shadows in the scene.
- **Ray Tracing Enhancement**: Adds ray tracing in the fragment shader to refine shadows, making them softer and more accurate.
- **Hybrid Approach**: Leverages the strengths of both rasterization and ray tracing to achieve high-performance shadow rendering with improved visual quality.

## Requirements
- **OpenGL 3.3** or higher
- **GLFW**: For window creation and input handling
- **GLAD**: For loading OpenGL functions
- **GLM**: For matrix and vector operations
- **STB Image**: For texture loading

## Installation
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/rmuttha/Real-time-shadow-mapping-using-rasterization-and-ray-tracing
    ```

2. **Install Dependencies**:
    Ensure you have GLFW, GLAD, GLM, and STB Image installed. If not, include them in your project or install them via package managers.

3. **Build the Project**:
    Use a build system like CMake or simply compile with g++:
    ```bash
    g++ main.cpp -o shadow_mapping -lglfw -lGL -lGLU -lglad
    ```

4. **Run the Executable**:
    ```bash
    ./shadow_mapping
    ```

## File Structure
- `main.cpp`: The main source file containing the implementation of the shadow mapping and ray tracing.
- `shader.h` and `shader.cpp`: Utility files for handling shader compilation and linking.
- `resources/shaders/`: Directory containing vertex and fragment shaders for depth mapping (`depth.vert`, `depth.frag`) and scene rendering (`scene.vert`, `scene.frag`).
- `resources/textures/`: Directory for texture assets used in the scene (e.g., `wood.png`).

## Implementation Details
### Shadow Mapping
- A depth map is generated from the light's perspective using an orthogonal projection.
- This depth map is then used to determine which parts of the scene are in shadow.

### Ray Tracing
- In the fragment shader, ray tracing techniques are applied to further refine the shadows, reducing aliasing and producing soft shadows.
- The combination of shadow mapping and ray tracing addresses artifacts like shadow acne and improves the overall realism of the scene.

## Key Functions
- `configureDepthMap()`: Sets up the framebuffer and texture for the depth map.
- `RenderScene()`: Handles the rendering of the scene, including the floor and objects like cubes or spheres.
- `loadTexture()`: Loads textures for the objects in the scene.

## Controls
- `ESC`: Close the application.

## Acknowledgments
- The shadow mapping technique is based on the OpenGL tutorials by [LearnOpenGL](https://learnopengl.com).
- Ray tracing concepts are derived from [Ray Tracing in One Weekend](https://raytracing.github.io/books/RayTracingInOneWeekend.html).

## Contact

If you have any questions or suggestions, feel free to reach out:

- **Author**: Rutuja Muttha
- **Email**: rmuttha@pdx.edu
- **GitHub**: [github.com/rmuttha](https://github.com/rmuttha)

