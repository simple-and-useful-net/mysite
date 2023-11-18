from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def reg(request):

    context={
    }

    return render(request, "reg.html", context )    


def temp(request):

    # 顧客データを辞書型で定義
    cust_data = [
        {'name': '顧客1', 'email': 'customer1@example.com', 'phone': '123-456-7890', 'address': '住所1'},
        {'name': '顧客2', 'email': 'customer2@example.com', 'phone': '234-567-8901', 'address': '住所2'},
        {'name': '顧客3', 'email': 'customer3@example.com', 'phone': '345-678-9012', 'address': '住所3'},
        {'name': '顧客4', 'email': 'customer4@example.com', 'phone': '456-789-0123', 'address': '住所4'},
        {'name': '顧客5', 'email': 'customer5@example.com', 'phone': '567-890-1234', 'address': '住所5'},
        {'name': '顧客6', 'email': 'customer6@example.com', 'phone': '678-901-2345', 'address': '住所6'},
        {'name': '顧客7', 'email': 'customer7@example.com', 'phone': '789-012-3456', 'address': '住所7'},
        {'name': '顧客8', 'email': 'customer8@example.com', 'phone': '890-123-4567', 'address': '住所8'},
        {'name': '顧客9', 'email': 'customer9@example.com', 'phone': '901-234-5678', 'address': '住所9'},
        {'name': '顧客10', 'email': 'customer10@example.com', 'phone': '012-345-6789', 'address': '住所10'},
    ]

    # キーの順番を指定
    key_order = ['name', 'phone', 'email']

    rows_data=[]
    for ix in range( len(cust_data) ):
        # キーの順番でリスト化
        order_data = [cust_data[ix][key] for key in key_order]
        rows_data.append(order_data)
        
    context={
        "name":"山田2",
        "nums": [1,2,3,4,5],
        "rows": rows_data,

        "rows_test":[
                ["col11", "col12"],
                ["col21", "col22"],
        ]
    }

    return render(request, "index.html", context )

# テスト    

