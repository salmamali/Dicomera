from apps.home.models import DicomEntity


def upload(file_path):
    DicomEntity.objects.create(
        path=file_path
    )