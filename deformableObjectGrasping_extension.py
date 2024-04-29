# Copyright (c) 2020-2023, NVIDIA CORPORATION. All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto. Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#

import os

from omni.isaac.examples.base_sample import BaseSampleExtension
from omni.isaac.examples.user_examples.deformableObjectGrasping import deformableObjectGrasping


class deformableObjectGrasping_extension(BaseSampleExtension):
    def on_startup(self, ext_id: str):
        super().on_startup(ext_id)
        super().start_extension(
            menu_name="",
            submenu_name="",
            name="deformable object grasping",
            title="deformable object grasping",
            doc_link="TODO:DOCLINK",
            overview="This Example introduces the user on how to simulate deformable object grasping using panda robot",
            file_path=os.path.abspath(__file__),
            sample=deformableObjectGrasping(),
        )
        return
