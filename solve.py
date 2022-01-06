from math import ceil
def wallpaper(l, w, h):
    # your code
    num2words1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty'}
    if l*w*h==0 :
        return "zero"
    summary = (2 * (l + w) * h / 5.2 * 1.15)
    summary = ceil(summary)
    if summary>0:
        return num2words1[summary]
    
