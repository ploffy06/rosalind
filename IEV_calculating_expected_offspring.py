domdom_domdom = 18147
domdom_domrec = 17286
domdom_recrec = 19906
domrec_domrec = 19987
domrec_recrec = 17174
recrec_recrec = 17017

expected_value = (
    (domdom_domdom * 1) +
    (domdom_domrec * 1) +
    (domdom_recrec * 1) +
    (domrec_domrec * 0.75) +
    (domrec_recrec * 0.5) +
    (recrec_recrec * 0)
) * 2

print(expected_value)