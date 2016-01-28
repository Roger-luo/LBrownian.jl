LBrownian.jl
---
The LBrownian.jl is a Brownian Motion simulator of L shaped particle in [Julia](http://julialang.org).

User Guide
---
to use this package
```julia
using LBrownian
```

initialize a L-shaped particle by using function `L_particle`

function `L_particle(central_pos,central_vel,angle,angle_vel,mass,StickLength)` is the constructor of a L-shaped particle.
the `angle` parameter means the angle between the stick and x-axis,and so does the angle velocity `angle_vel`

```julia
Lshape = L_particle([0,0],[0,0],[π/3,-π/3],[0,0],[1e-6,1e-6,1e-6],[0.1,0.1])
```

use function `time_evolution!` to evolute the system
function `time_evolution!(file::AbstractString,free_par::particle,time_step::Int64,dt=1e-6)`,need a filename `file`,and a particle object `free_par` ,and `time_step` for the whole time steps,`dt` is the time step,defaut to be `1e-6`

```julia
time_evolution!("data.dat",Lshape,convert(Int64,1e3))
```

use python to do animation

```python
python draw.py
```

future goals:
- animated by Julia packages
- evolution of a given particle
- interaction between particles
- complete Brownian Motion Simulator

PRs are welcome!
by [Roger luo](http://rogerluo.cc)
