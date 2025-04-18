def get_cart(session):
    return session.get('cart', {})

def save_cart(session, cart):
    session['cart'] = cart
    session.modified = True

def add_to_cart(session, product):
    cart = get_cart(session)
    product_id = str(product.id)
    
    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
            'image': product.image.url
        }

    save_cart(session, cart)

def remove_from_cart(session, product_id):
    cart = get_cart(session)
    product_id = str(product_id)
    if product_id in cart:
        del cart[product_id]
        save_cart(session, cart)
