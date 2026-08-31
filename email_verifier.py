

import requests

# =========================
# 🎨 Terminal Colors
# =========================

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"


def verify_email(email_address, api_key):
    api_key = api_key.strip()
    email_address = email_address.strip()

    print()
    print(f"{BOLD}{CYAN}╔══════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{CYAN}║           EMAIL VERIFICATION TOOL                ║{RESET}")
    print(f"{BOLD}{CYAN}╚══════════════════════════════════════════════════╝{RESET}")

    print()
    print(f"{BLUE}{BOLD}[*] Starting email verification:{RESET}")
    print(f"    {WHITE}{email_address}{RESET}")
    print()

    url = (f"https://emailreputation.abstractapi.com/v1/"f"?api_key={api_key}&email={email_address}")

    try:
        response = requests.get(url, timeout=10)

        # =========================
        # SUCCESS RESPONSE
        # =========================

        if response.status_code == 200:
            data = response.json()

            # Extract key details
            deliverability = data.get("email_deliverability", {}).get("status")

            status_detail = data.get("email_deliverability", {}).get("status_detail")

            is_format_valid = data.get("email_deliverability", {}).get("is_format_valid")

            is_smtp_valid = data.get("email_deliverability", {}).get("is_smtp_valid")

            quality_score = data.get("email_quality", {}).get("score")

            provider = data.get("email_sender", {}).get("email_provider_name")

            is_disposable = data.get("email_quality", {}).get("is_disposable")

            # =========================
            # RESULTS
            # =========================

            print(f"{MAGENTA}{BOLD}┌──────────────────────────────────────────────────┐{RESET}")
            print(f"{MAGENTA}{BOLD}│                  RESULTS                         │{RESET}")
            print(f"{MAGENTA}{BOLD}└──────────────────────────────────────────────────┘{RESET}")

            print(f"{CYAN}[+] Deliverability :{RESET} "f"{GREEN}{deliverability}{RESET} "f"{YELLOW}({status_detail}){RESET}")

            print(f"{CYAN}[+] Format Valid   :{RESET} "f"{GREEN}{is_format_valid}{RESET}")

            print(f"{CYAN}[+] SMTP Valid     :{RESET} "f"{GREEN}{is_smtp_valid}{RESET}")

            print(f"{CYAN}[+] Provider       :{RESET} "f"{WHITE}{provider}{RESET}")

            print(f"{CYAN}[+] Quality Score  :{RESET} "f"{YELLOW}{quality_score}{RESET}")

            print(f"{CYAN}[+] Disposable     :{RESET} "f"{YELLOW}{is_disposable}{RESET}")

            print(f"{BLUE}{'─' * 50}{RESET}")

            # =========================
            # FINAL VERDICT
            # =========================

            if deliverability == "deliverable":

                print(f"{GREEN}{BOLD}"f"[✓] SUCCESS: The email address is REAL and ACTIVE!"f"{RESET}")

                return True

            else:

                print(f"{RED}{BOLD}"f"[✗] FAILED: Email status is {deliverability}"f"{RESET}")

                return False

        # =========================
        # INVALID API KEY
        # =========================

        elif response.status_code == 401:

            print(f"{RED}{BOLD}""[✗] ERROR: Invalid API Key."f"{RESET}")

            print(f"{YELLOW}    Please check your API credentials.{RESET}")

            return False

        # =========================
        # OTHER HTTP ERRORS
        # =========================

        else:

            print(f"{RED}{BOLD}"f"[✗] ERROR: HTTP Status Code: {response.status_code}"f"{RESET}")

            return False

    # =========================
    # CONNECTION ERROR
    # =========================

    except requests.exceptions.RequestException as e:

        print(f"{RED}{BOLD}"f"[✗] ERROR: Connection error occurred."f"{RESET}")

        print(f"{YELLOW}    {e}{RESET}")

        return False


# =========================
# MAIN
# =========================

if __name__ == "__main__":

    API_KEY = "90c270e732e940efbec4d03ca2441989"

    print()
    print(f"{BOLD}{CYAN}[*] Email Verification{RESET}")
    print()

    target_email = input(f"{YELLOW}{BOLD}[?] Enter the email address to verify: {RESET}").strip()

    if target_email:

        verify_email(target_email, API_KEY)

    else:

        print(f"{RED}{BOLD}""[!] No email address provided. Exiting..."f"{RESET}")

