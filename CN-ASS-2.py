def tanh(x):
    exp_pos = 2.718281828459 ** x
    exp_neg = 2.718281828459 ** (-x)
    return (exp_pos - exp_neg) / (exp_pos + exp_neg)

def tanh_derivative(x):
    return 1 - (tanh(x) ** 2)

w = [0.1498, 0.1996, 0.2498, 0.2996, 0.3587, 0.4082, 0.5111, 0.5610]
i = [0.05, 0.10]
eta = 0.5

out_h1 = 0.5933
out_h2 = 0.5969
dE_total_dout_h1 = 0.0364
dE_total_dout_h2 = 0.0296

dout_h1_dnet_h1 = out_h1 * (1 - out_h1)
dout_h2_dnet_h2 = out_h2 * (1 - out_h2)

dE_total_dw = [0.0] * 8
dE_total_dw[0] = dE_total_dout_h1 * dout_h1_dnet_h1 * i[0]
dE_total_dw[1] = dE_total_dout_h1 * dout_h1_dnet_h1 * i[1]
dE_total_dw[2] = dE_total_dout_h2 * dout_h2_dnet_h2 * i[0]
dE_total_dw[3] = dE_total_dout_h2 * dout_h2_dnet_h2 * i[1]
dE_total_dw[4] = dE_total_dout_h1 * dout_h1_dnet_h1 * i[0]
dE_total_dw[5] = dE_total_dout_h1 * dout_h1_dnet_h1 * i[1]
dE_total_dw[6] = dE_total_dout_h2 * dout_h2_dnet_h2 * i[0]
dE_total_dw[7] = dE_total_dout_h2 * dout_h2_dnet_h2 * i[1]

for idx in range(len(w)):
    w[idx] -= eta * dE_total_dw[idx]

print(f"w1: {w[0]:.4f}")
print(f"w2: {w[1]:.4f}")
print(f"w3: {w[2]:.4f}")
print(f"w4: {w[3]:.4f}")
print(f"w5: {w[4]:.4f}")
print(f"w6: {w[5]:.4f}")
print(f"w7: {w[6]:.4f}")
print(f"w8: {w[7]:.4f}")
