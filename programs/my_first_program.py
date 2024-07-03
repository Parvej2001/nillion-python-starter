from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Define secret integer inputs for each party
    my_int1_party1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2_party1 = SecretInteger(Input(name="my_int2", party=party1))

    my_int1_party2 = SecretInteger(Input(name="my_int1", party=party2))
    my_int2_party2 = SecretInteger(Input(name="my_int2", party=party2))

    # Perform some computation involving the inputs
    sum_party1 = my_int1_party1 + my_int2_party1
    product_party2 = my_int1_party2 * my_int2_party2

    # Output the results for each party
    outputs = [
        Output(sum_party1, "sum_output", party1),
        Output(product_party2, "product_output", party2)
    ]

    return outputs
