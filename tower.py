def tower_hanoi(n,source,helper,destination):
    if n==1:
        print(f"Move Disk {n} from {source} to {destination}")
        return

    tower_hanoi(n-1,source,destination,helper)
    print(f"Move Disk {n} from {source} to {destination}")
    tower_hanoi(n-1,helper,source,destination)

n=int(input("Enter the number of Disks: "))

tower_hanoi(n, 'A' , 'B', 'C')
