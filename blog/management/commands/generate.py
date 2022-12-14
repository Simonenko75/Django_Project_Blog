from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from blog.models import Post


class Command(BaseCommand):
    help = 'Create fake posts'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Кількість постів для додавання')

    def handle(self, *args, **kwargs):
        total = kwargs['total']

        for i in range(total):
            fake = Faker()

            try:
                a = fake.name()
                ttl = fake.sentences(1)[0]
                txt = ' '.join(fake.sentences(3))
                pub = fake.year()

                Post.objects.create(
                    title=ttl,
                    author=a,
                    text=txt,
                    published=pub
                )
                print(f'{i+1} пост було успішно додано!!!Додалася новий пост під назвою {ttl}')
            except:
                raise CommandError('Error of creating')
            else:
                print(f'Додалася новий пост під назвою {ttl}')
