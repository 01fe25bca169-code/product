from product import product_details


def test_product_details():
    result = product_details(10, "book", 2, 1500)

    expected = (
        "Product ID: 10\n"
        "Product Name: book\n"
        "Quantity: 2\n"
        "Price: 1500"
    )

    assert result == expected