"""
This file is responsible for platform and version specific configurations
"""
"""
Math Inspector: a visual programming environment for scientific computing
Copyright (C) 2021 Matt Calhoun

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import platform, sys, os, subprocess
from pkg_resources import resource_filename

def version():
    """
    version detector. Precedence: installed dist, git, 'UNKNOWN'.
    """
    try:
        from ._dist_version import VERSION # version stored in `mathinspector/_dist_version.py`
    except ImportError:
        try:
            from setuptools_scm import get_version
            VERSION = get_version(root='..', relative_to=__file__)
        except (ImportError, LookupError):
            VERSION = "UNKNOWN"
    return VERSION

SYSTEM = platform.system()

def open_editor(app, file):
    if SYSTEM == "Windows":
        subprocess.run(["start", file])
    elif SYSTEM == "Linux":
        if "EDITOR" not in os.environ:         
            app.console.write("Could not open editor.  You must set the $EDITOR environment variable to use this feature.", tags="red")
            return
        subprocess.Popen([os.environ["EDITOR"], file])
    elif SYSTEM == "Darwin":
        subprocess.run(["open", file])

BUTTON_RIGHT = '<Button-3>' if SYSTEM in ("Windows", "Linux") else '<Button-2>'
BUTTON_RELEASE_RIGHT = '<ButtonRelease-3>' if SYSTEM in ("Windows", "Linux") else '<ButtonRelease-2>'
BUTTON_RIGHT_MOTION = '<B3-Motion>' if SYSTEM in ("Windows", "Linux") else '<B2-Motion>'
CONTROL_KEY = 'Control' if SYSTEM in ("Windows", "Linux") else 'Command'
if hasattr(sys, "_MEIPASS"):
    BASEPATH = os.path.join(
        sys._MEIPASS,
        "assets" if SYSTEM in ("Windows", "Linux") else "../Resources/assets")
    if SYSTEM == "Windows":
        AUTOSAVE_PATH = os.path.join(os.path.join(os.getenv('LOCALAPPDATA'), "MathInspector"), "autosave.math")
    else:
        AUTOSAVE_PATH = os.path.join(BASEPATH, "autosave.math")
else:
    BASEPATH = resource_filename("mathinspector", "assets")
    AUTOSAVE_PATH = os.path.join(BASEPATH, "autosave.math")

if SYSTEM in ("Windows", "Linux"):
    FONT = "LucidaConsole 12"
    DOC_FONT = "Nunito-ExtraLight 12"
    FONT_SIZE = {
        "extra-small": "8",
        "small": "10",
        "default": "12",
        "medium": "16",
        "large": "18",
        "extra-large": "22",
    }
    ITEM_FONTSIZE = {
        "name": "14",
        "class": "8",
        "value": "12",
        "argname": "8",
        "argvalue": "10",
    }
else:
    FONT = "Menlo 15"
    DOC_FONT = "Nunito-ExtraLight 16"
    FONT_SIZE = {
        "extra-small": "12",
        "small": "14",
        "default": "15",
        "medium": "18",
        "large": "22",
        "extra-large": "24",
    }
    ITEM_FONTSIZE = {
        "name": "18",
        "class": "12",
        "value": "16",
        "argname": "8",
        "argvalue": "12",
    }
