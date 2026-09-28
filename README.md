## Who Did What

| Member | GitHub Username | File |
| --- | --- | --- |
| Arnt Htoo Lwin | 123De-Ge | bank.py test_deposit.py test_withdraw.py |
| Arnt Htoo Lwin 2 | Perkins-23 | test_teardown.py conftest.py |
| Arnt Htoo Lwin 3 | Ali-969 | test_shared.py |

## Our Merge Conflict

I test conflict markers with three terminals,in terminal1 I 'push' with adding first row. 
In terminal2, edit that file by adding 2nd row and 'add & commit', then 'pull'.
After 'pull','conflict markers' happened as '<<<<<<< HEAD' before line from terminal2.
After row2, appear as "=======". Then 'pushed' row1, at the end ">>>>>>> 2e6ab560ee982892675fcbcaa90a96352eca751d".
In terminal3, the same markers happened when no initailising 'pull' has made. I edited into the correct table structure as shown in this file.
The reason is in one terminal, it is already pushed, but in other, it is not saved yet, it remains as the older one.
So, in that other one, when you pull the edition made is in same place as the pushed one.
Then the conflict happened. In order to avoid that, before add or commit, we should pull first.
