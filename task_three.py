for a in range(1, 400):
    for b in range(1, 400):

        c = (1000 - a - b) #condition (iii)

        if a < b < c:

            if a * a + b * b == c * c:
                product_abc = a * b * c
                print("the product abc is,",product_abc)
