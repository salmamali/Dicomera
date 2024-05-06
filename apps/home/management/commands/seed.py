import logging

from django.core.management.base import BaseCommand
import random

from apps.home.models import DicomEntity

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    logger.info("Delete Address instances")
    DicomEntity.objects.all().delete()


def create_address():
    """Creates an address object combining different elements from the list"""
    logger.info("Creating dicom")

    address = DicomEntity(
        image_type="123",
    instance_creator_uid = "123",
    path = "local-strooooge",
    )
    address.save()
    logger.info("{} address created.".format(address))
    return address

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Creating 15 addresses
    # for i in range(15):
    create_address()