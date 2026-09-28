## 1.No Group
I did this assignment by myself with no group. Arnt Htoo Lwin-6705142035

## 2.Who Did What

| Member | GitHub Username | File |
| --- | --- | --- |
| Arnt Htoo Lwin | 123De-Ge | bank.py test_deposit.py test_withdraw.py |
| Arnt Htoo Lwin 2 | Perkins-23 | test_teardown.py conftest.py |
| Arnt Htoo Lwin 3 | Ali-969 | test_shared.py |

## 3.Our Merge Conflict

I test conflict markers with three terminals,in terminal1 I 'push' with adding first row. 
In terminal2, edit that file by adding 2nd row and 'add & commit', then 'pull'.
After 'pull','conflict markers' happened as '<<<<<<< HEAD' before line from terminal2.
After row2, appear as "=======". Then 'pushed' row1, at the end ">>>>>>> 2e6ab560ee982892675fcbcaa90a96352eca751d".
In terminal3, the same markers happened when no initailising 'pull' has made. I edited into the correct table structure as shown in this file.
The reason is in one terminal, it is already pushed, but in other, it is not saved yet, it remains as the older one.
So, in that other one, when you pull the edition made is in same place as the pushed one.
Then the conflict happened. In order to avoid that, before add or commit, we should pull first.

## 4.Git Contribution Summary
     9  Arnt Htoo Lwin
     3  Arnt Htoo Lwin 2
     3  Arnt Htoo Lwin 3
     1  MrF

MrF(my display name, initial commit)
This result is before one last commitment to this file, so could be 10 Arnt Htoo Lwin after this.

## 5.Answers for Reflection Questions

1.My push failed because GitHub contains commits that your local folder doesn't have yet. I solved it using 'git pull origin main --no-rebase', it means GitHub to take my online and local history and create a Merge Commit.

2.The reason is in one terminal, it is already pushed, but in other, it is not saved yet, it remains as the older one. So, in that other one, when you pull the edition made is in same place as the pushed one.

3.Committing saves the code changes locally on local machine, it is like a checkpoint before actual changes.
Pushing takes those saved changes and uploads them to GitHub so who have accesses to repository can see those changes.

4.Fixtures allow to write setup code just once in a central place. Pytest then automatically injects that ready-made setup into any test that needs it, keeping test files clean and free of repetitive code.
