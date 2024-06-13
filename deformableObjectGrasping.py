"""
Feng Xu
2024-06-13
"""

import omni
import carb
import numpy as np
import math
from omni.isaac.examples.base_sample import BaseSample
# This extension has franka related tasks and controllers as well
from omni.isaac.franka import Franka
from omni.isaac.core.objects import DynamicCuboid
import numpy as np
import omni.usd
from pxr import UsdGeom, Sdf, Gf, PhysxSchema, UsdPhysics
from omni.physx.scripts import deformableUtils, physicsUtils
import omni.physxdemos as demo

from omni.isaac.core.utils.stage import add_reference_to_stage
from omni.isaac.core.prims import RigidPrim

class deformableObjectGrasping(BaseSample):
    def __init__(self) -> None:
        super().__init__()

    def setup_scene(self):
        world = self.get_world()
        
        world.scene.add_default_ground_plane()


        # Station W5
        table_prim_path = "/World/cute_table"
        table_absolute_asset_path = "/home/isle/Desktop/Table.usd"
        # self-modified: you should download the USD file and change the asset path
        add_reference_to_stage(usd_path=table_absolute_asset_path, prim_path=table_prim_path)
        table = world.scene.add(RigidPrim(prim_path=table_prim_path,
                                          name="cute_table",
                                          position=[-0.2, 0.55, 0.8],
                                          scale=[0.80],
                                          orientation=[1, 0, 0, 0]  # euler angles
                                          ))
        


        # Robot specific class that provides extra functionalities
        # such as having gripper and end_effector instances.
        franka = world.scene.add(Franka(prim_path="/World/Fancy_Franka", name="fancy_franka"))
        # add a cube for franka to pick up
        world.scene.add(
            DynamicCuboid(
                prim_path="/World/hard_cube",
                name="hard_cube",
                position=np.array([0.2, 0.5, 0.85]),
                scale=np.array([0.05, 0.05, 0.05]),
                color=np.array([1.0, 0, 0]), # red
            )
        )

        stage = omni.usd.get_context().get_stage() 
        # Configure the physics scene to use GPU dynamics for particles (fluids)
        physics_context = world.get_physics_context()
        physics_context.enable_gpu_dynamics(True)
        
        world.set_simulation_dt(physics_dt=1.0 / 600.0, rendering_dt=1.0 / 60.0)   #change dt
        
        # Create a cube mesh prim
        result, path = omni.kit.commands.execute("CreateMeshPrimCommand", prim_type="Cube")
        cube_prim = stage.GetPrimAtPath(path)
        
        xform = UsdGeom.Xformable(cube_prim)
        
        # Update or create necessary transform operations
        existing_ops = xform.GetOrderedXformOps()
        op_names = [op.GetOpName() for op in existing_ops]
        translate_op_name = "xformOp:translate"
        scale_op_name = "xformOp:scale"
        
        if translate_op_name in op_names:
            for op in existing_ops:
                if op.GetOpName() == translate_op_name:
                    op.Set(Gf.Vec3d(-0.15, 0.5, 0.85))
        else:
            xform.AddTranslateOp().Set(Gf.Vec3d(0.0, 0.0, 1.0))
        
        if scale_op_name in op_names:
            for op in existing_ops:
                if op.GetOpName() == scale_op_name:
                    op.Set(Gf.Vec3f(0.05, 0.05, 0.05))
        else:
            xform.AddScaleOp().Set(Gf.Vec3f(0.05, 0.05, 0.05))
        
        simulation_resolution = 10

        # Apply PhysxDeformableBodyAPI and PhysxCollisionAPI to skin mesh
        success = deformableUtils.add_physx_deformable_body(
            stage,
            xform.GetPath(),
            collision_simplification=True,
            simulation_hexahedral_resolution=simulation_resolution,
            self_collision=False,
        )

        # Create a deformable body material and set it on the deformable body
        deformable_material_path = omni.usd.get_stage_next_free_path(stage, "Cube", True)
        deformableUtils.add_deformable_body_material(
            stage,
            deformable_material_path,
            youngs_modulus=10000.0,
            poissons_ratio=0.49,
            damping_scale=0.0,
            dynamic_friction=0.5,
        )
        physicsUtils.add_physics_material_to_prim(stage, xform.GetPrim(), deformable_material_path) 
            
    async def setup_post_load(self):        
        self._world = self.get_world()
