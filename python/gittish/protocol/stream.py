# Copyright 2017 Carsten Klein
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import threading
from time import sleep


DEFAULT_SLEEP_TIME = 0.00001


# TBD:DOCUMENT
class SyncStream:

  def __init__(self, sleep_time = DEFAULT_SLEEP_TIME):
    self._semaphore = threading.Semaphore()
    self._data = None
    self._closed = False
    self._sleep_time = sleep_time

  def close(self):
    self._closed = True
    try:
      self._semaphore.release()
    except:
      pass

  def send(self, data):
    self._semaphore.acquire()
    self._data = data
    self._semaphore.release()

  def stream(self):
    while not self._closed:
      self._semaphore.acquire()
      data = self._data
      self._data = None
      self._semaphore.release()
      if self._closed:
        break
      if not data is None:
        yield data
      # make sure that we don't busy loop too much
      sleep(self._sleep_time)

# vim: expandtab:ts=2:sw=2:
