# Copyright (c) 2015 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Camera node App for use with Toolkit's Houdini engine.
"""

import sgtk


class TkCameraNodeApp(sgtk.platform.Application):
    """The Camera Node."""

    def init_app(self):
        """Initialize the app."""

        tk_houdini_camera = self.import_module("tk_houdini_cameranode")
        self.handler = tk_houdini_camera.TkCameraNodeHandler(self)

    def get_nodes(self):
        """
        Returns a list of hou.node objects for each tk camera node.

        Example usage::

        >>> import sgtk
        >>> eng = sgtk.platform.current_engine()
        >>> app = eng.apps["tk-houdini-cameranode"]
        >>> tk_camera_nodes = app.get_nodes()
        """

        self.log_debug("Retrieving tk-houdini-camera nodes...")
        tk_houdini_camera = self.import_module("tk_houdini_cameranode")
        nodes = tk_houdini_camera.TkCameraNodeHandler.\
            get_all_tk_camera_nodes()
        self.log_debug("Found %s tk-houdini-camera nodes." % (len(nodes),))
        return nodes

    def get_output_path(self, node):
        """
        Returns the evaluated output path for the supplied node.

        Example usage::

        >>> import sgtk
        >>> eng = sgtk.platform.current_engine()
        >>> app = eng.apps["tk-houdini-cameranode"]
        >>> output_path = app.get_output_path(tk_camera_node)
        """

        self.log_debug("Retrieving output path for %s" % (node,))
        tk_houdini_camera = self.import_module("tk_houdini_cameranode")
        output_path = tk_houdini_camera.TkCameraNodeHandler.\
            get_output_path(node)
        self.log_debug("Retrieved output path: %s" % (output_path,))
        return output_path
