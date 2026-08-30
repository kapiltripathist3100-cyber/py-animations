
# py-animations
```markdown

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A curated collection of modular, production-ready Python animations, visualizations, and procedural graphic generators. 

`py-animations` provides standalone scripts and reusable utilities for rendering mathematical concepts, algorithmic simulations, physics models, and terminal UI graphics.
```
---

## Features
```markdown
* **Algorithmic Visualizations:** Real-time visual representations of common sorting, pathfinding, and graph traversal algorithms.
* **Physics & Simulations:** Particle systems, n-body gravitational simulations, wave propagation, and cellular automata.
* **Mathematical Art:** Parametric curves, fractals (Mandelbrot, Julia sets), and generative geometry.
* **Multiple Output Engines:** Scripts supporting rendering via **Manim**, **Matplotlib**, **Pygame**, **Pillow (GIF generation)**, and **Terminal (Curses/Rich)**.
* **Zero Bloat:** Each animation module is self-contained with minimal external dependencies.
```
---

## Repository Structure
```markdown
```text
py-animations/
├── algorithms/       # Sorting, pathfinding, and tree traversal visualizers
├── math_art/         # Fractals, parametric equations, and geometric patterns
├── physics/          # Fluid dynamics, spring-mass systems, gravity simulations
├── terminal/         # ASCII art, CLI spinners, and terminal-based animations
├── assets/           # Sample outputs (GIFs, MP4s, static renders)
├── requirements.txt  # Core dependencies
└── README.md

```

---

## Quick Start

### Prerequisites

Ensure you have Python 3.8 or higher installed. If rendering vector or mathematical animations, ensure system-level dependencies (such as `ffmpeg` or `cairo`) are installed.

### Installation

1. **Clone the repository:**
```bash
git clone [https://github.com/your-username/py-animations.git](https://github.com/your-username/py-animations.git)
cd py-animations

```


2. **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```



---

## Usage Examples

### 1. Run a Sorting Algorithm Visualizer (Pygame / Matplotlib)

```bash
python algorithms/bubble_sort_visualizer.py --speed fast --elements 100

```

### 2. Generate a Fractal GIF (Pillow)

```bash
python math_art/mandelbrot_zoom.py --frames 120 --resolution 1080p --output assets/mandelbrot.gif

```

### 3. Run a Terminal Particle Stream (Rich / Curses)

```bash
python terminal/matrix_rain.py

```

---

## Dependencies

The core repository relies on the following standard visualization packages:

* [NumPy](https://numpy.org/) — Vectorized calculations and matrix manipulations.
* [Matplotlib](https://matplotlib.org/) — Plot-based and chart animations (`FuncAnimation`).
* [Pygame](https://www.pygame.org/) — Interactive 2D real-time simulation windows.
* [Pillow (PIL)](https://pillow.readthedocs.io/) — Frame-by-frame image generation and GIF exports.
* [Rich](https://rich.readthedocs.io/) — Terminal text formatting and CLI animations.

*(Refer to `requirements.txt` for specific version pinning.)*

---

## Contributing

Contributions are welcome! To add a new animation:

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/NewAnimation`).
3. Place your script in the appropriate directory (`algorithms/`, `physics/`, etc.).
4. Include a lightweight demo GIF/preview in `assets/` if applicable.
5. Commit your Changes (`git commit -m 'Add Lorenz Attractor simulation'`).
6. Push to the Branch (`git push origin feature/NewAnimation`).
7. Open a Pull Request.

---

## License

Distributed under the MIT License. See `LICENSE` for more details.

```

```
