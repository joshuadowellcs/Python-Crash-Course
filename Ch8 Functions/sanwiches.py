def sandwich_order(*sandwiches):

    
    for sandwich in sandwiches:
        print((f"\nYour {sandwich} sandwich is being made. Thanks for your order."))


sandwich_order('hook and ladder')

sandwich_order('Northender', 'Turkey', 'Ham', 'Peanut Butter')

sandwich_order('BLT', 'Veggie')
