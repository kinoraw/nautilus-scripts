#!/bin/bash

base=${1%.*}
export LANG=C && meshlabserver -i $1 -o $base-poisson2.ply -s ~/.local/share/nautilus/scripts/nautilus-scripts/MESHLAB/poisson2.mlx -om vc vn
