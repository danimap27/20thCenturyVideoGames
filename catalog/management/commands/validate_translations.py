from django.core.management.base import BaseCommand
from django.conf import settings
from pathlib import Path
import gettext

class Command(BaseCommand):
    help = "Check that compiled translation files are valid"

    def handle(self, *args, **options):
        invalid = False
        for locale_path in settings.LOCALE_PATHS:
            for mo_file in Path(locale_path).rglob("*.mo"):
                try:
                    with open(mo_file, "rb") as fh:
                        gettext.GNUTranslations(fh)
                except Exception as exc:
                    invalid = True
                    self.stderr.write(f"Invalid translation file: {mo_file} ({exc})")
        if invalid:
            self.stderr.write("Delete the invalid files and run 'django-admin compilemessages'.")
        else:
            self.stdout.write("All translation files are valid.")
