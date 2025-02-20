# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests tasks."""

# import pytest # Use pytest for writing tests!

from src.tasks import command

def test_task_command(mocker):
    """Test command task."""

    mock_task_command = mocker.patch(
        "src.tasks.command"
    )
    mock_task_command.return_value = "my return value"

    ret = command(None)
    assert isinstance(ret,str) 