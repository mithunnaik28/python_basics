clube={
    "murdeshwar":2,
    "shirali":3,
    "bailur":2,
    "bhatkal":12
}

print(clube)

clube["balse"]=2

clube["bailur"]=1

del clube["murdeshwar"]

print(clube)

# {'murdeshwar': 2, 'shirali': 3, 'bailur': 2, 'bhatkal': 12}
# {'shirali': 3, 'bailur': 1, 'bhatkal': 12, 'balse': 2}
