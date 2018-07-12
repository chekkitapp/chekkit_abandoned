from django.forms import ModelForm
from .models import Manufacturer, Product, Batches, Articles 


#Create the form class.
class ManufacturerForm(ModelForm):
	class Meta:
		model = Manufacturer
		fields = ['name','email', 'phonenumber', 'industry', 'address','code', ]

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields =




# >>> class ArticleForm(ModelForm):
# ...     class Meta:
# ...         model = Article
# ...         fields = ['pub_date', 'headline', 'content', 'reporter']

# # Creating a form to add an article.
# >>> form = ArticleForm()

# # Creating a form to change an existing article.
# >>> article = Article.objects.get(pk=1)
# >>> form = ArticleForm(instance=article)