def verifica_alfanumerico(username):
    return username.isalnum()

username1 = "user123"
username2 = "user123!"

print(verifica_alfanumerico(username1))  
print(verifica_alfanumerico(username2))  
