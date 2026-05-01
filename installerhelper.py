import subprocess
print("choose p, a or q")
print("p is pacman")
print("a is AUR")
print("q is quit")

choicing = input("p or a or q: ")

if choicing == "p":
    appc= input("app name in pacman:")
    subprocess.run(["sudo", "pacman", "-S", appc])
elif choicing == "a":
    app = input("app name on aur:")
    print(f"App: {app}")
    subprocess.run(["yay", "-S", app])
    
elif choicing == "q":
    quit()

else:
    print("invalid")
