"""
These are the names of fields for which I want to generate the dummy data

"name", "age", "state", "vote_date", "given_review", "party"

Fields and there meanings:

- name is voter's name.
- age is voter's age, always greater than 17 and less than 100. Datatype int.
- state is the valid state abbrevation for the India country. Ex: MH, DL etc.
- vote_date is date in format - "YYYY-MM-DD". The valid dates varies from  "2026-09-01" to "2026-09-30"
- given_review is boolean flag showing if person has given the after poll reviews
- party is the name of party the user has revealed to whom they have voted in poll reviews. Only present if given_review is True. Valid values are: BJP, Congress, JDP, JDU etc.

I need the data in list of dict format in Python. Need atleast 20 Records.

"""
data = [
    {
        "name": "Aarav Sharma",
        "age": 25,
        "state": "MH",
        "vote_date": "2026-09-05",
        "given_review": True,
        "party": "BJP"
    },
    {
        "name": "Priya Patel",
        "age": 34,
        "state": "GJ",
        "vote_date": "2026-09-12",
        "given_review": False
    },
    {
        "name": "Rahul Verma",
        "age": 42,
        "state": "DL",
        "vote_date": "2026-09-18",
        "given_review": True,
        "party": "Congress"
    },
    {
        "name": "Sneha Reddy",
        "age": 19,
        "state": "TS",
        "vote_date": "2026-09-22",
        "given_review": False
    },
    {
        "name": "Vikram Singh",
        "age": 67,
        "state": "RJ",
        "vote_date": "2026-09-29",
        "given_review": True,
        "party": "JDU"
    },
    {
        "name": "Aarav Sharma",
        "age": 28,
        "state": "MH",
        "vote_date": "2026-09-03",
        "given_review": True,
        "party": "BJP"
    },
    {
        "name": "Priya Verma",
        "age": 34,
        "state": "DL",
        "vote_date": "2026-09-05",
        "given_review": False
    },
    {
        "name": "Rahul Patil",
        "age": 42,
        "state": "MH",
        "vote_date": "2026-09-08",
        "given_review": True,
        "party": "Congress"
    },
    {
        "name": "Sneha Singh",
        "age": 23,
        "state": "UP",
        "vote_date": "2026-09-12",
        "given_review": True,
        "party": "JDU"
    },
    {
        "name": "Vikram Reddy",
        "age": 51,
        "state": "TS",
        "vote_date": "2026-09-15",
        "given_review": False
    },
    {
        "name": "Ananya Nair",
        "age": 31,
        "state": "KL",
        "vote_date": "2026-09-01",
        "given_review": True,
        "party": "Congress"
    },
    {
        "name": "Rohan Deshmukh",
        "age": 19,
        "state": "MH",
        "vote_date": "2026-09-21",
        "given_review": False
    },
    {
        "name": "Kavita Joshi",
        "age": 46,
        "state": "GJ",
        "vote_date": "2026-09-18",
        "given_review": True,
        "party": "BJP"
    },
    {
        "name": "Arjun Mehta",
        "age": 37,
        "state": "RJ",
        "vote_date": "2026-09-09",
        "given_review": True,
        "party": "JDP"
    },
    {
        "name": "Meera Iyer",
        "age": 29,
        "state": "TN",
        "vote_date": "2026-09-25",
        "given_review": False
    },
    {
        "name": "Suresh Kumar",
        "age": 63,
        "state": "AP",
        "vote_date": "2026-09-07",
        "given_review": True,
        "party": "JDU"
    },
    {
        "name": "Neha Gupta",
        "age": 26,
        "state": "HR",
        "vote_date": "2026-09-14",
        "given_review": False
    },
    {
        "name": "Aditya Das",
        "age": 40,
        "state": "WB",
        "vote_date": "2026-09-19",
        "given_review": True,
        "party": "Congress"
    },
    {
        "name": "Pooja Yadav",
        "age": 33,
        "state": "BR",
        "vote_date": "2026-09-22",
        "given_review": True,
        "party": "JDU"
    },
    {
        "name": "Karan Malhotra",
        "age": 55,
        "state": "PB",
        "vote_date": "2026-09-11",
        "given_review": False
    },
    {
        "name": "Divya Rao",
        "age": 21,
        "state": "KA",
        "vote_date": "2026-09-27",
        "given_review": True,
        "party": "BJP"
    },
    {
        "name": "Manoj Thakur",
        "age": 72,
        "state": "HP",
        "vote_date": "2026-09-16",
        "given_review": False
    },
    {
        "name": "Ishita Roy",
        "age": 24,
        "state": "AS",
        "vote_date": "2026-09-06",
        "given_review": True,
        "party": "JDP"
    },
    {
        "name": "Nikhil Jain",
        "age": 48,
        "state": "MP",
        "vote_date": "2026-09-29",
        "given_review": True,
        "party": "Congress"
    },
    {
        "name": "Simran Kaur",
        "age": 36,
        "state": "CH",
        "vote_date": "2026-09-10",
        "given_review": False
    },
    {
        "name": "Deepak Mishra",
        "age": 59,
        "state": "OD",
        "vote_date": "2026-09-24",
        "given_review": True,
        "party": "BJP"
    },
    {
        "name": "Ritu Saxena",
        "age": 30,
        "state": "UK",
        "vote_date": "2026-09-13",
        "given_review": False
    },
    {
        "name": "Varun Choudhary",
        "age": 44,
        "state": "JH",
        "vote_date": "2026-09-20",
        "given_review": True,
        "party": "JDU"
    },
    {
        "name": "Tanya Bose",
        "age": 18,
        "state": "TR",
        "vote_date": "2026-09-30",
        "given_review": False
    },
    {
        "name": "Ashok Pillai",
        "age": 81,
        "state": "GA",
        "vote_date": "2026-09-17",
        "given_review": True,
        "party": "BJP"
    }
]


