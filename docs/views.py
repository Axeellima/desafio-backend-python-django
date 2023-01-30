from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status

from .models import Doc
from .serializers import DocSerializer, DocListSerializer

from store.models import Store
from type.models import Type

import ipdb
import json


from rest_framework.generics import CreateAPIView, ListAPIView
# Create your views here.

class DocView(CreateAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocListSerializer

    def perform_create(self, serializer):
        save_serializers = []
        
        content = str(self.request.FILES["doc"].read(), 'utf-8')
        format_content = content.split('\r\n')

        for line in format_content:

            type = int(line[:1])

            event_date = line[1:5] + "-" + line[5:7] + "-" + line[7:9]

            value = line[9:19]

            cpf = line[19:30]

            card = line[30:42]

            hour = line[42:44] + ":" + line[44:46] + ":" + line[46:48]

            owner = line[48:62]

            store = line[62:]



            store = Store.objects.get_or_create(name=store)

            if(type):
                if(type == 1):
                    type = Type.objects.get_or_create(name="Debit", nature="Entry")
                elif(type == 2):
                    type = Type.objects.get_or_create(name="Bank slip", nature="Exit")
                elif(type == 3):
                    type = Type.objects.get_or_create(name="Financing", nature="Exit")
                elif(type == 4):
                    type = Type.objects.get_or_create(name="Credit", nature="Entry")
                elif(type == 5):
                    type = Type.objects.get_or_create(name="Loan Receipt", nature="Entry")
                elif(type == 6):
                    type = Type.objects.get_or_create(name="Sales", nature="Entry")
                elif(type == 7):
                    type = Type.objects.get_or_create(name="TED Recip", nature="Entry")
                elif(type == 8):
                    type = Type.objects.get_or_create(name="DOC Recip", nature="Entry")
                elif(type == 9):
                    type = Type.objects.get_or_create(name="Rent", nature="Exit")

                new_line = {}
                new_line["type"] = type[0]
                new_line["store"] = store[0]
                new_line["event_date"] = event_date
                new_line["hour"] = hour
                new_line["owner"] = owner
                new_line["card"] = card
                new_line["value"] = value
                new_line["cpf"] = cpf

                save_serializers.append(new_line)
                
                # serializer.save(type=type[0], store=store[0], event_date=event_date, hour=hour, owner=owner, card=card, value=value, cpf=cpf)
        serializer.save(data=save_serializers)

        return serializer.data