import requests,json,random

def credentials():
    lis=[chr(i) for i in range(65,65+26)]
    api_key=""
    url=input("Enter the url which needs to be shortened ...  ")
    ch=input("Do you want to enter custom alias ? (yes/y/no/n)...   ").lower()
    if ch=="yes" or ch=="y":
        custom_alias=input("Enter any alias...  ")
    else:
        random.shuffle(lis)
        custom_alias=''.join(lis)[0:9]

    return main(api_key,url,custom_alias)
    
def main(api_key,url,custom_alias):
    requ=f'https://cutt.ly/api/api.php?key={api_key}&short={url}&name={custom_alias}'
    response=requests.get(requ).json()['url']

    if response['status']==7:
        print(f"This is the short link {response['shortLink']}")

    elif response['status']==6:
        print("The link provided is from a blocked domain")

    elif response['status']==5:
        print("the link has not passed the validation. Includes invalid characters")

    elif response['status']==4:
        print(" Invalid API key")

    elif response['status']==3:
        print("the preferred link name is already taken. Change the custom_name and try agian")

    elif response['status']==2:
        print('the entered link is not a link.')

    else:
        print('the shortened link comes from the domain that shortens the link, i.e. the link has already been shortened.')
    again=input("Do you want to try again? (yes/y/no/n) ").lower()
    if again=="y" or again=="y":
        credentials()

#cont=int(input("Do you want to continue again ? "))
if __name__ == "__main__":
    credentials()

