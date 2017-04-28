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

import unittest

from gittish.protocol.stream import SyncStream


class SyncStreamTest(unittest.TestCase):

  def test_stream(self):
    stream = SyncStream()
    data = [1,2,3,4,5]
    idx = 0
    sent = data[idx]
    stream.send(sent)
    for read in stream.stream():
      self.assertEqual(sent, read)
      idx += 1
      if idx >= len(data):
        stream.close()
      else:
        sent = data[idx]
        stream.send(sent)

# vim: expandtab:ts=2:sw=2:
