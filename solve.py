def wallpaper(l, w, h):
    # your code
    num2words1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    summary = ((l * h * 2 + w * h * 2) * 1.15 / 5.2)
    summary = round(summary)
    if 1 <= summary < 19:
        return num2words1[summary]
    elif 20 <= summary <= 99:
        tens, below_ten = divmod(summary, 10)
        return num2words2[tens - 2] + '-' + num2words1[below_ten]
