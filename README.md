# Asteroids
 
A classic Asteroids-style arcade game built with Python and [pygame](https://www.pygame.org/). Pilot a ship through an asteroid field, shoot the rocks apart, and try not to crash.
 
## Motivation
 
I built this as part of Boot.dev's *Build Asteroids* guided project. The goal was hands-on practice with:
 
- Object-oriented programming: a base `CircleShape` class that the player, asteroids, and shots inherit from
- Game-loop fundamentals: handling input, updating state, and drawing each frame at a steady frame rate
- Working with sprite groups and collision detection in pygame
- Local Python tooling, including virtual environments and dependency management with `uv`
## Quick Start
 
**Requirements:** Python 3.13 or newer and [uv](https://docs.astral.sh/uv/).
 
```bash
git clone https://github.com/Feared81/asteroids.git
cd asteroids
uv sync
uv run main.py
```
 
`uv sync` creates the virtual environment and installs the dependencies (pygame 2.6.1). `uv run main.py` starts the game.
 
## Usage
 
Run the game from the project folder:
 
```bash
uv run main.py
```
 
### Controls
 
| Key | Action |
|---|---|
| `A` / `D` | Rotate the ship left / right |
| `W` / `S` | Move forward / backward |
| `Space` | Shoot |
 
Shoot asteroids to break them into smaller pieces, and avoid touching them. Close the window to quit.
 
## Contributing
 
Suggestions and improvements are welcome, though this is a small learning project.
 
1. Fork the repository.
2. Create a branch for your change: `git checkout -b my-feature`
3. Make your changes and test them by running the game.
4. Commit with a clear message and push the branch to your fork.
5. Open a pull request describing what you changed and why.
If you find a bug, please open an issue that describes what happened and how to reproduce it.
