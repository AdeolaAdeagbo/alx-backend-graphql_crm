import graphene
from graphene_django import DjangoObjectType
from crm.models import Product

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "price", "stock")

class UpdateLowStockProducts(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        threshold = graphene.Int(required=True)
        new_stock = graphene.Int(required=True)

    def mutate(self, info, threshold, new_stock):
        low_stock_products = Product.objects.filter(stock__lt=threshold)
        for product in low_stock_products:
            product.stock = new_stock
            product.save()
        return UpdateLowStockProducts(success=True)

class Mutation(graphene.ObjectType):
    update_low_stock_products = UpdateLowStockProducts.Field()

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello from CRM!")

schema = graphene.Schema(query=Query, mutation=Mutation)
