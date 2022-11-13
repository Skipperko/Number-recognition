one_result = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
two_result = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
three_result = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
four_result = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
five_result = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
six_result = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
seven_result = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
eight_result = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
nine_result = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
zero_result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
bad_result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

numbers_result = [zero_result, one_result, two_result, three_result, four_result, five_result,
            six_result, seven_result, eight_result, nine_result, bad_result]

one = [0, 0, 1, 0,
        0, 1, 1, 0,
        1, 0, 1, 0,
        0, 0, 1, 0,
        0, 0, 1, 0,
        0, 0, 1, 0,
        0, 0, 1, 0]

two = [0, 1, 1, 0,
        1, 0, 0, 1,
        0, 0, 0, 1,
        0, 0, 1, 0,
        0, 1, 0, 0,
        1, 0, 0, 0,
        1, 1, 1, 1]

three = [0, 1, 1, 0,
        1, 0, 0, 1,
        0, 0, 0, 1,
        0, 0, 1, 0,
        0, 0, 0, 1,
        1, 0, 0, 1,
        0, 1, 1, 0]

four = [0, 0, 0, 1,
        0, 0, 1, 0,
        0, 1, 0, 0,
        1, 0, 0, 0,
        1, 1, 1, 1,
        0, 0, 1, 0,
        0, 0, 1, 0]

five = [1, 1, 1, 1,
        1, 0, 0, 0,
        1, 0, 0, 0,
        1, 1, 1, 0,
        0, 0, 0, 1,
        0, 0, 0, 1,
        1, 1, 1, 0]

six = [0, 1, 1, 0,
        1, 0, 0, 0,
        1, 0, 0, 0,
        1, 1, 1, 0,
        1, 0, 0, 1,
        1, 0, 0, 1,
        0, 1, 1, 0]

seven = [1, 1, 1, 1,
        0, 0, 0, 1,
        0, 0, 0, 1,
        0, 0, 1, 0,
        0, 1, 0, 0,
        1, 0, 0, 0,
        1, 0, 0, 0,]

eight = [0, 1, 1, 0,
        1, 0, 0, 1,
        1, 0, 0, 1,
        0, 1, 1, 0,
        1, 0, 0, 1,
        1, 0, 0, 1,
        0, 1, 1, 0]

nine = [0, 1, 1, 0,
        1, 0, 0, 1,
        1, 0, 0, 1,
        0, 1, 1, 1,
        0, 0, 0, 1,
        0, 0, 0, 1,
        0, 1, 1, 0]

zero = [0, 1, 1, 0,
        1, 0, 0, 1,
        1, 0, 0, 1,
        1, 0, 0, 1,
        1, 0, 0, 1,
        1, 0, 0, 1,
        0, 1, 1, 0]

numbers = [zero, one, two, three, four, five,
        six, seven, eight, nine]


noised_data = 0.4

one_noise = [0, 0, noised_data, 0,
        0, noised_data, noised_data, 0,
        noised_data, 0, noised_data, 0,
        0, 0, noised_data, 0,
        0, 0, noised_data, 0,
        0, 0, noised_data, 0,
        0, 0, noised_data, 0]

two_noise = [0, noised_data, noised_data, 0,
        noised_data, 0, 0, noised_data,
        0, 0, 0, noised_data,
        0, 0, noised_data, 0,
        0, noised_data, 0, 0,
        noised_data, 0, 0, 0,
        noised_data, noised_data, noised_data, noised_data]

three_noise = [0, noised_data, noised_data, 0,
        noised_data, 0, 0, noised_data,
        0, 0, 0, noised_data,
        0, 0, noised_data, 0,
        0, 0, 0, noised_data,
        noised_data, 0, 0, noised_data,
        0, noised_data, noised_data, 0]

four_noise = [0, 0, 0, noised_data,
        0, 0, noised_data, 0,
        0, noised_data, 0, 0,
        noised_data, 0, 0, 0,
        noised_data, noised_data, noised_data, noised_data,
        0, 0, noised_data, 0,
        0, 0, noised_data, 0]

five_noise = [noised_data, noised_data, noised_data, noised_data,
        noised_data, 0, 0, 0,
        noised_data, 0, 0, 0,
        noised_data, noised_data, noised_data, 0,
        0, 0, 0, noised_data,
        0, 0, 0, noised_data,
        noised_data, noised_data, noised_data, 0]

six_noise = [0, noised_data, noised_data, 0,
        noised_data, 0, 0, 0,
        noised_data, 0, 0, 0,
        noised_data, noised_data, noised_data, 0,
        noised_data, 0, 0, noised_data,
        noised_data, 0, 0, noised_data,
        0, noised_data, noised_data, 0]

seven_noise = [noised_data, noised_data, noised_data, noised_data,
        0, 0, 0, noised_data,
        0, 0, 0, noised_data,
        0, 0, noised_data, 0,
        0, noised_data, 0, 0,
        noised_data, 0, 0, 0,
        noised_data, 0, 0, 0,]

eight_noise = [0, noised_data, noised_data, 0,
        noised_data, 0, 0, noised_data,
        noised_data, 0, 0, noised_data,
        0, noised_data, noised_data, 0,
        noised_data, 0, 0, noised_data,
        noised_data, 0, 0, noised_data,
        0, noised_data, noised_data, 0]

nine_noise = [0, noised_data, noised_data, 0,
        noised_data, 0, 0, noised_data,
        noised_data, 0, 0, noised_data,
        0, noised_data, noised_data, noised_data,
        0, 0, 0, noised_data,
        0, 0, 0, noised_data,
        0, noised_data, noised_data, 0]

zero_noise = [0, noised_data, noised_data, 0,
        noised_data, 0, 0, noised_data,
        noised_data, 0, 0, noised_data,
        noised_data, 0, 0, noised_data,
        noised_data, 0, 0, noised_data,
        noised_data, 0, 0, noised_data,
        0, noised_data, noised_data, 0]

noised_numbers = [zero_noise, one_noise, two_noise, three_noise, four_noise,
                  five_noise, six_noise, seven_noise, eight_noise, nine_noise]