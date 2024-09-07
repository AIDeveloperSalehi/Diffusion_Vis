# Diffusion Model Visualization Project

This project provides a visual representation of the concepts behind diffusion models, including both discrete and continuous processes. It generates artificial animations to illustrate how diffusion models work in graph structures and images. The generated animations are not exact output of the diffusion model and artificiall discrete and continuous noise are added to generative part of graph or image. The content is for the following post:


## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [File Descriptions](#file-descriptions)
5. [Theory](#theory)
6. [Applications](#applications)
7. [Contributing](#contributing)
8. [License](#license)

## Overview

This project consists of three main components:

1. Graph Animation: Visualizes the diffusion process in a graph structure.
2. Image Animation: Demonstrates the continuous diffusion process in an image.
3. GIF Combiner: Merges the graph and image animations into a single GIF for easy comparison.

The resulting animation serves as an educational tool to understand the principles of diffusion models in machine learning.

## Installation

To run this project, you need Python 3.7+ and the following libraries:

```
pip install networkx matplotlib pillow numpy
```

## Usage

1. Generate the graph animation:
   ```
   python graph_animation.py
   ```

2. Generate the image animation:
   ```
   python image_animation.py --image path/to/your/image.jpg --x0 2400 --y0 1000 --width 1000 --height 1000
   ```

3. Combine the animations:
   ```
   python combine_gifs.py
   ```

The final output will be a file named `combined_animation.gif` in your project directory.

## File Descriptions

- `graph_animation.py`: Creates a GIF showing the diffusion process in a graph structure.
- `image_animation.py`: Generates a GIF demonstrating image diffusion.
- `combine_gifs.py`: Merges the two animations into a single GIF.
- `requirements.txt`: Lists all Python libraries that your project depends on.

## Theory

This project visualizes two key concepts in diffusion models:

1. Discrete Diffusion (Graph Animation):
   - Represents the step-by-step denoising process for conditional diffusion.
   - The red nodes show a fixed subgraph, while blue nodes demonstrate the changing connections.

2. Continuous Diffusion (Image Animation):
   - Illustrates the gradual transformation from noise to a clear image.
   - A fixed portion of the image remains constant to show the conditioning process.

## Applications

Diffusion models have various applications, including:

- Text-to-image generation
- Image inpainting and restoration
- Style transfer
- Drug discovery
- Audio generation

This visualization helps in understanding how these models can be applied in different domains.

## Contributing

Contributions to improve the animations or extend the project are welcome. Please feel free to submit a pull request or open an issue.

