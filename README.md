
# py-animations
```markdown
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A curated collection of modular, production-ready Python animations, visualizations, and procedural graphic generators. 

`py-animations` provides standalone scripts and reusable utilities for rendering mathematical concepts, algorithmic simulations, physics models, geometric patterns, and terminal UI graphics.
```
---

## Features
```markdown
* **Algorithmic Visualizations:** Real-time visual representations of common sorting, pathfinding, and graph traversal algorithms.
* **Turtle Graphics & Geometric Art:** Recursive tree fractals, spirographs, Koch snowflakes, and step-by-step vector drawing routines using Python's native `turtle` engine.
* **Physics & Simulations:** Particle systems, n-body gravitational simulations, wave propagation, and cellular automata.
* **Mathematical Art:** Parametric curves, complex fractals (Mandelbrot, Julia sets), and generative geometry.
* **Multiple Output Engines:** Scripts supporting rendering via **Turtle Graphics**, **Manim**, **Matplotlib**, **Pygame**, **Pillow (GIF generation)**, and **Terminal (Curses/Rich)**.
* **Zero Bloat:** Each animation module is self-contained with minimal external dependencies.
```
---

## Repository Structure

```markdown
py-animations/
├── algorithms/       # Sorting, pathfinding, and tree traversal visualizers
├── turtle_art/       # Turtle-based geometric patterns, spirographs, and recursive trees
├── math_art/         # Fractals, parametric equations, and shader-like scripts
├── physics/          # Fluid dynamics, spring-mass systems, gravity simulations
├── terminal/         # ASCII art, CLI spinners, and terminal-based animations
├── assets/           # Sample outputs (GIFs, MP4s, static renders)
├── requirements.txt  # Core dependencies
└── README.md

```

---

## Quick Start

### Prerequisites

Ensure you have Python 3.8 or higher installed.

> **Note for Turtle graphics on Linux:** Python's built-in `turtle` module relies on Tkinter. On some Debian/Ubuntu systems, install Tkinter support if it is not pre-packaged:
> ```bash
> sudo apt-get install python3-tk
> 
> ```
> 
> 

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

### 1. Run a Turtle Fractal Tree Animation

```bash
python turtle_art/fractal_tree.py --depth 8 --branch-angle 25

```

### 2. Run a Sorting Algorithm Visualizer (Pygame / Matplotlib)

```bash
python algorithms/bubble_sort_visualizer.py --speed fast --elements 100

```

### 3. Generate a Fractal GIF (Pillow)

```bash
python math_art/mandelbrot_zoom.py --frames 120 --resolution 1080p --output assets/mandelbrot.gif

```

### 4. Run a Terminal Particle Stream (Rich / Curses)

```bash
python terminal/matrix_rain.py

```

---

## Dependencies

The repository leverages both Python's built-in toolsets and standard visualization packages:

* [Turtle Graphics](https://docs.python.org/3/library/turtle.html) — **Standard Library** module for vector drawing, recursive art, and step-by-step procedural animations without third-party installs.
* [NumPy](https://numpy.org/) — Vectorized calculations and matrix manipulations.
* [Matplotlib](https://matplotlib.org/) — Plot-based and chart animations (`FuncAnimation`).
* [Pygame](https://www.pygame.org/) — Interactive 2D real-time simulation windows.
* [Pillow (PIL)](https://pillow.readthedocs.io/) — Frame-by-frame image generation and GIF exports.
* [Rich](https://rich.readthedocs.io/) — Terminal text formatting and CLI animations.

*(Refer to `requirements.txt` for specific third-party package version pinning.)*

---

## Contributing

Contributions are welcome! To add a new animation:

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/NewAnimation`).
3. Place your script in the appropriate directory (`turtle_art/`, `algorithms/`, `physics/`, etc.).
4. Include a lightweight demo GIF/preview in `assets/` if applicable.
5. Commit your Changes (`git commit -m 'Add Turtle Dragon Curve animation'`).
6. Push to the Branch (`git push origin feature/NewAnimation`).
7. Open a Pull Request.

---

## License

Distributed under the MIT License. See `LICENSE` for more details.

```

```
