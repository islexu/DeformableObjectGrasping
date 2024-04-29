# DeformableObjectGrasping Extension for Omniverse Isaac Sim

## Overview

The DeformableObjectGrasping extension enhances the capabilities of robotic arms in the Omniverse Isaac Sim, focusing on interactions with deformable objects. This extension provides a customizable simulation environment to optimize robotic grasping mechanisms in virtual scenarios, aiding developers and researchers.

## Installation

Follow these steps to install the DeformableObjectGrasping extension:

1. **Navigate to the Isaac Sim extensions directory**:
   ```bash
   cd ~/.local/share/ov/pkg/isaac_sim-2023.1.1/exts/omni.isaac.examples/omni/isaac/examples/user_examples

2. **Clone the repository**:
   ```bash
   git clone https://github.com/islexu/DeformableObjectGrasping

## Repository Structure

The repository includes the following components:

- `__pycache__`: Python cache files (not essential for functionality).
- `deformableObjectGrasping`: Folder for storing USD files for simulations.
- `__init__.py`: Initializes the extension and imports necessary modules.
- `deformableObjectGrasping.py`: Core logic for setting up the simulation environment.
- `deformableObjectGrasping_extension.py`: Initializes and registers the extension within Isaac Sim.

## Key Files Explained

### `__init__.py`

Initializes the extension, ensuring the main simulation script and extension script are correctly integrated with the Isaac Sim environment.

### `deformableObjectGrasping.py`

Defines the `deformableObjectGrasping` class, extending `BaseSample` from Isaac Sim's API. This class includes methods to:
- Set up the simulation scene with a table, robot (Franka), and a graspable cube.
- Configure physical properties and appearances using USD and PhysX APIs.
- Enable deformable object simulation for realistic interactions.

### `deformableObjectGrasping_extension.py`

Inherits from `BaseSampleExtension`, managing the extension lifecycle:
- Starts the extension and integrates it into the Isaac Sim menu.
- Links functionality from `deformableObjectGrasping.py` to the UI for user access.

## Getting Started

After installation, access the DeformableObjectGrasping extension from the Isaac Sim menu under user examples. Customize the environment and parameters based on your needs to start simulating and interacting with the scene.

## Conclusion

DeformableObjectGrasping offers a robust platform for developing and studying robotic grasping technologies in a simulated environment, leveraging the advanced graphics and physics of Omniverse Isaac Sim for realistic and versatile robotic manipulation studies.
