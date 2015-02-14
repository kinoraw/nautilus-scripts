#!/bin/bash

base=${1%.*}
export LANG=C && meshlabserver -i $1 -o $base-poisson.ply -s ~/.local/share/nautilus/scripts/nautilus-scripts/MESHLAB/poisson.mlx -om vc vn
