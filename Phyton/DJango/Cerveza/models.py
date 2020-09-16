from django.db import models
from Cerveza.utils import image_upload_location

# Create your models here.
from core.models import CommonInfo


class compañia(CommonInfo):
    name = models.CharField('Name', max_length=50)
    tax_number = models.IntegerField('Tax_Number', max_length=5, unique=True)

    class Meta:
        verbose_name = "Compañia"  # Nombre de la clase en Singular
        verbose_name_plural = "Compañias"  # Nombre de la clase en Plural
        ordering = ['name']  # Orden de vista, '-' invertimos el sentido

    def __str__(self):
        return self.name


class cerveza(CommonInfo):

    COLOR_YELLOW = 1
    COLOR_AMBER = 2
    COLOR_BROWN = 3
    COLOR_BLACK = 4

    COLOR_CHOICES = (
        (COLOR_YELLOW, 'Yellow'),
        (COLOR_AMBER, 'Amber'),
        (COLOR_BROWN, 'Brown'),
        (COLOR_BLACK, 'Black')
    )

    name = models.CharField('Name', max_length=50)
    abv = models.DecimalField('Alcohol by volume', max_digits=5, decimal_places=2, default=0)
    color = models.PositiveSmallIntegerField('Color', choices=COLOR_CHOICES, default=COLOR_YELLOW)
    is_filtered = models.BooleanField("Is filtered?", default=False)
    image = models.ImageField("Image", blank=True, null=True, upload_to=image_upload_location)
    company = models.ForeignKey(compañia, related_name="cervezas", on_delete=models.CASCADE)

    class Meta:

            verbose_name = "Cerveza"    # Nombre de la clase en Singular
            verbose_name_plural = "Cervezas"  # Nombre de la clase en Plural
            ordering = ['name']   #Orden de vista, '-' invertimos el sentido

    def __str__(self):
        return self.name

    #Propiedad
    @property
    def is_alcoholic(self):
        return self.abv > 0

    def has_more_alcohol_than(self, alcohol):
        return self.abv > alcohol


class specialIngridients(CommonInfo):
    name = models.CharField('Name', max_length=50)
    cerveza = models.ManyToManyField(cerveza,blank=True, related_name="especial_cerveza_ingredients")

    class Meta:
        verbose_name = "Ingrediente_Especial"  # Nombre de la clase en Singular
        verbose_name_plural = "Ingredientes_Especiales"  # Nombre de la clase en Plural
        ordering = ['name']  # Orden de vista, '-' invertimos el sentido

    def __str__(self):
        return self.name