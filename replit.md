# Robot Simulation Game

## Overview

This is a Python-based robot simulation game built with Pygame where multiple robots with different movement patterns compete to collect coins in a 100x100 grid world. Each robot has unique behaviors, movement strategies, and personalities implemented through inheritance from a base robot class.

## System Architecture

### Frontend Architecture
- **Game Engine**: Pygame-based 2D visualization
- **Rendering**: Real-time grid-based display with 8x8 pixel tiles
- **UI Elements**: Score display, robot status, and speech bubbles
- **Window Size**: 1000x800 pixels (800x800 game world + 200px UI panel)

### Backend Architecture
- **Object-Oriented Design**: Base class inheritance pattern
- **Game Loop**: Standard Pygame event loop with clock-based timing
- **State Management**: Game world represented as 2D array
- **Movement System**: Direction-based movement (North=0, East=1, South=2, West=3)

### Core Components
1. **RobotBase Class**: Abstract base class defining robot interface
2. **Individual Robot Classes**: 12 unique robot implementations with distinct behaviors
3. **Game Class**: Main game controller handling world state and rendering
4. **World Grid**: 100x100 coordinate system for robot positioning

## Key Components

### Robot Behaviors
- **Noah**: Pattern-based movement (3 steps forward, turn right)
- **Zac**: Completely random movement
- **Nathan**: Target-seeking behavior with random destinations
- **Eden**: Spiral outward movement pattern
- **Samuel**: Bouncing ball physics simulation
- **Zak**: Circular movement patterns (clockwise/counter-clockwise)
- **William**: Directional preference with occasional randomization
- **Sophia**: Exploration mode with home-returning behavior
- **Willow**: Zigzag pattern alternating horizontal/vertical
- **Kate**: Conservative movement avoiding edges
- **Katie**: Aggressive movement with frequent direction changes
- **Jon**: Patrol route following specific waypoints

### Robot Interface
- `getMoveDirection()`: Returns movement direction (0-3)
- `speak()`: Returns robot dialogue text
- `celebrate()`: Returns celebration message for coin collection
- `setIcon()`: Returns RGB color tuple for visual representation

### Game Features
- Real-time robot movement simulation
- Coin collection scoring system
- Speech bubble display system
- Color-coded robot identification
- Boundary collision detection

## Data Flow

1. **Initialization**: Game creates world grid and spawns robots at random positions
2. **Game Loop**: 
   - Process pygame events
   - Update robot positions based on movement algorithms
   - Check for coin collections and boundary collisions
   - Render updated world state
   - Display UI elements and robot status
3. **Movement Processing**: Each robot's `getMoveDirection()` is called to determine next position
4. **Collision Detection**: Validate moves against world boundaries
5. **Scoring**: Update robot scores when coins are collected

## External Dependencies

- **Pygame**: Primary game engine and rendering library
- **Random**: Used for randomization in robot behaviors and game mechanics
- **Time**: For timing and delay functionality
- **OS/Sys**: System utilities for file operations

## Deployment Strategy

- **Local Execution**: Single-file Python application
- **Platform**: Cross-platform (Windows, macOS, Linux) via Pygame
- **Installation**: Requires Python 3.x and Pygame library
- **Execution**: Run `main.py` to start the simulation

## User Preferences

Preferred communication style: Simple, everyday language.

## Changelog

Changelog:
- July 07, 2025. Initial setup
- July 07, 2025. Added organized folder structure with bots/[robot_name]/ containing .py and .png files
- July 07, 2025. Added movementAllowed() function to RobotBase class for wall collision detection
- July 07, 2025. Updated all robots to use wall-avoiding random movement patterns
- July 07, 2025. Added bash functionality: robots bash every 5 seconds, steal coins, custom insults, red flash effects
- July 07, 2025. Successfully migrated from Replit Agent to standard Replit environment
- July 07, 2025. Fixed Eden bot logic to properly seek closest coins instead of moving in single direction