# dao - data access object
from connection import get_connection

def get_all_products(connection):
    cursor = connection.cursor()
    
    query = "SELECT product_id, name, uom_name, price_per_unit FROM gs.products inner join gs.uom ON products.uom_id = uom.uom_id;"

    cursor.execute(query)
    
    response = []
    
    for (product_id, name, uom_name, price_per_unit) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'uom_name': uom_name,
                'price_per_unit': price_per_unit
            }
        )
        
    return response


def insert_product (connection, product):
    cursor = connection.cursor()
    
    query = ("INSERT INTO products (name, uom_id, price_per_unit) values (%s, %s, %s);")
    # %s:- This are called parameterized values
    
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    
    cursor.execute(query, data)
    
    connection.commit()
    return cursor.lastrowid


def delete_row (connection, row_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products WHERE product_id = " + str(row_id) + ";")
    cursor.execute(query)
    connection.commit()



if __name__ == '__main__':
    connection = get_connection()
    
    # print(get_all_products(connection))
    
    # print(insert_product(connection, {
    #     'product_name': 'carrot',
    #     'uom_id': '1',
    #     'price_per_unit': '40'
    # }) )
    
    delete_row(connection, 3)
