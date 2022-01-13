# - For the exercises below, we know:
#   - The probability that a customer buys RAM memory from an electronics store is P(RAM) = 0.0822.
#   - The probability that a customer buys a gaming laptop is P(GL) = 0.0184.
#   - The probability that a customer buys RAM memory given that they bought a gaming laptop is P(RAM | GL) = 0.0022.
# - Calculate:
#   - P(GL ∩ RAM) — assign your answer to p_gl_and_ram.
#   - P(RAMC | GL) — assign your answer to p_non_ram_given_gl.
#   - P(GL ∩ RAMC) — assign your answer to p_gl_and_non_ram..
def main():
    p_ram = 0.0822
    p_gl = 0.0184
    p_ram_given_gl = 0.0022

    p_gl_and_ram = p_gl * p_ram_given_gl
    p_non_ram_given_gl = 1 - p_ram_given_gl
    p_gl_and_non_ram = p_gl * p_non_ram_given_gl
    p_gl_or_ram = p_gl + p_ram - p_gl_and_ram

    print(p_gl_and_ram, p_non_ram_given_gl, p_gl_and_non_ram, p_gl_or_ram, sep='\n')


if __name__ == '__main__':
    main()
