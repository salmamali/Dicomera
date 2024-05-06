import os

import pydicom
from pydicom import FileDataset

from apps.home.models import DicomEntity


def get(dicom: DicomEntity):
    dcom = os.listdir(dicom.path)
    dataset: FileDataset = pydicom.dcmread(dicom.path)


