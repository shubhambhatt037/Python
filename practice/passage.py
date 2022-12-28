
str = '''However, Ram has been in the news for all the wrong reasons too.
Illiterate 
bigots have weaponized the slogan Jai Shri Ram for
wanton acts of violence, crime and hatred, which are anathema to
what Ram actually stands for. These lumpen elements do not know
that Ram is maryada purushottam, the epitome of rectitude, the
touchstone of impeccable behaviour, the role model of the perfect
human being, and the very incarnation of saumya rasa, harmonious
equilibrium. '''

result = []

b = str.count("Ram")
print(b)

c = str.replace("Ram","Shree Ram")
print(c)

print(sorted(str,reverse = True))