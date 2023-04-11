from django.utils.translation import gettext_lazy as _


class FormFields:
    def __init__(self):

        self.category_name = _('CategoryName')

        self.product_name = _('ProductName')
        self.product_description = _('ProductDescription')
        self.product_price = _('ProductPrice')
        self.product_category = _('ProductCategory')
