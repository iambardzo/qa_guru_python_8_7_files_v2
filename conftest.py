import pytest
import os
import shutil
from utils import TMP_PATH, RESOURCES_PATH

@pytest.fixture(scope='session', autouse=True)
def create_delete_zip():
    if not os.path.exists(TMP_PATH):
        os.mkdir('tmp')
    shutil.make_archive('archive', 'zip', RESOURCES_PATH)
    shutil.move('archive.zip', os.path.join(TMP_PATH, 'archive.zip'))
        
    yield
    shutil.rmtree(TMP_PATH)
