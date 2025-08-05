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



if __name__ == '__main__':
    connection = get_connection()
    print(get_all_products(connection))
