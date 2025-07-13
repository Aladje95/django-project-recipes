import csv
from django.core.management.base import BaseCommand
from recipes.models import Recipe


class Command(BaseCommand):
    help = 'Importa receitas a partir de um arquivo CSV'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV com receitas a serem importadas'
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                title = row['title']
                description = row['description']
                slug = row['slug']
                preparation_time = row['preparation time']
                preparation_time_unit = row['preparation time unit']
                servings = row['servings']
                servings_unit = row['servings unit']
                preparation_steps = row['preparation steps']

                # Mostra o título no terminal
                self.stdout.write(self.style.NOTICE(f'Importando: {title}'))

                Recipe.objects.create(
                    title=title,
                    description=description,
                    slug=slug,
                    preparation_time=preparation_time,
                    preparation_time_unit=preparation_time_unit,
                    servings=servings,
                    servings_unit=servings_unit,
                    preparation_steps=preparation_steps,
                )

        self.stdout.write(self.style.SUCCESS('Receitas importadas com sucesso!'))
