from rest_framework import serializers
from .models import Store
import ipdb
class StoreSerializer(serializers.ModelSerializer):

    balance = serializers.SerializerMethodField("get_balance_value")
    list_order = serializers.SerializerMethodField("get_list_order")

    class Meta:
        model = Store
        fields = ["name", "balance", "list_order"]
        read_only_fields = ["balance", "list_order"]

    def get_balance_value(self, obj: Store):
        balance = 0
        array_value = []
        for newobj in obj.doc.all():
            value = int(newobj.value) / 100
            
            if(newobj.type.name == "Bank slip"):
                value = value * - 1
            elif(newobj.type.name == "Financing"):
                value = value * - 1
            elif(newobj.type.name == "Rent"):
                value = value * - 1
            
            array_value.append(value)

        for value in array_value:
            balance += value
        
        return round(balance, 2)

    def get_list_order(self, obj: Store):
        orders = []

        for doc in obj.doc.all():
            orders.append({
                "type": doc.type.name,
                "nature": doc.type.nature,
                "value" : round(int(doc.value) / 100, 2)
            })
        return orders