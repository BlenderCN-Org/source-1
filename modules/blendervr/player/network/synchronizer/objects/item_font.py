# -*- coding: utf-8 -*-
# file: blendervr/player/network/synchronizer/objects/item_font.py

## Copyright (C) LIMSI-CNRS (2014)
##
## contributor(s) : Jorge Gascon, Damien Touraine, David Poirier-Quinot,
## Laurent Pointal, Julian Adenauer,
##
## This software is a computer program whose purpose is to distribute
## blender to render on Virtual Reality device systems.
##
## This software is governed by the CeCILL  license under French law and
## abiding by the rules of distribution of free software.  You can  use,
## modify and/ or redistribute the software under the terms of the CeCILL
## license as circulated by CEA, CNRS and INRIA at the following URL
## "http://www.cecill.info".
##
## As a counterpart to the access to the source code and  rights to copy,
## modify and redistribute granted by the license, users are provided only
## with a limited warranty  and the software's author,  the holder of the
## economic rights,  and the successive licensors  have only  limited
## liability.
##
## In this respect, the user's attention is drawn to the risks associated
## with loading,  using,  modifying and/or developing or reproducing the
## software by the user in light of its specific status of free software,
## that may mean  that it is complicated to manipulate,  and  that  also
## therefore means  that it is reserved for developers  and  experienced
## professionals having in-depth computer knowledge. Users are therefore
## encouraged to load and test the software's suitability as regards their
## requirements in conditions enabling the security of their systems and/or
## data to be ensured and,  more generally, to use and operate it in the
## same conditions as regards security.
##
## The fact that you are presently reading this means that you have had
## knowledge of the CeCILL license and that you accept its terms.
##

#import copy
#import mathutils
from . import item_object


class Font:
    TEXT = b't'


class Master(Font, item_object.Master):
    def __init__(self, parent, item):
        Font.__init__(self)
        item_object.Master.__init__(self, parent, item)
        self._previousText = ""

    def getSynchronizerBuffer(self):
        buff = item_object.Master.getSynchronizerBuffer(self)

        if self._previousText != self._item.text:
            self_previousText = self._item.text
            buff.command(self.TEXT)
            buff.string(self_previousText)

        return buff


class Slave(Font, item_object.Slave):
    def __init__(self, parent, item):
        Font.__init__(self)
        item_object.Slave.__init__(self, parent, item)

    def _processCommand(self, command, buff):
        item_object.Slave._processCommand(self, command, buff)

        if command == self.TEXT:
            self._item.text = buff.string()

