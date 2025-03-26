#!/usr/bin/env python3
import numpy as np
from isaacsim import SimulationApp


def main():
    simulation_app = SimulationApp(
        {
            "headless": False,
            "exts": {
                "omni.replicator.core": False,
                "omni.replicator.replicator_yaml-2.0.10": False,
            },
        }
    )

    from omni.isaac.core import World
    from omni.isaac.core.objects import DynamicCuboid

    world = World()
    world.scene.add_default_ground_plane()

    cube = DynamicCuboid(
        prim_path="/World/Cube",
        name="my_cube",
        position=[0, 0, 1.0],
        size=0.5,
        color=np.array([0.2, 0.6, 1.0]),  # ✅ use NumPy array
    )

    world.reset()
    while simulation_app.is_running():
        world.step(render=True)

    simulation_app.close()
