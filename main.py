import argparse
import hashlib
import subprocess

def ascii():
    print("\033[38;5;196m ______    _____            ____   __    __    _____     ____    __   ___    _____   ______    \033[0m")
    print("\033[38;5;202m(_   _ \\  (_   _)          / ___) (  \\  /  )  / ___/    / ___)  () ) / __)  / ___/  (   __ \\   \033[0m")
    print("\033[38;5;208m  ) (_) )   | |           / /      \\ (__) /  ( (__     / /      ( (_/ /    ( (__     ) (__) )  \033[0m")
    print("\033[38;5;214m  \\   _/    | |          ( (        ) __ (    ) __)   ( (       ()   (      ) __)   (    __/   \033[0m")
    print("\033[38;5;220m  /  _ \\    | |   __     ( (       ( (  ) )  ( (      ( (       () /\\ \\    ( (       ) \\ \\  _  \033[0m")
    print("\033[38;5;226m _) (_) ) __| |___) )     \\ \\___    ) )( (    \\ \\___   \\ \\___   ( (  \\ \\    \\ \\___  ( ( \\ \\_)) \033[0m")
    print("\033[38;5;190m(______/  \\________/       \\____)  /_/  \\_\\    \\____\\   \\____)  ()_)  \\_\\    \\____\\  )_) \\__/  \033[0m")
    print("")
    print(" (usage : python3 main.py -t ['ip','domain','url','file'] -s [source])")

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--type", choices =['ip','domain','url','file'], help="type to analyze")
    parser.add_argument("-s","--source", help="source to analayse")
    parser.add_argument("-u","--update", action='store_true', help="update database")

    parser.set_defaults(func=help)

    args = parser.parse_args()

    update = args.update
    type_analyze = args.type
    source_file = args.source
    source_ip = args.source
    source_domain = args.source
    source_url = args.source

    if update:
        ascii()
        print("")
        print("updating...")
        print("")
        try:
            result = subprocess.run(["python", "update.py"], capture_output=True, text=True)
            print(result.stdout)
            print("update done")
        except subprocess.CalledProcessError as e:
            print(f"Error : {e}")

    if type_analyze == 'ip':
        ascii()
        print("")
        try:
            str(source_ip)
        except:
            print("Error: This is not ip")
            return
        
        print("ip to analyze :", source_ip)
        path_ip = "src/ip_bl.txt"
        result = False
        current_name = None

        with open(path_ip, 'r') as srcfile:
            for line in srcfile:
                clean_line = line.strip()

                if clean_line.startswith("$"):
                    current_name = clean_line[2:]

                elif source_ip == clean_line:
                    print(f"\033[91mHit\033[0m : {source_ip} \033[91mWarning\033[0m : {current_name}")
                    result = True

        if result == False:
            print("\033[92mNo Hit\033[0m - IP not in db")

    elif type_analyze =='domain':
        ascii()
        print("")       
        print("domain to analyze :", source_domain)
        path_ip = "src/domain_bl.txt"
        result = False
        current_name = None

        with open(path_ip, 'r') as srcfile:
            for line in srcfile:
                clean_line = line.strip()

                if clean_line.startswith("$"):
                    current_name = clean_line[2:]

                elif source_domain == clean_line:
                    print(f"\033[91mHit\033[0m : {source_domain} \033[91mWarning\033[0m : {current_name}")
                    result = True

        if result == False:
            print("\033[92mNo Hit\033[0m - Domain not in db")
    
    elif type_analyze =='url':
        ascii()
        print("")
        print("url to analyze :", source_url)
        path_ip = "src/url_bl.txt"
        result = False
        current_name = None

        with open(path_ip, 'r') as srcfile:
            for line in srcfile:
                clean_line = line.strip()

                if clean_line.startswith("$"):
                    current_name = clean_line[2:]

                elif source_url == clean_line:
                    print(f"\033[91mHit\033[0m : {source_url} \033[91mWarning\033[0m : {current_name}")
                    result = True

        if result == False:
            print("\033[92mNo Hit\033[0m - URL not in db")

    elif type_analyze =='file':
        ascii()
        print("")
        try:
            hash = hashlib.sha256(open(source_file,'rb').read()).hexdigest()
        except:
            print("\033[91mError\033[0m with file or path")
            return
        path_file = "src/hash_bl.txt"
        result = False
        current_name = None

        print(f"hash (sha256) : {hash}")
        with open(path_file, 'r') as srcfile:
            for line in srcfile:
                clean_line = line.strip()

                if clean_line.startswith("$"):
                    current_name = clean_line[2:]

                elif hash == clean_line:  
                    print(f"\033[91mHit\033[0m : {hash} \033[91mWarning\033[0m : {current_name}")
                    result = True

        if result == False:
            print("\033[92mNo Hit\033[0m - File not in db")

if __name__ == '__main__':
    main()