from django.core.management.base import BaseCommand
from content_migration.management.constants import (
    IMPORT_FILENAMES,
    LOCAL_MIGRATION_DATA_DIRECTORY,
)

from content_migration.management.import_civicrm_contacts_handler import (
    handle_import_civicrm_contacts,
)


class Command(BaseCommand):
    help = "Import Contacts Directory from Drupal site"

    def handle(self, *args: tuple, **options: dict[str, str]) -> None:
        file_name = (
            LOCAL_MIGRATION_DATA_DIRECTORY + IMPORT_FILENAMES["civicrm_contacts"]
        )

        handle_import_civicrm_contacts(file_name)
