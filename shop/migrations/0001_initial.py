# Generated by Django 4.2.11 on 2024-04-03 12:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Category Name"),
                ),
                (
                    "parent_category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="shop.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Product Title"),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Description"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Price"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
                (
                    "num_orders",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Number of Orders"
                    ),
                ),
                (
                    "categories",
                    models.ManyToManyField(related_name="products", to="shop.category"),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
        migrations.CreateModel(
            name="Shop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Shop Title")),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Description"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="shop_logos/", verbose_name="Shop Logo"
                    ),
                ),
            ],
            options={
                "verbose_name": "Shop",
                "verbose_name_plural": "Shops",
            },
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="product_images/", verbose_name="Product Image"
                    ),
                ),
                (
                    "is_main",
                    models.BooleanField(default=False, verbose_name="Main Image"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="shop.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Image",
                "verbose_name_plural": "Product Images",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="shop",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="shop.shop",
            ),
        ),
    ]
