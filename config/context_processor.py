from app.models.product import Category


def categories_context(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return context
