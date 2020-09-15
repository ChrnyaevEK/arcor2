#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from collections import defaultdict
from typing import Any, DefaultDict, Dict, Optional, Set

from aiologger import Logger  # type: ignore
from aiologger.levels import LogLevel  # type: ignore
from websockets.server import WebSocketServerProtocol as WsClient

from arcor2 import helpers as hlp
from arcor2.cached import UpdateableCachedProject, UpdateableCachedScene
from arcor2.data import events
from arcor2.object_types.abstract import Generic
from arcor2_arserver.object_types.utils import ObjectTypeDict
from arcor2_arserver_data.events.common import ShowMainScreen

logger = Logger.with_default_handlers(name="server", formatter=hlp.aiologger_formatter(), level=LogLevel.DEBUG)
VERBOSE: bool = False

PORT: int = int(os.getenv("ARCOR2_SERVER_PORT", 6789))

SCENE: Optional[UpdateableCachedScene] = None
PROJECT: Optional[UpdateableCachedProject] = None

MAIN_SCREEN: Optional[ShowMainScreen.Data] = ShowMainScreen.Data(ShowMainScreen.Data.WhatEnum.ScenesList)

INTERFACES: Set[WsClient] = set()

OBJECT_TYPES: ObjectTypeDict = {}

SCENE_OBJECT_INSTANCES: Dict[str, Generic] = {}

RUNNING_ACTION: Optional[str] = None  # ID of an action that is being executed during project editing
RUNNING_ACTION_PARAMS: Optional[Dict[str, Any]] = None

PACKAGE_STATE = events.PackageState.Data()
PACKAGE_INFO: Optional[events.PackageInfo.Data] = None
ACTION_STATE: Optional[events.ActionState.Data] = None
CURRENT_ACTION: Optional[events.CurrentAction.Data] = None
TEMPORARY_PACKAGE: bool = False

RegisteredUiDict = DefaultDict[str, Set[WsClient]]

ROBOT_JOINTS_REGISTERED_UIS: RegisteredUiDict = defaultdict(lambda: set())  # robot, UIs
ROBOT_EEF_REGISTERED_UIS: RegisteredUiDict = defaultdict(lambda: set())  # robot, UIs
