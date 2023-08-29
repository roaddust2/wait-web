import factory
from django.utils.text import slugify
from io import BytesIO
from PIL import Image
from app.models.home import CarouselItem
from app.models.product import Category, Product, ProductFeature, ProductImage
from django.core.files.uploadedfile import SimpleUploadedFile


def create_image(name: str, size: tuple) -> SimpleUploadedFile:
    """Function that creates image for testing purposes"""
    img_data = BytesIO()
    image = Image.new('RGB', size=size)
    image.save(img_data, format='JPEG')
    return SimpleUploadedFile(name.lower().replace(" ", "_"), img_data.getvalue())


class CarouselItemFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CarouselItem

    label = factory.Sequence(lambda n: 'Label %d' % n)
    placeholder = factory.Sequence(lambda n: 'Placeholder %d' % n)
    text_color = 'dark'
    link = None
    image_alt = factory.Sequence(lambda n: 'Image alt text %d' % n)
    priority = factory.Sequence(lambda n: n)

    @factory.lazy_attribute
    def image(self):
        image = create_image(f'image_{self.label}.jpg', (416, 624))
        return image


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category

    name = factory.Sequence(lambda n: 'Name %d' % n)
    description = factory.Sequence(lambda n: 'Description %d' % n)
    image_alt = factory.Sequence(lambda n: 'Image alt text %d' % n)

    @factory.lazy_attribute
    def category_slug(self):
        return slugify(self.name)

    @factory.lazy_attribute
    def image(self):
        image = create_image(f'image_{self.name}.jpg', (200, 200))
        return image


class ProductFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Product
        skip_postgeneration_save = True

    name = factory.Sequence(lambda n: 'Name %d' % n)
    description = factory.Sequence(lambda n: 'Description %d' % n)
    price = factory.Sequence(lambda n: n)

    @factory.lazy_attribute
    def category(self):
        if Category.objects.exists():
            return Category.objects.first()
        else:
            return CategoryFactory.create()

    @factory.lazy_attribute
    def product_slug(self):
        return slugify(self.name)

    @factory.post_generation
    def create_features_and_images(self, create, extracted, **kwargs):
        if not create:
            return
        ProductFeatureFactory.create_batch(3, product=self)
        ProductImageFactory.create(product=self, default=True)
        ProductImageFactory.create_batch(2, product=self)


class ProductFeatureFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ProductFeature

    feature = factory.Sequence(lambda n: 'Feature %d' % n)
    product = factory.SubFactory(ProductFactory)


class ProductImageFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ProductImage

    image_alt = factory.Sequence(lambda n: 'Image alt text %d' % n)
    product = factory.SubFactory(ProductFactory)
    default = False

    @factory.lazy_attribute
    def image(self):
        image = create_image(f'image_{self.product.name}.jpg', (200, 200))
        return image


class ProductSoldFactory(ProductFactory):

    sold = True
