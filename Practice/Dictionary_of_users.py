
user_scores = {
    "Alice": 95,
    "Bob": 88,
    "Charlie": 92
}


user_scores["Diana"] = 99


top_user = max(user_scores, key=user_scores.get)

print("All scores:", user_scores)
print("Top user:", top_user, "with score", user_scores[top_user])
