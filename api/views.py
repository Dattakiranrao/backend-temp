from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer


@api_view(["GET"])
def getData(request):
    # person = {"name": "Datta", "age": 22}
    # tempItems = []
    items = Item.objects.all()
    # for item in items:
    #     if(item.dietType == "non vegetarian"):
    #         tempItems.append(item)

    serializer = ItemSerializer(items, many=True)
    # serializer = ItemSerializer(tempItems, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def addRecipe(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def getDiet(request):
    if request.method == "POST":
        diet = request.data["dietType"]
        tempItems = []
        items = Item.objects.all()
        for item in items:
            if item.dietType == diet:
                tempItems.append(item)
        serializer = ItemSerializer(tempItems, many=True)
        return Response(serializer.data)
