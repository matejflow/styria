from django.core.management.base import BaseCommand

from core.factories import MemberFactory, StaffFactory, SuperUserFactory


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        """Seed demo users for site"""

        def save_test_user(user, username: str) -> None:
            user.is_active = True
            user.username = username
            user.set_password('test.123')
            try:
                user.save()
            except Exception:
                pass

        save_test_user(MemberFactory.build(), 'test_user')
        save_test_user(StaffFactory.build(), 'test_staff')
        save_test_user(SuperUserFactory.build(), 'test_admin')
