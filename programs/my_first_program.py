from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Compute the average of my_int1 and my_int2
    average = (my_int1 + my_int2) / 2

    # Output the computed average securely to Party1
    return [Output(average, "average_output", party1)]
