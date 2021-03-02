#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import pytest
import logging

from nomad.datamodel import EntryArchive

from eelsdbconverter import EELSApiJsonConverter


@pytest.fixture
def parser():
    return EELSApiJsonConverter()


def test_example(parser):
    archive = EntryArchive()
    parser.parse('tests/Test1/metadata.json', archive, logging)

    measurement = archive.section_measurement[0]
    assert measurement.section_metadata[0].section_sample[0].sample_id is not None
    assert measurement.section_metadata[0].section_experiment[0].method_name is not None
    assert measurement.section_data[0].section_spectrum[0].n_values == 226
