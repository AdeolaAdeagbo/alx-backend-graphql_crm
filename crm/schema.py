from graphene import ObjectType, Mutation, String, Int, List, Field
import graphene

# Mock data for demonstration
class Product(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    stock = graphene.Int()

# Global sample list (for simulation)
PRODUCTS = [
    {"id": 1, "name": "Laptop", "stock": 5},
    {"id": 2, "name": "Phone", "stock": 15},
    {"id": 3, "name": "Tablet", "stock": 8},
]

class UpdateLowStockProducts(Mutation):
    class Arguments:
        pass

    success = graphene.String()
    updated_products = List(Product)

    def mutate(self, info):
        updated = []
        for product in PRODUCTS:
            if product["stock"] < 10:
                product["stock"] += 10
                updated.append(product)
        return UpdateLowStockProducts(
            success="Low stock products updated successfully!",
            updated_products=[Product(**p) for p in updated]
        )

class Mutation(ObjectType):
    update_low_stock_products = UpdateLowStockProducts.Field()

class Query(ObjectType):
    hello = String(default_value="Hello from GraphQL!")

schema = graphene.Schema(query=Query, mutation=Mutation)
