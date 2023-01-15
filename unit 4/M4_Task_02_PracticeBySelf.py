# Print First word of the string

# import re
# result = re.findall(r'^\w+','Good Going Python')
# print(result)

# Extract all the words of a given string

# import re
# result = re.split("\s", "Good Going Python")
# print(result)

# Extract domain name from given email id's

# import re
txt = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
20-11-2020
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''

# result = re.findall(r'@\w+', txt)
# print(result)

# Extract date from given string

# import re 
# result = re.findall("\d{2}-\d{2}-\d{4}",txt)
# print(result)

# return all the words of a string that starts with vowel

# import re
# result = re.findall(r'\b[aeiouAEIOU]\w+', txt)
# print(result)

# Split a string with multiple delimiters

import re
text = "Hello, World! How are you. I'm fine!"
split = re.split(",|\.|!", text)
print(split)