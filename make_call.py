from twilio.rest import Client

contacts = {
    "mummy": "++918937032574",  
    "mama": "+919997982099" ,
    "papa":"+917906652130" 
    # Add more contacts as needed
}

def make_call(contact_name):
    if contact_name in contacts:
        account_sid = 'AC3c8d5381a0f392ddfb1f69e85c47bb9c'  # Replace with your Twilio account SID
        auth_token = '2d61c2ccdf7dc76d3d7f15f7bdff5d16'  # Replace with your Twilio auth token
        caller_number = '+12015003205'  # Replace with your Twilio phone number

        client = Client(account_sid, auth_token)

        call = client.calls.create(
            twiml=f'<Response><Say>Calling {contact_name}</Say></Response>',
            from_=caller_number,
            to=contacts[contact_name]
        )
        print(f"Call to {contact_name} initiated:", call.sid)
    else:
        print(f"Contact '{contact_name}' not found.")