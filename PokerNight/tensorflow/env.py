from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf  # pylint: disable=g-explicit-tensorflow-version-import
import numpy as np

from tf_agents import specs
from tf_agents.environments import tf_environment
from tf_agents.trajectories import time_step as ts
from tf_agents.utils import common


class Player:
    pass


class PokerEnv(tf_environment.TFEnvironment):
    playerCount = 5
    playerList: list[Player] = []

    def __init__(self):
        self._action_spec = specs.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=0, maximum=1, name='action')
        self._observation_spec = specs.BoundedArraySpec(
            shape=(4,), dtype=np.int32, minimum=0, name='observation')
        self._state = 0
        self._episode_ended = False
        super(PokerEnv, self).__init__(
            self._observation_spec, self._action_spec)

    def _reset(self):
        pass

    def _step(self, action):
        pass

    def _current_time_step(self):
        pass