# This is done, in this program
# Total % voting done statewise
# For every state, % of voting done in: Youngsters (< 25) compared with Others
# For every state, % of voting done in: Mid Age people (25+ to 55) compared with Others
# For every state, % of voting done in: Senior people (> 55) compared with Others


# Assignments
# Statewise which class of age group has given the more votes
#   In MH, yougsters are leading, they have voted 25% compared to others
#   In DL, middleage are leading, they have voted 55% compared to others
#   ETC.
# Polling results - Try this for assignment
# Statewise parties pcntg for after poll (as per given_review)
# Who is winning in specific state? By what percentage.
#   - input state (ex: MH)
#   - check if given_review is True
#   - compute all the counts for diff parties - BJP, Congress, JDU (it could be 0 as well)
#   - BJP %, JDU %


"""
Step 1. Total % voting done statewise
We need to compute below data
state - count of recs
MH - 42
DL - 19

PCNTG calc:
MH - 42 / Total voiting done * 100
"""
def get_voting_pcntg_statewise():
    state_wise_counts = {}
    for r in data:
        if r['state'] not in state_wise_counts:
            state_wise_counts[r['state']] = 0
        
        state_wise_counts[r['state']] += 1
    return state_wise_counts

# print(get_voting_pcntg_statewise())

def calculate_voting_pcntg():
    total_voting_counts = len(data)
    state_wise_counts = get_voting_pcntg_statewise()
    voting_pcntg_statewise = {}
    for k, v in state_wise_counts.items():
        voting_pcntg_statewise[k] = (v / total_voting_counts) * 100
    
    return voting_pcntg_statewise

# print(calculate_voting_pcntg())

"""
Step 2. Identify the percentage of voting done by specific age group

0-25 6
26-55 26
56-100 4

For Percent cal
0-25 6/Total voiting done * 100
26-55 26/Total voiting done * 100
56-100 4/Total voiting done * 100
"""
def get_voting_count_done_by_specific_age_group_class(age_group_name, from_age, to_age):
    age_group_specific_count = {age_group_name: 0}
    for r in data:
        if (r["age"] >= from_age) and (r["age"] <= to_age):
            age_group_specific_count[age_group_name] += 1

    return age_group_specific_count


print(get_voting_count_done_by_specific_age_group_class("youngsters", 0, 25))
print(get_voting_count_done_by_specific_age_group_class("midage", 26, 55))
print(get_voting_count_done_by_specific_age_group_class("seniors", 56, 100))

def get_voting_pcntg_done_by_different_class():
    pcnt_voting_by_age_class = {}
    pcnt_voting_by_age_class.update(get_voting_count_done_by_specific_age_group_class("youngsters", 0, 25))
    pcnt_voting_by_age_class.update(get_voting_count_done_by_specific_age_group_class("midage", 26, 55))
    pcnt_voting_by_age_class.update(get_voting_count_done_by_specific_age_group_class("seniors", 56, 100))

    total_voting_done = len(data)

    for voting_age_class in pcnt_voting_by_age_class.keys():
        voting_done_by_age_class = pcnt_voting_by_age_class[voting_age_class]
        pcnt = (voting_done_by_age_class / total_voting_done) * 100

        print(f"Voting % done by {voting_age_class} is: {pcnt}")

get_voting_pcntg_done_by_different_class()