# Surface Reconstruction Tools

## Installation Guide

On linux you need to install the zlib, png and jpeg libraries.
```bash
apt install libpng-dev zlib1g-dev libjpeg-dev
```

### From Command Line

#### Poisson Reconstruction
Use
```bash
mkdir bin
g++ -o ./bin/PoissonRecon src/PoissonRecon.cpp -pthread -ljpeg -lpng -lz
```

### Using Cmake


