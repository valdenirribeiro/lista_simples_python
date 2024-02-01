current_users = ['alice', 'debora', 'elisa', 'fernanda', 'luisa']
new_users = ['ana', 'deise', 'elisa', 'fatima', 'luisa']



print('-------------------------------------------------------------------')
for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user.upper()} já está em uso, você precisa escolher outro!")
    else:
        print(f"{new_user.title()} está disponivel, você pode usa-lo se desejar!") 
print('-------------------------------------------------------------------')  

       
