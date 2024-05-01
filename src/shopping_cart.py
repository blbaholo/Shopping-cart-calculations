import json


def shopping_baskets():
    with open("data/data.json", "r+") as read_file:
        data = json.load(read_file)
    return data


def get_customer_baskets(email, shopping_baskets):
    list_of_baskets = [
        basket
        for basket in shopping_baskets()
        if basket["email"] == email
    ]
    return list_of_baskets


def get_all_customers(shopping_baskets):
    list_of_emails = []
    for basket in shopping_baskets():
        if basket["email"] not in list_of_emails:
            list_of_emails.append(basket["email"])
        
    return sorted(list_of_emails)


def required_stock(shopping_baskets):
    items = []
    for basket in shopping_baskets():
        if basket["status"] == "PAID":
            for item in basket["items"]:
                items.append({"name": item["name"], "quantity": item["quantity"]})
    stock_dict = {}
    for item in items:
        name = item['name']
        quantity = item['quantity']
        if name not in stock_dict.keys():
            stock_dict[name] = stock_dict.get('name', 0)
            stock_dict[name] += quantity
        else:
            stock_dict[name] +=quantity
    return [{"name":name, "quantity": stock_dict[name]} for name in stock_dict]


def total_spent(email, shopping_baskets):
    total = 0
    for basket in get_customer_baskets(email, shopping_baskets):
        if basket["status"] != "OPEN":
            for item in basket["items"]:
                total += item["price"] * item["quantity"]
    return total


def top_customers(shopping_baskets):
    list_of_customers = [
        {"email": email, "total": total_spent(email, shopping_baskets)}
        for email in get_all_customers(shopping_baskets)
    ]
    return sorted(
        list_of_customers, key=lambda customer: customer["total"], reverse=True
    )


def get_customers_with_open_baskets(shopping_baskets):
    customers_with_open_baskets = []
    for basket in shopping_baskets():
        if basket["status"] == "OPEN" and basket['email'] not in customers_with_open_baskets:
            customers_with_open_baskets.append(basket["email"])
    return sorted(customers_with_open_baskets)



    