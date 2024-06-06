from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


class Picture(models.Model):
    name = models.CharField(max_length=128, verbose_name=_("name"))
    image = FilerImageField(
        verbose_name=_("image"),
        related_name="image",
        on_delete=models.CASCADE
    )
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name=_("order")
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _("picture")
        verbose_name_plural = _("pictures")
        ordering = ['my_order']
