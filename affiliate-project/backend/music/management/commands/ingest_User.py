# 向数据库批量添加数据
from datetime import datetime
import json

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware

from music.models import User


class Command(BaseCommand):
    help = 'Create tracks from JSON file'

    def handle(self, *args, **kwargs):
        # set the path to the datafile
        datafile = settings.BASE_DIR / 'data' / 'tracks.json'
        assert datafile.exists()

        # load the datafile
        with open(datafile, 'r') as f:
            data = json.load(f)

        users = [User(**track) for track in data]
        User.objects.bulk_create(users)