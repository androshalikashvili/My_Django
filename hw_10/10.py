import requests

def get_products():
    try:
        api_url = "https://fakestoreapi.com/products"
        response = requests.get(api_url)

        if response.status_code == 200:
            return response.json()
        
    except requests.exceptions.HTTPError as err:
        print(f"Http error: {err}")
    except requests.exceptions.ConnectionError as con_err:
        print(f"Connection error: {con_err}")
    except Exception as err:
        print(f"Something went wrong: {err}")


def parsing_price():
    products = get_products()

    if products:
        # Extracting product prices and IDs
        products_price = [{"title": product["title"], "price": product["price"]} for product in products]
                
        # Sorting products by price
        sorted_products = sorted(products_price, key=lambda x: x['price'])
        lowest_price = [item['price'] for item in sorted_products]
        x = len(sorted_products)
        total_price = 0
        # max_price = 0

        print('\n')
        print("  Products Name", ' ' * 82, 'Price' )
        print('=' * 110)
        for product in sorted_products:
            # max_price = int(product['price'])        
            total_price += product['price']
            print(f"  {product['title']:<97}{product['price']}")

        average_price = total_price / x
        print('=' * 110)
        print(f'Min_Price: {lowest_price[0]}')
        # print(f'Max_Price: {max_price}')
        print(f'Max_Price: {lowest_price[-1]}')
        print(f'Average_Price: {average_price}', '\n')

        # print(sorted_products)


def parse_category():
    products = get_products()
    
    # Extracting product Categorys
    # products_category = [{"title": product["category"]} for product in products]
    product_category = set()

    for product in products:
        product_category.add(product['category'])

    sort_category = sorted(product_category)

    print(*sort_category)


def parse_title():
    products = get_products()

    # print(products[0].keys(), "\n")

    if products:
        # Extracting product title and IDs
        products_title = [{"title": product["title"], "ID": product["id"]} for product in products]
                
        # Sorting products by price
        sorted_title = sorted(products_title, key=lambda x: x['title'])

        print('\n')
        print('  ID', ' ' * 10, 'Products Title')
        print('=' * 93)
        for product in sorted_title:
            print(f"  {product['ID']:<5} {product['title']}")

        # print(*sorted_title)


def parse_rating():
    products = get_products()

    # print(products[0].keys(), "\n")

    if products:
        # Extracting product ratings
        products_rating = [product['rating'] for product in products]
        sorted_rating = sorted(products_rating, key=lambda x: x['rate'])
                
        # Sorting products by price
        # sorted_rating = sorted(products_rating)
        
        print('\n')
        print('  Rate', ' ' * 10, 'Count')
        print('=' * 24)
        for product in sorted_rating:
            print(f"  {product['rate']:<15} {product['count']}")

        # print(sorted_rating)
        # print(products_rating)

# Call the parsing function to execute the code
            
# parsing_price()
# parse_category()
# parse_title()
parse_rating()
