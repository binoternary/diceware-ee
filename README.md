# diceware-ee
Eestikeelsete sõnade loend parooli loomiseks diceware meetodiga.

*Diceware*-i kirjeldus:  
http://world.std.com/~reinhold/diceware.html

Esialgse sõnaloendi allikas:  
http://www.eki.ee/tarkvara/wordlist/

Loendi filtreerimine:  
`cat lemmad.txt | egrep "^[aeh-pr-st-võäöü][abd-pr-võäöü]{2,5}[^ma]$" > lihtsad-lemmad.txt`  

Filtreeritud loendist indekseeritud nimekirja tegemine:  
`python3 sonad.py lihtsad-lemmad.txt > diceware-ee.txt`

Tulemus: [diceware-ee.txt](https://github.com/binoternary/diceware-ee/blob/master/diceware-ee.txt)
