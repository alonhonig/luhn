# NPI Luhn Algorithm
## Intro
This code validates National Provider Identifiers ([NPI](https://en.wikipedia.org/wiki/National_Provider_Identifier)) assigned by the Centers for Medicare and Medicaid Services ([CMS](http://en.wikipedia.org/wiki/Centers_for_Medicare_and_Medicaid_Services)). It uses the [Luhn Algorithm](http://en.wikipedia.org/wiki/Luhn_algorithm) to see if the first nine digits create a valid checksum with the final digit. For more details on the algorithm and its implementation, see official [guidelines](https://www.cms.gov/Regulations-and-Guidance/Administrative-Simplification/NationalProvIdentStand/Downloads/NPIcheckdigit.pdf)
## Usage
### Test
```python
# note: requires python 2.6+
from luhn import NPI

# Creating test identifiers
test_ids = [1356320139,
            1285849489,
            1265795159,
            1922087766,
            1932224400,
            1467538918,
            1861414096,
            1528142197,
            1306070885,
            141799038,
            1144258609,
            1467446575,
            1285652024,
            1104084334,
            144750284,
            1356585673,
            1740232941,
            1992776843,
            1215965934,
            1154348176,
            1558598797]
            
# printing the results
for i in test_ids:
      try:
            n = NPI(i)
            n.validate_input()
            print str(i) + " - " + str(n.luhn())
        except:
            print str(i) + " - False"

```
### Output
```BASH
1356320139 - True
1285849489 - True
1265795159 - False
1922087766 - True
1932224400 - False
1467538918 - True
1861414096 - True
1528142197 - True
1306070885 - False
141799038 - False
1144258609 - True
1467446575 - True
1285652024 - True
1104084334 - True
144750284 - False
1356585673 - True
1740232941 - True
1992776843 - True
1215965934 - True
1154348176 - False
1558598797 - True
```