from django.db import models
from django.utils.translation import gettext_lazy as _

class Shop(models.Model):
    title = models.CharField(_("Shop Title"), max_length=255)
    description = models.CharField(_("Description"), blank=True, max_length=255)
    image = models.ImageField(_("Shop Logo"), upload_to="shop_logos/", blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Shop")
        verbose_name_plural = _("Shops")

class Category(models.Model):
    title = models.CharField(_("Category Name"), max_length=255)
    parent_category = models.ForeignKey("self", on_delete = models.CASCADE, null=True, blank=True, related_name="children")


    def __str__(self):
        return self.title
    
    def get_all_parents(self):
        parents = [self]
        while self.parent_category:
            self = self.parent_category
            parents.append(self)
        return parents[::-1]
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="products")
    title = models.CharField(_("Product Title"), max_length=255)
    description = models.TextField(_("Description"), blank=True)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    is_active = models.BooleanField(_("Is Active"), default=True)
    num_orders = models.PositiveIntegerField(_("Number of Orders"), default=0)
    categories = models.ManyToManyField(Category, related_name="products")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = "images")
    image = models.ImageField(_("Product Image"), upload_to="product_images/")
    is_main = models.BooleanField(_("Main Image"), default=False)

    def __str__(self):
        return f"{self.product.title} - Image {self.pk}"
    
    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
