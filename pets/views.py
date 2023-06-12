from rest_framework.views import APIView, Request, Response, status
from .models import Pet
from groups.models import Group
from traits.models import Trait
from .serializers import PetSerializer


class PetView(APIView):
    def get(self, request: Request) -> Response:
        pets = Pet.objects.all()

        serializer = PetSerializer(instance=pets, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = PetSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        group_data = serializer.validated_data.pop("group")
        traits_data = serializer.validated_data.pop("traits")

        group_obj = Group.objects.filter(
            scientific_name__iexact=group_data["scientific_name"]
        ).first()

        if not group_obj:
            group_obj = Group.objects.create(**group_data)

        pet = Pet.objects.create(**serializer.validated_data, group=group_obj)

        for trait_dict in traits_data:
            trait_obj = Trait.objects.filter(name__iexact=trait_dict["name"]).first()

            if not trait_obj:
                trait_obj = Trait.objects.create(**trait_dict)

            pet.traits.add(trait_obj)

        serializer = PetSerializer(instance=pet)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
