#!/usr/bin/python3
<<<<<<< HEAD
"""
A fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""

from os import path
=======
# Fabfile to generates a .tgz archive from the contents of web_static.
import os.path
>>>>>>> a9fe34ecaf215ca72d84256baacbc86bc6faa8cd
from datetime import datetime
from fabric.api import local


def do_pack():
<<<<<<< HEAD
    """
    A function that generates an archive
    """
    date = datetime.now()
    archive = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        date.year, date.month, date.day,
        date.hour, date.minute, date.second
    )
    if not path.isdir("versions"):
        if local("mkdir versions").failed:
            return None
    cmd = "cd web_static && tar -cvzf ../{} . && cd -".format(archive)
    if local(cmd).succeeded:
        return archive
    return None
=======
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
>>>>>>> a9fe34ecaf215ca72d84256baacbc86bc6faa8cd
