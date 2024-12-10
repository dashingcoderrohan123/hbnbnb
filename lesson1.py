import os
import platform

def shutdown(option=None, delay=0):
    """
    Shutdown function to perform system operations.

    Parameters:
    - option: 'shutdown', 'restart', or 'logout'
    - delay: Time delay in seconds before performing the operation
    """
    if delay > 0:
        print(f"System will {option} in {delay} seconds...")
    else:
        print(f"System will {option} now...")
    
    if platform.system() == "Windows":
        if option == "shutdown":
            os.system(f"shutdown /s /t {delay}")
        elif option == "restart":
            os.system(f"shutdown /r /t {delay}")
        elif option == "logout":
            os.system("shutdown /l")
        else:
            print("Invalid option. Choose 'shutdown', 'restart', or 'logout'.")
    elif platform.system() == "Linux" or platform.system() == "Darwin":  
        if option == "shutdown":
            os.system(f"shutdown -h +{delay//60}")
        elif option == "restart":
            os.system(f"shutdown -r +{delay//60}")
        elif option == "logout":
            os.system("logout")
        else:
            print("Invalid option. Choose 'shutdown', 'restart', or 'logout'.")
    else:
        print("Unsupported operating system.")


shutdown("shutdown", 60)


