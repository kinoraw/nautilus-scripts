#!/bin/bash

base=${1%.*}
export LANG=C && meshlabserver -i $1 -o $base-poisson9.ply -s ~/.local/share/nautilus/scripts/nautilus-scripts/MESHLAB/poisson9_para_full_res.mlx -om vc vn
