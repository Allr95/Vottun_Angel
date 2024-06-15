#Use this script to know if an address is owner of a NFT

import requests

# Vottun API credentials
api_key = 'YOUR_VOTTUN_API_KEY'  # Replace with your Vottun API key
base_url = 'https://api.vottun.tech'  # Base URL for Vottun API

def is_owner(contract_address, account, network,id,id_application):
    try:
        url = f"{base_url}/erc/v1/erc721/ownerOf"
        print(url)
        headers = {
            'Authorization': f'Bearer {api_key}',
            'x-application-vkn':id_application
        }
        print(f'Bearer {api_key}')
        body = {
            'contractAddress': contract_address,
            'network': network,
            'id' : id
        }

        response = requests.post(url, headers=headers, json=body)
        response_data = response.json()
        
        owner = response_data.get('owner', '').lower()
        return owner == account.lower()
    
    except Exception as e:
        print(f"Error querying owner: {str(e)}")
        return False

# Example usage
contract_address = ''  # Replace with your ERC-721 contract address
account = ''  # Replace with the account address to check
network = ''  # Replace with the network. Use an integer
id = '' # Replace with the nft id. Use an integer
id_application = '' # Replace with the id_application

if is_owner(contract_address, account, network=network,id=id,id_application=id_application):
    print(f"Account {account} is the owner of NFT ID {id}.")
else:
    print(f"Account {account} is NOT the owner of NFT ID {id}.")