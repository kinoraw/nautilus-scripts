#!/bin/bash

base=${1%.*}
export LANG=C && meshlabserver -i $1 -o $base-marching_cubes.ply -s ~/.local/share/nautilus/scripts/nautilus-scripts/MESHLAB/poisson.mlx -om vc vn
