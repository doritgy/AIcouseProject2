import bank_exc_with_tests
import pytest

def main():
    while True:
        bank_exc_with_tests.display_menu()
        choice = bank_exc_with_tests.get_menu_choice()
        success:bool = bank_exc_with_tests.check_choice(choice)
        if choice == 4:
            print("bye bye, thank you for using bank application")
            break
        if success:
            bank_exc_with_tests.handle_menu(choice, None)
        else:
            continue

        if choice == 3:
            bank_exc_with_tests.display_menu_reports()
            choose = bank_exc_with_tests.get_menu_choose()
            if choice == 10:
                print("back to main menu")
                continue
            success = bank_exc_with_tests.check_choose(choose)
            if success:
                bank_exc_with_tests.handle_menu(None, choose)



if __name__ == "__main__":
    main()