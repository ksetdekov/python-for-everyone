text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
remain = float(text[pos + 1:])
print(remain)
