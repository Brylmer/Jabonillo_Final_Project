class PhoneNumberCategorizer:
    def __init__(self):
        print("Welcome to the Phone Number Categorization Program!")

        self.provider_prefixes = {
            'Globe/TM Network': ['0817', '0904', '0905', '0906', '0915', '0916', '0917', '0926', '0927',
                         '0935', '0936', '0937', '0945', '0954', '0955', '0956', '0965', '0966',
                         '0967', '0975', '0976', '0977', '0978', '0979', '0995', '0996', '0997'],

            'Sun Cellular': ['0922', '0923', '0924', '0925', '0931', '0932', '0933', '0934', '0940',
                             '0941', '0942', '0943', '0944', '0973', '0974'],

            'Talk n\' Text': ['0907', '0909', '0910', '0912', '0918', '0930', '0938', '0946', '0948',
                               '0950', '0963', '0989', '0998'],

            'DITO Network': ['0895', '0896', '0897', '0898', '0991', '0992', '0993', '0994'],

            'Smart Telecommunications': ['0908', '0920', '0929', '0947', '0961', '0918', '0921', '0939', '0949',
                      '0998', '0919', '0928', '0946', '0951', '0999']
                      
        }

    def get_user_phone_number(self):
        while True:
            phone_number = input("Enter your 11-digit Philippine phone number. Any provider will work: ").strip().replace(" ", "")
            if (phone_number.startswith('0') or phone_number.startswith('9')) and len(phone_number) == 11 and phone_number.isdigit():
                return phone_number
            else:
                print("Invalid phone number. Please enter a valid 11-digit Philippine Number.")

    def categorize_person(self, phone_number):
        print("\nResult:\n")
        provider = self.get_provider(phone_number)
        if provider:
            print(f"Your phone number ({phone_number}) is categorized under {provider}.")
        else:
            print("Unable to categorize the phone number.")

    def get_provider(self, phone_number):
        for provider, prefixes in self.provider_prefixes.items():
            if phone_number[:4] in prefixes:
                return provider
        return None

    def run(self):
        while True:
            phone_number = self.get_user_phone_number()
            self.categorize_person(phone_number)

            choice = input("Do you want to check another phone number? (y/n): ").lower()
            if choice != 'y':
                print("Exiting the program. Thank you!")
                break

if __name__ == "__main__":
    categorizer = PhoneNumberCategorizer()
    categorizer.run()
