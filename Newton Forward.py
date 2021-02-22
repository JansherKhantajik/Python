
# newton forward interpolation

def u_cal(u, n):

	temp = u;
    for i in range(1, n):
		temp = temp * (u - i);
	return temp;


# calculating factorial of given number n
def fact(n):
    f = 1;
    for i in range(2, n + 1):
        f *= i;
    return f;


n = 5;
x = [1891, 1901, 1911, 1921, 1931];

y = [[0 for i in range(n)]
     for j in range(n)];
y[0][0] = 46;
y[1][0] = 66;
y[2][0] = 81;
y[3][0] = 93;
y[4][0] = 101;
# Calculating the forward difference
# table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1];

    # Displaying the forward difference table
for i in range(n):
    print(x[i], end="\t");
    for j in range(n - i):
        print(y[i][j], end="\t");
    print("");

# Value to interpolate at
value = 1925;

# initializing u and sum
sum = y[0][0];
u = (value - x[0]) / (x[1] - x[0]);
for i in range(1, n):
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i);

print("\nValue at", value,
      "is", round(sum, 6));
