from fractions import Fraction

# favorable outcomes
# Calculate the probability for each scenario
P1 = Fraction(4, 7) * Fraction(5, 9) * Fraction(4, 8)
P2 = Fraction(4, 7) * Fraction(4, 9) * Fraction(4, 8)
P3 = Fraction(3, 7) * Fraction(5, 9) * Fraction(4, 8)

# Sum the probabilities of each scenario to get the total probability
P_total = P1 + P2 + P3

print(P_total)


