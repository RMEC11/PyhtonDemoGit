import logging

import pytest

from pytestspractice.BaseClass import BaseClass


@pytest.mark.usefixtures("datLoad")
class Test_data(BaseClass):

    def test_usercreat(self, datLoad):
        log = self.getLogger()
        log.info(datLoad)
        log.error(datLoad[0])
        log.warning(datLoad[2])