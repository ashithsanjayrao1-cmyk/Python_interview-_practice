def create_multiplier(n):
    def multiplirt(x):
        return x * n
    return multiplirt

double = create_multiplier(2)
print(double)