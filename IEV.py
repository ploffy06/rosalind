from helpers.file_read_helper import read_single_line

def expected_offspring(
        domdom_domdom, domdom_domrec, domdom_recrec,
        domrec_domrec, domrec_recrec, recrec_recrec
):
    expected_value = (
        (domdom_domdom * 1) +
        (domdom_domrec * 1) +
        (domdom_recrec * 1) +
        (domrec_domrec * 0.75) +
        (domrec_recrec * 0.5) +
        (recrec_recrec * 0)
    ) * 2

    return expected_value

if __name__ == '__main__':
    dd_dd, dd_dr, dd_rr, dr_dr, dr_rr, rr_rr = map(int, read_single_line())
    expected_offspring = expected_offspring(dd_dd, dd_dr, dd_rr, dr_dr, dr_rr, rr_rr)

    print(expected_offspring)